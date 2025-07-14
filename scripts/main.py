# scripts/main.py
import os
import json
import asyncio
import aiohttp
import requests
import logging
from fastapi import FastAPI, Request, WebSocket, Depends, HTTPException, BackgroundTasks
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

# --- Configuration ---
ROOT_DIRECTORY = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
COMFYUI_API_URL = "http://comfyui:8188"
OLLAMA_API_URL = "http://ollama:11434/api/generate"
COMFYUI_OUTPUT_DIR = "/app/comfyui_output"

from scripts.database import (
    initialize_database, log_chat_message, log_asset_creation,
    update_asset_status, get_asset, update_asset_source_path,
    get_db_connection
)
from scripts.project_integrator import move_asset

# --- FastAPI App Setup ---
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.on_event("startup")
def on_startup():
    """Initialize the database when the application starts."""
    initialize_database()

app.mount("/output", StaticFiles(directory=COMFYUI_OUTPUT_DIR), name="output")

# --- WebSocket Connection Manager ---
class ConnectionManager:
    def __init__(self):
        self.active_connections: list[WebSocket] = []
    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)
    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)
    async def broadcast(self, message: dict):
        for connection in self.active_connections:
            await connection.send_json(message)
manager = ConnectionManager()

# --- Agent Prompts ---
CONVERSATIONAL_AGENTS = {
    "PM": """You are a helpful and organized Project Manager AI for a Game Boy game project.\nYour goal is to understand the user's high-level requests and delegate them as tasks to the appropriate departments.\nAnalyze the user's request and the recent project history to make informed decisions.\n\n**Recent Project History:**\n{history}\n\nBased on the user's request and the history, decide which department (Art, Writing, Code, QA, Sound) is best suited for the task.\nRespond in JSON format with the following structure:\n{\"department\": \"target_department\", \"task_description\": \"A clear and concise description of the task for that department.\"}\n""",
    "Art": "You are a creative and inspiring Art Director AI. You take tasks from the Project Manager and generate detailed, creative prompts for an image generation model to create game assets like sprites, backgrounds, and UI elements.",
    "Writing": "You are a knowledgeable and eloquent Writing Director AI. You generate game content like character dialogue, item descriptions, and world lore based on requests.",
    "Code": "You are a logical and efficient Code Director AI. You generate GBScript or pseudocode for game mechanics based on requests.",
    "QA": "You are a meticulous QA Tester AI. You analyze game mechanics and assets for potential issues, bugs, or inconsistencies.",
    "Sound": "You are a talented Music and Sound Director AI. You create descriptions for sound effects and music tracks suitable for a Game Boy game."
}

def get_conversation_history() -> str:
    """Retrieves the last 20 conversation entries from the database."""
    conn = get_db_connection()
    if conn is None:
        return "No history found."
    try:
        rows = conn.execute("""
            SELECT user_message, agent_response
            FROM conversations
            ORDER BY timestamp DESC
            LIMIT 20
        """).fetchall()
        history = "\n".join([
            f"- User: {row['user_message']}\n  - Agent Response: {row['agent_response']}"
            for row in reversed(rows)
        ])
        return history if history else "No conversation history found."
    except Exception as e:
        print(f"Error getting conversation history: {e}")
        return "Error retrieving history."
    finally:
        if conn:
            conn.close()


# --- Helper Functions ---
async def call_ollama_agent(agent_name: str, task: str) -> dict:
    """Calls the Ollama agent and returns the parsed JSON response."""
    system_prompt = CONVERSATIONAL_AGENTS[agent_name]
    if agent_name == "PM":
        history = get_conversation_history()
        system_prompt = system_prompt.replace("{history}", history)

    full_prompt = f"{system_prompt}\n\nUSER TASK: {task}"
    payload = {"model": "llama3", "prompt": full_prompt, "format": "json", "stream": False}
    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(OLLAMA_API_URL, json=payload, timeout=300) as response:
                response.raise_for_status()
                response_text = await response.text()
                ollama_payload = json.loads(response_text)
                model_response_str = ollama_payload.get("response", "{}")
                return json.loads(model_response_str)
    except Exception as e:
        print(f"Error calling agent: {e}")
        return {"error": str(e)}

async def call_comfyui(prompt_payload: dict):
    async with aiohttp.ClientSession() as session:
        async with session.post(f"{COMFYUI_API_URL}/prompt", json=prompt_payload) as response:
            if response.status != 200:
                raise Exception(f"ComfyUI Error: {await response.text()}")
            return await response.json()

async def poll_comfyui_for_result(prompt_id: str):
    async with aiohttp.ClientSession() as session:
        start_time = asyncio.get_event_loop().time()
        while asyncio.get_event_loop().time() - start_time < 900:  # 15 minute timeout
            async with session.get(f"{COMFYUI_API_URL}/history/{prompt_id}") as response:
                if response.status == 200:
                    history = await response.json()
                    if prompt_id in history and history[prompt_id].get("outputs"):
                        outputs = history[prompt_id]["outputs"]
                        if '9' in outputs and 'images' in outputs['9']:
                            return outputs['9']['images'][0]
            await asyncio.sleep(2)
    raise Exception("Polling for ComfyUI result timed out.")

