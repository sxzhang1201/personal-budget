# Add expenses

## Why this exists

Every report and chart depends on rows in `data/expenses.csv`. This workflow keeps the ledger complete and consistently formatted.

## When to do it

- After a purchase you want to track
- When reconciling bank or card statements (batch entry)

## Where

| Item | Path |
|------|------|
| Ledger | `data/expenses.csv` |

## Steps

1. Open `data/expenses.csv` in a text editor or spreadsheet.
2. Add **one row per expense** at the bottom (keep the header row unchanged).
3. Set `date` in `YYYY-MM-DD` format.
4. Choose a `category` (consistent spelling helps summaries).
5. Enter a positive `amount`.
6. Optionally fill `description`, `payment_method`, and `notes`.
7. Save the file.

### Example row

```csv
2026-06-08,Groceries,AH (Almere),42.15,Debit card,
```

## What to check before done

- [ ] Date parses as `YYYY-MM-DD`
- [ ] `category` and `amount` are not empty
- [ ] `amount` is positive (no minus sign)
- [ ] You know which [budget month](../rules/budget-month.md) the date falls into

## Next steps

```bash
python3 scripts/monthly_summary.py --month 2026-05
python3 scripts/expense_dashboard.py --open
```
