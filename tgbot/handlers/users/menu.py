from aiogram import Dispatcher
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.dispatcher.filters import Text

from tgbot.keyboards.default import start_menu_kb


async def show_menu(message: Message):
    await message.answer("Выберите товар из меню ниже:", reply_markup=start_menu_kb)


async def get_food(message: Message):
    await message.answer(f"Вы выбрали {message.text}. Потрясающий выбор!", reply_markup=ReplyKeyboardRemove())


def register_menu(dp: Dispatcher):
    dp.register_message_handler(show_menu, Text(equals=["Меню"]))
    dp.register_message_handler(get_food, Text(equals=["Котлетки", "Пюрешка", "Макарошки"]))
