#! payment neded

import json, os
from llamaapi import LlamaAPI
from dotenv import load_dotenv

# Initialize the SDK
load_dotenv()
llama_ai = LlamaAPI(os.getenv("LLAMA_API_KEY"))


def llama(msg="hi"):

    # Build the API request
    api_request_json = {
        "model": "llama3.1-70b",
        "messages": [
            {"role": "user", "content": "hi whatsup!"},
        ],
        # "functions": [
        #     {
        #         "name": "get_current_weather",
        #         "description": "Get the current weather in a given location",
        #         "parameters": {
        #             "type": "object",
        #             "properties": {
        #                 "location": {
        #                     "type": "string",
        #                     "description": "The city and state, e.g. San Francisco, CA",
        #                 },
        #                 "days": {
        #                     "type": "number",
        #                     "description": "for how many days ahead you wants the forecast",
        #                 },
        #                 "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]},
        #             },
        #         },
        #         "required": ["location", "days"],
        #     }
        # ],
        "stream": False,
        # "function_call": "get_current_weather",
    }

    # Execute the Request
    # response = llama_ai.run(api_request_json)
    # print(response)
    # print(json.dumps(response.json(), indent=2))
    return "llama"
