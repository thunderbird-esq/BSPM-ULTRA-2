from pydantic_settings import BaseSettings
from pydantic import computed_field
import os

class Settings(BaseSettings):
    gb_project_path: str = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'project_files'))
    comfyui_output_path: str
    gbs_cli_path: str
    emulator_path: str
    ollama_api_url: str
    comfyui_api_url: str = os.getenv("COMFYUI_URL", "http://host.docker.internal:8188")

    class Config:
        env_file = ".env"
        env_file_encoding = 'utf-8'
        extra = 'ignore'

settings = Settings()
