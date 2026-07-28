# 05 Factor Scores — 2026-07-28

Primary home for `Adj Score` explainability. Percentiles are `INDEX_UNION_PCTL (n=514)`.

## Family Construction

Each metric is winsorized at the 5th/95th percentile across the 514-name universe, then z-scored; a
family is the equal-weighted mean of its available metric z-scores (≥ 2 required, else `UNAVAILABLE`).

| Family | Weight | Metrics (polarity) | n signals |
|---|---|---|---|
| Fundamental | 0.30 | — | **`UNAVAILABLE` (L046)** |
| Technical / Price | 0.30 | 20d momentum (+), 60d momentum (+), RS20 vs SPY (+), RS60 vs SPY (+), MA alignment daily+weekly (+), MACD state daily+weekly (+), 20d volume ratio (+), RSI headroom `70 − RSI14_d` (+) | 8 |
| Sentiment / Positioning | 0.25 | — | **`UNAVAILABLE` (L047)** |
| Macro / Regime | 0.15 | 60d beta (**−**), 30d realized vol (**−**), 60d max drawdown (+, shallower is better) | 3 |

**Encodings.** MA alignment `BULLISH/MIXED/BEARISH` → `+1 / 0 / −1`. MACD
`BULLISH_CROSS / ABOVE_SIGNAL / ON_SIGNAL / BELOW_SIGNAL / BEARISH_CROSS` → `+1 / +0.5 / 0 / −0.5 / −1`.
RSI enters as headroom-to-overbought so polarity is uniformly "higher is better" and extended names are
not rewarded.

**Return basis.** Every momentum, relative-strength, volatility, beta, tracking-error and drawdown input
is computed from **adjusted** closes (L003). Entry, target and CI prices use the unadjusted 2026-07-27
close (L002). This is the Track B rule accepted 2026-07-26 — and it earned its keep again today: three
names (PAYX, FAST, ASML) carry an ex-dividend adjustment on the basis bar, PAYX by
1.030% (L054).

**Disclosed judgment — defensive Macro polarity (`INFERRED`, L053).** Lower beta, lower realized vol and
shallower drawdown score *better* this run. This is a regime-conditional reading of the `03` evidence
(index flat and below both moving averages, SOXX -21.19% from its 60-day high,
41.44% of the universe at negative beta, TLT -3.78% over 20 days).
It is **not** a permanent rule and **not** a family-weight change — altering weights requires the
evolution policy and is gated off at `eff_n = 1`. It is flagged here because it materially shapes
the leaderboard: it is the single largest reason insurers, rails, defense, staples and lab-services names
fill the top of the book, and why 15 of the 24 published names carry
negative beta.

**Data-quality multiplier: 0.8** for every name — "notable coverage gaps", two of four families
`UNAVAILABLE` plus the entire Enhancing block (L036, L046, L047, L048). Since 0.8 < 0.85,
`rules.md § Evidence Thresholds` #4 independently forbids marking any name investable.

**Calibration feedback applied** (from `02 § 0`): weighted-mean rank IC **-0.1715** over 260
settled pairs (≥ 20) → **confidence capped at `MEDIUM` universe-wide**; no name carries `HIGH` anywhere
in this package. CI coverage 74.62% is inside the healthy 55–85% band, so the
sigma-widening rule does **not** fire and sigma stays `REALIZED_VOL_30D`. **No positive per-name `mu`
adjustment was made anywhere** — every `mu` is the unmodified mu-Calibration-Table value for the name's
percentile band (L027).

## Penalties Applied

| Penalty | Rule | Value | Names (universe) | In published set |
|---|---|---|---|---|
| Earnings inside 14 calendar days, buffered by the estimate band | `rules.md § Risk Controls` | **−0.10**, confidence capped `LOW` | 34 | 3 |
| 30d realized vol > 2× universe median (0.0936 → threshold 0.1872) | `rules.md § Risk Controls` | −0.05 | 30 | 0 |
| TD-9 daily sell-setup 9 **and** RSI(14) daily ≥ 70 (exhaustion confirmed by price action) | `rules.md § TD-9 Definition` | −0.05 | 4 | 0 |
| Unstable earnings profile | `rules.md § Risk Controls` | **not applied** | — | Requires fundamentals — `UNAVAILABLE` (L046). Disclosed as an *unapplied* penalty, not as absent risk |
| Size > 2% of 20-day ADV | `rules.md § Risk Controls` | **not binding** | — | No position is sized; `NO_TRADE` |

67 of 514 names carry at least one penalty.

### Earnings-date grounding

58 names were grounded across **two bounded shortlist passes with zero transport
failures** (L022–L026): CONFIRMED 31, ESTIMATED_CADENCE 22,
ESTIMATED_PRINT_WEEK 5. The sequence was top-40 pre-penalty ranks (40 names) →
post-penalty top-40 entrants (18 names), iterated **until the post-penalty top-20 was fully
earnings-grounded**. The cap is 4 passes / 60 names; this run needed 2 passes / 58 names.

Unlike 2026-07-27, **no retry round was required** — the endpoint returned a resolution for all 58 names
on first request. A transport `FETCH_ERROR` is not a resolution and reads downstream as penalty-free, so
it would have been retried or excluded.

Names that entered the top-30 only after convergence and were never earnings-grounded
(DXCM, BXP, BAC, FRT, KVUE, FFIV, SO) are **excluded from publication rather than scored
penalty-free**.

`ESTIMATED_PRINT_WEEK` is the conservative branch: vendor-empty **and** no print-like signature, so the
name is treated as printing this week and penalised. This run is the **first to apply the gpt-5-2026-07-27
Track B refinement** (accepted, `HUMAN_REVIEW`, effective 2026-07-28): print-like iff `|1d move| ≥ 3.5%` **or**
(`volume ≥ 1.8× trailing median` **and** `|1d move| ≥ 1.5%`), which removes the volume-only false
positives that EQR and PKG tripped on ~0.01% price moves.

## Ranked Candidate Table — Published Set (24 names)

Field derivations per `rules.md § Price and Target Citation Standard`. `mu` from the mu Calibration Table
band for each name's percentile (L027); `sigma` = `REALIZED_VOL_30D` (L013);
`target_price = entry × (1 + mu)` (L028); CI bounds = `entry × (1 + mu ± 1.04σ)` (L029). Target date
**2026-08-25** (`run_date + 28d`). **Every name below is monitoring sleeve — zero investable.**

