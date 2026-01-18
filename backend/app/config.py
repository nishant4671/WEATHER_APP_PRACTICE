import os
from typing import List
from pydantic_settings import BaseSettings
from pydantic import Field


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""
    
    # App Configuration
    app_name: str = "Weather App Backend"
    version: str = "1.0.0"
    debug: bool = False
    
    # API Configuration
    openweather_api_key: str = Field(..., env="OPENWEATHER_API_KEY")
    openweather_base_url: str = "https://api.openweathermap.org/data/2.5"
    
    # CORS Configuration
    cors_origins: str = "*"
    
    # Server Configuration
    host: str = "0.0.0.0"
    port: int = 8000
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = False


settings = Settings()
__all__ = ["settings"]
