from aiogram.utils import executor
from create_bot import dp
from database import sqlite3_db
import asyncio
from handlers import welcome_handler, newreminder_handler, readreminders_handler, remind_handler


async def on_startup(_):
    sqlite3_db.sql_start()


welcome_handler.register_start_handler(dp)
newreminder_handler.register_newreminder_handlers(dp)
readreminders_handler.register_readreminder_handler(dp)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    asyncio.ensure_future(remind_handler.remind(), loop=loop)
    executor.start_polling(dp, on_startup=on_startup, loop=loop)