async def run_generation_task(final_prompt: str, task_name: str, asset_type: str):
    """
    Runs the full asset generation pipeline: logs creation, calls ComfyUI,
    polls for results, and broadcasts updates via WebSocket.
    """
    await manager.broadcast({"event": "NEW", "name": task_name, "status": "QUEUED"})
    asset_id = -1
    try:
        source_path = "placeholder"
        asset_id = log_asset_creation(
            task_name=task_name,
            asset_type=asset_type,
            final_prompt=final_prompt,
            source_path=source_path
        )
        if asset_id == -1:
            raise Exception("Failed to log asset creation in the database.")

        await manager.broadcast({"event": "UPDATE", "name": task_name, "status": "GENERATING", "asset_id": asset_id})

        workflow_path = os.path.join(ROOT_DIRECTORY, "workflow_pixel_art.json")
        with open(workflow_path, 'r') as f:
            workflow = json.load(f)

        workflow["6"]["inputs"]["text"] = final_prompt

        comfy_response = await call_comfyui({"prompt": workflow})
        prompt_id = comfy_response.get("prompt_id")
        if not prompt_id:
            raise Exception(f"ComfyUI did not return a prompt_id. Response: {comfy_response}")

        image_result = await poll_comfyui_for_result(prompt_id)
        update_asset_source_path(asset_id, image_result['filename'])

        await manager.broadcast({
            "event": "UPDATE",
            "name": task_name,
            "status": "COMPLETED",
            "asset_id": asset_id,
            "image_url": f"/output/{image_result['filename']}"
        })
    except Exception as e:
        print(f"Generation task failed: {e}")
        await manager.broadcast({"event": "ERROR", "name": task_name, "asset_id": asset_id, "message": str(e)})

# --- API Endpoints ---
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            await websocket.receive_text()
    except:
        manager.disconnect(websocket)

from pydantic import BaseModel

class ChatMessage(BaseModel):
    message: str
    history: list = []

@app.post("/api/v1/chat/{agent_name}")
async def chat_with_agent(agent_name: str, chat_message: ChatMessage, background_tasks: BackgroundTasks):
    """
    Handles a chat message with a specified agent, logs the interaction,
    and returns the agent's response.
    """
    if agent_name not in CONVERSATIONAL_AGENTS:
        raise HTTPException(status_code=404, detail="Agent not found")

    response_data = await call_ollama_agent(agent_name, chat_message.message)

    background_tasks.add_task(
        log_chat_message,
        user_message=chat_message.message,
        agent_response=json.dumps(response_data)
    )

    return response_data

class AssetApproval(BaseModel):
    asset_id: int
    asset_type: str

@app.post("/api/v1/approve_asset")
async def approve_asset(approval: AssetApproval):
    """
    Approves an asset, moving it to the project folder and updating its status.
    """
    asset = get_asset(approval.asset_id)
    if not asset:
        raise HTTPException(status_code=404, detail="Asset not found in database.")

    if not asset['source_path'] or asset['source_path'] == 'placeholder':
        raise HTTPException(status_code=400, detail="Asset has no source path to move.")

    source_file_path = os.path.join(COMFYUI_OUTPUT_DIR, asset['source_path'])
    gb_project_path = os.path.join(ROOT_DIRECTORY, "gbstudio_project")

    success = move_asset(
        source_path=source_file_path,
        asset_type=approval.asset_type,
        project_path=gb_project_path
    )

    if not success:
        raise HTTPException(status_code=500, detail=f"Failed to move asset file from {source_file_path}.")

    if not update_asset_status(approval.asset_id, "approved"):
        raise HTTPException(status_code=500, detail="Failed to update asset status in database after moving file.")

    return {"status": "success", "message": f"Asset {approval.asset_id} approved and moved."}


@app.post("/api/v1/integrate_and_playtest")
async def integrate_and_playtest():
    return {"status": "success", "message": "Integration process initiated."}

@app.post("/api/v1/execute_generation")
async def execute_generation(request: Request, background_tasks: BackgroundTasks):
    data = await request.json()
    final_prompt = data.get("prompt")
    task_name = data.get("task_name", "Untitled Asset")
    asset_type = data.get("asset_type", "sprite")
    background_tasks.add_task(run_generation_task, final_prompt, task_name, asset_type)
    return JSONResponse(content={"message": "Generation has started."})

@app.get("/", response_class=HTMLResponse)
async def read_root():
    html_path = os.path.join(ROOT_DIRECTORY, "index.html")
    with open(html_path) as f:
        return HTMLResponse(content=f.read(), status_code=200)