from utils.imports import *
from utils.models import MODELS
from utils.model_keyboards import *


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


@dp.message_handler(commands=["deepseek"])
async def gpt_command(message: types.Message):
    await dp.current_state(user=message.from_user.id).update_data(
        selected_model="🐋 deepseek-llm"
    )
    await message.reply(
        "You've switched to the Deepseek LLM model. Now send your question."
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
