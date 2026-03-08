import json
from app import storage


def test_ensure_data_file_creates_file(tmp_path, monkeypatch):
    data_dir = tmp_path / "data"
    expenses_file = data_dir / "expenses.json"

    monkeypatch.setattr(storage, "DATA_DIR", str(data_dir))
    monkeypatch.setattr(storage, "EXPENSES_FILE", str(expenses_file))

    storage.ensure_data_file()

    assert data_dir.exists()
    assert expenses_file.exists()
    assert json.loads(expenses_file.read_text(encoding="utf-8")) == []


def test_load_data_returns_empty_list_for_missing_file(tmp_path):
    missing_file = tmp_path / "missing.json"
    result = storage.load_data(str(missing_file))
    assert result == []


def test_save_and_load_data(tmp_path):
    test_file = tmp_path / "expenses.json"
    sample_data = [
        {
            "title": "Groceries",
            "amount": 20.0,
            "category": "Food",
            "expense_date": "2026-03-08"
        }
    ]

    storage.save_data(str(test_file), sample_data)
    loaded_data = storage.load_data(str(test_file))

    assert loaded_data == sample_data


def test_load_data_returns_empty_list_for_bad_json(tmp_path):
    bad_file = tmp_path / "bad.json"
    bad_file.write_text("{bad json", encoding="utf-8")

    result = storage.load_data(str(bad_file))

    assert result == []
    