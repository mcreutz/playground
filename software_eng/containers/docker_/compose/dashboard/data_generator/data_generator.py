import time
import random
import signal
import sys
import os

import psycopg2

abort = False


def signal_handler(sig, frame):
    print("Exiting gracefully.")
    global abort
    abort = True
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)
print("Press Ctrl+C to abort.")

# Establish db connection
DB_HOST = os.environ['DB_HOST']
DB_PORT = os.environ['DB_PORT']
DB_NAME = os.environ['DB_NAME']
POSTGRES_USER = os.environ['POSTGRES_USER']
POSTGRES_PASSWORD = os.environ['POSTGRES_PASSWORD']

con = psycopg2.connect(database=DB_NAME, user=POSTGRES_USER,
                       password=POSTGRES_PASSWORD, host=DB_HOST, port=DB_PORT)
cur = con.cursor()

# Create table, if not exists
cur.execute("""CREATE TABLE IF NOT EXISTS motor_temps (
        ts timestamp,
        m01_temp REAL,
        m02_temp REAL,
        m03_temp REAL,
        PRIMARY KEY(ts)
        );""")
con.commit()

while not abort:
    # Insert random data
    cur.execute(f"""INSERT INTO motor_temps (
            ts, m01_temp, m02_temp, m03_temp) 
            VALUES (
                current_timestamp,
                {10 + (random.random() * 2)},
                {20 + (random.random() * 4)},
                {40 + (random.random() * 8)}
            );""")

    # Delete old data
    cur.execute("""delete from motor_temps 
            where ts < now() - interval '3 minutes'""")

    con.commit()

    # Wait interval
    print(".", end="")
    time.sleep(0.1)

# Close connection
con.close()
