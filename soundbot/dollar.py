import requests
from pprint import pprint as printsub
import logging
from aiogram import Bot, Dispatcher, executor, types
import requests
from pprint import pprint as print
def UZS_Dollar(qiymat):
    API_KEY = '9c79089800f9b46119e4230d'
    currency = 'USD'
    url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/pair/{currency}/UZS"
    response = requests.get(url)
    dollar = response.json()['conversion_rate']
    return int(dollar)*qiymat
API_TOKEN = '6604252458:AAHUUsL0bjgUvd7mXQYQ8SwzPuFonitxDSE'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Kurs haqida malumot beruvchi botga xush kelipsiz!")

@dp.message_handler()
async def bg-remover(message: types.Message):
    try:

    except:
        await message.answer("Dasturda xatolik yuz berdi")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
