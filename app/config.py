import os
from dotenv import load_dotenv

load_dotenv()

GROK_API_CLOUD_KEY = os.getenv("GROK_API_CLOUD_KEY", "")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4o-mini")
