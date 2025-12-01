import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    PROJECT_NAME: str = "DAYAN Backend"
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./dayan.db")
    SECRET_KEY: str = os.getenv("SECRET_KEY", "secret123")
    ALGORITHM: str = "HS256"

settings = Settings()
