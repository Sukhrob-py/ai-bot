import logging
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import executor
import os

from commands.commands import commands_f
from models.llama import llama
from models.claude35sonnet import claude
from models.geminipro import geminiPro
from models.thebai import thebai
from models.gpt import gpt

from dotenv import load_dotenv

load_dotenv()
logging.basicConfig(level=logging.INFO)

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

bot = Bot(token=TELEGRAM_BOT_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

MODELS = {
    "🤖 gpt-4": "gpt-4",
    "⚡ gemini-1.5-flash": "gemini-model-id",
    "🌟 gemini-1.5-pro": "gemini-model-id",
    "🚀 theBai-4.0": "theb ai-4.0",
    "🐪 lama3": "lama-3.1",
    "🧠 claude35": "claude-3.5-sonnet",
}


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
    for i in range(1, 3, 2):
        keyboard.row(*buttons[i : i + 2])
    keyboard.add(buttons[3])
    keyboard.add(buttons[4])
    keyboard.add(buttons[5])
    return keyboard


@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.reply(
        "Hello! Choose a model to ask a question.",
        reply_markup=model_selection_keyboard(),
    )


@dp.message_handler(commands=["gpt"])
async def gpt_command(message: types.Message):
    await dp.current_state(user=message.from_user.id).update_data(
        selected_model="🤖 gpt-4"
    )
    await message.reply("You've switched to the GPT-4 model. Now send your question.")


@dp.message_handler(commands=["geminiflash"])
async def gpt_command(message: types.Message):
    await dp.current_state(user=message.from_user.id).update_data(
        selected_model="⚡ gemini-1.5-flash"
    )
    await message.reply(
        "You've switched to the Gemini 1.5-flash model. Now send your question."
    )


@dp.message_handler(commands=["geminipro"])
async def gpt_command(message: types.Message):
    await dp.current_state(user=message.from_user.id).update_data(
        selected_model="🌟 gemini-1.5-pro"
    )
    await message.reply(
        "You've switched to the Gemini 1.5-pro model. Now send your question."
    )


@dp.message_handler(commands=["lama3"])
async def gpt_command(message: types.Message):
    await dp.current_state(user=message.from_user.id).update_data(
        selected_model="🐪 lama3"
    )
    await message.reply(
        "You've switched to the Lama-3.1 model. Now send your question."
    )


@dp.message_handler(commands=["thebai"])
async def gpt_command(message: types.Message):
    await dp.current_state(user=message.from_user.id).update_data(
        selected_model="🚀 theBai-4.0"
    )
    await message.reply(
        "You've switched to the Lama-3.1 model. Now send your question."
    )


@dp.message_handler(commands=["claude35"])
async def gpt_command(message: types.Message):
    await dp.current_state(user=message.from_user.id).update_data(
        selected_model="🧠 claude35"
    )
    await message.reply(
        "You've switched to the Claude-3.5 Sonnet model. Now send your question."
    )


@dp.callback_query_handler(lambda c: c.data.startswith("model_"))
async def process_model_selection(callback_query: types.CallbackQuery):
    model = callback_query.data.split("_")[1]
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(
        callback_query.from_user.id,
        f"You've selected the {model} model. Now send your question.",
    )

    await dp.current_state(user=callback_query.from_user.id).update_data(
        selected_model=model
    )  # Add 'await'


@dp.message_handler()
async def handle_question(message: types.Message):
    user_data = await dp.current_state(user=message.from_user.id).get_data()
    selected_model = user_data.get("selected_model", "🤖 gpt-4")

    if selected_model not in MODELS:
        await message.reply("Please select a model first using /start.")
        return

    if selected_model == "🤖 gpt-4":
        res = gpt(message.text)
        await message.reply(res)

    elif selected_model == "⚡ gemini-1.5-flash":
        res = geminiPro(message.text)
        await message.reply(res)

    elif selected_model == "🌟 gemini-1.5-pro":
        res = geminiPro(message.text)
        await message.reply(res)

    elif selected_model == "🐪 lama3":
        res = llama(message.text)
        await message.reply(res)

    elif selected_model == "🧠 claude35":
        res = claude(message.text)
        await message.reply(res)

    elif selected_model == "🚀 theBai-4.0":
        res = thebai(message.text)
        await message.reply(res)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
