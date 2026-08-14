# Centralized app settings, loaded from environment variables (.env in local dev).
from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[3]

class Settings(BaseSettings):

    # database
    database_url:str  # async : used by FastAPI
    database_url_sync:str  # sync : used by Alembic

    # auth
    jwt_secret: str 
    jwt_algorithm: str
    jwt_expire_minutes: str
    google_client_id: str

    # llm
    groq_api_key: str

    # resend (email)
    resend_api_key: str

    # application
    environment: str = "development"

    model_config = SettingsConfigDict(
        env_file=BASE_DIR / ".env",
        env_file_encoding="utf-8",
        case_sensitive=False
    )


settings = Settings()
