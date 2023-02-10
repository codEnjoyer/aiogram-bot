from aiogram.types.reply_keyboard import ReplyKeyboardMarkup, KeyboardButton

start_menu_kb = ReplyKeyboardMarkup() \
    .row(KeyboardButton(text="Котлетки")) \
    .row(KeyboardButton(text="Пюрешка"), KeyboardButton(text="Макарошки"))
