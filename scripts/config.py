from pydantic_settings import BaseSettings
from pydantic import computed_field
import os

class Settings(BaseSettings):
    gb_project_path: str = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'project_files'))
    
    # Base path for the ComfyUI installation, loaded from .env
    comfyui_path: str 

    gbs_cli_path: str
    emulator_path: str
    ollama_api_url: str
    comfyui_api_url: str

    @computed_field
    @property
    def comfyui_output_path(self) -> str:
        """Dynamically constructs the path to the ComfyUI output directory."""
        return os.path.join(self.comfyui_path, "output")

    class Config:
        env_file = ".env"
        env_file_encoding = 'utf-8'

settings = Settings()
