import subprocess
import sys
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

USECASES = {
    "1": "usecase/usecase_1/data_construction.sql",
    "2": "usecase/usecase_2/book_spin60.py",
    "3": "usecase/usecase_3/johnny_spin60_registration.py",
    "4": "usecase/usecase_4/usecase_4.py",
    "5": "usecase/usecase_5/usecase_5.py",
    "6": "usecase/usecase_6/blacklisting_johnny.py",
    "7": "usecase/usecase_7/attender.py",
    "8": "usecase/usecase_8/usecase_8.py",
}


def run_sql_file(path):
    sql_file = os.path.join(BASE_DIR, path)
    if not os.path.exists(sql_file):
        print(f"[ERROR] SQL file not found: {sql_file}")
        return

    print(f"Running SQL file: {sql_file}")
    import sqlite3

    db_path = os.path.join(BASE_DIR, "DB2.db")
    if not os.path.exists(db_path):
        print(f"[ERROR] Database file not found: {db_path}")
        return

    with open(sql_file, "r", encoding="utf-8") as f:
        sql = f.read()

    con = sqlite3.connect(db_path)
    cur = con.cursor()
    try:
        cur.executescript(sql)
        con.commit()
        print("SQL script executed successfully.")
    except sqlite3.Error as e:
        print("SQL execution error:", e)
    finally:
        con.close()


def run_python_file(path):
    script = os.path.join(BASE_DIR, path)
    if not os.path.exists(script):
        print(f"[ERROR] Python file not found: {script}")
        return

    print(f"Running Python file: {script}")
    result = subprocess.run([sys.executable, script], cwd=BASE_DIR)
    if result.returncode != 0:
        print(f"Python script exited with non-zero status {result.returncode}")


def show_menu():
    print("""
===== Usecase Interface =====
Choose a usecase (1-8) to run:
1. Insert base data (SQL)
2. Spin60 booking (Python)
3. Johnny attendance registration (Python)
4. Weekly schedule (Python)
5. Johnny history (Python)
6. Blacklisting (Python)
7. Top attendees in month (Python)
8. Joint training pair analysis (Python)
q. Quit
""")


def main():
    while True:
        show_menu()
        choice = input("Select case: ").strip().lower()
        if choice == "q":
            print("Goodbye")
            break

        path = USECASES.get(choice)
        if not path:
            print("Invalid choice, try again.")
            continue

        if path.endswith(".sql"):
            run_sql_file(path)
        elif path.endswith(".py"):
            run_python_file(path)
        else:
            print("Unknown file type for use case")

        input("Press Enter to return to menu...")


if __name__ == "__main__":
    main()
