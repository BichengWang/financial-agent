# 05 Factor Scores — 2026-07-24

Primary home for `Adj Score` explainability. Universe: 514 scored names, percentiles `INDEX_UNION_PCTL (n=514)`. Every numeric field below is rendered programmatically from `run_computed_manifest.json`; none was hand-transcribed.

## Scoring Method (as executed)

`Adj Score = (0.30·Fund_Z + 0.30·Tech_Z + 0.25·Sent_Z + 0.15·Macro_Z) × DQ − Penalties`

Baseline family weights are unchanged. `Fund_Z` and `Sent_Z` are `UNAVAILABLE` universe-wide (ledger rows L144, L145); per `rules.md § Family Aggregation` their displayed contribution is `0.00 (UNAVAILABLE)`, the data-quality multiplier is lowered, and **they do not count toward the 3-of-4 threshold**. The effective arithmetic is therefore `(0.30·Tech_Z + 0.15·Macro_Z) × 0.80 − Penalties`.

**Family construction.** Each metric is winsorized at the 5th/95th percentile across the 514-name universe, then z-scored; a family is the equal-weighted mean of its available metric z-scores (≥2 required, else `UNAVAILABLE`).

| Family | Metrics (polarity) | n signals |
|---|---|---|
| **Technical / Price** | 20d momentum (+), 60d momentum (+), RS20 vs SPY (+), RS60 vs SPY (+), MA alignment daily+weekly (+), MACD state daily+weekly (+), 20d volume ratio (+), RSI headroom `70 − RSI14_d` (+) | 8 |
| **Macro / Regime** | 60d beta (**−**), 30d realized vol (**−**), 60d max drawdown (+, i.e. shallower is better) | 3 |
| Fundamental | — | `UNAVAILABLE` |
| Sentiment / Positioning | — | `UNAVAILABLE` |

**Encodings.** MA alignment `BULLISH/MIXED/BEARISH` → `+1 / 0 / −1`. MACD `BULLISH_CROSS / ABOVE_SIGNAL / ON_SIGNAL / BELOW_SIGNAL / BEARISH_CROSS` → `+1 / +0.5 / 0 / −0.5 / −1`. RSI enters as headroom-to-overbought so that polarity is uniformly "higher is better" and extended names are not rewarded.

**Disclosed judgment — defensive Macro polarity (`INFERRED`).** Lower beta, lower realized vol, and shallower drawdown score *better* this run. This is a regime-conditional reading of the evidence in `03` (index flat, SOXX −19.5% from its high, 40.9% of the universe at negative beta, TLT −4.69%), not a permanent rule and not a family-weight change — altering weights would require the evolution policy. It is flagged here because it materially shapes the leaderboard: it is the single largest reason insurers, rails, utilities and defense sit at the top.

**Data-quality multiplier: 0.80** for every name — "notable coverage gaps", being two of four families `UNAVAILABLE` plus the entire Enhancing input block (L146). Since 0.80 < 0.85, `rules.md § Evidence Thresholds` #4 (data completeness ≥ 85%) independently forbids marking any name investable, on top of the family gap.

**Calibration feedback applied** (from `02 § 0`): rank IC −0.0939 over n=189 ≥ 20 → confidence capped at `MEDIUM`; CI coverage 76.19% is inside the healthy band, so no sigma-widening fires. **No positive per-name `mu` adjustments were made anywhere** — every `mu` is the unmodified mu-Calibration-Table value for the name's percentile band.

## Penalties Applied

| Penalty | Rule | Value | Names affected (published set) |
|---|---|---|---|
| Earnings inside 14 calendar days, buffered by the estimate band | `rules.md § Risk Controls` | **−0.10**, confidence capped `LOW` | 7 |
| 30d realized vol > 2× universe median (0.0960 → threshold 0.1920) | `rules.md § Risk Controls` | −0.05 | 3 |
| TD-9 sell-setup 9 **and** RSI(14) daily ≥ 70 (exhaustion confirmed by price action) | `rules.md § TD-9 Definition` | −0.05 | 0 in the published set |
| Unstable earnings profile | `rules.md § Risk Controls` | not applied | Requires fundamentals — `UNAVAILABLE` (L144). Disclosed as an unapplied penalty, not treated as absent risk. |

The volatility penalty uses the **universe** median rather than the sector median the rule nominates, because GICS labels are sourceable for only 68 of 76 shortlist names and not universe-wide. This is a documented substitution, and it is the more conservative direction for the low-vol names that dominate the leaderboard (they are compared against a broader, higher median).

## Ranked Candidate Table

26 published names — 21 organic top-ranked plus 5 binding carry-forwards from `02 § 5`. `Kelly 0.25` is reported raw from the disclosed fallback `raw_kelly = mu / sigma²`; values above 0.05 mean the **5% single-name NAV cap binds**, which it does for every name here. Sharpe/Sortino/Treynor/Calmar use the sourced 1-month risk-free rate of 0.3175% (L136) and are therefore **not** `RAW_DIAGNOSTIC`.

