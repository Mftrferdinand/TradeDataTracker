---
name: TradeDataTracker
description: Data tracker for trade signals called from MarketAnalysis. Records TP/SL per asset in monthly .md files. Bold entries, plain title. Send as clickable file attachment.
---

# TradeDataTracker

## Purpose
Every order that hits TP or SL gets recorded in a per-asset, per-month .md file. Files separated by asset (XAUUSD, BTC, EURUSD, etc.). Sent as clickable file attachments.

## File Location
- Directory: `~/.hermes/market-history/`
- Filename: `{ASSET}_{YYYY}-{MM}.md`
- Examples: `XAUUSD_2026-07.md`, `BTC_2026-07.md`

## File Format

```
XAUUSD, JULY 2026
**✷ A1 : TP : 200 Pips**
**✷ A2 : SL : 100 Pips**
**✷ A3 : TP : 1000 Pips**
```

### Format Rules
- Title line: `{ASSET}, {MONTH} {YEAR}` — plain text, NO bold
- Entry lines: `**{symbol} A{N} : {result}**` — bold
- ✷ digunakan untuk SELL dan BUY (tidak ada ✧ lagi — sinkron dengan MarketAnalysis)
- TP format: `TP : {pips} Pips` (100, 200, 500, 1000)
- SL format: `SL : 100 Pips`
- One entry per line
- Append new entries at the end

### Result Labels
- `TP : 100 Pips` = only TP1 hit
- `TP : 200 Pips` = TP2 hit
- `TP : 500 Pips` = TP3 hit
- `TP : 1000 Pips` = TP4 hit (all TPs)
- `SL : 100 Pips` = stop loss hit

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
2. Run helper script:
   `python ~/.hermes/skills/research/trade-data-tracker/scripts/add_history.py {ASSET} {ANALYST_NUM} {DIRECTION} {RESULT} {PIPS}`
3. Script creates/appends to file
4. Send file to user: `MEDIA:~/.hermes/market-history/{ASSET}_{YYYY}-{MM}.md`

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
