from aiogram import types
import random



async def photo(message: types.Message):
    photos =(
        'images/1.jpg',
        'images/2.jpg',
        'images/3.jpg',
        'images/4.jpg',
        'images/5.jpg'
    )
    photo= open(random.choice(photos),'rb')
    await bot.send_photo(message.from_user.id,photo=photo)