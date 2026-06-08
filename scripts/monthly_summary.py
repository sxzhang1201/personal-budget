#!/usr/bin/env python3
"""Summarize monthly expenses by category from data/expenses.csv."""

from __future__ import annotations

import argparse
import csv
from collections import defaultdict
from datetime import datetime
from decimal import Decimal, InvalidOperation
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CSV_PATH = PROJECT_ROOT / "data" / "expenses.csv"


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
    try:
        return datetime.strptime(value, "%Y-%m").strftime("%Y-%m")
    except ValueError as exc:
        raise SystemExit(f"Invalid --month value {value!r}. Use YYYY-MM.") from exc


def budget_month(expense_date: datetime) -> str:
    """Map an expense date to its budget month (21st through 20th cycles).

    Expenses on the 21st or later belong to that calendar month.
    Expenses on the 20th or earlier belong to the previous calendar month.
    """
    if expense_date.day > 20:
        return expense_date.strftime("%Y-%m")

    year = expense_date.year
    month = expense_date.month - 1
    if month == 0:
        month = 12
        year -= 1
    return f"{year}-{month:02d}"


def read_expenses(csv_path: Path, month_filter: str | None) -> dict[str, Decimal]:
    totals: dict[str, Decimal] = defaultdict(Decimal)

    if not csv_path.exists():
        raise SystemExit(f"CSV file not found: {csv_path}")

    with csv_path.open(newline="", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        required_fields = {"date", "category", "amount"}
        missing_fields = required_fields.difference(reader.fieldnames or [])
        if missing_fields:
            fields = ", ".join(sorted(missing_fields))
            raise SystemExit(f"CSV is missing required field(s): {fields}")

        for row_number, row in enumerate(reader, start=2):
            date_value = (row.get("date") or "").strip()
            category = (row.get("category") or "").strip()
            amount_value = (row.get("amount") or "").strip()

            if not date_value and not category and not amount_value:
                continue

            try:
                expense_date = datetime.strptime(date_value, "%Y-%m-%d")
            except ValueError as exc:
                raise SystemExit(
                    f"Invalid date on row {row_number}: {date_value!r}. Use YYYY-MM-DD."
                ) from exc

            if month_filter and budget_month(expense_date) != month_filter:
                continue

            if not category:
                raise SystemExit(f"Missing category on row {row_number}.")

            try:
                amount = Decimal(amount_value)
            except InvalidOperation as exc:
                raise SystemExit(
                    f"Invalid amount on row {row_number}: {amount_value!r}."
                ) from exc

            totals[category] += amount

    return dict(sorted(totals.items()))


def print_summary(totals: dict[str, Decimal], month_filter: str | None) -> None:
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


def main() -> None:
    args = parse_args()
    month_filter = parse_month(args.month) if args.month else None
    totals = read_expenses(args.csv, month_filter)
    print_summary(totals, month_filter)


if __name__ == "__main__":
    main()
