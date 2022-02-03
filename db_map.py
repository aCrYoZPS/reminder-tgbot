import sqlite3
import time
conn = sqlite3.connect('reminders.db')
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS reminders(
            id INT PRIMARY KEY,
            reminder TEXT,
            reminder_time TEXT,
            reminder_date TEXT,
            userid TEXT);        
            """)
conn.commit();
datetime = time.localtime()
date = str(datetime[2]) + '.' + str(datetime[1])
cur.execute(f"SELECT * FROM reminders WHERE reminder_date is {date}")
reminders_list = cur.fetchall()
print(reminders_list)
if reminders_list == []:
    print('yea')
