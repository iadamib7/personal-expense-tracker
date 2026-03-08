from app.config import APP_NAME
from app.storage import ensure_data_file
from app.tracker import (
    add_expense,
    view_expenses,
    filter_expenses_by_category,
    get_total_spending
)
from app.reports import print_report
from app.utils import is_valid_date, is_valid_amount


def show_menu() -> None:
    print(f"\n===== {APP_NAME} =====")
    print("1. Add expense")
    print("2. View all expenses")
    print("3. Filter expenses by category")
    print("4. Show total spending")
    print("5. Show expense report")
    print("6. Exit")


def get_valid_date_input(prompt: str) -> str:
    while True:
        date_input = input(prompt).strip()
        if is_valid_date(date_input):
            return date_input
        print("Invalid date format. Use YYYY-MM-DD.")


def get_valid_amount_input(prompt: str) -> float:
    while True:
        amount_input = input(prompt).strip()
        if is_valid_amount(amount_input):
            return float(amount_input)
        print("Invalid amount. Enter a positive number.")


def handle_add_expense() -> None:
    print("\n--- Add Expense ---")
    title = input("Enter expense title: ").strip()
    category = input("Enter category: ").strip()
    amount = get_valid_amount_input("Enter amount: ")
    expense_date = get_valid_date_input("Enter expense date (YYYY-MM-DD): ")

    add_expense(title, amount, category, expense_date)
    print("Expense added successfully.")


def handle_view_expenses() -> None:
    print("\n--- All Expenses ---")
    expenses = view_expenses()

    if not expenses:
        print("No expenses found.")
        return

    for index, expense in enumerate(expenses, start=1):
        print(
            f"{index}. {expense['title']} | "
            f"${expense['amount']:.2f} | "
            f"{expense['category']} | "
            f"{expense['expense_date']}"
        )


def handle_filter_by_category() -> None:
    print("\n--- Filter by Category ---")
    category = input("Enter category: ").strip()
    filtered_expenses = filter_expenses_by_category(category)

    if not filtered_expenses:
        print("No expenses found for that category.")
        return

    for index, expense in enumerate(filtered_expenses, start=1):
        print(
            f"{index}. {expense['title']} | "
            f"${expense['amount']:.2f} | "
            f"{expense['category']} | "
            f"{expense['expense_date']}"
        )


def handle_total_spending() -> None:
    total = get_total_spending()
    print(f"\nTotal spending: ${total:.2f}")


def main() -> None:
    ensure_data_file()

    while True:
        show_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            handle_add_expense()
        elif choice == "2":
            handle_view_expenses()
        elif choice == "3":
            handle_filter_by_category()
        elif choice == "4":
            handle_total_spending()
        elif choice == "5":
            print_report()
        elif choice == "6":
            print("Goodbye.")
            break
        else:
            print("Invalid choice. Please select from 1 to 6.")


if __name__ == "__main__":
    main()
    