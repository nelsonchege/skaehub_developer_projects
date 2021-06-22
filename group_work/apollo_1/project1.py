import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print("the sqlite version is"+ sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()
name = input("enter file location and database name at the end")
create_connection(name)