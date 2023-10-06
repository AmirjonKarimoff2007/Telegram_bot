from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp

@dp.message_handler(CommandStart(deep_link='sariqdev'))
async def bot_start(message: types.Message):
    args = message.get_args()
    text = f"salom,{message.from_user.full_name}!\n"
    text += f"Sizni {args} tavsiya qildi\n"
    text += "Xush kelipsiz siz bizning qadrli mijozimizsiz!"
    await message.answer(text)
@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!")
