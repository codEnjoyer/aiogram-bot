from aiogram.types.reply_keyboard import ReplyKeyboardMarkup, KeyboardButton

menu_button = KeyboardButton(text="Меню")
items_button = KeyboardButton(text="Товары")
start_kb = ReplyKeyboardMarkup() \
    .row(menu_button, items_button)
