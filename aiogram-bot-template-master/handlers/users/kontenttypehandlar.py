from aiogram import types
from aiogram.dispatcher import filters
from loader import dp

@dp.message_handler(content_types=types.ContentTypes.PHOTO)
async def photo_handler(msg: types.Message):
    await msg.answer("Bu qanday rasm!")
# Document filter
@dp.message_handler(content_types=types.ContentTypes.DOCUMENT)
async def Document_handler(msg: types.Message):
    await msg.answer("Bu qanaqa file!")
# voice filter
@dp.message_handler(content_types=types.ContentTypes.VOICE)
async def voice_handler(msg: types.Message):
    await msg.answer("Yaxshi eshitmadim,aniqroq gapiring!")
#video filter
@dp.message_handler(content_types='video')
async def video_handler(msg: types.Message):
    await msg.answer("Bu qanday video!")
# stiker filter
@dp.message_handler(content_types=types.ContentTypes.STICKER)
async def sticer_handler(msg: types.Message):
    await msg.answer("Zo'r!")
@dp.message_handler(content_types='hashtags')
async def hashtags_handler(msg: types.Message):
    text = 'bunday hash tag bizda mavjud emas'
    await msg.answer(test)