| Ticker | Company | Entry | Date | Tag | Adj Score | Score Trace | Pctl | Beta | 30d RVol | Sharpe | Sortino | IR | Kelly .25 | VaR95 | CVaR95 | MaxDD60 | TD9 D/W/M | RSI14 D/W/M | MACD D/W/M | Days→Earn | mu | sigma | SigSrc | Target | Target Date | CI Lo | CI Hi | Ledger | Metric Ledger | Conf | Primary Thesis | Key Risk |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| RTX | RTX Corporation Common Sto | 218.42 | 2026-07-27 | HISTORICAL | +0.3651 | (0.30×0.00<sub>UNAVL</sub> + 0.30×+1.2164 + 0.25×0.00<sub>UNAVL</sub> + 0.15×+0.6102) × 0.8 − 0.00 = +0.3651 | 100.00 | -0.068 | 9.36% | 0.6070 | 1.1111 | 0.7014 | 0.0500 | -9.44% | -13.28% | -5.58% | SELL_SETUP_4/SELL_SETUP_9/SELL_SETUP_1 | 77.33/69.16/75.98 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | ~91d (2026-10-27, ESTIMATED_CADENCE ±5d) | +6.0% | 9.36% | REALIZED_VOL_30D | 231.53 | 2026-08-25 | 210.26 | 252.79 | L002,L003,L012 | L013-L021,L027-L039 | MEDIUM | Industrials / Aerospace; RS60 +22.8pp, mom60 +26.9% | RSI14_d 77.33 overbought; beta -0.068 reverses in a risk-on turn |
| TRV | The Travelers Companies In | 390.35 | 2026-07-27 | HISTORICAL | +0.3076 | (0.30×0.00<sub>UNAVL</sub> + 0.30×+0.8648 + 0.25×0.00<sub>UNAVL</sub> + 0.15×+0.8339) × 0.8 − 0.00 = +0.3076 | 99.81 | -0.708 | 9.15% | 0.6207 | 1.8099 | 0.8771 | 0.0500 | -9.10% | -12.86% | -5.96% | SELL_SETUP_7/SELL_SETUP_9/SELL_SETUP_9 | 81.67/80.19/77.5 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | ~91d (2026-10-27, ESTIMATED_CADENCE ±5d) | +6.0% | 9.15% | REALIZED_VOL_30D | 413.77 | 2026-08-25 | 376.61 | 450.93 | L002,L003,L012 | L013-L021,L027-L039 | MEDIUM | Finance / Property-Casualty Insurers; RS60 +25.6pp, mom60 +29.7% | RSI14_d 81.67 overbought; beta -0.708 reverses in a risk-on turn |
| PAYX | Paychex Inc. Common Stock | 115.48 | 2026-07-27 | HISTORICAL | +0.2953 | (0.30×0.00<sub>UNAVL</sub> + 0.30×+0.8381 + 0.25×0.00<sub>UNAVL</sub> + 0.15×+0.7843) × 0.8 − 0.00 = +0.2953 | 99.61 | -0.610 | 9.15% | 0.6211 | 1.3870 | 0.7236 | 0.0500 | -9.09% | -12.85% | -6.35% | SELL_SETUP_1/SELL_SETUP_9/SELL_SETUP_2 | 67.48/66.21/51.32 | ABOVE_SIGNAL/ABOVE_SIGNAL/BELOW_SIGNAL | ~91d (2026-10-27, ESTIMATED_CADENCE ±5d) | +6.0% | 9.15% | REALIZED_VOL_30D | 122.41 | 2026-08-25 | 111.42 | 133.40 | L002,L003,L012 | L013-L021,L027-L039 | MEDIUM | Industrials / Diversified Commercial Services; RS60 +20.2pp, mom60 +24.4% | beta -0.610 reverses in a risk-on turn |
| SJM | The J.M. Smucker Company C | 121.05 | 2026-07-27 | HISTORICAL | +0.2738 | (0.30×0.00<sub>UNAVL</sub> + 0.30×+0.7798 + 0.25×0.00<sub>UNAVL</sub> + 0.15×+0.7217) × 0.8 − 0.00 = +0.2738 | 99.42 | -0.762 | 9.49% | 0.5986 | 1.1540 | 0.6501 | 0.0500 | -9.66% | -13.55% | -8.42% | SELL_SETUP_8/SELL_SETUP_3/SELL_SETUP_1 | 64.82/65.78/57.81 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | 29d (2026-08-26, CONFIRMED) | +6.0% | 9.49% | REALIZED_VOL_30D | 128.31 | 2026-08-25 | 116.36 | 140.26 | L002,L003,L012 | L013-L021,L027-L039 | MEDIUM | Consumer Staples / Packaged Foods; RS60 +22.3pp, mom60 +26.4% | beta -0.762 reverses in a risk-on turn |
| CSX | CSX Corporation Common Sto | 51.8 | 2026-07-27 | HISTORICAL | +0.2702 | (0.30×0.00<sub>UNAVL</sub> + 0.30×+0.7620 + 0.25×0.00<sub>UNAVL</sub> + 0.15×+0.7281) × 0.8 − 0.00 = +0.2702 | 99.22 | +0.113 | 7.42% | 0.7657 | 1.4335 | 0.8689 | 0.0500 | -6.24% | -9.29% | -4.20% | SELL_SETUP_3/SELL_SETUP_9/SELL_SETUP_9 | 64.1/72.1/75.39 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | ~91d (2026-10-27, ESTIMATED_CADENCE ±5d) | +6.0% | 7.42% | REALIZED_VOL_30D | 54.91 | 2026-08-25 | 50.91 | 58.91 | L002,L003,L012 | L013-L021,L027-L039 | MEDIUM | Industrials / Railroads; RS60 +12.2pp, mom60 +16.3% | 2 of 4 families UNAVAILABLE |
| DGX | Quest Diagnostics Incorpor | 231.84 | 2026-07-27 | HISTORICAL | +0.2688 | (0.30×0.00<sub>UNAVL</sub> + 0.30×+0.7428 + 0.25×0.00<sub>UNAVL</sub> + 0.15×+0.7540) × 0.8 − 0.00 = +0.2688 | 99.03 | -0.585 | 9.45% | 0.6011 | 2.0692 | 0.8294 | 0.0500 | -9.59% | -13.47% | -6.22% | SELL_SETUP_8/SELL_SETUP_6/SELL_SETUP_6 | 75.04/69.79/69.55 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | ~91d (2026-10-27, ESTIMATED_CADENCE ±5d) | +6.0% | 9.45% | REALIZED_VOL_30D | 245.75 | 2026-08-25 | 222.96 | 268.54 | L002,L003,L012 | L013-L021,L027-L039 | MEDIUM | Health Care / Medical Specialities; RS60 +18.8pp, mom60 +23.0% | RSI14_d 75.04 overbought; beta -0.585 reverses in a risk-on turn |
| BBY | Best Buy Co. Inc. Common S | 88.45 | 2026-07-27 | HISTORICAL | +0.2545 | (0.30×0.00<sub>UNAVL</sub> + 0.30×+0.9579 + 0.25×0.00<sub>UNAVL</sub> + 0.15×+0.2048) × 0.8 − 0.00 = +0.2545 | 98.83 | +0.823 | 8.94% | 0.6356 | 1.1826 | 0.4372 | 0.0500 | -8.75% | -12.41% | -8.93% | SELL_SETUP_2/SELL_SETUP_9/SELL_SETUP_3 | 71.0/68.3/60.98 | BULLISH_CROSS/ABOVE_SIGNAL/ABOVE_SIGNAL | 30d (2026-08-27, CONFIRMED) | +6.0% | 8.94% | REALIZED_VOL_30D | 93.76 | 2026-08-25 | 85.53 | 101.98 | L002,L003,L012 | L013-L021,L027-L039 | MEDIUM | Consumer Discretionary / Consumer Electronics/Video Chains; RS60 +48.5pp, mom60 +52.6% | RSI14_d 71.0 overbought |
| IQV | IQVIA Holdings Inc. Common | 213.22 | 2026-07-27 | HISTORICAL | +0.2520 | (0.30×0.00<sub>UNAVL</sub> + 0.30×+0.9629 + 0.25×0.00<sub>UNAVL</sub> + 0.15×+0.1740) × 0.8 − 0.00 = +0.2520 | 98.64 | +0.148 | 11.29% | 0.5032 | 1.0473 | 0.4797 | 0.0500 | -12.63% | -17.26% | -10.23% | SELL_SETUP_3/SELL_SETUP_6/SELL_SETUP_2 | 65.6/60.89/53.47 | BELOW_SIGNAL/ABOVE_SIGNAL/BULLISH_CROSS | ~91d (2026-10-27, ESTIMATED_CADENCE ±5d) | +6.0% | 11.29% | REALIZED_VOL_30D | 226.01 | 2026-08-25 | 200.98 | 251.05 | L002,L003,L012 | L013-L021,L027-L039 | MEDIUM | Health Care / Biotechnology: Commercial Physical; RS60 +32.0pp, mom60 +36.1% | 2 of 4 families UNAVAILABLE |
| MET | MetLife Inc. Common Stock | 95.19 | 2026-07-27 | HISTORICAL | +0.2493 | (0.30×0.00<sub>UNAVL</sub> + 0.30×+1.0542 + 0.25×0.00<sub>UNAVL</sub> + 0.15×+0.8027) × 0.8 − 0.10 = +0.2493 | 98.44 | -0.005 | 7.04% | 0.8069 | 1.2326 | 0.9176 | 0.0500 | -5.62% | -8.50% | -4.77% | SELL_SETUP_2/SELL_SETUP_9/SELL_SETUP_4 | 68.04/71.35/67.86 | BULLISH_CROSS/ABOVE_SIGNAL/BULLISH_CROSS | 8d (2026-08-05, CONFIRMED) | +6.0% | 7.04% | REALIZED_VOL_30D | 100.90 | 2026-08-25 | 93.93 | 107.87 | L002,L003,L012 | L013-L021,L027-L039 | LOW | Finance / Life Insurance; RS60 +17.4pp, mom60 +21.5% | earnings inside horizon; beta -0.005 reverses in a risk-on turn |
| UNP | Union Pacific Corporation  | 299.3 | 2026-07-27 | HISTORICAL | +0.2453 | (0.30×0.00<sub>UNAVL</sub> + 0.30×+0.6638 + 0.25×0.00<sub>UNAVL</sub> + 0.15×+0.7166) × 0.8 − 0.00 = +0.2453 | 98.25 | -0.163 | 7.63% | 0.7447 | 1.1719 | 0.8175 | 0.0500 | -6.59% | -9.72% | -7.58% | SELL_SETUP_3/SELL_SETUP_6/SELL_SETUP_9 | 62.46/67.48/67.29 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | ~91d (2026-10-27, ESTIMATED_CADENCE ±5d) | +6.0% | 7.63% | REALIZED_VOL_30D | 317.26 | 2026-08-25 | 293.51 | 341.01 | L002,L003,L012 | L013-L021,L027-L039 | MEDIUM | Industrials / Railroads; RS60 +9.5pp, mom60 +13.6% | beta -0.163 reverses in a risk-on turn |
| IVZ | Invesco Ltd Common Stock | 30.11 | 2026-07-27 | HISTORICAL | +0.2413 | (0.30×0.00<sub>UNAVL</sub> + 0.30×+1.1667 + 0.25×0.00<sub>UNAVL</sub> + 0.15×-0.3227) × 0.8 − 0.00 = +0.2413 | 98.05 | +1.527 | 11.00% | 0.5167 | 0.8159 | 0.6304 | 0.0500 | -12.14% | -16.65% | -11.40% | SELL_SETUP_4/SELL_SETUP_4/SELL_SETUP_9 | 60.68/65.03/69.22 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | ~91d (2026-10-27, ESTIMATED_CADENCE ±5d) | +6.0% | 11.00% | REALIZED_VOL_30D | 31.92 | 2026-08-25 | 28.47 | 35.36 | L002,L003,L012 | L013-L021,L027-L039 | MEDIUM | Finance / Investment Managers; RS60 +14.2pp, mom60 +18.4% | 2 of 4 families UNAVAILABLE |
| PFG | Principal Financial Group  | 111.29 | 2026-07-27 | HISTORICAL | +0.2391 | (0.30×0.00<sub>UNAVL</sub> + 0.30×+0.6018 + 0.25×0.00<sub>UNAVL</sub> + 0.15×+0.7890) × 0.8 − 0.00 = +0.2391 | 97.86 | -0.033 | 6.97% | 0.8157 | 1.0252 | 0.9755 | 0.0500 | -5.49% | -8.35% | -6.16% | SELL_SETUP_1/SELL_SETUP_9/SELL_SETUP_9 | 54.18/66.53/73.58 | BELOW_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | ~91d (2026-10-27, ESTIMATED_CADENCE ±5d) | +6.0% | 6.97% | REALIZED_VOL_30D | 117.97 | 2026-08-25 | 109.91 | 126.03 | L002,L003,L012 | L013-L021,L027-L039 | MEDIUM | Finance / Accident &Health Insurance; RS60 +8.5pp, mom60 +12.6% | beta -0.033 reverses in a risk-on turn |
| PRU | Prudential Financial Inc.  | 121.89 | 2026-07-27 | HISTORICAL | +0.2375 | (0.30×0.00<sub>UNAVL</sub> + 0.30×+1.0127 + 0.25×0.00<sub>UNAVL</sub> + 0.15×+0.7874) × 0.8 − 0.10 = +0.2375 | 97.66 | +0.268 | 6.16% | 0.9219 | 1.9234 | 1.0053 | 0.0500 | -4.17% | -6.70% | -2.66% | SELL_SETUP_2/SELL_SETUP_9/SELL_SETUP_2 | 72.36/70.86/64.54 | ABOVE_SIGNAL/ABOVE_SIGNAL/BULLISH_CROSS | 7d (2026-08-04, CONFIRMED) | +6.0% | 6.16% | REALIZED_VOL_30D | 129.20 | 2026-08-25 | 121.39 | 137.02 | L002,L003,L012 | L013-L021,L027-L039 | LOW | Finance / Life Insurance; RS60 +24.0pp, mom60 +28.1% | earnings inside horizon; RSI14_d 72.36 overbought |
| NSC | Norfolk Southern Corporati | 343.35 | 2026-07-27 | HISTORICAL | +0.2355 | (0.30×0.00<sub>UNAVL</sub> + 0.30×+0.6219 + 0.25×0.00<sub>UNAVL</sub> + 0.15×+0.7187) × 0.8 − 0.00 = +0.2355 | 97.47 | -0.101 | 7.24% | 0.7851 | 1.3473 | 0.8589 | 0.0500 | -5.94% | -8.91% | -7.86% | SELL_SETUP_3/SELL_SETUP_6/SELL_SETUP_4 | 64.18/66.04/66.36 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | ~91d (2026-10-27, ESTIMATED_CADENCE ±5d) | +6.0% | 7.24% | REALIZED_VOL_30D | 363.95 | 2026-08-25 | 338.11 | 389.79 | L002,L003,L012 | L013-L021,L027-L039 | MEDIUM | Industrials / Railroads; RS60 +6.3pp, mom60 +10.5% | beta -0.101 reverses in a risk-on turn |
| ITW | Illinois Tool Works Inc. C | 284.82 | 2026-07-27 | HISTORICAL | +0.2271 | (0.30×0.00<sub>UNAVL</sub> + 0.30×+0.6131 + 0.25×0.00<sub>UNAVL</sub> + 0.15×+0.6664) × 0.8 − 0.00 = +0.2271 | 97.27 | +0.464 | 6.66% | 0.8536 | 1.7159 | 0.9586 | 0.0500 | -4.98% | -7.71% | -5.65% | SELL_SETUP_3/SELL_SETUP_8/SELL_SETUP_1 | 66.39/64.09/60.75 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | ~91d (2026-10-27, ESTIMATED_CADENCE ±5d) | +6.0% | 6.66% | REALIZED_VOL_30D | 301.91 | 2026-08-25 | 282.19 | 321.63 | L002,L003,L012 | L013-L021,L027-L039 | MEDIUM | Industrials / Industrial Machinery/Components; RS60 +3.7pp, mom60 +7.9% | 2 of 4 families UNAVAILABLE |
| CTAS | Cintas Corporation Common  | 210.98 | 2026-07-27 | HISTORICAL | +0.2271 | (0.30×0.00<sub>UNAVL</sub> + 0.30×+0.6765 + 0.25×0.00<sub>UNAVL</sub> + 0.15×+0.5394) × 0.8 − 0.00 = +0.2271 | 97.08 | -0.294 | 10.29% | 0.5523 | 1.2639 | 0.6819 | 0.0500 | -10.97% | -15.19% | -7.19% | SELL_SETUP_2/SELL_SETUP_6/SELL_SETUP_1 | 75.19/67.27/59.73 | ABOVE_SIGNAL/ABOVE_SIGNAL/BELOW_SIGNAL | ~91d (2026-10-27, ESTIMATED_CADENCE ±5d) | +6.0% | 10.29% | REALIZED_VOL_30D | 223.64 | 2026-08-25 | 201.07 | 246.21 | L002,L003,L012 | L013-L021,L027-L039 | MEDIUM | Industrials / Garments and Clothing; RS60 +17.5pp, mom60 +21.6% | RSI14_d 75.19 overbought; beta -0.294 reverses in a risk-on turn |
| EXR | Extra Space Storage Inc Co | 148.29 | 2026-07-27 | HISTORICAL | +0.2265 | (0.30×0.00<sub>UNAVL</sub> + 0.30×+0.5181 + 0.25×0.00<sub>UNAVL</sub> + 0.15×+0.8510) × 0.8 − 0.00 = +0.2265 | 96.88 | +0.030 | 6.36% | 0.8940 | 1.7965 | 0.9211 | 0.0500 | -4.49% | -7.09% | -5.45% | SELL_SETUP_2/BUY_SETUP_2/SELL_SETUP_1 | 55.25/56.59/55.03 | BULLISH_CROSS/ABOVE_SIGNAL/ABOVE_SIGNAL | ~91d (2026-10-27, ESTIMATED_CADENCE ±5d) | +6.0% | 6.36% | REALIZED_VOL_30D | 157.19 | 2026-08-25 | 147.39 | 166.99 | L002,L003,L012 | L013-L021,L027-L039 | MEDIUM | Real Estate / Real Estate Investment Trusts; RS60 +2.5pp, mom60 +6.7% | 2 of 4 families UNAVAILABLE |
| MPC | Marathon Petroleum Corpora | 312.35 | 2026-07-27 | HISTORICAL | +0.2255 | (0.30×0.00<sub>UNAVL</sub> + 0.30×+1.0643 + 0.25×0.00<sub>UNAVL</sub> + 0.15×+0.5840) × 0.8 − 0.10 = +0.2255 | 96.69 | -0.432 | 9.46% | 0.6008 | 1.0461 | 0.6321 | 0.0500 | -9.60% | -13.48% | -9.09% | BUY_SETUP_3/SELL_SETUP_6/SELL_SETUP_6 | 69.71/73.77/81.22 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | 7d (2026-08-04, CONFIRMED) | +6.0% | 9.46% | REALIZED_VOL_30D | 331.09 | 2026-08-25 | 300.37 | 361.81 | L002,L003,L012 | L013-L021,L027-L039 | LOW | Energy / Integrated oil Companies; RS60 +25.5pp, mom60 +29.7% | earnings inside horizon; beta -0.432 reverses in a risk-on turn |
| WELL | Welltower Inc. Common Stoc | 248.34 | 2026-07-27 | HISTORICAL | +0.2197 | (0.30×0.00<sub>UNAVL</sub> + 0.30×+0.5280 + 0.25×0.00<sub>UNAVL</sub> + 0.15×+0.7745) × 0.8 − 0.00 = +0.2197 | 96.49 | -0.573 | 6.89% | 0.8251 | 1.4755 | 0.8431 | 0.0500 | -5.36% | -8.19% | -11.26% | SELL_SETUP_9/SELL_SETUP_6/SELL_SETUP_4 | 67.61/69.59/77.07 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | ~91d (2026-10-27, ESTIMATED_CADENCE ±5d) | +6.0% | 6.89% | REALIZED_VOL_30D | 263.24 | 2026-08-25 | 245.46 | 281.03 | L002,L003,L012 | L013-L021,L027-L039 | MEDIUM | Real Estate / Real Estate Investment Trusts; RS60 +13.4pp, mom60 +17.5% | beta -0.573 reverses in a risk-on turn |
| CB | Chubb Limited  Common Stoc | 358.91 | 2026-07-27 | HISTORICAL | +0.2176 | (0.30×0.00<sub>UNAVL</sub> + 0.30×+0.4224 + 0.25×0.00<sub>UNAVL</sub> + 0.15×+0.9683) × 0.8 − 0.00 = +0.2176 | 96.30 | -0.980 | 8.03% | 0.7079 | 1.3335 | 1.1227 | 0.0500 | -7.24% | -10.53% | -6.57% | SELL_SETUP_3/BUY_SETUP_1/SELL_SETUP_9 | 59.4/64.6/69.25 | BULLISH_CROSS/ABOVE_SIGNAL/ABOVE_SIGNAL | ~91d (2026-10-27, ESTIMATED_CADENCE ±5d) | +6.0% | 8.03% | REALIZED_VOL_30D | 380.44 | 2026-08-25 | 350.49 | 410.40 | L002,L003,L012 | L013-L021,L027-L039 | MEDIUM | Finance / Property-Casualty Insurers; RS60 +6.4pp, mom60 +10.5% | beta -0.980 reverses in a risk-on turn |
| LMT | Lockheed Martin Corporatio | 580.0 | 2026-07-27 | HISTORICAL | +0.2063 | (0.30×0.00<sub>UNAVL</sub> + 0.30×+0.7112 + 0.25×0.00<sub>UNAVL</sub> + 0.15×+0.2964) × 0.8 − 0.00 = +0.2063 | 96.10 | -0.460 | 12.18% | 0.4663 | 1.1869 | 0.6500 | 0.0500 | -14.10% | -19.10% | -10.40% | SELL_SETUP_4/SELL_SETUP_2/BUY_SETUP_3 | 70.25/56.94/58.69 | ABOVE_SIGNAL/BULLISH_CROSS/ABOVE_SIGNAL | ~91d (2026-10-27, ESTIMATED_CADENCE ±5d) | +6.0% | 12.18% | REALIZED_VOL_30D | 614.80 | 2026-08-25 | 541.31 | 688.29 | L002,L003,L012 | L013-L021,L027-L039 | MEDIUM | Industrials / Military/Government/Technical; RS60 +10.4pp, mom60 +14.5% | RSI14_d 70.25 overbought; beta -0.460 reverses in a risk-on turn |
| PM | Philip Morris Internationa | 195.66 | 2026-07-27 | HISTORICAL | +0.2057 | (0.30×0.00<sub>UNAVL</sub> + 0.30×+0.5549 + 0.25×0.00<sub>UNAVL</sub> + 0.15×+0.6041) × 0.8 − 0.00 = +0.2057 | 95.91 | -0.546 | 9.26% | 0.6139 | 1.2923 | 0.7233 | 0.0500 | -9.27% | -13.07% | -10.01% | SELL_SETUP_2/SELL_SETUP_3/SELL_SETUP_1 | 62.03/65.58/69.54 | ABOVE_SIGNAL/ABOVE_SIGNAL/BULLISH_CROSS | ~91d (2026-10-27, ESTIMATED_CADENCE ±5d) | +6.0% | 9.26% | REALIZED_VOL_30D | 207.40 | 2026-08-25 | 188.57 | 226.23 | L002,L003,L012 | L013-L021,L027-L039 | MEDIUM | Health Care /  Medicinal Chemicals and Botanical; RS60 +17.1pp, mom60 +21.2% | beta -0.546 reverses in a risk-on turn |
| BNY | The Bank of New York Mello | 157.77 | 2026-07-27 | HISTORICAL | +0.2022 | (0.30×0.00<sub>UNAVL</sub> + 0.30×+0.5466 + 0.25×0.00<sub>UNAVL</sub> + 0.15×+0.5918) × 0.8 − 0.00 = +0.2022 | 95.71 | +0.564 | 7.21% | 0.7881 | 1.5655 | 0.9372 | 0.0500 | -5.89% | -8.85% | -3.34% | BUY_SETUP_1/SELL_SETUP_9/SELL_SETUP_9 | 62.23/82.91/90.85 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | ~91d (2026-10-27, ESTIMATED_CADENCE ±5d) | +6.0% | 7.21% | REALIZED_VOL_30D | 167.24 | 2026-08-25 | 155.41 | 179.06 | L002,L003,L012 | L013-L021,L027-L039 | MEDIUM | Finance / Major Banks; RS60 +15.6pp, mom60 +19.8% | 2 of 4 families UNAVAILABLE |
| PKG | Packaging Corporation of A | 252.37 | 2026-07-27 | HISTORICAL | +0.1749 | (0.30×0.00<sub>UNAVL</sub> + 0.30×+0.6806 + 0.25×0.00<sub>UNAVL</sub> + 0.15×+0.0961) × 0.8 − 0.00 = +0.1749 | 91.81 | +0.806 | 9.54% | 0.4908 | 1.1079 | 0.5098 | 0.0500 | -10.74% | -14.65% | -10.43% | SELL_SETUP_3/SELL_SETUP_8/SELL_SETUP_2 | 69.48/65.62/67.69 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | ~91d (2026-10-27, ESTIMATED_CADENCE ±5d) | +5.0% | 9.54% | REALIZED_VOL_30D | 264.99 | 2026-08-25 | 239.95 | 290.02 | L002,L003,L012 | L013-L021,L027-L039 | MEDIUM | Consumer Discretionary / Containers/Packaging; RS60 +13.4pp, mom60 +17.6% | 2 of 4 families UNAVAILABLE |

