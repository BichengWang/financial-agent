```text
══════════════════════════════════════════════════════
QUANTITATIVE EQUITY SELECTION REPORT — 2026-07-28
Run Status: NO_TRADE
Classification: INTERNAL — INVESTMENT COMMITTEE USE
══════════════════════════════════════════════════════
```

## Executive Summary

A pre-open run on the 2026-07-27 close scored 514 of the 515 S&P 500 ∪ Nasdaq-100
index-union names, with all five Required inputs grounded and every published price confirmed by two
independent sources. The market is a `NEUTRAL` rotation: SPY flat and marginally below both moving
averages with falling volatility, while semis sit -21.19% below their 60-day
high and 41.44% of the universe carries negative beta. **Zero names are
investable and the run publishes `NO_TRADE`** — not because the candidates are weak, but because two of
four factor families do not exist at universe scale, which makes the "3 of 4 families" evidence threshold
unsatisfiable and holds data quality at 0.8, below the 0.85 completeness bar. 35 predictions
settled today, and this run establishes the exact date the `eff_n` evidence gate stops blocking
calibration work: **2026-08-05** for the second window.

## MoM Reflection Summary

Baseline `gpt-5-2026-06-30` (CROSS_MODEL_BASELINE,
28 days old). Over that month SPY returned
-0.67% and the baseline's equity forecasts hit
7/14
(50.00%) on alpha — a coin flip, and the same conclusion under the
alternative exact-target baseline. All three core-ETF forecasts settled MISS. Rolling calibration now
reads: hit rate 50.77%, CI coverage 74.62%, mean z -0.1973 over
n=260 — magnitude calibration healthy, **rank ordering inverted** (rank IC -0.1715). Full detail in `02`.

## Regime

| Regime | Data Quality | Key Macro Risk | Ledger Rows |
|---|---|---|---|
| **`NEUTRAL`** — rotation, not trend | `DELAYED`, DQ 0.8 | A risk-on turn would reverse the defensive leadership this book is built on: 15 of 24 published names carry negative beta | L002, L003, L007, L013, L015, L017–L020 |

## Core ETF Market Forecast

| ETF | Entry | mu | sigma | Target | 70% CI | Confidence |
|---|---|---|---|---|---|---|
| SPY | 739.09 | +0.50% | 3.64% | 742.79 | 714.83 – 770.74 | MEDIUM |
| QQQ | 682.12 | +0.86% | 7.27% | 687.99 | 636.43 – 739.55 | MEDIUM |
| SOXX | 516.23 | +1.82% | 18.58% | 525.64 | 425.88 – 625.41 | MEDIUM |

**Read these with the defect stated in `03`.** `mu = beta × SPY_mu` scales a magnitude by a direction, so
SOXX receives the most bullish forecast in the block (+1.82%) precisely because it is the
most volatile — while every ledger-backed piece of evidence about it points down. The formula is applied
unmodified because only the evolution agent may change it and Track A is gated at `eff_n = 1`.
Settled record to date: 20.83% over n=48.

## Ranked Candidates — monitoring sleeve only, 24 names