| # | Ticker | Sector | Entry | Px Date | Tag | Adj Score | Score Trace | Pctl | Beta | 30d RVol | Sharpe | Sortino | IR | Kelly 0.25 | VaR95 | CVaR95 | MaxDD60 | TD9 D/W/M | RSI14 D/W/M | MACD D/W/M | Days→Earn | mu | sigma | Sigma Src | Target | Target Date | CI70 Lo | CI70 Hi | Conf |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | TRV | Finance | 387.26 | 2026-07-24 | DELAYED | +0.3680 | (0.30×UNAVAIL + 0.30×+1.112 + 0.25×UNAVAIL + 0.15×+0.842)×0.80 − 0.00 = +0.3680 | 100.0 | -0.693 | +9.33% | 0.61 | 1.71 | 0.80 | 1.724 | -9.39% | -13.21% | -5.96% | SELL_SETUP_6 / SELL_SETUP_8 / SELL_SETUP_4 | 80.8 / 79.3 / 75.9 | ABOVE_SIGNAL / ABOVE_SIGNAL / ABOVE_SIGNAL | 84 | +6.0% | +9.33% | REALIZED_VOL_30D | 410.50 | 2026-08-21 | 372.93 | 448.06 | LOW |
| 2 | PAYX | Industrials | 113.55 | 2026-07-24 | DELAYED | +0.3037 | (0.30×UNAVAIL + 0.30×+0.867 + 0.25×UNAVAIL + 0.15×+0.797)×0.80 − 0.00 = +0.3037 | 99.8 | -0.638 | +9.45% | 0.60 | 1.37 | 0.66 | 1.681 | -9.59% | -13.46% | -6.35% | BUY_SETUP_3 / SELL_SETUP_9 / SELL_SETUP_2 | 64.6 / 63.0 / 47.5 | ABOVE_SIGNAL / ABOVE_SIGNAL / BELOW_SIGNAL | 83 | +6.0% | +9.45% | REALIZED_VOL_30D | 120.36 | 2026-08-21 | 109.21 | 131.52 | LOW |
| 3 | DGX | Health Care | 227.86 | 2026-07-24 | DELAYED | +0.3028 | (0.30×UNAVAIL + 0.30×+0.888 + 0.25×UNAVAIL + 0.15×+0.748)×0.80 − 0.00 = +0.3028 | 99.6 | -0.568 | +9.62% | 0.59 | 1.90 | 0.76 | 1.621 | -9.87% | -13.82% | -6.60% | SELL_SETUP_7 / SELL_SETUP_5 / SELL_SETUP_6 | 72.1 / 67.4 / 67.4 | ABOVE_SIGNAL / ABOVE_SIGNAL / ABOVE_SIGNAL | 90 | +6.0% | +9.62% | REALIZED_VOL_30D | 241.53 | 2026-08-21 | 218.74 | 264.33 | LOW |
| 4 | UNP | Industrials | 307.32 | 2026-07-24 | DELAYED | +0.2991 | (0.30×UNAVAIL + 0.30×+0.873 + 0.25×UNAVAIL + 0.15×+0.748)×0.80 − 0.00 = +0.2991 | 99.4 | -0.164 | +7.32% | 0.78 | 1.17 | 0.81 | 2.802 | -6.07% | -9.07% | -8.06% | SELL_SETUP_2 / SELL_SETUP_5 / SELL_SETUP_6 | 72.8 / 72.4 / 67.0 | ABOVE_SIGNAL / ABOVE_SIGNAL / ABOVE_SIGNAL | 90 | +6.0% | +7.32% | REALIZED_VOL_30D | 325.76 | 2026-08-21 | 302.38 | 349.14 | LOW |
| 5 | PCG | Utilities | 17.85 | 2026-07-24 | DELAYED | +0.2798 | (0.30×UNAVAIL + 0.30×+0.721 + 0.25×UNAVAIL + 0.15×+0.889)×0.80 − 0.00 = +0.2798 | 99.2 | -0.268 | +7.19% | 0.79 | 1.32 | 0.80 | 2.898 | -5.87% | -8.82% | -5.71% | SELL_SETUP_3 / SELL_SETUP_3 / SELL_SETUP_1 | 59.8 / 58.0 / 54.8 | ABOVE_SIGNAL / ABOVE_SIGNAL / ABOVE_SIGNAL | 89 | +6.0% | +7.19% | REALIZED_VOL_30D | 18.92 | 2026-08-21 | 17.59 | 20.26 | LOW |
| 6 | RTX | Industrials | 212.79 | 2026-07-24 | DELAYED | +0.2598 | (0.30×UNAVAIL + 0.30×+0.992 + 0.25×UNAVAIL + 0.15×+0.598)×0.80 − 0.05 = +0.2598 | 99.0 | -0.040 | +9.75% | 0.58 | 1.06 | 0.69 | 1.577 | -10.09% | -14.09% | -5.58% | SELL_SETUP_3 / SELL_SETUP_9 / SELL_SETUP_1 | 74.0 / 66.5 / 74.0 | ABOVE_SIGNAL / ABOVE_SIGNAL / ABOVE_SIGNAL | 90 | +6.0% | +9.75% | REALIZED_VOL_30D | 225.56 | 2026-08-21 | 203.97 | 247.14 | LOW |
| 7 | NSC | Industrials | 350.66 | 2026-07-24 | DELAYED | +0.2571 | (0.30×UNAVAIL + 0.30×+0.692 + 0.25×UNAVAIL + 0.15×+0.759)×0.80 − 0.00 = +0.2571 | 98.8 | -0.107 | +7.05% | 0.81 | 1.32 | 0.85 | 3.015 | -5.64% | -8.53% | -7.86% | SELL_SETUP_2 / SELL_SETUP_5 / SELL_SETUP_1 | 73.2 / 70.5 / 66.0 | ABOVE_SIGNAL / ABOVE_SIGNAL / ABOVE_SIGNAL | 90 | +6.0% | +7.05% | REALIZED_VOL_30D | 371.70 | 2026-08-21 | 345.98 | 397.42 | LOW |
| 8 | GD | Industrials | 386.75 | 2026-07-24 | DELAYED | +0.2337 | (0.30×UNAVAIL + 0.30×+1.009 + 0.25×UNAVAIL + 0.15×+0.763)×0.80 − 0.10 = +0.2337 | 98.6 | 0.008 | +7.57% | 0.75 | 1.25 | 0.75 | 2.615 | -6.50% | -9.60% | -5.70% | SELL_SETUP_5 / SELL_SETUP_4 / SELL_SETUP_1 | 70.0 / 64.3 / 76.6 | ABOVE_SIGNAL / ABOVE_SIGNAL / ABOVE_SIGNAL | 5 | +6.0% | +7.57% | REALIZED_VOL_30D | 409.95 | 2026-08-21 | 379.49 | 440.42 | LOW |
| 9 | CSX | Industrials | 53.23 | 2026-07-24 | DELAYED | +0.2315 | (0.30×UNAVAIL + 0.30×+0.791 + 0.25×UNAVAIL + 0.15×+0.763)×0.80 − 0.05 = +0.2315 | 98.4 | 0.114 | +7.22% | 0.79 | 1.63 | 0.89 | 2.878 | -5.91% | -8.87% | -4.20% | SELL_SETUP_2 / SELL_SETUP_9 / SELL_SETUP_8 | 76.0 / 78.5 / 75.3 | ABOVE_SIGNAL / ABOVE_SIGNAL / ABOVE_SIGNAL | 90 | +6.0% | +7.22% | REALIZED_VOL_30D | 56.42 | 2026-08-21 | 52.43 | 60.42 | LOW |
| 10 | CTAS | UNAVAILABLE | 205.91 | 2026-07-24 | DELAYED | +0.2279 | (0.30×UNAVAIL + 0.30×+0.666 + 0.25×UNAVAIL + 0.15×+0.567)×0.80 − 0.00 = +0.2279 | 98.2 | -0.287 | +10.33% | 0.55 | 1.21 | 0.67 | 1.405 | -11.05% | -15.28% | -7.19% | SELL_SETUP_1 / SELL_SETUP_5 / SELL_SETUP_1 | 72.1 / 64.8 / 57.9 | ABOVE_SIGNAL / ABOVE_SIGNAL / BELOW_SIGNAL | 83 | +6.0% | +10.33% | REALIZED_VOL_30D | 218.26 | 2026-08-21 | 196.14 | 240.39 | LOW |
| 11 | PM | UNAVAILABLE | 193.00 | 2026-07-24 | DELAYED | +0.2272 | (0.30×UNAVAIL + 0.30×+0.638 + 0.25×UNAVAIL + 0.15×+0.617)×0.80 − 0.00 = +0.2272 | 98.0 | -0.542 | +9.43% | 0.60 | 1.28 | 0.68 | 1.687 | -9.56% | -13.43% | -10.01% | SELL_SETUP_1 / SELL_SETUP_2 / SELL_SETUP_1 | 59.4 / 62.9 / 66.3 | ABOVE_SIGNAL / ABOVE_SIGNAL / BULLISH_CROSS | 83 | +6.0% | +9.43% | REALIZED_VOL_30D | 204.58 | 2026-08-21 | 185.65 | 223.51 | LOW |
| 12 | MPC | Energy | 309.24 | 2026-07-24 | DELAYED | +0.2224 | (0.30×UNAVAIL + 0.30×+1.044 + 0.25×UNAVAIL + 0.15×+0.598)×0.80 − 0.10 = +0.2224 | 97.9 | -0.445 | +9.70% | 0.59 | 1.04 | 0.59 | 1.594 | -10.00% | -13.98% | -9.09% | BUY_SETUP_2 / SELL_SETUP_5 / SELL_SETUP_6 | 68.1 / 72.9 / 80.0 | ABOVE_SIGNAL / ABOVE_SIGNAL / ABOVE_SIGNAL | 11 | +6.0% | +9.70% | REALIZED_VOL_30D | 327.79 | 2026-08-21 | 296.60 | 358.99 | LOW |
| 13 | LMT | Industrials | 582.60 | 2026-07-24 | DELAYED | +0.2155 | (0.30×UNAVAIL + 0.30×+0.763 + 0.25×UNAVAIL + 0.15×+0.271)×0.80 − 0.00 = +0.2155 | 97.7 | -0.441 | +12.88% | 0.44 | 1.14 | 0.62 | 0.904 | -15.26% | -20.54% | -10.40% | SELL_SETUP_3 / SELL_SETUP_1 / BUY_SETUP_3 | 71.5 / 56.9 / 57.3 | ABOVE_SIGNAL / BELOW_SIGNAL / ABOVE_SIGNAL | 90 | +6.0% | +12.88% | REALIZED_VOL_30D | 617.56 | 2026-08-21 | 539.50 | 695.61 | LOW |
| 14 | PKG | Consumer Discretionary | 254.39 | 2026-07-24 | DELAYED | +0.2063 | (0.30×UNAVAIL + 0.30×+0.811 + 0.25×UNAVAIL + 0.15×+0.098)×0.80 − 0.00 = +0.2063 | 97.5 | 0.794 | +9.96% | 0.57 | 1.26 | 0.65 | 1.512 | -10.44% | -14.52% | -10.43% | SELL_SETUP_2 / SELL_SETUP_7 / SELL_SETUP_2 | 72.1 / 66.3 / 66.0 | BULLISH_CROSS / ABOVE_SIGNAL / ABOVE_SIGNAL | 91 | +6.0% | +9.96% | REALIZED_VOL_30D | 269.65 | 2026-08-21 | 243.30 | 296.01 | LOW |
| 15 | TMO | Industrials | 568.26 | 2026-07-24 | DELAYED | +0.2025 | (0.30×UNAVAIL + 0.30×+0.855 + 0.25×UNAVAIL + 0.15×+0.395)×0.80 − 0.05 = +0.2025 | 97.3 | 0.093 | +10.22% | 0.56 | 1.93 | 0.59 | 1.437 | -10.86% | -15.05% | -8.48% | SELL_SETUP_2 / SELL_SETUP_9 / SELL_SETUP_1 | 70.8 / 62.8 / 55.8 | ABOVE_SIGNAL / ABOVE_SIGNAL / BULLISH_CROSS | 90 | +6.0% | +10.22% | REALIZED_VOL_30D | 602.36 | 2026-08-21 | 541.97 | 662.74 | LOW |
| 16 | SJM | Consumer Staples | 118.32 | 2026-07-24 | DELAYED | +0.1974 | (0.30×UNAVAIL + 0.30×+0.454 + 0.25×UNAVAIL + 0.15×+0.737)×0.80 − 0.00 = +0.1974 | 97.1 | -0.715 | +9.47% | 0.60 | 1.07 | 0.61 | 1.672 | -9.63% | -13.51% | -8.42% | SELL_SETUP_7 / SELL_SETUP_2 / SELL_SETUP_1 | 61.1 / 62.9 / 53.9 | ABOVE_SIGNAL / ABOVE_SIGNAL / ABOVE_SIGNAL | 33 | +6.0% | +9.47% | REALIZED_VOL_30D | 125.42 | 2026-08-21 | 113.76 | 137.07 | LOW |
| 17 | BNY | Finance | 158.91 | 2026-07-24 | DELAYED | +0.1962 | (0.30×UNAVAIL + 0.30×+0.523 + 0.25×UNAVAIL + 0.15×+0.588)×0.80 − 0.00 = +0.1962 | 96.9 | 0.585 | +7.38% | 0.77 | 1.49 | 0.97 | 2.750 | -6.19% | -9.21% | -3.34% | SELL_SETUP_2 / SELL_SETUP_9 / SELL_SETUP_9 | 63.5 / 83.6 / 89.9 | ABOVE_SIGNAL / ABOVE_SIGNAL / ABOVE_SIGNAL | 82 | +6.0% | +7.38% | REALIZED_VOL_30D | 168.44 | 2026-08-21 | 156.24 | 180.65 | LOW |
| 18 | VLO | Energy | 302.50 | 2026-07-24 | DELAYED | +0.1887 | (0.30×UNAVAIL + 0.30×+0.963 + 0.25×UNAVAIL + 0.15×+0.481)×0.80 − 0.10 = +0.1887 | 96.7 | -0.735 | +11.78% | 0.48 | 1.12 | 0.54 | 1.081 | -13.44% | -18.27% | -10.02% | BUY_SETUP_2 / SELL_SETUP_5 / SELL_SETUP_9 | 63.0 / 71.2 / 81.0 | ABOVE_SIGNAL / ABOVE_SIGNAL / ABOVE_SIGNAL | 6 | +6.0% | +11.78% | REALIZED_VOL_30D | 320.65 | 2026-08-21 | 283.59 | 357.71 | LOW |
| 19 | MTB | Finance | 249.60 | 2026-07-24 | DELAYED | +0.1881 | (0.30×UNAVAIL + 0.30×+0.419 + 0.25×UNAVAIL + 0.15×+0.730)×0.80 − 0.00 = +0.1881 | 96.5 | 0.293 | +6.37% | 0.89 | 1.40 | 0.96 | 3.695 | -4.51% | -7.12% | -6.66% | SELL_SETUP_1 / SELL_SETUP_8 / SELL_SETUP_2 | 62.5 / 68.8 / 68.1 | BELOW_SIGNAL / ABOVE_SIGNAL / ABOVE_SIGNAL | 82 | +6.0% | +6.37% | REALIZED_VOL_30D | 264.58 | 2026-08-21 | 248.04 | 281.11 | LOW |
| 20 | MET | Finance | 94.83 | 2026-07-24 | DELAYED | +0.1878 | (0.30×UNAVAIL + 0.30×+0.800 + 0.25×UNAVAIL + 0.15×+0.798)×0.80 − 0.10 = +0.1878 | 96.3 | 0.003 | +7.26% | 0.78 | 1.18 | 0.91 | 2.849 | -5.97% | -8.95% | -4.77% | SELL_SETUP_1 / SELL_SETUP_9 / SELL_SETUP_4 | 67.1 / 70.3 / 65.2 | BELOW_SIGNAL / ABOVE_SIGNAL / BULLISH_CROSS | 12 | +6.0% | +7.26% | REALIZED_VOL_30D | 100.52 | 2026-08-21 | 93.36 | 107.68 | LOW |
| 21 | HIG | Finance | 140.53 | 2026-07-24 | DELAYED | +0.1811 | (0.30×UNAVAIL + 0.30×+0.679 + 0.25×UNAVAIL + 0.15×+0.984)×0.80 − 0.10 = +0.1811 | 96.1 | -0.576 | +6.26% | 0.91 | 1.76 | 1.00 | 3.827 | -4.33% | -6.90% | -7.95% | SELL_SETUP_5 / SELL_SETUP_5 / SELL_SETUP_1 | 58.1 / 57.7 / 62.5 | ABOVE_SIGNAL / ABOVE_SIGNAL / BELOW_SIGNAL | 4 | +6.0% | +6.26% | REALIZED_VOL_30D | 148.96 | 2026-08-21 | 139.81 | 158.11 | LOW |
| 22 | BAC | Finance | 62.05 | 2026-07-24 | DELAYED | +0.1692 | (0.30×UNAVAIL + 0.30×+0.317 + 0.25×UNAVAIL + 0.15×+0.776)×0.80 − 0.00 = +0.1692 | 92.6 | 0.274 | +5.57% | 0.84 | 1.42 | 0.85 | 4.027 | -4.19% | -6.48% | -7.15% | SELL_SETUP_3 / SELL_SETUP_8 / SELL_SETUP_2 | 68.4 / 70.5 / 70.0 | BELOW_SIGNAL / ABOVE_SIGNAL / ABOVE_SIGNAL | 81 | +5.0% | +5.57% | REALIZED_VOL_30D | 65.15 | 2026-08-21 | 61.56 | 68.75 | LOW |
| 23 | JPM | Finance | 353.21 | 2026-07-24 | DELAYED | +0.1674 | (0.30×UNAVAIL + 0.30×+0.329 + 0.25×UNAVAIL + 0.15×+0.737)×0.80 − 0.00 = +0.1674 | 92.0 | 0.295 | +6.54% | 0.72 | 1.19 | 0.78 | 2.923 | -5.79% | -8.47% | -6.10% | SELL_SETUP_3 / SELL_SETUP_8 / SELL_SETUP_2 | 68.2 / 69.9 / 72.3 | ABOVE_SIGNAL / ABOVE_SIGNAL / BELOW_SIGNAL | 81 | +5.0% | +6.54% | REALIZED_VOL_30D | 370.87 | 2026-08-21 | 346.85 | 394.89 | LOW |
| 24 | AAPL | UNAVAILABLE | 333.02 | 2026-07-24 | DELAYED | +0.1271 | (0.30×UNAVAIL + 0.30×+0.881 + 0.25×UNAVAIL + 0.15×+0.130)×0.80 − 0.10 = +0.1271 | 78.0 | 0.498 | +9.68% | 0.17 | 0.24 | 0.25 | 0.533 | -13.98% | -17.95% | -12.71% | SELL_SETUP_1 / SELL_SETUP_4 / SELL_SETUP_3 | 65.2 / 69.0 / 70.2 | ABOVE_SIGNAL / ABOVE_SIGNAL / ABOVE_SIGNAL | 6 | +2.0% | +9.68% | REALIZED_VOL_30D | 339.68 | 2026-08-21 | 306.14 | 373.22 | LOW |
| 25 | UNH | Health Care | 420.74 | 2026-07-24 | DELAYED | +0.1263 | (0.30×UNAVAIL + 0.30×+0.131 + 0.25×UNAVAIL + 0.15×+0.790)×0.80 − 0.00 = +0.1263 | 77.8 | -0.042 | +7.29% | 0.23 | 0.67 | 0.27 | 0.941 | -10.03% | -13.02% | -6.06% | BUY_SETUP_2 / BUY_SETUP_1 / SELL_SETUP_4 | 51.5 / 66.2 / 52.8 | BELOW_SIGNAL / ABOVE_SIGNAL / ABOVE_SIGNAL | 88 | +2.0% | +7.29% | REALIZED_VOL_30D | 429.15 | 2026-08-21 | 397.25 | 461.06 | LOW |
| 26 | LLY | UNAVAILABLE | 1196.03 | 2026-07-24 | DELAYED | +0.1190 | (0.30×UNAVAIL + 0.30×+0.653 + 0.25×UNAVAIL + 0.15×+0.518)×0.80 − 0.10 = +0.1190 | 75.6 | 0.070 | +9.49% | 0.18 | 0.43 | 0.18 | 0.556 | -13.65% | -17.54% | -7.18% | SELL_SETUP_2 / BUY_SETUP_1 / SELL_SETUP_3 | 57.0 / 65.3 / 67.6 | BELOW_SIGNAL / ABOVE_SIGNAL / ABOVE_SIGNAL | 12 | +2.0% | +9.49% | REALIZED_VOL_30D | 1219.95 | 2026-08-21 | 1101.96 | 1337.94 | LOW |

