# TradeDataTracker

**Data tracker for signals from MarketAnalysis — records TP/SL results into per-asset monthly table format.** Clean markdown tables for AI chat agents. Synchronized with MarketAnalysis v3 final format.

This tool works in tandem with [MarketAnalysis](https://github.com/Mftrferdinand/MarketAnalysis):
- **MarketAnalysis** → Full market analysis with Astronacci + Fibonacci. Structured format for AI chat agent — detailed research, entry areas with fixed RR, tight risk management.
- **TradeDataTracker** → Records every TP/SL result in clean monthly tables. Uses ✷ for both SELL and BUY.

## Features

- **Per-asset tracking** — separate files per asset
- **✷ for both directions** — synchronized with MarketAnalysis (no ✧)
- **Monthly organization** — `XAUUSD_2026-07.md`, `BTC_2026-07.md`
- **Table format** — `| # | Type | Result | Pips |` clean and parseable
- **AI-ready** — structured format parseable by any chat AI agent, sent via MEDIA: path

## File Naming

| Asset | File Name |
|-------|-----------|
| XAUUSD | `XAUUSD_{YYYY}-{MM}.md` |
| BTC | `BTC_{YYYY}-{MM}.md` |
| EURUSD | `EURUSD_{YYYY}-{MM}.md` |
| Any asset | `{ASSET}_{YYYY}-{MM}.md` |

## Format

```
XAUUSD, JULY 2026

| # | Type | Result | Pips |
|---|------|--------|------|
| A1 | ✷ SELL | TP | 200 |
| A2 | ✷ SELL | SL | 100 |
| A3 | ✷ BUY | TP | 500 |
```

- Title: `{ASSET}, {MONTH} {YEAR}` — plain text
- Empty line after title
- Table with 4 columns: `#`, `Type`, `Result`, `Pips`
- ✷ untuk SELL dan BUY (sama dengan MarketAnalysis — tidak ada ✧)
- `Type` column: `✷ SELL` or `✷ BUY`
- `Result` column: `TP` or `SL`
- `Pips` column: numbers only (100, 200, 500, 1000)
- Append new rows at the end of table
- File dikirim via MEDIA: path ke user

## Result Labels

| Hit | Pips |
|-----|------|
| TP1 only | 100 |
| TP2 | 200 |
| TP3 | 500 |
| TP4 (all) | 1000 |
| SL | 100 |

## Usage

```
python scripts/add_history.py XAUUSD 1 sell tp 200
python scripts/add_history.py BTC 3 buy sl 100
```

Arguments: `ASSET ANALYST_NUM DIRECTION RESULT [PIPS]`

**Note:** Script format menggunakan bold entry style lama. Saat ini data di-append manual ke file oleh gue sebagai Hermes agent.

## Viewing History

User bilang "history xauusd" atau "lihat history":
1. Gue cek file `{ASSET}_{YYYY}-{MM}.md`
2. Kirim via MEDIA: path
3. Kalau belum ada: "belum ada history untuk {ASSET} bulan ini"

## Related

- [MarketAnalysis](https://github.com/Mftrferdinand/MarketAnalysis) — generates the signals that TradeDataTracker logs
