from config import dp, bot
from aiogram import types, Dispatcher
ADMINS = [620663358,]

async def check_user_is_admin(message: types.Message):
    """
    Функция для проверки прав админа автора сообщения
    в том чате, в который сообщение было отправлено
    """
    admins = await message.chat.get_administrators()
    for admin in admins:
        if admin["user"]["id"] == message.from_user.id:
            return True
    return False


async def echo(message: types.Message):
    bad_words = ['java', 'html', 'дурак', "дура"]
    username = f"@{message.from_user.username}" \
        if message.from_user.username is not None else message.from_user.first_name
    for word in bad_words:
        if word in message.text.lower().replace(' ', ''):
            await message.reply(f"Админ удалите {username} из группы")



async def ban_user(message: types.Message):
    """
    обработчик, чтоб банить пользователя в чате
    через команду
    """
    if message.chat.type != 'private':
        admin_author = await check_user_is_admin(message)
        print(f"{admin_author=}")
        if admin_author and message.reply_to_message:
            await message.bot.ban_chat_member(
                chat_id=message.chat.id,
                user_id=message.reply_to_message.from_user.id
            )
