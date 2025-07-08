# main.py
import os
import json
import requests
import asyncio
import aiohttp
from fastapi import FastAPI, Request, WebSocket
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles

# --- Configuration ---
OLLAMA_API_URL = "http://127.0.0.1:11434/api/generate"
COMFYUI_API_URL = "http://127.0.0.1:8188/prompt"

# --- Agent Prompts (The "Source of Truth") ---
AGENT_PROMPTS = {
    "PM": """You are the Project Manager for a game being made for the Game Boy Color. Your role is to be the sole interface between the Studio Director (the user) and the development departments.

CORE DIRECTIVES:
1. Analyze User Requests: Read the user's request. Identify the core intent and the departments needed.
2. Deconstruct & Delegate: Break down the request into specific, actionable, single-task instructions. For art, you MUST specify a style ('isometric' or 'general_pixel_art').
3. Enforce GBC Compliance: You are the first line of defense.
4. Communicate Clearly: Summarize department outputs for the user. Provide your own brief analysis.
5. OUTPUT FORMAT (STRICT): Always respond with a single JSON object. Do not add any text outside this object.

EXAMPLE OUTPUT:
{
  "summary_for_user": "I've received your request for a knight character. I'm tasking the Art Department to create a high-quality pixel art sprite.",
  "delegations": [
    {
      "department": "Art",
      "style": "general_pixel_art",
      "task": "Create a sprite for a brave female knight with a futuristic visor."
    }
  ]
}
""",
"Art": """You are an expert pixel artist and a master of AI image generation. Your job is to convert a simple user request into a masterpiece-level, highly-detailed prompt for ComfyUI, while adhering to the Game Boy Color aesthetic.

CORE DIRECTIVES:
1.  **Elaborate Dramatically:** Take the user's simple task and expand it with rich, descriptive keywords. Add details about lighting (e.g., 'cinematic lighting', 'rim lighting', 'god rays'), composition ('centered', 'rule of thirds'), character details ('wearing detailed futuristic armor', 'expressive eyes'), and mood ('epic', 'serene', 'ominous').
2.  **Enforce the GBC Style:** Your prompt **must** include the following keywords to maintain the aesthetic: `pixel art, 16-bit, detailed pixel art, vibrant color palette, masterpiece, best quality`.
3.  **Generate a Negative Prompt:** Create a detailed negative prompt to prevent common issues. It **must** include: `photograph, realistic, 3d, noisy, blurry, watermark, text, signature, low quality, ugly`.
4.  **OUTPUT FORMAT (STRICT):** Respond with a single JSON object containing two keys: "final_prompt" and "negative_prompt".

**EXAMPLE INPUT TASK:** "Create a sprite for a brave female knight with a futuristic visor."

**EXAMPLE OUTPUT:**
{
  "final_prompt": "masterpiece, best quality, game asset, full body sprite of a brave female knight, dynamic standing pose, wearing detailed futuristic plate armor with glowing blue accents, reflective helmet with a holographic visor, holding a large plasma rifle, cinematic lighting, rim lighting, pixel art, 16-bit, detailed pixel art, vibrant color palette",
  "negative_prompt": "photograph, realistic, 3d, noisy, blurry, watermark, text, signature, low quality, ugly, deformed, mutated"
}
"""
}

# --- FastAPI Application Setup ---
app = FastAPI()
app.mount("/output", StaticFiles(directory=os.path.expanduser("~/ComfyUI/output")), name="output")

# --- API Endpoints ---
@app.post("/api/v1/prompt")
async def handle_prompt(request: Request):
    data = await request.json()
    user_message = data.get("message")

    # 1. Call PM Agent
    pm_response_json = call_ollama_agent("PM", user_message)
    if "error" in pm_response_json:
        return JSONResponse(status_code=500, content=pm_response_json)

    summary_for_user = pm_response_json.get("summary_for_user", "The PM is processing the request.")
    delegations = pm_response_json.get("delegations", [])

    aggregated_results = []

    # 2. Execute Delegations
    for delegation in delegations:
        dept = delegation.get("department")
        task = delegation.get("task")
        style = delegation.get("style")

        if dept == "Art":
            art_prompt_json = call_ollama_agent("Art", task)
            if "error" in art_prompt_json:
                aggregated_results.append({"department": "Art", "status": "error", "response": art_prompt_json})
                continue

            final_art_prompt = art_prompt_json.get("final_prompt", task)
            negative_prompt = art_prompt_json.get("negative_prompt", "text, watermark, blurry")

            comfy_response = await call_comfyui(final_art_prompt, negative_prompt, style) # Use await here
            aggregated_results.append({"department": "Art", "status": "success", "response": comfy_response})

    return JSONResponse(content={
        "summary_for_user": summary_for_user,
        "aggregated_results": aggregated_results
    })

