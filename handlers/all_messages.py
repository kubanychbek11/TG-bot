from aiogram import types

async def echo(message: types.Message):
    if len(message.text.split()) > 2:
        await message.reply(message.text.upper())