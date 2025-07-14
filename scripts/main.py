# scripts/main.py
import os
import json
import asyncio
import aiohttp
import requests
import logging
from fastapi import FastAPI, Request, WebSocket, Depends, HTTPException, BackgroundTasks
from pydantic import BaseModel
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from scripts.config import settings
from scripts.database import (
    initialize_database, log_chat_message, log_asset_creation,
    update_asset_status, get_asset, update_asset_source_path,
    get_db_connection, get_approved_assets
)
from scripts.project_integrator import move_asset, compile_gb_studio_project, launch_in_emulator

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

app.mount("/output", StaticFiles(directory=settings.comfyui_output_path), name="output")

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
    "PM": """You are a master Project Manager AI for a Game Boy game. Your primary role is to be the central hub for all development requests.
- **Analyze Requests**: Carefully analyze the user's request and the provided project history.
- **Delegate Tasks**: Based on your analysis, delegate the task to the most appropriate department: `Art`, `Writing`, `Code`, `QA`, or `Sound`.
- **Maintain Context**: Use the project history to understand the current state of the game and avoid redundant or conflicting tasks.
- **Format Response**: Your response MUST be a JSON object with two keys: `department` (the name of the target department) and `task_description` (a clear, concise, and actionable task for that department).

**Project History:**
{history}

**User Request:**""",
    "Art": """You are a visionary Art Director AI for a retro Game Boy game. You translate task descriptions into concrete, detailed prompts for an image generation model.

- **Analyze Request**: Examine the user's request to determine the asset's category.
- **Categorize Asset**: You MUST categorize the asset into one of three types: 'sprite', 'background', or 'ui'.
- **Select Workflow**: Based on the category, you MUST select the appropriate workflow file:
    - For a 'sprite', choose 'workflow_pixel_art.json'.
    - For a 'background', choose 'workflow_background.json'.
    - For a 'ui' element, choose 'workflow_ui_element.json'.
- **Generate Prompt**: Create a detailed, creative, and specific prompt for the image model, adhering to a 1-bit pixel art style suitable for the original Game Boy.
- **Format Response**: Your response MUST BE ONLY a valid JSON object. Do not include any other text, explanations, or markdown. The JSON object must contain exactly these three keys:
    1.  `"workflow"`: The string name of the selected JSON file (e.g., "workflow_pixel_art.json").
    2.  `"asset_type"`: The category you determined (e.g., "sprite").
    3.  `"prompt"`: The detailed text prompt for the image model.
""",
    "Writing": """You are a master storyteller and Writing Director AI for a Game Boy RPG. You are responsible for all in-game text.
- **Content Creation**: Generate content such as character dialogue, item descriptions, quest logs, and world-building lore.
- **Tone and Style**: Maintain a consistent tone that fits a classic fantasy RPG adventure. Keep text concise and impactful, suitable for the Game Boy's small screen.
- **Format Response**: Your response MUST be a JSON object with one key: `text_content` (the generated text).""",
    "Code": """You are a brilliant Code Director AI specializing in GBScript, the visual scripting language for GB Studio.
- **Mechanics Implementation**: Translate game design requests into logical, step-by-step pseudocode or GBScript event descriptions.
- **Clarity and Detail**: Provide enough detail for a developer to implement the logic directly in GB Studio.
- **Format Response**: Your response MUST be a JSON object with one key: `code_logic` (the detailed pseudocode or script description).""",
    "QA": """You are a meticulous QA Tester AI. Your job is to find and document potential issues.
- **Analyze and Identify**: Review game mechanics, assets, and text for bugs, inconsistencies, or gameplay balance issues.
- **Bug Reporting**: Create clear, concise, and actionable bug reports.
- **Format Response**: Your response MUST be a JSON object with one key: `issue_report` (a detailed description of the identified issue and steps to reproduce it).""",
    "Sound": """You are an innovative Music and Sound Director AI for a Game Boy game.
- **Sound Design**: Create descriptions for sound effects (SFX) and music tracks that can be created with a classic 4-channel sound chip.
- **Atmosphere and Mood**: Your descriptions should evoke a specific mood or atmosphere (e.g., 'a cheerful town theme', 'a tense battle track', 'a sound effect for opening a chest').
- **Format Response**: Your response MUST be a JSON object with one key: `sound_description` (a detailed description of the music or sound effect)."""
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
            async with session.post(settings.ollama_api_url, json=payload, timeout=300) as response:
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
        async with session.post(f"{settings.comfyui_api_url}/prompt", json=prompt_payload) as response:
            if response.status != 200:
                raise Exception(f"ComfyUI Error: {await response.text()}")
            return await response.json()

