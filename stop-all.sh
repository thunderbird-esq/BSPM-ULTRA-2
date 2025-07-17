#!/bin/bash

# GBStudio Hub - Stop All Services

set -e

# Colors
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SESSION_NAME="gbstudio-hub"

echo -e "${YELLOW}Stopping all GBStudio Hub services...${NC}"

# Stop tmux session if running
if tmux has-session -t $SESSION_NAME 2>/dev/null; then
    echo "Stopping tmux session..."
    tmux kill-session -t $SESSION_NAME
fi

# Stop Docker services
echo "Stopping Docker services..."
cd "$PROJECT_ROOT"
docker-compose down

# Kill any remaining ComfyUI processes
echo "Cleaning up any remaining processes..."
pkill -f "main.py.*8188" 2>/dev/null || true
pkill -f "ComfyUI" 2>/dev/null || true

echo -e "${GREEN}All services stopped successfully!${NC}"