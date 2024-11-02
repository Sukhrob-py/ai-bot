from utils.imports import *
from utils.models import MODELS
from utils.message_handler_commands import *

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

    elif selected_model == "🐋 deepseek-llm":
        res = deepseek(message.text)
        await message.reply(res)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
