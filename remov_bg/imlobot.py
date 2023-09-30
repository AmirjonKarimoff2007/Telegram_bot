import logging
from aiogram import Bot, Dispatcher, executor, types
from test import checkWord
API_TOKEN = '6473410449:AAE6FTD8Vg0Bm36Xx5UxcP0oRWf994mTM2Q'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Salom imlo botga xush kelipsiz!")
@dp.message_handler(commands=['help'])
async def userhelp(message: types.Message):
    await message.reply("Assalomu Aleykum sizga qanday yordam bera olaman!")

@dp.message_handler()
async def checkimlo(message: types.Message):
    word = message.text
    result = checkWord(word)
    if result['available']:
        response += f"{word.capitalize()}"
    else:
        response = f"xato:{word.capitalize()}n"
        for text in result['matches']:
            response += f"tugri:{text.capitalize()}"
    await message.answer(response)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)