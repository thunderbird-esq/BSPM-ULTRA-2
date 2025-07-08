# main.py - FINAL PRODUCTION BUILD v3.0
import os
import json
import requests
import asyncio
import aiohttp
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

# --- FastAPI App Setup ---
app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/output", StaticFiles(directory=os.path.expanduser("~/ComfyUI/output")), name="output")

# --- Configuration ---
COMFYUI_API_URL = "http://127.0.0.1:8188"
OLLAMA_API_URL = "http://127.0.0.1:11434/api/generate"
POSITIVE_PLACEHOLDER = "POSITIVE_PROMPT_PLACEHOLDER"
NEGATIVE_PLACEHOLDER = "NEGATIVE_PROMPT_PLACEHOLDER"

# --- Agent Prompts ---
AGENT_PROMPTS = {
    "PM": """You are the Project Manager for a game being made for the Game Boy Color. Your role is to be the sole interface between the Studio Director (the user) and the development departments.
CORE DIRECTIVES:
1. Analyze User Requests: Read the user's request. Identify the core intent and the departments needed.
2. OUTPUT FORMAT (STRICT): Your entire response must be ONLY the following JSON object and nothing else.
EXAMPLE OUTPUT:
{
  "summary_for_user": "I've received your request for a sprite sheet. I'm tasking the Art Department to create this asset.",
  "delegations": [ { "department": "Art", "task": "A full sprite sheet for the Phillie Phanatic." } ]
}
""",
"Art": """You are an expert pixel artist and a master of AI image generation. Your job is to convert a simple user request into a masterpiece-level, highly-detailed prompt for ComfyUI.
CORE DIRECTIVES:
1.  **Elaborate:** Take the user's task and expand it with rich keywords. For a sprite sheet, describe different poses (e.g., 'standing idle animation, walking cycle, attack animation').
2.  **Enforce Style:** Your prompt MUST include: `pixel art, sprite sheet, 16-bit, vibrant GBC color palette, masterpiece, clean lines, white background`.
3.  **Generate Negative Prompt:** Create a detailed negative prompt. It MUST include: `photograph, realistic, 3d, noisy, blurry, watermark, text, signature, jpeg artifacts`.
4.  **BE CONCISE:** The final positive prompt must be under 75 tokens.
5.  **OUTPUT FORMAT (STRICT):** Your entire response must be ONLY the following JSON object containing two keys: "final_prompt" and "negative_prompt".
"""
}

# --- Helper Functions ---
def load_workflow(filepath):
    try:
        with open(filepath, 'r') as f:
            return json.load(f)
    except Exception as e:
        print(f"CRITICAL ERROR: Could not load or parse workflow file at {filepath}: {e}")
        return None

def call_ollama_agent(agent_name: str, prompt: str) -> dict:
    full_prompt = f"{AGENT_PROMPTS[agent_name]}\n\nUSER TASK: {prompt}"
    payload = {"model": "llama3", "prompt": full_prompt, "format": "json", "stream": False}
    try:
        response = requests.post(OLLAMA_API_URL, json=payload, timeout=60)
        response.raise_for_status()
        response_text = response.json().get("response", "")
        start_index = response_text.find('{')
        end_index = response_text.rfind('}') + 1
        if start_index != -1 and end_index != 0:
            json_str = response_text[start_index:end_index]
            return json.loads(json_str)
        else:
            raise ValueError("No valid JSON object found in LLM response.")
    except Exception as e:
        print(f"Error calling {agent_name} agent or parsing its response: {e}")
        return {"error": str(e)}

def inject_prompts_into_workflow(workflow, positive_prompt, negative_prompt):
    try:
        workflow['6']['inputs']['text'] = positive_prompt
        workflow['7']['inputs']['text'] = negative_prompt
        return workflow
    except KeyError as e:
        print(f"--- ERROR injecting prompts: KeyError: {e}. Check workflow.json for nodes '6' and '7'.")
        return None

