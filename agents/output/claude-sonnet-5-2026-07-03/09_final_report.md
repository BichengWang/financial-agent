```
══════════════════════════════════════════════════════
QUANTITATIVE EQUITY SELECTION REPORT — 2026-07-03
Run Status: NO_TRADE
Classification: INTERNAL — INVESTMENT COMMITTEE USE
══════════════════════════════════════════════════════
```

## Executive Summary

This run materialized the full 515-name S&P 500 ∪ Nasdaq-100 universe and grounded a 30-name Sampled Universe Protocol subset (documented fallback: Yahoo Finance is blocked by this session's egress policy, and per-name IBKR fetch across all 515 names was infeasible in one session) via Interactive Brokers 5-year daily history and live snapshot prices. Twelve names clear the 60th-percentile ranking floor on Technical/Price and Macro/Regime evidence alone, led by `INTC`, `AMAT`, and `AMD`. **No name is investable**: no cross-sectional fundamental or sentiment/positioning feed is wired this session, so Fund_Z and Sent_Z are `UNAVAILABLE` universe-wide, and the "≥3 of 4 factor families non-negative" evidence gate cannot be cleared by any name regardless of score. The regime is classified `BULL` (medium confidence) on a falling VIX and strong 60-day momentum across SPY/QQQ/SOXX, tempered by a near-term daily pullback. Final status: **`NO_TRADE`**.

## MoM Reflection Summary

(Summarizes `02_reflection.md`; no new facts.) Baseline: `gpt-5-2026-06-07` (`CROSS_MODEL_BASELINE`, no same-model folder exists yet). Of the 6 prior watchlist names re-priceable this run, 3 hit their implied direction (`UNH` +5.36% alpha, `JPM` +5.64% alpha, `CAT` +8.45% alpha) and 3 missed (`XOM` -10.37% alpha, `WMT` -9.57% alpha, `GS` -3.09% alpha) against a +1.11% SPY benchmark return over the window — informal 50% hit rate on a small, non-ledger-backed sample. `CAT` alone both hit and still clears today's independent ranking floor (`PROMOTE`); `UNH`/`JPM` hit but no longer rank (`DOWNGRADE`); `XOM`/`WMT`/`GS` missed and no longer rank (`DROP`). Formal prediction-ledger settlement: 0 due (earliest open `target_date` system-wide is 2026-07-08).

## Regime Table

| Regime | Data Quality | Key Macro Risk | Ledger Rows |
| --- | --- | --- | --- |
| `BULL` (MEDIUM confidence) | `DELAYED_PARTIAL`; DQ=0.75 for factor scoring (2 of 4 families unsourceable) | VIX low (16.15) but a daily-timeframe pullback (SPY/QQQ/SOXX 20d momentum -1.3%/-4.3%/-8.0%) inside the broader 60d uptrend (+13.0%/+21.1%/+62.9%) — regime confidence capped at MEDIUM on this divergence, not HIGH. | L004, L005, L006–L019 |

## Core ETF Market Forecast (Summary of `03`)

| ETF | Entry | mu | sigma | Target (2026-07-31) | 70% CI | Confidence |
| --- | ---: | ---: | ---: | ---: | --- | --- |
| SPY | 745.76 | +2.0% | 4.4% | 760.68 | 726.44 – 794.91 | MEDIUM |
| QQQ | 725.17 | +3.2% | 8.5% | 748.38 | 684.48 – 812.28 | MEDIUM |
| SOXX | 599.70 | +5.0%* | 22.0% | 629.69 | 492.69 – 766.68 | MEDIUM |

*SOXX mu adjusted -1.5pp from the raw beta-scaled +6.55% for monthly-overbought/exhaustion signals (see `03`).

## Ranked Candidate Table (Monitoring Sleeve — Not Investable)

| Rank | Ticker | Entry | mu | sigma | Adj Score | Pctl | TD9(D) | RSI14(D) | MACD(D) | Confidence |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- | ---: | --- | --- |
| 1 | INTC | 127.02 | +6.0% | 26.2% | 0.375 | 100.0 | BUY_SETUP_2 | 49.2 | BELOW_SIGNAL | MEDIUM |
| 2 | AMAT | 650.91 | +6.0% | 26.8% | 0.353 | 96.6 | BUY_SETUP_2 | 54.0 | ABOVE_SIGNAL | MEDIUM |
| 3 | AMD | 540.88 | +5.0% | 23.4% | 0.296 | 93.1 | BUY_SETUP_1 | 52.3 | BELOW_SIGNAL | MEDIUM |
| 4 | MU | 1032.28 | +4.0% | 36.5% | 0.192 | 89.7 | BUY_SETUP_2 | 48.5 | BELOW_SIGNAL | MEDIUM |
| 5 | PANW | 352.04 | +4.0% | 16.1% | 0.179 | 86.2 | SELL_SETUP_9 | 78.5 | ABOVE_SIGNAL | MEDIUM |
| 6 | MRVL | 272.05 | +3.0% | 41.8% | 0.171 | 82.8 | BUY_SETUP_2 | 46.5 | BELOW_SIGNAL | MEDIUM |
| 7 | FLEX | 153.53 | +2.0% | 22.8% | 0.139 | 79.3 | BUY_SETUP_2 | 44.7 | BELOW_SIGNAL | MEDIUM |
| 8 | DELL | 425.25 | +2.0% | 35.5% | 0.087 | 75.9 | BUY_SETUP_1 | 52.6 | BELOW_SIGNAL | MEDIUM |
| 9 | MRNA | 72.50 | +2.0% | 22.5% | 0.084 | 72.4 | SELL_SETUP_5 | 80.7 | ABOVE_SIGNAL | MEDIUM |
| 10 | CAT | 991.41 | +1.0% | 15.5% | 0.080 | 69.0 | BUY_SETUP_2 | 50.9 | BEARISH_CROSS | MEDIUM |
| 11 | HUM | 409.42 | +1.0% | 11.4% | 0.077 | 65.5 | SELL_SETUP_6 | 72.0 | ABOVE_SIGNAL | MEDIUM |
| 12 | DDOG | 264.48 | +1.0% | 18.4% | 0.051 | 62.1 | SELL_SETUP_5 | 68.4 | ABOVE_SIGNAL | LOW |

Values above summarize `05_factor_scores.md § Technical Indicator Summary` and `technical_indicators.json` (daily timeframe); no new facts are introduced.

Full score attribution, all 30 sampled names (including the 18 below the 60th-percentile ranking floor), and per-name Recommendation Metrics Blocks are in `05_factor_scores.md` and `06_top_candidates.md`.

## Portfolio Analytics / No-Trade Rationale

No portfolio was drafted. `07_portfolio_proposal.md`'s Task 0 feasibility pre-check found zero investable names supplied by Factor Scoring — a data-completeness gate (Fund_Z and Sent_Z fully `UNAVAILABLE` universe-wide), not a sizing or constraint-band infeasibility. Per the Portfolio Construction Agent's Failure Rule, `NO_TRADE` is recommended directly rather than forcing a portfolio below the minimum investable count of 5. The Risk Committee (`08_risk_review.md`) reviewed and `APPROVE`d this recommendation.

## Assumptions and Limitations

- **Price source:** IBKR only. Yahoo Finance (the `technical_indicators.py` default fetch) is blocked by this session's egress policy — confirmed via a direct 403 from the proxy. No Yahoo data appears anywhere in this run.
- **Universe scope for scoring:** 30-name Sampled Universe Protocol fallback (not the full 515-name union) for price-history-dependent technicals and factor scoring, documented in `00`, `01`, `03`, `04`, `08`, `13` per `main.md`'s disclosure requirement. `eligible_universe.txt` itself (515 names) is unaffected — it required no network fetch.
- **Data-integrity exclusion:** `SNDK` was dropped after IBKR returned data identical to `MU`'s under a distinct contract ID; replaced with `COST`.
- **Earnings-date coverage:** sourced via WebSearch for the top-12 ranked names only (scope-limited); 18 of 30 sampled names carry `next_earnings_date = UNAVAILABLE`.
- **No fundamental or sentiment/positioning feed:** this is the primary driver of `NO_TRADE` and is expected to recur in future runs of this system until such a feed is wired (tracked as the Track B evolution proposal in `13_evolution_log.md`).
- **Confidence caps:** no name carries `HIGH` confidence this run (2-of-4-family ceiling and/or a same-day-pullback-vs-60d-uptrend divergence at the regime level).

## Next Scheduled Review

No durable scheduler is currently active (`runbook.md § Scheduler` — last job expired). Next run is manual, or upon `CronCreate` recreation per `runbook.md`. Weekly parameter review published today (`14_weekly_review.md`, Friday). Monthly structural review not due (2026-07-03 is not the last trading day of July).
