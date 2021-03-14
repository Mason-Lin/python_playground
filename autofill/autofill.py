import csv
import sys
import time
from pathlib import Path

try:
    import win32com.client as comctl
except ImportError:
    print("please: pip install pywin32")
    sys.exit(1)

csv_content = """account,name,salary
0000123, Tom, 10000
0000456, Marry, 15000
0000789, Jack, 20000
"""


def create_dummy_salary():
    csv_file = Path("salary.csv").resolve()
    if not csv_file.exists():
        csv_file.write_text(csv_content)
    return csv_file


def get_employees(csv_file_path) -> list:
    employees = []
    with open(csv_file_path, newline="") as csv_file:
        reader = csv.DictReader(csv_file, delimiter=",")
        for row in reader:
            employees.append(row)
    return employees


def enter_employees_data(employees):
    JUMP_TO_NEXT = "{TAB}"  # you can use {ENTER} or {RIGHT} as well
    wsh = comctl.Dispatch("WScript.Shell")
    for employee in employees:
        account = employee["account"]
        name = employee["name"]
        salary = employee["salary"]
        wsh.SendKeys(f"{account}{JUMP_TO_NEXT}")
        wsh.SendKeys(f"{name}{JUMP_TO_NEXT}")
        wsh.SendKeys(f"{salary}{JUMP_TO_NEXT}")


def countdown(seconds=3):
    for i in range(seconds, 0, -1):
        print(f"Starting...{i}")
        time.sleep(1)


csv_file_path = create_dummy_salary()
employees = get_employees(csv_file_path)
print("employees:", employees)
countdown(3)
enter_employees_data(employees)
