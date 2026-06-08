# Scripts

Command-line tools in `scripts/`.

## `monthly_summary.py`

**Purpose:** Print category totals to the terminal.

```bash
python3 scripts/monthly_summary.py [--month YYYY-MM] [--csv PATH]
```

| Flag | Default | Description |
|------|---------|-------------|
| `--month` | all months | Filter by budget month |
| `--csv` | `data/expenses.csv` | Input file |

Workflow: [Monthly summary](../workflows/monthly-summary.md)

---

## `expense_dashboard.py`

**Purpose:** Generate interactive HTML dashboard.

```bash
python3 scripts/expense_dashboard.py [--output PATH] [--csv PATH] [--open]
```

| Flag | Default | Description |
|------|---------|-------------|
| `--output` | `reports/dashboard.html` | HTML destination |
| `--csv` | `data/expenses.csv` | Input file |
| `--open` | off | Open browser after write |

Uses `dashboard_template.html` and embeds expense JSON for client-side charts.

Workflow: [Dashboard](../workflows/dashboard.md)

---

## `dashboard_template.html`

Not run directly. HTML/CSS/JS template with a `__DASHBOARD_DATA__` placeholder replaced by `expense_dashboard.py`.

Chart library: [Chart.js](https://www.chartjs.org/) (CDN).

---

## Dependencies

| Script | Python packages |
|--------|-----------------|
| `monthly_summary.py` | stdlib only |
| `expense_dashboard.py` | stdlib only |
| MkDocs site | see `requirements-docs.txt` |
