from aiogram import types
from aiogram.dispatcher.filters.builtin import Command
from loader import dp

@dp.message_handler(commands=['til','vaqt'])
async def change_language(message: types.Message):
    await message.answer("til o'zgardi")