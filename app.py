import logging
import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, executor, types
load_dotenv()


API_TOKEN = "7402410233:AAEvUvC-BFtD5E4ZzfVunxza7-UJDF2dfE0"

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    username = message.from_user.username
    await message.reply(f"Welkome @{username}")

@dp.message_handler()
async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)

    await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
