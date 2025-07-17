# Start from the official ComfyUI base image
FROM comfyanonymous/comfyui:latest

# Install system-level dependencies for custom nodes
RUN apt-get update && apt-get install -y git

# Install python dependencies for custom nodes like the Manager
RUN pip install opencv-python GitPython uv

# Copy your entire local ComfyUI directory into the image.
# This ensures all custom nodes, models, configs, etc., are included.
COPY . /ComfyUI

# Set the working directory
WORKDIR /ComfyUI

# Set the default command
CMD ["python", "main.py", "--listen", "0.0.0.0"]
