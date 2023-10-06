from aiogram import types
from aiogram.dispatcher import filters
from loader import dp
@dp.message_handler(hashtags = 'savol')
@dp.message_handler(cashtags=['javob','savol'])
async def tags(msg: types.Message):
    text = 'Savolingiz qabul qilindi tez orada javob yozamiz'
    text += 'biz bilan ishlaganingiz uchun katta raxmat!'
    await msg.answer(text)