import sqlite3

def find_group_lesson(activity: str, time: str, center: str):
     with sqlite3.connect("DB2.db") as con:
        cursor = con.cursor()

        #Find activity_type_id
        cursor.execute("SELECT id FROM activity_type WHERE name = ?", (activity,))
        activity_row = cursor.fetchone()
        if not activity_row:
            print("Activity not found")
            return
        activity_id = activity_row[0]

        #Find center
        cursor.execute("SELECT id FROM center WHERE name = ?", (center,))
        center_row = cursor.fetchone()
        if not center_row:
            print("Center not found")
            return
        center_id = center_row[0]

        # Find group_lesson
        cursor.execute("""
        SELECT group_lesson.id, group_lesson.capacity
        FROM group_lesson
        JOIN room ON group_lesson.room_id = room.id
        JOIN center ON room.center_id = center.id
        JOIN lesson_types ON group_lesson.id = lesson_types.lesson_id
        WHERE group_lesson.time = ? AND center.id = ? AND lesson_types.activity_type_id = ?
        """, (time, center_id, activity_id))

        lesson_row = cursor.fetchone()
        if not lesson_row:
            print("Lesson not found")
            return None
        lesson_id, capacity = lesson_row

        return lesson_id

def registration_group_lesson(member: str, lesson: int):
    with sqlite3.connect("DB2.db") as con:
        cursor = con.cursor()

        # Find member_id
        cursor.execute("SELECT id FROM member WHERE mail = ?", (member,))
        member_row = cursor.fetchone()
        if not member_row:
            print("User not found")
            return
        member_id = member_row[0]

        if not lesson:
            print("Lesson not found")
            return None

        # Check if already registered
        cursor.execute("SELECT COUNT(*) FROM group_lesson_participates WHERE member_id = ? AND group_lesson_id = ?", (member_id, lesson))
        if cursor.fetchone()[0] > 0:
            print("Already registered")
            return

        # Insert registration
        cursor.execute("INSERT INTO group_lesson_participates (member_id, group_lesson_id, date) VALUES (?, ?, datetime('now'))", (member_id, lesson))
        con.commit()

        print("Registration successful")

lesson = find_group_lesson("Spin60", "2026-03-17 18:30", "Øya treningssenter");
registration_group_lesson("johnny@stud.ntnu.no", lesson);