| # | Ticker | Sector | Adj Score | Pctl | Score Trace | Beta | 30d RVol | Sharpe | IR | TD9 D/W/M | RSI D | Days→Earn | mu | Target | 70% CI | Conf |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **RTX** | Industrials | +0.3651 | 100.00 | T +1.216 · M +0.610 · DQ 0.8 · P −0.00 | -0.068 | 9.36% | 0.607 | 0.701 | SELL_SETUP_4/SELL_SETUP_9/SELL_SETUP_1 | 77.33 | ~91d (2026-10-27, ESTIMATED_CADENCE ±5d) | +6.0% | 231.53 | 210.26 – 252.79 | MEDIUM |
| 2 | **TRV** | Finance | +0.3076 | 99.81 | T +0.865 · M +0.834 · DQ 0.8 · P −0.00 | -0.708 | 9.15% | 0.621 | 0.877 | SELL_SETUP_7/SELL_SETUP_9/SELL_SETUP_9 | 81.67 | ~91d (2026-10-27, ESTIMATED_CADENCE ±5d) | +6.0% | 413.77 | 376.61 – 450.93 | MEDIUM |
| 3 | **PAYX** | Industrials | +0.2953 | 99.61 | T +0.838 · M +0.784 · DQ 0.8 · P −0.00 | -0.610 | 9.15% | 0.621 | 0.724 | SELL_SETUP_1/SELL_SETUP_9/SELL_SETUP_2 | 67.48 | ~91d (2026-10-27, ESTIMATED_CADENCE ±5d) | +6.0% | 122.41 | 111.42 – 133.40 | MEDIUM |
| 4 | **SJM** | Consumer Staples | +0.2738 | 99.42 | T +0.780 · M +0.722 · DQ 0.8 · P −0.00 | -0.762 | 9.49% | 0.599 | 0.650 | SELL_SETUP_8/SELL_SETUP_3/SELL_SETUP_1 | 64.82 | 29d (2026-08-26, CONFIRMED) | +6.0% | 128.31 | 116.36 – 140.26 | MEDIUM |
| 5 | **CSX** | Industrials | +0.2702 | 99.22 | T +0.762 · M +0.728 · DQ 0.8 · P −0.00 | +0.113 | 7.42% | 0.766 | 0.869 | SELL_SETUP_3/SELL_SETUP_9/SELL_SETUP_9 | 64.1 | ~91d (2026-10-27, ESTIMATED_CADENCE ±5d) | +6.0% | 54.91 | 50.91 – 58.91 | MEDIUM |
| 6 | **DGX** | Health Care | +0.2688 | 99.03 | T +0.743 · M +0.754 · DQ 0.8 · P −0.00 | -0.585 | 9.45% | 0.601 | 0.829 | SELL_SETUP_8/SELL_SETUP_6/SELL_SETUP_6 | 75.04 | ~91d (2026-10-27, ESTIMATED_CADENCE ±5d) | +6.0% | 245.75 | 222.96 – 268.54 | MEDIUM |
| 7 | **BBY** | Consumer Discretionary | +0.2545 | 98.83 | T +0.958 · M +0.205 · DQ 0.8 · P −0.00 | +0.823 | 8.94% | 0.636 | 0.437 | SELL_SETUP_2/SELL_SETUP_9/SELL_SETUP_3 | 71.0 | 30d (2026-08-27, CONFIRMED) | +6.0% | 93.76 | 85.53 – 101.98 | MEDIUM |
| 8 | **IQV** | Health Care | +0.2520 | 98.64 | T +0.963 · M +0.174 · DQ 0.8 · P −0.00 | +0.148 | 11.29% | 0.503 | 0.480 | SELL_SETUP_3/SELL_SETUP_6/SELL_SETUP_2 | 65.6 | ~91d (2026-10-27, ESTIMATED_CADENCE ±5d) | +6.0% | 226.01 | 200.98 – 251.05 | MEDIUM |
| 9 | **MET** | Finance | +0.2493 | 98.44 | T +1.054 · M +0.803 · DQ 0.8 · P −0.10 | -0.005 | 7.04% | 0.807 | 0.918 | SELL_SETUP_2/SELL_SETUP_9/SELL_SETUP_4 | 68.04 | 8d (2026-08-05, CONFIRMED) | +6.0% | 100.90 | 93.93 – 107.87 | LOW |
| 10 | **UNP** | Industrials | +0.2453 | 98.25 | T +0.664 · M +0.717 · DQ 0.8 · P −0.00 | -0.163 | 7.63% | 0.745 | 0.817 | SELL_SETUP_3/SELL_SETUP_6/SELL_SETUP_9 | 62.46 | ~91d (2026-10-27, ESTIMATED_CADENCE ±5d) | +6.0% | 317.26 | 293.51 – 341.01 | MEDIUM |
| 11 | **IVZ** | Finance | +0.2413 | 98.05 | T +1.167 · M -0.323 · DQ 0.8 · P −0.00 | +1.527 | 11.00% | 0.517 | 0.630 | SELL_SETUP_4/SELL_SETUP_4/SELL_SETUP_9 | 60.68 | ~91d (2026-10-27, ESTIMATED_CADENCE ±5d) | +6.0% | 31.92 | 28.47 – 35.36 | MEDIUM |
| 12 | **PFG** | Finance | +0.2391 | 97.86 | T +0.602 · M +0.789 · DQ 0.8 · P −0.00 | -0.033 | 6.97% | 0.816 | 0.976 | SELL_SETUP_1/SELL_SETUP_9/SELL_SETUP_9 | 54.18 | ~91d (2026-10-27, ESTIMATED_CADENCE ±5d) | +6.0% | 117.97 | 109.91 – 126.03 | MEDIUM |
| 13 | **PRU** | Finance | +0.2375 | 97.66 | T +1.013 · M +0.787 · DQ 0.8 · P −0.10 | +0.268 | 6.16% | 0.922 | 1.005 | SELL_SETUP_2/SELL_SETUP_9/SELL_SETUP_2 | 72.36 | 7d (2026-08-04, CONFIRMED) | +6.0% | 129.20 | 121.39 – 137.02 | LOW |
| 14 | **NSC** | Industrials | +0.2355 | 97.47 | T +0.622 · M +0.719 · DQ 0.8 · P −0.00 | -0.101 | 7.24% | 0.785 | 0.859 | SELL_SETUP_3/SELL_SETUP_6/SELL_SETUP_4 | 64.18 | ~91d (2026-10-27, ESTIMATED_CADENCE ±5d) | +6.0% | 363.95 | 338.11 – 389.79 | MEDIUM |
| 15 | **ITW** | Industrials | +0.2271 | 97.27 | T +0.613 · M +0.666 · DQ 0.8 · P −0.00 | +0.464 | 6.66% | 0.854 | 0.959 | SELL_SETUP_3/SELL_SETUP_8/SELL_SETUP_1 | 66.39 | ~91d (2026-10-27, ESTIMATED_CADENCE ±5d) | +6.0% | 301.91 | 282.19 – 321.63 | MEDIUM |
| 16 | **CTAS** | Industrials | +0.2271 | 97.08 | T +0.677 · M +0.539 · DQ 0.8 · P −0.00 | -0.294 | 10.29% | 0.552 | 0.682 | SELL_SETUP_2/SELL_SETUP_6/SELL_SETUP_1 | 75.19 | ~91d (2026-10-27, ESTIMATED_CADENCE ±5d) | +6.0% | 223.64 | 201.07 – 246.21 | MEDIUM |
| 17 | **EXR** | Real Estate | +0.2265 | 96.88 | T +0.518 · M +0.851 · DQ 0.8 · P −0.00 | +0.030 | 6.36% | 0.894 | 0.921 | SELL_SETUP_2/BUY_SETUP_2/SELL_SETUP_1 | 55.25 | ~91d (2026-10-27, ESTIMATED_CADENCE ±5d) | +6.0% | 157.19 | 147.39 – 166.99 | MEDIUM |
| 18 | **MPC** | Energy | +0.2255 | 96.69 | T +1.064 · M +0.584 · DQ 0.8 · P −0.10 | -0.432 | 9.46% | 0.601 | 0.632 | BUY_SETUP_3/SELL_SETUP_6/SELL_SETUP_6 | 69.71 | 7d (2026-08-04, CONFIRMED) | +6.0% | 331.09 | 300.37 – 361.81 | LOW |
| 19 | **WELL** | Real Estate | +0.2197 | 96.49 | T +0.528 · M +0.775 · DQ 0.8 · P −0.00 | -0.573 | 6.89% | 0.825 | 0.843 | SELL_SETUP_9/SELL_SETUP_6/SELL_SETUP_4 | 67.61 | ~91d (2026-10-27, ESTIMATED_CADENCE ±5d) | +6.0% | 263.24 | 245.46 – 281.03 | MEDIUM |
| 20 | **CB** | Finance | +0.2176 | 96.30 | T +0.422 · M +0.968 · DQ 0.8 · P −0.00 | -0.980 | 8.03% | 0.708 | 1.123 | SELL_SETUP_3/BUY_SETUP_1/SELL_SETUP_9 | 59.4 | ~91d (2026-10-27, ESTIMATED_CADENCE ±5d) | +6.0% | 380.44 | 350.49 – 410.40 | MEDIUM |
| 21 | **LMT** | Industrials | +0.2063 | 96.10 | T +0.711 · M +0.296 · DQ 0.8 · P −0.00 | -0.460 | 12.18% | 0.466 | 0.650 | SELL_SETUP_4/SELL_SETUP_2/BUY_SETUP_3 | 70.25 | ~91d (2026-10-27, ESTIMATED_CADENCE ±5d) | +6.0% | 614.80 | 541.31 – 688.29 | MEDIUM |
| 22 | **PM** | Health Care | +0.2057 | 95.91 | T +0.555 · M +0.604 · DQ 0.8 · P −0.00 | -0.546 | 9.26% | 0.614 | 0.723 | SELL_SETUP_2/SELL_SETUP_3/SELL_SETUP_1 | 62.03 | ~91d (2026-10-27, ESTIMATED_CADENCE ±5d) | +6.0% | 207.40 | 188.57 – 226.23 | MEDIUM |
| 23 | **BNY** | Finance | +0.2022 | 95.71 | T +0.547 · M +0.592 · DQ 0.8 · P −0.00 | +0.564 | 7.21% | 0.788 | 0.937 | BUY_SETUP_1/SELL_SETUP_9/SELL_SETUP_9 | 62.23 | ~91d (2026-10-27, ESTIMATED_CADENCE ±5d) | +6.0% | 167.24 | 155.41 – 179.06 | MEDIUM |
| 24 | **PKG** | Consumer Discretionary | +0.1749 | 91.81 | T +0.681 · M +0.096 · DQ 0.8 · P −0.00 | +0.806 | 9.54% | 0.491 | 0.510 | SELL_SETUP_3/SELL_SETUP_8/SELL_SETUP_2 | 69.48 | ~91d (2026-10-27, ESTIMATED_CADENCE ±5d) | +5.0% | 264.99 | 239.95 – 290.02 | MEDIUM |

