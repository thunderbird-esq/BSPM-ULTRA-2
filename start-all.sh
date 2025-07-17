#!/bin/bash

# GBStudio Hub - Start All Services
# This script starts ComfyUI, Ollama, and Backend with consolidated output

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# Configuration
COMFYUI_PATH="$HOME/ComfyUI"
PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Array to hold all background PIDs
pids=()

echo -e "${GREEN}========================================${NC}"
echo -e "${GREEN}  GBStudio Hub - Starting All Services${NC}"
echo -e "${GREEN}========================================${NC}"

# Function to cleanup processes on exit
cleanup() {
    echo -e "\n${YELLOW}Shutting down all services...${NC}"
    # Kill all tracked PIDs
    for pid in "${pids[@]}"; do
        kill "$pid" 2>/dev/null || true
    done
    # Stop Docker containers
    cd "$PROJECT_ROOT"
    docker-compose down --remove-orphans 2>/dev/null || true
    echo -e "${GREEN}All services stopped.${NC}"
    exit 0
}

# Function to handle errors
error_handler() {
    echo -e "\n${RED}An error occurred. Line $1: $2${NC}"
    cleanup
}

# Trap cleanup on script exit, interrupt, term, and errors
trap cleanup INT TERM
trap 'error_handler $LINENO "$BASH_COMMAND"' ERR

# Check prerequisites
echo -e "${BLUE}Checking prerequisites...${NC}"

if [ ! -d "$COMFYUI_PATH" ]; then
    echo -e "${RED}Error: ComfyUI not found at $COMFYUI_PATH${NC}"
    exit 1
fi

if [ ! -f "$COMFYUI_PATH/venv/bin/activate" ]; then
    echo -e "${RED}Error: ComfyUI virtual environment not found at $COMFYUI_PATH/venv${NC}"
    exit 1
fi

if ! command -v docker-compose &> /dev/null; then
    echo -e "${RED}Error: docker-compose not found${NC}"
    exit 1
fi

echo -e "${GREEN}✓ All prerequisites found${NC}"

# Start Ollama and Backend via Docker
echo -e "${BLUE}Starting Ollama and Backend (Docker)...${NC}"
cd "$PROJECT_ROOT"
docker-compose up -d
sleep 5 # Increased sleep to allow containers to initialize

# Start ComfyUI locally
echo -e "${BLUE}Starting ComfyUI locally...${NC}"
cd "$COMFYUI_PATH"
source venv/bin/activate
python main.py --listen 0.0.0.0 --port 8188 2>&1 | sed "s/^/[${CYAN}ComfyUI${NC}] /" &
pids+=($!) # Add ComfyUI PID to array

# Start monitoring Docker logs in background and prefix them
echo -e "${BLUE}Starting log monitoring...${NC}"
cd "$PROJECT_ROOT"

# Function to check if a container is running
is_container_running() {
    docker-compose ps -q "$1" | grep -q .
}

# Wait for backend container to be running before starting logs
echo "Waiting for backend container..."
while ! is_container_running backend; do
    sleep 1
done
echo "Backend container is up."

# Monitor Backend logs
docker-compose logs -f backend 2>&1 | sed "s/^/[${PURPLE}Backend${NC}] /" &
pids+=($!) # Add Backend log PID to array

# Wait for ollama container to be running before starting logs
echo "Waiting for ollama container..."
while ! is_container_running ollama; do
    sleep 1
done
echo "Ollama container is up."

# Monitor Ollama logs
docker-compose logs -f ollama 2>&1 | sed "s/^/[${YELLOW}Ollama${NC}] /" &
pids+=($!) # Add Ollama log PID to array

echo -e "\n${GREEN}========================================${NC}"
echo -e "${GREEN}  All Services Started Successfully!${NC}"
echo -e "${GREEN}========================================${NC}"
echo -e "${CYAN}ComfyUI:${NC}  http://localhost:8188"
echo -e "${PURPLE}Backend:${NC}   http://localhost:8000"
echo -e "${YELLOW}Ollama:${NC}    http://localhost:11434"
echo -e "\n${GREEN}Press Ctrl+C to stop all services${NC}"
echo -e "${GREEN}========================================${NC}\n"

# Wait for all background processes to complete
wait
