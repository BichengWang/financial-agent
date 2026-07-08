# Plan: Turtle Trading System (`turtle-trader` sub-repo)

## Context

`investments/equity/turtle-trader/` currently holds only a 4-line Chinese stub
(`The Complete TurtleTrader.md` — "海龟交易法 / 编写策略开始执行"). The goal is a real,
runnable Turtle Trading System here: a Python **script** plus a **SKILL.md**.

The system mirrors the proven sibling pattern in
`investments/equity/daily_investment_system/` — a deterministic, stdlib-only Python
helper (`technical_indicators.py`) that fetches from Yahoo Finance and emits JSON, paired
with markdown spec/operating files, under a strict non-fabrication discipline. We reuse
that style so the new sub-system is consistent and discoverable in the same repo.

Confirmed decisions:
- **Universe:** US equities & ETFs (dollars-per-point = 1). Default scan universe = the
  **S&P 500 ∪ Nasdaq-100 constituents** (deduped, ~540 names).
- **Data provider:** **`yfinance`** for price history (bulk threaded download).
  Index membership is **not** available from yfinance, so constituents are sourced from the
  **Wikipedia** S&P 500 / Nasdaq-100 tables (`pandas.read_html`), cached locally and refreshable.
- **Script:** one script with both a **live signal scanner** and a **historical backtester** (`--mode`).
- **skill.md:** a Claude Code **SKILL.md** (YAML frontmatter, invocable).

> Note: using `yfinance`/`pandas` adds dependencies and departs from the sibling's
> stdlib-only design — accepted deliberately so the large index scan is fast and the
> constituent lists are maintainable.

## Deliverables (files in `investments/equity/turtle-trader/`)

1. `turtle.py` — the deterministic Turtle engine (scanner + backtester).
2. `SKILL.md` — Claude Code skill: Turtle rules, parameters, when/how to run the script.
3. (leave `The Complete TurtleTrader.md` as-is; SKILL.md supersedes it as the entry point.)

## Turtle rules implemented (classic Dennis/Eckhardt, adapted to equities)

- **N (volatility) = 20-day Wilder ATR**: `TR = max(H−L, |H−PDC|, |L−PDC|)`,
  `N = (19·prevN + TR)/20`, seeded by the simple average of the first 20 TRs.
- **Position sizing (Unit):** `unit_shares = floor((risk_pct · account) / N)` with
  `risk_pct` default `0.01` (1% of equity per N of move). `dollar_volatility = N · shares`.
- **Entries (two systems):**
  - **System 1:** 20-day Donchian breakout (close/high beyond prior-20 extreme), with the
    **last-breakout filter** (skip if the prior System-1 breakout would have won) and the
    **55-day failsafe** (take a skipped signal if price reaches the 55-day breakout).
  - **System 2:** 55-day breakout, always taken.
- **Adds (pyramiding):** add 1 Unit every **+½N** favorable move, max **4 units/market**.
- **Stops:** **2N** from entry; on each add, raise all stops so the whole position sits 2N
  below (long) / above (short) the most recent unit.
- **Exits:** System 1 → 10-day low/high; System 2 → 20-day low/high.
- **Portfolio unit caps** (4/market, 6 correlated, 10 loosely-correlated, 12/direction) and
  the **drawdown money-management** (cut size 20% per 10% equity drawdown): caps enforced at
  the scanner aggregate level; drawdown overlay available as a backtest flag. Documented in SKILL.md.

All parameters exposed as CLI flags (entry/exit lengths, N period, risk %, stop multiple,
add spacing, max units, system 1/2/both) with the classic defaults above.

## `turtle.py` design

Dependencies: `yfinance`, `pandas`, `lxml` (for `read_html`) on top of the stdlib
(`argparse`, `json`, `datetime`, `math`). Document them in a `requirements.txt` in the sub-repo.

**Universe layer** (`--universe {sp500,nasdaq100,both}`, default `both`):
- `load_constituents(index)` — read S&P 500 / Nasdaq-100 tickers from the Wikipedia tables via
  `pandas.read_html`, normalize to Yahoo symbols (`BRK.B → BRK-B`), dedup the union.