async def poll_comfyui_for_result(prompt_id: str):
    async with aiohttp.ClientSession() as session:
        start_time = asyncio.get_event_loop().time()
        while asyncio.get_event_loop().time() - start_time < 900:  # 15 minute timeout
            async with session.get(f"{settings.comfyui_api_url}/history/{prompt_id}") as response:
                if response.status == 200:
                    history = await response.json()
                    if prompt_id in history and history[prompt_id].get("outputs"):
                        outputs = history[prompt_id]["outputs"]
                        if '9' in outputs and 'images' in outputs['9']:
                            return outputs['9']['images'][0]
            await asyncio.sleep(2)
    raise Exception("Polling for ComfyUI result timed out.")

async def run_generation_task(final_prompt: str, task_name: str, asset_type: str, workflow_filename: str):
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

        workflow_path = os.path.join(os.path.dirname(settings.gb_project_path), "workflows", workflow_filename)
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

async def generate_writing_asset(prompt: str, task_name: str):
    """Saves generated text to a file and logs it to the database."""
    logging.info(f"Generating writing asset with prompt: {prompt}")
    await manager.broadcast({"event": "NEW", "name": task_name, "status": "GENERATING"})
    try:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"writing_{timestamp}.txt"
        asset_dir = os.path.join(settings.gb_project_path, "assets", "dialogue")
        os.makedirs(asset_dir, exist_ok=True)
        filepath = os.path.join(asset_dir, filename)
        with open(filepath, "w") as f:
            f.write(prompt)
        asset_id = log_asset_creation(
            task_name=task_name, asset_type='writing', final_prompt=prompt, source_path=filepath
        )
        update_asset_status(asset_id, 'approved')
        await manager.broadcast({"event": "UPDATE", "name": task_name, "status": "COMPLETED", "asset_id": asset_id})
    except Exception as e:
        logging.error(f"Failed to generate writing asset: {e}")
        await manager.broadcast({"event": "ERROR", "name": task_name, "message": str(e)})

async def generate_code_asset(prompt: str, task_name: str):
    """Saves generated code logic to a file and logs it to the database."""
    logging.info(f"Generating code asset with prompt: {prompt}")
    await manager.broadcast({"event": "NEW", "name": task_name, "status": "GENERATING"})
    try:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"code_{timestamp}.txt"
        asset_dir = os.path.join(settings.gb_project_path, "assets", "scripts")
        os.makedirs(asset_dir, exist_ok=True)
        filepath = os.path.join(asset_dir, filename)
        with open(filepath, "w") as f:
            f.write(prompt)
        asset_id = log_asset_creation(
            task_name=task_name, asset_type='code', final_prompt=prompt, source_path=filepath
        )
        update_asset_status(asset_id, 'approved')
        await manager.broadcast({"event": "UPDATE", "name": task_name, "status": "COMPLETED", "asset_id": asset_id})
    except Exception as e:
        logging.error(f"Failed to generate code asset: {e}")
        await manager.broadcast({"event": "ERROR", "name": task_name, "message": str(e)})

async def generate_sound_asset(prompt: str, task_name: str):
    """Saves generated sound description to a file and logs it to the database."""
    logging.info(f"Generating sound asset with prompt: {prompt}")
    await manager.broadcast({"event": "NEW", "name": task_name, "status": "GENERATING"})
    try:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"sound_{timestamp}.txt"
        asset_dir = os.path.join(settings.gb_project_path, "assets", "music")
        os.makedirs(asset_dir, exist_ok=True)
        filepath = os.path.join(asset_dir, filename)
        with open(filepath, "w") as f:
            f.write(prompt)
        asset_id = log_asset_creation(
            task_name=task_name, asset_type='sound', final_prompt=prompt, source_path=filepath
        )
        update_asset_status(asset_id, 'approved')
        await manager.broadcast({"event": "UPDATE", "name": task_name, "status": "COMPLETED", "asset_id": asset_id})
    except Exception as e:
        logging.error(f"Failed to generate sound asset: {e}")
        await manager.broadcast({"event": "ERROR", "name": task_name, "message": str(e)})

# --- API Endpoints ---
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            await websocket.receive_text()
    except:
        manager.disconnect(websocket)

class ChatMessage(BaseModel):
    message: str
    history: list = []

