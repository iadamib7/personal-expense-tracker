import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
EXPENSES_FILE = os.path.join(DATA_DIR, "expenses.json")

DATE_FORMAT = "%Y-%m-%d"
APP_NAME = "Personal Expense Tracker"

