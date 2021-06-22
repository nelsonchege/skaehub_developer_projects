import sqlite3
try:
    con = sqlite3.connect('Apollo2.db')
    cur = con.cursor()
    # create table
    cur.execute('''CREATE TABLE name(name, age)''')
    # insert Row of Data
    cur.execute("INSERT into name VALUES('Caroline', '16')")
    print("the sqlite version is" + sqlite3.version)
except sqlite3.Error as error:
    print("\nError while connecting to sqlite", error)
finally:
    if con:
        con.close()
        print("\nThe SQLite connection is closed.")