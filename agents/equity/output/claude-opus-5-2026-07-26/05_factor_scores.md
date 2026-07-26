# 05 Factor Scores — 2026-07-26

Primary home for `Adj Score` explainability. 514 names scored; percentiles labelled **`INDEX_UNION_PCTL (n=514)`**. Every numeric field traces to a `01_preflight.md` ledger row.

## Scoring Architecture

Baseline family weights are unchanged: Fundamental 0.30, Technical 0.30, Sentiment 0.25, Macro 0.15.

`Fund_Z` and `Sent_Z` are **`UNAVAILABLE` universe-wide** (L144, L145). Per `rules.md § Family Aggregation` their displayed contribution is `0.00 (UNAVAILABLE)`, the data-quality multiplier is lowered, and **they do not count toward the 3-of-4 threshold**. The effective arithmetic is:

`Adj Score = (0.30·Tech_Z + 0.15·Macro_Z) × 0.80 − Penalties`

**Family construction.** Each metric is winsorized at the 5th/95th percentile across the 514-name universe, then z-scored; a family is the equal-weighted mean of its available metric z-scores (≥2 required, else `UNAVAILABLE`).

| Family | Metrics (polarity) | n signals |
|---|---|---|
| **Technical / Price** | 20d momentum (+), 60d momentum (+), RS20 vs SPY (+), RS60 vs SPY (+), MA alignment daily+weekly (+), MACD state daily+weekly (+), 20d volume ratio (+), RSI headroom `70 − RSI14_d` (+) | 8 |
| **Macro / Regime** | 60d beta (**−**), 30d realized vol (**−**), 60d max drawdown (+, i.e. shallower is better) | 3 |
| Fundamental | — | `UNAVAILABLE` (L144) |
| Sentiment / Positioning | — | `UNAVAILABLE` (L145) |

**Encodings.** MA alignment `BULLISH/MIXED/BEARISH` → `+1 / 0 / −1`. MACD `BULLISH_CROSS / ABOVE_SIGNAL / ON_SIGNAL / BELOW_SIGNAL / BEARISH_CROSS` → `+1 / +0.5 / 0 / −0.5 / −1`. RSI enters as headroom-to-overbought so polarity is uniformly "higher is better" and extended names are not rewarded.

**Return basis.** All momentum, relative-strength, volatility, beta, tracking-error and drawdown inputs are computed from **adjusted closes** this run (L003; rationale in `13`). Entry, target and CI prices use the unadjusted 2026-07-24 close (L002).

**Disclosed judgment — defensive Macro polarity (`INFERRED`, L140).** Lower beta, lower realized vol and shallower drawdown score *better* this run. This is a regime-conditional reading of the evidence in `03` (index flat and below both MAs, SOXX −19.54% from its high, 41.2% of the universe at negative beta, TLT −4.45%), **not** a permanent rule and **not** a family-weight change — altering weights would require the evolution policy and is gated off at `eff_n = 1`. It is flagged here because it materially shapes the leaderboard: it is the single largest reason insurers, rails, utilities and defense fill the top of the book.

**Data-quality multiplier: 0.80** for every name — "notable coverage gaps", being two of four families `UNAVAILABLE` plus the entire Enhancing block (L146). Since 0.80 < 0.85, `rules.md § Evidence Thresholds` #4 independently forbids marking any name investable.

**Calibration feedback applied** (from `02 § 0`): rank IC −0.1282 over n=203 ≥ 20 → confidence capped at `MEDIUM`; CI coverage 75.37% is inside the healthy band, so no sigma-widening fires. **No positive per-name `mu` adjustments were made anywhere** — every `mu` is the unmodified mu-Calibration-Table value for the name's percentile band (L030).

## Penalties Applied

| Penalty | Rule | Value | Names affected (universe) | In published set |
|---|---|---|---|---|
| Earnings inside 14 calendar days, buffered by the estimate band | `rules.md § Risk Controls` | **−0.10**, confidence capped `LOW` | 37 | 5 (GD, MPC, MET, VLO, HIG) |
| 30d realized vol > 2× universe median (0.0961 → threshold 0.1922) | `rules.md § Risk Controls` | −0.05 | 31 | 0 |
| TD-9 daily sell-setup 9 **and** RSI(14) daily ≥ 70 (exhaustion confirmed by price action) | `rules.md § TD-9 Definition` | −0.05 | 4 (ALLE, CVX, WELL, XOM) | 0 |
| Unstable earnings profile | `rules.md § Risk Controls` | **not applied** | — | Requires fundamentals — `UNAVAILABLE` (L144). Disclosed as an *unapplied* penalty, not as absent risk |

71 of 514 names carry at least one penalty; one name (WELL) carries two (−0.15).

**Earnings-date grounding.** 56 names were fetched across two bounded passes (L022–L024): 34 `CONFIRMED` from `api.nasdaq.com/api/analyst/{sym}/earnings-date`, 21 resolved as `ESTIMATED_CADENCE +91d` (vendor-empty *with* a print-like signature in the last 12 sessions → next report is outside the 14-day window → no penalty), and 1 (HIG) resolved as `ESTIMATED_PRINT_WEEK (±5d)` (vendor-empty *without* a signature → conservative penalized branch). The 6 names that entered the top 30 only on the third pass are excluded from publication rather than scored penalty-free.

## Ranked Candidate Table — Published Set (24 names)

Field derivations per `rules.md § Price and Target Citation Standard`. `mu` from the mu Calibration Table band for each name's percentile; `sigma` = `REALIZED_VOL_30D` (L013, L030); `target_price = entry × (1 + mu)`; CI bounds = `entry × (1 + mu ± 1.04σ)`. Target date **2026-08-23** (`run_date + 28d`).

