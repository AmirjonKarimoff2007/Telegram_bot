from aiogram import types
from aiogram.dispatcher.filters.builtin import Command
from loader import dp


# Echo bot
@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    await message.answer(message.text)
