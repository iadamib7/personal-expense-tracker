from app.storage import load_data
from app.config import EXPENSES_FILE


def get_category_summary() -> dict:
    expenses = load_data(EXPENSES_FILE)
    category_totals = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]
        category_totals[category] = category_totals.get(category, 0) + amount

    return category_totals


def get_monthly_summary() -> dict:
    expenses = load_data(EXPENSES_FILE)
    monthly_totals = {}

    for expense in expenses:
        month = expense["expense_date"][:7]
        monthly_totals[month] = monthly_totals.get(month, 0) + expense["amount"]

    return monthly_totals


def print_report() -> None:
    expenses = load_data(EXPENSES_FILE)
    total_spending = sum(expense["amount"] for expense in expenses)
    category_summary = get_category_summary()
    monthly_summary = get_monthly_summary()

    print("\n===== EXPENSE REPORT =====")
    print(f"Total expenses recorded: {len(expenses)}")
    print(f"Total spending: ${total_spending:.2f}")

    print("\nSpending by category:")
    if category_summary:
        for category, amount in category_summary.items():
            print(f"- {category}: ${amount:.2f}")
    else:
        print("No expenses recorded yet.")

    print("\nMonthly spending:")
    if monthly_summary:
        for month, amount in monthly_summary.items():
            print(f"- {month}: ${amount:.2f}")
    else:
        print("No monthly data available.")
        