| Ticker | Company/Sector | Entry | Date | Tag | Adj Score | Score Trace | Pctl | Beta | 30d RVol | Sharpe | Sortino | IR | Kelly .25 | VaR95 | CVaR95 | MaxDD60 | TD9 D/W/M | RSI14 D/W/M | MACD D/W/M | Days→Earn | mu | sigma | SigSrc | Target | Target Date | CI Lo | CI Hi | Ledger | Conf |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| TRV | Finance | 387.26 | 2026-07-24 | HISTORICAL | +0.3705 | (0.30×+1.124 + 0.15×+0.840)×0.80 − 0.00 = +0.3705 | 100.0 | -0.701 | 9.33% | 0.6093 | 1.7066 | 0.7982 | 0.0500 | -9.39% | -13.21% | -5.96% | SELL_SETUP_6/SELL_SETUP_8/SELL_SETUP_9 | 80.9/79.7/77.2 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | ~+91d (ESTIMATED_CADENCE ±5d) | +6.0% | 9.33% | REALIZED_VOL_30D | 410.50 | 2026-08-23 | 372.93 | 448.06 | L001-L027,L030,L135 | LOW |
| RTX | Industrials | 212.79 | 2026-07-24 | HISTORICAL | +0.3089 | (0.30×+0.988 + 0.15×+0.598)×0.80 − 0.00 = +0.3089 | 99.8 | -0.061 | 9.75% | 0.5826 | 1.0595 | 0.6933 | 0.0500 | -10.09% | -14.09% | -5.58% | SELL_SETUP_3/SELL_SETUP_9/SELL_SETUP_1 | 74.0/66.8/74.9 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | ~+91d (ESTIMATED_CADENCE ±5d) | +6.0% | 9.75% | REALIZED_VOL_30D | 225.56 | 2026-08-23 | 203.97 | 247.14 | L001-L027,L030,L135 | LOW |
| PAYX | Industrials | 113.55 | 2026-07-24 | HISTORICAL | +0.3072 | (0.30×+0.888 + 0.15×+0.783)×0.80 − 0.00 = +0.3072 | 99.6 | -0.614 | 9.45% | 0.6016 | 1.3668 | 0.6723 | 0.0500 | -9.59% | -13.46% | -6.35% | BUY_SETUP_3/SELL_SETUP_9/SELL_SETUP_2 | 64.7/64.5/50.2 | ABOVE_SIGNAL/ABOVE_SIGNAL/BELOW_SIGNAL | ~+91d (ESTIMATED_CADENCE ±5d) | +6.0% | 9.45% | REALIZED_VOL_30D | 120.36 | 2026-08-23 | 109.21 | 131.52 | L001-L027,L030,L135 | LOW |
| DGX | Health Care | 227.86 | 2026-07-24 | HISTORICAL | +0.3058 | (0.30×+0.891 + 0.15×+0.766)×0.80 − 0.00 = +0.3058 | 99.4 | -0.576 | 9.55% | 0.5947 | 2.0143 | 0.7637 | 0.0500 | -9.76% | -13.68% | -6.22% | SELL_SETUP_7/SELL_SETUP_5/SELL_SETUP_6 | 72.7/68.3/68.7 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | ~+91d (ESTIMATED_CADENCE ±5d) | +6.0% | 9.55% | REALIZED_VOL_30D | 241.53 | 2026-08-23 | 218.89 | 264.17 | L001-L027,L030,L135 | LOW |
| UNP | Industrials | 307.32 | 2026-07-24 | HISTORICAL | +0.2992 | (0.30×+0.866 + 0.15×+0.762)×0.80 − 0.00 = +0.2992 | 99.2 | -0.164 | 7.32% | 0.7767 | 1.1652 | 0.8162 | 0.0500 | -6.07% | -9.07% | -7.58% | SELL_SETUP_2/SELL_SETUP_5/SELL_SETUP_9 | 73.0/73.3/68.6 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | ~+91d (ESTIMATED_CADENCE ±5d) | +6.0% | 7.32% | REALIZED_VOL_30D | 325.76 | 2026-08-23 | 302.38 | 349.14 | L001-L027,L030,L135 | LOW |
| PCG | Utilities | 17.85 | 2026-07-24 | HISTORICAL | +0.2807 | (0.30×+0.726 + 0.15×+0.888)×0.80 − 0.00 = +0.2807 | 99.0 | -0.260 | 7.12% | 0.7979 | 1.3562 | 0.8028 | 0.0500 | -5.75% | -8.67% | -5.71% | SELL_SETUP_3/SELL_SETUP_3/SELL_SETUP_1 | 60.1/58.5/55.6 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | ~+91d (ESTIMATED_CADENCE ±5d) | +6.0% | 7.12% | REALIZED_VOL_30D | 18.92 | 2026-08-23 | 17.60 | 20.24 | L001-L027,L030,L135 | LOW |
| CSX | Industrials | 53.23 | 2026-07-24 | HISTORICAL | +0.2777 | (0.30×+0.775 + 0.15×+0.764)×0.80 − 0.00 = +0.2777 | 98.8 | +0.113 | 7.22% | 0.7871 | 1.6322 | 0.8919 | 0.0500 | -5.91% | -8.87% | -4.20% | SELL_SETUP_2/SELL_SETUP_9/SELL_SETUP_9 | 76.1/78.9/76.5 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | ~+91d (ESTIMATED_CADENCE ±5d) | +6.0% | 7.22% | REALIZED_VOL_30D | 56.42 | 2026-08-23 | 52.43 | 60.42 | L001-L027,L030,L135 | LOW |
| WRB | Finance | 75.46 | 2026-07-24 | HISTORICAL | +0.2523 | (0.30×+0.544 + 0.15×+1.015)×0.80 − 0.00 = +0.2523 | 98.6 | -0.922 | 7.27% | 0.7816 | 1.4247 | 0.9987 | 0.0500 | -6.00% | -8.98% | -7.59% | SELL_SETUP_5/SELL_SETUP_5/SELL_SETUP_1 | 67.4/65.2/61.9 | BULLISH_CROSS/ABOVE_SIGNAL/BELOW_SIGNAL | ~+91d (ESTIMATED_CADENCE ±5d) | +6.0% | 7.27% | REALIZED_VOL_30D | 79.99 | 2026-08-23 | 74.28 | 85.69 | L001-L027,L030,L135 | LOW |
| TMO | Industrials | 568.26 | 2026-07-24 | HISTORICAL | +0.2471 | (0.30×+0.837 + 0.15×+0.385)×0.80 − 0.00 = +0.2471 | 98.4 | +0.098 | 10.22% | 0.5560 | 1.9289 | 0.5871 | 0.0500 | -10.86% | -15.05% | -8.48% | SELL_SETUP_2/SELL_SETUP_9/SELL_SETUP_1 | 70.8/62.9/55.8 | ABOVE_SIGNAL/ABOVE_SIGNAL/BULLISH_CROSS | ~+91d (ESTIMATED_CADENCE ±5d) | +6.0% | 10.22% | REALIZED_VOL_30D | 602.36 | 2026-08-23 | 541.95 | 662.76 | L001-L027,L030,L135 | LOW |
| NSC | Industrials | 350.66 | 2026-07-24 | HISTORICAL | +0.2423 | (0.30×+0.634 + 0.15×+0.751)×0.80 − 0.00 = +0.2423 | 98.2 | -0.100 | 7.05% | 0.8056 | 1.3174 | 0.8521 | 0.0500 | -5.64% | -8.53% | -7.86% | SELL_SETUP_2/SELL_SETUP_5/SELL_SETUP_4 | 73.2/71.0/67.4 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | ~+91d (ESTIMATED_CADENCE ±5d) | +6.0% | 7.05% | REALIZED_VOL_30D | 371.70 | 2026-08-23 | 345.98 | 397.42 | L001-L027,L030,L135 | LOW |
| GD | Industrials | 386.75 | 2026-07-24 | HISTORICAL | +0.2366 | (0.30×+1.024 + 0.15×+0.757)×0.80 − 0.10 = +0.2366 | 98.0 | -0.019 | 7.69% | 0.7388 | 1.2455 | 0.7445 | 0.0500 | -6.69% | -9.84% | -5.70% | SELL_SETUP_5/SELL_SETUP_4/SELL_SETUP_1 | 70.3/65.0/78.3 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | 2026-07-29 (3d, CONFIRMED) | +6.0% | 7.69% | REALIZED_VOL_30D | 409.95 | 2026-08-23 | 379.02 | 440.89 | L001-L027,L030,L135 | LOW |
| PM | Health Care | 193.00 | 2026-07-24 | HISTORICAL | +0.2286 | (0.30×+0.649 + 0.15×+0.608)×0.80 − 0.00 = +0.2286 | 97.9 | -0.540 | 9.45% | 0.6014 | 1.2833 | 0.6796 | 0.0500 | -9.59% | -13.46% | -10.01% | SELL_SETUP_1/SELL_SETUP_2/SELL_SETUP_1 | 59.7/64.1/68.9 | ABOVE_SIGNAL/ABOVE_SIGNAL/BULLISH_CROSS | ~+91d (ESTIMATED_CADENCE ±5d) | +6.0% | 9.45% | REALIZED_VOL_30D | 204.58 | 2026-08-23 | 185.61 | 223.55 | L001-L027,L030,L135 | LOW |
| MPC | Energy | 309.24 | 2026-07-24 | HISTORICAL | +0.2267 | (0.30×+1.067 + 0.15×+0.589)×0.80 − 0.10 = +0.2267 | 97.7 | -0.439 | 9.70% | 0.5858 | 1.0384 | 0.5927 | 0.0500 | -10.00% | -13.98% | -9.09% | BUY_SETUP_2/SELL_SETUP_5/SELL_SETUP_6 | 68.2/73.2/80.9 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | 2026-08-04 (9d, CONFIRMED) | +6.0% | 9.70% | REALIZED_VOL_30D | 327.79 | 2026-08-23 | 296.60 | 358.99 | L001-L027,L030,L135 | LOW |
| CTAS | Industrials | 205.91 | 2026-07-24 | HISTORICAL | +0.2248 | (0.30×+0.656 + 0.15×+0.561)×0.80 − 0.00 = +0.2248 | 97.5 | -0.290 | 10.33% | 0.5500 | 1.2145 | 0.6662 | 0.0500 | -11.05% | -15.28% | -7.19% | SELL_SETUP_1/SELL_SETUP_5/SELL_SETUP_1 | 72.1/65.0/58.4 | ABOVE_SIGNAL/ABOVE_SIGNAL/BELOW_SIGNAL | ~+91d (ESTIMATED_CADENCE ±5d) | +6.0% | 10.33% | REALIZED_VOL_30D | 218.26 | 2026-08-23 | 196.14 | 240.39 | L001-L027,L030,L135 | LOW |
| SJM | Consumer Staples | 118.32 | 2026-07-24 | HISTORICAL | +0.2245 | (0.30×+0.563 + 0.15×+0.745)×0.80 − 0.00 = +0.2245 | 97.3 | -0.756 | 9.47% | 0.6000 | 1.0687 | 0.6068 | 0.0500 | -9.63% | -13.51% | -8.42% | SELL_SETUP_7/SELL_SETUP_2/SELL_SETUP_1 | 61.2/63.6/56.6 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | 2026-08-26 (31d, CONFIRMED) | +6.0% | 9.47% | REALIZED_VOL_30D | 125.42 | 2026-08-23 | 113.76 | 137.07 | L001-L027,L030,L135 | LOW |
| CB | Finance | 359.75 | 2026-07-24 | HISTORICAL | +0.2205 | (0.30×+0.430 + 0.15×+0.976)×0.80 − 0.00 = +0.2205 | 97.1 | -0.977 | 8.21% | 0.6925 | 1.3469 | 1.0161 | 0.0500 | -7.54% | -10.90% | -6.57% | SELL_SETUP_2/SELL_SETUP_5/SELL_SETUP_9 | 60.1/65.1/69.4 | BELOW_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | ~+91d (ESTIMATED_CADENCE ±5d) | +6.0% | 8.21% | REALIZED_VOL_30D | 381.33 | 2026-08-23 | 350.64 | 412.03 | L001-L027,L030,L135 | LOW |
| LMT | Industrials | 582.60 | 2026-07-24 | HISTORICAL | +0.2186 | (0.30×+0.776 + 0.15×+0.269)×0.80 − 0.00 = +0.2186 | 96.9 | -0.459 | 12.88% | 0.4411 | 1.1430 | 0.6207 | 0.0500 | -15.26% | -20.54% | -10.40% | SELL_SETUP_3/SELL_SETUP_1/BUY_SETUP_3 | 71.7/57.5/58.9 | ABOVE_SIGNAL/BELOW_SIGNAL/ABOVE_SIGNAL | ~+91d (ESTIMATED_CADENCE ±5d) | +6.0% | 12.88% | REALIZED_VOL_30D | 617.56 | 2026-08-23 | 539.50 | 695.61 | L001-L027,L030,L135 | LOW |
| WAB | Industrials | 302.50 | 2026-07-24 | HISTORICAL | +0.2103 | (0.30×+0.848 + 0.15×+0.057)×0.80 − 0.00 = +0.2103 | 96.7 | +0.806 | 11.10% | 0.5117 | 0.9780 | 0.6561 | 0.0500 | -12.32% | -16.88% | -8.71% | SELL_SETUP_4/SELL_SETUP_1/SELL_SETUP_9 | 75.1/74.3/77.6 | ABOVE_SIGNAL/BULLISH_CROSS/ABOVE_SIGNAL | ~+91d (ESTIMATED_CADENCE ±5d) | +6.0% | 11.10% | REALIZED_VOL_30D | 320.65 | 2026-08-23 | 285.71 | 355.59 | L001-L027,L030,L135 | LOW |
| EQR | Real Estate | 67.86 | 2026-07-24 | HISTORICAL | +0.2089 | (0.30×+0.408 + 0.15×+0.924)×0.80 − 0.00 = +0.2089 | 96.5 | -0.133 | 6.06% | 0.9381 | 1.5081 | 1.1322 | 0.0500 | -3.99% | -6.48% | -6.01% | BUY_SETUP_3/SELL_SETUP_5/SELL_SETUP_4 | 49.7/58.6/57.9 | BELOW_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | ~+91d (ESTIMATED_CADENCE ±5d) | +6.0% | 6.06% | REALIZED_VOL_30D | 71.93 | 2026-08-23 | 67.66 | 76.21 | L001-L027,L030,L135 | LOW |
| PKG | Consumer Discretionary | 254.39 | 2026-07-24 | HISTORICAL | +0.2040 | (0.30×+0.810 + 0.15×+0.081)×0.80 − 0.00 = +0.2040 | 96.3 | +0.811 | 9.99% | 0.5690 | 1.2579 | 0.6476 | 0.0500 | -10.48% | -14.57% | -10.43% | SELL_SETUP_2/SELL_SETUP_7/SELL_SETUP_2 | 72.2/67.1/68.1 | BULLISH_CROSS/ABOVE_SIGNAL/ABOVE_SIGNAL | ~+91d (ESTIMATED_CADENCE ±5d) | +6.0% | 9.99% | REALIZED_VOL_30D | 269.65 | 2026-08-23 | 243.23 | 296.07 | L001-L027,L030,L135 | LOW |
| BNY | Finance | 158.91 | 2026-07-24 | HISTORICAL | +0.1964 | (0.30×+0.521 + 0.15×+0.594)×0.80 − 0.00 = +0.1964 | 96.1 | +0.566 | 7.38% | 0.7695 | 1.4931 | 0.9703 | 0.0500 | -6.19% | -9.21% | -3.34% | SELL_SETUP_2/SELL_SETUP_9/SELL_SETUP_9 | 63.5/84.1/90.9 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | ~+91d (ESTIMATED_CADENCE ±5d) | +6.0% | 7.38% | REALIZED_VOL_30D | 168.44 | 2026-08-23 | 156.24 | 180.65 | L001-L027,L030,L135 | LOW |
| MET | Finance | 94.83 | 2026-07-24 | HISTORICAL | +0.1955 | (0.30×+0.830 + 0.15×+0.801)×0.80 − 0.10 = +0.1955 | 95.9 | -0.006 | 7.26% | 0.7832 | 1.1803 | 0.9085 | 0.0500 | -5.97% | -8.95% | -4.77% | SELL_SETUP_1/SELL_SETUP_9/SELL_SETUP_4 | 67.2/71.0/67.7 | BELOW_SIGNAL/ABOVE_SIGNAL/BULLISH_CROSS | 2026-08-05 (10d, CONFIRMED) | +6.0% | 7.26% | REALIZED_VOL_30D | 100.52 | 2026-08-23 | 93.36 | 107.68 | L001-L027,L030,L135 | LOW |
| VLO | Energy | 302.50 | 2026-07-24 | HISTORICAL | +0.1859 | (0.30×+0.946 + 0.15×+0.491)×0.80 − 0.10 = +0.1859 | 94.7 | -0.737 | 11.78% | 0.3975 | 0.9211 | 0.4496 | 0.0500 | -14.44% | -19.27% | -9.62% | BUY_SETUP_2/SELL_SETUP_5/SELL_SETUP_9 | 63.1/71.6/82.3 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | 2026-07-30 (4d, CONFIRMED) | +5.0% | 11.78% | REALIZED_VOL_30D | 317.62 | 2026-08-23 | 280.57 | 354.68 | L001-L027,L030,L135 | LOW |
| HIG | Finance | 140.53 | 2026-07-24 | HISTORICAL | +0.1830 | (0.30×+0.681 + 0.15×+0.997)×0.80 − 0.10 = +0.1830 | 94.3 | -0.575 | 6.26% | 0.7479 | 1.4484 | 0.8304 | 0.0500 | -5.33% | -7.90% | -7.51% | SELL_SETUP_5/SELL_SETUP_5/SELL_SETUP_1 | 58.2/58.4/64.0 | ABOVE_SIGNAL/ABOVE_SIGNAL/BELOW_SIGNAL | print week (ESTIMATED ±5d) | +5.0% | 6.26% | REALIZED_VOL_30D | 147.56 | 2026-08-23 | 138.41 | 156.71 | L001-L027,L030,L135 | LOW |

