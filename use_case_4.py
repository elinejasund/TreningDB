import sqlite3

# opens the file
def getWeeklySchedule():
    with sqlite3.connect("DB2.db") as con:
        cur = con.cursor()
        query = """
        SELECT *
        FROM group_lesson
        WHERE time BETWEEN ? AND ?
        ORDER BY time
        """
        cur.execute(query, ("2025-03-16", "2025-03-23"))
        # To get a prettier output:
        rows = cur.fetchall()
        for row in rows:
            print(row)

getWeeklySchedule()