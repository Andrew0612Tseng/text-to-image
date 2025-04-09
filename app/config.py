import os
from dotenv import load_dotenv

# 加載環境變量
load_dotenv()

# API設置
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError("未設置OPENAI_API_KEY環境變量")

DEFAULT_IMAGE_SIZE = "1024x1024"
DEFAULT_MODEL = "dall-e-3"