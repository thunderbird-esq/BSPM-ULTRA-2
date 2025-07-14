# Implementation Plan: GB Studio Asset Generation Hub

This document outlines the step-by-step plan to enhance and expand the GB Studio Asset Generation Hub. The project's current state is a functional proof-of-concept. This plan will guide its evolution into a robust, feature-rich, and user-friendly tool for game developers.

## Phase 1: Enhance Core Functionality & Stability

This phase focuses on strengthening the project's foundation, making it more reliable and easier to maintain.

### Step 1.1: Advanced Error Handling & Logging

**Goal:** To provide clearer insights into the application's state and handle errors gracefully.

**Actions:**
1.  **Integrate Structured Logging:** Replace `print()` statements in `scripts/main.py` with a proper logging library (e.g., `logging`). This will allow for different log levels (INFO, WARNING, ERROR) and provide more context for debugging.
2.  **Implement Granular Error Responses:** The API will return more specific error messages instead of generic "500 Internal Server Error" responses.

**Example (`scripts/main.py`):**
```python
# Before
# ...
# except Exception as e:
#     return JSONResponse(status_code=500, content={"error": f"A critical error occurred: {str(e)}"})

# After
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# ...
except aiohttp.ClientConnectorError as e:
    logging.error(f"ComfyUI Connection Error: {e}")
    return JSONResponse(status_code=502, content={"error": "Could not connect to the ComfyUI service."})
except Exception as e:
    logging.error(f"An unhandled error occurred: {e}", exc_info=True)
    return JSONResponse(status_code=500, content={"error": "An internal server error occurred."})
```

### Step 1.2: Configuration Management

**Goal:** To separate configuration from code, making the application easier to configure and deploy.

**Actions:**
1.  Create a `config.py` file or use environment variables (`.env`) to store settings like API URLs, file paths, and model names.
2.  Refactor `scripts/main.py` to import these settings instead of using hardcoded constants.

**Example (`scripts/config.py`):**
```python
# scripts/config.py
import os

COMFYUI_API_URL = os.getenv("COMFYUI_API_URL", "http://127.0.0.1:8188")
OLLAMA_API_URL = os.getenv("OLLAMA_API_URL", "http://127.0.0.1:11434/api/generate")
LLM_MODEL = os.getenv("LLM_MODEL", "llama3")
```
**Example (`scripts/main.py`):**
```python
# scripts/main.py
# from . import config # (if using a package structure)
# ...
# payload = {"model": config.LLM_MODEL, "prompt": full_prompt, ...}
# response = requests.post(config.OLLAMA_API_URL, json=payload, timeout=60)
```

## Phase 2: Expand Creative Capabilities

This phase focuses on increasing the variety and quality of assets the tool can generate.

### Step 2.1: Multi-Asset Type Support

**Goal:** To extend the generation pipeline to create backgrounds and other assets, not just sprites.

**Actions:**
1.  **Create New ComfyUI Workflows:** Design and save new workflow JSON files tailored for different asset types (e.g., `workflow_background.json`, `workflow_tilemap.json`).
2.  **Update the "PM" Agent:** Enhance the Project Manager agent to identify the requested asset type and include it in the plan.

**Example (`scripts/main.py` - PM Prompt):**
```python
# AGENT_PROMPTS["PM"]
# ...
# "plan": [ { "department": "Art", "task": "...", "asset_type": "sprite_sheet" | "background" | "tilemap" } ]
```

### Step 2.2: Dynamic Workflow Selection

**Goal:** To enable the application to use the correct ComfyUI workflow based on the PM's plan.

**Actions:**
1.  Modify the `/api/v1/execute` endpoint to load the appropriate workflow file based on the `asset_type` field in the plan.

**Example (`scripts/main.py`):**
```python
# in handle_execution function
# ...
asset_type = delegation.get("asset_type", "sprite_sheet") # Default to sprite sheet
workflow_filename = f"workflow_{asset_type}.json"
workflow_path = os.path.join(ROOT_DIRECTORY, workflow_filename)
workflow = load_workflow(workflow_path)

if not workflow:
    return JSONResponse(status_code=404, content={"error": f"Workflow '{workflow_filename}' not found."})
# ...
```

## Phase 3: Improve User Experience & Workflow

This phase focuses on making the tool more interactive and seamlessly integrated with the developer's workflow.

### Step 3.1: Frontend UI Overhaul

**Goal:** To create a more intuitive and responsive web interface for interacting with the agents.

**Actions:**
1.  Replace the current `index.html` with a modern JavaScript frontend (e.g., using Vue.js, React, or Svelte).
2.  The new UI will feature a proper chat interface, display the PM's proposed plans clearly, and show generated images directly on the page.

### Step 3.2: Direct Asset Integration

**Goal:** To automatically place generated assets into the correct GB Studio project folders.

**Actions:**
1.  After an image is successfully generated, add a step to move it from the temporary output directory to the appropriate subfolder in `project_files/assets/`.
2.  The destination will be determined by the `asset_type` from the plan (e.g., `backgrounds`, `sprites`).

**Example (Conceptual Code):**
```python
# After image is generated in handle_execution
# ...
image_filename = comfy_result.get("filename")
asset_type = delegation.get("asset_type") # e.g., "sprites"
source_path = os.path.join(COMFYUI_OUTPUT_DIRECTORY, image_filename)
destination_path = os.path.join(ROOT_DIRECTORY, "project_files", "assets", asset_type, image_filename)

# Add logic to create the directory if it doesn't exist
os.makedirs(os.path.dirname(destination_path), exist_ok=True)
os.rename(source_path, destination_path)
```
This concludes the initial implementation plan. Each phase builds upon the last, progressively transforming the project into a powerful and indispensable tool for GBC game development.
