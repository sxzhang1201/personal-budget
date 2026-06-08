# Site usage

This documentation site is built with **[Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)**, the same stack used by the [NMCB hand-over documentation](https://nmcb-fair.github.io/nmcb-handover-docs/).

---

## Local preview

Install doc dependencies (one-time):

```bash
pip install -r requirements-docs.txt
```

Regenerate the embedded dashboard page, then serve:

```bash
python3 scripts/expense_dashboard.py --output docs/dashboard.html
mkdocs serve
```

Open [http://127.0.0.1:8000](http://127.0.0.1:8000). The site reloads when you edit files under `docs/`.

---

## Build static site

```bash
python3 scripts/expense_dashboard.py --output docs/dashboard.html
mkdocs build
```

Output is written to `site/`. Open `site/index.html` or deploy the folder to any static host.

---

## Publish to GitHub Pages

Pushing to `master` runs `.github/workflows/docs.yml`, which:

1. Installs MkDocs Material
2. Generates `docs/dashboard.html` from the current CSV
3. Deploys to GitHub Pages

After the workflow completes, the site is available at:

**https://sxzhang1201.github.io/personal-budget/**

Enable Pages in the repo settings if needed: **Settings → Pages → Source: GitHub Actions**.

---

## Edit content

| Change | Edit |
|--------|------|
| Home page / data-flow diagram | `docs/index.md` |
| Navigation | `mkdocs.yml` → `nav` |
| Workflow pages | `docs/workflows/*.md` |
| Theme colours | `mkdocs.yml` → `theme.palette` |

Mermaid diagrams use fenced code blocks:

````markdown
```mermaid
flowchart LR
  A --> B
```
````

---

## Relationship to the dashboard

| Artifact | Location | Audience |
|----------|----------|----------|
| **Documentation site** | `docs/` → `site/` | How the project works |
| **Interactive dashboard** | `reports/dashboard.html` | Spending charts and KPIs |

The nav link **Dashboard (live)** opens the generated HTML chart page inside the doc site bundle.
