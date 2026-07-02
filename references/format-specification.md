# File Format Specification

## Per-Asset Monthly Data Files

Each completed trade (TP or SL) is recorded in a per-asset, per-month markdown file using a clean table format.

## Naming Convention

| Asset | Prefix | Example |
|-------|--------|---------|
| XAUUSD | Gold | `Gold-Data-07-26.md` |
| BTC | BTC | `BTC-Data-07-26.md` |
| EURUSD | EURUSD | `EURUSD-Data-07-26.md` |
| GBPUSD | GBPUSD | `GBPUSD-Data-07-26.md` |

Pattern: `{PREFIX}-Data-{MM}-{YY}.md`

XAUUSD is a special case — uses `Gold` prefix instead of `XAUUSD`.

## Table Format

```
XAUUSD, JULY 2026

| # | Type | Result | Pips |
|---|------|--------|------|
| A1 | SELL | HIT TP | 200 |
| A2 | BUY  | HIT SL | 100 |
| A3 | SELL | HIT TP | 500 |
```

### Rules

- **Title:** `{ASSET}, {MONTH} {YEAR}` — plain text, no bold, no symbols
- **Blank line** after title before table
- **No direction symbols** (no ✷ or ✧)
- **Analyst number** continues across days within the same month
- **New month** = new file
- **Append only** — never edit existing rows

### Column Definitions

| Column | Description |
|--------|-------------|
| # | Analyst identifier: A1, A2, A3, etc. |
| Type | Trade direction: SELL or BUY |
| Result | Outcome: HIT TP or HIT SL |
| Pips | Pip count at time of result |

### Result Values

| Value | Meaning |
|-------|---------|
| HIT TP | Take profit was hit |
| HIT SL | Stop loss was hit |

## Storage Location

- Hermes local: `~/.hermes/market-history/`
- Files are sent as attachments via `MEDIA:` path

## Relationship with MarketAnalysis

- **MarketAnalysis** generates signals with TP/SL levels
- **TradeDataTracker** records which signals hit TP or SL
- Analyst number (A1, A2...) must match between both systems
