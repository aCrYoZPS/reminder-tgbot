from aiogram import types, Dispatcher
from database import sqlite3_db
from keyboards import kb_welcome


async def read_rem(msg: types.Message):
    reminders = sqlite3_db.sql_fetchall_where_userid(str(msg.from_user.id))
    print(reminders)
    if reminders == []:
        await msg.reply("У вас нет никаких напоминаний :(",reply_markup=kb_welcome)
    else:
        lines = []
        for rem in reminders:
            rem = [str(item) for item in rem]
            del rem[3:]
            line = '. '.join(rem)
            lines.append(line)
        text = '\n'.join(lines)
        await msg.reply(text,reply_markup=kb_welcome)


def register_readreminder_handler(dp: Dispatcher):
    dp.register_message_handler(read_rem, commands=['readrem'])
