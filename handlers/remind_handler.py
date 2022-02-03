from create_bot import bot
from database import sqlite3_db

import asyncio


async def remind():
    import time
    while True:
        dt = time.localtime()
        if int(dt[4]) < 10:
            mins = '0' + str(dt[4])
            inttimenow = float(dt[3]) + (float(mins) / 1000)
        else:
            mins = str(dt[4])
            inttimenow = float(dt[3]) + (float(mins) / 100)

        if int(dt[1]) < 10:
            months = '0' + str(dt[1])
        else:
            months = str(dt[1])

        date = str(dt[2]) + '.' + months
        timee = str(dt[3]) + ':' + mins
        reminders = sqlite3_db.sql_fetchall_where_date(date)
        # Максимально непонятно, но как есть...
        # item[0] - текст напоминания
        # item[1] - время, на которое запланировано напоминание
        # item[2] - дата, на которую запланировано напоминание
        # item[3] - id пользователя в тг
        # item[4] - id напоминания в бд
        for item in reminders:
            inttimerem = float(item[1][0] + item[1][1]) + (float(item[1][3] + item[1][4]) / 100)
            if str(item[1]) == timee or inttimerem <= inttimenow:
                sqlite3_db.sql_delete_command_where_id(item[4])
                await bot.send_message(int(item[3]), item[0])
        await asyncio.sleep(20)