## Score Attribution

| Ticker | Fund_Z | Tech_Z | Sent_Z | Macro_Z | Composite_Z | DQ | Penalties | Adj Score | Families non-neg | Top Positive Drivers | Top Negative Drivers |
|---|---|---|---|---|---|---|---|---|---|---|---|
| TRV | UNAVAILABLE | +1.112 | UNAVAILABLE | +0.842 | +0.4600 | 0.80 | 0.00 | +0.3680 | 2/4 | 20d momentum: +21.67; 60d momentum: +24.91; RS20 vs SPY: +21.04 | INSUFFICIENT_SOURCEABLE_DRIVERS |
| PAYX | UNAVAILABLE | +0.867 | UNAVAILABLE | +0.797 | +0.3796 | 0.80 | 0.00 | +0.3037 | 2/4 | 20d momentum: +17.40; 60d momentum: +24.79; RS20 vs SPY: +16.77 | INSUFFICIENT_SOURCEABLE_DRIVERS |
| DGX | UNAVAILABLE | +0.888 | UNAVAILABLE | +0.748 | +0.3786 | 0.80 | 0.00 | +0.3028 | 2/4 | 20d momentum: +10.48; 60d momentum: +16.82; RS20 vs SPY: +9.85 | 30d RVol 9.6% |
| UNP | UNAVAILABLE | +0.873 | UNAVAILABLE | +0.748 | +0.3739 | 0.80 | 0.00 | +0.2991 | 2/4 | 20d momentum: +14.79; 60d momentum: +14.78; RS20 vs SPY: +14.16 | INSUFFICIENT_SOURCEABLE_DRIVERS |
| PCG | UNAVAILABLE | +0.721 | UNAVAILABLE | +0.889 | +0.3497 | 0.80 | 0.00 | +0.2798 | 2/4 | 20d momentum: +4.51; 60d momentum: +9.78; RS20 vs SPY: +3.88 | INSUFFICIENT_SOURCEABLE_DRIVERS |
| RTX | UNAVAILABLE | +0.992 | UNAVAILABLE | +0.598 | +0.3873 | 0.80 | 0.05 | +0.2598 | 2/4 | 20d momentum: +14.04; 60d momentum: +21.12; RS20 vs SPY: +13.41 | 30d RVol 9.8% |
| NSC | UNAVAILABLE | +0.692 | UNAVAILABLE | +0.759 | +0.3214 | 0.80 | 0.00 | +0.2571 | 2/4 | 20d momentum: +12.37; 60d momentum: +10.72; RS20 vs SPY: +11.74 | INSUFFICIENT_SOURCEABLE_DRIVERS |
| GD | UNAVAILABLE | +1.009 | UNAVAILABLE | +0.763 | +0.4172 | 0.80 | 0.10 | +0.2337 | 2/4 | 20d momentum: +12.20; 60d momentum: +23.29; RS20 vs SPY: +11.57 | INSUFFICIENT_SOURCEABLE_DRIVERS |
| CSX | UNAVAILABLE | +0.791 | UNAVAILABLE | +0.763 | +0.3519 | 0.80 | 0.05 | +0.2315 | 2/4 | 20d momentum: +12.20; 60d momentum: +17.69; RS20 vs SPY: +11.57 | INSUFFICIENT_SOURCEABLE_DRIVERS |
| CTAS | UNAVAILABLE | +0.666 | UNAVAILABLE | +0.567 | +0.2849 | 0.80 | 0.00 | +0.2279 | 2/4 | 20d momentum: +21.78; 60d momentum: +18.19; RS20 vs SPY: +21.15 | 30d RVol 10.3% |
| PM | UNAVAILABLE | +0.638 | UNAVAILABLE | +0.617 | +0.2840 | 0.80 | 0.00 | +0.2272 | 2/4 | 20d momentum: +7.86; 60d momentum: +16.34; RS20 vs SPY: +7.23 | INSUFFICIENT_SOURCEABLE_DRIVERS |
| MPC | UNAVAILABLE | +1.044 | UNAVAILABLE | +0.598 | +0.4030 | 0.80 | 0.10 | +0.2224 | 2/4 | 20d momentum: +21.96; 60d momentum: +32.95; RS20 vs SPY: +21.33 | 30d RVol 9.7% |
| LMT | UNAVAILABLE | +0.763 | UNAVAILABLE | +0.271 | +0.2694 | 0.80 | 0.00 | +0.2155 | 2/4 | 20d momentum: +15.36; 60d momentum: +13.72; RS20 vs SPY: +14.73 | MACD(D/W) score: +0.00; 30d RVol 12.9% |
| PKG | UNAVAILABLE | +0.811 | UNAVAILABLE | +0.098 | +0.2579 | 0.80 | 0.00 | +0.2063 | 2/4 | 20d momentum: +5.52; 60d momentum: +14.29; RS20 vs SPY: +4.89 | 30d RVol 10.0% |
| TMO | UNAVAILABLE | +0.855 | UNAVAILABLE | +0.395 | +0.3156 | 0.80 | 0.05 | +0.2025 | 2/4 | 20d momentum: +12.36; 60d momentum: +20.85; RS20 vs SPY: +11.73 | 30d RVol 10.2% |
| SJM | UNAVAILABLE | +0.454 | UNAVAILABLE | +0.737 | +0.2467 | 0.80 | 0.00 | +0.1974 | 2/4 | 20d momentum: +5.17; 60d momentum: +20.67; RS20 vs SPY: +4.54 | INSUFFICIENT_SOURCEABLE_DRIVERS |
| BNY | UNAVAILABLE | +0.523 | UNAVAILABLE | +0.588 | +0.2453 | 0.80 | 0.00 | +0.1962 | 2/4 | 20d momentum: +9.27; 60d momentum: +19.00; RS20 vs SPY: +8.64 | INSUFFICIENT_SOURCEABLE_DRIVERS |
| VLO | UNAVAILABLE | +0.963 | UNAVAILABLE | +0.481 | +0.3609 | 0.80 | 0.10 | +0.1887 | 2/4 | 20d momentum: +18.60; 60d momentum: +25.90; RS20 vs SPY: +17.97 | 30d RVol 11.8% |
| MTB | UNAVAILABLE | +0.419 | UNAVAILABLE | +0.730 | +0.2351 | 0.80 | 0.00 | +0.1881 | 2/4 | 20d momentum: +5.42; 60d momentum: +14.75; RS20 vs SPY: +4.79 | MACD(D/W) score: +0.00 |
| MET | UNAVAILABLE | +0.800 | UNAVAILABLE | +0.798 | +0.3598 | 0.80 | 0.10 | +0.1878 | 2/4 | 20d momentum: +12.05; 60d momentum: +21.14; RS20 vs SPY: +11.42 | MACD(D/W) score: +0.00 |
| HIG | UNAVAILABLE | +0.679 | UNAVAILABLE | +0.984 | +0.3513 | 0.80 | 0.10 | +0.1811 | 2/4 | 20d momentum: +7.79; 60d momentum: +1.25; RS20 vs SPY: +7.16 | RS60 vs SPY: -2.58 |
| BAC | UNAVAILABLE | +0.317 | UNAVAILABLE | +0.776 | +0.2116 | 0.80 | 0.00 | +0.1692 | 2/4 | 20d momentum: +6.63; 60d momentum: +17.83; RS20 vs SPY: +6.00 | MACD(D/W) score: +0.00 |
| JPM | UNAVAILABLE | +0.329 | UNAVAILABLE | +0.737 | +0.2092 | 0.80 | 0.00 | +0.1674 | 2/4 | 20d momentum: +5.40; 60d momentum: +13.41; RS20 vs SPY: +4.77 | INSUFFICIENT_SOURCEABLE_DRIVERS |
| AAPL | UNAVAILABLE | +0.881 | UNAVAILABLE | +0.130 | +0.2839 | 0.80 | 0.10 | +0.1271 | 2/4 | 20d momentum: +21.03; 60d momentum: +23.02; RS20 vs SPY: +20.40 | 30d RVol 9.7% |
| UNH | UNAVAILABLE | +0.131 | UNAVAILABLE | +0.790 | +0.1579 | 0.80 | 0.00 | +0.1263 | 2/4 | 20d momentum: +1.25; 60d momentum: +14.71; RS20 vs SPY: +0.62 | MACD(D/W) score: +0.00 |
| LLY | UNAVAILABLE | +0.653 | UNAVAILABLE | +0.518 | +0.2737 | 0.80 | 0.10 | +0.1190 | 2/4 | 20d momentum: +6.06; 60d momentum: +36.85; RS20 vs SPY: +5.43 | MACD(D/W) score: +0.00 |

