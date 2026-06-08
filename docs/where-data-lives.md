# Where data lives

All project data and outputs use paths **relative to the repository root**.

```text
personal-budget/
├── data/
│   └── expenses.csv          # Source of truth — one row per expense
├── reports/
│   ├── dashboard.html        # Generated interactive dashboard
│   ├── expense_summary_all.txt
│   ├── monthly_report_2026-05.txt
│   └── sample_monthly_report_2026-06.txt
├── scripts/
│   ├── expense_data.py       # Shared CSV loading and budget month logic
│   ├── expense_dashboard.py  # Dashboard generator
│   ├── monthly_summary.py    # Terminal category summaries
│   └── dashboard_template.html
├── docs/                     # MkDocs source (this site)
└── mkdocs.yml
```

---

## `data/expenses.csv` { #expenses-csv }

| Property | Value |
|----------|--------|
| **Role** | Single ledger for all expenses |
| **Format** | CSV with header row |
| **Edited by** | You (manually or via spreadsheet) |
| **Read by** | All Python scripts via `expense_data.load_expenses()` |

### Columns

| Column | Required | Example |
|--------|----------|---------|
| `date` | Yes | `2026-06-01` |
| `category` | Yes | `Groceries` |
| `description` | No | `AH (Almere)` |
| `amount` | Yes | `35.70` |
| `payment_method` | No | `Debit card` |
| `notes` | No | Optional memo |

!!! warning "Do not overwrite without backup"
    There is no automatic history. Copy or commit the CSV before bulk edits.

---

## `reports/` { #reports }

Generated and optional saved outputs. Safe to delete and recreate **except** if you stored notes there you care about.

| File | Created by | Purpose |
|------|------------|---------|
| `dashboard.html` | `expense_dashboard.py` | Interactive charts and metrics |
| `*.txt` | Manual copy of terminal output | Archived summaries |

Regenerate the dashboard:

```bash
python3 scripts/expense_dashboard.py
```

For this documentation site, the dashboard is also copied to `docs/dashboard.html` before `mkdocs build`.

---

## `scripts/`

Python entry points and shared modules. See [Systems](systems/index.md) for detail.

| Script | Input | Output |
|--------|-------|--------|
| `monthly_summary.py` | CSV | stdout (terminal table) |
| `expense_dashboard.py` | CSV | HTML file |
| `expense_data.py` | CSV | Python `Expense` objects (imported, not run directly) |

---

## What is *not* stored here

- No database files
- No cloud credentials
- No automatic bank import

Everything stays on your machine unless you push the repo to GitHub or copy files elsewhere.
