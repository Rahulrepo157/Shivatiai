import sqlite3

def init_db():
    conn = sqlite3.connect('database.db')
    print("Opened database successfully")

    conn.execute('CREATE TABLE IF NOT EXISTS requests (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, email TEXT, product TEXT, message TEXT)')
    print("Table created successfully")
    conn.close()

if __name__ == '__main__':
    init_db()