from utils.imports import *
from utils.models import MODELS

async def set_commands(dp: Dispatcher):
    commands = commands_f()
    await bot.set_my_commands(commands)


async def on_startup(dp):
    await set_commands(dp)


def model_selection_keyboard():
    keyboard = InlineKeyboardMarkup(row_width=2)
    buttons = [
        InlineKeyboardButton(text=model, callback_data=f"model_{model}")
        for model in MODELS.keys()
    ]
    keyboard.add(buttons[0])
    keyboard.row(*buttons[1:3])
    keyboard.add(buttons[3])
    keyboard.add(buttons[4])
    keyboard.row(*buttons[5:7])
    return keyboard