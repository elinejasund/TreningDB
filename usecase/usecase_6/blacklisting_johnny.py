import sqlite3

con = sqlite3.connect('../DB2.db')
cursor = con.cursor()

# Run the SQL file (this performs the INSERTs)
with open("blacklisting_johnny.sql", "r") as f:
    cursor.executescript(f.read())

con.commit()

# Find member id for Johnny
cursor.execute("SELECT id FROM member WHERE mail = ?", ("johnny@stud.ntnu.no",))
row = cursor.fetchone()

if not row:
    print("User not found")
    con.close()
    exit(1)

member_id = row[0]

# Count penalties in the last 30 days
cursor.execute("""
    SELECT COUNT(*)
    FROM penalties
    WHERE member_id = ?
    AND date >= datetime('now', '-30 days')
""", (member_id,))

penalty_count = cursor.fetchone()[0]

if penalty_count >= 3:
    print("User is blacklisted from booking for 30 days.")
else:
    print("User is not blacklisted.")

con.close()