# pip install anthropic
# payment neded

import anthropic

client = anthropic.Anthropic(
    api_key="",
)


def claude(msg="hi"):
    # message = client.messages.create(
    #     model="claude-3-5-sonnet-20241022",
    #     max_tokens=1024,
    #     messages=[{"role": "user", "content": "Hello, Claude"}],
    # )

    # return message
    return "claude 3.5 sonnet"
