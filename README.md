# Personal Budget

A small local budgeting project for tracking expenses manually in a CSV file and summarizing monthly spending by category.

## Project Structure

```text
data/
  expenses.csv
reports/
  dashboard.html
scripts/
  expense_data.py
  expense_dashboard.py
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

## Budget Month Rule

Each budget month runs from the **21st of one calendar month through the 20th of the next**.

- Expenses dated **after the 20th** (21st onward) belong to that calendar month.
- Expenses dated **on or before the 20th** belong to the previous calendar month.

Examples:

- `2026-05-25` → May budget month
- `2026-05-20` → April budget month
- `2026-06-05` → May budget month
- `2026-06-21` → June budget month

The `--month` flag uses this budget month, not the calendar month of the date.

## Run A Monthly Summary

Summarize all expenses:

```bash
python3 scripts/monthly_summary.py
```

Summarize one month:

```bash
python3 scripts/monthly_summary.py --month 2026-06
```

## Expense Dashboard

Generate an interactive HTML dashboard with charts and metrics:

```bash
python3 scripts/expense_dashboard.py --open
```

This writes `reports/dashboard.html`. Open that file in your browser any time to review spending.

The dashboard includes:

- **Metrics**: total spend, transaction count, daily average, top category, largest expense, month-over-month change, fixed vs variable costs
- **Charts**: monthly trend, category breakdown, category share, payment methods, stacked category view by month
- **Table**: 10 most recent expenses for the selected budget month

Use the budget month dropdown to switch months. Charts use Chart.js from a CDN, so you need internet access when viewing the dashboard.

## Optional Report Files

The `reports/` folder is available for anything you want to save later, such as copied command output, monthly notes, or exported charts.

This project intentionally avoids databases, cloud services, and Python package dependencies for the core scripts so everything stays local and simple.

## Documentation site

A [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) site — styled like the [NMCB hand-over documentation](https://nmcb-fair.github.io/nmcb-handover-docs/) — explains workflows, data paths, and the budget month rule.

```bash
pip install -r requirements-docs.txt
python3 scripts/expense_dashboard.py --output docs/dashboard.html
mkdocs serve
```

Open [http://127.0.0.1:8000](http://127.0.0.1:8000). Published docs (after GitHub Actions): **https://sxzhang1201.github.io/personal-budget/**

See `docs/site-usage.md` for build and publish details.
