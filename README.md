# GB Studio Asset Generation Hub

This project is a collection of tools and scripts to automate the generation of assets for GB Studio projects using AI.

## Project Structure

- `project_files/`: Contains the GB Studio project.
- `scripts/`: Contains Python scripts for automating asset generation.
- `temp_outputs/`: Contains temporary output files from the asset generation scripts.
- `docker-compose.yml`: Defines the services for running the project, including ComfyUI.
- `project_docs/`: Contains documentation for the project, such as the Art Style Guide and Game Design Document.

## Getting Started

### Prerequisites

- Docker
- Python 3.9+
- [ComfyUI](https://github.com/comfyanonymous/ComfyUI) installed in your home directory (`~/ComfyUI`).

### Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/gbstudio_hub.git
    cd gbstudio_hub
    ```

2.  **Run the services:**
    The `docker-compose.yml` file is configured to run ComfyUI, Ollama, and Langflow.
    ```bash
    docker-compose up -d
    ```
    This will start all the required services in the background.

3.  **Install Python dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Quick Start

### Option 1: All-in-One Startup (Recommended)
Start all services with colored output in a single terminal:
```bash
./start-all.sh
```

### Option 2: tmux Multi-Pane View
Start all services in separate tmux panes for better monitoring:
```bash
./start-tmux.sh
```

### Stop All Services
```bash
./stop-all.sh
```

## Services Overview

Once started, the following services will be available:
- **Backend (FastAPI)**: http://localhost:8000 - Main web interface
- **ComfyUI**: http://localhost:8188 - Image generation service  
- **Ollama**: http://localhost:11434 - LLM service

## Manual Startup (Alternative)

If you prefer to start services individually:

1. **Start Docker services (Backend + Ollama):**
   ```bash
   docker-compose up -d
   ```

2. **Start ComfyUI locally:**
   ```bash
   cd ~/ComfyUI && source venv/bin/activate && python main.py --listen 0.0.0.0 --port 8188
   ```

3. **Access the web interface:**
   Open http://localhost:8000 in your browser

## Workflow

1. **Use the web interface:**
   Navigate to `http://localhost:8000` for the Command Deck interface.

2. **Open the GB Studio project:**
   Open the `project_files/MyGBCGame.gbsproj` file in GB Studio to see generated assets.