- Cache to `turtle-trader/universe/{sp500,nasdaq100}.json` with a fetch date; reuse the cache
  unless `--refresh-universe` is passed (so a scan doesn't depend on Wikipedia being up every run).
- `--tickers` / `--tickers-file` override the index universe for ad-hoc scans.

**Data layer** (price history via yfinance):
- `fetch_history(tickers, period/start, interval="1d")` — one bulk `yfinance.download(...)`
  call (threaded, `auto_adjust=True`, `group_by="ticker"`) returning OHLCV per name; chunk the
  ~540-name list and add a small throttle/retry to stay under Yahoo rate limits.
- Local price cache under `turtle-trader/cache/` keyed by ticker (skip re-download of unchanged
  history); `--history-dir` with OHLC CSVs still supported for fully offline / deterministic runs.
- Per-ticker failures → that name is marked `UNAVAILABLE`, the scan continues.

**Compute core (deterministic, pure functions):**
- `true_range_series`, `wilder_n` (ATR-20 / N), `donchian_high/low` (rolling prior-period extreme).
- `unit_size(account, n, risk_pct, dollars_per_point=1)`.
- `breakout_signal(bars, entry_period)` → `LONG_ENTRY | SHORT_ENTRY | NONE`.
- `last_breakout_was_winner(bars, entry_period, exit_period, stop_mult)` — walks history to
  resolve the System-1 last-trade filter deterministically.
- `entry_plan(entry_price, n, direction, ...)` → initial 2N stop, +½N add grid (≤4 units),
  active exit level.

**`--mode scan`** (stateless "what would I do today", mirrors the sibling's JSON contract):
over the resolved universe (default S&P 500 ∪ Nasdaq-100) + `--account`, emit per ticker
`as_of, close, n_atr20, dollar_volatility, unit_shares,
unit_dollar_exposure`, a `system1` and `system2` block (breakout levels, signal, exit levels,
last-trade-filter state for S1), and — when today is an entry — `entry_plan` (stop, add levels,
exit). Aggregate section applies the 6/10/12 unit caps across the scanned list. Because the
default universe is ~540 names, support `--signals-only` to emit just the names with an active
breakout entry today (the actionable set), with the full per-name detail available otherwise.
Missing/insufficient data → `status: UNAVAILABLE` (never fabricated). JSON to stdout or `--output`.

**`--mode backtest`** (per-ticker simulation over fetched history):
event loop applying entries, ½N adds (≤4 units), staged 2N stops, and 10/20-day exits on a
notional account; optional `--drawdown-throttle`. Per-ticker + aggregate stats:
`total_return, cagr, max_drawdown, num_trades, win_rate, avg_win, avg_loss, profit_factor,
expectancy`. JSON output + a compact stdout summary table. Note in output that cross-market
correlation caps are not modeled in the per-instrument backtest.

**Output convention:** default stdout; document writing dated artifacts to
`investments/equity/output/turtle-{YYYY-MM-DD}/` to match the repo (`runbook.md` convention),
via `--output`. Ranges: scan default `2y` (needs ≥56 bars), backtest default `max`.

## `SKILL.md` design

YAML frontmatter:
```
---
name: turtle-trader
description: Turtle Trading System for US equities & ETFs — volatility (N/ATR) position
  sizing, 20/55-day Donchian breakout entries, ½N pyramiding, 2N stops, 10/20-day exits.
  Activates on /turtle-trader or intent like "run the turtle system" / "scan turtle breakouts".
---
```
Body sections: Overview · Markets/universe · The rules (N, sizing, entries, adds, stops,
exits, unit caps, drawdown throttle) with exact parameters · How to run (`scan` and
`backtest` command examples, flags, offline `--history-dir`) · Output schema & location ·
Non-fabrication discipline (prices come from a tool/CSV fetch this run or are `UNAVAILABLE`;
no invented values) · When to use / workflow.

## Verification

0. **Setup:** `pip install -r requirements.txt` (yfinance, pandas, lxml).
1. **Universe:** `python3 turtle.py --refresh-universe` → `universe/sp500.json` + `nasdaq100.json`
   populate with sane counts (~503 / ~100) and Yahoo-normalized symbols.
2. **Scan (full index, live):** `python3 turtle.py --mode scan --universe both --account 100000 --signals-only --pretty`
   → valid JSON; actionable names show `n_atr20`, `unit_shares`, system1/system2 signals + stop/add/exit levels.
3. **Scan (ad-hoc override):** `python3 turtle.py --mode scan --tickers SPY QQQ AAPL --account 100000 --pretty`.
4. **Backtest (live):** `python3 turtle.py --mode backtest --tickers SPY --range max --system both --pretty`
   → equity-curve stats (CAGR, max DD, trades, win rate) print and validate.
5. **Offline/deterministic:** craft a tiny OHLC CSV fixture, run with `--history-dir` (no network)
   → confirm N, breakout, unit-size, and stop math against hand calculations on the fixture.
6. **Edge handling:** a too-short series and a bad ticker both return `status: UNAVAILABLE`, not a crash.
7. **Skill:** confirm `SKILL.md` frontmatter parses (name/description) and command examples run as written.
