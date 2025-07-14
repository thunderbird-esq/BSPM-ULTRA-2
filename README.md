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

## Workflow

1.  **Start the FastAPI server:**
    ```bash
    python scripts/main.py
    ```
    This will start the FastAPI server on `http://localhost:8000`.

2.  **Use the web interface:**
    Open your web browser and navigate to `http://localhost:8000`. You will be greeted with a simple web interface to interact with the asset generation pipeline.

3.  **Open the GB Studio project:**
    Open the `project_files/MyGBCGame.gbsproj` file in GB Studio to see the generated assets.