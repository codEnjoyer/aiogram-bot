from aiogram import Dispatcher

from .fsm_test import register_test_handlers


def register_states(dp: Dispatcher):
    register_test_handlers(dp)
