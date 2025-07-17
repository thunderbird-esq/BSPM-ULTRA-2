# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a GB Studio Asset Generation Hub - a FastAPI-based application that automates the generation of assets for Game Boy Studio projects using AI. It integrates ComfyUI for image generation, Ollama for conversational AI agents, and GB Studio CLI for project compilation.

## Development Commands

### Environment Setup
```bash
# Install Python dependencies
pip install -r requirements.txt

# Start all services with Docker Compose
docker-compose up -d
```

### Running the Application
```bash
# Start the FastAPI server
python scripts/main.py

# Run tests
pytest

# Run tests with specific configuration
pytest tests/
```

### Docker Services
The application runs three main services:
- **Backend**: FastAPI server on port 8000
- **ComfyUI**: Image generation service on port 8188
- **Ollama**: LLM service on port 11434

## Architecture Overview

### Core Components

**FastAPI Application** (`scripts/main.py`):
- Main application entry point with WebSocket support
- Manages conversational AI agents (PM, Art, Writing, Code, QA, Sound)
- Handles asset generation pipeline orchestration
- Integrates with ComfyUI and Ollama services

**Configuration Management** (`scripts/config.py`):
- Uses Pydantic settings with environment variable support
- Requires `.env` file with paths and API URLs
- Key settings: `gb_project_path`, `comfyui_output_path`, `gbs_cli_path`, `emulator_path`

**Database Layer** (`scripts/database.py`):
- SQLite database for tracking conversations and assets
- Manages asset lifecycle (queued → generating → completed → approved → integrated)
- Stores chat history and asset metadata

**Project Integration** (`scripts/project_integrator.py`):
- Handles moving generated assets to GB Studio project folders
- Manages GB Studio project compilation via CLI
- Launches compiled ROMs in emulator

**GB Studio Project Editor** (`scripts/gbsproj_editor.py`):
- Modifies `.gbsproj` files to include generated assets
- Handles project file structure and asset references

### Asset Generation Pipeline

1. **User Request** → PM Agent (analyzes and delegates to appropriate department)
2. **Department Processing** → Art/Writing/Code/Sound agents generate specific outputs
3. **Asset Creation** → ComfyUI generates images or saves text/code assets
4. **Review & Approval** → Assets stored in database with approval workflow
5. **Integration** → Approved assets moved to GB Studio project and compiled
6. **Playtesting** → Compiled ROM launched in emulator

### Workflow System

ComfyUI workflows in `workflows/` directory:
- `workflow_pixel_art.json`: For sprite generation
- `workflow_background.json`: For background generation
- `workflow_ui_element.json`: For UI element generation

Each workflow uses placeholder tokens `[SUBJECT]` and `[ASSET_TYPE]` that get replaced with dynamic content.

## File Structure

```
project_files/          # GB Studio project files
├── MyGBCGame.gbsproj   # Main project file
└── assets/             # Generated assets organized by type
    ├── backgrounds/
    ├── sprites/
    ├── music/
    └── dialogue/

scripts/                # Python application code
├── main.py            # FastAPI application
├── config.py          # Settings management
├── database.py        # Database operations
├── project_integrator.py  # Asset integration
└── gbsproj_editor.py  # Project file editing

static/                 # Web interface assets
├── css/
└── js/

workflows/             # ComfyUI workflow definitions
```

## Environment Configuration

Required environment variables in `.env`:
- `COMFYUI_OUTPUT_PATH`: Path to ComfyUI output directory
- `GBS_CLI_PATH`: Path to GB Studio CLI executable
- `EMULATOR_PATH`: Path to Game Boy emulator
- `OLLAMA_API_URL`: Ollama service URL (typically http://localhost:11434)
- `COMFYUI_API_URL`: ComfyUI service URL (typically http://localhost:8188)

## Development Notes

### Agent System
The application uses specialized AI agents for different aspects of game development:
- **PM**: Project management and task delegation
- **Art**: Visual asset generation with ComfyUI integration
- **Writing**: Text content generation (dialogue, descriptions)
- **Code**: GBScript logic generation
- **QA**: Bug identification and testing
- **Sound**: Audio asset descriptions

### WebSocket Communication
Real-time updates for asset generation progress are broadcast via WebSocket to connected clients at `/ws` endpoint.

### Database Schema
Assets have lifecycle states: `queued` → `generating` → `completed` → `approved` → `integrated`

### GB Studio Integration
The system automatically integrates approved assets into the GB Studio project structure and updates the `.gbsproj` file accordingly.
