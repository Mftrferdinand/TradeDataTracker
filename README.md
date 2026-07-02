# TradeDataTracker

Track completed trade orders (TP/SL) per asset in separate monthly markdown files with table format.

## File Naming
- **XAUUSD** → `Gold-Data-{MM}-{YY}.md`
- **BTC** → `BTC-Data-{MM}-{YY}.md`
- **EURUSD** → `EURUSD-Data-{MM}-{YY}.md`
- And so on for other assets

## Format
```
XAUUSD, JULY 2026

| # | Type | Result | Pips |
|---|------|--------|------|
| A1 | SELL | HIT TP | 200 |
| A2 | SELL | HIT SL | 100 |
```

## Usage


## Skill
This repo contains the SKILL.md file for Hermes Agent that runs the tracker.
Script: `scripts/add_history.py`

