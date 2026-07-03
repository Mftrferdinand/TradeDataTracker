# TradeDataTracker

**Data tracker for signals from MarketAnalysis — records TP/SL results into per-asset monthly data.** Clean format for AI chat agents. Synchronized with MarketAnalysis v3 final format.

This tool works in tandem with [MarketAnalysis](https://github.com/Mftrferdinand/MarketAnalysis):
- **MarketAnalysis** → Full market analysis with Astronacci + Fibonacci. Structured format for AI chat agent — detailed research, entry areas with fixed RR, tight risk management.
- **TradeDataTracker** → Records every TP/SL result. Uses ✷ for both SELL and BUY (synchronized with MarketAnalysis v3 update).

## Features

- **Per-asset tracking** — separate files per asset
- **✷ for both directions** — synchronized with MarketAnalysis (no ✧)
- **Monthly organization** — `XAUUSD_2026-07.md`, `BTC_2026-07.md`
- **AI-ready** — structured format parseable by any chat AI agent

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
**✷ A1 : TP : 200 Pips**
**✷ A2 : SL : 100 Pips**
**✷ A3 : TP : 1000 Pips**
```

- ✷ untuk SELL dan BUY (sama dengan MarketAnalysis — tidak ada ✧)
- Bold entry lines, plain title
- `TP : {pips} Pips` atau `SL : 100 Pips`
- Append new entries at the end

## Usage

```
python scripts/add_history.py XAUUSD 1 sell tp 200
python scripts/add_history.py BTC 3 buy sl 100
```

Arguments: `ASSET ANALYST_NUM DIRECTION RESULT [PIPS]`

## Related

- [MarketAnalysis](https://github.com/Mftrferdinand/MarketAnalysis) — generates the signals that TradeDataTracker logs
