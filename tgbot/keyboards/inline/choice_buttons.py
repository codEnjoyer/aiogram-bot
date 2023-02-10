from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from tgbot.config import load_config
from tgbot.keyboards.inline import buy_callback

config = load_config(".env")
apple_quantity = 3
pear_quantity = 2

apple_button = InlineKeyboardButton(text=f"Купить {apple_quantity} яблока",
                                    callback_data=buy_callback.new(item_name="apple", quantity=apple_quantity))
pear_button = InlineKeyboardButton(text=f"Купить {pear_quantity} груши",
                                   callback_data=buy_callback.new(item_name="pear", quantity=pear_quantity))
cancel_button = InlineKeyboardButton(text="Отмена", callback_data="cancel")

choice_kb = InlineKeyboardMarkup() \
    .row(apple_button, pear_button) \
    .row(cancel_button)

apple_kb = InlineKeyboardMarkup()\
    .row(InlineKeyboardButton(text="Ссылка для покупки яблок", url=config.misc.apples_url))
pear_kb = InlineKeyboardMarkup()\
    .row(InlineKeyboardButton(text="Ссылка для покупки груш", url=config.misc.pears_url))