### Why the published set jumps from rank 23 to rank 43

The set is built by the rule established on 2026-07-26 and 2026-07-27: walk the post-penalty rank order,
**skip any name whose earnings were never grounded**, and take the first 24. Ranks 1–23
are contiguous and all grounded. Ranks 24–42 contain the
7 names that entered the top-30 only after the penalty pass and were never
fetched (DXCM, BXP, BAC, FRT, KVUE, FFIV, SO), plus names that fell on their own penalties. PKG at
rank 43 is the 24th *grounded* name. Publishing an ungrounded name would present it as
penalty-free — indistinguishable from "verified clear of earnings" — which is exactly the failure the
2026-07-27 Track B change was written to prevent.

## Score Attribution

| Ticker | Fund_Z | Tech_Z | Sent_Z | Macro_Z | Composite_Z | DQ | Penalties | Adj Score | Top Positive Drivers | Top Negative Drivers | Metric Ledger Rows |
|---|---|---|---|---|---|---|---|---|---|---|---|
| RTX | `UNAVAILABLE` | +1.2164 | `UNAVAILABLE` | +0.6102 | +0.4564 | 0.8 | 0.00 | +0.3651 | 20d volume ratio +2.309; RS20 vs SPY +1.768; 20d momentum +1.768 | RSI headroom to 70 -1.697 | L013–L021 |
| TRV | `UNAVAILABLE` | +0.8648 | `UNAVAILABLE` | +0.8339 | +0.3845 | 0.8 | 0.00 | +0.3076 | 60d momentum +1.831; RS60 vs SPY +1.831; RS20 vs SPY +1.768 | RSI headroom to 70 -1.697; 20d volume ratio -0.933 | L013–L021 |
| PAYX | `UNAVAILABLE` | +0.8381 | `UNAVAILABLE` | +0.7843 | +0.3691 | 0.8 | 0.00 | +0.2953 | RS20 vs SPY +1.768; 20d momentum +1.768; 60d momentum +1.417 | RSI headroom to 70 -1.530 | L013–L021 |
| SJM | `UNAVAILABLE` | +0.7798 | `UNAVAILABLE` | +0.7217 | +0.3422 | 0.8 | 0.00 | +0.2738 | 60d momentum +1.578; RS60 vs SPY +1.578; MA alignment (d+w) +1.251 | RSI headroom to 70 -1.227 | L013–L021 |
| CSX | `UNAVAILABLE` | +0.7620 | `UNAVAILABLE` | +0.7281 | +0.3378 | 0.8 | 0.00 | +0.2702 | 20d volume ratio +1.488; MA alignment (d+w) +1.251; 60d max drawdown (shallower better) +1.127 | RSI headroom to 70 -1.145 | L013–L021 |
| DGX | `UNAVAILABLE` | +0.7428 | `UNAVAILABLE` | +0.7540 | +0.3359 | 0.8 | 0.00 | +0.2688 | 60d momentum +1.307; RS60 vs SPY +1.307; MA alignment (d+w) +1.251 | RSI headroom to 70 -1.697 | L013–L021 |
| BBY | `UNAVAILABLE` | +0.9579 | `UNAVAILABLE` | +0.2048 | +0.3181 | 0.8 | 0.00 | +0.2545 | 60d momentum +1.947; RS60 vs SPY +1.947; MACD state (d+w) +1.708 | RSI headroom to 70 -1.697; 20d volume ratio -0.687; 60d beta (lower better) -0.400 | L013–L021 |
| IQV | `UNAVAILABLE` | +0.9629 | `UNAVAILABLE` | +0.1740 | +0.3150 | 0.8 | 0.00 | +0.2520 | 20d volume ratio +2.309; 60d momentum +1.947; RS60 vs SPY +1.947 | RSI headroom to 70 -1.316; 30d realized vol (lower better) -0.315; MACD state (d+w) -0.117 | L013–L021 |
| MET | `UNAVAILABLE` | +1.0542 | `UNAVAILABLE` | +0.8027 | +0.4367 | 0.8 | 0.10 | +0.2493 | 20d volume ratio +2.309; MACD state (d+w) +1.708; MA alignment (d+w) +1.251 | RSI headroom to 70 -1.594 | L013–L021 |
| UNP | `UNAVAILABLE` | +0.6638 | `UNAVAILABLE` | +0.7166 | +0.3066 | 0.8 | 0.00 | +0.2453 | RS20 vs SPY +1.291; 20d momentum +1.291; MA alignment (d+w) +1.251 | RSI headroom to 70 -0.959 | L013–L021 |
| IVZ | `UNAVAILABLE` | +1.1667 | `UNAVAILABLE` | -0.3227 | +0.3016 | 0.8 | 0.00 | +0.2413 | 20d volume ratio +2.309; RS20 vs SPY +1.767; 20d momentum +1.767 | 60d beta (lower better) -1.128; RSI headroom to 70 -0.756; 30d realized vol (lower better) -0.236 | L013–L021 |
| PFG | `UNAVAILABLE` | +0.6018 | `UNAVAILABLE` | +0.7890 | +0.2989 | 0.8 | 0.00 | +0.2391 | 20d volume ratio +2.309; MA alignment (d+w) +1.251; 60d max drawdown (shallower better) +1.036 | MACD state (d+w) -0.117; RSI headroom to 70 -0.017 | L013–L021 |
| PRU | `UNAVAILABLE` | +1.0127 | `UNAVAILABLE` | +0.7874 | +0.4219 | 0.8 | 0.10 | +0.2375 | 60d momentum +1.710; RS60 vs SPY +1.710; RS20 vs SPY +1.434 | RSI headroom to 70 -1.697 | L013–L021 |
| NSC | `UNAVAILABLE` | +0.6219 | `UNAVAILABLE` | +0.7187 | +0.2944 | 0.8 | 0.00 | +0.2355 | MA alignment (d+w) +1.251; MACD state (d+w) +1.100; 20d momentum +1.056 | RSI headroom to 70 -1.154 | L013–L021 |
| ITW | `UNAVAILABLE` | +0.6131 | `UNAVAILABLE` | +0.6664 | +0.2839 | 0.8 | 0.00 | +0.2271 | 20d volume ratio +2.309; MA alignment (d+w) +1.251; MACD state (d+w) +1.100 | RSI headroom to 70 -1.406; 60d beta (lower better) -0.030 | L013–L021 |
| CTAS | `UNAVAILABLE` | +0.6765 | `UNAVAILABLE` | +0.5394 | +0.2839 | 0.8 | 0.00 | +0.2271 | RS20 vs SPY +1.768; 20d momentum +1.768; 60d momentum +1.203 | RSI headroom to 70 -1.697; 20d volume ratio -0.276; 30d realized vol (lower better) -0.046 | L013–L021 |
| EXR | `UNAVAILABLE` | +0.5181 | `UNAVAILABLE` | +0.8510 | +0.2831 | 0.8 | 0.00 | +0.2265 | 20d volume ratio +1.899; MACD state (d+w) +1.708; MA alignment (d+w) +1.251 | 20d momentum -0.326; RS20 vs SPY -0.326; RSI headroom to 70 -0.139 | L013–L021 |
| MPC | `UNAVAILABLE` | +1.0643 | `UNAVAILABLE` | +0.5840 | +0.4069 | 0.8 | 0.10 | +0.2255 | 60d momentum +1.828; RS60 vs SPY +1.828; RS20 vs SPY +1.768 | RSI headroom to 70 -1.697 | L013–L021 |
| WELL | `UNAVAILABLE` | +0.5280 | `UNAVAILABLE` | +0.7745 | +0.2746 | 0.8 | 0.00 | +0.2197 | MA alignment (d+w) +1.251; MACD state (d+w) +1.100; 60d beta (lower better) +1.042 | RSI headroom to 70 -1.545; 20d volume ratio -0.317 | L013–L021 |
| CB | `UNAVAILABLE` | +0.4224 | `UNAVAILABLE` | +0.9683 | +0.2720 | 0.8 | 0.00 | +0.2176 | MACD state (d+w) +1.708; 60d beta (lower better) +1.357; MA alignment (d+w) +1.251 | RSI headroom to 70 -0.611; 20d volume ratio -0.522 | L013–L021 |
| LMT | `UNAVAILABLE` | +0.7112 | `UNAVAILABLE` | +0.2964 | +0.2578 | 0.8 | 0.00 | +0.2063 | MACD state (d+w) +1.708; 20d momentum +1.662; RS20 vs SPY +1.662 | RSI headroom to 70 -1.697; 30d realized vol (lower better) -0.555; 20d volume ratio -0.194 | L013–L021 |
| PM | `UNAVAILABLE` | +0.5549 | `UNAVAILABLE` | +0.6041 | +0.2571 | 0.8 | 0.00 | +0.2057 | MA alignment (d+w) +1.251; 60d momentum +1.174; RS60 vs SPY +1.174 | 20d volume ratio -1.056; RSI headroom to 70 -0.910 | L013–L021 |
| BNY | `UNAVAILABLE` | +0.5466 | `UNAVAILABLE` | +0.5918 | +0.2527 | 0.8 | 0.00 | +0.2022 | MA alignment (d+w) +1.251; 20d momentum +1.133; RS20 vs SPY +1.133 | 20d volume ratio -1.425; RSI headroom to 70 -0.933; 60d beta (lower better) -0.133 | L013–L021 |
| PKG | `UNAVAILABLE` | +0.6806 | `UNAVAILABLE` | +0.0961 | +0.2186 | 0.8 | 0.00 | +0.1749 | 20d volume ratio +2.309; MA alignment (d+w) +1.251; MACD state (d+w) +1.100 | RSI headroom to 70 -1.697; 60d beta (lower better) -0.382 | L013–L021 |

