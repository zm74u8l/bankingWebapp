import os
from dotenv import load_dotenv
load_dotenv()

class Settings:
    ENV = os.getenv("ENV", "dev")
    TINK_CLIENT_ID = os.getenv("TINK_CLIENT_ID")
    TINK_CLIENT_SECRET = os.getenv("TINK_CLIENT_SECRET")
    API_URL = os.getenv("API_URL")

settings = Settings()