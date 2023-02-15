from aiogram import Dispatcher
from aiogram.types import Message

from tgbot.keyboards.default.start import start_kb
from tgbot.services import register_commands

from .menu import show_menu, get_food, register_menu
from .purchase import show_items, buying_apple, buying_pear, buying_cancel, register_purchase


async def user_start(message: Message):
    await message.reply("Hello, user!", reply_markup=start_kb)


def register_user(dp: Dispatcher):
    dp.register_message_handler(user_start, commands=["start"], state="*")

    register_commands(dp)
    register_menu(dp)
    register_purchase(dp)
