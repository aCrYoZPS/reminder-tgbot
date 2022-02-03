from aiogram import types, Dispatcher
from create_bot import bot
from keyboards import kb_welcome


async def handle_start(msg: types.Message):
    await bot.send_message(msg.from_user.id,
                           f"Я бот для напоминаний. Приятно познакомиться, {msg.from_user.first_name}",reply_markup=kb_welcome)


async def handle_help(msg: types.Message):
    await bot.send_message(msg.from_user.id, '''Используйте комманду /newreminder, чтобы установить напоминание.\nИспользуйте комманду /readrem, чтобы увидеть все ваши напоминания.\nИспользуйте комманду /cancel, чтобы отменить запись напоминания. ''',
                           reply_markup=kb_welcome)


def register_start_handler(dp: Dispatcher):
    dp.register_message_handler(handle_start, commands=['start'])
    dp.register_message_handler(handle_help, commands=['help'])
