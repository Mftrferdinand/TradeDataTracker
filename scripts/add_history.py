#!/usr/bin/env python3
"""Add completed order to per-asset monthly history file (TABLE format).

Per-asset files: XAUUSD → Gold-Data-{MM}-{YY}.md, BTC → BTC-Data-{MM}-{YY}.md, etc.

Usage: python add_history.py ASSET ANALYST_NUM DIRECTION RESULT [PIPS]
  ASSET:        XAUUSD, BTC, EURUSD, etc.
  ANALYST_NUM:  1, 2, 3, etc.
  DIRECTION:    sell or buy
  RESULT:       tp or sl
  PIPS:         100, 200, 500, 1000 (for TP), 100 (for SL)

Example: python add_history.py XAUUSD 1 sell tp 200
         python add_history.py BTC 3 buy sl 100
"""
import sys
import os
from datetime import datetime

# Table header
TABLE_HEADER = "| # | Type | Result | Pips |\n|---|------|--------|------|"

# Asset to file prefix mapping
ASSET_PREFIX = {
    "XAUUSD": "Gold",
}

def get_filename(asset: str, month_num: str, year_short: str) -> str:
    """Get per-asset filename based on asset name."""
    prefix = ASSET_PREFIX.get(asset, asset)
    return f"{prefix}-Data-{month_num}-{year_short}.md"

def main():
    if len(sys.argv) < 5:
        print("Usage: python add_history.py ASSET ANALYST_NUM DIRECTION RESULT [PIPS]")
        sys.exit(1)

    asset = sys.argv[1].upper()
    analyst_num = sys.argv[2]
    direction = sys.argv[3].lower()
    result = sys.argv[4].lower()
    pips = sys.argv[5] if len(sys.argv) > 5 else "100"

    # Direction string (no symbol)
    direction_str = "SELL" if direction == "sell" else "BUY"

    # Result string
    if result == "tp":
        result_str = "HIT TP"
    elif result == "sl":
        result_str = "HIT SL"
    else:
        result_str = result.upper()

    # Current month
    now = datetime.now()
    month_name = now.strftime("%B").upper()
    year = now.year
    month_num = now.strftime("%m")
    year_short = str(year)[-2:]

    # File path — per asset, separate file
    history_dir = os.path.expanduser("~/.hermes/market-history")
    os.makedirs(history_dir, exist_ok=True)
    filename = get_filename(asset, month_num, year_short)
    filepath = os.path.join(history_dir, filename)

    # Table entry line
    entry_line = f"| A{analyst_num} | {direction_str} | {result_str} | {pips} |"

    # Check if file exists
    if os.path.exists(filepath):
        # Append entry
        with open(filepath, "a") as f:
            f.write(entry_line + "\n")
        print(f"Appended to {filepath}")
    else:
        # Create new file: plain title, blank line, table header, entry
        title_line = f"{asset}, {month_name} {year}"
        with open(filepath, "w") as f:
            f.write(title_line + "\n")
            f.write("\n")
            f.write(TABLE_HEADER + "\n")
            f.write(entry_line + "\n")
        print(f"Created {filepath}")

    # Print full file content
    with open(filepath, "r") as f:
        print("\n--- FILE CONTENT ---")
        print(f.read())

    # Print absolute path for MEDIA delivery
    print(f"\nFILE_PATH:{filepath}")

if __name__ == "__main__":
    main()