import sqlite3

con = sqlite3.connect('../DB2.db')
cursor = con.cursor()

# Run the SQL file (this performs the INSERTs)
with open("attender.sql", "r") as f:
    cursor.executescript(f.read())

con.commit()

# Parameter month
month = "2026-03"

cursor.execute("""
    WITH attendance AS (
        SELECT member_id, COUNT(*) AS total_attendances
        FROM group_lesson_participates
        WHERE strftime('%Y-%m', date) = ?
        GROUP BY member_id
    ),
    max_attendance AS (
        SELECT MAX(total_attendances) AS max_number
        FROM attendance
    )
    SELECT member.name, member.mail, attendance.total_attendances
    FROM attendance
    JOIN member ON attendance.member_id = member.id
    WHERE attendance.total_attendances = (SELECT max_number FROM max_attendance);
    """, (month,))

rows = cursor.fetchall()

if not rows:
    print("No group lessons were attended this month.")
else:
    print(f"Members with most attendances in {month}:")
    for name, mail, total_attendances in rows:
        print(f"{name} ({mail}) - {total_attendances} attendances")

con.close()