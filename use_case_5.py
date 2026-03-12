import sqlite3

# open the file – use the correct relative/absolute path
with sqlite3.connect("DB2.db") as con:      # or "../DB2.db" depending on cwd
    cur = con.cursor()
    cur.execute("SELECT * FROM visit WHERE member_id=?", ("11",))
    print(cur.fetchall())

# Why is only one date fetched?