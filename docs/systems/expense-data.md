# Expense data module

`scripts/expense_data.py` is the shared library for reading and classifying expenses.

## Why it exists

Both `monthly_summary.py` and `expense_dashboard.py` need the same parsing rules and [budget month](../rules/budget-month.md) logic. Centralizing avoids drift.

## `Expense` record

Each CSV row becomes a frozen dataclass:

| Field | Type | Notes |
|-------|------|-------|
| `date` | `datetime` | Parsed from `YYYY-MM-DD` |
| `category` | `str` | Required |
| `description` | `str` | May be empty |
| `amount` | `Decimal` | Exact money arithmetic |
| `payment_method` | `str` | Defaults to `"Unknown"` if blank |
| `notes` | `str` | May be empty |

Property `expense.budget_month` returns the `YYYY-MM` budget month string.

## Functions

### `budget_month(expense_date)`

Maps a calendar date to a budget month (21st through 20th rule). Used by summaries, dashboard, and tests.

### `load_expenses(csv_path)`

- Validates required columns: `date`, `category`, `amount`
- Skips completely blank rows
- Raises `SystemExit` with row numbers on invalid dates or amounts
- Returns expenses sorted by date, then category

## Usage in other scripts

```python
from expense_data import load_expenses, budget_month

for expense in load_expenses(csv_path):
    print(expense.budget_month, expense.category, expense.amount)
```

Run scripts from the repo root or `scripts/` directory so the import resolves.

## See also

- [Where data lives — CSV columns](../where-data-lives.md#expenses-csv)
- [Budget month rule](../rules/budget-month.md)