## No-Trade Rationale

Three independent grounds, each sufficient on its own:

| # | Ground | Margin |
|---|---|---|
| 1 | **Evidence Threshold #2** — "≥ 3 of 4 factor families non-negative" is unsatisfiable: `Fund_Z` and `Sent_Z` are `UNAVAILABLE` universe-wide | structural, not marginal |
| 2 | **Evidence Threshold #4** — data completeness ≥ 85% fails at DQ 0.8 | 5pp short |
| 3 | **Event concentration** — 3 published names report inside 14 days vs a limit of 2 | 1 over |

A fourth finding — max attainable sleeve beta 0.899853 vs a 0.90 floor —
is reported as **corroborating only**: it misses by 1.47 basis points, which
is inside estimation error on a 60-day regression and should not be treated as a structural result.

Correlation (0.1931 vs cap 0.45), 95th-pctl drawdown
(7.57% vs cap 8%) and sector concentration
(33.3% vs cap 30%) all pass. **The sleeve is
disqualified for being too defensive, never for being too risky.**

## Assumptions and Limitations

1. **Two of four factor families are missing.** Scores rest on Technical (0.30) and Macro (0.15) only —
   45% of the intended weight. This is the single change that would make `GO` structurally reachable.
2. **VaR95, CVaR95 and the 95th-pctl drawdown are parametric** and assume normal returns.
3. **`mu` is a table lookup**, not a per-name view; no positive adjustment was applied anywhere.
4. **Earnings coverage is bounded by design** — 58 of 514 names, converged so the
   post-penalty top-20 is fully grounded. 7 top-30 entrants were never
   grounded and are excluded rather than published penalty-free.
5. **Bulk price history has no redundancy** — stockanalysis.com is the only working bulk source; Yahoo is
   429-blocked and Nasdaq's bulk endpoint serves a bot challenge.
6. **The score's rank ordering is currently inverted** (rank IC -0.1715). Every forecast here is a
   settleable paper record, not a recommendation.

## Next Scheduled Review

| When | What |
|---|---|
| 2026-07-28 12:15 ET | Midday monitor — observation only |
| 2026-07-28 16:20 ET | Close log |
| 2026-07-31 17:15 ET | Weekly parameter review (Friday) + month-end structural review |
| **2026-08-05** | **`eff_n` reaches 2** — first movement in the Track A evidence gate since it was introduced |
| 2026-08-25 | Target date for all 24 forecasts published today |
