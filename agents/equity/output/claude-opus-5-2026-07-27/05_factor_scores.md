# 05 Factor Scores — 2026-07-27

Primary home for `Adj Score` explainability. Percentiles are `INDEX_UNION_PCTL (n=514)`.

## Family Construction

Each metric is winsorized at the 5th/95th percentile across the 514-name universe, then z-scored; a
family is the equal-weighted mean of its available metric z-scores (≥2 required, else `UNAVAILABLE`).

| Family | Weight | Metrics (polarity) | n signals |
|---|---|---|---|
| Fundamental | 0.30 | — | **`UNAVAILABLE` (L046)** |
| Technical / Price | 0.30 | 20d momentum (+), 60d momentum (+), RS20 vs SPY (+), RS60 vs SPY (+), MA alignment daily+weekly (+), MACD state daily+weekly (+), 20d volume ratio (+), RSI headroom `70 − RSI14_d` (+) | 8 |
| Sentiment / Positioning | 0.25 | — | **`UNAVAILABLE` (L047)** |
| Macro / Regime | 0.15 | 60d beta (**−**), 30d realized vol (**−**), 60d max drawdown (+, shallower is better) | 3 |

**Encodings.** MA alignment `BULLISH/MIXED/BEARISH` → `+1 / 0 / −1`. MACD
`BULLISH_CROSS / ABOVE_SIGNAL / ON_SIGNAL / BELOW_SIGNAL / BEARISH_CROSS` → `+1 / +0.5 / 0 / −0.5 / −1`.
RSI enters as headroom-to-overbought so polarity is uniformly "higher is better" and extended names
are not rewarded.

**Return basis.** Every momentum, relative-strength, volatility, beta, tracking-error and drawdown
input is computed from **adjusted** closes (L003). Entry, target and CI prices use the unadjusted
2026-07-24 close (L002).

**Disclosed judgment — defensive Macro polarity (`INFERRED`, L053).** Lower beta, lower realized vol
and shallower drawdown score *better* this run. This is a regime-conditional reading of the evidence
in `03` (index flat and below both MAs, SOXX -19.54% from its
60-day high, 41.25% of the universe at negative beta,
TLT -4.45%). It is **not** a permanent rule and **not** a
family-weight change — altering weights requires the evolution policy and is gated off at
`eff_n = 1`. It is flagged here because it materially shapes the leaderboard: it is the
single largest reason insurers, rails, defense, utilities and lab-services names fill the top of the
book, and it is why 19 of the 24 published names
carry negative beta.

**Data-quality multiplier: 0.8** for every name — "notable coverage gaps", being two of
four families `UNAVAILABLE` plus the entire Enhancing block (L035, L048). Since
0.8 < 0.85, `rules.md § Evidence Thresholds` #4 independently forbids marking any name
investable.

**Calibration feedback applied** (from `02 § 0`): weighted-mean rank IC
-0.1843 over 231
settled pairs (≥ 20) → **confidence capped at `MEDIUM` universe-wide**; no name carries `HIGH`
anywhere in this package. CI coverage 74.03% is inside the healthy 55–85% band,
so the sigma-widening rule does **not** fire and sigma stays `REALIZED_VOL_30D`. **No positive
per-name `mu` adjustment was made anywhere** — every `mu` is the unmodified mu-Calibration-Table value
for the name's percentile band (L027).

## Penalties Applied

| Penalty | Rule | Value | Names (universe) | In published set |
|---|---|---|---|---|
| Earnings inside 14 calendar days, buffered by the estimate band | `rules.md § Risk Controls` | **−0.10**, confidence capped `LOW` | 40 | 7 |
| 30d realized vol > 2× universe median (0.0961 → threshold 0.1922) | `rules.md § Risk Controls` | −0.05 | 31 | 0 |
| TD-9 daily sell-setup 9 **and** RSI(14) daily ≥ 70 (exhaustion confirmed by price action) | `rules.md § TD-9 Definition` | −0.05 | 4 | 1 |
| Unstable earnings profile | `rules.md § Risk Controls` | **not applied** | — | Requires fundamentals — `UNAVAILABLE` (L046). Disclosed as an *unapplied* penalty, not as absent risk |
| Size > 2% of 20-day ADV | `rules.md § Risk Controls` | **not binding** | — | No position is sized; `NO_TRADE` |

75 of 514 names carry at least one penalty.

### Earnings-date grounding

57 names were grounded across **three bounded shortlist passes plus two retry rounds** (L022–L026):
CONFIRMED 34, ESTIMATED_CADENCE 16, ESTIMATED_PRINT_WEEK 7.
The sequence was: top-40 pre-earnings ranks (40 names) → post-penalty top-20 entrants (4) →
second-round top-20 entrants (13), with a retry round after each pass that hit a transport failure
(6 names across 2 rounds), iterated **until the post-penalty top-20 was fully earnings-grounded**. Names that entered the top-30 only after convergence
(AON, ESS, ITW, WM, JNJ, DUK, CTVA, AMP) are **excluded from publication rather than scored
penalty-free**.

`ESTIMATED_PRINT_WEEK` names (CB, EQR, HIG, MTB, OKE, PFG, WRB)
are the conservative branch: vendor-empty **and** no ≥3.5% one-day move in the last 12 sessions, so
they are treated as printing this week and penalised (L026). This run required the price move and did
not accept volume alone — the tightening the 2026-07-26 package identified after EQR/PKG tripped a
volume-only signature on ~0.01% price moves.

**Divergence from the concurrent `gpt-5-2026-07-27` Track B, disclosed.** That run accepted a slightly
looser refinement effective 2026-07-28: `move ≥3.5%` **or** (`volume ≥1.8×` **and** `move ≥1.5%`).
Under that rule, CB, MTB and PFG would resolve to `ESTIMATED_CADENCE` instead of `ESTIMATED_PRINT_WEEK`.
None of the three is in this run's published set (ranks 132, 182,
179), and the one published `ESTIMATED_PRINT_WEEK` name — HIG, 1-day move 2.64% on
0.94× volume — resolves identically under both rules. **The difference therefore changes nothing in
this package.** This run predates that change's effective date, so the stricter branch was applied.

## Ranked Candidate Table — Published Set (24 names)

Field derivations per `rules.md § Price and Target Citation Standard`. `mu` from the mu Calibration
Table band for each name's percentile (L027); `sigma` = `REALIZED_VOL_30D` (L013);
`target_price = entry × (1 + mu)` (L028); CI bounds = `entry × (1 + mu ± 1.04σ)` (L029). Target date
**2026-08-24** (`run_date + 28d`). **Every name below is monitoring sleeve — zero investable.**

