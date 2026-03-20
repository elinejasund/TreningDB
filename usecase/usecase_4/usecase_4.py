from datetime import date, datetime
import sqlite3
from enum import Enum
import sys

mapping = {
    "mandag": "MONDAY",
    "tirsdag": "TUESDAY",
    "onsdag": "WEDNESDAY",
    "torsdag": "THURSDAY",
    "fredag": "FRIDAY",
    "lørdag": "SATURDAY",
    "søndag": "SUNDAY"
}

class Weekday(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7

# opens the file
def getWeeklySchedule(start_day: int | str, week: int):
    start_day_no = start_day
    start_day = mapping.get(start_day.lower(), start_day)
    weekday = Weekday(start_day) if isinstance(start_day, int) else Weekday[start_day.upper()]

    start_date = date.fromisocalendar(2026, week, weekday.value)  # (year, week, day of week)
    start_datetime = datetime(start_date.year, start_date.month, start_date.day)

    end_date = date.fromisocalendar(2026, week + 1, Weekday.MONDAY.value)
    end_datetime = datetime(end_date.year, end_date.month, end_date.day)

    # Assumes that group lesson is the table of interest, not visits

    with sqlite3.connect("TreningDB.db") as con:
        cur = con.cursor()
        query = """
        SELECT name, time
        FROM group_lesson
        JOIN lesson_types ON group_lesson.id = lesson_types.lesson_id
        JOIN activity_type ON lesson_types.activity_type_id = activity_type.id
        WHERE time BETWEEN ? AND ?
        ORDER BY time
        """
        cur.execute(query, (
        # AI GEN: (line 51-52)
        start_datetime.strftime("%Y-%m-%d %H:%M:%S"),
        end_datetime.strftime("%Y-%m-%d %H:%M:%S")))

        # To get a prettier output:
        rows = cur.fetchall()
        if len(rows) == 0:
            print("Ingen gruppetimer i dette tidsintervallet.")
            return
        
        print(f"Timeplan for uke 12 f.o.m. {start_day_no}:")
        for row in rows:
            print("Gruppetime: "+row[0] + "       " + "Tid: " + row[1])

if __name__ == "__main__":
    start_day = sys.argv[1]
    week = int(sys.argv[2])

    getWeeklySchedule(start_day, week)