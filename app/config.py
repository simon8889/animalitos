from pydantic_settings import BaseSettings
from os import getenv

class Settings(BaseSettings):
    DATABASE_URL: str = getenv("DB_URL")
    DEBUG: bool = True
    AWS_BUCKET: str = getenv("AWS_BUCKET")
    AWS_ACCESS_KEY_ID: str = getenv("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY: str = getenv("AWS_SECRET_ACCESS_KEY")

    class Config:
        env_file = ".env"

settings = Settings()