from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand, BotCommandScopeDefault, BotCommandScopeChat, Message
from aiogram.utils.markdown import quote_html


async def set_default_commands(bot: Bot) -> bool:
    return await bot.set_my_commands(
        commands=[
            BotCommand("start", "Запустить бота"),
            BotCommand("get_commands", "Получить доступные команды"),
            BotCommand("delete_commands", "Удалить доступные команды"),
            BotCommand("test", "Начать тестирование"),
        ],
        scope=BotCommandScopeDefault()
    )


async def message_get_commands(message: Message):
    no_lang = await message.bot.get_my_commands(scope=BotCommandScopeChat(message.from_user.id))
    no_scope = await message.bot.get_my_commands()
    ru_lang = await message.bot.get_my_commands(scope=BotCommandScopeChat(message.from_user.id), language_code="ru")

    await message.reply("\n".join(
        f"<pre>{quote_html(arg)=}</>" for arg in (no_lang, no_scope, ru_lang)
    ))


async def message_reset_commands(message: Message):
    await message.bot.delete_my_commands()
    await message.reply("Команды были удалены!")


def register_commands(dp: Dispatcher):
    dp.register_message_handler(message_get_commands, commands=["get_commands"])
    dp.register_message_handler(message_reset_commands, commands=["delete_commands"])
