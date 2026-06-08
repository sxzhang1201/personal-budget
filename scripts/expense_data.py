"""Shared helpers for reading and classifying expenses."""

from __future__ import annotations

import csv
from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal, InvalidOperation
from pathlib import Path


@dataclass(frozen=True)
class Expense:
    date: datetime
    category: str
    description: str
    amount: Decimal
    payment_method: str
    notes: str

    @property
    def budget_month(self) -> str:
        return budget_month(self.date)

    def to_dict(self) -> dict[str, str | float]:
        return {
            "date": self.date.strftime("%Y-%m-%d"),
            "category": self.category,
            "description": self.description,
            "amount": float(self.amount),
            "payment_method": self.payment_method,
            "notes": self.notes,
            "budget_month": self.budget_month,
        }


def budget_month(expense_date: datetime) -> str:
    """Map an expense date to its budget month (21st through 20th cycles)."""
    if expense_date.day > 20:
        return expense_date.strftime("%Y-%m")

    year = expense_date.year
    month = expense_date.month - 1
    if month == 0:
        month = 12
        year -= 1
    return f"{year}-{month:02d}"


def load_expenses(csv_path: Path) -> list[Expense]:
    if not csv_path.exists():
        raise SystemExit(f"CSV file not found: {csv_path}")

    expenses: list[Expense] = []

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

            if not category:
                raise SystemExit(f"Missing category on row {row_number}.")

            try:
                amount = Decimal(amount_value)
            except InvalidOperation as exc:
                raise SystemExit(
                    f"Invalid amount on row {row_number}: {amount_value!r}."
                ) from exc

            expenses.append(
                Expense(
                    date=expense_date,
                    category=category,
                    description=(row.get("description") or "").strip(),
                    amount=amount,
                    payment_method=(row.get("payment_method") or "").strip() or "Unknown",
                    notes=(row.get("notes") or "").strip(),
                )
            )

    return sorted(expenses, key=lambda expense: (expense.date, expense.category))