Every row shows two `UNAVAILABLE` families. No missing metric is presented as neutral or supportive anywhere in this package.

## Metric Availability

| Metric Group | Sourceable Count | UNAVAILABLE Count | DQ / Confidence Effect | Notes |
|---|---|---|---|---|
| Price / volume history | 514 | 0 | none | 1,255–1,307 bars per name; 3-source verified closes |
| Realized vol, downside vol, beta, tracking error | 514 | 0 | none | All `DERIVED`, formulas in `01` |
| Tail risk (max DD60, VaR95, CVaR95) | 514 | 0 | none | VaR/CVaR parametric from the same sigma; normality assumed and stated |
| Kelly sizing | 514 | 0 | none | `mu/σ²` fallback disclosed |
| Technical pack (TD-9/RSI/MACD/MA/momentum/volume/RS × 3 timeframes) | 517 of 518 records | 1 | negligible | Clears the 70% bar on every timeframe → RSI and MACD contribute to `Tech_Z` |
| Risk-free rate | 1 | 0 | none | Ratios are true excess-return ratios |
| **Fundamental family** | **0** | **514** | **`Fund_Z` UNAVAILABLE; DQ → 0.80; blocks evidence threshold #2** | SHADOW tooling exists, not promoted |
| **Sentiment family** | **0** | **514** | **`Sent_Z` UNAVAILABLE; DQ → 0.80; blocks evidence threshold #2** | SHADOW tooling exists, not promoted |
| Options IV/skew, short interest, bid-ask, revisions, institutional flow | 0 | 514 | DQ 0.80 + confidence cap; **never a GO blocker** | Enhancing per `§ Input Classification` |
| GICS sector | 68 of 76 | 8 | cosmetic here | Would bind the 30% sector cap in a live book |

