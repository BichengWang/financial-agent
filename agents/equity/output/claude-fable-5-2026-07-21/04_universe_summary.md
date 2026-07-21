# 04 Universe Summary — 2026-07-21 (claude-fable-5)

## Construction

`build_index_universe.py --sp500-cache agents/equity/turtle-trader/universe/sp500.json --nasdaq100-cache agents/equity/turtle-trader/universe/nasdaq100.json` → **515-name union** (503 S&P 500 ∪ 101 Nasdaq-100, 89-name overlap; both caches fetched 2026-06-21 — stale relative to today but used per the stale-cache rule in `rules.md § Index-Union Universe Protocol` point 5; refresh is a maintenance task, not a fallback trigger). Full path used — the Sampled Universe Protocol emergency fallback was **not** invoked.

## Inclusion / Exclusion Log

Applied filters per `rules.md § Universe Construction`:

| Filter | Threshold | Result |
|---|---|---|
| Price | > $5 | 0 names excluded on this basis alone |
| ADV20 | > $20M | 0 names excluded on this basis alone |
| Listing history | ≥ 60 trading days fetched | **1 exclusion: `FDXF`** — indicator status `UNAVAILABLE`, sparse/thin trading history (large intraday price swings, gaps of days between prints) consistent with a recent listing or illiquid instrument |

**Eligible universe after filters: 514** (515 union − 1 FDXF). Percentile label: `INDEX_UNION_PCTL (n=514)`.

## Metric Coverage Summary

| `rules.md § Financial Metrics and Score Attribution` input | Sourceable across eligible universe? | Effect |
|---|---|---|
| Price history (5y daily, Yahoo v8) | 513/514 (99.8%) | GO-eligible; FDXF excluded |
| 30d realized vol (sigma via Sigma Fallback Chain step 2) | 513/514 | GO-eligible |
| 60d beta vs SPY | 513/514 (≥20 matched daily return pairs required) | Feeds Macro_Z |
| Technical indicator pack (TD-9/RSI/MACD/MA/momentum/RS/volume, d/w/m) | 517/518 requested (incl. SPY/QQQ/SOXX); 513/514 eligible names | Feeds Tech_Z |
| Next earnings date | 46/60 confirmed (top-60 shortlist), 14/60 `ESTIMATED post-print cadence (±5d)` | GO-eligible (5th Required input) |
| Fundamental family (Fund_Z) | **20/514 (3.9%)** — SHADOW-only shortlist run | Below 70% promotion bar → `UNAVAILABLE` for scoring, diagnostic only |
| Sentiment family (Sent_Z) | **20/514 (3.9%)** — SHADOW-only shortlist run | Below 70% promotion bar → `UNAVAILABLE` for scoring, diagnostic only |
| Options IV/skew, short interest, bid-ask tape, analyst-revision tape, institutional flow, GICS sector feed | Not wired (Enhancing) | DQ capped at 0.80, confidence capped, never a GO blocker alone |

Fund_Z/Sent_Z unavailability is the dominant driver of this run's structural evidence-threshold gate (`rules.md § Evidence Thresholds` #2: ≥3 of 4 families non-negative — mathematically unreachable with only 2 of 4 families ever sourceable). This is unchanged from every session since 2026-07-06 and remains blocked on `agents/equity/plan/2026-07-15-claude-fable-5-top-priority.md` Phase 2 (bulk `companyfacts.zip` + threaded Nasdaq sentiment across the full ~514-name universe), not attempted this run.

## Technical Indicator Coverage (daily/weekly/monthly)

TD-9, RSI(14), MACD(12,26,9), MA20/50 alignment, 20/60-bar momentum, 20-bar volume ratio, and 20/60-bar relative strength vs SPY: **513/514 eligible names (99.8%) fully sourced across all three timeframes**; `FDXF` `UNAVAILABLE` (excluded from the universe entirely, not merely from the technical pack). No partial-timeframe gaps observed among sourced names.