## Score Attribution

Every ranked name discloses family z-scores, DQ, penalties, drivers and metric ledger rows. Two families read `UNAVAILABLE` on every row — no missing metric is presented as neutral or supportive anywhere in this package.

| Ticker | Fund_Z | Tech_Z | Sent_Z | Macro_Z | Composite_Z | DQ | Penalties | Adj Score | Families | Top Positive Drivers | Top Negative Drivers | Metric Ledger Rows |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| TRV | UNAVAILABLE | +1.124 | UNAVAILABLE | +0.840 | +0.4632 | 0.80 | 0.00 | +0.3705 | 2/4 | 20d momentum: +21.67%; 60d momentum: +25.44%; RS20 vs SPY: +21.04% | INSUFFICIENT_SOURCEABLE_DRIVERS | L001-L027,L030,L135,L144,L145 |
| RTX | UNAVAILABLE | +0.988 | UNAVAILABLE | +0.598 | +0.3861 | 0.80 | 0.00 | +0.3089 | 2/4 | 20d momentum: +14.04%; 60d momentum: +21.63%; RS20 vs SPY: +13.41% | 30d realized vol: +0.0975 | L001-L027,L030,L135,L144,L145 |
| PAYX | UNAVAILABLE | +0.888 | UNAVAILABLE | +0.783 | +0.3840 | 0.80 | 0.00 | +0.3072 | 2/4 | 20d momentum: +17.40%; 60d momentum: +26.40%; RS20 vs SPY: +16.77% | INSUFFICIENT_SOURCEABLE_DRIVERS | L001-L027,L030,L135,L144,L145 |
| DGX | UNAVAILABLE | +0.891 | UNAVAILABLE | +0.766 | +0.3823 | 0.80 | 0.00 | +0.3058 | 2/4 | 20d momentum: +10.93%; 60d momentum: +17.30%; RS20 vs SPY: +10.30% | INSUFFICIENT_SOURCEABLE_DRIVERS | L001-L027,L030,L135,L144,L145 |
| UNP | UNAVAILABLE | +0.866 | UNAVAILABLE | +0.762 | +0.3740 | 0.80 | 0.00 | +0.2992 | 2/4 | 20d momentum: +14.79%; 60d momentum: +15.38%; RS20 vs SPY: +14.16% | INSUFFICIENT_SOURCEABLE_DRIVERS | L001-L027,L030,L135,L144,L145 |
| PCG | UNAVAILABLE | +0.726 | UNAVAILABLE | +0.888 | +0.3508 | 0.80 | 0.00 | +0.2807 | 2/4 | 20d momentum: +4.81%; 60d momentum: +10.10%; RS20 vs SPY: +4.18% | INSUFFICIENT_SOURCEABLE_DRIVERS | L001-L027,L030,L135,L144,L145 |
| CSX | UNAVAILABLE | +0.775 | UNAVAILABLE | +0.764 | +0.3471 | 0.80 | 0.00 | +0.2777 | 2/4 | 20d momentum: +12.20%; 60d momentum: +18.05%; RS20 vs SPY: +11.57% | 60d beta (defensive polarity): +0.1130 | L001-L027,L030,L135,L144,L145 |
| WRB | UNAVAILABLE | +0.544 | UNAVAILABLE | +1.015 | +0.3154 | 0.80 | 0.00 | +0.2523 | 2/4 | 20d momentum: +8.90%; 60d momentum: +13.44%; RS20 vs SPY: +8.27% | INSUFFICIENT_SOURCEABLE_DRIVERS | L001-L027,L030,L135,L144,L145 |
| TMO | UNAVAILABLE | +0.837 | UNAVAILABLE | +0.385 | +0.3089 | 0.80 | 0.00 | +0.2471 | 2/4 | 20d momentum: +12.36%; 60d momentum: +20.97%; RS20 vs SPY: +11.73% | 60d beta (defensive polarity): +0.0977; 30d realized vol: +0.1022 | L001-L027,L030,L135,L144,L145 |
| NSC | UNAVAILABLE | +0.634 | UNAVAILABLE | +0.751 | +0.3029 | 0.80 | 0.00 | +0.2423 | 2/4 | 20d momentum: +12.37%; 60d momentum: +11.20%; RS20 vs SPY: +11.74% | INSUFFICIENT_SOURCEABLE_DRIVERS | L001-L027,L030,L135,L144,L145 |
| GD | UNAVAILABLE | +1.024 | UNAVAILABLE | +0.757 | +0.4208 | 0.80 | 0.10 | +0.2366 | 2/4 | 20d momentum: +12.69%; 60d momentum: +23.84%; RS20 vs SPY: +12.06% | INSUFFICIENT_SOURCEABLE_DRIVERS | L001-L027,L030,L135,L144,L145 |
| PM | UNAVAILABLE | +0.649 | UNAVAILABLE | +0.608 | +0.2858 | 0.80 | 0.00 | +0.2286 | 2/4 | 20d momentum: +7.86%; 60d momentum: +17.31%; RS20 vs SPY: +7.23% | 60d max drawdown: -0.1001 | L001-L027,L030,L135,L144,L145 |
| MPC | UNAVAILABLE | +1.067 | UNAVAILABLE | +0.589 | +0.4084 | 0.80 | 0.10 | +0.2267 | 2/4 | 20d momentum: +21.96%; 60d momentum: +33.46%; RS20 vs SPY: +21.33% | 30d realized vol: +0.0970 | L001-L027,L030,L135,L144,L145 |
| CTAS | UNAVAILABLE | +0.656 | UNAVAILABLE | +0.561 | +0.2810 | 0.80 | 0.00 | +0.2248 | 2/4 | 20d momentum: +21.78%; 60d momentum: +18.51%; RS20 vs SPY: +21.15% | 30d realized vol: +0.1033 | L001-L027,L030,L135,L144,L145 |
| SJM | UNAVAILABLE | +0.563 | UNAVAILABLE | +0.745 | +0.2806 | 0.80 | 0.00 | +0.2245 | 2/4 | 20d momentum: +5.17%; 60d momentum: +22.01%; RS20 vs SPY: +4.54% | INSUFFICIENT_SOURCEABLE_DRIVERS | L001-L027,L030,L135,L144,L145 |
| CB | UNAVAILABLE | +0.430 | UNAVAILABLE | +0.976 | +0.2756 | 0.80 | 0.00 | +0.2205 | 2/4 | 20d momentum: +8.74%; 60d momentum: +9.24%; RS20 vs SPY: +8.11% | INSUFFICIENT_SOURCEABLE_DRIVERS | L001-L027,L030,L135,L144,L145 |
| LMT | UNAVAILABLE | +0.776 | UNAVAILABLE | +0.269 | +0.2732 | 0.80 | 0.00 | +0.2186 | 2/4 | 20d momentum: +15.36%; 60d momentum: +14.47%; RS20 vs SPY: +14.73% | 30d realized vol: +0.1288; 60d max drawdown: -0.1040 | L001-L027,L030,L135,L144,L145 |
| WAB | UNAVAILABLE | +0.848 | UNAVAILABLE | +0.057 | +0.2629 | 0.80 | 0.00 | +0.2103 | 2/4 | 20d momentum: +7.10%; 60d momentum: +15.08%; RS20 vs SPY: +6.47% | 60d beta (defensive polarity): +0.8056; 30d realized vol: +0.1110 | L001-L027,L030,L135,L144,L145 |
| EQR | UNAVAILABLE | +0.408 | UNAVAILABLE | +0.924 | +0.2611 | 0.80 | 0.00 | +0.2089 | 2/4 | 20d momentum: +2.08%; 60d momentum: +5.24%; RS20 vs SPY: +1.45% | INSUFFICIENT_SOURCEABLE_DRIVERS | L001-L027,L030,L135,L144,L145 |
| PKG | UNAVAILABLE | +0.810 | UNAVAILABLE | +0.081 | +0.2550 | 0.80 | 0.00 | +0.2040 | 2/4 | 20d momentum: +5.52%; 60d momentum: +15.04%; RS20 vs SPY: +4.89% | 60d beta (defensive polarity): +0.8111; 30d realized vol: +0.0999; 60d max drawdown: -0.1043 | L001-L027,L030,L135,L144,L145 |
| BNY | UNAVAILABLE | +0.521 | UNAVAILABLE | +0.594 | +0.2455 | 0.80 | 0.00 | +0.1964 | 2/4 | 20d momentum: +9.27%; 60d momentum: +19.00%; RS20 vs SPY: +8.64% | 60d beta (defensive polarity): +0.5661 | L001-L027,L030,L135,L144,L145 |
| MET | UNAVAILABLE | +0.830 | UNAVAILABLE | +0.801 | +0.3693 | 0.80 | 0.10 | +0.1955 | 2/4 | 20d momentum: +12.05%; 60d momentum: +22.07%; RS20 vs SPY: +11.42% | INSUFFICIENT_SOURCEABLE_DRIVERS | L001-L027,L030,L135,L144,L145 |
| VLO | UNAVAILABLE | +0.946 | UNAVAILABLE | +0.491 | +0.3574 | 0.80 | 0.10 | +0.1859 | 2/4 | 20d momentum: +18.60%; 60d momentum: +26.50%; RS20 vs SPY: +17.97% | 30d realized vol: +0.1178 | L001-L027,L030,L135,L144,L145 |
| HIG | UNAVAILABLE | +0.681 | UNAVAILABLE | +0.997 | +0.3538 | 0.80 | 0.10 | +0.1830 | 2/4 | 20d momentum: +7.79%; 60d momentum: +1.73%; RS20 vs SPY: +7.16% | RS60 vs SPY: -2.36% | L001-L027,L030,L135,L144,L145 |

