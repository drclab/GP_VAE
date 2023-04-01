import os
from pathlib import Path
from dotenv import load_dotenv

PROFILE_DIR = Path(os.path.abspath(os.path.dirname(__file__))) 
API_DIR = PROFILE_DIR.parent.parent

key_file = API_DIR / 'chatgpt.env'

load_dotenv(key_file)

api_key = os.getenv('API_KEY')

print(api_key)