import httpx
from typing import Dict
from openai import OpenAI
from models.user import user
import os
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

# Access them using os.environ or os.getenv()
API_Key = os.getenv("API_Key")



client = OpenAI(
    api_key=API_Key,
    base_url="https://api.groq.com/openai/v1",
)
ID = 1
Prompts = {}
async def ChatGPT(Prompt:user) -> Dict:
    try:
        global ID
        Prompts['current'] = Prompt.prompt
        response = client.responses.create(
        input= f'Based on dictionary of previous and new prompts respond to user while cuurent is most recent {Prompts}',
        model="openai/gpt-oss-20b",
        )
        Prompts[ID] = Prompt.prompt
        ID += 1
        return response
    except httpx.RequestError as e:
        return {
            "status": "error",
            "message": f"Request failed: {str(e)}"
        }

    except Exception as e:
        return {
            "status": "error",
            "message": f"Unexpected error: {str(e)}"
        }

    