## Technical Indicator Summary

All values from `technical_indicators.json` (ledger row L135), computed from the same 2026-07-24 bars used for every other metric. TD-9 is setup-count only; no Countdown.

| Ticker | TD9 D/W/M | RSI14 D/W/M | MACD State D/W/M | MA Align D/W/M | Mom 20d/60d | RS20/RS60 vs SPY | Vol Ratio 20d |
|---|---|---|---|---|---|---|---|
| TRV | SELL_SETUP_6 / SELL_SETUP_8 / SELL_SETUP_4 | 80.8 / 79.3 / 75.9 | ABOVE_SIGNAL / ABOVE_SIGNAL / ABOVE_SIGNAL | BULLISH / BULLISH / BULLISH | 21.67% / 24.91% | 21.04% / 21.08% | 1.25 |
| PAYX | BUY_SETUP_3 / SELL_SETUP_9 / SELL_SETUP_2 | 64.6 / 63.0 / 47.5 | ABOVE_SIGNAL / ABOVE_SIGNAL / BELOW_SIGNAL | BULLISH / MIXED / MIXED | 17.40% / 24.79% | 16.77% / 20.96% | 0.85 |
| DGX | SELL_SETUP_7 / SELL_SETUP_5 / SELL_SETUP_6 | 72.1 / 67.4 / 67.4 | ABOVE_SIGNAL / ABOVE_SIGNAL / ABOVE_SIGNAL | BULLISH / BULLISH / BULLISH | 10.48% / 16.82% | 9.85% / 12.99% | 1.41 |
| UNP | SELL_SETUP_2 / SELL_SETUP_5 / SELL_SETUP_6 | 72.8 / 72.4 / 67.0 | ABOVE_SIGNAL / ABOVE_SIGNAL / ABOVE_SIGNAL | BULLISH / BULLISH / BULLISH | 14.79% / 14.78% | 14.16% / 10.95% | 1.20 |
| PCG | SELL_SETUP_3 / SELL_SETUP_3 / SELL_SETUP_1 | 59.8 / 58.0 / 54.8 | ABOVE_SIGNAL / ABOVE_SIGNAL / ABOVE_SIGNAL | BULLISH / BULLISH / MIXED | 4.51% / 9.78% | 3.88% / 5.95% | 1.92 |
| RTX | SELL_SETUP_3 / SELL_SETUP_9 / SELL_SETUP_1 | 74.0 / 66.5 / 74.0 | ABOVE_SIGNAL / ABOVE_SIGNAL / ABOVE_SIGNAL | BULLISH / BULLISH / BULLISH | 14.04% / 21.12% | 13.41% / 17.29% | 1.24 |
| NSC | SELL_SETUP_2 / SELL_SETUP_5 / SELL_SETUP_1 | 73.2 / 70.5 / 66.0 | ABOVE_SIGNAL / ABOVE_SIGNAL / ABOVE_SIGNAL | BULLISH / BULLISH / BULLISH | 12.37% / 10.72% | 11.74% / 6.89% | 1.14 |
| GD | SELL_SETUP_5 / SELL_SETUP_4 / SELL_SETUP_1 | 70.0 / 64.3 / 76.6 | ABOVE_SIGNAL / ABOVE_SIGNAL / ABOVE_SIGNAL | BULLISH / BULLISH / BULLISH | 12.20% / 23.29% | 11.57% / 19.46% | 1.30 |
| CSX | SELL_SETUP_2 / SELL_SETUP_9 / SELL_SETUP_8 | 76.0 / 78.5 / 75.3 | ABOVE_SIGNAL / ABOVE_SIGNAL / ABOVE_SIGNAL | BULLISH / BULLISH / BULLISH | 12.20% / 17.69% | 11.57% / 13.86% | 1.08 |
| CTAS | SELL_SETUP_1 / SELL_SETUP_5 / SELL_SETUP_1 | 72.1 / 64.8 / 57.9 | ABOVE_SIGNAL / ABOVE_SIGNAL / BELOW_SIGNAL | BULLISH / MIXED / BULLISH | 21.78% / 18.19% | 21.15% / 14.36% | 0.81 |
| PM | SELL_SETUP_1 / SELL_SETUP_2 / SELL_SETUP_1 | 59.4 / 62.9 / 66.3 | ABOVE_SIGNAL / ABOVE_SIGNAL / BULLISH_CROSS | BULLISH / BULLISH / BULLISH | 7.86% / 16.34% | 7.23% / 12.51% | 0.83 |
| MPC | BUY_SETUP_2 / SELL_SETUP_5 / SELL_SETUP_6 | 68.1 / 72.9 / 80.0 | ABOVE_SIGNAL / ABOVE_SIGNAL / ABOVE_SIGNAL | BULLISH / BULLISH / BULLISH | 21.96% / 32.95% | 21.33% / 29.12% | 0.87 |
| LMT | SELL_SETUP_3 / SELL_SETUP_1 / BUY_SETUP_3 | 71.5 / 56.9 / 57.3 | ABOVE_SIGNAL / BELOW_SIGNAL / ABOVE_SIGNAL | BULLISH / BULLISH / BULLISH | 15.36% / 13.72% | 14.73% / 9.89% | 1.36 |
| PKG | SELL_SETUP_2 / SELL_SETUP_7 / SELL_SETUP_2 | 72.1 / 66.3 / 66.0 | BULLISH_CROSS / ABOVE_SIGNAL / ABOVE_SIGNAL | BULLISH / BULLISH / BULLISH | 5.52% / 14.29% | 4.89% / 10.46% | 2.06 |
| TMO | SELL_SETUP_2 / SELL_SETUP_9 / SELL_SETUP_1 | 70.8 / 62.8 / 55.8 | ABOVE_SIGNAL / ABOVE_SIGNAL / BULLISH_CROSS | BULLISH / MIXED / MIXED | 12.36% / 20.85% | 11.73% / 17.02% | 1.27 |
| SJM | SELL_SETUP_7 / SELL_SETUP_2 / SELL_SETUP_1 | 61.1 / 62.9 / 53.9 | ABOVE_SIGNAL / ABOVE_SIGNAL / ABOVE_SIGNAL | BULLISH / MIXED / MIXED | 5.17% / 20.67% | 4.54% / 16.84% | 0.70 |
| BNY | SELL_SETUP_2 / SELL_SETUP_9 / SELL_SETUP_9 | 63.5 / 83.6 / 89.9 | ABOVE_SIGNAL / ABOVE_SIGNAL / ABOVE_SIGNAL | BULLISH / BULLISH / BULLISH | 9.27% / 19.00% | 8.64% / 15.17% | 0.52 |
| VLO | BUY_SETUP_2 / SELL_SETUP_5 / SELL_SETUP_9 | 63.0 / 71.2 / 81.0 | ABOVE_SIGNAL / ABOVE_SIGNAL / ABOVE_SIGNAL | BULLISH / BULLISH / BULLISH | 18.60% / 25.90% | 17.97% / 22.07% | 0.76 |
| MTB | SELL_SETUP_1 / SELL_SETUP_8 / SELL_SETUP_2 | 62.5 / 68.8 / 68.1 | BELOW_SIGNAL / ABOVE_SIGNAL / ABOVE_SIGNAL | BULLISH / BULLISH / BULLISH | 5.42% / 14.75% | 4.79% / 10.92% | 1.06 |
| MET | SELL_SETUP_1 / SELL_SETUP_9 / SELL_SETUP_4 | 67.1 / 70.3 / 65.2 | BELOW_SIGNAL / ABOVE_SIGNAL / BULLISH_CROSS | BULLISH / BULLISH / BULLISH | 12.05% / 21.14% | 11.42% / 17.31% | 1.31 |
| HIG | SELL_SETUP_5 / SELL_SETUP_5 / SELL_SETUP_1 | 58.1 / 57.7 / 62.5 | ABOVE_SIGNAL / ABOVE_SIGNAL / BELOW_SIGNAL | BULLISH / BULLISH / BULLISH | 7.79% / 1.25% | 7.16% / -2.58% | 1.56 |
| BAC | SELL_SETUP_3 / SELL_SETUP_8 / SELL_SETUP_2 | 68.4 / 70.5 / 70.0 | BELOW_SIGNAL / ABOVE_SIGNAL / ABOVE_SIGNAL | BULLISH / BULLISH / BULLISH | 6.63% / 17.83% | 6.00% / 14.00% | 0.83 |
| JPM | SELL_SETUP_3 / SELL_SETUP_8 / SELL_SETUP_2 | 68.2 / 69.9 / 72.3 | ABOVE_SIGNAL / ABOVE_SIGNAL / BELOW_SIGNAL | BULLISH / BULLISH / BULLISH | 5.40% / 13.41% | 4.77% / 9.58% | 0.72 |
| AAPL | SELL_SETUP_1 / SELL_SETUP_4 / SELL_SETUP_3 | 65.2 / 69.0 / 70.2 | ABOVE_SIGNAL / ABOVE_SIGNAL / ABOVE_SIGNAL | BULLISH / BULLISH / BULLISH | 21.03% / 23.02% | 20.40% / 19.19% | 0.77 |
| UNH | BUY_SETUP_2 / BUY_SETUP_1 / SELL_SETUP_4 | 51.5 / 66.2 / 52.8 | BELOW_SIGNAL / ABOVE_SIGNAL / ABOVE_SIGNAL | MIXED / BULLISH / MIXED | 1.25% / 14.71% | 0.62% / 10.88% | 0.62 |
| LLY | SELL_SETUP_2 / BUY_SETUP_1 / SELL_SETUP_3 | 57.0 / 65.3 / 67.6 | BELOW_SIGNAL / ABOVE_SIGNAL / ABOVE_SIGNAL | BULLISH / BULLISH / BULLISH | 6.06% / 36.85% | 5.43% / 33.02% | 0.71 |

