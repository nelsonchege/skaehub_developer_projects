import sqlite3
def sqlite_connect(db_name):
    db_path = "C:/Users/nelson/Desktop/flutter_projects/apollo_1"
    db_file = db_path + db_name
    # The try block lets you test a block of code for errors.
    try:
        sqlite_connection = sqlite3.connect(db_file)
        # Create a query to request for version
        print("Database created SQLite" + db_name + " and Successfully Connected to it")
        print("The SQLite version is" + sqlite3.version)
    # The except block lets you handle the error.
    except sqlite3.Error as error:
        print("Error while connecting to sqlite", error)
    return sqlite_connection
def create_table(sqlite_connection):
    try:
        # sqlite3.Cursor class is an instance which you can use to invoke methods that execute SQLite statements, fetch data from the result sets of the queries.
        cursor = sqlite_connection.cursor()
        cursor.execute('''CREATE TABLE stocks
                (date text, trans text, symbol text, qty real, price real)''')
        print("Successfully created table")
    except sqlite3.Error as error:
        print("Error while creating table", error)
def insert_data(sqlite_connection):
    try:
        cursor = sqlite_connection.cursor()
        # Insert a row of data
        cursor.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")
        cursor.execute("INSERT INTO stocks VALUES ('2007-01-05','SELL','TSLA',100,35.14)")
        print("Successfully inserted data")
    except sqlite3.Error as error:
        print("Error while inserting data", error)
def select_data(sqlite_connection):
    try:
        cursor = sqlite_connection.cursor()
        cursor.execute("SELECT * FROM stocks")
        stocks = cursor.fetchall()
        for row in stocks:
            print(row)
    except sqlite3.Error as error:
        print("Error while selecting data", error)
name = input("Please Enter SQLite DB name: ")
connection = sqlite_connect(name)
create_table(connection)
insert_data(connection)
select_data(connection)
connection.close