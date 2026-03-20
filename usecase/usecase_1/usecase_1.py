import sqlite3
import os

def execute_file(path):
    base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
    
    db_path = os.path.join(base_path, 'TreningDB.db')

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    with open(path, 'r', encoding='utf-8') as fil:
        sql = fil.read()

    cursor.executescript(sql)

    conn.commit()
    conn.close()

    print(f'Data er lagt inn i databasen.')

execute_file('usecase/usecase_1/usecase_1.sql')