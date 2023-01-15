from handlers.start import start_command
from handlers.help import help_command
from handlers.shop import shop_start, address
#from handlers.pictures import photo
from handlers.info import info_command
from handlers.shop_categories import show_pizza
from handlers.all_messages import echo
from aiogram import executor, Bot, Dispatcher, types
from aiogram.dispatcher.filters import Text
from dotenv import load_dotenv
from os import getenv
import random


if __name__ == "__main__":
    load_dotenv()
    bot = Bot(getenv("TG_TOKEN"))
    dp = Dispatcher(bot=bot)

    dp.register_message_handler(start_command, commands=['start'])
#    dp.register_message_handler(photo, commands=['picture'])
    dp.register_message_handler(help_command, commands=['help'])
    dp.register_message_handler(info_command, commands=['myinfo'])
    dp.register_callback_query_handler(shop_start, text='shop_start')
    dp.register_message_handler(show_pizza, Text(equals='Хочу пиццы'))
    dp.register_callback_query_handler(address,Text(equals='address'))
    @dp.message_handler(commands=['picture'])
    async def photo(message: types.Message):
        photos = (
            'images/1.jpg',
            'images/2.jpg',
            'images/3.jpg',
            'images/4.jpg',
            'images/5.jpg'
        )
        photo = open(random.choice(photos), 'rb')
        await bot.send_photo(message.from_user.id, photo=photo)
    dp.register_message_handler(echo)

    executor.start_polling(dp, skip_updates=True)
