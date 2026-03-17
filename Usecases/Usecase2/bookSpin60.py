import sqlite3

con = sqlite3.connect("DB2.db")
cursor = con.cursor()

# Find member_id
cursor.execute("SELECT id FROM member WHERE mail LIKE 'johnny@stud.ntnu.no'")
member_row = cursor.fetchone()
if not member_row:
    print("User not found")
    con.close()
    exit(1)
member_id = member_row[0]

# Find activity_type_id
cursor.execute("SELECT id FROM activity_type WHERE name LIKE 'Spin60'")
activity_row = cursor.fetchone()
if not activity_row:
    print("Activity not found")
    con.close()
    exit(1)
activity_id = activity_row[0]

# Find group_lesson
cursor.execute("""
SELECT group_lesson.id, group_lesson.capacity
FROM group_lesson
JOIN room ON group_lesson.room_id = room.id
JOIN center ON room.center_id = center.id
JOIN lesson_types ON group_lesson.id = lesson_types.lesson_id
WHERE group_lesson.time LIKE '2025-03-17 18:30' AND center.name LIKE 'Øya treningssenter' AND lesson_types.activity_type_id = ?
""", (activity_id,))

lesson_row = cursor.fetchone()
if not lesson_row:
    print("Training not found")
    con.close()
    exit(1)
lesson_id, capacity = lesson_row

# Check current participants
cursor.execute("SELECT COUNT(*) FROM group_lesson_booking WHERE group_lesson_id = ?", (lesson_id,))
current_count = cursor.fetchone()[0]

if current_count >= capacity:
    print("Training is full")
    con.close()
    exit(1)

# Check if already booked
cursor.execute("SELECT COUNT(*) FROM group_lesson_booking WHERE member_id = ? AND group_lesson_id = ?", (member_id, lesson_id))
if cursor.fetchone()[0] > 0:
    print("Already booked")
    con.close()
    exit(1)

# Insert booking
cursor.execute("INSERT INTO group_lesson_booking (member_id, group_lesson_id, time_booked) VALUES (?, ?, datetime('now'))", (member_id, lesson_id))
con.commit()

print("Booking successful")

con.close()