from app import reports
from app.storage import save_data


def test_get_category_summary(tmp_path, monkeypatch):
    expenses_file = tmp_path / "expenses.json"
    sample_data = [
        {"title": "Lunch", "amount": 15.0, "category": "Food", "expense_date": "2026-03-08"},
        {"title": "Dinner", "amount": 20.0, "category": "Food", "expense_date": "2026-03-09"},
        {"title": "Taxi", "amount": 25.0, "category": "Transport", "expense_date": "2026-03-09"},
    ]

    save_data(str(expenses_file), sample_data)
    monkeypatch.setattr(reports, "EXPENSES_FILE", str(expenses_file))

    summary = reports.get_category_summary()

    assert summary["Food"] == 35.0
    assert summary["Transport"] == 25.0


def test_get_monthly_summary(tmp_path, monkeypatch):
    expenses_file = tmp_path / "expenses.json"
    sample_data = [
        {"title": "Lunch", "amount": 15.0, "category": "Food", "expense_date": "2026-03-08"},
        {"title": "Dinner", "amount": 20.0, "category": "Food", "expense_date": "2026-03-09"},
        {"title": "Book", "amount": 30.0, "category": "School", "expense_date": "2026-04-01"},
    ]

    save_data(str(expenses_file), sample_data)
    monkeypatch.setattr(reports, "EXPENSES_FILE", str(expenses_file))

    summary = reports.get_monthly_summary()

    assert summary["2026-03"] == 35.0
    assert summary["2026-04"] == 30.0
    