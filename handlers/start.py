from aiogram import types
from handlers.constants import START_TEXT
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

start_kb = InlineKeyboardMarkup(resize_keyboard=True)
start_kb.add(InlineKeyboardButton('Магазин',callback_data='shop_start'))
start_kb.add(InlineKeyboardButton('Наш адрес',callback_data='address'))

async  def start_command(message: types.Message):
    await message.answer(
        text=START_TEXT.format(
            first_name=message.from_user.first_name),
        reply_markup=start_kb
    )
    await message.delete()