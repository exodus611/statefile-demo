#!/usr/bin/env python3
"""Morning price check: compare today's price against the seven-day average."""

import json
from datetime import date

SOURCES = {"provider-a": "https://example.com/a/prices.json"}


def load(path="results.json"):
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def average(values):
    return sum(values) / len(values)


def main():
    data = load()
    history = data["history"][-7:]
    avg = average(history)
    today = data["today"]
    drift = (today - avg) / avg * 100
    print(f"{date.today()}: ${today:.2f} ({drift:+.1f}% vs 7-day average)")


if __name__ == "__main__":
    main()
