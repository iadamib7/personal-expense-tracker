# Personal Expense Tracker

# Personal Expense Tracker

A beginner Python project for tracking personal expenses using JSON storage.

## Features
- Add expenses
- View all expenses
- Filter by category
- Show total spending
- Generate expense reports

## Project Structure
- `app/models.py` -> expense data model
- `app/storage.py` -> save/load JSON data
- `app/tracker.py` -> expense logic
- `app/reports.py` -> summaries and reports
- `app/main.py` -> command-line interface
- `tests/` -> unit tests
- `data/expenses.json` -> stored expense data

## How to Run

```bash
python -m app.main
