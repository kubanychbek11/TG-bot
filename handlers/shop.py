from aiogram import types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


shop_kb = ReplyKeyboardMarkup(resize_keyboard=True)
shop_kb.add(
    KeyboardButton("Хочу пиццы"),
    KeyboardButton("Хочу напитки"),
    KeyboardButton("Хочу мерч")
)
async  def shop_start(cb: types.CallbackQuery):
    """ответ на нажатие кнопки магазина"""
    await cb.bot.send_message(
        chat_id=cb.from_user.id,
        text="Выберите категорию ",
        reply_markup=shop_kb
    )


async def address(cb: types.CallbackQuery):
    await cb.bot.send_message(

        chat_id=cb.from_user.id,
        text="Наш адресс город Токмок ул. Шамсинская 6"
    )