`Fund_Z` and `Sent_Z` enter the arithmetic as `0.00` **labelled `UNAVAILABLE`** — never as neutral or
supportive evidence, and they do not count toward the "3 of 4 families supportive" threshold.

## Metric Availability

| Metric Group | Sourceable Count | `UNAVAILABLE` Count | DQ / Confidence Effect | Notes |
|---|---|---|---|---|
| Risk / return ratios (Sharpe, Sortino, IR, Treynor, Calmar) | 514/514 | 0 | none | rf from L008; all ratios risk-free adjusted, not `RAW_DIAGNOSTIC` |
| Tail risk (VaR95, CVaR95, MaxDD60) | 514/514 | 0 | none | parametric, normality stated (L035) |
| Sizing (Kelly raw, 0.25×Kelly) | 514/514 | 0 | none | every published name is 5%-cap-binding (L034) |
| Technical pack (TD-9, RSI, MACD, MA, momentum, volume, RS) | 514/514 | 0 | none | daily/weekly/monthly (L010, L019) |
| Fundamental / quality | 0/514 | 514 | **DQ → 0.8**, family `UNAVAILABLE` | L046 |
| Sentiment / positioning | 0/514 | 514 | **DQ → 0.8**, family `UNAVAILABLE` | L047 |
| Options IV / skew, short interest, bid-ask | 0/514 | 514 | confidence cap, gross-exposure cap | L048 — Enhancing, never a `GO` blocker |