| Ticker | Company | Entry | Date | Tag | Adj Score | Score Trace | Pctl | Beta | 30d RVol | Sharpe | Sortino | IR | Kelly .25 | VaR95 | CVaR95 | MaxDD60 | TD9 D/W/M | RSI14 D/W/M | MACD D/W/M | Days→Earn | mu | sigma | SigSrc | Target | Target Date | CI Lo | CI Hi | Ledger | Metric Ledger | Conf | Primary Thesis | Key Risk |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| TRV | The Travelers Companies In | 387.26 | 2026-07-24 | HISTORICAL | +0.3705 | (0.30×0.00<sub>UNAVL</sub> + 0.30×+1.1240 + 0.25×0.00<sub>UNAVL</sub> + 0.15×+0.8397) × 0.8 − 0.00 = +0.3705 | 100.00 | -0.701 | 9.33% | 0.6093 | 1.7066 | 0.7982 | 0.0500 | -9.39% | -13.21% | -5.96% | SELL_SETUP_6/SELL_SETUP_8/SELL_SETUP_9 | 80.9/79.7/77.2 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | ~81d (ESTIMATED_CADENCE ±5d) | +6.0% | 9.33% | REALIZED_VOL_30D | 410.50 | 2026-08-24 | 372.93 | 448.06 | L002,L003,L012 | L013-L021,L027-L039 | MEDIUM | Finance / Property-Casualty Insurers; RS60 +21.4pp, mom60 +25.4% | RSI14_d 80.9 overbought; beta -0.701 reverses in a risk-on turn |
| RTX | RTX Corporation Common Sto | 212.79 | 2026-07-24 | HISTORICAL | +0.3089 | (0.30×0.00<sub>UNAVL</sub> + 0.30×+0.9877 + 0.25×0.00<sub>UNAVL</sub> + 0.15×+0.5984) × 0.8 − 0.00 = +0.3089 | 99.81 | -0.061 | 9.75% | 0.5826 | 1.0595 | 0.6933 | 0.0500 | -10.09% | -14.09% | -5.58% | SELL_SETUP_3/SELL_SETUP_9/SELL_SETUP_1 | 74.0/66.8/74.9 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | ~87d (ESTIMATED_CADENCE ±5d) | +6.0% | 9.75% | REALIZED_VOL_30D | 225.56 | 2026-08-24 | 203.97 | 247.14 | L002,L003,L012 | L013-L021,L027-L039 | MEDIUM | Industrials / Aerospace; RS60 +17.5pp, mom60 +21.6% | RSI14_d 74.0 overbought; beta -0.061 reverses in a risk-on turn |
| PAYX | Paychex Inc. Common Stock | 113.55 | 2026-07-24 | HISTORICAL | +0.3072 | (0.30×0.00<sub>UNAVL</sub> + 0.30×+0.8884 + 0.25×0.00<sub>UNAVL</sub> + 0.15×+0.7832) × 0.8 − 0.00 = +0.3072 | 99.61 | -0.614 | 9.45% | 0.6016 | 1.3668 | 0.6723 | 0.0500 | -9.59% | -13.46% | -6.35% | BUY_SETUP_3/SELL_SETUP_9/SELL_SETUP_2 | 64.7/64.5/50.2 | ABOVE_SIGNAL/ABOVE_SIGNAL/BELOW_SIGNAL | ~80d (ESTIMATED_CADENCE ±5d) | +6.0% | 9.45% | REALIZED_VOL_30D | 120.36 | 2026-08-24 | 109.21 | 131.52 | L002,L003,L012 | L013-L021,L027-L039 | MEDIUM | Industrials / Diversified Commercial Service; RS60 +22.3pp, mom60 +26.4% | beta -0.614 reverses in a risk-on turn |
| DGX | Quest Diagnostics Incorpor | 227.86 | 2026-07-24 | HISTORICAL | +0.3058 | (0.30×0.00<sub>UNAVL</sub> + 0.30×+0.8911 + 0.25×0.00<sub>UNAVL</sub> + 0.15×+0.7664) × 0.8 − 0.00 = +0.3058 | 99.42 | -0.576 | 9.55% | 0.5947 | 2.0143 | 0.7636 | 0.0500 | -9.76% | -13.68% | -6.22% | SELL_SETUP_7/SELL_SETUP_5/SELL_SETUP_6 | 72.7/68.3/68.7 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | ~87d (ESTIMATED_CADENCE ±5d) | +6.0% | 9.55% | REALIZED_VOL_30D | 241.53 | 2026-08-24 | 218.89 | 264.17 | L002,L003,L012 | L013-L021,L027-L039 | MEDIUM | Health Care / Medical Specialities; RS60 +13.2pp, mom60 +17.3% | RSI14_d 72.7 overbought; beta -0.576 reverses in a risk-on turn |
| UNP | Union Pacific Corporation  | 307.32 | 2026-07-24 | HISTORICAL | +0.2992 | (0.30×0.00<sub>UNAVL</sub> + 0.30×+0.8658 + 0.25×0.00<sub>UNAVL</sub> + 0.15×+0.7620) × 0.8 − 0.00 = +0.2992 | 99.22 | -0.164 | 7.32% | 0.7767 | 1.1652 | 0.8162 | 0.0500 | -6.07% | -9.07% | -7.58% | SELL_SETUP_2/SELL_SETUP_5/SELL_SETUP_9 | 73.0/73.3/68.6 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | ~87d (ESTIMATED_CADENCE ±5d) | +6.0% | 7.32% | REALIZED_VOL_30D | 325.76 | 2026-08-24 | 302.38 | 349.14 | L002,L003,L012 | L013-L021,L027-L039 | MEDIUM | Industrials / Railroads; RS60 +11.3pp, mom60 +15.4% | RSI14_d 73.0 overbought; beta -0.164 reverses in a risk-on turn |
| PCG | Pacific Gas & Electric Co. | 17.85 | 2026-07-24 | HISTORICAL | +0.2807 | (0.30×0.00<sub>UNAVL</sub> + 0.30×+0.7255 + 0.25×0.00<sub>UNAVL</sub> + 0.15×+0.8880) × 0.8 − 0.00 = +0.2807 | 99.03 | -0.260 | 7.12% | 0.7979 | 1.3562 | 0.8028 | 0.0500 | -5.75% | -8.67% | -5.71% | SELL_SETUP_3/SELL_SETUP_3/SELL_SETUP_1 | 60.1/58.5/55.6 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | ~86d (ESTIMATED_CADENCE ±5d) | +6.0% | 7.12% | REALIZED_VOL_30D | 18.92 | 2026-08-24 | 17.60 | 20.24 | L002,L003,L012 | L013-L021,L027-L039 | MEDIUM | Utilities / Power Generation; RS60 +6.0pp, mom60 +10.1% | beta -0.260 reverses in a risk-on turn |
| CSX | CSX Corporation Common Sto | 53.23 | 2026-07-24 | HISTORICAL | +0.2777 | (0.30×0.00<sub>UNAVL</sub> + 0.30×+0.7750 + 0.25×0.00<sub>UNAVL</sub> + 0.15×+0.7638) × 0.8 − 0.00 = +0.2777 | 98.83 | +0.113 | 7.22% | 0.7871 | 1.6322 | 0.8919 | 0.0500 | -5.91% | -8.87% | -4.20% | SELL_SETUP_2/SELL_SETUP_9/SELL_SETUP_9 | 76.1/78.9/76.5 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | ~87d (ESTIMATED_CADENCE ±5d) | +6.0% | 7.22% | REALIZED_VOL_30D | 56.42 | 2026-08-24 | 52.43 | 60.42 | L002,L003,L012 | L013-L021,L027-L039 | MEDIUM | Industrials / Railroads; RS60 +14.0pp, mom60 +18.1% | RSI14_d 76.1 overbought |
| TMO | Thermo Fisher Scientific I | 568.26 | 2026-07-24 | HISTORICAL | +0.2471 | (0.30×0.00<sub>UNAVL</sub> + 0.30×+0.8369 + 0.25×0.00<sub>UNAVL</sub> + 0.15×+0.3852) × 0.8 − 0.00 = +0.2471 | 98.64 | +0.098 | 10.22% | 0.5560 | 1.9289 | 0.5871 | 0.0500 | -10.86% | -15.05% | -8.48% | SELL_SETUP_2/SELL_SETUP_9/SELL_SETUP_1 | 70.8/62.9/55.8 | ABOVE_SIGNAL/ABOVE_SIGNAL/BULLISH_CROSS | ~87d (ESTIMATED_CADENCE ±5d) | +6.0% | 10.22% | REALIZED_VOL_30D | 602.36 | 2026-08-24 | 541.95 | 662.76 | L002,L003,L012 | L013-L021,L027-L039 | MEDIUM | Industrials / Industrial Machinery/Component; RS60 +16.9pp, mom60 +21.0% | RSI14_d 70.8 overbought |
| NSC | Norfolk Southern Corporati | 350.66 | 2026-07-24 | HISTORICAL | +0.2423 | (0.30×0.00<sub>UNAVL</sub> + 0.30×+0.6341 + 0.25×0.00<sub>UNAVL</sub> + 0.15×+0.7511) × 0.8 − 0.00 = +0.2423 | 98.44 | -0.100 | 7.05% | 0.8056 | 1.3174 | 0.8521 | 0.0500 | -5.64% | -8.53% | -7.86% | SELL_SETUP_2/SELL_SETUP_5/SELL_SETUP_4 | 73.2/71.0/67.4 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | ~87d (ESTIMATED_CADENCE ±5d) | +6.0% | 7.05% | REALIZED_VOL_30D | 371.70 | 2026-08-24 | 345.98 | 397.42 | L002,L003,L012 | L013-L021,L027-L039 | MEDIUM | Industrials / Railroads; RS60 +7.1pp, mom60 +11.2% | RSI14_d 73.2 overbought; beta -0.100 reverses in a risk-on turn |
| WELL | Welltower Inc. Common Stoc | 252.07 | 2026-07-24 | HISTORICAL | +0.2406 | (0.30×0.00<sub>UNAVL</sub> + 0.30×+0.8140 + 0.25×0.00<sub>UNAVL</sub> + 0.15×+0.7939) × 0.8 − 0.05 = +0.2406 | 98.25 | -0.573 | 6.82% | 0.8327 | 1.3611 | 0.8016 | 0.0500 | -5.26% | -8.06% | -11.26% | SELL_SETUP_9/SELL_SETUP_5/SELL_SETUP_4 | 74.1/72.6/77.6 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | ~80d (ESTIMATED_CADENCE ±5d) | +6.0% | 6.82% | REALIZED_VOL_30D | 267.19 | 2026-08-24 | 249.30 | 285.08 | L002,L003,L012 | L013-L021,L027-L039 | MEDIUM | Real Estate / Real Estate Investment Trusts; RS60 +14.0pp, mom60 +18.1% | RSI14_d 74.1 overbought; beta -0.573 reverses in a risk-on turn |
| GD | General Dynamics Corporati | 386.75 | 2026-07-24 | HISTORICAL | +0.2366 | (0.30×0.00<sub>UNAVL</sub> + 0.30×+1.0243 + 0.25×0.00<sub>UNAVL</sub> + 0.15×+0.7568) × 0.8 − 0.10 = +0.2366 | 98.05 | -0.019 | 7.69% | 0.7388 | 1.2455 | 0.7445 | 0.0500 | -6.69% | -9.84% | -5.70% | SELL_SETUP_5/SELL_SETUP_4/SELL_SETUP_1 | 70.3/65.0/78.3 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | 2d (2026-07-29, CONFIRMED) | +6.0% | 7.69% | REALIZED_VOL_30D | 409.95 | 2026-08-24 | 379.02 | 440.89 | L002,L003,L012 | L013-L021,L027-L039 | LOW | Industrials / Marine Transportation; RS60 +19.8pp, mom60 +23.8% | earnings inside horizon; RSI14_d 70.3 overbought; beta -0.019 reverses in a risk-on turn |
| PM | Philip Morris Internationa | 193.0 | 2026-07-24 | HISTORICAL | +0.2286 | (0.30×0.00<sub>UNAVL</sub> + 0.30×+0.6486 + 0.25×0.00<sub>UNAVL</sub> + 0.15×+0.6082) × 0.8 − 0.00 = +0.2286 | 97.86 | -0.540 | 9.45% | 0.6014 | 1.2833 | 0.6796 | 0.0500 | -9.59% | -13.46% | -10.01% | SELL_SETUP_1/SELL_SETUP_2/SELL_SETUP_1 | 59.7/64.1/68.9 | ABOVE_SIGNAL/ABOVE_SIGNAL/BULLISH_CROSS | ~80d (ESTIMATED_CADENCE ±5d) | +6.0% | 9.45% | REALIZED_VOL_30D | 204.58 | 2026-08-24 | 185.61 | 223.55 | L002,L003,L012 | L013-L021,L027-L039 | MEDIUM | Health Care /  Medicinal Chemicals and Botan; RS60 +13.2pp, mom60 +17.3% | beta -0.540 reverses in a risk-on turn |
| MPC | Marathon Petroleum Corpora | 309.24 | 2026-07-24 | HISTORICAL | +0.2267 | (0.30×0.00<sub>UNAVL</sub> + 0.30×+1.0669 + 0.25×0.00<sub>UNAVL</sub> + 0.15×+0.5890) × 0.8 − 0.10 = +0.2267 | 97.66 | -0.439 | 9.70% | 0.5858 | 1.0384 | 0.5927 | 0.0500 | -10.00% | -13.98% | -9.09% | BUY_SETUP_2/SELL_SETUP_5/SELL_SETUP_6 | 68.2/73.2/80.9 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | 8d (2026-08-04, CONFIRMED) | +6.0% | 9.70% | REALIZED_VOL_30D | 327.79 | 2026-08-24 | 296.60 | 358.99 | L002,L003,L012 | L013-L021,L027-L039 | LOW | Energy / Integrated oil Companies; RS60 +29.4pp, mom60 +33.5% | earnings inside horizon; beta -0.439 reverses in a risk-on turn |
| CTAS | Cintas Corporation Common  | 205.91 | 2026-07-24 | HISTORICAL | +0.2248 | (0.30×0.00<sub>UNAVL</sub> + 0.30×+0.6558 + 0.25×0.00<sub>UNAVL</sub> + 0.15×+0.5615) × 0.8 − 0.00 = +0.2248 | 97.47 | -0.290 | 10.33% | 0.5500 | 1.2145 | 0.6662 | 0.0500 | -11.05% | -15.28% | -7.19% | SELL_SETUP_1/SELL_SETUP_5/SELL_SETUP_1 | 72.1/65.0/58.4 | ABOVE_SIGNAL/ABOVE_SIGNAL/BELOW_SIGNAL | ~80d (ESTIMATED_CADENCE ±5d) | +6.0% | 10.33% | REALIZED_VOL_30D | 218.26 | 2026-08-24 | 196.14 | 240.39 | L002,L003,L012 | L013-L021,L027-L039 | MEDIUM | Industrials / Garments and Clothing; RS60 +14.4pp, mom60 +18.5% | RSI14_d 72.1 overbought; beta -0.290 reverses in a risk-on turn |
| SJM | The J.M. Smucker Company C | 118.32 | 2026-07-24 | HISTORICAL | +0.2245 | (0.30×0.00<sub>UNAVL</sub> + 0.30×+0.5629 + 0.25×0.00<sub>UNAVL</sub> + 0.15×+0.7449) × 0.8 − 0.00 = +0.2245 | 97.27 | -0.756 | 9.47% | 0.6000 | 1.0687 | 0.6068 | 0.0500 | -9.63% | -13.51% | -8.42% | SELL_SETUP_7/SELL_SETUP_2/SELL_SETUP_1 | 61.2/63.6/56.6 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | 30d (2026-08-26, CONFIRMED) | +6.0% | 9.47% | REALIZED_VOL_30D | 125.42 | 2026-08-24 | 113.76 | 137.07 | L002,L003,L012 | L013-L021,L027-L039 | MEDIUM | Consumer Staples / Packaged Foods; RS60 +17.9pp, mom60 +22.0% | beta -0.756 reverses in a risk-on turn |
| LMT | Lockheed Martin Corporatio | 582.6 | 2026-07-24 | HISTORICAL | +0.2186 | (0.30×0.00<sub>UNAVL</sub> + 0.30×+0.7763 + 0.25×0.00<sub>UNAVL</sub> + 0.15×+0.2687) × 0.8 − 0.00 = +0.2186 | 97.08 | -0.459 | 12.88% | 0.4411 | 1.1430 | 0.6207 | 0.0500 | -15.26% | -20.54% | -10.40% | SELL_SETUP_3/SELL_SETUP_1/BUY_SETUP_3 | 71.7/57.5/58.9 | ABOVE_SIGNAL/BELOW_SIGNAL/ABOVE_SIGNAL | ~87d (ESTIMATED_CADENCE ±5d) | +6.0% | 12.88% | REALIZED_VOL_30D | 617.56 | 2026-08-24 | 539.50 | 695.61 | L002,L003,L012 | L013-L021,L027-L039 | MEDIUM | Industrials / Military/Government/Technical; RS60 +10.4pp, mom60 +14.5% | RSI14_d 71.7 overbought; beta -0.459 reverses in a risk-on turn |
| WAB | Westinghouse Air Brake Tec | 302.5 | 2026-07-24 | HISTORICAL | +0.2103 | (0.30×0.00<sub>UNAVL</sub> + 0.30×+0.8479 + 0.25×0.00<sub>UNAVL</sub> + 0.15×+0.0568) × 0.8 − 0.00 = +0.2103 | 96.88 | +0.806 | 11.10% | 0.5117 | 0.9780 | 0.6561 | 0.0500 | -12.32% | -16.88% | -8.71% | SELL_SETUP_4/SELL_SETUP_1/SELL_SETUP_9 | 75.1/74.3/77.6 | ABOVE_SIGNAL/BULLISH_CROSS/ABOVE_SIGNAL | ~86d (ESTIMATED_CADENCE ±5d) | +6.0% | 11.10% | REALIZED_VOL_30D | 320.65 | 2026-08-24 | 285.71 | 355.59 | L002,L003,L012 | L013-L021,L027-L039 | MEDIUM | Industrials / Railroads; RS60 +11.0pp, mom60 +15.1% | RSI14_d 75.1 overbought |
| PKG | Packaging Corporation of A | 254.39 | 2026-07-24 | HISTORICAL | +0.2040 | (0.30×0.00<sub>UNAVL</sub> + 0.30×+0.8097 + 0.25×0.00<sub>UNAVL</sub> + 0.15×+0.0809) × 0.8 − 0.00 = +0.2040 | 96.69 | +0.811 | 9.99% | 0.5690 | 1.2579 | 0.6476 | 0.0500 | -10.48% | -14.57% | -10.43% | SELL_SETUP_2/SELL_SETUP_7/SELL_SETUP_2 | 72.2/67.1/68.1 | BULLISH_CROSS/ABOVE_SIGNAL/ABOVE_SIGNAL | ~88d (ESTIMATED_CADENCE ±5d) | +6.0% | 9.99% | REALIZED_VOL_30D | 269.65 | 2026-08-24 | 243.23 | 296.07 | L002,L003,L012 | L013-L021,L027-L039 | MEDIUM | Consumer Discretionary / Containers/Packaging; RS60 +10.9pp, mom60 +15.0% | RSI14_d 72.2 overbought |
| MET | MetLife Inc. Common Stock | 94.83 | 2026-07-24 | HISTORICAL | +0.1955 | (0.30×0.00<sub>UNAVL</sub> + 0.30×+0.8304 + 0.25×0.00<sub>UNAVL</sub> + 0.15×+0.8014) × 0.8 − 0.10 = +0.1955 | 96.49 | -0.006 | 7.26% | 0.7832 | 1.1803 | 0.9085 | 0.0500 | -5.97% | -8.95% | -4.77% | SELL_SETUP_1/SELL_SETUP_9/SELL_SETUP_4 | 67.2/71.0/67.7 | BELOW_SIGNAL/ABOVE_SIGNAL/BULLISH_CROSS | 9d (2026-08-05, CONFIRMED) | +6.0% | 7.26% | REALIZED_VOL_30D | 100.52 | 2026-08-24 | 93.36 | 107.68 | L002,L003,L012 | L013-L021,L027-L039 | LOW | Finance / Life Insurance; RS60 +18.0pp, mom60 +22.1% | earnings inside horizon; beta -0.006 reverses in a risk-on turn |
| BNY | The Bank of New York Mello | 158.91 | 2026-07-24 | HISTORICAL | +0.1952 | (0.30×0.00<sub>UNAVL</sub> + 0.30×+0.5162 + 0.25×0.00<sub>UNAVL</sub> + 0.15×+0.5941) × 0.8 − 0.00 = +0.1952 | 96.30 | +0.566 | 7.38% | 0.7695 | 1.4931 | 0.9703 | 0.0500 | -6.19% | -9.21% | -3.34% | SELL_SETUP_2/SELL_SETUP_9/SELL_SETUP_9 | 63.5/84.1/90.9 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | ~79d (ESTIMATED_CADENCE ±5d) | +6.0% | 7.38% | REALIZED_VOL_30D | 168.44 | 2026-08-24 | 156.24 | 180.65 | L002,L003,L012 | L013-L021,L027-L039 | MEDIUM | Finance / Major Banks; RS60 +14.9pp, mom60 +19.0% | 2 of 4 families UNAVAILABLE |
| VLO | Valero Energy Corporation  | 302.5 | 2026-07-24 | HISTORICAL | +0.1859 | (0.30×0.00<sub>UNAVL</sub> + 0.30×+0.9460 + 0.25×0.00<sub>UNAVL</sub> + 0.15×+0.4908) × 0.8 − 0.10 = +0.1859 | 95.32 | -0.737 | 11.78% | 0.4824 | 1.1178 | 0.5395 | 0.0500 | -13.44% | -18.27% | -9.62% | BUY_SETUP_2/SELL_SETUP_5/SELL_SETUP_9 | 63.1/71.6/82.3 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | 3d (2026-07-30, CONFIRMED) | +6.0% | 11.78% | REALIZED_VOL_30D | 320.65 | 2026-08-24 | 283.59 | 357.71 | L002,L003,L012 | L013-L021,L027-L039 | LOW | Energy / Integrated oil Companies; RS60 +22.4pp, mom60 +26.5% | earnings inside horizon; beta -0.737 reverses in a risk-on turn |
| HIG | The Hartford Insurance Gro | 140.53 | 2026-07-24 | HISTORICAL | +0.1830 | (0.30×0.00<sub>UNAVL</sub> + 0.30×+0.6809 + 0.25×0.00<sub>UNAVL</sub> + 0.15×+0.9967) × 0.8 − 0.10 = +0.1830 | 94.93 | -0.575 | 6.26% | 0.7479 | 1.4484 | 0.8304 | 0.0500 | -5.33% | -7.90% | -7.51% | SELL_SETUP_5/SELL_SETUP_5/SELL_SETUP_1 | 58.2/58.4/64.0 | ABOVE_SIGNAL/ABOVE_SIGNAL/BELOW_SIGNAL | print wk (ESTIMATED_PRINT_WEEK ±5d) | +5.0% | 6.26% | REALIZED_VOL_30D | 147.56 | 2026-08-24 | 138.41 | 156.71 | L002,L003,L012 | L013-L021,L027-L039 | LOW | Finance / Property-Casualty Insurers; RS60 -2.4pp, mom60 +1.7% | earnings inside horizon; beta -0.575 reverses in a risk-on turn |
| PSX | Phillips 66 Common Stock | 206.77 | 2026-07-24 | HISTORICAL | +0.1720 | (0.30×0.00<sub>UNAVL</sub> + 0.30×+0.8405 + 0.25×0.00<sub>UNAVL</sub> + 0.15×+0.5857) × 0.8 − 0.10 = +0.1720 | 92.59 | -0.601 | 9.93% | 0.4714 | 0.8677 | 0.5240 | 0.0500 | -11.39% | -15.46% | -10.04% | BUY_SETUP_1/SELL_SETUP_3/SELL_SETUP_7 | 67.3/69.8/74.5 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | 9d (2026-08-05, CONFIRMED) | +5.0% | 9.93% | REALIZED_VOL_30D | 217.11 | 2026-08-24 | 195.75 | 238.47 | L002,L003,L012 | L013-L021,L027-L039 | LOW | Energy / Integrated oil Companies; RS60 +22.0pp, mom60 +26.1% | earnings inside horizon; beta -0.601 reverses in a risk-on turn |
| LH | Labcorp Holdings Inc. Comm | 296.77 | 2026-07-24 | HISTORICAL | +0.1700 | (0.30×0.00<sub>UNAVL</sub> + 0.30×+0.6882 + 0.25×0.00<sub>UNAVL</sub> + 0.15×+0.8733) × 0.8 − 0.10 = +0.1700 | 91.81 | -0.246 | 7.01% | 0.6683 | 1.5192 | 0.7956 | 0.0500 | -6.56% | -9.43% | -6.20% | SELL_SETUP_2/SELL_SETUP_5/SELL_SETUP_1 | 71.2/63.4/62.0 | ABOVE_SIGNAL/ABOVE_SIGNAL/BULLISH_CROSS | 3d (2026-07-30, CONFIRMED) | +5.0% | 7.01% | REALIZED_VOL_30D | 311.61 | 2026-08-24 | 289.98 | 333.23 | L002,L003,L012 | L013-L021,L027-L039 | LOW | Health Care / Medical Specialities; RS60 +10.6pp, mom60 +14.7% | earnings inside horizon; RSI14_d 71.2 overbought; beta -0.246 reverses in a risk-on turn |

