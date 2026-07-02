#!/usr/bin/env python3
"""Add completed order to per-asset monthly history file.

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

def main():
    if len(sys.argv) < 5:
        print("Usage: python add_history.py ASSET ANALYST_NUM DIRECTION RESULT [PIPS]")
        sys.exit(1)

    asset = sys.argv[1].upper()
    analyst_num = sys.argv[2]
    direction = sys.argv[3].lower()
    result = sys.argv[4].lower()
    pips = sys.argv[5] if len(sys.argv) > 5 else "100"

    # Direction symbol
    if direction == "sell":
        symbol = "✷"
    elif direction == "buy":
        symbol = "✧"
    else:
        symbol = "✷"

    # Result string
    if result == "tp":
        result_str = f"TP : {pips} Pips"
    elif result == "sl":
        result_str = f"SL : 100 Pips"
    else:
        result_str = result.upper()

    # Current month
    now = datetime.now()
    month_name = now.strftime("%B").upper()
    year = now.year
    year_month = now.strftime("%Y-%m")

    # File path
    history_dir = os.path.expanduser("~/.hermes/market-history")
    os.makedirs(history_dir, exist_ok=True)
    filename = f"{asset}_{year_month}.md"
    filepath = os.path.join(history_dir, filename)

    # Entry line (bold)
    entry_line = f"**{symbol} A{analyst_num} : {result_str}**"

    # Check if file exists
    if os.path.exists(filepath):
        # Append entry
        with open(filepath, "a") as f:
            f.write(entry_line + "\n")
        print(f"Appended to {filepath}")
    else:
        # Create new file with title
        title_line = f"{asset}, {month_name} {year}"
        with open(filepath, "w") as f:
            f.write(title_line + "\n")
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
