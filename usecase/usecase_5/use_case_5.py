import sqlite3

# open the file – use the correct relative/absolute path
with sqlite3.connect("DB2.db") as con:
    cur = con.cursor()

    query = """
    SELECT group_lesson_participates.member_id, group_lesson_participates.date, activity_type.name FROM group_lesson_participates
    JOIN lesson_types ON group_lesson_participates.group_lesson_id = lesson_types.lesson_id
    JOIN activity_type ON lesson_types.activity_type_id = activity_type.id
    JOIN member ON group_lesson_participates.member_id = member.id
    WHERE member.mail LIKE 'johnny@stud.ntnu.no'
    """
    
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(row)

# Får ikke til å sette inn/lese data via data_construction.sql?