from aiogram import types

async def info_command(message: types.Message):
    await message.reply(f'Ваш id - {message.from_user.id}\n'
                        f'Ваше имя - {message.from_user.first_name}\n'
                        f'Ваш тэг - {message.from_user.username}')