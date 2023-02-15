from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import Message
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher.filters.state import StatesGroup, State


class FSMTest(StatesGroup):
    first_question = State()
    second_question = State()


async def enter_test(message: Message):
    await message.answer("Вы начали тестирование. В этом сообщении находится зашифрованный первый вопрос.")
    await FSMTest.first()


async def send_second_question(message: Message, state: FSMContext):
    answer = message.text
    async with state.proxy() as data:
        data["first_answer"] = answer
    await message.answer("Вы ответили на первый вопрос. В этом сообщении находится зашифрованный второй вопрос.")
    await FSMTest.next()


async def end_test(message: Message, state: FSMContext):
    answer = message.text
    async with state.proxy() as data:
        data["second_answer"] = answer
        await message.answer("Спасибо за прохождение теста. Вы уже знаете свой результат.\n"
                             f"Лучше перечитайте, что вы тут понаписали: {dict(data.items())}")
    await state.finish()


def register_test_handlers(dp: Dispatcher):
    dp.register_message_handler(enter_test, Command("test"), state=None)
    dp.register_message_handler(send_second_question, state=FSMTest.first_question)
    dp.register_message_handler(end_test, state=FSMTest.second_question)
