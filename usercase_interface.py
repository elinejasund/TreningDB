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


def prompt_yes_no(message, default="y"):
    valid = {"y": True, "n": False}
    prompt = f"{message} [{'Y/n' if default.lower() == 'y' else 'y/N'}]: "
    while True:
        answer = input(prompt).strip().lower()
        if not answer:
            answer = default.lower()
        if answer in valid:
            return valid[answer]
        print("Vennligst svar 'y' eller 'n'.")


def run_sql_file(path):
    sql_file = os.path.join(BASE_DIR, path)
    if not os.path.exists(sql_file):
        print(f"ERROR: SQL fil ikke funnet: {sql_file}")
        return
    print(f"Kjører SQL fil: {sql_file}")
    import sqlite3
    db_path = os.path.join(BASE_DIR, 'DB2.db')
    if not os.path.exists(db_path):
        print(f"ERROR: Database fil ikke funnet: {db_path}")
        return

    with open(sql_file, "r", encoding="utf-8") as f:
        sql = f.read()

    con = sqlite3.connect(db_path)
    cur = con.cursor()
    try:
        cur.executescript(sql)
        con.commit()
        print("SQL ble kjørt uten feil.")
    except sqlite3.Error as e:
        print("SQL kjørefeil:", e)
    finally:
        con.close()


def run_python_file(path, args=None):
    script = os.path.join(BASE_DIR, path)
    if not os.path.exists(script):
        print(f"ERROR: Python fil ikke funnet: {script}")
        return

    cmd = [sys.executable, script]
    if args:
        cmd.extend(args)

    print(f"Kjører Python file: {script}")
    result = subprocess.run(cmd, cwd=BASE_DIR)
    if result.returncode != 0:
        print(f"Python script exited med non-zero status {result.returncode}")
    else:
        print("Python ble kjørt uten feil.")


def usecase_1():
    print("Usecase 1: Sett in basedata (treningssenter, saler, sykler, brukere, trenere, treninger) via SQL.")
    if prompt_yes_no("Ønsker du å kjøre den initiale SQL data inserten?"):
        run_sql_file(USECASES['1'])
    else:
        return


def usecase_2():
    print('Usecase 2: Booking på Øya treningssenter.')
    user = 'johnny@stud.ntnu.no'
    activity = 'Spin60'
    time = 'tirsdag 17. mars kl.18:30'

    if not prompt_yes_no(f'Ønsker du å booke {activity} time {time} for brukeren {user}?'):
        run_python_file(USECASES['2'])
    else:
        return


def usecase_3():
    print('Usecase 3: Registrer oppmøte for treningsøkten.')
    user = 'johnny@stud.ntnu.no'
    training = 'Spin60 tirsdag 17. mars kl.18:30'

    if not prompt_yes_no(f'Ønsker du å registrere oppmøte for {training} for brukeren {user}?'):
        run_python_file(USECASES['3'])
    else:
        return


def usecase_4():
    print('Usecase 4: Ukentlig timeplan for tidsintervall.')
    print('Testdata er lagt inn for uke 12 frem til tirsdag, så det er best å teste med startdag mandag eller tirsdag i uke 12.')
    start_day = input("Startdag (f.eks. mandag): ").strip()
    week = input("Ukenummer (f.eks. 12): ").strip()

    if prompt_yes_no(f"Ønsker du å vise den ukentlige timeplanen for uke {week}, fra {start_day} til søndag"):
        run_python_file(USECASES['4'], args=[start_day, str(week)])
    else:
        return


def usecase_5():
    print('Usecase 5: Bruker sin besøkshistorie query (unique rows).')
    user = input('Brukernavn [johnny@stud.ntnu.no]: ').strip() or 'johnny@stud.ntnu.no'
    since = input('Since dato [2026-01-01]: ').strip() or '2026-01-01'
    print(f"Computing historie for {user} siden {since}")

    if prompt_yes_no('Ønsker du å kjøre brukeren sin besøkshistorie SQL nå?'):
        run_sql_file(USECASES['5'])
    else:
        return


def usecase_6():
    print('Usecase 6: Svarteliste logikk for brukere med 3 prikker i 30 dager.')
    user = "johnny@stud.ntnu.no"
    if prompt_yes_no(f"Vil du svarteliste brukeren {user} nå?"):
        print(f"{user} har blitt svartelistet fra elektronisk booking for 30 dager.")
        if prompt_yes_no('Ønsker du å teste svartelisten ved å prøve en booking?'):
            usecase_2()
    else:
        return


def usecase_7():
    print('Usecase 7: Finn personen som har deltatt i flest felles treningsøkter i en måned.')
    month = input('Måned [2026-03]: ').strip() or '2026-03'
    print(f"Finn personen som har deltatt i flest felles treningsøkter i måned {month}.")
    run_python_file(USECASES['7'])


def usecase_8():
    print('Usecase 8: Analyse på felles treningsøkter og personer som trener sammen.')
    if prompt_yes_no('Ønsker du å kjøre joint training pair analysis SQL nå?'):
        run_python_file(USECASES['8'])
    else:
       return


def show_menu():
    print("""
===== Usecase Interface =====
Choose a usecase (1-8) to run:
1. Insert base data
2. Spin60 booking
3. Registration attendance
4. Weekly schedule
5. Johnny visit history
6. Blacklisting
7. Top session attendees
8. Joint training pair analysis
q. Quit
""")

def main():
    while True:
        show_menu()
        choice = input('Velg case: ').strip().lower()

        match choice:
            case 'q':
                break
            case '1':
                usecase_1()
            case '2':
                usecase_2()
            case '3':
                usecase_3()
            case '4':
                usecase_4()
            case '5':
                usecase_5()
            case '6':
                usecase_6()
            case '7':
                usecase_7()
            case '8':
                usecase_8()
            case _:
                print('Ugyldig input, prøv igjen.')

        input('Trykk "Enter" for å returnere til menyen...')


if __name__ == '__main__':
    main()
