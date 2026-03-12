from datetime import date, datetime
import sqlite3
from enum import Enum

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
    weekday = Weekday(start_day) if isinstance(start_day, int) else Weekday[start_day.upper()]

    start_date = date.fromisocalendar(2025, week, weekday.value)  # (year, week, day of week)
    start_datetime = datetime(start_date.year, start_date.month, start_date.day)

    end_date = date.fromisocalendar(2025, week + 1, Weekday.MONDAY.value)
    end_datetime = datetime(end_date.year, end_date.month, end_date.day)

    print(start_datetime)
    print(end_datetime)

    with sqlite3.connect("DB2.db") as con:
        cur = con.cursor()
        query = """
        SELECT time
        FROM group_lesson
        WHERE time BETWEEN ? AND ?
        ORDER BY time
        """
        cur.execute(query, (datetime(2025,1,1), datetime(2026,1,1)))

        # To get a prettier output:
        rows = cur.fetchall()
        for row in rows:
            print(row[0])

getWeeklySchedule("monday", 12)