async def execute_comfyui_prompt(session, prompt_payload):
    """Queues a prompt and polls the history to get the output."""
    try:
        # Queue the prompt
        async with session.post(f"{COMFYUI_API_URL}/prompt", json=prompt_payload) as response:
            if response.status != 200:
                error_text = await response.text()
                print(f"Error queuing prompt with ComfyUI: {error_text}")
                return {"status": "error", "message": f"ComfyUI rejected prompt: {error_text}"}
            queue_data = await response.json()
            prompt_id = queue_data.get("prompt_id")
            print(f"--- Prompt queued successfully with ID: {prompt_id}")

        # Poll the history for the result
        start_time = asyncio.get_event_loop().time()
        while asyncio.get_event_loop().time() - start_time < 180: # 3 minute timeout
            async with session.get(f"{COMFYUI_API_URL}/history/{prompt_id}") as response:
                if response.status == 200:
                    history_data = await response.json()
                    # Check if our prompt ID is in the history
                    if prompt_id in history_data:
                        prompt_history = history_data[prompt_id]
                        outputs = prompt_history.get("outputs", {})
                        # Find the SaveImage node's output (node ID '9')
                        if "9" in outputs:
                            image_data = outputs["9"].get("images", [])
                            if image_data and "filename" in image_data[0]:
                                filename = image_data[0]["filename"]
                                print(f"--- SUCCESS: Found image filename: {filename}")
                                return {"status": "success", "message": "Image generated!", "image_url": f"/output/{filename}"}
            
            await asyncio.sleep(2) # Wait 2 seconds before polling again
        
        return {"status": "error", "message": "Image generation timed out."}

    except Exception as e:
        print(f"An error occurred during ComfyUI execution: {e}")
        return {"status": "error", "message": str(e)}

# --- Main API Endpoint ---
@app.post("/api/v1/prompt")
async def handle_prompt(request: Request):
    data = await request.json()
    user_message = data.get("message")
    
    try:
        pm_response = call_ollama_agent("PM", user_message)
        if "error" in pm_response:
            return JSONResponse(status_code=500, content={"error": f"PM Agent failed: {pm_response['error']}"})

        summary = pm_response.get("summary_for_user", "PM response was invalid.")
        delegations = pm_response.get("delegations", [])
        results = []

        for delegation in delegations:
            if delegation.get("department") == "Art":
                art_agent_response = call_ollama_agent("Art", delegation.get("task"))
                if "error" in art_agent_response:
                    results.append({"department": "Art", "response": art_agent_response})
                    continue

                positive_prompt = art_agent_response.get("final_prompt", "")
                negative_prompt = art_agent_response.get("negative_prompt", "")
                
                workflow = load_workflow("workflow_pixel_art.json")
                if not workflow:
                    return JSONResponse(status_code=500, content={"error": "Could not load workflow_pixel_art.json"})

                workflow = inject_prompts_into_workflow(workflow, positive_prompt, negative_prompt)
                if not workflow:
                     return JSONResponse(status_code=500, content={"error": "Failed to inject prompts into workflow."})

                payload = {"prompt": workflow, "client_id": "gbstudio_hub"}
                
                async with aiohttp.ClientSession() as session:
                    comfy_result = await execute_comfyui_prompt(session, payload)

                response_detail = {
                    "pm_instruction": delegation.get("task"),
                    "generated_prompt": positive_prompt,
                    **comfy_result # Merge the result from ComfyUI
                }
                results.append({"department": "Art", "response": response_detail})
        
        return JSONResponse(content={"summary_for_user": summary, "aggregated_results": results, "delegations": delegations})

    except Exception as e:
        print(f"An unexpected error occurred in handle_prompt: {e}")
        return JSONResponse(status_code=500, content={"error": f"A critical error occurred: {str(e)}"})

# Serve the main HTML file
@app.get("/", response_class=HTMLResponse)
async def read_root():
    try:
        with open("index.html") as f:
            return HTMLResponse(content=f.read(), status_code=200)
    except FileNotFoundError:
        return HTMLResponse(content="<h1>index.html not found</h1>", status_code=404)