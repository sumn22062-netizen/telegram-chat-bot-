import sqlite3
from datetime import datetime
DB_NAME="assistant.db"

def init_db():
    conn=sqlite3.connect(DB_NAME)
    cursor=conn.cursor() ## it give control to the data base 
    cursor.execute('''
        create table if not exists expenses(
            id interger primary key autoincrement,
            item_name text not null,
            amount real not null,,
            date TEXT NOT NULL

        )
    ''')


    cursor.execute('''
        create table if not exists notes(
                   id integer primary key autoincrement,
                   summary text not null,
                   date text not null
                   )
''')
    
    conn.commit()## change the date dase permanent
    conn.close()
    print("database table initialized successfully.....")

    def add_expense(item_name:str,amount:float):
        conn=sqlite3.connect(DB_NAME)
        cursor=conn.cursor()
        current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cursor.execute(
            "INSERT INTO expenses (item_name, amount, date) VALUES (?, ?, ?)",
            (item_name, amount, current_date)
        )

    def add_note(summary:str):
        conn=sqlite3.connect(DB_NAME)
        cursor=conn.cursor()
        current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        cursor.execute(
            "insert into notes(summary,date) values(?,?)",
            (summary,current_date)
        )
        conn.commit()
        conn.close()

    
