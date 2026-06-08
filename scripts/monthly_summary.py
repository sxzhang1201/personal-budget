#!/usr/bin/env python3
"""Summarize monthly expenses by category from data/expenses.csv."""

from __future__ import annotations

import argparse
from collections import defaultdict
from decimal import Decimal
from pathlib import Path

from expense_data import load_expenses, load_monthly_income


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CSV_PATH = PROJECT_ROOT / "data" / "expenses.csv"
DEFAULT_BUDGET_PATH = PROJECT_ROOT / "data" / "budget.json"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Summarize monthly expenses by category."
    )
    parser.add_argument(
        "--month",
        help=(
            "Budget month to summarize in YYYY-MM format "
            "(each month runs from the 21st through the 20th). "
            "Defaults to all months."
        ),
    )
    parser.add_argument(
        "--csv",
        default=DEFAULT_CSV_PATH,
        type=Path,
        help="Path to the expenses CSV file.",
    )
    return parser.parse_args()


def parse_month(value: str) -> str:
    from datetime import datetime

    try:
        return datetime.strptime(value, "%Y-%m").strftime("%Y-%m")
    except ValueError as exc:
        raise SystemExit(f"Invalid --month value {value!r}. Use YYYY-MM.") from exc


def summarize_by_category(csv_path: Path, month_filter: str | None) -> dict[str, Decimal]:
    totals: dict[str, Decimal] = defaultdict(Decimal)

    for expense in load_expenses(csv_path):
        if month_filter and expense.budget_month != month_filter:
            continue
        totals[expense.category] += expense.amount

    return dict(sorted(totals.items()))


def print_summary(
    totals: dict[str, Decimal],
    month_filter: str | None,
    monthly_income: Decimal,
) -> None:
    title = f"Expense summary for {month_filter}" if month_filter else "Expense summary"
    print(title)
    print("=" * len(title))

    if not totals:
        print("No expenses found.")
        return

    grand_total = sum(totals.values(), Decimal("0"))
    category_width = max(len("Category"), *(len(category) for category in totals))

    print(f"{'Category':<{category_width}}  Amount")
    print(f"{'-' * category_width}  {'-' * 10}")

    for category, amount in totals.items():
        print(f"{category:<{category_width}}  ${amount:>9,.2f}")

    print(f"{'-' * category_width}  {'-' * 10}")
    print(f"{'Total':<{category_width}}  ${grand_total:>9,.2f}")

    if month_filter:
        remaining = monthly_income - grand_total
        spent_share = grand_total / monthly_income if monthly_income else Decimal("0")
        print()
        print(f"{'Monthly income':<{category_width}}  ${monthly_income:>9,.2f}")
        print(f"{'Remaining':<{category_width}}  ${remaining:>9,.2f}")
        print(f"{'Spent of income':<{category_width}}  {spent_share * 100:>8.1f}%")


def main() -> None:
    args = parse_args()
    month_filter = parse_month(args.month) if args.month else None
    monthly_income = load_monthly_income(DEFAULT_BUDGET_PATH)
    totals = summarize_by_category(args.csv, month_filter)
    print_summary(totals, month_filter, monthly_income)


if __name__ == "__main__":
    main()
