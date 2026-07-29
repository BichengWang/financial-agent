# 05 Factor Scores — 2026-07-29

Primary home for `Adj Score` explainability. Percentiles are **`INDEX_UNION_PCTL (n=514)`**.

## Family Construction

Each metric is winsorized at the 5th/95th percentile across the 514-name universe, then z-scored; a
family is the equal-weighted mean of its available metric z-scores (>= 2 required, else `UNAVAILABLE`).

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

**Return basis.** Every momentum, relative-strength, volatility, beta, tracking-error and drawdown
input is computed from **adjusted** closes (L003); entry, target and CI prices use the unadjusted
2026-07-28 close (L002). This is the Track B rule accepted 2026-07-26. The universe-wide scan for
last-bar `c` != `a` found exactly **1** name (WST, ex-dividend 2026-07-28), and it is not in the published
set — a quieter day than 2026-07-28, when three published names carried the artifact.

**Disclosed judgment — defensive Macro polarity (`INFERRED`, L050).** Lower beta, lower realized vol
and shallower drawdown score *better* this run. This is a regime-conditional reading of the `03`
evidence (SPY below both moving averages, SOXX -24.97% from its 60-day
high, 42.02% of the universe at negative beta, TLT
-3.31% over 20 days). It is **not** a permanent rule and **not** a family-weight
change — weights are protected and gated at `eff_n = 1`.

Unlike prior runs, this polarity now has **direct settled evidence** behind it rather than only
contemporaneous technicals: over the exact 2026-07-01 → 2026-07-28 window, the defensive baseline book
returned +2.11% mean alpha while the semiconductor-heavy book returned
-14.24% (`02 § 1`, L051). That is a 16.3pp
spread realized over the settlement window, not a forecast. It remains disclosed judgment, and it is
the single largest reason insurers, staples, rails, defense and lab-services names fill the top of the
book — **19 of the 24 published names carry negative beta**.

**Data-quality multiplier: 0.8** for every name — "notable coverage gaps", two of four families
`UNAVAILABLE` plus the entire Enhancing block (L036, L046, L047, L048). Since 0.8 < 0.85,
`rules.md § Evidence Thresholds` #4 independently forbids marking any name investable.

**Calibration feedback applied** (from `02 § 0`): weighted-mean rank IC **-0.2064** over 298
settled pairs (>= 20) → **confidence capped at `MEDIUM` universe-wide**; no name carries `HIGH` anywhere
in this package. CI coverage 74.50% is inside the healthy 55–85% band, so the
sigma-widening rule does **not** fire and sigma stays `REALIZED_VOL_30D`. **No positive per-name `mu`
adjustment was made anywhere** — every `mu` is the unmodified mu-Calibration-Table value for the name's
percentile band (L027).

## Penalties Applied

| Penalty | Rule | Value | Names (universe) | In published set |
|---|---|---|---|---|
| Earnings inside 14 calendar days | `rules.md § Risk Controls` | **−0.10**, confidence capped `LOW` | 272 | 1 (ADP) |
| 30d realized vol > 2× universe median (0.0968 → threshold 0.1937) | `rules.md § Risk Controls` | −0.05 | 31 | 0 |
| TD-9 daily sell-setup 9 **and** RSI(14) daily >= 70 | `rules.md § TD-9 Definition` | −0.05 | 9 | 1 (DGX) |
| Unstable earnings profile | `rules.md § Risk Controls` | **not applied** | — | Requires fundamentals — `UNAVAILABLE` (L046). Disclosed as an *unapplied* penalty, not as absent risk |
| Size > 2% of 20-day ADV | `rules.md § Risk Controls` | **not binding** | — | No position is sized; `NO_TRADE` |

293 of 514 names carry at least one penalty. The earnings count is high because 2026-07-29 sits at the
peak of Q2 reporting season — 272 of 514 names print within 14 days, and 56
report **today**.

### Earnings-date grounding — method changed this run

Earnings dates are now grounded by a **forward calendar sweep** rather than the per-name
vendor-empty print-signature heuristic. This is this run's accepted Track B change; the full
problem statement, validation and decision are in `13_evolution_log.md`.

| | Retired heuristic | **Adopted method** |
|---|---|---|
| Source | `api.nasdaq.com/api/analyst/{sym}/earnings-date` per name | `api.nasdaq.com/api/calendar/earnings?date=…` swept forward (L022) |
| Coverage | 59 shortlist names over 2 bounded passes | **514 of 514 — the entire universe** |
| Sweep completeness | n/a | **28/28 business days, 0 failures**, 2026-07-29 → 2026-09-04 |
| Vendor-empty fallback | infer "+91d" from a past price/volume signature | none needed |
| Cross-validation | — | **25/25 agreement** with the per-name endpoint's `CONFIRMED` dates, 0 disagreements (L023) |

Grounding states: **317** names appear on a dated calendar page
inside the window; **197** do not appear in a *complete* sweep, which
is positive evidence that they do not report before 2026-09-04. Both states are grounded, so
**no name is excluded from publication for want of an earnings date** — the "skip ungrounded names"
rule that shaped the 2026-07-26, -27 and -28 published sets has nothing to skip, and this run's set is
a clean contiguous ranks 1–24.

**What the change caught.** The heuristic and the calendar disagree on the penalty for **9
names**, and six of those were about to be published as penalty-free:

| Ticker | Heuristic said | Calendar says | Penalty |
|---|---|---|---|
| ADP | ESTIMATED_CADENCE (+91d) | 2026-07-29 (+0d) | **none → −0.10** |
| AON | ESTIMATED_CADENCE (+91d) | 2026-07-29 (+0d) | **none → −0.10** |
| FICO | ESTIMATED_CADENCE (+91d) | 2026-07-29 (+0d) | **none → −0.10** |
| VRSK | ESTIMATED_CADENCE (+91d) | 2026-07-29 (+0d) | **none → −0.10** |
| AWK | ESTIMATED_CADENCE (+91d) | 2026-07-29 (+0d) | **none → −0.10** |
| HUM | ESTIMATED_CADENCE (+91d) | 2026-07-29 (+0d) | **none → −0.10** |
| SCHW | ESTIMATED_PRINT_WEEK (+3d) | >2026-09-04 (+38d) | **−0.10 → none** |
| ACGL | ESTIMATED_PRINT_WEEK (+3d) | >2026-09-04 (+38d) | **−0.10 → none** |
| FE | ESTIMATED_PRINT_WEEK (+3d) | >2026-09-04 (+38d) | **−0.10 → none** |

**6 false "clear of earnings" calls** — ADP, AON, AWK, FICO, HUM and VRSK all report **today**,
yet the heuristic scored them at "+91d, no penalty". ADP ranked #4 and AON #8 pre-regrounding. This is
the same failure class the 2026-07-27 Track B change addressed (a non-resolution reading downstream as
*penalty-free*) arriving by a different route. 3 names moved the other way — SCHW, ACGL and FE
were penalised by the conservative `ESTIMATED_PRINT_WEEK` branch but do not print inside the window.

## Ranked Candidate Table — Published Set (24 names)

