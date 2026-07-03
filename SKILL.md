---
name: TradeDataTracker
description: Data tracker for trade signals called from MarketAnalysis. Records TP/SL per asset in monthly .md files as table format. Send as clickable file attachment.
---

# TradeDataTracker

## Purpose
Every order that hits TP or SL gets recorded in a per-asset, per-month .md file. Files separated by asset (XAUUSD, BTC, EURUSD, etc.). Sent as clickable file attachments (MEDIA:).

## File Location
- Directory: `~/.hermes/market-history/`
- Filename: `{ASSET}_{YYYY}-{MM}.md`
- Examples: `XAUUSD_2026-07.md`, `BTC_2026-07.md`

## File Format (TABLE)

```
XAUUSD, JULY 2026

| # | Type | Result | Pips |
|---|------|--------|------|
| A1 | ✷ SELL | TP | 200 |
| A2 | ✷ SELL | SL | 100 |
| A3 | ✷ BUY | TP | 500 |
```

### Format Rules
- Title line: `{ASSET}, {MONTH} {YEAR}` — plain text, NO bold
- Empty line after title
- Table header: `| # | Type | Result | Pips |` with separator `|---|------|--------|------|`
- Each entry: `| A{N} | ✷ SELL/BUY | TP/SL | {pips} |`
- ✷ digunakan untuk SELL dan BUY (sinkron dengan MarketAnalysis)
- Append new entries as new rows at the end of table
- Kirim via `MEDIA:` path ke user

### Result Labels
- `TP | 100` = only TP1 hit
- `TP | 200` = TP2 hit
- `TP | 500` = TP3 hit
- `TP | 1000` = TP4 hit (all TPs)
- `SL | 100` = stop loss hit

## Script
The script is available in two locations:

- **GitHub repo:** `scripts/add_history.py` (inside this repository)
- **Hermes install path:** `~/.hermes/skills/research/trade-data-tracker/scripts/add_history.py` (after installing as a Hermes skill)

Usage:
```
python add_history.py XAUUSD 1 sell tp 200
python add_history.py BTC 3 buy sl 100
```

Arguments: `ASSET ANALYST_NUM DIRECTION RESULT [PIPS]`

## Trigger
When user reports:
- "A1 TP hit" / "A1 SL hit"
- "order TP" / "order SL"
- "TP2 hit" / "TP3 hit" / "TP4 hit"
- Any confirmation that a position has closed

## Process
1. Determine: asset, analyst number, direction (sell/buy), result (TP + pips, or SL)
2. Read current file, append new row to table
3. Send file to user via MEDIA: path
4. If file doesn't exist yet, create with header + first row

## Viewing History
When user asks "history xauusd", "history btc", "lihat history":
1. Determine asset and current month
2. Check if file exists
3. Send file: `MEDIA:~/.hermes/market-history/{ASSET}_{YYYY}-{MM}.md`
4. If file doesn't exist: "belum ada history untuk {ASSET} bulan ini"

## Integration with MarketAnalysis-FormatChatAiAgent
- Analyst numbers must match between analysis skill and history tracker
- ✷ digunakan untuk SELL dan BUY — sinkron dengan MarketAnalysis (tidak ada ✧)
- When new analysis is created and previous order completed, add previous order to history BEFORE creating new analysis
- History files are per-asset, per-month — never mix assets in one file

## GitHub
- Repo: `TradeDataTracker`
- Under: `mftrferdinand/TradeDataTracker`
