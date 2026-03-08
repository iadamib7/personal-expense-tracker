from app.models import Expense
from app.storage import load_data, save_data
from app.config import EXPENSES_FILE


def add_expense(title: str, amount: float, category: str, expense_date: str) -> None:
    expenses = load_data(EXPENSES_FILE)
    new_expense = Expense(
        title=title,
        amount=amount,
        category=category,
        expense_date=expense_date
    )
    expenses.append(new_expense.to_dict())
    save_data(EXPENSES_FILE, expenses)


def view_expenses() -> list:
    return load_data(EXPENSES_FILE)


def filter_expenses_by_category(category: str) -> list:
    expenses = load_data(EXPENSES_FILE)
    return [expense for expense in expenses if expense["category"].lower() == category.lower()]


def get_total_spending() -> float:
    expenses = load_data(EXPENSES_FILE)
    return sum(expense["amount"] for expense in expenses)
