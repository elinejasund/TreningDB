import sqlite3
import os

def execute_file(path):
    base_path = os.path.dirname(os.path.dirname(__file__))
    
    db_path = os.path.join(base_path, "DB2.db")

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    with open(path, "r", encoding="utf-8") as fil:
        sql = fil.read()

    cursor.executescript(sql)

    conn.commit()
    conn.close()

    print(f"Added tables to database at")

execute_file("table_construction/table_construction.sql")
