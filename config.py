from main import *
from all_array import *
import sqlite3
def database():
    db = sqlite3.connect('server.db')
    sql = db.cursor()
    sql.execute("""CREATE TABLE IF NOT EXISTS aboutCoin (
        name TEXT,
        data TEXT,
        price BIGINT
    )""")
    db.commit()
    sql.execute("SELECT name FROM aboutCoin")
    if sql.fetchone() is None:
        sql.execute(f"INSERT INTO users VALUES (?, ?, ?)", (nameCoin, dataCoin, priceCoin))
        db.commit()
    else:
        print("Пішов нахуй")
    for value in sql.execute("SELECT * FROM aboutCoin"):
        print(value)
