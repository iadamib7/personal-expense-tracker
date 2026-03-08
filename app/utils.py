from datetime import datetime
from app.config import DATE_FORMAT


def is_valid_date(date_string: str) -> bool:
    try:
        datetime.strptime(date_string, DATE_FORMAT)
        return True
    except ValueError:
        return False


def is_valid_amount(value: str) -> bool:
    try:
        amount = float(value)
        return amount > 0
    except ValueError:
        return False
    