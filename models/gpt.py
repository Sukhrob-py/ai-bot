import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=OPENAI_API_KEY)


def gpt(msg):
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": msg},
    ]
    response = client.chat.completions.create(
        model="gpt-4",
        messages=messages,
    )
    return response.choices[0].message.content.strip()
