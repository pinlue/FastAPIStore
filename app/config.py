from pathlib import Path

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str
    debug: bool
    database_url: str
    cors_origins: list[str]
    static_dir: str
    images_dir: str

    class Config:
        env_file = Path(__file__).parent / ".env"
        env_file_encoding = "utf-8"

settings = Settings()