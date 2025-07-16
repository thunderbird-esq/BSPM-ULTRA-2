import json
import os
import uuid
from PIL import Image
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def get_project_file_path(project_path: str) -> str:
    """Finds the .gbsproj file in the given project directory."""
    for root, _, files in os.walk(project_path):
        for file in files:
            if file.endswith('.gbsproj'):
                return os.path.join(root, file)
    raise FileNotFoundError("No .gbsproj file found in the specified project path.")

def add_asset_to_project(
    project_path: str,
    asset_filename: str,
    asset_type: str,
    task_name: str
) -> bool:
    """
    Adds a new asset entry to the .gbsproj JSON file.

    Args:
        project_path: The root path of the GB Studio project.
        asset_filename: The filename of the asset (e.g., 'player_sprite.png').
        asset_type: The type of asset ('sprite', 'background', etc.).
        task_name: The name of the task, used as the asset name in the project.

    Returns:
        True if the asset was added successfully, False otherwise.
    """
    try:
        gbsproj_path = get_project_file_path(project_path)
        
        with open(gbsproj_path, 'r') as f:
            project_data = json.load(f)

        asset_path_map = {
            "sprite": "assets/sprites/",
            "background": "assets/backgrounds/",
            "ui": "assets/ui/",
            "music": "assets/music/"
        }
        
        relative_asset_path = os.path.join(asset_path_map.get(asset_type, ""), asset_filename)
        full_asset_path = os.path.join(project_path, relative_asset_path)

        if not os.path.exists(full_asset_path):
            logging.error(f"Asset file not found at {full_asset_path}. Cannot add to project file.")
            return False

        if asset_type == 'sprite':
            new_asset = create_sprite_asset(full_asset_path, asset_filename, task_name)
            project_data['sprites'].append(new_asset)
        elif asset_type == 'background':
            new_asset = create_background_asset(full_asset_path, asset_filename, task_name)
            project_data['backgrounds'].append(new_asset)
        else:
            logging.warning(f"Asset type '{asset_type}' not yet supported by gbsproj_editor. Skipping JSON modification.")
            return True # Return True to not break the workflow for other asset types

        with open(gbsproj_path, 'w') as f:
            json.dump(project_data, f, indent=4)
            
        logging.info(f"Successfully added asset '{task_name}' to {gbsproj_path}")
        return True

    except Exception as e:
        logging.error(f"Failed to add asset to .gbsproj file: {e}")
        return False

def create_sprite_asset(image_path: str, filename: str, name: str) -> dict:
    """Creates a dictionary for a new sprite asset."""
    with Image.open(image_path) as img:
        width, height = img.size

    # GB Studio sprites are 16x16. Calculate frames based on this.
    frames = (width // 16) * (height // 16)

    return {
        "id": str(uuid.uuid4()),
        "name": name,
        "filename": filename,
        "width": width,
        "height": height,
        "type": "actor_animated" if frames > 1 else "static",
        "frames": frames,
        "animations": [],
        "animSpeed": 3,
        "collisionGroup": ""
    }

def create_background_asset(image_path: str, filename: str, name: str) -> dict:
    """Creates a dictionary for a new background asset."""
    with Image.open(image_path) as img:
        width, height = img.size

    return {
        "id": str(uuid.uuid4()),
        "name": name,
        "filename": filename,
        "width": width,
        "height": height,
        "imageWidth": width,
        "imageHeight": height,
        "autoColor": True
    }
