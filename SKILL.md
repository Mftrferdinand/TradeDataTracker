---
name: TradeDataTracker
description: Track completed trade orders (TP/SL) per asset in separate monthly .md files. XAUUSD → Gold-Data-{MM}-{YY}.md. Table format, no symbols. Send as clickable file.
---

# TradeDataTracker

## Purpose
Every completed order (TP or SL) gets recorded into a per-asset, per-month .md file with TABLE format. XAUUSD → `Gold-Data-{MM}-{YY}.md`, other assets → `{ASSET}-Data-{MM}-{YY}.md`. Sent as clickable file attachments.

## File Location
- Directory: `~/.hermes/market-history/`
- Naming by asset:
  - **XAUUSD** → `Gold-Data-{MM}-{YY}.md`
  - **BTC** → `BTC-Data-{MM}-{YY}.md`
  - **EURUSD** → `EURUSD-Data-{MM}-{YY}.md`
- Examples: `Gold-Data-07-26.md`, `BTC-Data-07-26.md`

## File Format

```
XAUUSD, JULY 2026

| # | Type | Result | Pips |
|---|------|--------|------|
| A1 | SELL | HIT TP | 200 |
| A2 | SELL | HIT SL | 100 |
```

### Format Rules
- Title line: `{ASSET}, {MONTH} {YEAR}` — plain text, NO bold, NO symbols
- Blank line after title
- Table: **#**, **Type**, **Result**, **Pips**
- Header: `| # | Type | Result | Pips |`
- Separator: `|---|------|--------|------|`
- Entry: `| A{N} | SELL/BUY | HIT TP/HIT SL | {pips} |`
- No direction symbols (✷ / ✧)
- Pips column = actual pip count
- One entry per row, append at end
- Analyst number continues across days in same month
- New month = new file

### Result Labels
- `HIT TP` = take profit hit
- `HIT SL` = stop loss hit

## Script
Path: `~/.hermes/skills/research/trade-data-tracker/scripts/add_history.py`

Usage:
```
python add_history.py XAUUSD 1 sell tp 200
python add_history.py BTC 3 buy sl 100
```

## GitHub
- Repo: `TradeDataTracker`
- Under: `mftrferdinand/TradeDataTracker`

## Process
1. Determine: asset, analyst number, direction, result (TP + pips or SL)
2. Run: `python ~/.hermes/skills/research/trade-data-tracker/scripts/add_history.py {ASSET} {N} {DIR} {RESULT} {PIPS}`
3. Script creates/updates file at `~/.hermes/market-history/{filename}.md`
4. Send file: `MEDIA:~/.hermes/market-history/{filename}.md`
