---
name: turtle-trader
description: Turtle Trading System for US equities & ETFs — volatility (N/ATR) position sizing, 20/55-day Donchian breakout entries, ½N pyramiding, 2N stops, 10/20-day exits. Scans the S&P 500 ∪ Nasdaq-100 for today's actionable breakouts and backtests the rules historically. Activates on /turtle-trader or intent like "run the turtle system", "scan turtle breakouts", or "backtest the turtle strategy".
---

# Turtle Trader

A deterministic implementation of the classic Dennis/Eckhardt **Turtle Trading System**,
adapted from futures to **US equities & ETFs** (dollars-per-point = 1). Everything lives in
one script, `turtle.py`, with two modes: a stateless **scanner** ("what would I do today")
and a per-instrument **backtester**.

This skill is the operating spec. The companion compute system in
`../daily_investment_system/` is multi-factor research; this one is a single, rule-based
trend-following strategy with explicit money management.

## Universe (where the tickers come from)

- Default scan universe = **S&P 500 ∪ Nasdaq-100 constituents** (deduped, ~540 names).
- Constituent lists are read from the **Wikipedia** index tables (`pandas.read_html`),
  normalized to Yahoo symbols (`BRK.B → BRK-B`), and cached in `universe/*.json`. yfinance has
  no index-membership API, so this is the source of truth for *which names exist*.
- Refresh the lists with `--refresh-universe` (do this occasionally; constituents change).
- `--universe {sp500,nasdaq100,both}` narrows the index; `--tickers` / `--tickers-file`
  override entirely for an ad-hoc watchlist.

## Data

- Price history via **yfinance** bulk threaded `download()` (OHLCV, auto-adjusted), chunked
  with a throttle to respect rate limits, cached per ticker for the day in `cache/`.
- `--history-dir DIR` reads `TICKER.csv` OHLC files instead — fully offline and deterministic.
- **Non-fabrication discipline:** every value comes from a yfinance fetch this run or from a
  CSV; a name with no/insufficient data is reported `status: UNAVAILABLE`. Nothing is invented.

## The rules (defaults match the original system)

| Rule | Default | Flag |
|---|---|---|
| **N (volatility)** = 20-day Wilder ATR: `TR = max(H−L, |H−PDC|, |L−PDC|)`, `N = (19·prevN + TR)/20` | 20 | `--n-period` |
| **Unit size** = `floor((risk% · account) / N)` shares — a 1 N move ≈ risk% of equity | 1% | `--risk-pct`, `--account` |
| **System 1 entry** = 20-day Donchian breakout, **skipped if the last breakout won**, with a **55-day failsafe** | 20/10 | — |
| **System 2 entry** = 55-day breakout, always taken | 55/20 | — |
| **Adds (pyramiding)** = +1 Unit every **+½N** favorable move | ½N, ≤4 | `--add-spacing`, `--max-units` |
| **Stops** = **2N** from entry; ratchet so the whole position sits 2N from the most recent unit | 2N | `--stop-mult` |
| **Exits** = System 1 → 10-day low/high; System 2 → 20-day low/high | 10/20 | — |
| **Direction** = long-only by default (equity short breakouts rarely pay) | long-only | `--allow-short` |

**Portfolio overlay** (reported in the scan `portfolio` block): max 4 Units/market,
6 Units/closely-correlated, 10/loosely-correlated, 12/direction. **Drawdown money management**
(trade 20% smaller per 10% equity drawdown) is available in the backtest via `--drawdown-throttle`.

The System 1 *last-trade filter* is computed deterministically by replaying single-Unit
System 1 trades over the fetched history and inspecting the most recent closed trade
(winner ⇒ skip the next 20-day breakout unless the 55-day failsafe also fires).

## How to run

```bash
pip install -r requirements.txt

# 1) Refresh the index constituent lists (run occasionally)
python3 turtle.py --refresh-universe

# 2) Scan today's actionable breakouts across S&P 500 ∪ Nasdaq-100
python3 turtle.py --mode scan --universe both --account 100000 --signals-only --pretty

# 3) Ad-hoc scan of a custom watchlist
python3 turtle.py --mode scan --tickers SPY QQQ AAPL NVDA --account 100000 --pretty

# 4) Backtest both systems on one name over full history
python3 turtle.py --mode backtest --tickers SPY --range max --system both --include-trades --pretty

# 5) Fully offline / deterministic run from CSVs (TICKER.csv with Date,Open,High,Low,Close,Volume)
python3 turtle.py --mode scan --tickers DEMO --history-dir ./fixtures --account 100000 --pretty
```

Useful flags: `--allow-short` (off by default; enables short breakouts), `--range` (yfinance
period; default `2y` scan / `max` backtest), `--no-cache`, `--chunk-size`, `--pause`,
`--output FILE`, `--no-compound`.

## Output

JSON to stdout (or `--output`). Backtest also prints a compact stderr summary table.

- **Scan** — per ticker: `as_of, close, n_atr20, unit_shares, unit_dollar_exposure,
  dollar_volatility`, a `system1`/`system2` block (breakout levels, `signal`, exit levels,
  S1 `last_trade_filter` + `failsafe_55d`), and an `entry_plan` (entry, `initial_stop`,
  `add_levels`, `stop_after_each_add`, `exit_level`) when a name is actionable today. A
  top-level `portfolio` block summarizes signal counts and the unit caps. `--signals-only`
  emits just the actionable names (the ~540-name universe is otherwise verbose).
- **Backtest** — per ticker×system: `total_return_pct, cagr_pct, max_drawdown_pct,
  num_trades, win_rate_pct, avg_win, avg_loss, profit_factor, expectancy` (+ `trades` with
  `--include-trades`), plus an `aggregate` block. Per-instrument runs are independent;
  cross-market correlation/unit caps are not modeled in the backtest.

To persist dated artifacts alongside the sibling system, write to
`../output/turtle-{YYYY-MM-DD}/` via `--output`.

## When to use

- "Scan for turtle breakouts / what should I buy today" → **scan mode**, `--signals-only`.
- "How would the turtle rules have done on X" → **backtest mode**.
- The output is a *decision-support* artifact (entries, stops, sizing), not an order router.
  It never places trades — execution is the user's.
