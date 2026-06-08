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

Open [http://127.0.0.1:8000](http://127.0.0.1:8000). The root URL opens the **dashboard**; project docs are under **Documentation** in the nav.

---

## Build static site

```bash
python3 scripts/expense_dashboard.py --output docs/dashboard.html
mkdocs build
```

Output is written to `site/`. Open `site/index.html` for the dashboard, or `site/documentation/` for the docs home.

---

## Publish to GitHub Pages

Pushing to `master` runs `.github/workflows/docs.yml`, which:

1. Installs MkDocs Material
2. Generates `docs/dashboard.html` from the current CSV
3. Runs `mkdocs build`
4. Publishes the `site/` folder via the official **GitHub Pages** Actions deploy

In **Settings → Pages**, choose **Source: GitHub Actions** (not “Deploy from a branch”).

After a successful run, the site URL appears at the top of that Settings page, usually:

**https://sxzhang1201.github.io/personal-budget/**

---

## Edit content

| Change | Edit |
|--------|------|
| Home page / data-flow diagram | `docs/documentation.md` |
| Site home (dashboard) | `docs/dashboard.html` → copied to `index.html` on build |
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
| **Interactive dashboard** | `docs/dashboard.html` | Spending charts and KPIs (also served at `/`) |

The **Dashboard** tab is first in the nav and is also copied to `/` when the site is built.
