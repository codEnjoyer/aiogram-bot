from aiogram.dispatcher.filters.state import StatesGroup, State


class FSMTest(StatesGroup):
    first_question = State()
    second_question = State()
