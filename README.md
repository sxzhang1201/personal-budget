# Personal Budget

A small local budgeting project for tracking expenses manually in a CSV file and summarizing monthly spending by category.

## Project Structure

```text
data/
  expenses.csv
reports/
scripts/
  monthly_summary.py
```

## Workflow

1. Open `data/expenses.csv`.
2. Add one row for each expense.
3. Keep dates in `YYYY-MM-DD` format.
4. Use positive numbers in the `amount` column.
5. Run the summary script when you want to review spending.

The starter CSV includes one example row. Replace it with your own expenses when you are ready.

## CSV Columns

- `date`: Expense date, such as `2026-06-01`
- `category`: Spending category, such as `Groceries`, `Rent`, `Utilities`, or `Dining`
- `description`: Short note about the expense
- `amount`: Expense amount, such as `54.32`
- `payment_method`: Cash, debit card, credit card, bank transfer, etc.
- `notes`: Optional extra details

## Run A Monthly Summary

Summarize all expenses:

```bash
python3 scripts/monthly_summary.py
```

Summarize one month:

```bash
python3 scripts/monthly_summary.py --month 2026-06
```

## Optional Report Files

The `reports/` folder is available for anything you want to save later, such as copied command output, monthly notes, or exported charts.

This project intentionally avoids databases, cloud services, and external dependencies so everything stays local and simple.
