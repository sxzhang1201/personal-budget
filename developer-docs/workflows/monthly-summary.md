# Monthly summary

## Why this exists

Fast **category totals** in the terminal without opening a browser — useful for quick checks or copying into `reports/*.txt`.

## When to do it

- End of a budget month review
- Before updating archived text reports

## Where

| Input | Output |
|-------|--------|
| `data/expenses.csv` | Printed table on stdout |

## Steps

Summarize **all** expenses (every budget month combined):

```bash
python3 scripts/monthly_summary.py
```

Summarize **one budget month**:

```bash
python3 scripts/monthly_summary.py --month 2026-05
```

Use a custom CSV path:

```bash
python3 scripts/monthly_summary.py --csv path/to/expenses.csv --month 2026-05
```

### Example output

```text
Expense summary for 2026-05
===========================
Category       Amount
-------------  ----------
Dining         $   112.75
Groceries      $   215.62
...
Total          $ 2,524.80
```

## What to check before done

- [ ] `--month` uses **budget month**, not calendar month of each row
- [ ] Totals match expectations for large fixed items (mortgage, insurance)
- [ ] Optional: save output to `reports/monthly_report_YYYY-MM.txt`

## See also

- [Budget month rule](../rules/budget-month.md)
- [Dashboard workflow](dashboard.md) for charts and KPIs
