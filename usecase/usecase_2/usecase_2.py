import sqlite3

def find_group_lesson(activity: str, time: str, center: str):
     with sqlite3.connect("DB2.db") as con:
        cursor = con.cursor()

        #Find activity_type_id
        cursor.execute("SELECT id FROM activity_type WHERE name = ?", (activity,))
        activity_row = cursor.fetchone()
        if not activity_row:
            print("Treningstype ikke funnet.")
            return
        activity_id = activity_row[0]

        #Find center
        cursor.execute("SELECT id FROM center WHERE name = ?", (center,))
        center_row = cursor.fetchone()
        if not center_row:
            print("Treningssenter ikke funnet.")
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
            print("Gruppetime ikke funnet.")
            return None, None
        lesson_id, capacity = lesson_row

        return lesson_id, capacity

def book_group_lesson(member: str, lesson_id: int, capacity: int):
    with sqlite3.connect("DB2.db") as con:
        cursor = con.cursor()

        # Find member
        cursor.execute("SELECT id FROM member WHERE mail = ?", (member,))
        member_row = cursor.fetchone()
        if not member_row:
            print("Bruker ikke funnet.")
            return
        member_id = member_row[0]

        if not lesson_id:
            print("Gruppetime ikke funnet.")
            return

        # Check current participants
        cursor.execute("SELECT COUNT(*) FROM group_lesson_booking WHERE group_lesson_id = ?", (lesson_id,))
        current_count = cursor.fetchone()[0]

        if current_count >= capacity:
            print("Gruppetimen er full.")
            return

        # Check if already booked
        cursor.execute("SELECT COUNT(*) FROM group_lesson_booking WHERE member_id = ? AND group_lesson_id = ?", (member_id, lesson_id))
        if cursor.fetchone()[0] > 0:
            print("Denne gruppetimen har du allerede booket.")
            return

        # Insert booking
        cursor.execute("INSERT INTO group_lesson_booking (member_id, group_lesson_id, time_booked) VALUES (?, ?, datetime('now'))", (member_id, lesson_id))
        con.commit()

        print("Du har booket nå gruppetimen!")

lesson_id, capacity = find_group_lesson("Spin60", "2026-03-17 18:30", "Øya treningssenter")
book_group_lesson("johnny@stud.ntnu.no", lesson_id, capacity)
