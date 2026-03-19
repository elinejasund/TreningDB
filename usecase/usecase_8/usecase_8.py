import sqlite3
import os

def execute_select(path):
    base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
    db_path = os.path.join(base_path, "DB2.db")

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    with open(path, "r", encoding="utf-8") as fil:
        sql = fil.read().strip()

    cursor.execute(sql)
    results = cursor.fetchall()

    # Print results nicely
    for row in results:
        print(f"Member1: {row[0]} Member2: {row[1]} Amount: {row[2]}")

    conn.close()

execute_select("usecase/usecase_8/use_case_8.sql")