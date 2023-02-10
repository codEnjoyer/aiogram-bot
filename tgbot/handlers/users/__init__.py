from aiogram import Dispatcher
from aiogram.types import Message
from aiogram.dispatcher.filters import Text

from tgbot.keyboards.default.start import start_kb

from .menu import show_menu, get_food
from .purchase import show_items, buying_apple, buying_pear, buying_cancel
from ...keyboards.inline import buy_callback


async def user_start(message: Message):
    await message.reply("Hello, user!", reply_markup=start_kb)


def register_menu(dp: Dispatcher):
    dp.register_message_handler(show_menu, Text(equals=["Меню"]))
    dp.register_message_handler(get_food, Text(equals=["Котлетки", "Пюрешка", "Макарошки"]))


def register_purchase(dp: Dispatcher):
    dp.register_message_handler(show_items, Text(equals="Товары"))

    dp.register_callback_query_handler(buying_apple, buy_callback.filter(item_name="apple"))
    dp.register_callback_query_handler(buying_pear, buy_callback.filter(item_name="pear"))
    dp.register_callback_query_handler(buying_cancel, Text(equals="cancel"))


def register_user(dp: Dispatcher):
    dp.register_message_handler(user_start, commands=["start"], state="*")

    register_menu(dp)
    register_purchase(dp)
