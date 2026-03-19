import sqlite3

con = sqlite3.connect("../DB2.db")
cursor = con.cursor()

cursor.execute("SELECT * FROM member")
rows = cursor.fetchall()

print(rows)

con.close()