import sqlite3
from aiogram.dispatcher import FSMContext

def sql_start():
    global cur, conn
    conn = sqlite3.connect("reminders.db")
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS reminders(
                reminder TEXT,
                reminder_time TEXT,
                reminder_date TEXT,
                userid TEXT,
                reminder_id INT);        
                """)
    conn.commit()

#добавление напоминания в машине состояний
async def sql_add_command(state : FSMContext):
    async with state.proxy() as data:
        cur.execute("INSERT INTO reminders VALUES (?, ?, ?, ?, ?)", tuple(data.values()))
        conn.commit()
#удаление записи из бд
def sql_delete_command_where_id(id):
    conn = sqlite3.connect("reminders.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM reminders WHERE reminder_id=?", [id])
    conn.commit()

#поиск даты в бд
def sql_fetchall_where_date(date):
    conn = sqlite3.connect("reminders.db")
    cur = conn.cursor()
    cur.execute('SELECT * FROM reminders WHERE reminder_date=?', [date])
    reminders = cur.fetchall()
    return reminders

#поиск даты в бд
def sql_fetchall_where_userid(userid):
    conn = sqlite3.connect("reminders.db")
    cur = conn.cursor()
    cur.execute('SELECT * FROM reminders WHERE userid=?', [userid])
    reminders = cur.fetchall()
    return reminders

