import subprocess
import shutil
import os
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def move_asset(source_path: str, asset_type: str, project_path: str) -> bool:
    """Moves a file to the correct asset subfolder based on its type."""
    if not os.path.exists(source_path):
        logging.error(f"Asset move failed: Source file not found at {source_path}")
        return False

    destination_map = {
        "sprite": "assets/sprites",
        "background": "assets/backgrounds",
        "music": "assets/music",
        "ui": "assets/ui"
    }
    subfolder = destination_map.get(asset_type.lower())
    if not subfolder:
        logging.error(f"Asset move failed: Unknown asset type '{asset_type}'")
        return False

    destination_dir = os.path.join(project_path, subfolder)
    try:
        os.makedirs(destination_dir, exist_ok=True)
        shutil.move(source_path, destination_dir)
        logging.info(f"Successfully moved {source_path} to {destination_dir}")
        return True
    except (shutil.Error, OSError) as e:
        logging.error(f"Asset move failed: {e}")
        return False

def compile_gb_studio_project(project_path: str, gbs_cli_path: str) -> (bool, str):
    """Compiles the GB Studio project using a specific CLI path."""
    if not os.path.exists(gbs_cli_path):
        logging.error(f"GB Studio CLI not found at the configured path: {gbs_cli_path}")
        return False, ""
    try:
        process = subprocess.run(
            [gbs_cli_path, "build", "--destination", "build/web"],
            cwd=project_path, check=True, capture_output=True, text=True
        )
        logging.info("GB Studio project compiled successfully.")
        rom_path = os.path.join(project_path, "build/web/game.gb")
        return True, rom_path
    except subprocess.CalledProcessError as e:
        logging.error(f"GB Studio compilation failed: {e.stderr}")
        return False, ""

def launch_in_emulator(rom_path: str, emulator_path: str) -> bool:
    """Launches a given ROM file in a specific emulator application on macOS."""
    if not os.path.exists(rom_path):
        logging.error(f"Emulator launch failed: ROM not found at {rom_path}")
        return False
    if not os.path.exists(emulator_path):
        logging.error(f"Emulator not found at the configured path: {emulator_path}")
        return False
    try:
        subprocess.run(["open", "-a", emulator_path, rom_path], check=True)
        logging.info(f"Launched {rom_path} in {os.path.basename(emulator_path)}.")
        return True
    except subprocess.CalledProcessError as e:
        logging.error(f"Failed to launch emulator: {e}")
        return False
