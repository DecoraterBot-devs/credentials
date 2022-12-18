"""
Creates a database from sql script files.
"""
import sqlite3


def create_database(db_name):
    conn = sqlite3.connect(db_name)
    with open('Tables/Credentials.sql') as f:
        conn.executescript(f.read())
    with open('Tables/DefaultCogs.sql') as f:
        conn.executescript(f.read())
    with open('Data/Credentials.sql') as f:
        conn.executescript(f.read())
    with open('Data/DefaultCogs.sql') as f:
        conn.executescript(f.read())
    conn.commit()
    conn.close()


create_database('credentials.db')
