from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
import sqlite3
from database import sqlite3_db
import random
from keyboards import kb_welcome

conn = sqlite3.connect('reminders.db')
cur = conn.cursor()
reminder = []


class FSMReminders(StatesGroup):
    rem_text = State()
    rem_time = State()
    rem_date = State()


# Отмена
async def handle_cancel(msg: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await msg.reply("Запись напоминания отменена.", reply_markup=kb_welcome)


# Начало ввода напоминания
async def rem_start(msg: types.Message):
    await FSMReminders.rem_text.set()
    await msg.reply("Введите текст напоминания:", reply_markup=kb_welcome)


# Ловим текст ремайндера
async def handle_text(msg: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['text'] = msg.text
    await FSMReminders.next()
    await msg.reply("Теперь введите время напоминания (например: 8:30, 18:05):")


# Ловим время ремайндера
async def handle_time(msg: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['time'] = msg.text
    await FSMReminders.next()
    await msg.reply("Теперь введите дату напоминания (например: 9.10, 22.01):")


# Ловим дату ремайндера
async def handle_date(msg: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['date'] = msg.text
        data['uid'] = msg.from_user.id
        data["reminder_id"] = random.randint(0, 2000000)
    await sqlite3_db.sql_add_command(state)
    await msg.reply(f"Запись напоминания выполнена, {msg.from_user.first_name}")
    await state.finish()


def register_newreminder_handlers(dp: Dispatcher):
    dp.register_message_handler(rem_start, commands=['newreminder'], state=None)
    dp.register_message_handler(handle_cancel, state="*", commands=['cancel'])
    dp.register_message_handler(handle_text, state=FSMReminders.rem_text)
    dp.register_message_handler(handle_time, state=FSMReminders.rem_time)
    dp.register_message_handler(handle_date, state=FSMReminders.rem_date)