## Score Attribution

| Ticker | Fund_Z | Tech_Z | Sent_Z | Macro_Z | Composite_Z | DQ | Penalties | Adj Score | Top Positive Drivers | Top Negative Drivers | Metric Ledger Rows |
|---|---|---|---|---|---|---|---|---|---|---|---|
| TRV | `UNAVAILABLE` | +1.1240 | `UNAVAILABLE` | +0.8397 | +0.463155 | 0.8 | −0.00 | +0.3705 | mom60 +25.44%; RS60 +21.35pp; MA D+W +1.00 | Fund_Z UNAVAILABLE (L046); Sent_Z UNAVAILABLE (L047); beta -0.701 | L013–L021, L027–L039 |
| RTX | `UNAVAILABLE` | +0.9877 | `UNAVAILABLE` | +0.5984 | +0.386070 | 0.8 | −0.00 | +0.3089 | mom60 +21.63%; RS60 +17.54pp; MA D+W +1.00 | Fund_Z UNAVAILABLE (L046); Sent_Z UNAVAILABLE (L047); beta -0.061 | L013–L021, L027–L039 |
| PAYX | `UNAVAILABLE` | +0.8884 | `UNAVAILABLE` | +0.7832 | +0.384000 | 0.8 | −0.00 | +0.3072 | mom60 +26.40%; RS60 +22.31pp; MA D+W +0.50 | Fund_Z UNAVAILABLE (L046); Sent_Z UNAVAILABLE (L047); beta -0.614 | L013–L021, L027–L039 |
| DGX | `UNAVAILABLE` | +0.8911 | `UNAVAILABLE` | +0.7664 | +0.382290 | 0.8 | −0.00 | +0.3058 | mom60 +17.30%; RS60 +13.21pp; MA D+W +1.00 | Fund_Z UNAVAILABLE (L046); Sent_Z UNAVAILABLE (L047); beta -0.576 | L013–L021, L027–L039 |
| UNP | `UNAVAILABLE` | +0.8658 | `UNAVAILABLE` | +0.7620 | +0.374040 | 0.8 | −0.00 | +0.2992 | mom60 +15.38%; RS60 +11.29pp; MA D+W +1.00 | Fund_Z UNAVAILABLE (L046); Sent_Z UNAVAILABLE (L047); beta -0.164 | L013–L021, L027–L039 |
| PCG | `UNAVAILABLE` | +0.7255 | `UNAVAILABLE` | +0.8880 | +0.350850 | 0.8 | −0.00 | +0.2807 | mom60 +10.10%; RS60 +6.01pp; MA D+W +1.00 | Fund_Z UNAVAILABLE (L046); Sent_Z UNAVAILABLE (L047); beta -0.260 | L013–L021, L027–L039 |
| CSX | `UNAVAILABLE` | +0.7750 | `UNAVAILABLE` | +0.7638 | +0.347070 | 0.8 | −0.00 | +0.2777 | mom60 +18.05%; RS60 +13.96pp; MA D+W +1.00 | Fund_Z UNAVAILABLE (L046); Sent_Z UNAVAILABLE (L047); beta +0.113 | L013–L021, L027–L039 |
| TMO | `UNAVAILABLE` | +0.8369 | `UNAVAILABLE` | +0.3852 | +0.308850 | 0.8 | −0.00 | +0.2471 | mom60 +20.97%; RS60 +16.88pp; MA D+W +0.50 | Fund_Z UNAVAILABLE (L046); Sent_Z UNAVAILABLE (L047); beta +0.098 | L013–L021, L027–L039 |
| NSC | `UNAVAILABLE` | +0.6341 | `UNAVAILABLE` | +0.7511 | +0.302895 | 0.8 | −0.00 | +0.2423 | mom60 +11.20%; RS60 +7.11pp; MA D+W +1.00 | Fund_Z UNAVAILABLE (L046); Sent_Z UNAVAILABLE (L047); beta -0.100 | L013–L021, L027–L039 |
| WELL | `UNAVAILABLE` | +0.8140 | `UNAVAILABLE` | +0.7939 | +0.363285 | 0.8 | −0.05 | +0.2406 | mom60 +18.06%; RS60 +13.97pp; MA D+W +1.00 | Fund_Z UNAVAILABLE (L046); Sent_Z UNAVAILABLE (L047); penalties -0.05 | L013–L021, L027–L039 |
| GD | `UNAVAILABLE` | +1.0243 | `UNAVAILABLE` | +0.7568 | +0.420810 | 0.8 | −0.10 | +0.2366 | mom60 +23.84%; RS60 +19.75pp; MA D+W +1.00 | Fund_Z UNAVAILABLE (L046); Sent_Z UNAVAILABLE (L047); penalties -0.10 | L013–L021, L027–L039 |
| PM | `UNAVAILABLE` | +0.6486 | `UNAVAILABLE` | +0.6082 | +0.285810 | 0.8 | −0.00 | +0.2286 | mom60 +17.31%; RS60 +13.22pp; MA D+W +1.00 | Fund_Z UNAVAILABLE (L046); Sent_Z UNAVAILABLE (L047); beta -0.540 | L013–L021, L027–L039 |
| MPC | `UNAVAILABLE` | +1.0669 | `UNAVAILABLE` | +0.5890 | +0.408420 | 0.8 | −0.10 | +0.2267 | mom60 +33.46%; RS60 +29.37pp; MA D+W +1.00 | Fund_Z UNAVAILABLE (L046); Sent_Z UNAVAILABLE (L047); penalties -0.10 | L013–L021, L027–L039 |
| CTAS | `UNAVAILABLE` | +0.6558 | `UNAVAILABLE` | +0.5615 | +0.280965 | 0.8 | −0.00 | +0.2248 | mom60 +18.51%; RS60 +14.42pp; MA D+W +0.50 | Fund_Z UNAVAILABLE (L046); Sent_Z UNAVAILABLE (L047); beta -0.290 | L013–L021, L027–L039 |
| SJM | `UNAVAILABLE` | +0.5629 | `UNAVAILABLE` | +0.7449 | +0.280605 | 0.8 | −0.00 | +0.2245 | mom60 +22.01%; RS60 +17.92pp; MA D+W +1.00 | Fund_Z UNAVAILABLE (L046); Sent_Z UNAVAILABLE (L047); beta -0.756 | L013–L021, L027–L039 |
| LMT | `UNAVAILABLE` | +0.7763 | `UNAVAILABLE` | +0.2687 | +0.273195 | 0.8 | −0.00 | +0.2186 | mom60 +14.47%; RS60 +10.38pp; MA D+W +1.00 | Fund_Z UNAVAILABLE (L046); Sent_Z UNAVAILABLE (L047); beta -0.459 | L013–L021, L027–L039 |
| WAB | `UNAVAILABLE` | +0.8479 | `UNAVAILABLE` | +0.0568 | +0.262890 | 0.8 | −0.00 | +0.2103 | mom60 +15.08%; RS60 +10.99pp; MA D+W +1.00 | Fund_Z UNAVAILABLE (L046); Sent_Z UNAVAILABLE (L047); beta +0.806 | L013–L021, L027–L039 |
| PKG | `UNAVAILABLE` | +0.8097 | `UNAVAILABLE` | +0.0809 | +0.255045 | 0.8 | −0.00 | +0.2040 | mom60 +15.04%; RS60 +10.95pp; MA D+W +1.00 | Fund_Z UNAVAILABLE (L046); Sent_Z UNAVAILABLE (L047); beta +0.811 | L013–L021, L027–L039 |
| MET | `UNAVAILABLE` | +0.8304 | `UNAVAILABLE` | +0.8014 | +0.369330 | 0.8 | −0.10 | +0.1955 | mom60 +22.07%; RS60 +17.98pp; MA D+W +1.00 | Fund_Z UNAVAILABLE (L046); Sent_Z UNAVAILABLE (L047); penalties -0.10 | L013–L021, L027–L039 |
| BNY | `UNAVAILABLE` | +0.5162 | `UNAVAILABLE` | +0.5941 | +0.243975 | 0.8 | −0.00 | +0.1952 | mom60 +19.00%; RS60 +14.91pp; MA D+W +1.00 | Fund_Z UNAVAILABLE (L046); Sent_Z UNAVAILABLE (L047); beta +0.566 | L013–L021, L027–L039 |
| VLO | `UNAVAILABLE` | +0.9460 | `UNAVAILABLE` | +0.4908 | +0.357420 | 0.8 | −0.10 | +0.1859 | mom60 +26.50%; RS60 +22.41pp; MA D+W +1.00 | Fund_Z UNAVAILABLE (L046); Sent_Z UNAVAILABLE (L047); penalties -0.10 | L013–L021, L027–L039 |
| HIG | `UNAVAILABLE` | +0.6809 | `UNAVAILABLE` | +0.9967 | +0.353775 | 0.8 | −0.10 | +0.1830 | mom60 +1.73%; RS60 -2.36pp; MA D+W +1.00 | Fund_Z UNAVAILABLE (L046); Sent_Z UNAVAILABLE (L047); penalties -0.10 | L013–L021, L027–L039 |
| PSX | `UNAVAILABLE` | +0.8405 | `UNAVAILABLE` | +0.5857 | +0.340005 | 0.8 | −0.10 | +0.1720 | mom60 +26.13%; RS60 +22.04pp; MA D+W +1.00 | Fund_Z UNAVAILABLE (L046); Sent_Z UNAVAILABLE (L047); penalties -0.10 | L013–L021, L027–L039 |
| LH | `UNAVAILABLE` | +0.6882 | `UNAVAILABLE` | +0.8733 | +0.337455 | 0.8 | −0.10 | +0.1700 | mom60 +14.65%; RS60 +10.56pp; MA D+W +0.50 | Fund_Z UNAVAILABLE (L046); Sent_Z UNAVAILABLE (L047); penalties -0.10 | L013–L021, L027–L039 |