Field derivations per `rules.md § Price and Target Citation Standard`. `mu` from the mu Calibration
Table band for each name's percentile (L027); `sigma` = `REALIZED_VOL_30D` (L013);
`target_price = entry × (1 + mu)` (L028); CI bounds = `entry × (1 + mu ± 1.04σ)` (L029). Target date
**2026-08-26** (`run_date + 28d`). Every name below is at or above the 95th percentile, so every `mu` is
the table's `+6.0%` band. **Every name below is monitoring sleeve — zero investable.**

| Ticker | Company | Entry | Date | Tag | Adj Score | Score Trace | Pctl | Beta | 30d RVol | Sharpe | Sortino | IR | Kelly .25 | VaR95 | CVaR95 | MaxDD60 | TD9 D/W/M | RSI14 D/W/M | MACD D/W/M | Days→Earn | mu | sigma | SigSrc | Target | Target Date | CI Lo | CI Hi | Ledger | Metric Ledger | Conf | Primary Thesis | Key Risk |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| TRV | The Travelers Companies In | 397.22 | 2026-07-28 | HISTORICAL | +0.3311 | (0.30×0.00<sub>UNAVL</sub> + 0.30×+0.9621 + 0.25×0.00<sub>UNAVL</sub> + 0.15×+0.8348) × 0.8 − 0.00 = +0.3311 | 100.00 | -0.729 | 9.32% | 0.6100 | 1.7076 | 0.8693 | 0.0500 | -9.38% | -13.20% | -5.96% | SELL_SETUP_8/SELL_SETUP_9/SELL_SETUP_9 | 83.33/81.20/78.14 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | >2026-09-04 (NO_PRINT_IN_WINDOW) | +6.0% | 9.32% | REALIZED_VOL_30D | 421.05 | 2026-08-26 | 382.55 | 459.56 | L002,L003,L011 | L013-L021,L027-L035 | MEDIUM | Finance / Property-Casualty Insurers; RS60 +27.4pp, mom60 +30.7% | RSI14_d 83.33 overbought; beta -0.729 reverses in a risk-on turn |
| PAYX | Paychex Inc. Common Stock | 118.87 | 2026-07-28 | HISTORICAL | +0.3283 | (0.30×0.00<sub>UNAVL</sub> + 0.30×+1.0044 + 0.25×0.00<sub>UNAVL</sub> + 0.15×+0.7269) × 0.8 − 0.00 = +0.3283 | 99.81 | -0.562 | 9.73% | 0.5844 | 1.3375 | 0.6965 | 0.0500 | -10.05% | -14.04% | -6.35% | SELL_SETUP_2/SELL_SETUP_9/SELL_SETUP_2 | 73.00/69.69/53.88 | ABOVE_SIGNAL/ABOVE_SIGNAL/BELOW_SIGNAL | >2026-09-04 (NO_PRINT_IN_WINDOW) | +6.0% | 9.73% | REALIZED_VOL_30D | 126.00 | 2026-08-26 | 113.97 | 138.03 | L002,L003,L011 | L013-L021,L027-L035 | MEDIUM | Industrials / Diversified Commercial Services; RS60 +28.0pp, mom60 +31.3% | RSI14_d 73.00 overbought; beta -0.562 reverses in a risk-on turn |
| INCY | Incyte Corp. Common Stock | 129.93 | 2026-07-28 | HISTORICAL | +0.3174 | (0.30×0.00<sub>UNAVL</sub> + 0.30×+1.1939 + 0.25×0.00<sub>UNAVL</sub> + 0.15×+0.2571) × 0.8 − 0.00 = +0.3174 | 99.61 | -0.356 | 12.94% | 0.4394 | 0.8457 | 0.5664 | 0.0500 | -15.35% | -20.66% | -9.50% | SELL_SETUP_3/SELL_SETUP_9/SELL_SETUP_2 | 76.76/72.68/77.32 | BULLISH_CROSS/ABOVE_SIGNAL/ABOVE_SIGNAL | >2026-09-04 (NO_PRINT_IN_WINDOW) | +6.0% | 12.94% | REALIZED_VOL_30D | 137.73 | 2026-08-26 | 120.24 | 155.21 | L002,L003,L011 | L013-L021,L027-L035 | MEDIUM | Health Care / Biotechnology: Commercial Physical; RS60 +33.0pp, mom60 +36.4% | RSI14_d 76.76 overbought; beta -0.356 reverses in a risk-on turn |
| BRO | Brown & Brown Inc. Common  | 73.65 | 2026-07-28 | HISTORICAL | +0.3034 | (0.30×0.00<sub>UNAVL</sub> + 0.30×+0.9230 + 0.25×0.00<sub>UNAVL</sub> + 0.15×+0.6826) × 0.8 − 0.00 = +0.3034 | 99.42 | -0.990 | 11.54% | 0.4926 | 1.4159 | 0.6581 | 0.0500 | -13.04% | -17.78% | -6.59% | SELL_SETUP_2/SELL_SETUP_9/SELL_SETUP_1 | 69.06/57.94/45.63 | BULLISH_CROSS/ABOVE_SIGNAL/BELOW_SIGNAL | >2026-09-04 (NO_PRINT_IN_WINDOW) | +6.0% | 11.54% | REALIZED_VOL_30D | 78.07 | 2026-08-26 | 69.23 | 86.91 | L002,L003,L011 | L013-L021,L027-L035 | MEDIUM | Finance / Specialty Insurers; RS60 +19.5pp, mom60 +22.8% | beta -0.990 reverses in a risk-on turn |
| RTX | RTX Corporation Common Sto | 218.58 | 2026-07-28 | HISTORICAL | +0.2925 | (0.30×0.00<sub>UNAVL</sub> + 0.30×+0.9084 + 0.25×0.00<sub>UNAVL</sub> + 0.15×+0.6210) × 0.8 − 0.00 = +0.2925 | 99.22 | -0.105 | 9.49% | 0.5989 | 1.0365 | 0.7017 | 0.0500 | -9.67% | -13.56% | -5.58% | SELL_SETUP_5/SELL_SETUP_9/SELL_SETUP_1 | 77.42/69.22/76.01 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | >2026-09-04 (NO_PRINT_IN_WINDOW) | +6.0% | 9.49% | REALIZED_VOL_30D | 231.69 | 2026-08-26 | 210.11 | 253.28 | L002,L003,L011 | L013-L021,L027-L035 | MEDIUM | Industrials / Aerospace; RS60 +21.3pp, mom60 +24.7% | RSI14_d 77.42 overbought; beta -0.105 reverses in a risk-on turn |
| KO | Coca-Cola Company (The) Co | 88.27 | 2026-07-28 | HISTORICAL | +0.2867 | (0.30×0.00<sub>UNAVL</sub> + 0.30×+0.7504 + 0.25×0.00<sub>UNAVL</sub> + 0.15×+0.8887) × 0.8 − 0.00 = +0.2867 | 99.03 | -0.639 | 8.21% | 0.6925 | 1.3266 | 0.9465 | 0.0500 | -7.55% | -10.91% | -6.23% | SELL_SETUP_3/SELL_SETUP_1/SELL_SETUP_9 | 67.03/69.10/73.28 | BULLISH_CROSS/ABOVE_SIGNAL/ABOVE_SIGNAL | >2026-09-04 (NO_PRINT_IN_WINDOW) | +6.0% | 8.21% | REALIZED_VOL_30D | 93.57 | 2026-08-26 | 86.03 | 101.10 | L002,L003,L011 | L013-L021,L027-L035 | MEDIUM | Consumer Staples / Beverages (Production/Distribution; RS60 +9.4pp, mom60 +12.8% | beta -0.639 reverses in a risk-on turn |
| MRSH | Marsh Common Stock | 192.19 | 2026-07-28 | HISTORICAL | +0.2796 | (0.30×0.00<sub>UNAVL</sub> + 0.30×+0.7407 + 0.25×0.00<sub>UNAVL</sub> + 0.15×+0.8484) × 0.8 − 0.00 = +0.2796 | 98.83 | -0.872 | 9.59% | 0.5932 | 1.3437 | 0.8362 | 0.0500 | -9.82% | -13.75% | -6.28% | SELL_SETUP_2/SELL_SETUP_6/SELL_SETUP_1 | 70.50/63.16/51.79 | BULLISH_CROSS/ABOVE_SIGNAL/BELOW_SIGNAL | >2026-09-04 (NO_PRINT_IN_WINDOW) | +6.0% | 9.59% | REALIZED_VOL_30D | 203.72 | 2026-08-26 | 184.56 | 222.88 | L002,L003,L011 | L013-L021,L027-L035 | MEDIUM | Finance / Specialty Insurers; RS60 +11.9pp, mom60 +15.2% | RSI14_d 70.50 overbought; beta -0.872 reverses in a risk-on turn |
| IQV | IQVIA Holdings Inc. Common | 242.94 | 2026-07-28 | HISTORICAL | +0.2690 | (0.30×0.00<sub>UNAVL</sub> + 0.30×+1.2335 + 0.25×0.00<sub>UNAVL</sub> + 0.15×-0.2256) × 0.8 − 0.00 = +0.2690 | 98.64 | +0.199 | 16.02% | 0.3550 | 1.0069 | 0.4000 | 0.0500 | -20.43% | -26.99% | -10.23% | SELL_SETUP_4/SELL_SETUP_6/SELL_SETUP_2 | 79.55/69.06/58.87 | BULLISH_CROSS/ABOVE_SIGNAL/BULLISH_CROSS | >2026-09-04 (NO_PRINT_IN_WINDOW) | +6.0% | 16.02% | REALIZED_VOL_30D | 257.52 | 2026-08-26 | 217.05 | 297.98 | L002,L003,L011 | L013-L021,L027-L035 | MEDIUM | Health Care / Biotechnology: Commercial Physical; RS60 +50.0pp, mom60 +53.4% | RSI14_d 79.55 overbought |
| CTAS | Cintas Corporation Common  | 214.90 | 2026-07-28 | HISTORICAL | +0.2563 | (0.30×0.00<sub>UNAVL</sub> + 0.30×+0.7800 + 0.25×0.00<sub>UNAVL</sub> + 0.15×+0.5760) × 0.8 − 0.00 = +0.2563 | 98.44 | -0.295 | 10.04% | 0.5663 | 1.3277 | 0.6730 | 0.0500 | -10.57% | -14.68% | -7.19% | SELL_SETUP_3/SELL_SETUP_6/SELL_SETUP_1 | 77.29/68.82/60.73 | ABOVE_SIGNAL/ABOVE_SIGNAL/BELOW_SIGNAL | >2026-09-04 (NO_PRINT_IN_WINDOW) | +6.0% | 10.04% | REALIZED_VOL_30D | 227.79 | 2026-08-26 | 205.35 | 250.23 | L002,L003,L011 | L013-L021,L027-L035 | MEDIUM | Industrials / Garments and Clothing; RS60 +20.0pp, mom60 +23.3% | RSI14_d 77.29 overbought; beta -0.295 reverses in a risk-on turn |
| ITW | Illinois Tool Works Inc. C | 295.16 | 2026-07-28 | HISTORICAL | +0.2527 | (0.30×0.00<sub>UNAVL</sub> + 0.30×+0.7622 + 0.25×0.00<sub>UNAVL</sub> + 0.15×+0.5819) × 0.8 − 0.00 = +0.2527 | 98.25 | +0.560 | 7.27% | 0.7826 | 1.6290 | 0.9490 | 0.0500 | -5.99% | -8.97% | -5.65% | SELL_SETUP_4/SELL_SETUP_8/SELL_SETUP_1 | 72.92/68.28/63.00 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | >2026-09-04 (NO_PRINT_IN_WINDOW) | +6.0% | 7.27% | REALIZED_VOL_30D | 312.87 | 2026-08-26 | 290.57 | 335.17 | L002,L003,L011 | L013-L021,L027-L035 | MEDIUM | Industrials / Industrial Machinery/Components; RS60 +11.7pp, mom60 +15.1% | RSI14_d 72.92 overbought |
| PM | Philip Morris Internationa | 200.17 | 2026-07-28 | HISTORICAL | +0.2513 | (0.30×0.00<sub>UNAVL</sub> + 0.30×+0.7418 + 0.25×0.00<sub>UNAVL</sub> + 0.15×+0.6106) × 0.8 − 0.00 = +0.2513 | 98.05 | -0.575 | 9.46% | 0.6009 | 1.2425 | 0.7163 | 0.0500 | -9.61% | -13.49% | -10.01% | SELL_SETUP_3/SELL_SETUP_3/SELL_SETUP_1 | 65.71/67.78/70.59 | ABOVE_SIGNAL/ABOVE_SIGNAL/BULLISH_CROSS | >2026-09-04 (NO_PRINT_IN_WINDOW) | +6.0% | 9.46% | REALIZED_VOL_30D | 212.18 | 2026-08-26 | 192.48 | 231.88 | L002,L003,L011 | L013-L021,L027-L035 | MEDIUM | Health Care / Medicinal Chemicals and Botanical ; RS60 +18.9pp, mom60 +22.3% | beta -0.575 reverses in a risk-on turn |
| VLTO | Veralto Corp Common Stock  | 98.47 | 2026-07-28 | HISTORICAL | +0.2356 | (0.30×0.00<sub>UNAVL</sub> + 0.30×+0.5797 + 0.25×0.00<sub>UNAVL</sub> + 0.15×+0.8036) × 0.8 − 0.00 = +0.2356 | 97.86 | -0.406 | 7.77% | 0.7320 | 1.5331 | 0.8543 | 0.0500 | -6.82% | -10.00% | -7.33% | SELL_SETUP_2/SELL_SETUP_6/SELL_SETUP_1 | 70.19/60.38/54.12 | BULLISH_CROSS/ABOVE_SIGNAL/BELOW_SIGNAL | >2026-09-04 (NO_PRINT_IN_WINDOW) | +6.0% | 7.77% | REALIZED_VOL_30D | 104.38 | 2026-08-26 | 96.42 | 112.33 | L002,L003,L011 | L013-L021,L027-L035 | MEDIUM | Industrials / Electrical Products; RS60 +8.5pp, mom60 +11.8% | RSI14_d 70.19 overbought; beta -0.406 reverses in a risk-on turn |
| WELL | Welltower Inc. Common Stoc | 243.57 | 2026-07-28 | HISTORICAL | +0.2315 | (0.30×0.00<sub>UNAVL</sub> + 0.30×+0.5757 + 0.25×0.00<sub>UNAVL</sub> + 0.15×+0.7775) × 0.8 − 0.00 = +0.2315 | 97.66 | -0.646 | 7.23% | 0.7864 | 1.4217 | 0.8505 | 0.0500 | -5.93% | -8.89% | -11.26% | BUY_SETUP_1/SELL_SETUP_6/SELL_SETUP_4 | 60.30/66.09/76.35 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | >2026-09-04 (NO_PRINT_IN_WINDOW) | +6.0% | 7.23% | REALIZED_VOL_30D | 258.18 | 2026-08-26 | 239.87 | 276.50 | L002,L003,L011 | L013-L021,L027-L035 | MEDIUM | Real Estate / Real Estate Investment Trusts; RS60 +9.1pp, mom60 +12.5% | beta -0.646 reverses in a risk-on turn |
| UNP | Union Pacific Corporation  | 294.45 | 2026-07-28 | HISTORICAL | +0.2268 | (0.30×0.00<sub>UNAVL</sub> + 0.30×+0.5854 + 0.25×0.00<sub>UNAVL</sub> + 0.15×+0.7195) × 0.8 − 0.00 = +0.2268 | 97.47 | -0.211 | 7.85% | 0.7239 | 1.1658 | 0.8135 | 0.0500 | -6.96% | -10.18% | -7.58% | SELL_SETUP_4/SELL_SETUP_6/SELL_SETUP_9 | 57.11/64.40/66.42 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | >2026-09-04 (NO_PRINT_IN_WINDOW) | +6.0% | 7.85% | REALIZED_VOL_30D | 312.12 | 2026-08-26 | 288.06 | 336.17 | L002,L003,L011 | L013-L021,L027-L035 | MEDIUM | Industrials / Railroads; RS60 +6.5pp, mom60 +9.8% | beta -0.211 reverses in a risk-on turn |
| SJM | The J.M. Smucker Company C | 123.04 | 2026-07-28 | HISTORICAL | +0.2185 | (0.30×0.00<sub>UNAVL</sub> + 0.30×+0.5481 + 0.25×0.00<sub>UNAVL</sub> + 0.15×+0.7246) × 0.8 − 0.00 = +0.2185 | 97.27 | -0.792 | 9.73% | 0.5846 | 1.1665 | 0.6469 | 0.0500 | -10.05% | -14.04% | -8.42% | SELL_SETUP_9/SELL_SETUP_3/SELL_SETUP_1 | 67.23/67.19/58.67 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | 28d (2026-08-26, CONFIRMED_CALENDAR) | +6.0% | 9.73% | REALIZED_VOL_30D | 130.42 | 2026-08-26 | 117.98 | 142.87 | L002,L003,L011 | L013-L021,L027-L035 | MEDIUM | Consumer Staples / Packaged Foods; RS60 +23.6pp, mom60 +26.9% | beta -0.792 reverses in a risk-on turn |
| SCHW | Charles Schwab Corporation | 105.97 | 2026-07-28 | HISTORICAL | +0.2134 | (0.30×0.00<sub>UNAVL</sub> + 0.30×+0.5031 + 0.25×0.00<sub>UNAVL</sub> + 0.15×+0.7723) × 0.8 − 0.00 = +0.2134 | 97.08 | -0.331 | 7.70% | 0.7385 | 1.2078 | 0.8274 | 0.0500 | -6.70% | -9.86% | -7.62% | SELL_SETUP_2/SELL_SETUP_9/SELL_SETUP_1 | 69.81/66.94/65.57 | BULLISH_CROSS/ABOVE_SIGNAL/BELOW_SIGNAL | >2026-09-04 (NO_PRINT_IN_WINDOW) | +6.0% | 7.70% | REALIZED_VOL_30D | 112.33 | 2026-08-26 | 103.84 | 120.81 | L002,L003,L011 | L013-L021,L027-L035 | MEDIUM | Finance / Investment Bankers/Brokers/Service; RS60 +12.7pp, mom60 +16.1% | beta -0.331 reverses in a risk-on turn |
| ACGL | Arch Capital Group Ltd. Co | 106.48 | 2026-07-28 | HISTORICAL | +0.2127 | (0.30×0.00<sub>UNAVL</sub> + 0.30×+0.4538 + 0.25×0.00<sub>UNAVL</sub> + 0.15×+0.8646) × 0.8 − 0.00 = +0.2127 | 96.88 | -0.753 | 7.44% | 0.7644 | 1.5742 | 1.0359 | 0.0500 | -6.27% | -9.32% | -9.52% | SELL_SETUP_3/SELL_SETUP_6/SELL_SETUP_1 | 67.47/66.61/62.41 | BULLISH_CROSS/ABOVE_SIGNAL/BELOW_SIGNAL | >2026-09-04 (NO_PRINT_IN_WINDOW) | +6.0% | 7.44% | REALIZED_VOL_30D | 112.87 | 2026-08-26 | 104.63 | 121.11 | L002,L003,L011 | L013-L021,L027-L035 | MEDIUM | Finance / Property-Casualty Insurers; RS60 +9.4pp, mom60 +12.7% | beta -0.753 reverses in a risk-on turn |
| ADP | Automatic Data Processing  | 264.17 | 2026-07-28 | HISTORICAL | +0.2058 | (0.30×0.00<sub>UNAVL</sub> + 0.30×+0.9295 + 0.25×0.00<sub>UNAVL</sub> + 0.15×+0.6891) × 0.8 − 0.10 = +0.2058 | 96.69 | -0.649 | 10.00% | 0.5688 | 1.3449 | 0.6983 | 0.0500 | -10.49% | -14.59% | -7.49% | SELL_SETUP_2/SELL_SETUP_6/SELL_SETUP_2 | 69.25/64.84/54.59 | BULLISH_CROSS/ABOVE_SIGNAL/BELOW_SIGNAL | 0d (2026-07-29, CONFIRMED_CALENDAR) | +6.0% | 10.00% | REALIZED_VOL_30D | 280.02 | 2026-08-26 | 252.56 | 307.48 | L002,L003,L011 | L013-L021,L027-L035 | LOW | Industrials / Diversified Commercial Services; RS60 +22.2pp, mom60 +25.6% | reports 2026-07-29 — inside horizon; beta -0.649 reverses in a risk-on turn |
| OMC | Omnicom Group Inc. Common  | 86.22 | 2026-07-28 | HISTORICAL | +0.2035 | (0.30×0.00<sub>UNAVL</sub> + 0.30×+0.7297 + 0.25×0.00<sub>UNAVL</sub> + 0.15×+0.2361) × 0.8 − 0.00 = +0.2035 | 96.49 | +0.109 | 11.66% | 0.4876 | 0.6751 | 0.5848 | 0.0500 | -13.24% | -18.02% | -8.77% | SELL_SETUP_2/SELL_SETUP_6/SELL_SETUP_1 | 65.22/61.92/56.84 | BULLISH_CROSS/ABOVE_SIGNAL/BULLISH_CROSS | >2026-09-04 (NO_PRINT_IN_WINDOW) | +6.0% | 11.66% | REALIZED_VOL_30D | 91.39 | 2026-08-26 | 80.94 | 101.85 | L002,L003,L011 | L013-L021,L027-L035 | MEDIUM | Consumer Discretionary / Advertising; RS60 +10.2pp, mom60 +13.6% | 2 of 4 families UNAVAILABLE |
| DGX | Quest Diagnostics Incorpor | 235.94 | 2026-07-28 | HISTORICAL | +0.2004 | (0.30×0.00<sub>UNAVL</sub> + 0.30×+0.6599 + 0.25×0.00<sub>UNAVL</sub> + 0.15×+0.7671) × 0.8 − 0.05 = +0.2004 | 96.30 | -0.642 | 9.64% | 0.5895 | 1.9766 | 0.8404 | 0.0500 | -9.91% | -13.87% | -6.22% | SELL_SETUP_9/SELL_SETUP_6/SELL_SETUP_6 | 77.23/71.19/70.36 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | >2026-09-04 (NO_PRINT_IN_WINDOW) | +6.0% | 9.64% | REALIZED_VOL_30D | 250.10 | 2026-08-26 | 226.43 | 273.76 | L002,L003,L011 | L013-L021,L027-L035 | MEDIUM | Health Care / Medical Specialities; RS60 +18.6pp, mom60 +22.0% | RSI14_d 77.23 overbought; beta -0.642 reverses in a risk-on turn |
| BBY | Best Buy Co. Inc. Common S | 89.47 | 2026-07-28 | HISTORICAL | +0.1978 | (0.30×0.00<sub>UNAVL</sub> + 0.30×+0.7133 + 0.25×0.00<sub>UNAVL</sub> + 0.15×+0.2222) × 0.8 − 0.00 = +0.1978 | 96.10 | +0.790 | 9.04% | 0.6293 | 1.1331 | 0.4359 | 0.0500 | -8.91% | -12.61% | -8.93% | SELL_SETUP_3/SELL_SETUP_9/SELL_SETUP_3 | 72.57/68.98/61.46 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | 29d (2026-08-27, CONFIRMED_CALENDAR) | +6.0% | 9.04% | REALIZED_VOL_30D | 94.84 | 2026-08-26 | 86.43 | 103.25 | L002,L003,L011 | L013-L021,L027-L035 | MEDIUM | Consumer Discretionary / Consumer Electronics/Video Chains; RS60 +46.5pp, mom60 +49.9% | RSI14_d 72.57 overbought |
| PFG | Principal Financial Group  | 114.09 | 2026-07-28 | HISTORICAL | +0.1972 | (0.30×0.00<sub>UNAVL</sub> + 0.30×+0.4386 + 0.25×0.00<sub>UNAVL</sub> + 0.15×+0.7665) × 0.8 − 0.00 = +0.1972 | 95.91 | -0.048 | 7.31% | 0.7780 | 0.9822 | 0.9508 | 0.0500 | -6.06% | -9.05% | -6.16% | SELL_SETUP_2/SELL_SETUP_9/SELL_SETUP_9 | 60.61/69.13/74.81 | BELOW_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | >2026-09-04 (NO_PRINT_IN_WINDOW) | +6.0% | 7.31% | REALIZED_VOL_30D | 120.94 | 2026-08-26 | 112.26 | 129.61 | L002,L003,L011 | L013-L021,L027-L035 | MEDIUM | Finance / Accident &Health Insurance; RS60 +10.6pp, mom60 +14.0% | beta -0.048 reverses in a risk-on turn |
| EXR | Extra Space Storage Inc Co | 152.21 | 2026-07-28 | HISTORICAL | +0.1946 | (0.30×0.00<sub>UNAVL</sub> + 0.30×+0.4013 + 0.25×0.00<sub>UNAVL</sub> + 0.15×+0.8195) × 0.8 − 0.00 = +0.1946 | 95.71 | -0.002 | 6.83% | 0.8324 | 1.7325 | 0.9050 | 0.0500 | -5.27% | -8.07% | -5.45% | SELL_SETUP_3/SELL_SETUP_1/SELL_SETUP_1 | 62.32/59.97/56.71 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | >2026-09-04 (NO_PRINT_IN_WINDOW) | +6.0% | 6.83% | REALIZED_VOL_30D | 161.34 | 2026-08-26 | 150.53 | 172.16 | L002,L003,L011 | L013-L021,L027-L035 | MEDIUM | Real Estate / Real Estate Investment Trusts; RS60 +4.0pp, mom60 +7.4% | beta -0.002 reverses in a risk-on turn |
| TMO | Thermo Fisher Scientific I | 576.41 | 2026-07-28 | HISTORICAL | +0.1942 | (0.30×0.00<sub>UNAVL</sub> + 0.30×+0.6015 + 0.25×0.00<sub>UNAVL</sub> + 0.15×+0.4158) × 0.8 − 0.00 = +0.1942 | 95.52 | +0.056 | 10.31% | 0.5514 | 1.8403 | 0.5805 | 0.0500 | -11.02% | -15.24% | -7.61% | SELL_SETUP_4/SELL_SETUP_9/SELL_SETUP_1 | 70.22/64.16/56.62 | ABOVE_SIGNAL/ABOVE_SIGNAL/BULLISH_CROSS | >2026-09-04 (NO_PRINT_IN_WINDOW) | +6.0% | 10.31% | REALIZED_VOL_30D | 610.99 | 2026-08-26 | 549.18 | 672.81 | L002,L003,L011 | L013-L021,L027-L035 | MEDIUM | Industrials / Industrial Machinery/Components; RS60 +17.1pp, mom60 +20.5% | RSI14_d 70.22 overbought |

### Published-set construction

All 514 scored names are earnings-grounded, so the set is simply **ranks 1–24, contiguous** —
percentile floor 95.52. There is no rank jump and no "excluded, never grounded"
list to disclose, unlike 2026-07-26 through 2026-07-28.

## Score Attribution

| Ticker | Fund_Z | Tech_Z | Sent_Z | Macro_Z | Composite_Z | DQ | Penalties | Adj Score | Top Positive Drivers | Top Negative Drivers | Metric Ledger Rows |
|---|---|---|---|---|---|---|---|---|---|---|---|
| TRV | `UNAVAILABLE` (L046) | +0.9621 | `UNAVAILABLE` (L047) | +0.8348 | +0.4138 | 0.8 | 0.00 | +0.3311 | RS60 vs SPY: z +1.82; 60d momentum: z +1.82; RS20 vs SPY: z +1.74 | RSI headroom to 70: z -1.60 | L013-L021 |
| PAYX | `UNAVAILABLE` (L046) | +1.0044 | `UNAVAILABLE` (L047) | +0.7269 | +0.4104 | 0.8 | 0.00 | +0.3283 | RS60 vs SPY: z +1.87; 60d momentum: z +1.87; RS20 vs SPY: z +1.74 | RSI headroom to 70: z -1.57 | L013-L021 |
| INCY | `UNAVAILABLE` (L046) | +1.1939 | `UNAVAILABLE` (L047) | +0.2571 | +0.3967 | 0.8 | 0.00 | +0.3174 | 20d volume ratio: z +2.45; RS60 vs SPY: z +1.87; 60d momentum: z +1.87 | RSI headroom to 70: z -1.60; 30d realized vol (lower better): z -0.63 | L013-L021 |
| BRO | `UNAVAILABLE` (L046) | +0.9230 | `UNAVAILABLE` (L047) | +0.6826 | +0.3793 | 0.8 | 0.00 | +0.3034 | 20d volume ratio: z +1.65; MACD state d+w: z +1.51; 60d beta (defensive polarity): z +1.37 | RSI headroom to 70: z -1.20; 30d realized vol (lower better): z -0.27 | L013-L021 |
| RTX | `UNAVAILABLE` (L046) | +0.9084 | `UNAVAILABLE` (L047) | +0.6210 | +0.3657 | 0.8 | 0.00 | +0.2925 | RS20 vs SPY: z +1.49; 20d momentum: z +1.49; RS60 vs SPY: z +1.38 | RSI headroom to 70: z -1.60 | L013-L021 |
| KO | `UNAVAILABLE` (L046) | +0.7504 | `UNAVAILABLE` (L047) | +0.8887 | +0.3584 | 0.8 | 0.00 | +0.2867 | 20d volume ratio: z +2.45; MACD state d+w: z +1.51; MA alignment d+w: z +1.20 | RSI headroom to 70: z -1.01 | L013-L021 |
| MRSH | `UNAVAILABLE` (L046) | +0.7407 | `UNAVAILABLE` (L047) | +0.8484 | +0.3495 | 0.8 | 0.00 | +0.2796 | MACD state d+w: z +1.51; RS20 vs SPY: z +1.41; 20d momentum: z +1.41 | RSI headroom to 70: z -1.34 | L013-L021 |
| IQV | `UNAVAILABLE` (L046) | +1.2335 | `UNAVAILABLE` (L047) | -0.2256 | +0.3362 | 0.8 | 0.00 | +0.2690 | 20d volume ratio: z +2.45; RS60 vs SPY: z +1.87; 60d momentum: z +1.87 | RSI headroom to 70: z -1.60; 30d realized vol (lower better): z -1.42 | L013-L021 |
| CTAS | `UNAVAILABLE` (L046) | +0.7800 | `UNAVAILABLE` (L047) | +0.5760 | +0.3204 | 0.8 | 0.00 | +0.2563 | RS20 vs SPY: z +1.74; 20d momentum: z +1.74; RS60 vs SPY: z +1.28 | RSI headroom to 70: z -1.60 | L013-L021 |
| ITW | `UNAVAILABLE` (L046) | +0.7622 | `UNAVAILABLE` (L047) | +0.5819 | +0.3159 | 0.8 | 0.00 | +0.2527 | 20d volume ratio: z +2.45; MA alignment d+w: z +1.20; 60d max drawdown (shallower better): z +1.06 | RSI headroom to 70: z -1.56; 60d beta (defensive polarity): z -0.14 | L013-L021 |
| PM | `UNAVAILABLE` (L046) | +0.7418 | `UNAVAILABLE` (L047) | +0.6106 | +0.3141 | 0.8 | 0.00 | +0.2513 | RS60 vs SPY: z +1.21; 60d momentum: z +1.21; MA alignment d+w: z +1.20 | RSI headroom to 70: z -0.89 | L013-L021 |
| VLTO | `UNAVAILABLE` (L046) | +0.5797 | `UNAVAILABLE` (L047) | +0.8036 | +0.2945 | 0.8 | 0.00 | +0.2356 | MACD state d+w: z +1.51; 20d volume ratio: z +1.38; RS20 vs SPY: z +0.94 | RSI headroom to 70: z -1.31 | L013-L021 |
| WELL | `UNAVAILABLE` (L046) | +0.5757 | `UNAVAILABLE` (L047) | +0.7775 | +0.2893 | 0.8 | 0.00 | +0.2315 | MA alignment d+w: z +1.20; 60d beta (defensive polarity): z +1.10; 20d volume ratio: z +1.05 | RSI headroom to 70: z -0.38 | L013-L021 |
| UNP | `UNAVAILABLE` (L046) | +0.5854 | `UNAVAILABLE` (L047) | +0.7195 | +0.2836 | 0.8 | 0.00 | +0.2268 | MA alignment d+w: z +1.20; 20d volume ratio: z +0.99; MACD state d+w: z +0.90 | RSI headroom to 70: z -0.08 | L013-L021 |
| SJM | `UNAVAILABLE` (L046) | +0.5481 | `UNAVAILABLE` (L047) | +0.7246 | +0.2731 | 0.8 | 0.00 | +0.2185 | RS60 vs SPY: z +1.55; 60d momentum: z +1.55; 60d beta (defensive polarity): z +1.25 | RSI headroom to 70: z -1.03; 20d volume ratio: z -0.47 | L013-L021 |
| SCHW | `UNAVAILABLE` (L046) | +0.5031 | `UNAVAILABLE` (L047) | +0.7723 | +0.2668 | 0.8 | 0.00 | +0.2134 | RS20 vs SPY: z +1.53; 20d momentum: z +1.53; MACD state d+w: z +1.51 | RSI headroom to 70: z -1.27; 20d volume ratio: z -1.06 | L013-L021 |
| ACGL | `UNAVAILABLE` (L046) | +0.4538 | `UNAVAILABLE` (L047) | +0.8646 | +0.2658 | 0.8 | 0.00 | +0.2127 | MACD state d+w: z +1.51; 60d beta (defensive polarity): z +1.21; MA alignment d+w: z +1.20 | RSI headroom to 70: z -1.05; 20d volume ratio: z -0.26 | L013-L021 |
| ADP | `UNAVAILABLE` (L046) | +0.9295 | `UNAVAILABLE` (L047) | +0.6891 | +0.3822 | 0.8 | 0.10 | +0.2058 | RS20 vs SPY: z +1.57; 20d momentum: z +1.57; MACD state d+w: z +1.51 | RSI headroom to 70: z -1.22 | L013-L021 |
| OMC | `UNAVAILABLE` (L046) | +0.7297 | `UNAVAILABLE` (L047) | +0.2361 | +0.2543 | 0.8 | 0.00 | +0.2035 | MACD state d+w: z +1.51; RS20 vs SPY: z +1.48; 20d momentum: z +1.48 | RSI headroom to 70: z -0.84; 30d realized vol (lower better): z -0.30; 20d volume ratio: z -0.14 | L013-L021 |
| DGX | `UNAVAILABLE` (L046) | +0.6599 | `UNAVAILABLE` (L047) | +0.7671 | +0.3130 | 0.8 | 0.05 | +0.2004 | MA alignment d+w: z +1.20; RS60 vs SPY: z +1.19; 60d momentum: z +1.19 | RSI headroom to 70: z -1.60 | L013-L021 |
| BBY | `UNAVAILABLE` (L046) | +0.7133 | `UNAVAILABLE` (L047) | +0.2222 | +0.2473 | 0.8 | 0.00 | +0.1978 | RS60 vs SPY: z +1.87; 60d momentum: z +1.87; RS20 vs SPY: z +1.33 | RSI headroom to 70: z -1.53; 20d volume ratio: z -1.27; 60d beta (defensive polarity): z -0.38 | L013-L021 |
| PFG | `UNAVAILABLE` (L046) | +0.4386 | `UNAVAILABLE` (L047) | +0.7665 | +0.2466 | 0.8 | 0.00 | +0.1972 | 20d volume ratio: z +1.38; MA alignment d+w: z +1.20; 60d max drawdown (shallower better): z +1.00 | RSI headroom to 70: z -0.41; MACD state d+w: z -0.32 | L013-L021 |
| EXR | `UNAVAILABLE` (L046) | +0.4013 | `UNAVAILABLE` (L047) | +0.8195 | +0.2433 | 0.8 | 0.00 | +0.1946 | 20d volume ratio: z +1.53; MA alignment d+w: z +1.20; 60d max drawdown (shallower better): z +1.08 | RSI headroom to 70: z -0.57; 20d momentum: z -0.04; RS20 vs SPY: z -0.04 | L013-L021 |
| TMO | `UNAVAILABLE` (L046) | +0.6015 | `UNAVAILABLE` (L047) | +0.4158 | +0.2428 | 0.8 | 0.00 | +0.1942 | RS20 vs SPY: z +1.18; 20d momentum: z +1.18; RS60 vs SPY: z +1.07 | RSI headroom to 70: z -1.31 | L013-L021 |

## Metric Availability

| Metric Group | Sourceable Count | `UNAVAILABLE` Count | DQ / Confidence Effect | Notes |
|---|---|---|---|---|
| Price / return / volatility | 514 | 0 | none | L002, L003, L013, L014 |
| Beta / tracking error / drawdown | 514 | 0 | none | L015, L016, L019 |
| Momentum / relative strength | 514 | 0 | none | L017, L018 |
| Technical indicator pack | 514 | 0 | none | L021 |
| Next earnings date | 514 | 0 | none | L022 — full universe |
| Fundamental family | 0 | 514 | DQ 0.8; blocks threshold #2 | L046 |
| Sentiment family | 0 | 514 | DQ 0.8; blocks threshold #2 | L047 |
| Options IV / short interest / bid-ask / revisions | 0 | 514 | caps confidence only | L036, L048 |

No score cites a metric absent from `01_preflight.md`, and no missing metric is described as neutral
or supportive anywhere in this package.

## Technical Indicator Summary

| Ticker | TD9 D/W/M | RSI14 D/W/M | MACD State D/W/M | MACD Hist D/W/M | MA Alignment D/W/M | 20/60 Mom D | RS20/60 vs SPY | Indicator Ledger Rows |
|---|---|---|---|---|---|---|---|---|
| TRV | SELL_SETUP_8/SELL_SETUP_9/SELL_SETUP_9 | 83.33/81.20/78.14 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | +4.0538/+9.2242/+6.6298 | BULLISH/BULLISH/BULLISH | +19.69%/+30.72% | +19.71pp/+27.37pp | L021 |
| PAYX | SELL_SETUP_2/SELL_SETUP_9/SELL_SETUP_2 | 73.00/69.69/53.88 | ABOVE_SIGNAL/ABOVE_SIGNAL/BELOW_SIGNAL | +0.4317/+3.5004/-2.1844 | BULLISH/MIXED/MIXED | +20.34%/+31.33% | +20.36pp/+27.98pp | L021 |
| INCY | SELL_SETUP_3/SELL_SETUP_9/SELL_SETUP_2 | 76.76/72.68/77.32 | BULLISH_CROSS/ABOVE_SIGNAL/ABOVE_SIGNAL | +0.3978/+2.5523/+3.4359 | BULLISH/BULLISH/BULLISH | +13.32%/+36.38% | +13.34pp/+33.03pp | L021 |
| BRO | SELL_SETUP_2/SELL_SETUP_9/SELL_SETUP_1 | 69.06/57.94/45.63 | BULLISH_CROSS/ABOVE_SIGNAL/BELOW_SIGNAL | +0.0562/+2.3064/-3.6766 | BULLISH/MIXED/MIXED | +15.15%/+22.80% | +15.17pp/+19.45pp | L021 |
| RTX | SELL_SETUP_5/SELL_SETUP_9/SELL_SETUP_1 | 77.42/69.22/76.01 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | +2.1704/+2.9208/+2.0137 | BULLISH/BULLISH/BULLISH | +16.68%/+24.66% | +16.70pp/+21.31pp | L021 |
| KO | SELL_SETUP_3/SELL_SETUP_1/SELL_SETUP_9 | 67.03/69.10/73.28 | BULLISH_CROSS/ABOVE_SIGNAL/ABOVE_SIGNAL | +0.2293/+0.3690/+1.2948 | BULLISH/BULLISH/BULLISH | +6.80%/+12.80% | +6.82pp/+9.45pp | L021 |
| MRSH | SELL_SETUP_2/SELL_SETUP_6/SELL_SETUP_1 | 70.50/63.16/51.79 | BULLISH_CROSS/ABOVE_SIGNAL/BELOW_SIGNAL | +0.6562/+3.5295/-3.3549 | BULLISH/MIXED/MIXED | +15.94%/+15.24% | +15.96pp/+11.89pp | L021 |
| IQV | SELL_SETUP_4/SELL_SETUP_6/SELL_SETUP_2 | 79.55/69.06/58.87 | BULLISH_CROSS/ABOVE_SIGNAL/BULLISH_CROSS | +1.6117/+7.2410/+3.4859 | BULLISH/MIXED/MIXED | +25.69%/+53.40% | +25.71pp/+50.05pp | L021 |
| CTAS | SELL_SETUP_3/SELL_SETUP_6/SELL_SETUP_1 | 77.29/68.82/60.73 | ABOVE_SIGNAL/ABOVE_SIGNAL/BELOW_SIGNAL | +2.1176/+5.1709/-3.6573 | BULLISH/MIXED/BULLISH | +27.10%/+23.34% | +27.12pp/+19.99pp | L021 |
| ITW | SELL_SETUP_4/SELL_SETUP_8/SELL_SETUP_1 | 72.92/68.28/63.00 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | +1.4490/+3.4637/+2.2664 | BULLISH/BULLISH/BULLISH | +11.02%/+15.09% | +11.04pp/+11.74pp | L021 |
| PM | SELL_SETUP_3/SELL_SETUP_3/SELL_SETUP_1 | 65.71/67.78/70.59 | ABOVE_SIGNAL/ABOVE_SIGNAL/BULLISH_CROSS | +1.2023/+1.9719/+1.0388 | BULLISH/BULLISH/BULLISH | +9.46%/+22.27% | +9.48pp/+18.92pp | L021 |
| VLTO | SELL_SETUP_2/SELL_SETUP_6/SELL_SETUP_1 | 70.19/60.38/54.12 | BULLISH_CROSS/ABOVE_SIGNAL/BELOW_SIGNAL | +0.2104/+1.6577/-1.5455 | BULLISH/MIXED/UNAVAILABLE | +11.66%/+11.81% | +11.68pp/+8.46pp | L021 |
| WELL | BUY_SETUP_1/SELL_SETUP_6/SELL_SETUP_4 | 60.30/66.09/76.35 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | +0.0922/+2.7854/+3.7204 | BULLISH/BULLISH/BULLISH | +6.96%/+12.45% | +6.97pp/+9.10pp | L021 |
| UNP | SELL_SETUP_4/SELL_SETUP_6/SELL_SETUP_9 | 57.11/64.40/66.42 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | +0.1513/+2.9866/+5.7259 | BULLISH/BULLISH/BULLISH | +7.98%/+9.83% | +7.99pp/+6.48pp | L021 |
| SJM | SELL_SETUP_9/SELL_SETUP_3/SELL_SETUP_1 | 67.23/67.19/58.67 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | +0.8385/+1.9073/+2.0818 | BULLISH/BULLISH/MIXED | +6.17%/+26.91% | +6.19pp/+23.55pp | L021 |
| SCHW | SELL_SETUP_2/SELL_SETUP_9/SELL_SETUP_1 | 69.81/66.94/65.57 | BULLISH_CROSS/ABOVE_SIGNAL/BELOW_SIGNAL | +0.0251/+1.7132/-0.1553 | BULLISH/MIXED/BULLISH | +17.03%/+16.05% | +17.05pp/+12.70pp | L021 |
| ACGL | SELL_SETUP_3/SELL_SETUP_6/SELL_SETUP_1 | 67.47/66.61/62.41 | BULLISH_CROSS/ABOVE_SIGNAL/BELOW_SIGNAL | +0.1989/+1.2301/-0.1472 | BULLISH/BULLISH/BULLISH | +8.59%/+12.72% | +8.61pp/+9.37pp | L021 |
| ADP | SELL_SETUP_2/SELL_SETUP_6/SELL_SETUP_2 | 69.25/64.84/54.59 | BULLISH_CROSS/ABOVE_SIGNAL/BELOW_SIGNAL | +0.4518/+7.0734/-5.3577 | BULLISH/MIXED/MIXED | +17.42%/+25.59% | +17.44pp/+22.24pp | L021 |
| OMC | SELL_SETUP_2/SELL_SETUP_6/SELL_SETUP_1 | 65.22/61.92/56.84 | BULLISH_CROSS/ABOVE_SIGNAL/BULLISH_CROSS | +0.1469/+1.1175/+0.3955 | BULLISH/BULLISH/MIXED | +16.62%/+13.58% | +16.64pp/+10.23pp | L021 |
| DGX | SELL_SETUP_9/SELL_SETUP_6/SELL_SETUP_6 | 77.23/71.19/70.36 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | +2.5642/+3.3361/+3.4917 | BULLISH/BULLISH/BULLISH | +11.41%/+21.99% | +11.43pp/+18.64pp | L021 |
| BBY | SELL_SETUP_3/SELL_SETUP_9/SELL_SETUP_3 | 72.57/68.98/61.46 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | +0.1409/+2.5641/+1.7039 | BULLISH/BULLISH/BULLISH | +15.24%/+49.88% | +15.26pp/+46.53pp | L021 |
| PFG | SELL_SETUP_2/SELL_SETUP_9/SELL_SETUP_9 | 60.61/69.13/74.81 | BELOW_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | -0.2738/+0.5624/+2.8588 | BULLISH/BULLISH/BULLISH | +5.14%/+13.96% | +5.16pp/+10.61pp | L021 |
| EXR | SELL_SETUP_3/SELL_SETUP_1/SELL_SETUP_1 | 62.32/59.97/56.71 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | +0.3473/+0.6970/+1.5417 | BULLISH/BULLISH/BULLISH | +2.66%/+7.35% | +2.68pp/+4.00pp | L021 |
| TMO | SELL_SETUP_4/SELL_SETUP_9/SELL_SETUP_1 | 70.22/64.16/56.62 | ABOVE_SIGNAL/ABOVE_SIGNAL/BULLISH_CROSS | +3.2209/+13.0079/+3.7353 | BULLISH/MIXED/MIXED | +13.82%/+20.47% | +13.84pp/+17.11pp | L021 |

## Evidence Thresholds — why zero names are investable

| # | Threshold | Result |
|---|---|---|
| 1 | Adjusted-score pctl >= 80 | **PASS** — 103 names |
| 2 | >= 3 of 4 families non-negative | **FAIL** universe-wide — only 2 families sourceable (L046, L047) |
| 3 | No family > 50% of conviction | **FAIL** universe-wide — Technical is 0.30 of the 0.45 available weight, i.e. 66.7% |
| 4 | Data completeness >= 85% | **FAIL** universe-wide — DQ 0.8 (L049) |
| 5 | No hard stop | PASS |

Zero names clear all five. Under `rules.md § Downgrade to NO_TRADE` #1 (fewer than 5 investable
names), the recommendation to the portfolio agent is **`NO_TRADE`**. All 24 names above are
published as a **monitoring sleeve** with full `mu`/`sigma`/CI so every one is settleable on 2026-08-26 —
`REVIEW_ONLY`/`NO_TRADE` status governs execution, not evaluation.