## Technical Indicator Summary — published set

| Ticker | TD9 D/W/M | RSI14 D/W/M | MACD State D/W/M | MACD Hist D/W/M | MA Alignment D/W/M | 20/60 Mom (daily) | RS20/60 vs SPY | Indicator Ledger Rows |
|---|---|---|---|---|---|---|---|---|
| RTX | SELL_SETUP_4/SELL_SETUP_9/SELL_SETUP_1 | 77.33/69.16/75.98 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | 1.8216/2.9106/2.0035 | BULLISH/BULLISH/BULLISH | +16.19% / +26.93% | +14.80pp / +22.80pp | L010, L018–L020 |
| TRV | SELL_SETUP_7/SELL_SETUP_9/SELL_SETUP_9 | 81.67/80.19/77.5 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | 3.798/8.7858/6.1914 | BULLISH/BULLISH/BULLISH | +19.24% / +29.69% | +17.85pp / +25.56pp | L010, L018–L020 |
| PAYX | SELL_SETUP_1/SELL_SETUP_9/SELL_SETUP_2 | 67.48/66.21/51.32 | ABOVE_SIGNAL/ABOVE_SIGNAL/BELOW_SIGNAL | 0.1273/3.2081/-2.4766 | BULLISH/MIXED/MIXED | +15.60% / +24.37% | +14.21pp / +20.24pp | L010, L018–L020 |
| SJM | SELL_SETUP_8/SELL_SETUP_3/SELL_SETUP_1 | 64.82/65.78/57.81 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | 0.6041/1.7803/1.9548 | BULLISH/BULLISH/MIXED | +4.68% / +26.44% | +3.29pp / +22.31pp | L010, L018–L020 |
| CSX | SELL_SETUP_3/SELL_SETUP_9/SELL_SETUP_9 | 64.1/72.1/75.39 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | 0.2054/0.4416/1.6536 | BULLISH/BULLISH/BULLISH | +8.69% / +16.29% | +7.30pp / +12.16pp | L010, L018–L020 |
| DGX | SELL_SETUP_8/SELL_SETUP_6/SELL_SETUP_6 | 75.04/69.79/69.55 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | 2.0666/3.0744/3.23 | BULLISH/BULLISH/BULLISH | +10.91% / +22.96% | +9.52pp / +18.83pp | L010, L018–L020 |
| BBY | SELL_SETUP_2/SELL_SETUP_9/SELL_SETUP_3 | 71.0/68.3/60.98 | BULLISH_CROSS/ABOVE_SIGNAL/ABOVE_SIGNAL | 0.0415/2.499/1.6388 | BULLISH/BULLISH/BULLISH | +13.82% / +52.61% | +12.43pp / +48.48pp | L010, L018–L020 |
| IQV | SELL_SETUP_3/SELL_SETUP_6/SELL_SETUP_2 | 65.6/60.89/53.47 | BELOW_SIGNAL/ABOVE_SIGNAL/BULLISH_CROSS | -0.5342/5.3443/1.5892 | BULLISH/MIXED/MIXED | +11.55% / +36.10% | +10.16pp / +31.97pp | L010, L018–L020 |
| MET | SELL_SETUP_2/SELL_SETUP_9/SELL_SETUP_4 | 68.04/71.35/67.86 | BULLISH_CROSS/ABOVE_SIGNAL/BULLISH_CROSS | 0.0194/1.5025/0.8538 | BULLISH/BULLISH/BULLISH | +10.75% / +21.48% | +9.36pp / +17.35pp | L010, L018–L020 |
| UNP | SELL_SETUP_3/SELL_SETUP_6/SELL_SETUP_9 | 62.46/67.48/67.29 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | 0.8732/3.2961/6.0354 | BULLISH/BULLISH/BULLISH | +11.53% / +13.62% | +10.14pp / +9.49pp | L010, L018–L020 |
| IVZ | SELL_SETUP_4/SELL_SETUP_4/SELL_SETUP_9 | 60.68/65.03/69.22 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | 0.1117/0.2384/0.6792 | BULLISH/BULLISH/BULLISH | +15.10% / +18.35% | +13.71pp / +14.22pp | L010, L018–L020 |
| PFG | SELL_SETUP_1/SELL_SETUP_9/SELL_SETUP_9 | 54.18/66.53/73.58 | BELOW_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | -0.58/0.3837/2.6801 | BULLISH/BULLISH/BULLISH | +3.29% / +12.59% | +1.90pp / +8.46pp | L010, L018–L020 |
| PRU | SELL_SETUP_2/SELL_SETUP_9/SELL_SETUP_2 | 72.36/70.86/64.54 | ABOVE_SIGNAL/ABOVE_SIGNAL/BULLISH_CROSS | 0.1706/2.3755/0.6228 | BULLISH/BULLISH/BULLISH | +12.60% / +28.14% | +11.21pp / +24.01pp | L010, L018–L020 |
| NSC | SELL_SETUP_3/SELL_SETUP_6/SELL_SETUP_4 | 64.18/66.04/66.36 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | 1.5957/3.208/4.6948 | BULLISH/BULLISH/BULLISH | +9.76% / +10.48% | +8.37pp / +6.35pp | L010, L018–L020 |
| ITW | SELL_SETUP_3/SELL_SETUP_8/SELL_SETUP_1 | 66.39/64.09/60.75 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | 0.6579/2.8038/1.6066 | BULLISH/BULLISH/BULLISH | +7.04% / +7.86% | +5.65pp / +3.73pp | L010, L018–L020 |
| CTAS | SELL_SETUP_2/SELL_SETUP_6/SELL_SETUP_1 | 75.19/67.27/59.73 | ABOVE_SIGNAL/ABOVE_SIGNAL/BELOW_SIGNAL | 1.9871/4.9207/-3.9075 | BULLISH/MIXED/BULLISH | +22.73% / +21.62% | +21.34pp / +17.49pp | L010, L018–L020 |
| EXR | SELL_SETUP_2/BUY_SETUP_2/SELL_SETUP_1 | 55.25/56.59/55.03 | BULLISH_CROSS/ABOVE_SIGNAL/ABOVE_SIGNAL | 0.0293/0.4469/1.2915 | BULLISH/BULLISH/BULLISH | -0.62% / +6.67% | -2.01pp / +2.54pp | L010, L018–L020 |
| MPC | BUY_SETUP_3/SELL_SETUP_6/SELL_SETUP_6 | 69.71/73.77/81.22 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | 1.0818/5.1368/11.17 | BULLISH/BULLISH/BULLISH | +22.94% / +29.66% | +21.55pp / +25.53pp | L010, L018–L020 |
| WELL | SELL_SETUP_9/SELL_SETUP_6/SELL_SETUP_4 | 67.61/69.59/77.07 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | 0.6439/3.0898/4.0248 | BULLISH/BULLISH/BULLISH | +9.24% / +17.49% | +7.85pp / +13.36pp | L010, L018–L020 |
| CB | SELL_SETUP_3/BUY_SETUP_1/SELL_SETUP_9 | 59.4/64.6/69.25 | BULLISH_CROSS/ABOVE_SIGNAL/ABOVE_SIGNAL | 0.0659/2.4868/3.3595 | BULLISH/BULLISH/BULLISH | +5.12% / +10.52% | +3.73pp / +6.39pp | L010, L018–L020 |
| LMT | SELL_SETUP_4/SELL_SETUP_2/BUY_SETUP_3 | 70.25/56.94/58.69 | ABOVE_SIGNAL/BULLISH_CROSS/ABOVE_SIGNAL | 7.495/1.6986/3.6519 | BULLISH/BULLISH/BULLISH | +14.31% / +14.51% | +12.92pp / +10.38pp | L010, L018–L020 |
| PM | SELL_SETUP_2/SELL_SETUP_3/SELL_SETUP_1 | 62.03/65.58/69.54 | ABOVE_SIGNAL/ABOVE_SIGNAL/BULLISH_CROSS | 0.9419/1.6841/0.751 | BULLISH/BULLISH/BULLISH | +8.24% / +21.25% | +6.85pp / +17.12pp | L010, L018–L020 |
| BNY | BUY_SETUP_1/SELL_SETUP_9/SELL_SETUP_9 | 62.23/82.91/90.85 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | 0.0326/1.4884/3.7193 | BULLISH/BULLISH/BULLISH | +10.34% / +19.75% | +8.95pp / +15.62pp | L010, L018–L020 |
| PKG | SELL_SETUP_3/SELL_SETUP_8/SELL_SETUP_2 | 69.48/65.62/67.69 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | 1.9291/2.9965/2.2022 | BULLISH/BULLISH/BULLISH | +4.48% / +17.58% | +3.09pp / +13.45pp | L010, L018–L020 |

