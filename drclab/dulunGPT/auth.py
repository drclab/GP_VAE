import os
from pathlib import Path
from dotenv import load_dotenv

import openai

PROFILE_DIR = Path(os.path.abspath(os.path.dirname(__file__))) 
API_DIR = PROFILE_DIR.parent.parent

key_file = API_DIR / 'chatgpt.env'

load_dotenv(key_file)

api_key = os.getenv('API_KEY')

openai.api_key = api_key

prompt = 'who is Dr. Junhua Zhang'

response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
)

message = response.choices[0].text.strip()

print(message)

