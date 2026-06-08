#!/usr/bin/env python3
"""Generate an interactive HTML expense dashboard from data/expenses.csv."""

from __future__ import annotations

import argparse
import json
import webbrowser
from datetime import datetime, timezone
from pathlib import Path

from expense_data import load_expenses, load_monthly_income


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CSV_PATH = PROJECT_ROOT / "data" / "expenses.csv"
DEFAULT_BUDGET_PATH = PROJECT_ROOT / "data" / "budget.json"
DEFAULT_OUTPUT_PATH = PROJECT_ROOT / "reports" / "dashboard.html"
DASHBOARD_TEMPLATE_PATH = Path(__file__).resolve().parent / "dashboard_template.html"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate an interactive HTML expense dashboard."
    )
    parser.add_argument(
        "--csv",
        default=DEFAULT_CSV_PATH,
        type=Path,
        help="Path to the expenses CSV file.",
    )
    parser.add_argument(
        "--output",
        default=DEFAULT_OUTPUT_PATH,
        type=Path,
        help="Path for the generated HTML dashboard.",
    )
    parser.add_argument(
        "--open",
        action="store_true",
        help="Open the dashboard in your default browser after generating it.",
    )
    return parser.parse_args()


def build_dashboard_payload(csv_path: Path, budget_path: Path = DEFAULT_BUDGET_PATH) -> dict:
    expenses = load_expenses(csv_path)
    monthly_income = load_monthly_income(budget_path)
    budget_months = sorted({expense.budget_month for expense in expenses})
    default_month = budget_months[-1] if budget_months else None

    try:
        source_csv = str(csv_path.relative_to(PROJECT_ROOT))
    except ValueError:
        source_csv = str(csv_path)

    return {
        "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC"),
        "source_csv": source_csv,
        "monthly_income": float(monthly_income),
        "expenses": [expense.to_dict() for expense in expenses],
        "budget_months": budget_months,
        "default_month": default_month,
    }


def render_dashboard(payload: dict) -> str:
    template = DASHBOARD_TEMPLATE_PATH.read_text(encoding="utf-8")
    data_json = json.dumps(payload, indent=2)
    return template.replace("__DASHBOARD_DATA__", data_json)


def main() -> None:
    args = parse_args()
    payload = build_dashboard_payload(args.csv)
    html = render_dashboard(payload)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(html, encoding="utf-8")
    print(f"Dashboard written to {args.output}")

    if args.open:
        webbrowser.open(args.output.resolve().as_uri())


if __name__ == "__main__":
    main()