@app.post("/api/v1/chat/{agent_name}")
async def chat_with_agent(agent_name: str, chat_message: ChatMessage, background_tasks: BackgroundTasks):
    """
    Handles a chat message with a specified agent, logs the interaction,
    and can trigger different generation pipelines.
    """
    if agent_name not in CONVERSATIONAL_AGENTS:
        raise HTTPException(status_code=404, detail="Agent not found")

    # Get the initial response from the LLM
    response_data = await call_ollama_agent(agent_name, chat_message.message)

    # Log the conversation
    background_tasks.add_task(
        log_chat_message,
        user_message=chat_message.message,
        agent_response=json.dumps(response_data)
    )

    # Trigger different pipelines based on the agent
    if agent_name == "Art":
        workflow = response_data.get("workflow")
        asset_type = response_data.get("asset_type")
        prompt = response_data.get("prompt")
        if workflow and asset_type and prompt:
            task_name = chat_message.message # Use the user's message as the task name
            background_tasks.add_task(run_generation_task, prompt, task_name, asset_type, workflow)
    elif agent_name == "Writing":
        prompt = response_data.get("text_content")
        if prompt:
            task_name = chat_message.message
            background_tasks.add_task(generate_writing_asset, prompt, task_name)
    elif agent_name == "Code":
        prompt = response_data.get("code_logic")
        if prompt:
            task_name = chat_message.message
            background_tasks.add_task(generate_code_asset, prompt, task_name)
    elif agent_name == "Sound":
        prompt = response_data.get("sound_description")
        if prompt:
            task_name = chat_message.message
            background_tasks.add_task(generate_sound_asset, prompt, task_name)

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

    source_file_path = os.path.join(settings.comfyui_output_path, asset['source_path'])
    gb_project_path = settings.gb_project_path

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


from scripts.config import settings
from scripts.database import get_approved_assets
from scripts.project_integrator import move_asset, compile_gb_studio_project, launch_in_emulator

@app.post("/api/v1/integrate_and_playtest")
async def integrate_and_playtest(background_tasks: BackgroundTasks):
    """
    Integrates all 'approved' assets into the GB Studio project,
    compiles it, and launches it in an emulator.
    """
    # 1. Get all approved assets from the database
    approved_assets = get_approved_assets()
    if not approved_assets:
        return JSONResponse(
            status_code=404,
            content={"status": "error", "message": "No approved assets found to integrate."}
        )

    # 2. Move each asset to the project folder
    moved_assets = []
    moved_asset_details = []
    for asset in approved_assets:
        # Skip if source_path is missing or a placeholder
        if not asset['source_path'] or asset['source_path'] == 'placeholder':
            logging.warning(f"Skipping asset ID {asset['id']} due to missing source path.")
            continue

        source_path = os.path.join(settings.comfyui_output_path, asset['source_path'])
        success = move_asset(
            source_path=source_path,
            asset_type=asset['asset_type'],
            project_path=settings.gb_project_path
        )
        if success:
            moved_assets.append(asset['task_name'])
            moved_asset_details.append({'name': asset['task_name'], 'type': asset['asset_type']})
            # IMPORTANT: Update status to 'integrated' to prevent re-integration
            update_asset_status(asset['id'], 'integrated')
        else:
            logging.error(f"Failed to move asset: {asset['task_name']} (ID: {asset['id']})")

    if not moved_assets:
        return JSONResponse(
            status_code=500,
            content={"status": "error", "message": "Failed to move any of the approved assets."}
        )

    # 3. Compile the project
    logging.info("Starting GB Studio project compilation...")
    compile_success, rom_path = compile_gb_studio_project(
        project_path=settings.gb_project_path,
        gbs_cli_path=settings.gbs_cli_path
    )

    if not compile_success:
        logging.error("GB Studio project compilation failed.")
        return JSONResponse(
            status_code=500,
            content={"status": "error", "message": "GB Studio project compilation failed."}
        )
    logging.info(f"GB Studio project compiled successfully. ROM at: {rom_path}")

    # 4. Launch in emulator (as a background task)
    background_tasks.add_task(
        launch_in_emulator,
        rom_path=rom_path,
        emulator_path=settings.emulator_path
    )

    return {
        "status": "success",
        "message": "Integration and playtesting process initiated.",
        "moved_assets": moved_asset_details,
        "rom_path": rom_path
    }

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
    html_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "index.html")
    with open(html_path) as f:
        return HTMLResponse(content=f.read(), status_code=200)