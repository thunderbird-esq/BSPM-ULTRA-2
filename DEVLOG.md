# DEVLOG.md

This document tracks the development, debugging, and architectural decisions made for the GB Studio Automation Hub project.

## Initial Setup & Core Problem Identification

The initial goal was to create a system that could automate the generation of game assets. However, the initial development process was plagued by fundamental environment and dependency issues.

**Key Challenge:** The primary obstacle was the lack of a stable, reproducible development environment. Initial attempts to install dependencies globally using `pip` led to a series of cascading, difficult-to-diagnose errors.

## The Road to Stability: A Step-by-Step Breakdown

The following steps were taken to debug the system and achieve a functional state.

### 1. Implementing a Virtual Environment

-   **Problem:** Global package installation was causing conflicts and unpredictable behavior.
-   **Solution:** A Python virtual environment (`.venv`) was created to isolate project dependencies.
-   **Key Learning:** The `source .venv/bin/activate` command proved unreliable in the execution shell. The solution was to adopt a more robust method of calling executables by their direct path (e.g., `.venv/bin/pip`, `.venv/bin/uvicorn`). This guarantees that the correct, isolated environment is always used.

### 2. Re-installing and Patching ComfyUI

-   **Problem:** The project's primary dependency, ComfyUI, was either missing or corrupted. Furthermore, its own dependencies were incompatible with the host machine's operating system (macOS Catalina 10.15.7).
-   **Solution:**
    1.  A fresh clone of the ComfyUI repository was performed.
    2.  The `git checkout -f HEAD` command was used to resolve file checkout errors during the clone.
    3.  The `av` library, which was incompatible with the OS, was identified as a blocker. Since it is only used for video/audio features, it was removed from ComfyUI's `requirements.txt` to allow the installation to proceed.

### 3. Debugging the Runtime Environment

-   **Problem:** Once installed, ComfyUI failed to run due to a series of runtime errors.
-   **Solution:**
    1.  **Python Version:** A `SyntaxError` on an f-string indicated that the `python` command was resolving to an outdated system Python. The fix was to explicitly use `python3`.
    2.  **NumPy/Torch Conflict:** A `numpy` version conflict with `torch` was resolved by downgrading `numpy` to a version less than 2.0 (`pip install 'numpy<2'`).
    3.  **CUDA Error:** An `AssertionError: Torch not compiled with CUDA enabled` was resolved by launching ComfyUI with the `--cpu` flag, forcing it to run on the CPU and ignore the missing NVIDIA GPU.

### 4. Optimizing Performance and Quality

-   **Problem:** Initial generations were unacceptably slow (estimated >1 hour) and produced low-quality, "blobby" output.
-   **Solution:**
    1.  **Model Precision:** The primary performance bottleneck was the model running in `float32`. The ComfyUI launch command was updated with `--force-fp16` to use faster 16-bit half-precision.
    2.  **LoRA Correction:** A corrupt LoRA file was identified via a `HeaderTooLarge` error. It was replaced with a known-good, standard pixel art LoRA.
    3.  **Prompt Engineering:** The "garbage output" was addressed by creating a hybrid prompt system. The Art Specialist LLM generates a creative description of the *subject*, which is then appended with a hardcoded "base prompt" containing the non-negotiable technical and stylistic constraints for GBC pixel art.

## V2 Architecture: The Interactive Multi-Agent Workflow

The initial "fire-and-forget" pipeline was a regression that removed user agency. The system was completely overhauled to restore and enhance the interactive workflow.

-   **Problem:** The user had no control over the generation process after the initial prompt. The pipeline was functional but produced poor results with no opportunity for correction.
-   **Solution:** A multi-step, human-in-the-loop UI and backend was implemented.
    1.  **PM Agent Re-instated:** The Project Manager agent was restored as the primary point of contact. It receives the user's high-level request and creates a plan.
    2.  **Two-Step Approval UI:** The frontend was redesigned to support a two-step approval process.
        -   **Step 1:** The user sees the PM's full plan in a dedicated chat window and must approve it.
        -   **Step 2:** Upon plan approval, the Art Specialist agent generates a creative prompt. The user sees this prompt and must give final approval before the expensive image generation task is started.
    3.  **Asynchronous Generation:** The final generation process is still handled by an asynchronous background task, allowing the UI to remain responsive. A WebSocket is used to push real-time status updates (e.g., "QUEUED", "COMPLETED") to an asset grid in the UI.
    4.  **Future-Proofing:** The new UI and backend logic are designed to be extensible for a future feedback and revision loop.