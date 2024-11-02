# ! payment need
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
DEEP_SEEK_API_KEY = os.getenv("DEEP_SEEK_API_KEY")

client = OpenAI(api_key=DEEP_SEEK_API_KEY, base_url="https://api.deepseek.com")


def deepseek(msg="hi"):
    # response = client.chat.completions.create(
    #     model="deepseek-chat",
    #     messages=[
    #         {"role": "system", "content": "You are a helpful assistant"},
    #         {"role": "user", "content": "Hello"},
    #     ],
    #     stream=False,
    # )

    # return response.choices[0].message.content
    return "Deepseek LLM"