## Metric Availability

| Metric Group | Sourceable Count | `UNAVAILABLE` Count | DQ / Confidence Effect | Notes |
|---|---:|---:|---|---|
| Risk / return (Sharpe, Sortino, IR, Treynor, Calmar, beta, TE) | 206 | 0 | none | L013–L016, L030 |
| Tail risk (60d max DD, VaR95, CVaR95) | 206 | 0 | negative drivers only | L017, L031 |
| Sizing (raw Kelly, 0.25 Kelly, cap status) | 206 | 0 | investability gate | L032 |
| Technical (TD-9, RSI, MACD, MA, momentum, volume, RS — D/W/M) | 518 | 0 | drives `Tech_Z` | L019–L021 |
| Fundamental / quality | **0** | **514** | family `UNAVAILABLE`; DQ → 0.8; blocks Threshold #2 | L046 |
| Sentiment / positioning | **0** | **514** | family `UNAVAILABLE`; DQ → 0.8; blocks Threshold #2 | L047 |
| Enhancing (IV/skew, short interest, bid-ask, revisions, ownership) | 0 | 514 | confidence cap `MEDIUM`, gross cap 50% — never a `GO` blocker | L048 |

No score in this artifact cites a metric absent from `01_preflight.md`, and **no missing metric is
described as neutral or supportive** — `Fund_Z` and `Sent_Z` are carried as `UNAVAILABLE` in every
table and contribute `0.00 (UNAVAILABLE)` to the arithmetic while *lowering* DQ and failing the
family-count threshold.

