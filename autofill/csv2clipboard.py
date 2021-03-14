import csv
import sys
import time
from pathlib import Path

try:
    import win32clipboard
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


def countdown(seconds=3):
    for i in range(seconds, 0, -1):
        print(f"Starting...{i}")
        time.sleep(1)


def get_paste_buffer():
    win32clipboard.OpenClipboard(0)
    try:
        result = win32clipboard.GetClipboardData()
    except TypeError:
        result = ""  # non-text
    win32clipboard.CloseClipboard()
    return result


def set_paste_buffer(text):
    win32clipboard.OpenClipboard(0)
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardText(text, win32clipboard.CF_UNICODETEXT)
    win32clipboard.CloseClipboard()


def copy_employees_data(employees):
    for employee in employees:
        account = employee["account"]
        name = employee["name"]
        salary = employee["salary"]
        set_paste_buffer(account)
        print(get_paste_buffer())


csv_file_path = create_dummy_salary()
employees = get_employees(csv_file_path)
print("employees:", employees)
countdown(3)
copy_employees_data(employees)