## Metric Availability

| Metric Group | Sourceable Count | UNAVAILABLE Count | DQ / Confidence Effect | Notes |
|---|---|---|---|---|
| Price / volume history | 514 | 0 | none | 185–1,255 bars per name; adjusted-close basis |
| Realized vol, downside vol, beta, tracking error | 514 | 0 | none | all `DERIVED`, formulas in `01` |
| Tail risk (max DD60, VaR95, CVaR95) | 514 | 0 | none | VaR/CVaR parametric from the same sigma; normality assumed and stated |
| Kelly sizing | 514 | 0 | none | `mu/σ²` fallback disclosed |
| Technical pack (TD-9/RSI/MACD/MA/momentum/volume/RS × 3 timeframes) | ≥510 of 518 records | ≤8 | negligible | clears the 70% bar on every timeframe → RSI and MACD contribute to `Tech_Z` |
| Risk-free rate | 1 | 0 | none | ratios are true excess-return ratios (L007) |
| **Fundamental family** | **0** | **514** | **`Fund_Z` UNAVAILABLE; DQ → 0.80; blocks evidence threshold #2** | SHADOW tooling exists, not promoted |
| **Sentiment family** | **0** | **514** | **`Sent_Z` UNAVAILABLE; DQ → 0.80; blocks evidence threshold #2** | SHADOW tooling exists, not promoted |
| Options IV/skew, short interest, bid-ask, revisions, institutional flow | 0 | 514 | DQ 0.80 + confidence cap; **never a `GO` blocker** | Enhancing per `§ Input Classification` |
| GICS sector | 24 of 24 published | 0 | portfolio constraint | binds the 30% sector cap — see `07` |