## What Drives the Leaderboard

The top of the book is a single coherent trade: **short-duration, low-beta, cash-generative defensives that have been absorbing the rotation out of growth.** Insurers (TRV, MET, HIG, MTB, BNY), rails (UNP, NSC, CSX), defense (GD, LMT, RTX), healthcare services (DGX, TMO), utilities (PCG), staples (PM, SJM) and refiners (MPC, VLO) fill nearly every top-20 slot.

Mechanically:

- **`Tech_Z` supplies most of the signal** (weight 0.30 vs Macro's 0.15, and a wider z-range). Relative strength versus SPY over 20 and 60 days is the strongest single contributor — these names are outperforming a flat index.
- **`Macro_Z` amplifies it** through the disclosed defensive polarity. The top names cluster at low or negative beta (TRV −0.69, PAYX −0.64, DGX −0.57) and below-median realized vol.
- **The two are not independent this run.** In a rotation, the names with the best relative strength are largely the same names with the lowest beta — so `Tech_Z` and `Macro_Z` are positively correlated across the leaderboard, and the composite is closer to a single factor than the 2-family arithmetic suggests. `rules.md § Evidence Thresholds` #3 ("no single factor family contributes more than 50% of total conviction") is therefore **at genuine risk of violation in spirit** even where the arithmetic passes. This is recorded as a concern for `08` rather than papered over.

**Signal-decay warning.** Many top ranks are **post-catalyst**: TRV printed 2026-07-17 (+9.22%), LMT, DGX, TMO, RTX, NSC, UNP and CSX all printed on 2026-07-23, and PKG printed on 2026-07-24 (+8.76%). Their momentum and relative-strength z-scores are substantially earned by a single gap that has already occurred. For a 2–6 week horizon this is a real decay risk, and it argues that today's `Tech_Z` is flattered. TRV additionally carries RSI(14) of 80.8 daily / 79.3 weekly — clearly overbought — and did not trip the exhaustion penalty only because its TD-9 sell-setup count is 6/8/4, short of the 9 the conjunction requires. That is the stated rule, applied consistently, but TRV's extension is flagged as its key risk in `06`.

## Investable Subset

**Empty — 0 of 514 names.**

| Evidence threshold | Requirement | Best achieved | Pass? |
|---|---|---|---|
| #1 | Adj-score percentile ≥ 80th | 100.0 (TRV) | Yes |
| #2 | ≥ 3 of 4 factor families non-negative | **2 of 4 available; max 2 non-negative** | **No — 0/514 names** |
| #3 | No family > 50% of conviction | Tech ≈ 2/3 of the composite by weight | Marginal |
| #4 | Data completeness ≥ 85% | **80%** | **No — 0/514 names** |
| #5 | No hard stop from `§ Stop Criteria` | — | Yes |

Thresholds #2 and #4 fail for **every** name in the universe, both traceable to the same root cause: `Fund_Z` and `Sent_Z` are unavailable. **Recommendation: `NO_TRADE`** per `agents.md § Output Standard` ("If fewer than 5 names pass, recommend `NO_TRADE`").

## Monitoring Sleeve

All 26 published names are monitoring-sleeve only, each carrying a full Recommendation Metrics Block — `mu` from the calibration table, `sigma` from `REALIZED_VOL_30D`, target price, 70% CI, target date 2026-08-21 — so each produces a settleable prediction record in `15_predictions.json`. Confidence is `LOW` for all 26.

## Near-Miss / Excluded Names

These 16 names entered the top 40 **only after** the post-penalty re-rank, i.e. after the bounded second earnings pass had already run. Per the bounded-second-pass convention they are **excluded with disclosure** rather than published with an ungrounded (and therefore penalty-free, artificially flattering) earnings field. Publishing them would have meant treating Required input #4 as absent risk.

| Ticker | Rank | Pctl | Adj Score | Reason |
|---|---|---|---|---|
| GL | 22 | 95.9 | +0.1807 | Entered top-40 only after the bounded second-pass re-rank; next earnings date not fetched → Required input #4 ungrounded → excluded with disclosure rather than published penalty-free |
| FFIV | 23 | 95.7 | +0.1807 | Entered top-40 only after the bounded second-pass re-rank; next earnings date not fetched → Required input #4 ungrounded → excluded with disclosure rather than published penalty-free |
| ESS | 24 | 95.5 | +0.1797 | Entered top-40 only after the bounded second-pass re-rank; next earnings date not fetched → Required input #4 ungrounded → excluded with disclosure rather than published penalty-free |
| VRSK | 25 | 95.3 | +0.1791 | Entered top-40 only after the bounded second-pass re-rank; next earnings date not fetched → Required input #4 ungrounded → excluded with disclosure rather than published penalty-free |
| INCY | 27 | 94.9 | +0.1786 | Entered top-40 only after the bounded second-pass re-rank; next earnings date not fetched → Required input #4 ungrounded → excluded with disclosure rather than published penalty-free |
| DUK | 28 | 94.7 | +0.1770 | Entered top-40 only after the bounded second-pass re-rank; next earnings date not fetched → Required input #4 ungrounded → excluded with disclosure rather than published penalty-free |
| ABBV | 29 | 94.5 | +0.1765 | Entered top-40 only after the bounded second-pass re-rank; next earnings date not fetched → Required input #4 ungrounded → excluded with disclosure rather than published penalty-free |
| WST | 30 | 94.3 | +0.1744 | Entered top-40 only after the bounded second-pass re-rank; next earnings date not fetched → Required input #4 ungrounded → excluded with disclosure rather than published penalty-free |
| PSA | 31 | 94.2 | +0.1738 | Entered top-40 only after the bounded second-pass re-rank; next earnings date not fetched → Required input #4 ungrounded → excluded with disclosure rather than published penalty-free |
| TRGP | 32 | 94.0 | +0.1722 | Entered top-40 only after the bounded second-pass re-rank; next earnings date not fetched → Required input #4 ungrounded → excluded with disclosure rather than published penalty-free |
| ITW | 34 | 93.6 | +0.1718 | Entered top-40 only after the bounded second-pass re-rank; next earnings date not fetched → Required input #4 ungrounded → excluded with disclosure rather than published penalty-free |
| HWM | 35 | 93.4 | +0.1709 | Entered top-40 only after the bounded second-pass re-rank; next earnings date not fetched → Required input #4 ungrounded → excluded with disclosure rather than published penalty-free |
| EA | 36 | 93.2 | +0.1707 | Entered top-40 only after the bounded second-pass re-rank; next earnings date not fetched → Required input #4 ungrounded → excluded with disclosure rather than published penalty-free |
| MCK | 37 | 93.0 | +0.1706 | Entered top-40 only after the bounded second-pass re-rank; next earnings date not fetched → Required input #4 ungrounded → excluded with disclosure rather than published penalty-free |
| STT | 38 | 92.8 | +0.1701 | Entered top-40 only after the bounded second-pass re-rank; next earnings date not fetched → Required input #4 ungrounded → excluded with disclosure rather than published penalty-free |
| HUM | 40 | 92.4 | +0.1692 | Entered top-40 only after the bounded second-pass re-rank; next earnings date not fetched → Required input #4 ungrounded → excluded with disclosure rather than published penalty-free |

The `DROP` names from `02 § 5` — CAT, GOOGL, GE, GS, EQIX, CVX, NVDA, FCX, V — are held out of the scored set as required and appear only in that rejection log.
