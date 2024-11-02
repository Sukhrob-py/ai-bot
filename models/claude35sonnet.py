# pip install anthropic
# payment neded

import anthropic

client = anthropic.Anthropic(
    api_key="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",
)


def claude(msg="hi"):
    # message = client.messages.create(
    #     model="claude-3-5-sonnet-20241022",
    #     max_tokens=1024,
    #     messages=[{"role": "user", "content": "Hello, Claude"}],
    # )

    # return message
    return "claude 3.5 sonnet"