## Sector Distribution of the Published Set

| Sector | Names | Share |
|---|---|---|
| Industrials | 8 | 33.3% |
| Finance | 6 | 25.0% |
| Health Care | 4 | 16.7% |
| Consumer Staples | 2 | 8.3% |
| Real Estate | 2 | 8.3% |
| Consumer Discretionary | 2 | 8.3% |

Mean published beta -0.3288; 19 of 24 carry negative beta — the
defensive-polarity signature.

## Hallucination Prevention Checklist

- [x] Every numeric `entry_price` has `price_date` + `price_tag` — all 24 at 2026-07-28, `HISTORICAL`
- [x] Every numeric metric cites Source Ledger rows
- [x] Every `Adj Score` has a full score trace with family z-scores, DQ, penalties, drivers
- [x] Missing metrics are `UNAVAILABLE` (L046, L047), never neutral or supportive
- [x] Kelly and technical indicator fields follow `rules.md`
- [x] `target_price = entry_price × (1 + mu)` — recomputed and asserted in the verification pass
- [x] Every sigma states its source (`REALIZED_VOL_30D`, L013)
- [x] No published name has `price_tag = UNAVAILABLE`
- [x] `mu`/`sigma` derive from the calibration table and sigma chain, not assertion
- [x] No live-sounding wording without ledger support — the basis is stated as the 2026-07-28 close throughout
