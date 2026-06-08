# Dashboard workflow

## Why this exists

The terminal summary shows category totals only. The dashboard adds **trends**, **payment-method splits**, **month-over-month change**, and a **recent transactions** table.

## When to do it

- Monthly review with visuals
- After adding many new rows
- Before publishing the documentation site (dashboard is embedded in docs)

## Where

| Input | Output |
|-------|--------|
| `data/expenses.csv` | `reports/dashboard.html` (default) |

## Steps

Generate the dashboard:

```bash
python3 scripts/expense_dashboard.py
```

Generate and open in your browser:

```bash
python3 scripts/expense_dashboard.py --open
```

Custom output path:

```bash
python3 scripts/expense_dashboard.py --output reports/dashboard.html
```

For MkDocs, copy into `docs/` before building the site:

```bash
python3 scripts/expense_dashboard.py --output docs/dashboard.html
```

## Dashboard contents

### Metrics (selected budget month)

| Metric | Description |
|--------|-------------|
| Total spend | Sum of all expenses in the budget month |
| Transactions | Count and average transaction size |
| Daily average | Total ÷ 30 (budget month length) |
| Top category | Highest-spend category |
| Largest expense | Single biggest row |
| Month over month | % change vs previous budget month |
| Fixed / variable | Fixed = Mortgage, Insurance, Utilities, Membership |

### Charts

- Monthly spending trend
- Category bar chart and pie chart
- Payment method donut
- Stacked category breakdown by budget month

Use the **Budget month** dropdown to switch periods.

!!! note "Internet required"
    Charts load Chart.js from a CDN. Offline viewing shows layout but not graphs.

## What to check before done

- [ ] Budget month dropdown lists expected months
- [ ] Fixed costs (mortgage, utilities) appear in the selected month
- [ ] Regenerated after CSV edits

## Live page

Open the [Interactive dashboard](../dashboard.html) from this site (generated at build time).
