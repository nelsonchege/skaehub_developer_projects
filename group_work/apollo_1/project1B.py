# Import sqlite3 module
import sqlite3
from sqlite3 import Error
#Create the database
try:
    Create = sqlite3.connect('example2.db')
    print("\nDatabase created and connected to SQLite.")
    Table = Create.cursor()
    # Create table
    Table.execute('''CREATE TABLE stocks
                   (date text, trans text, symbol text, qty real, price real)''')
    # Insert a row of data
    Table.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")
    # Create a query to request for version
    sqlite_select_Query = "select sqlite_version();"
    Table.execute(sqlite_select_Query)
    record = Table.fetchall()
    print("\nSQLite Database Version is: ", record)
except Error as e:
      print(e)
finally:
    if Create:
        Create.close()

