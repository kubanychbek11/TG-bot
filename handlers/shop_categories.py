from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

buy_item_kb = InlineKeyboardMarkup()
buy_item_kb.add(
    InlineKeyboardButton('Купить',callback_data='buy_item')
)

async def show_pizza(message: types.Message):
    await message.answer(text='Вот наше меню:')
    """Функция ответа пользователю заглавными буквами"""
    await message.answer(text='Пицца с ананасами',reply_markup=buy_item_kb)
    await message.answer(text='Пицца с грибами',reply_markup=buy_item_kb)
    await message.answer(text='Пицца с оливками',reply_markup=buy_item_kb)