## Technical Indicator Summary

All values from `technical_indicators.json` (L135), computed from the same 2026-07-24 adjusted bars used for every other metric. TD-9 is setup-count only; no Countdown.

| Ticker | TD9 D/W/M | RSI14 D/W/M | MACD State D/W/M | MA Align D/W/M | Mom 20d/60d | RS20/RS60 vs SPY | Vol Ratio 20d |
|---|---|---|---|---|---|---|---|
| TRV | SELL_SETUP_6 / SELL_SETUP_8 / SELL_SETUP_9 | 80.9 / 79.7 / 77.2 | ABOVE_SIGNAL / ABOVE_SIGNAL / ABOVE_SIGNAL | BULLISH / BULLISH / BULLISH | +21.67% / +25.44% | +21.04% / +21.35% | 1.29 |
| RTX | SELL_SETUP_3 / SELL_SETUP_9 / SELL_SETUP_1 | 74.0 / 66.8 / 74.9 | ABOVE_SIGNAL / ABOVE_SIGNAL / ABOVE_SIGNAL | BULLISH / BULLISH / BULLISH | +14.04% / +21.63% | +13.41% / +17.54% | 1.26 |
| PAYX | BUY_SETUP_3 / SELL_SETUP_9 / SELL_SETUP_2 | 64.7 / 64.5 / 50.2 | ABOVE_SIGNAL / ABOVE_SIGNAL / BELOW_SIGNAL | BULLISH / MIXED / MIXED | +17.40% / +26.40% | +16.77% / +22.31% | 0.85 |
| DGX | SELL_SETUP_7 / SELL_SETUP_5 / SELL_SETUP_6 | 72.7 / 68.3 / 68.7 | ABOVE_SIGNAL / ABOVE_SIGNAL / ABOVE_SIGNAL | BULLISH / BULLISH / BULLISH | +10.93% / +17.30% | +10.30% / +13.21% | 1.42 |
| UNP | SELL_SETUP_2 / SELL_SETUP_5 / SELL_SETUP_9 | 73.0 / 73.3 / 68.6 | ABOVE_SIGNAL / ABOVE_SIGNAL / ABOVE_SIGNAL | BULLISH / BULLISH / BULLISH | +14.79% / +15.38% | +14.16% / +11.29% | 1.21 |
| PCG | SELL_SETUP_3 / SELL_SETUP_3 / SELL_SETUP_1 | 60.1 / 58.5 / 55.6 | ABOVE_SIGNAL / ABOVE_SIGNAL / ABOVE_SIGNAL | BULLISH / BULLISH / BULLISH | +4.81% / +10.10% | +4.18% / +6.01% | 1.94 |
| CSX | SELL_SETUP_2 / SELL_SETUP_9 / SELL_SETUP_9 | 76.1 / 78.9 / 76.5 | ABOVE_SIGNAL / ABOVE_SIGNAL / ABOVE_SIGNAL | BULLISH / BULLISH / BULLISH | +12.20% / +18.05% | +11.57% / +13.96% | 1.08 |
| WRB | SELL_SETUP_5 / SELL_SETUP_5 / SELL_SETUP_1 | 67.4 / 65.2 / 61.9 | BULLISH_CROSS / ABOVE_SIGNAL / BELOW_SIGNAL | BULLISH / MIXED / BULLISH | +8.90% / +13.44% | +8.27% / +9.35% | 0.95 |
| TMO | SELL_SETUP_2 / SELL_SETUP_9 / SELL_SETUP_1 | 70.8 / 62.9 / 55.8 | ABOVE_SIGNAL / ABOVE_SIGNAL / BULLISH_CROSS | BULLISH / MIXED / MIXED | +12.36% / +20.97% | +11.73% / +16.88% | 1.28 |
| NSC | SELL_SETUP_2 / SELL_SETUP_5 / SELL_SETUP_4 | 73.2 / 71.0 / 67.4 | ABOVE_SIGNAL / ABOVE_SIGNAL / ABOVE_SIGNAL | BULLISH / BULLISH / BULLISH | +12.37% / +11.20% | +11.74% / +7.11% | 1.05 |
| GD | SELL_SETUP_5 / SELL_SETUP_4 / SELL_SETUP_1 | 70.3 / 65.0 / 78.3 | ABOVE_SIGNAL / ABOVE_SIGNAL / ABOVE_SIGNAL | BULLISH / BULLISH / BULLISH | +12.69% / +23.84% | +12.06% / +19.75% | 1.33 |
| PM | SELL_SETUP_1 / SELL_SETUP_2 / SELL_SETUP_1 | 59.7 / 64.1 / 68.9 | ABOVE_SIGNAL / ABOVE_SIGNAL / BULLISH_CROSS | BULLISH / BULLISH / BULLISH | +7.86% / +17.31% | +7.23% / +13.22% | 0.85 |
| MPC | BUY_SETUP_2 / SELL_SETUP_5 / SELL_SETUP_6 | 68.2 / 73.2 / 80.9 | ABOVE_SIGNAL / ABOVE_SIGNAL / ABOVE_SIGNAL | BULLISH / BULLISH / BULLISH | +21.96% / +33.46% | +21.33% / +29.37% | 0.89 |
| CTAS | SELL_SETUP_1 / SELL_SETUP_5 / SELL_SETUP_1 | 72.1 / 65.0 / 58.4 | ABOVE_SIGNAL / ABOVE_SIGNAL / BELOW_SIGNAL | BULLISH / MIXED / BULLISH | +21.78% / +18.51% | +21.15% / +14.42% | 0.81 |
| SJM | SELL_SETUP_7 / SELL_SETUP_2 / SELL_SETUP_1 | 61.2 / 63.6 / 56.6 | ABOVE_SIGNAL / ABOVE_SIGNAL / ABOVE_SIGNAL | BULLISH / BULLISH / MIXED | +5.17% / +22.01% | +4.54% / +17.92% | 0.70 |
| CB | SELL_SETUP_2 / SELL_SETUP_5 / SELL_SETUP_9 | 60.1 / 65.1 / 69.4 | BELOW_SIGNAL / ABOVE_SIGNAL / ABOVE_SIGNAL | BULLISH / BULLISH / BULLISH | +8.74% / +9.24% | +8.11% / +5.15% | 1.06 |
| LMT | SELL_SETUP_3 / SELL_SETUP_1 / BUY_SETUP_3 | 71.7 / 57.5 / 58.9 | ABOVE_SIGNAL / BELOW_SIGNAL / ABOVE_SIGNAL | BULLISH / BULLISH / BULLISH | +15.36% / +14.47% | +14.73% / +10.38% | 1.41 |
| WAB | SELL_SETUP_4 / SELL_SETUP_1 / SELL_SETUP_9 | 75.1 / 74.3 / 77.6 | ABOVE_SIGNAL / BULLISH_CROSS / ABOVE_SIGNAL | BULLISH / BULLISH / BULLISH | +7.10% / +15.08% | +6.47% / +10.99% | 1.46 |
| EQR | BUY_SETUP_3 / SELL_SETUP_5 / SELL_SETUP_4 | 49.7 / 58.6 / 57.9 | BELOW_SIGNAL / ABOVE_SIGNAL / ABOVE_SIGNAL | MIXED / BULLISH / BULLISH | +2.08% / +5.24% | +1.45% / +1.15% | 1.79 |
| PKG | SELL_SETUP_2 / SELL_SETUP_7 / SELL_SETUP_2 | 72.2 / 67.1 / 68.1 | BULLISH_CROSS / ABOVE_SIGNAL / ABOVE_SIGNAL | BULLISH / BULLISH / BULLISH | +5.52% / +15.04% | +4.89% / +10.95% | 2.10 |
| BNY | SELL_SETUP_2 / SELL_SETUP_9 / SELL_SETUP_9 | 63.5 / 84.1 / 90.9 | ABOVE_SIGNAL / ABOVE_SIGNAL / ABOVE_SIGNAL | BULLISH / BULLISH / BULLISH | +9.27% / +19.00% | +8.64% / +14.91% | 0.55 |
| MET | SELL_SETUP_1 / SELL_SETUP_9 / SELL_SETUP_4 | 67.2 / 71.0 / 67.7 | BELOW_SIGNAL / ABOVE_SIGNAL / BULLISH_CROSS | BULLISH / BULLISH / BULLISH | +12.05% / +22.07% | +11.42% / +17.98% | 1.37 |
| VLO | BUY_SETUP_2 / SELL_SETUP_5 / SELL_SETUP_9 | 63.1 / 71.6 / 82.3 | ABOVE_SIGNAL / ABOVE_SIGNAL / ABOVE_SIGNAL | BULLISH / BULLISH / BULLISH | +18.60% / +26.50% | +17.97% / +22.41% | 0.72 |
| HIG | SELL_SETUP_5 / SELL_SETUP_5 / SELL_SETUP_1 | 58.2 / 58.4 / 64.0 | ABOVE_SIGNAL / ABOVE_SIGNAL / BELOW_SIGNAL | BULLISH / BULLISH / BULLISH | +7.79% / +1.73% | +7.16% / -2.36% | 1.58 |

