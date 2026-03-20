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

    start_date = date.fromisocalendar(2026, week, weekday.value)  # (year, week, day of week)
    start_datetime = datetime(start_date.year, start_date.month, start_date.day)

    end_date = date.fromisocalendar(2026, week + 1, Weekday.MONDAY.value)
    end_datetime = datetime(end_date.year, end_date.month, end_date.day)

    # Assumes that group lesson is the table of interest

    with sqlite3.connect("DB2.db") as con:
        cur = con.cursor()
        query = """
        SELECT name, time
        FROM group_lesson
        JOIN lesson_types ON group_lesson.id = lesson_types.lesson_id
        JOIN activity_type ON lesson_types.activity_type_id = activity_type.id
        WHERE time BETWEEN ? AND ?
        ORDER BY time
        """
        cur.execute(query, (start_datetime, end_datetime))

        # To get a prettier output:
        rows = cur.fetchall()
        for row in rows:
            print("Gruppetime: "+row[0] + "       " + "Tid: " + row[1])

# Assumes that the task asks for the schedule of the 12th week of 2026, starting on the input day

getWeeklySchedule("monday", 12)