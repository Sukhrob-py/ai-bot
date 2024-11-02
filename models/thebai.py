import requests
import json, os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("THEBAI")

url = "https://api.theb.ai/v1/search/completions"


# url = "https://api.baizhi.ai/v1/search/completions"
def thebai(msg):
    payload = json.dumps(
        {
            "messages": [{"role": "user", "content": msg}],
            "stream": False,
        }
    )
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    return response.json()["choices"][0]["message"]["content"]
