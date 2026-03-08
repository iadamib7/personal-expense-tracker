from app.models import Expense


def test_expense_to_dict():
    expense = Expense(
        title="Lunch",
        amount=12.5,
        category="Food",
        expense_date="2026-03-08"
    )

    result = expense.to_dict()

    assert result["title"] == "Lunch"
    assert result["amount"] == 12.5
    assert result["category"] == "Food"
    assert result["expense_date"] == "2026-03-08"
    