TD-9 setup `9` and RSI ≥ 70 are treated as **exhaustion flags**, not standalone signals: they reduce
`Tech_Z` through the RSI-headroom metric and add the −0.05 penalty only when *both* fire together
(L037). MACD is read as supportive only where it aligns with momentum and relative strength.

## Investable Determination

| Evidence threshold (`rules.md § Evidence Thresholds`) | Result |
|---|---|
| 1. Adjusted-score percentile ≥ 80th | **PASS** — 103 names qualify |
| 2. At least 3 of 4 factor families non-negative | **FAIL** — only 2 families exist (L046, L047); unsatisfiable for every name |
| 3. No single family > 50% of conviction | **FAIL** — Tech_Z supplies 66.7% of every composite by construction |
| 4. Data completeness ≥ 85% | **FAIL** — DQ 0.8 (80%) |
| 5. No hard stop from `§ Stop Criteria` | PASS |

**0 of 514 names are investable.** Fewer than 5 ⇒ `NO_TRADE` per `rules.md § Stop Criteria`
Downgrade #1. All 24 published names are **monitoring sleeve**; each still carries a full
`mu`/`sigma`/CI so it is settleable — a monitor list without forecasts would be a publishing failure,
not caution.

## Near-Miss Rejection Log

308 of 514 names fall below the 60th percentile and are not ranked in either
sleeve. The 7 ungrounded top-30 entrants above are the true near-misses:
they may well deserve a place, and the honest statement is that **this run does not know**, because their
event risk was never verified.
