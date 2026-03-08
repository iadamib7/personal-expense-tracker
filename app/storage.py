import json
import os

from app.config import DATA_DIR, EXPENSES_FILE


def ensure_data_file() -> None:
    os.makedirs(DATA_DIR, exist_ok=True)

    if not os.path.exists(EXPENSES_FILE):
        with open(EXPENSES_FILE, "w", encoding="utf-8") as file:
            json.dump([], file)


def load_data(file_path: str) -> list:
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_data(file_path: str, data: list) -> None:
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)
        
