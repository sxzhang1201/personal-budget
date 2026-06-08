# Site usage

The public GitHub Pages site publishes **only the dashboard**. These notes are for maintainers.

The site is built with [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/).

---

## Local preview

Install doc dependencies (one-time):

```bash
pip install -r requirements-docs.txt
```

Regenerate the dashboard page, then serve:

```bash
python3 scripts/expense_dashboard.py --output docs/dashboard.html
mkdocs serve
```

Open [http://127.0.0.1:8000](http://127.0.0.1:8000) — you should see the dashboard immediately.

---

## Build static site

```bash
python3 scripts/expense_dashboard.py --output docs/dashboard.html
mkdocs build
```

Output is written to `site/`. `site/index.html` is the dashboard (copied by `docs/hooks.py` after build).

---

## Publish to GitHub Pages

Pushing to `master` runs `.github/workflows/docs.yml`, which:

1. Installs MkDocs Material
2. Generates `docs/dashboard.html` from the current CSV
3. Runs `mkdocs build` (dashboard copied to `index.html`)
4. Publishes `site/` via GitHub Pages Actions

Live URL: **https://sxzhang1201.github.io/personal-budget/**

---

## What to edit

| Change | Edit |
|--------|------|
| Dashboard layout, charts, metrics | `scripts/dashboard_template.html` |
| Dashboard data logic | `scripts/expense_data.py`, `scripts/expense_dashboard.py` |
| Public site config | `mkdocs.yml` (nav is dashboard-only) |
| Maintainer docs | `developer-docs/` (not published) |

Workflow and script write-ups live under `developer-docs/` only.