# --- Helper Functions ---
def call_ollama_agent(agent_name: str, prompt: str) -> dict:
    """Calls the local Ollama API with a specific agent's system prompt."""
    full_prompt = f"{AGENT_PROMPTS[agent_name]}\n\nUSER TASK: {prompt}"
    
    payload = {
        "model": "phi3",
        "prompt": full_prompt,
        "format": "json",
        "stream": False
    }
    try:
        response = requests.post(OLLAMA_API_URL, json=payload, timeout=120)
        response.raise_for_status()
        response_json_str = response.json().get("response", "{}")
        return json.loads(response_json_str)
    except (requests.exceptions.RequestException, json.JSONDecodeError) as e:
        print(f"Error calling {agent_name} agent: {e}")
        return {"error": str(e)}

async def call_comfyui(prompt: str, negative_prompt: str, style: str) -> dict:
    """Constructs and sends a workflow to ComfyUI, then waits for the result."""

    # Determine checkpoint and LoRA based on style
    if style == "isometric":
        checkpoint = "isopixel-1024_step_5000.ckpt"
        lora = "None"
        final_prompt = f"isopixel, {prompt}"
    else: # general_pixel_art
        checkpoint = "sd_xl_base_1.0.safetensors"
        lora = "pixelart.safetensors"
        final_prompt = f"pixelart, 8bit, {prompt}"

    # Simplified workflow definition
    workflow = {
        "4": {"class_type": "CheckpointLoaderSimple", "inputs": {"ckpt_name": checkpoint}},
        "5": {"class_type": "EmptyLatentImage", "inputs": {"width": 768, "height": 768, "batch_size": 1}},
        "6": {"class_type": "CLIPTextEncode", "inputs": {"text": final_prompt}},
        "7": {"class_type": "CLIPTextEncode", "inputs": {"text": negative_prompt}},
        "3": {"class_type": "KSampler", "inputs": {"seed": 12345, "steps": 25, "cfg": 7, "sampler_name": "euler", "scheduler": "normal", "denoise": 1.0, "positive": ["6", 0], "negative": ["7", 0], "latent_image": ["5", 0]}},
        "8": {"class_type": "VAEDecode", "inputs": {}},
        "9": {"class_type": "SaveImage", "inputs": {"filename_prefix": "gbstudio_hub_art", "images": ["8", 0]}}
    }

    # Dynamically wire up the workflow
    if style == "general_pixel_art" and lora != "None":
        workflow["10"] = {"class_type": "LoraLoader", "inputs": {"lora_name": lora, "strength_model": 1.0, "strength_clip": 1.0, "model": ["4", 0], "clip": ["4", 1]}}
        workflow["6"]["inputs"]["clip"] = ["10", 1]
        workflow["7"]["inputs"]["clip"] = ["10", 1]
        workflow["3"]["inputs"]["model"] = ["10", 0]
        workflow["8"]["inputs"]["vae"] = ["4", 2]
    else:
        workflow["6"]["inputs"]["clip"] = ["4", 1]
        workflow["7"]["inputs"]["clip"] = ["4", 1]
        workflow["3"]["inputs"]["model"] = ["4", 0]
        workflow["8"]["inputs"]["vae"] = ["4", 2]

    # Prepare and send the initial request
    payload = {"prompt": workflow}
    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(COMFYUI_API_URL, json=payload) as response:
                if response.status != 200:
                    return {"status": "error", "message": f"ComfyUI rejected the prompt: {await response.text()}"}
                prompt_data = await response.json()
                prompt_id = prompt_data.get('prompt_id')

            # WebSocket connection to get the final image filename
            ws_url = f"ws://{COMFYUI_API_URL.split('//')[1].split('/')[0]}/ws?clientId={prompt_id}"
            async with session.ws_connect(ws_url) as ws:
                async for msg in ws:
                    if msg.type == aiohttp.WSMsgType.TEXT:
                        data = msg.json()
                        if data['type'] == 'executed' and data['data']['node'] == '9': # Node 9 is our SaveImage node
                            filename = data['data']['output']['images'][0]['filename']
                            image_url = f"/output/{filename}"
                            return {"status": "success", "message": "Image generated successfully!", "image_url": image_url}
    except Exception as e:
        print(f"Error communicating with ComfyUI: {e}")
        return {"status": "error", "message": str(e)}

    return {"status": "error", "message": "Did not receive image data from ComfyUI."}

# Serve the main HTML file
@app.get("/", response_class=HTMLResponse)
async def read_root():
    with open("index.html") as f:
        return HTMLResponse(content=f.read(), status_code=200)