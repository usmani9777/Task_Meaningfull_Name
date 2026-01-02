import httpx
from core.config import Setting
from typing import Dict
import os
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

# Access them using os.environ or os.getenv()
URL = os.getenv('External_Joke_URL')




async def Joke() -> Dict[str, str]:
    try:
        response = httpx.get(URL, timeout=5.0)
        response.raise_for_status()

        data = response.json()

        if data.get("error"):
            return {
                "status": "error",
                "message": "External API returned an error"
            }

        if data.get("type") == "single":
            return {
                "status": "success",
                "type": "single",
                "joke": data.get("joke", "")
            }

        return {
            "status": "success",
            "type": "two-part",
            "setup": data.get("setup", ""),
            "delivery": data.get("delivery", "")
        }

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

    
# url = 'https://v2.jokeapi.dev/joke/Any'
# response = httpx.get(URL.External_Joke_URL)
# c = response.json()

# if c["type"] == 'single':
#   try:
#     print(c['joke'])
#   except:
#     print(c)
# else:
#   print(c['setup'],c['delivery'])

