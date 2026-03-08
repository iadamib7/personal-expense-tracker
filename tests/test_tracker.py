from app import tracker
from app.storage import save_data


def test_add_expense(tmp_path, monkeypatch):
    expenses_file = tmp_path / "expenses.json"
    save_data(str(expenses_file), [])

    monkeypatch.setattr(tracker, "EXPENSES_FILE", str(expenses_file))

    tracker.add_expense("Lunch", 15.0, "Food", "2026-03-08")
    expenses = tracker.view_expenses()

    assert len(expenses) == 1
    assert expenses[0]["title"] == "Lunch"
    assert expenses[0]["amount"] == 15.0
    assert expenses[0]["category"] == "Food"
    assert expenses[0]["expense_date"] == "2026-03-08"


def test_filter_expenses_by_category(tmp_path, monkeypatch):
    expenses_file = tmp_path / "expenses.json"
    sample_data = [
        {"title": "Lunch", "amount": 15.0, "category": "Food", "expense_date": "2026-03-08"},
        {"title": "Taxi", "amount": 25.0, "category": "Transport", "expense_date": "2026-03-08"},
        {"title": "Dinner", "amount": 18.0, "category": "Food", "expense_date": "2026-03-09"},
    ]

    save_data(str(expenses_file), sample_data)
    monkeypatch.setattr(tracker, "EXPENSES_FILE", str(expenses_file))

    filtered = tracker.filter_expenses_by_category("Food")

    assert len(filtered) == 2
    assert all(expense["category"] == "Food" for expense in filtered)


def test_get_total_spending(tmp_path, monkeypatch):
    expenses_file = tmp_path / "expenses.json"
    sample_data = [
        {"title": "Lunch", "amount": 15.0, "category": "Food", "expense_date": "2026-03-08"},
        {"title": "Taxi", "amount": 25.0, "category": "Transport", "expense_date": "2026-03-08"},
    ]

    save_data(str(expenses_file), sample_data)
    monkeypatch.setattr(tracker, "EXPENSES_FILE", str(expenses_file))

    total = tracker.get_total_spending()

    assert total == 40.0
    