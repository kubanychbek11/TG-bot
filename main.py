import random

from aiogram import types, executor
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
from os import getenv

load_dotenv()
bot = Bot(getenv("TG_TOKEN"))
dp = Dispatcher(bot=bot)

@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    await message.answer(f"Hello {message.from_user.full_name} ")
    await  message.reply("Привет босс")

@dp.message_handler(commands=['help'])
async def command_start(message: types.Message):
    await message.answer("start = команда для начала работы с ботом\n"
                         "help - описание команд\n"
                         "myinfo - данные о вас\n"
                         "picture - рандомная картинка"
                         )

@dp.message_handler(commands=['myinfo'])
async def command_start(message: types.Message):
    await message.reply(f'Ваш id - {message.from_user.id}\n'
                        f'Ваше имя - {message.from_user.first_name}\n'
                        f'Ваш тэг - {message.from_user.username}')

@dp.message_handler(commands=['picture'])
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


@dp.message_handler()
async def echo(message: types.Message):
    if len(message.text.split()) > 2:
        await message.reply(message.text.upper())


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)