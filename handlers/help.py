from aiogram import types

async def help_command(message: types.Message):
    await message.answer("start = команда для начала работы с ботом\n"
                         "help - описание команд\n"
                         "myinfo - данные о вас\n"
                         "picture - рандомная картинка"
                         )