## What Drives the Leaderboard

The top of the book is a single coherent trade: **short-duration, low-beta, cash-generative defensives that have been absorbing the rotation out of growth.** Insurers (TRV, WRB, CB, MET, HIG), rails (UNP, CSX, NSC, WAB), defense and aerospace (GD, RTX, LMT), healthcare services (DGX, TMO), utilities (PCG), staples (PM, SJM) and refiners (MPC, VLO) fill nearly every published slot.

Mechanically:

- **`Tech_Z` supplies most of the signal** (weight 0.30 vs Macro's 0.15, and a wider z-range: −1.25 to +1.12 against Macro's −2.41 to +1.17). Relative strength versus SPY over 20 and 60 days is the strongest single contributor — these names are outperforming a flat index.
- **`Macro_Z` amplifies it** through the disclosed defensive polarity (L140). The published set averages a 60-day beta of **−0.247**, and **19 of 24 names carry negative beta**.

**Evidence threshold #3 is at genuine risk, and the arithmetic says so.** `Tech_Z` supplies a mean of **69.7%** of total conviction across the published set (range 46.9%–96.8%), and **22 of 24 names exceed the 50% single-family limit**. Because `Fund_Z` and `Sent_Z` are unavailable, the composite is close to a one-and-a-half-factor model. This is recorded as a live concern for `08` rather than papered over — and it is a second, independent reason no name in this set should be treated as investable even if the family gap closed tomorrow.

