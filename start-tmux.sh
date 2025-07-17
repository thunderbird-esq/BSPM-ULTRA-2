#!/bin/bash

# GBStudio Hub - Start All Services in tmux
# This script starts all services in separate tmux panes for better monitoring

set -e

# Configuration
COMFYUI_PATH="$HOME/ComfyUI"
PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SESSION_NAME="gbstudio-hub"

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m'

echo -e "${GREEN}Starting GBStudio Hub in tmux session: $SESSION_NAME${NC}"

# Kill existing session if it exists
tmux kill-session -t $SESSION_NAME 2>/dev/null || true

# Create new tmux session
tmux new-session -d -s $SESSION_NAME

# Split into 3 panes
tmux split-window -h
tmux split-window -v

# Pane 0: ComfyUI
tmux select-pane -t 0
tmux send-keys "cd '$COMFYUI_PATH'" C-m
tmux send-keys "source venv/bin/activate" C-m
tmux send-keys "echo 'Starting ComfyUI...'" C-m
tmux send-keys "python main.py --listen 0.0.0.0 --port 8188" C-m

# Pane 1: Docker services (Backend + Ollama)
tmux select-pane -t 1
tmux send-keys "cd '$PROJECT_ROOT'" C-m
tmux send-keys "echo 'Starting Docker services...'" C-m
tmux send-keys "docker-compose up" C-m

# Pane 2: Logs and monitoring
tmux select-pane -t 2
tmux send-keys "cd '$PROJECT_ROOT'" C-m
tmux send-keys "echo 'Service Status Monitor'" C-m
tmux send-keys "echo '====================='" C-m
tmux send-keys "echo 'ComfyUI:  http://localhost:8188'" C-m
tmux send-keys "echo 'Backend:   http://localhost:8000'" C-m
tmux send-keys "echo 'Ollama:    http://localhost:11434'" C-m
tmux send-keys "echo ''" C-m
tmux send-keys "echo 'Use Ctrl+B then arrow keys to switch panes'" C-m
tmux send-keys "echo 'Type \"exit\" in each pane to stop services'" C-m

# Attach to session
echo -e "${BLUE}Attaching to tmux session. Use Ctrl+B then 'd' to detach.${NC}"
tmux attach-session -t $SESSION_NAME