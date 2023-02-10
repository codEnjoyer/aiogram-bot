import logging

from aiogram.types import Message, CallbackQuery

from tgbot.keyboards.inline import choice_kb, apple_kb, pear_kb


async def show_items(message: Message):
    await message.answer(
        """На продажу есть 2 товара: яблоки и груши.\nЕсли вы не заинтересованы в предложенном, то нажмите "Отмена".""",
        reply_markup=choice_kb)


async def buying_apple(callback: CallbackQuery, callback_data: dict):
    await callback.answer(cache_time=30)
    logging.info(f"callback = {callback_data}")
    quantity = callback_data.get("quantity")
    await callback.message.answer(f"""Вы выбрали яблоки. Их всего {quantity}""", reply_markup=apple_kb)


async def buying_pear(callback: CallbackQuery, callback_data: dict):
    await callback.answer(cache_time=30)
    logging.info(f"callback = {callback_data}")
    quantity = callback_data.get("quantity")
    await callback.message.answer(f"""Вы выбрали груши. Их всего {quantity}""", reply_markup=pear_kb)


async def buying_cancel(callback: CallbackQuery):

    await callback.message.edit_reply_markup()
    await callback.message.edit_text("Вы отменили покупку.")
    await callback.answer("Вы успешно отменили покупку.", show_alert=True)
    logging.info(f"Покупка отменена. callback = {callback.data}")
