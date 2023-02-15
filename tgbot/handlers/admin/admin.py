from aiogram import Dispatcher
from aiogram.types import Message

from tgbot.keyboards.default.start import start_kb


async def admin_start(message: Message):
    await message.reply("Hello, admin!", reply_markup=start_kb)


def register_admin(dp: Dispatcher):
    # dp.register_message_handler(admin_start, commands=["start"], state="*", is_admin=True)
    pass