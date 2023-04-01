import sys
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

default_prompt = 'How to use ChatGPT?'

def answer(prompt):

        response = openai.Completion.create(
                engine="text-davinci-002",
                prompt=prompt,
                max_tokens=1024,
                n=1,
                stop=None,
                temperature=0.5,
        )

        return response.choices[0].text#.strip()


def main(args):
    print(answer(prompt=args))

if __name__ == "__main__":
        if len(sys.argv) > 1:
                main(sys.argv[1])
        else:
                main('I have a dream')
         

