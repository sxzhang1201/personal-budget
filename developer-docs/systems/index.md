# Systems

Python modules and scripts that power summaries and the dashboard.

| Component | Role |
|-----------|------|
| [Expense data](expense-data.md) | Shared CSV parsing and budget month logic |
| [Scripts](scripts.md) | CLI entry points |

```mermaid
flowchart LR
  CSV["expenses.csv"] --> ED["expense_data.py"]
  ED --> MS["monthly_summary.py"]
  ED --> DB["expense_dashboard.py"]
  DB --> TPL["dashboard_template.html"]
  TPL --> HTML["dashboard.html"]
```

All scripts are stdlib-only — no `pip install` required for reporting.
