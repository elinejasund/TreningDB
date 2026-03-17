import sqlite3

# open the file – use the correct relative/absolute path
with sqlite3.connect("DB2.db") as con:      # or "../DB2.db" depending on cwd
    cur = con.cursor()
    cur.execute("SELECT * FROM member WHERE mail LIKE 'johnny@stud.ntnu.no'")
    member_row = cur.fetchone()
    if not member_row:
        print("User not found")
        con.close()
        exit(1)
    johnny_id = member_row[0]

    # Må hente fra group_lesson participates, for å kunne hente ut hvilken gruppetime han har vært med på
    # cur.execute("SELECT member FROM visit WHERE member_id = ?", (johnny_id,))

    print(member_row)
