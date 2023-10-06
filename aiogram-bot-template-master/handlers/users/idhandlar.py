from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp
ID = [5955950834]
@dp.message_handler(chat_id = ID,commands='start')
async def bot_start(message: types.Message):
    await message.answer('siz bizning super foydalanuvchimizsiz!')