**The two available families are not independent this run.** In a rotation, the names with the best relative strength are largely the same names with the lowest beta, so `Tech_Z` and `Macro_Z` are positively correlated across the leaderboard. The effective breadth of the score is narrower than a 2-family arithmetic suggests.

**The #1 name is visibly extended, and the exhaustion penalty does not catch it.** TRV carries RSI(14) of **80.9 daily / 79.7 weekly / 77.2 monthly** — clearly overbought on all three timeframes — plus a **monthly TD-9 `SELL_SETUP_9`**. It did not trip the −0.05 exhaustion penalty only because that penalty requires the conjunction of a *daily* TD-9 `9` with daily RSI ≥ 70, and TRV's daily setup count is 6. The rule is applied consistently and as written; the consequence is disclosed rather than patched mid-run. TRV's extension is recorded as its key risk in `06`, and the daily-only scope of the exhaustion conjunction is a reasonable candidate for a future Track B refinement.

**Signal-decay warning.** Much of the top of the book is **post-catalyst**: the `ESTIMATED_CADENCE` resolutions in `01` (L023) are themselves evidence that TRV, RTX, PAYX, DGX, UNP, CSX, NSC, TMO, PM, CTAS, LMT, WAB and BNY all printed within the last 12 sessions, several with gaps of 4–10% (LMT +10.54%, WAB +10.04%, TMO +8.71%, RTX +7.33%). Their momentum and relative-strength z-scores are substantially earned by a single gap that has already occurred. For a 2–6 week horizon this is a real decay risk and it means today's `Tech_Z` is flattered.

