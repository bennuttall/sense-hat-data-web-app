import os
import sqlite3 as sqlite
from sense_hat import SenseHat
from datetime import datetime

db_path='/home/pi/.config/sensedata.db'

path = '/'.join(db_path.split('/')[:-1])
filename = db_path.split('/')[:-1]

if not os.path.exists(path):
    os.makedirs(path)

db = sqlite.connect(db_path, check_same_thread=False)
cursor = db.cursor()

def create_table():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS
            sensedata (
                datetime TEXT,
                temperature REAL,
                humidity REAL
            )
    """)
    db.commit()

def record_data():
    sense = SenseHat()

    d = get_timestamp()
    t = sense.temperature
    h = sense.humidity
    values = (d, t, h)

    cursor.execute("""
        INSERT INTO
            sensedata
        VALUES
            (?, ?, ?)
    """, values)
    db.commit()

def get_timestamp():
    dt = datetime.now()
    dt_date = str(dt.date())
    dt_time = str(dt.time())
    timestamp = "%s %s" % (dt_date, dt_time[:8])
    return timestamp

def retreive_data():
    cursor.execute("""
        SELECT
            *
        FROM
            sensedata
        ORDER BY
            datetime(datetime) DESC
        LIMIT
            0, 1
    """)
    result = cursor.fetchone()
    if not result:
        return None

    return result

def main():
    create_table()
    record_data()

if __name__ == '__main__':
    main()
