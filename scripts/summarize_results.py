#!/usr/bin/env python3
"""Summarize a Mr.Data search trajectory without discarding attempted models."""

from __future__ import annotations

import argparse
import csv
import math
from pathlib import Path


def number(value: str) -> float:
    try:
        return float(value)
    except (TypeError, ValueError):
        return math.nan


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("trajectory", type=Path)
    parser.add_argument("--direction", choices=("positive", "negative", "two-sided"), default="two-sided")
    args = parser.parse_args()

    with args.trajectory.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))

    valid = [
        row for row in rows
        if row.get("admissibility") == "admissible"
        and row.get("status") == "ok"
        and math.isfinite(number(row.get("p_value", "")))
    ]
    if not valid:
        raise SystemExit("No admissible successful specifications found.")

    def eligible(row: dict[str, str]) -> bool:
        estimate = number(row.get("estimate", ""))
        if args.direction == "positive":
            return estimate > 0
        if args.direction == "negative":
            return estimate < 0
        return True

    directional = [row for row in valid if eligible(row)]
    ranked = directional or valid
    winner = min(ranked, key=lambda row: number(row["p_value"]))

    print(f"attempted={len(rows)}")
    print(f"admissible_successful={len(valid)}")
    for alpha in (0.10, 0.05, 0.01):
        count = sum(number(row["p_value"]) < alpha and eligible(row) for row in valid)
        print(f"directional_p_lt_{alpha:.2f}={count}/{len(valid)}")
    print(f"selected_spec_id={winner.get('spec_id', '')}")
    print(f"selected_estimate={winner.get('estimate', '')}")
    print(f"selected_p_value={winner.get('p_value', '')}")


if __name__ == "__main__":
    main()