**A note on the rank-IC evidence.** `02 § 0` reports a statistically significant *inverse* relationship between `adj_score` and realized alpha on the most recent settled vintage (−0.5912, p=0.026) and a negative pooled weighted mean (−0.1282, n=203). Read against this leaderboard, that is a warning that the score's *ordering* — not merely its magnitude — is currently unreliable. It is one more reason the `NO_TRADE` conclusion below is the right one, and it cannot be repaired by any Track A change while `eff_n = 1`.

## Investable Subset

**Empty — 0 of 514 names.**

| Evidence threshold | Requirement | Best achieved | Pass? |
|---|---|---|---|
| #1 | Adj-score percentile ≥ 80th | 100.0 (TRV) | Yes |
| #2 | ≥ 3 of 4 factor families non-negative | **2 of 4 available; max 2 non-negative** | **No — 0/514 names** |
| #3 | No family > 50% of conviction | Tech_Z mean 69.7% of conviction; 22 of 24 published names breach | **No — for 22 of 24** |
| #4 | Data completeness ≥ 85% | **80%** | **No — 0/514 names** |
| #5 | No hard stop from `§ Stop Criteria` | — | Yes |

Thresholds #2 and #4 fail for **every** name in the universe, both traceable to the same root cause: `Fund_Z` and `Sent_Z` are unavailable. Threshold #3 fails for almost every published name as a direct consequence.

**Recommendation: `NO_TRADE`** per `agents.md § Output Standard` ("If fewer than 5 names pass, recommend `NO_TRADE`").

## Monitoring Sleeve

All 24 published names are **monitoring-sleeve only**, each carrying a full Recommendation Metrics Block — `mu` from the calibration table, `sigma` from `REALIZED_VOL_30D`, target price, 70% CI, target date 2026-08-23 — so each produces a settleable prediction record in `15_predictions.json`. Confidence is **`LOW` for all 24**: the family-coverage gap forces `LOW` independently of the rank-IC `MEDIUM` cap, and 5 names are additionally capped `LOW` by the earnings penalty.

**Kelly note.** `0.25 × Kelly` is cap-binding at the 5% single-name NAV limit for all 24 published names (raw Kelly is large because `mu/σ²` with monthly sigma produces high nominal values). No published name has `0.25 × Kelly ≤ 0` (which would block investable status) and none falls below the 2% NAV threshold that would trigger the additional penalty. The Kelly gate is therefore *not* what stops this book — the evidence thresholds are.

## Near-Miss / Excluded Names

These 6 names entered the top 30 **only after** the post-penalty re-rank, i.e. after the bounded second earnings pass had already run. Per the bounded-second-pass convention they are **excluded with disclosure** rather than published with an ungrounded (and therefore artificially penalty-free) earnings field. Publishing them would mean treating Required input #4 as absent risk.

| Ticker | Rank | Pctl | Adj Score | Reason |
|---|---|---|---|---|
| MTB | 23 | 95.7 | +0.1905 | Third-pass entrant; next earnings date not fetched → Required input #4 ungrounded → excluded with disclosure |
| AON | 24 | 95.5 | +0.1905 | as above |
| ESS | 25 | 95.3 | +0.1890 | as above |
| ITW | 26 | 95.1 | +0.1867 | as above |
| WM | 27 | 94.9 | +0.1862 | as above |
| JNJ | 29 | 94.5 | +0.1834 | as above |

## Rejection Log — Prior-Vintage Names Below the Ranking Floor

Names ranked by the MoM baseline that fall below the 60th-percentile floor today and therefore appear in **neither** sleeve (`02 § 5`):

| Ticker | Rank | Pctl | Prior score | Realized alpha |
|---|---|---|---|---|
| CAT | 465 | 9.55 | 100.0 | −12.27% |
| GOOGL | 453 | 11.89 | 93.9 | −6.59% |
| FCX | 422 | 17.93 | 63.6 | −1.12% |
| SHW | 352 | 31.58 | 75.8 | −9.08% |
| GS | 280 | 45.61 | 66.7 | +2.72% |
| GE | 246 | 52.24 | 87.9 | −5.50% |
| CVX | 228 | 55.75 | 78.8 | +12.51% |
| EQIX | 224 | 56.53 | 72.7 | −2.01% |

CVX and GS are dropped despite *validated* theses — the move has already been realized and neither name's current technical/macro setup ranks. CVX additionally carries the TD-9 exhaustion penalty this run.

## Hallucination Prevention Checklist

- [x] Every numeric `entry_price` has `price_date` (2026-07-24) + `price_tag` (`HISTORICAL`)
- [x] Every numeric metric cites Source Ledger rows
- [x] Every `Adj Score` has a score trace with family z-scores, DQ, penalties, and metric drivers
- [x] Missing metrics are `UNAVAILABLE`, not neutral or supportive (`Fund_Z`, `Sent_Z`, 4 monthly MACD, 1 monthly RSI)
- [x] Kelly and technical indicator fields follow `rules.md § Financial Metrics` and `§ Technical Indicator Pack Definition`
- [x] `target_price = entry_price × (1 + mu)`, computed, never guessed
- [x] Every sigma has a stated source (`REALIZED_VOL_30D` on all 24 + 3 ETFs)
- [x] No published name has `price_tag = UNAVAILABLE`
- [x] `mu`/`sigma` derive from the architecture (calibration table + fallback chain), not assertion
- [x] No live-sounding wording without non-illustrative ledger support — this package says "the 2026-07-24 close", never "current" or "closed at" without a row