## Technical Indicator Summary

| Ticker | TD9 D/W/M | RSI14 D/W/M | MACD State D/W/M | MA Align D/W/M | Mom 20d/60d | RS20/RS60 vs SPY | Vol Ratio 20d | Indicator Ledger |
|---|---|---|---|---|---|---|---|---|
| TRV | SELL_SETUP_6/SELL_SETUP_8/SELL_SETUP_9 | 80.9/79.7/77.2 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | BULLISH/BULLISH/BULLISH | +21.67%/+25.44% | +21.04pp/+21.35pp | 1.29 | L019–L021 |
| RTX | SELL_SETUP_3/SELL_SETUP_9/SELL_SETUP_1 | 74.0/66.8/74.9 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | BULLISH/BULLISH/BULLISH | +14.04%/+21.63% | +13.41pp/+17.54pp | 1.26 | L019–L021 |
| PAYX | BUY_SETUP_3/SELL_SETUP_9/SELL_SETUP_2 | 64.7/64.5/50.2 | ABOVE_SIGNAL/ABOVE_SIGNAL/BELOW_SIGNAL | BULLISH/MIXED/MIXED | +17.40%/+26.40% | +16.77pp/+22.31pp | 0.85 | L019–L021 |
| DGX | SELL_SETUP_7/SELL_SETUP_5/SELL_SETUP_6 | 72.7/68.3/68.7 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | BULLISH/BULLISH/BULLISH | +10.93%/+17.30% | +10.30pp/+13.21pp | 1.42 | L019–L021 |
| UNP | SELL_SETUP_2/SELL_SETUP_5/SELL_SETUP_9 | 73.0/73.3/68.6 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | BULLISH/BULLISH/BULLISH | +14.79%/+15.38% | +14.16pp/+11.29pp | 1.21 | L019–L021 |
| PCG | SELL_SETUP_3/SELL_SETUP_3/SELL_SETUP_1 | 60.1/58.5/55.6 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | BULLISH/BULLISH/BULLISH | +4.81%/+10.10% | +4.18pp/+6.01pp | 1.94 | L019–L021 |
| CSX | SELL_SETUP_2/SELL_SETUP_9/SELL_SETUP_9 | 76.1/78.9/76.5 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | BULLISH/BULLISH/BULLISH | +12.20%/+18.05% | +11.57pp/+13.96pp | 1.08 | L019–L021 |
| TMO | SELL_SETUP_2/SELL_SETUP_9/SELL_SETUP_1 | 70.8/62.9/55.8 | ABOVE_SIGNAL/ABOVE_SIGNAL/BULLISH_CROSS | BULLISH/MIXED/MIXED | +12.36%/+20.97% | +11.73pp/+16.88pp | 1.28 | L019–L021 |
| NSC | SELL_SETUP_2/SELL_SETUP_5/SELL_SETUP_4 | 73.2/71.0/67.4 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | BULLISH/BULLISH/BULLISH | +12.37%/+11.20% | +11.74pp/+7.11pp | 1.05 | L019–L021 |
| WELL | SELL_SETUP_9/SELL_SETUP_5/SELL_SETUP_4 | 74.1/72.6/77.6 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | BULLISH/BULLISH/BULLISH | +12.67%/+18.06% | +12.04pp/+13.97pp | 1.13 | L019–L021 |
| GD | SELL_SETUP_5/SELL_SETUP_4/SELL_SETUP_1 | 70.3/65.0/78.3 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | BULLISH/BULLISH/BULLISH | +12.69%/+23.84% | +12.06pp/+19.75pp | 1.33 | L019–L021 |
| PM | SELL_SETUP_1/SELL_SETUP_2/SELL_SETUP_1 | 59.7/64.1/68.9 | ABOVE_SIGNAL/ABOVE_SIGNAL/BULLISH_CROSS | BULLISH/BULLISH/BULLISH | +7.86%/+17.31% | +7.23pp/+13.22pp | 0.85 | L019–L021 |
| MPC | BUY_SETUP_2/SELL_SETUP_5/SELL_SETUP_6 | 68.2/73.2/80.9 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | BULLISH/BULLISH/BULLISH | +21.96%/+33.46% | +21.33pp/+29.37pp | 0.89 | L019–L021 |
| CTAS | SELL_SETUP_1/SELL_SETUP_5/SELL_SETUP_1 | 72.1/65.0/58.4 | ABOVE_SIGNAL/ABOVE_SIGNAL/BELOW_SIGNAL | BULLISH/MIXED/BULLISH | +21.78%/+18.51% | +21.15pp/+14.42pp | 0.81 | L019–L021 |
| SJM | SELL_SETUP_7/SELL_SETUP_2/SELL_SETUP_1 | 61.2/63.6/56.6 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | BULLISH/BULLISH/MIXED | +5.17%/+22.01% | +4.54pp/+17.92pp | 0.70 | L019–L021 |
| LMT | SELL_SETUP_3/SELL_SETUP_1/BUY_SETUP_3 | 71.7/57.5/58.9 | ABOVE_SIGNAL/BELOW_SIGNAL/ABOVE_SIGNAL | BULLISH/BULLISH/BULLISH | +15.36%/+14.47% | +14.73pp/+10.38pp | 1.41 | L019–L021 |
| WAB | SELL_SETUP_4/SELL_SETUP_1/SELL_SETUP_9 | 75.1/74.3/77.6 | ABOVE_SIGNAL/BULLISH_CROSS/ABOVE_SIGNAL | BULLISH/BULLISH/BULLISH | +7.10%/+15.08% | +6.47pp/+10.99pp | 1.46 | L019–L021 |
| PKG | SELL_SETUP_2/SELL_SETUP_7/SELL_SETUP_2 | 72.2/67.1/68.1 | BULLISH_CROSS/ABOVE_SIGNAL/ABOVE_SIGNAL | BULLISH/BULLISH/BULLISH | +5.52%/+15.04% | +4.89pp/+10.95pp | 2.10 | L019–L021 |
| MET | SELL_SETUP_1/SELL_SETUP_9/SELL_SETUP_4 | 67.2/71.0/67.7 | BELOW_SIGNAL/ABOVE_SIGNAL/BULLISH_CROSS | BULLISH/BULLISH/BULLISH | +12.05%/+22.07% | +11.42pp/+17.98pp | 1.37 | L019–L021 |
| BNY | SELL_SETUP_2/SELL_SETUP_9/SELL_SETUP_9 | 63.5/84.1/90.9 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | BULLISH/BULLISH/BULLISH | +9.27%/+19.00% | +8.64pp/+14.91pp | 0.52 | L019–L021 |
| VLO | BUY_SETUP_2/SELL_SETUP_5/SELL_SETUP_9 | 63.1/71.6/82.3 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | BULLISH/BULLISH/BULLISH | +18.60%/+26.50% | +17.97pp/+22.41pp | 0.72 | L019–L021 |
| HIG | SELL_SETUP_5/SELL_SETUP_5/SELL_SETUP_1 | 58.2/58.4/64.0 | ABOVE_SIGNAL/ABOVE_SIGNAL/BELOW_SIGNAL | BULLISH/BULLISH/BULLISH | +7.79%/+1.73% | +7.16pp/-2.36pp | 1.58 | L019–L021 |
| PSX | BUY_SETUP_1/SELL_SETUP_3/SELL_SETUP_7 | 67.3/69.8/74.5 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | BULLISH/BULLISH/BULLISH | +20.38%/+26.13% | +19.75pp/+22.04pp | 0.64 | L019–L021 |
| LH | SELL_SETUP_2/SELL_SETUP_5/SELL_SETUP_1 | 71.2/63.4/62.0 | ABOVE_SIGNAL/ABOVE_SIGNAL/BULLISH_CROSS | BULLISH/MIXED/BULLISH | +11.43%/+14.65% | +10.80pp/+10.56pp | 1.28 | L019–L021 |

