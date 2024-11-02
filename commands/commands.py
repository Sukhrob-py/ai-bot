from aiogram import Bot, Dispatcher, types

commands = [
    types.BotCommand(command="/start", description="Start the bot"),
    types.BotCommand(command="/gpt", description="Gpt model"),
    types.BotCommand(command="/geminiflash", description="Gemini 1.5-flash model"),
    types.BotCommand(command="/geminipro", description="Gemini 1.5-pro model"),
    types.BotCommand(command="/thebai", description="TheB ai 4.0 model"),
    types.BotCommand(command="/lama3", description="Llama-3.1 model"),
    types.BotCommand(command="/claude35", description="Claude-3.5 Sonnet model"),
]


def commands_f():
    return commands
