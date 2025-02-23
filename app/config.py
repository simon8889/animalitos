from pydantic_settings import BaseSettings
from os import getenv

class Settings(BaseSettings):
    DATABASE_URL: str = getenv("DB_URL")
    DEBUG: bool = True

    class Config:
        env_file = ".env"

settings = Settings()