## Investable Subset

**Empty — 0 of 514 names.** Three of the five Evidence Thresholds fail independently, for every name
in the universe:

| Threshold | Requirement | This run | Status |
|---|---|---|---|
| #1 | Adjusted-score pctl ≥ 80th | 103 names clear this | **passes for 103 names** |
| #2 | ≥ 3 of 4 factor families non-negative | max achievable is **2** — `Fund_Z` and `Sent_Z` are `UNAVAILABLE` and cannot count | **fails universe-wide** |
| #3 | No single family > 50% of total conviction | Technical carries 0.30 of the 0.45 available weight = **66.7%** | **fails universe-wide** |
| #4 | Data completeness ≥ 85% | DQ = 0.8 → 80% | **fails universe-wide** |
| #5 | No hard stop from `§ Stop Criteria` | none fires | passes |

Thresholds #2, #3 and #4 all trace to the same root cause: two of four factor families have no fetch
path at universe scale. This is a **data-coverage** blocker, not a market judgement, and it is not
something scoring can work around. Per `agents.md § Factor Scoring`, fewer than 5 names passing means
**`NO_TRADE` is recommended**.

## Monitoring Sleeve

All 24 published names, each carrying a settleable `mu` and `sigma` so the forecast is
auditable at 2026-08-24. `rules.md § Sigma Fallback Chain` is satisfied for every one — there is no
blanket `sigma = UNAVAILABLE` anywhere, which would be a publishing failure rather than caution.

