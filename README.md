# TradeDataTracker

**Data tracker untuk sinyal yang di-call dari MarketAnalysis — catat hasil TP/SL ke data lengkap per aset per bulan.** Format tabel rapi untuk AI chat agent. Saling berhubungan dengan MarketAnalysis untuk pengambilan data trading yang akurat.

This tool works in tandem with [MarketAnalysis](https://github.com/Mftrferdinand/MarketAnalysis):
- **MarketAnalysis** → full market analysis with Astronacci + Fibonacci. Structured format for AI chat agent — detailed research, live entries, tight risk management (TP/SL). Scripts for accurate and comprehensive market analysis across all assets.
- **TradeDataTracker** → data tracker for signals called from MarketAnalysis. Records TP/SL per asset in clean monthly tables. AI chat agent format — integrated with MarketAnalysis for end-to-end accurate data logging.

Together they form a complete chat AI agent workflow: signal → execution → data logging.

## Features

- **Per-asset tracking** — separate files per asset (XAUUSD → Gold-Data, BTC → BTC-Data, etc.)
- **Clean table format** — `| # | Type | Result | Pips |` with no symbols
- **Monthly organization** — `Gold-Data-07-26.md`, `BTC-Data-07-26.md`
- **Accurate data logging** — every entry recorded with analyst number, direction, and pip result
- **AI-ready** — structured format parseable by any chat AI agent

## File Naming

| Asset | File Name |
|-------|-----------|
| XAUUSD | `Gold-Data-{MM}-{YY}.md` |
| BTC | `BTC-Data-{MM}-{YY}.md` |
| EURUSD | `EURUSD-Data-{MM}-{YY}.md` |
| Any asset | `{ASSET}-Data-{MM}-{YY}.md` |

## Format

```
XAUUSD, JULY 2026

| # | Type | Result | Pips |
|---|------|--------|------|
| A1 | SELL | HIT TP | 200 |
| A2 | SELL | HIT SL | 100 |
```

## Clean UI

Table format is lightweight, no bold/blockquote/symbols — just pure data. Easy to read on any platform (Telegram, Discord, terminal, GitHub).

## Usage

**Add a trade result:**
```bash
python scripts/add_history.py XAUUSD 1 sell tp 200
python scripts/add_history.py BTC 2 buy sl 50
```

Arguments: `ASSET ANALYST_NUM DIRECTION RESULT PIPS`

## Skill

For Hermes Agent: install the skill and it automatically records TP/SL results on your command.

## Related

- [MarketAnalysis](https://github.com/Mftrferdinand/MarketAnalysis) — Market analysis with Astronacci + Fibonacci, generates the signals that TradeDataTracker logs
