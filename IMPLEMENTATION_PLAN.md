# Implementation Plan: GB Studio Automation Hub

This document outlines the future development phases for the GB Studio Automation Hub. With the core pipeline now stable and functional, we can focus on expanding capabilities, improving workflow efficiency, and adding advanced features.

---

### Phase 1: Hardening and Quality of Life Improvements

This phase is focused on making the existing system more robust, user-friendly, and easier to maintain.

*   **1.1. Complete the Asset Pipeline:**
    *   **Action:** Implement the file-moving logic in the `approve_asset` endpoint. When an asset is approved, its file will be moved from the temporary `ComfyUI/output` directory to the appropriate subdirectory within `project_files/assets` (e.g., `sprites`, `backgrounds`). This completes the end-to-end automation for the art department.

*   **1.2. Enhance the UI:**
    *   **Action:** Display the full conversation history for each asset, allowing the user to see the initial prompt and all subsequent revision feedback.
    *   **Action:** Implement version tracking in the UI. When an asset is revised, allow the user to view and compare previous versions.
    *   **Action:** Add more descriptive loading states and clearer error messages to give the user better insight into the system's status.

*   **1.3. Externalize Configuration:**
    *   **Action:** Move hardcoded values from `scripts/main.py` (like agent prompts, model names, and file paths) into a dedicated `config.py` or `config.json` file. This will make the system easier to configure and modify without changing the core application logic.

---

### Phase 2: Expanding Creative Capabilities

This phase focuses on transforming the tool into a true multi-disciplinary game development assistant.

*   **2.1. Onboard New Departments:**
    *   **Action: Audio Department:**
        *   Integrate a text-to-audio model (e.g., `audiocraft`).
        *   Create a new "Audio Specialist" agent responsible for translating high-level requests ("an upbeat battle theme") into detailed prompts for the audio model.
        *   Update the PM agent to recognize and delegate audio-related tasks.
    *   **Action: Writing Department:**
        *   Implement a "Writer" agent that uses a standard LLM call to generate game content like character dialogue, item descriptions, or location lore based on user requests.

*   **2.2. Expand Art Department Capabilities:**
    *   **Action:** Add support for new asset types like **backgrounds**, **tilemaps**, and **UI elements**.
    *   **Action:** This will involve creating new, specialized "base prompts" and potentially new ComfyUI workflow files (`workflow_background.json`, etc.) tailored for each asset type. The PM agent will be updated to recognize these new task types and delegate them accordingly.

---

### Phase 3: Advanced Features & True Automation

This phase focuses on the ultimate goal: seamless, end-to-end integration with GB Studio.

*   **3.1. Automated Post-Processing:**
    *   **Action:** Create a `post_processor.py` script that uses the `Pillow` library.
    *   **Action:** After an image is generated, automatically trigger this script to perform critical GBC compliance tasks, such as:
        *   Quantizing the image's colors to the precise 56-color GBC palette.
        *   Resizing the image to ensure its dimensions are multiples of 8.
        *   (Optional) Slicing a generated sprite sheet into individual frames for easier import.

*   **3.2. Direct GB Studio Project Integration:**
    *   **Action:** Research the `.gbsproj` file format, which is a structured text file (JSON).
    *   **Action:** Create a utility that can programmatically modify the `.gbsproj` file.
    *   **Action:** When an asset is approved, the system will not only move the file but also automatically add the asset's metadata to the `.gbsproj` file. This will make the new asset appear directly within the GB Studio editor upon next launch, completely eliminating the need for manual importing. This represents the final step in achieving a truly automated workflow.