## Near-Miss Rejection List

| Rank | Ticker | Adj Score | Pctl | Penalty | Why not published |
|---|---|---|---|---|---|
| 21 | AON | +0.1905 | 96.10 | −0.00 | earnings not grounded — entered the top-30 only after the bounded passes converged; excluded rather than scored penalty-free |
| 22 | ESS | +0.1890 | 95.91 | −0.00 | earnings not grounded — entered the top-30 only after the bounded passes converged; excluded rather than scored penalty-free |
| 23 | ITW | +0.1867 | 95.71 | −0.00 | earnings not grounded — entered the top-30 only after the bounded passes converged; excluded rather than scored penalty-free |
| 24 | WM | +0.1862 | 95.52 | −0.00 | earnings not grounded — entered the top-30 only after the bounded passes converged; excluded rather than scored penalty-free |
| 26 | JNJ | +0.1834 | 95.13 | −0.00 | earnings not grounded — entered the top-30 only after the bounded passes converged; excluded rather than scored penalty-free |
| 28 | DUK | +0.1824 | 94.74 | −0.00 | earnings not grounded — entered the top-30 only after the bounded passes converged; excluded rather than scored penalty-free |
| 29 | CTVA | +0.1806 | 94.54 | −0.00 | earnings not grounded — entered the top-30 only after the bounded passes converged; excluded rather than scored penalty-free |
| 30 | AMP | +0.1804 | 94.35 | −0.00 | earnings not grounded — entered the top-30 only after the bounded passes converged; excluded rather than scored penalty-free |
| 31 | MNST | +0.1802 | 94.15 | −0.00 | earnings not grounded — entered the top-30 only after the bounded passes converged; excluded rather than scored penalty-free |
| 32 | GL | +0.1786 | 93.96 | −0.00 | earnings not grounded — entered the top-30 only after the bounded passes converged; excluded rather than scored penalty-free |
| 33 | VRSK | +0.1782 | 93.76 | −0.00 | earnings not grounded — entered the top-30 only after the bounded passes converged; excluded rather than scored penalty-free |
| 34 | PSA | +0.1765 | 93.57 | −0.00 | earnings not grounded — entered the top-30 only after the bounded passes converged; excluded rather than scored penalty-free |

## What Drives the Leaderboard

With Fundamental and Sentiment absent, `Adj Score` is `(0.30·Tech_Z + 0.15·Macro_Z) × 0.8 − penalties`,
so Technical dominates at two-thirds of available weight. Combined with the disclosed defensive Macro
polarity (L053), the leaderboard is a **low-beta, low-vol, positive-relative-strength screen**:
19 of 24 published names carry negative 60-day
beta, and the top sector is Industrials at 6 of the top 10. That concentration is
precisely what makes the portfolio beta band unreachable in `07`.
