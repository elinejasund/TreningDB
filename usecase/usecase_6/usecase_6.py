import sqlite3

con = sqlite3.connect('DB2.db')
cursor = con.cursor()

def is_blacklisted(member_id):
    cursor.execute("""
        SELECT COUNT(*)
        FROM penalties
        WHERE member_id = ?
        AND date >= datetime('now', '-30 days')
    """, (member_id,))
    penalty_count = cursor.fetchone()[0]
    return penalty_count >= 3

cursor.execute("SELECT id FROM member WHERE mail = ?", ("johnny@stud.ntnu.no",))
row = cursor.fetchone()

if not row:
    print("Bruker ikke funnet")
    con.close()
    exit(1)

member_id = row[0]

# General check to see blacklisted status
if is_blacklisted(member_id):
    print("Brukeren er svartelistet fra booking for 30 dager.")
else:
    print("Brukeren er ikke svartelistet.")

# Check to attempt joining group lesson and see if
# blacklist status is accounted for. Assuming lesson_id = 2 to test.
lesson_id = 2
if is_blacklisted(member_id):
    print("Påmelding nektet: bruker er svartelistet.")
else:
    cursor.execute("""
        INSERT OR IGNORE INTO group_lesson_booking (member_id, group_lesson_id, time_booked)
        VALUES (?, ?, datetime('now'))
    """, (member_id, lesson_id))
    print("Påmelding vellykket!")

con.commit()
con.close()