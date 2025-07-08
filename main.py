# main.py - v2.1 Event-Driven & Conversational
import os
import json
import requests
import aiohttp
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Dict, Any

# --- FastAPI App Setup ---
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"],
)
app.mount("/output", StaticFiles(directory=os.path.expanduser("~/ComfyUI/output")), name="output")

# --- Configuration ---
COMFYUI_API_URL = "http://127.0.0.1:8188"
OLLAMA_API_URL = "http://127.0.0.1:11434/api/generate"

# --- Pydantic Models for API validation ---
class PromptRequest(BaseModel):
    message: str
    history: List[Dict[str, str]] = []

class Plan(BaseModel):
    department: str
    task: str
    style: str = "general_pixel_art" # Add style to plan

class ExecutionRequest(BaseModel):
    plan: List[Plan]

# --- Agent Prompts ---
AGENT_PROMPTS = {
    "PM": """
Role: Conversational Project Manager for a game development studio.
Responsible for reading conversation history, interpreting the user's latest message, and formulating actionable, department-specific plans for approval.

Inputs:
- "conversation_history": Chronological array of prior user and system messages.
- "user_message": The latest input from the user.

Output (STRICT, JSON ONLY):
Respond with a single JSON object using the schema:
{
  "response_to_user": "string (Your conversational reply, including the full plan you are proposing)",
  "action_type": "propose_delegation" | "clarify" | "respond",
  "plan": [ { "department": "string", "task": "string", "style": "string" }, ... ]
}

Core Directives:
1.  Maintain context by reviewing "conversation_history".
2.  If the user gives a new task, formulate a plan and set "action_type" to "propose_delegation". Your "response_to_user" MUST clearly state the plan you are proposing and ask for approval.
3.  For Art tasks, you must determine the style ('isometric' or 'general_pixel_art') and include it in the plan.
4.  If the request is ambiguous, set "action_type" to "clarify" and ask a question. `plan` must be an empty array.
5.  If the request is a simple question or comment, set "action_type" to "respond" and answer it. `plan` must be an empty array.
6.  Output ONLY the JSON object.

CONVERSATION HISTORY:
{{conversation_history}}

USER'S LATEST MESSAGE:
{{user_message}}
""",
    "Art": """
Role: Art Department specialist for a game development studio.
Responsible for transforming a task into a concise, high-quality prompt for ComfyUI.

Inputs:
- "task": A single string task from the project manager.

Output (STRICT, JSON ONLY):
Return a single JSON object with two keys: "final_prompt" and "negative_prompt".

Core Directives:
1.  Elaborate on the task with rich, descriptive keywords. For a sprite sheet, describe multiple poses.
2.  Enforce GBC style: MUST include `pixel art, 16-bit, vibrant GBC color palette, masterpiece`.
3.  Use prompt weighting for complex scenes, e.g., `(Phillie Phanatic:1.3)`.
4.  The positive prompt must be under 75 tokens.
5.  Generate a comprehensive negative prompt including `photograph, realistic, 3d, noisy, blurry, watermark, text`.
6.  Output ONLY the required JSON object.

TASK:
{{task}}
"""
}

# --- Helper Functions ---
def call_ollama_agent(agent_name: str, prompt_data: dict) -> dict:
    prompt_template = AGENT_PROMPTS[agent_name]
    if agent_name == "PM":
        history_str = "\n".join([f"{msg['sender']}: {msg['content']}" for msg in prompt_data.get("history", [])])
        full_prompt = prompt_template.replace("{{conversation_history}}", history_str).replace("{{user_message}}", prompt_data["message"])
    else: # For Art agent
        full_prompt = prompt_template.replace("{{task}}", prompt_data["message"])

    payload = {"model": "llama3", "prompt": full_prompt, "format": "json", "stream": False}
    try:
        response = requests.post(OLLAMA_API_URL, json=payload, timeout=60)
        response.raise_for_status()
        response_text = response.json().get("response", "")
        start_index = response_text.find('{')
        end_index = response_text.rfind('}') + 1
        if start_index != -1 and end_index != 0:
            return json.loads(response_text[start_index:end_index])
    except Exception as e:
        return {"error": str(e)}

def load_workflow(filepath):
    try:
        with open(filepath, 'r') as f: return json.load(f)
    except Exception: return None

def inject_prompts_into_workflow(workflow, positive_prompt, negative_prompt):
    try:
        workflow['6']['inputs']['text'] = positive_prompt
        workflow['7']['inputs']['text'] = negative_prompt
        return workflow
    except KeyError: return None

# --- API Endpoints ---
@app.post("/api/v1/prompt")
async def handle_prompt(request: PromptRequest):
    """Receives a prompt and history, consults the PM, and returns the PM's plan."""
    try:
        pm_response = call_ollama_agent("PM", request.dict())
        return JSONResponse(content=pm_response)
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": f"Critical error in /prompt: {str(e)}"})

@app.post("/api/v1/execute")
async def handle_execution(request: ExecutionRequest):
    """Receives an approved plan, executes the tasks, and returns the ComfyUI prompt_id."""
    results = []
    for delegation in request.plan:
        if delegation.department == "Art":
            art_agent_response = call_ollama_agent("Art", {"message": delegation.task})
            if "error" in art_agent_response:
                return JSONResponse(status_code=500, content={"error": "Art Agent failed."})

            positive_prompt = art_agent_response.get("final_prompt", "")
            negative_prompt = art_agent_response.get("negative_prompt", "")
            
            # This logic can be expanded to load different workflows based on delegation style
            workflow = load_workflow("workflow_pixel_art.json")
            if not workflow:
                return JSONResponse(status_code=500, content={"error": "Could not load workflow file."})

            workflow = inject_prompts_into_workflow(workflow, positive_prompt, negative_prompt)

            payload = {"prompt": workflow, "client_id": "gbstudio_hub"}
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.post(f"{COMFYUI_API_URL}/prompt", json=payload) as response:
                        if response.status != 200:
                            return JSONResponse(status_code=500, content={"error": f"ComfyUI rejected prompt: {await response.text()}"})
                        prompt_data = await response.json()
                        # The ONLY job of this endpoint is to return the ID of the queued job
                        return JSONResponse(content={"prompt_id": prompt_data.get("prompt_id")})
            except Exception as e:
                return JSONResponse(status_code=500, content={"error": f"Failed to queue prompt with ComfyUI: {str(e)}"})
    
    return JSONResponse(status_code=400, content={"error": "No executable tasks found in the plan."})

# Serve the main HTML file
@app.get("/", response_class=HTMLResponse)
async def read_root():
    with open("index.html") as f: return HTMLResponse(content=f.read(), status_code=200)

