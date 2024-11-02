import requests
import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")


def geminiPro(msg):
    gemini_response = requests.post(
        url=f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key={GEMINI_API_KEY}",
        headers={"Content-Type": "application/json"},  # Fix header
        json={"contents": [{"parts": [{"text": msg}]}]},
    )
    if gemini_response.status_code == 200:
        gemini_result = gemini_response.json()["candidates"][0]["content"]["parts"][0][
            "text"
        ]
        return gemini_result
    else:
        return "There was an error with the Gemini API request."
