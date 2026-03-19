import sqlite3
import os

con = sqlite3.connect('DB2.db')
cursor = con.cursor()

base = os.path.dirname(os.path.abspath(__file__))
sql_path = os.path.join(base, "blacklisting_johnny.sql")

with open(sql_path, "r") as f:
    cursor.executescript(f.read())

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
    print("User not found")
    con.close()
    exit(1)

member_id = row[0]

# General check to see blacklisted status
if is_blacklisted(member_id):
    print("User is blacklisted from booking for 30 days.")
else:
    print("User is not blacklisted.")

# Check to attempt joining group lesson and see if
# blacklist status is accounted for. Assuming lesson_id = 1 to test.
lesson_id = 1
if is_blacklisted(member_id):
    print("Sign-up denied: user is blacklisted.")
else:
    cursor.execute("""
        INSERT INTO group_lesson_signups (member_id, lesson_id, signup_time)
        VALUES (?, ?, datetime('now'))
    """, (member_id, lesson_id))
    print("Sign-up successful!")

con.commit()
con.close()