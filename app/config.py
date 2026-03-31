from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    TELEGRAM_TOKEN: str
    DATABASE_URL: str = "sqlite:///./finance.db"
    SECRET_KEY: str
    APP_ENV: str = "development"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()