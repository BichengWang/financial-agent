# 05 — Factor Scores — 2026-08-03

Universe **512** scored names · label **`INDEX_UNION_PCTL (n=512)`** ·
basis 2026-08-03 completed close.

## Scoring architecture actually executed

`Adj Score = (0.30*Fund_Z + 0.30*Tech_Z + 0.25*Sent_Z + 0.15*Macro_Z) * DQ - Penalties`

| Family | Weight | State | Sourceable metrics |
|---|---|---|---|
| Fundamental | 0.30 | **`UNAVAILABLE`** | 0 — contributes `0.00 (UNAVAILABLE)` |
| Technical / Price | 0.30 | `AVAILABLE` | **6 slots** (deduplicated this run): 20d momentum, 60d momentum, MA alignment (d+w), MACD state (d+w), 20d volume ratio, 60d max drawdown |
| Sentiment / Positioning | 0.25 | **`UNAVAILABLE`** | 0 — contributes `0.00 (UNAVAILABLE)` |
| Macro / Regime | 0.15 | `AVAILABLE` | 4: 60d beta (distance from 1.0, negated), sector RS60 leadership, rate sensitivity vs TLT (\\|beta\\| negated), realized-vol stability (30d/60d, negated) |

Each family z-score is the equal-weighted mean of its metric z-scores, computed cross-sectionally
over the 512 scored names after winsorizing at the 5th/95th percentiles, per
`rules.md § Family Aggregation`.

State encodings (disclosed so this run is reproducible): MA alignment `BULLISH=+1, MIXED=0,
BEARISH=-1`, averaged over daily+weekly. MACD state `BULLISH_CROSS=+2, ABOVE_SIGNAL=+1,
ON_SIGNAL=0, BELOW_SIGNAL=-1, BEARISH_CROSS=-2`, averaged over daily+weekly. `max_drawdown_60d` is
z-scored **as a signed negative number**, so a shallower drawdown scores higher — it is *not*
negated a second time.

**Data-quality multiplier = 0.80** ("notable coverage gaps"): two of four families are unavailable
universe-wide. Only 2 of 4 families carry information, so the effective score is
`(0.30*Tech_Z + 0.15*Macro_Z) * 0.80` — stated plainly rather than hidden behind a composite number.

## Tech_Z deduplication — **applied this run**

The Track B change accepted on 2026-08-01 and stamped **effective 2026-08-03** is live in this package.
`technical_indicators.py::add_relative_strength` computes `relative_strength = momentum -
benchmark_momentum`; subtracting SPY's momentum is a constant shift across every name, and a constant
shift leaves a cross-sectional z-score unchanged. Re-measured on today's universe:

| Identity | Max abs difference over 512 names |
|---|---|
| `z(rs20)` vs `z(mom20)` | **4.4409e-16** |
| `z(rs60)` vs `z(mom60)` | **4.4409e-16** |

Floating-point zero, reproducing the 2026-08-01 measurement exactly. `Tech_Z` is therefore built from
**6 distinct metrics**, not 8. Momentum now carries **33.3%** of `Tech_Z` (16.7% of the live composite)
instead of 50% (33.3%). Relative strength is still computed, displayed and ledgered below as a
diagnostic — it simply stops being counted twice in the arithmetic.

**Measured effect of the switch, this run** (both engines run side by side on identical inputs):

| Statistic | Value |
|---|---|
| Top-24 published-set overlap with the legacy 8-slot engine | **13/24** |
| Top-30 overlap | **18/30** |
| Median rank move, all 512 names | **31 places** |
| 90th-pctl rank move | 70 places |
| Max rank move | 138 places |
| Rank-1 name | DXCM (legacy engine: DXCM) |

The turnover is larger than the 2026-08-01 estimate (which measured 19/24 top-24 overlap and a
median move of 12 places on the 2026-07-31 cross-section). That estimate was made on a different
day's dispersion and is not a forecast of today's; the honest reading is that the effect size varies
with how concentrated momentum is on the day. Names entering the published set purely on the switch:
**KKR, ARES, TGT, REGN, VEEV, MSFT, PCAR, LH, COF, BX, HIG**. Names leaving: **PRU, DDOG, MET, SOLV, CPAY, DVA, AMGN, HPQ, AIZ, HST, CDW**.

## Engine verification performed before publishing

Because this is the first package on a changed engine, the engine was validated by **reproducing the
prior package** from the same 2026-07-31 basis under the legacy 8-slot configuration:

| Check | Result |
|---|---|
| Entry prices vs `claude-opus-5-2026-08-01` top-20 | 18/20 exact to the cent; NTAP and PFG differ by $0.03 (0.017% / 0.026%) |
| `Tech_Z` reproduction | all 20 names within 0.03 absolute |
| `Macro_Z` reproduction | mean absolute error 0.092, max 0.293, concentrated in the vol-stability slot |
| Defect found and fixed | **drawdown polarity** — `max_drawdown_60d` was being negated before z-scoring, which inverted the metric so that *deeper* drawdowns scored *better* |

The drawdown-polarity defect was introduced in this run's engine and caught by the reproduction test
before any score was published; all figures in this artifact are post-fix. The residual `Macro_Z`
gap is a genuine under-specification: the disclosed methodology does not pin down the vol-stability
window precisely enough to reproduce it exactly. That is this run's evolution proposal — see `13`.

## Calibration feedback binding (read before scoring)

From `02 § 0`: weighted-mean rank IC **-0.0879** over n=515 settled `EQUITY_ALPHA` records,
non-positive in **20 of 32** vintages. `agents.md § Calibration Feedback Binding`
therefore **caps all confidence at `MEDIUM`**, applied to every record in this package. CI coverage is
69.90% (inside 55–85%), so the wider-sigma rule does **not** trigger and sigma stays
`REALIZED_VOL_30D`.

## Ranked candidates (top 20 of 205 ranked)

| Rank | Ticker | Company | Entry | Price Date | Tag | Adj Score | Score Trace | Pctl | Beta | 30d RVol | Sharpe | Sortino | IR | Kelly 0.25 | VaR95 | CVaR95 | Max DD60 | TD9 D/W/M | RSI14 D/W/M | MACD D/W/M | Days to Earn | mu | sigma | Sigma Source | Target | Target Date | 70% CI Lo | 70% CI Hi | Ledger | Metric Ledger | Conf | Primary Thesis | Key Risk |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **DXCM** | DexCom Inc. Common Stock | 87.31 | 2026-08-03 | `HISTORICAL` | **+0.4297** | `(0.3*0.00(UA) + 0.3*+1.4253 + 0.25*0.00(UA) + 0.15*+0.7300) * 0.80 - 0.00 = +0.4297` | 100.00 | +0.205 | 15.33% | 0.371 | 0.892 | 0.394 | 63.79% | -19.30% | -25.59% | -13.86% | S5/S4/S2 | 72.6/67.8/53.5 | ABOVE/ABOVE/ABOVE | none in 28d sweep | +6.0% | 15.33% | `REALIZED_VOL_30D` | 92.55 | 2026-08-31 | 78.62 | 106.47 | `L-PX-DXCM` | `L-TI-DXCM`,`L-RM-DXCM`,`L-EA-DXCM` | MEDIUM | Health Care leader on the deduplicated Tech_Z (`INFERRED`) | rank-order inversion risk (see § Calibration) |
| 2 | **BMY** | Bristol-Myers Squibb Company | 65.47 | 2026-08-03 | `HISTORICAL` | **+0.3993** | `(0.3*0.00(UA) + 0.3*+1.3623 + 0.25*0.00(UA) + 0.15*+0.6031) * 0.80 - 0.00 = +0.3993` | 99.80 | -0.203 | 8.67% | 0.656 | 1.156 | 0.781 | 199.73% | -8.30% | -11.85% | -9.32% | S9/S7/S2 | 71.8/68.5/65.5 | ABOVE/ABOVE/ABOVE | none in 28d sweep | +6.0% | 8.67% | `REALIZED_VOL_30D` | 69.40 | 2026-08-31 | 63.50 | 75.30 | `L-PX-BMY` | `L-TI-BMY`,`L-RM-BMY`,`L-EA-BMY` | MEDIUM | Health Care leader on the deduplicated Tech_Z (`INFERRED`) | rank-order inversion risk (see § Calibration) |
| 3 | **BEN** | Franklin Resources Inc. Comm | 35.24 | 2026-08-03 | `HISTORICAL` | **+0.3643** | `(0.3*0.00(UA) + 0.3*+1.0970 + 0.25*0.00(UA) + 0.15*+0.8420) * 0.80 - 0.00 = +0.3643` | 99.61 | +1.095 | 8.12% | 0.700 | 1.098 | 0.557 | 227.30% | -7.40% | -10.73% | -6.42% | S7/S1/S8 | 66.1/74.3/71.8 | BULL_X/ABOVE/ABOVE | none in 28d sweep | +6.0% | 8.12% | `REALIZED_VOL_30D` | 37.35 | 2026-08-31 | 34.38 | 40.33 | `L-PX-BEN` | `L-TI-BEN`,`L-RM-BEN`,`L-EA-BEN` | MEDIUM | Finance leader on the deduplicated Tech_Z (`INFERRED`) | rank-order inversion risk (see § Calibration) |
| 4 | **BAX** | Baxter International Inc. Co | 28.10 | 2026-08-03 | `HISTORICAL` | **+0.3377** | `(0.3*0.00(UA) + 0.3*+1.2327 + 0.25*0.00(UA) + 0.15*+0.3485) * 0.80 - 0.00 = +0.3377` | 99.41 | +0.644 | 14.23% | 0.400 | 0.930 | 0.380 | 74.07% | -17.48% | -23.32% | -7.19% | S7/S9/S3 | 76.4/73.6/51.7 | ABOVE/ABOVE/ABOVE | none in 28d sweep | +6.0% | 14.23% | `REALIZED_VOL_30D` | 29.79 | 2026-08-31 | 25.63 | 33.94 | `L-PX-BAX` | `L-TI-BAX`,`L-RM-BAX`,`L-EA-BAX` | MEDIUM | Health Care leader on the deduplicated Tech_Z (`INFERRED`) | rank-order inversion risk (see § Calibration) |
| 5 | **WTW** | Willis Towers Watson Public  | 341.63 | 2026-08-03 | `HISTORICAL` | **+0.3289** | `(0.3*0.00(UA) + 0.3*+1.1885 + 0.25*0.00(UA) + 0.15*+0.3638) * 0.80 - 0.00 = +0.3289` | 99.22 | -0.367 | 9.85% | 0.578 | 1.911 | 0.738 | 154.71% | -10.25% | -14.28% | -6.18% | S7/S7/S2 | 81.6/68.4/60.8 | ABOVE/ABOVE/BELOW | none in 28d sweep | +6.0% | 9.85% | `REALIZED_VOL_30D` | 362.13 | 2026-08-31 | 327.14 | 397.11 | `L-PX-WTW` | `L-TI-WTW`,`L-RM-WTW`,`L-EA-WTW` | MEDIUM | Finance leader on the deduplicated Tech_Z (`INFERRED`) | rank-order inversion risk (see § Calibration) |
| 6 | **COO** | The Cooper Companies Inc. Co | 74.23 | 2026-08-03 | `HISTORICAL` | **+0.2826** | `(0.3*0.00(UA) + 0.3*+0.8388 + 0.25*0.00(UA) + 0.15*+0.6774) * 0.80 - 0.00 = +0.2826` | 99.02 | -0.380 | 8.75% | 0.650 | 1.093 | 0.737 | 195.83% | -8.44% | -12.03% | -7.67% | S5/S1/S2 | 63.3/55.8/46.2 | BULL_X/ABOVE/BULL_X | 37 | +6.0% | 8.75% | `REALIZED_VOL_30D` | 78.68 | 2026-08-31 | 71.93 | 85.44 | `L-PX-COO` | `L-TI-COO`,`L-RM-COO`,`L-EA-COO` | MEDIUM | Health Care leader on the deduplicated Tech_Z (`INFERRED`) | rank-order inversion risk (see § Calibration) |
| 7 | **BBY** | Best Buy Co. Inc. Common Sto | 85.25 | 2026-08-03 | `HISTORICAL` | **+0.2648** | `(0.3*0.00(UA) + 0.3*+0.8678 + 0.25*0.00(UA) + 0.15*+0.4710) * 0.80 - 0.00 = +0.2648` | 98.83 | +0.421 | 8.14% | 0.699 | 1.341 | 0.401 | 226.45% | -7.43% | -10.77% | -8.93% | B2/S9/S4 | 56.3/65.1/58.9 | BELOW/ABOVE/ABOVE | 24 | +6.0% | 8.14% | `REALIZED_VOL_30D` | 90.36 | 2026-08-31 | 83.15 | 97.58 | `L-PX-BBY` | `L-TI-BBY`,`L-RM-BBY`,`L-EA-BBY` | MEDIUM | Consumer Discretionary leader on the deduplicated Tech_Z (`INFERRED`) | rank-order inversion risk (see § Calibration) |
| 8 | **FTNT** | Fortinet Inc. Common Stock | 163.21 | 2026-08-03 | `HISTORICAL` | **+0.2643** | `(0.3*0.00(UA) + 0.3*+0.5854 + 0.25*0.00(UA) + 0.15*+1.0318) * 0.80 - 0.00 = +0.2643` | 98.63 | +0.968 | 10.70% | 0.531 | 1.713 | 0.257 | 130.99% | -11.66% | -16.04% | -10.10% | S4/S9/S6 | 61.3/77.7/78.4 | BELOW/ABOVE/ABOVE | none in 28d sweep | +6.0% | 10.70% | `REALIZED_VOL_30D` | 173.00 | 2026-08-31 | 154.84 | 191.17 | `L-PX-FTNT` | `L-TI-FTNT`,`L-RM-FTNT`,`L-EA-FTNT` | MEDIUM | Technology leader on the deduplicated Tech_Z (`INFERRED`) | rank-order inversion risk (see § Calibration) |
| 9 | **ROST** | Ross Stores Inc. Common Stoc | 252.91 | 2026-08-03 | `HISTORICAL` | **+0.2596** | `(0.3*0.00(UA) + 0.3*+0.9091 + 0.25*0.00(UA) + 0.15*+0.3448) * 0.80 - 0.00 = +0.2596` | 98.43 | +0.219 | 8.84% | 0.643 | 0.755 | 0.564 | 191.85% | -8.59% | -12.22% | -13.03% | S7/S4/S9 | 71.0/69.1/76.4 | ABOVE/BULL_X/ABOVE | 17 | +6.0% | 8.84% | `REALIZED_VOL_30D` | 268.08 | 2026-08-31 | 244.83 | 291.34 | `L-PX-ROST` | `L-TI-ROST`,`L-RM-ROST`,`L-EA-ROST` | MEDIUM | Consumer Discretionary leader on the deduplicated Tech_Z (`INFERRED`) | rank-order inversion risk (see § Calibration) |
| 10 | **NTAP** | NetApp Inc. Common Stock | 182.92 | 2026-08-03 | `HISTORICAL` | **+0.2576** | `(0.3*0.00(UA) + 0.3*+0.7564 + 0.25*0.00(UA) + 0.15*+0.6338) * 0.80 - 0.00 = +0.2576` | 98.24 | +1.439 | 12.08% | 0.471 | 0.756 | 0.176 | 102.71% | -13.94% | -18.89% | -15.81% | S9/S5/S5 | 68.0/74.3/71.5 | ABOVE/ABOVE/ABOVE | 23 | +6.0% | 12.08% | `REALIZED_VOL_30D` | 193.90 | 2026-08-31 | 170.91 | 216.89 | `L-PX-NTAP` | `L-TI-NTAP`,`L-RM-NTAP`,`L-EA-NTAP` | MEDIUM | Technology leader on the deduplicated Tech_Z (`INFERRED`) | rank-order inversion risk (see § Calibration) |
| 11 | **KKR** | KKR & Co. Inc. Common Stock | 106.56 | 2026-08-03 | `HISTORICAL` | **+0.2488** | `(0.3*0.00(UA) + 0.3*+0.7839 + 0.25*0.00(UA) + 0.15*+0.5060) * 0.80 - 0.00 = +0.2488` | 98.04 | +1.273 | 10.42% | 0.546 | 1.026 | 0.409 | 138.26% | -11.19% | -15.46% | -13.08% | S1/S6/S3 | 65.8/55.3/49.3 | ABOVE/ABOVE/BELOW | none in 28d sweep | +6.0% | 10.42% | `REALIZED_VOL_30D` | 112.95 | 2026-08-31 | 101.41 | 124.50 | `L-PX-KKR` | `L-TI-KKR`,`L-RM-KKR`,`L-EA-KKR` | MEDIUM | Finance leader on the deduplicated Tech_Z (`INFERRED`) | rank-order inversion risk (see § Calibration) |
| 12 | **IQV** | IQVIA Holdings Inc. Common S | 233.36 | 2026-08-03 | `HISTORICAL` | **+0.2463** | `(0.3*0.00(UA) + 0.3*+0.9479 + 0.25*0.00(UA) + 0.15*+0.1565) * 0.80 - 0.00 = +0.2463` | 97.85 | -0.211 | 15.39% | 0.369 | 1.226 | 0.461 | 63.29% | -19.40% | -25.71% | -10.23% | B1/S7/S3 | 66.4/66.3/57.0 | ABOVE/ABOVE/ABOVE | none in 28d sweep | +6.0% | 15.39% | `REALIZED_VOL_30D` | 247.36 | 2026-08-31 | 210.00 | 284.72 | `L-PX-IQV` | `L-TI-IQV`,`L-RM-IQV`,`L-EA-IQV` | MEDIUM | Health Care leader on the deduplicated Tech_Z (`INFERRED`) | rank-order inversion risk (see § Calibration) |
| 13 | **ARES** | Ares Management Corporation  | 138.57 | 2026-08-03 | `HISTORICAL` | **+0.2416** | `(0.3*0.00(UA) + 0.3*+0.8771 + 0.25*0.00(UA) + 0.15*+0.2589) * 0.80 - 0.00 = +0.2416` | 97.65 | +1.722 | 13.46% | 0.423 | 0.816 | 0.249 | 82.80% | -16.21% | -21.73% | -20.28% | S2/S3/S3 | 69.3/57.4/51.6 | ABOVE/ABOVE/BELOW | none in 28d sweep | +6.0% | 13.46% | `REALIZED_VOL_30D` | 146.88 | 2026-08-31 | 127.49 | 166.28 | `L-PX-ARES` | `L-TI-ARES`,`L-RM-ARES`,`L-EA-ARES` | MEDIUM | Finance leader on the deduplicated Tech_Z (`INFERRED`) | rank-order inversion risk (see § Calibration) |
| 14 | **TGT** | Target Corporation Common St | 149.35 | 2026-08-03 | `HISTORICAL` | **+0.2409** | `(0.3*0.00(UA) + 0.3*+1.0498 + 0.25*0.00(UA) + 0.15*-0.0922) * 0.80 - 0.00 = +0.2409` | 97.46 | -0.164 | 10.03% | 0.567 | 0.973 | 0.617 | 149.12% | -10.55% | -14.66% | -10.69% | S6/S2/S9 | 69.5/68.2/65.0 | ABOVE/ABOVE/ABOVE | 16 | +6.0% | 10.03% | `REALIZED_VOL_30D` | 158.31 | 2026-08-31 | 142.73 | 173.89 | `L-PX-TGT` | `L-TI-TGT`,`L-RM-TGT`,`L-EA-TGT` | MEDIUM | Consumer Discretionary leader on the deduplicated Tech_Z (`INFERRED`) | rank-order inversion risk (see § Calibration) |
| 15 | **REGN** | Regeneron Pharmaceuticals In | 759.24 | 2026-08-03 | `HISTORICAL` | **+0.2396** | `(0.3*0.00(UA) + 0.3*+0.5291 + 0.25*0.00(UA) + 0.15*+0.9386) * 0.80 - 0.00 = +0.2396` | 97.26 | +0.320 | 9.40% | 0.605 | 1.341 | 0.521 | 169.92% | -9.50% | -13.36% | -16.84% | S5/S7/S1 | 76.4/60.4/52.8 | ABOVE/ABOVE/ABOVE | none in 28d sweep | +6.0% | 9.40% | `REALIZED_VOL_30D` | 804.79 | 2026-08-31 | 730.61 | 878.98 | `L-PX-REGN` | `L-TI-REGN`,`L-RM-REGN`,`L-EA-REGN` | MEDIUM | Health Care leader on the deduplicated Tech_Z (`INFERRED`) | rank-order inversion risk (see § Calibration) |
| 16 | **ZBRA** | Zebra Technologies Corporati | 291.64 | 2026-08-03 | `HISTORICAL` | **+0.2361** | `(0.3*0.00(UA) + 0.3*+1.0510 + 0.25*0.00(UA) + 0.15*+0.6987) * 0.80 - 0.10 = +0.2361` | 97.06 | +1.396 | 11.19% | 0.508 | 1.285 | 0.247 | 119.83% | -12.46% | -17.05% | -16.64% | S6/S7/S4 | 68.0/63.4/50.5 | ABOVE/ABOVE/ABOVE | 1 | +6.0% | 11.19% | `REALIZED_VOL_30D` | 309.14 | 2026-08-31 | 275.20 | 343.07 | `L-PX-ZBRA` | `L-TI-ZBRA`,`L-RM-ZBRA`,`L-EA-ZBRA` | MEDIUM | Industrials leader on the deduplicated Tech_Z (`INFERRED`) | prints in 1d — penalised, confidence capped |
| 17 | **VEEV** | Veeva Systems Inc. Class A C | 206.25 | 2026-08-03 | `HISTORICAL` | **+0.2339** | `(0.3*0.00(UA) + 0.3*+0.9040 + 0.25*0.00(UA) + 0.15*+0.1409) * 0.80 - 0.00 = +0.2339` | 96.87 | -0.004 | 12.76% | 0.446 | 1.061 | 0.451 | 92.10% | -15.06% | -20.29% | -18.82% | S6/S6/S2 | 63.8/56.8/47.4 | ABOVE/ABOVE/BELOW | 23 | +6.0% | 12.76% | `REALIZED_VOL_30D` | 218.62 | 2026-08-31 | 191.25 | 246.00 | `L-PX-VEEV` | `L-TI-VEEV`,`L-RM-VEEV`,`L-EA-VEEV` | MEDIUM | Technology leader on the deduplicated Tech_Z (`INFERRED`) | rank-order inversion risk (see § Calibration) |
| 18 | **GRMN** | Garmin Ltd. Common Stock (Sw | 304.76 | 2026-08-03 | `HISTORICAL` | **+0.2318** | `(0.3*0.00(UA) + 0.3*+1.0203 + 0.25*0.00(UA) + 0.15*-0.1086) * 0.80 - 0.00 = +0.2318` | 96.67 | +0.173 | 15.28% | 0.372 | 1.365 | 0.462 | 64.23% | -19.21% | -25.48% | -7.03% | S6/S6/S2 | 79.9/73.1/69.9 | ABOVE/ABOVE/ABOVE | none in 28d sweep | +6.0% | 15.28% | `REALIZED_VOL_30D` | 323.05 | 2026-08-31 | 274.61 | 371.48 | `L-PX-GRMN` | `L-TI-GRMN`,`L-RM-GRMN`,`L-EA-GRMN` | MEDIUM | Industrials leader on the deduplicated Tech_Z (`INFERRED`) | rank-order inversion risk (see § Calibration) |
| 19 | **MSFT** | Microsoft Corporation Common | 487.65 | 2026-08-03 | `HISTORICAL` | **+0.2305** | `(0.3*0.00(UA) + 0.3*+0.9667 + 0.25*0.00(UA) + 0.15*-0.0126) * 0.80 - 0.00 = +0.2305` | 96.48 | +1.066 | 16.05% | 0.354 | 1.521 | 0.301 | 58.20% | -20.49% | -27.07% | -23.38% | S5/S4/S2 | 78.3/64.0/57.0 | ABOVE/ABOVE/BELOW | none in 28d sweep | +6.0% | 16.05% | `REALIZED_VOL_30D` | 516.91 | 2026-08-31 | 435.49 | 598.33 | `L-PX-MSFT` | `L-TI-MSFT`,`L-RM-MSFT`,`L-EA-MSFT` | MEDIUM | Technology leader on the deduplicated Tech_Z (`INFERRED`) | rank-order inversion risk (see § Calibration) |
| 20 | **PCAR** | PACCAR Inc. Common Stock | 132.06 | 2026-08-03 | `HISTORICAL` | **+0.2303** | `(0.3*0.00(UA) + 0.3*+0.8621 + 0.25*0.00(UA) + 0.15*+0.1952) * 0.80 - 0.00 = +0.2303` | 96.28 | +1.034 | 8.90% | 0.639 | 1.440 | 0.502 | 189.46% | -8.68% | -12.33% | -5.86% | B2/S9/S2 | 59.7/66.7/66.6 | ABOVE/ABOVE/ABOVE | none in 28d sweep | +6.0% | 8.90% | `REALIZED_VOL_30D` | 139.98 | 2026-08-31 | 127.76 | 152.20 | `L-PX-PCAR` | `L-TI-PCAR`,`L-RM-PCAR`,`L-EA-PCAR` | MEDIUM | Consumer Discretionary leader on the deduplicated Tech_Z (`INFERRED`) | rank-order inversion risk (see § Calibration) |

## Score attribution

| Ticker | Fund_Z | Tech_Z | Sent_Z | Macro_Z | Composite_Z | DQ | Penalties | Adj Score | Top Positive Drivers | Top Negative Drivers | Metric Ledger |
|---|---|---|---|---|---|---|---|---|---|---|---|
| DXCM | `UNAVAILABLE` | +1.4253 | `UNAVAILABLE` | +0.7300 | +0.5371 | 0.80 | 0.00 | **+0.4297** | vol_conf +2.42; sector_lead +1.93; mom60 +1.86 | vol_stability -0.55 | `L-TI-DXCM`,`L-RM-DXCM` |
| BMY | `UNAVAILABLE` | +1.3623 | `UNAVAILABLE` | +0.6031 | +0.4992 | 0.80 | 0.00 | **+0.3993** | vol_conf +2.42; sector_lead +1.93; mom20 +1.83 | vol_stability -0.34; beta -0.28 | `L-TI-BMY`,`L-RM-BMY` |
| BEN | `UNAVAILABLE` | +1.0970 | `UNAVAILABLE` | +0.8420 | +0.4554 | 0.80 | 0.00 | **+0.3643** | vol_conf +1.79; macd +1.68; beta +1.64 | INSUFFICIENT_SOURCEABLE_DRIVERS | `L-TI-BEN`,`L-RM-BEN` |
| BAX | `UNAVAILABLE` | +1.2327 | `UNAVAILABLE` | +0.3485 | +0.4221 | 0.80 | 0.00 | **+0.3377** | sector_lead +1.93; mom60 +1.86; mom20 +1.83 | vol_stability -0.89; rate_sens -0.84 | `L-TI-BAX`,`L-RM-BAX` |
| WTW | `UNAVAILABLE` | +1.1885 | `UNAVAILABLE` | +0.3638 | +0.4111 | 0.80 | 0.00 | **+0.3289** | mom60 +1.86; mom20 +1.83; sector_lead +1.41 | beta -0.57; vol_stability -0.44 | `L-TI-WTW`,`L-RM-WTW` |
| COO | `UNAVAILABLE` | +0.8388 | `UNAVAILABLE` | +0.6774 | +0.3533 | 0.80 | 0.00 | **+0.2826** | sector_lead +1.93; macd +1.68; mom60 +1.33 | beta -0.59 | `L-TI-COO`,`L-RM-COO` |
| BBY | `UNAVAILABLE` | +0.8678 | `UNAVAILABLE` | +0.4710 | +0.3310 | 0.80 | 0.00 | **+0.2648** | vol_stability +2.32; mom60 +1.86; ma_align +1.29 | rate_sens -0.88; sector_lead -0.36; macd -0.20 | `L-TI-BBY`,`L-RM-BBY` |
| FTNT | `UNAVAILABLE` | +0.5854 | `UNAVAILABLE` | +1.0318 | +0.3304 | 0.80 | 0.00 | **+0.2643** | vol_stability +2.32; mom60 +1.86; beta +1.64 | sector_lead -0.94; macd -0.20; mom20 -0.11 | `L-TI-FTNT`,`L-RM-FTNT` |
| ROST | `UNAVAILABLE` | +0.9091 | `UNAVAILABLE` | +0.3448 | +0.3245 | 0.80 | 0.00 | **+0.2596** | mom20 +1.83; macd +1.68; ma_align +1.29 | sector_lead -0.36; vol_conf -0.00 | `L-TI-ROST`,`L-RM-ROST` |
| NTAP | `UNAVAILABLE` | +0.7564 | `UNAVAILABLE` | +0.6338 | +0.3220 | 0.80 | 0.00 | **+0.2576** | vol_stability +2.32; mom60 +1.86; mom20 +1.42 | vol_conf -0.97; sector_lead -0.94; dd60 -0.11 | `L-TI-NTAP`,`L-RM-NTAP` |
| KKR | `UNAVAILABLE` | +0.7839 | `UNAVAILABLE` | +0.5060 | +0.3111 | 0.80 | 0.00 | **+0.2488** | vol_conf +1.69; sector_lead +1.41; beta +1.34 | vol_stability -0.38; rate_sens -0.35 | `L-TI-KKR`,`L-RM-KKR` |
| IQV | `UNAVAILABLE` | +0.9479 | `UNAVAILABLE` | +0.1565 | +0.3078 | 0.80 | 0.00 | **+0.2463** | sector_lead +1.93; mom60 +1.86; mom20 +1.56 | vol_stability -0.73; beta -0.30; rate_sens -0.27 | `L-TI-IQV`,`L-RM-IQV` |
| ARES | `UNAVAILABLE` | +0.8771 | `UNAVAILABLE` | +0.2589 | +0.3020 | 0.80 | 0.00 | **+0.2416** | vol_conf +2.14; mom20 +1.62; sector_lead +1.41 | vol_stability -0.65; dd60 -0.61; rate_sens -0.29 | `L-TI-ARES`,`L-RM-ARES` |
| TGT | `UNAVAILABLE` | +1.0498 | `UNAVAILABLE` | -0.0922 | +0.3011 | 0.80 | 0.00 | **+0.2409** | mom20 +1.83; ma_align +1.29; macd +1.05 | sector_lead -0.36; beta -0.21; rate_sens -0.06 | `L-TI-TGT`,`L-RM-TGT` |
| REGN | `UNAVAILABLE` | +0.5291 | `UNAVAILABLE` | +0.9386 | +0.2995 | 0.80 | 0.00 | **+0.2396** | sector_lead +1.93; mom20 +1.83; macd +1.05 | dd60 -0.22 | `L-TI-REGN`,`L-RM-REGN` |
| ZBRA | `UNAVAILABLE` | +1.0510 | `UNAVAILABLE` | +0.6987 | +0.4201 | 0.80 | 0.10 | **+0.2361** | vol_conf +2.42; mom60 +1.77; vol_stability +1.69 | dd60 -0.20; sector_lead -0.18 | `L-TI-ZBRA`,`L-RM-ZBRA` |
| VEEV | `UNAVAILABLE` | +0.9040 | `UNAVAILABLE` | +0.1409 | +0.2923 | 0.80 | 0.00 | **+0.2339** | vol_conf +2.14; mom60 +1.47; macd +1.05 | sector_lead -0.94; dd60 -0.45 | `L-TI-VEEV`,`L-RM-VEEV` |
| GRMN | `UNAVAILABLE` | +1.0203 | `UNAVAILABLE` | -0.1086 | +0.2898 | 0.80 | 0.00 | **+0.2318** | mom20 +1.83; mom60 +1.70; ma_align +1.29 | vol_stability -1.55; vol_conf -0.62; sector_lead -0.18 | `L-TI-GRMN`,`L-RM-GRMN` |
| MSFT | `UNAVAILABLE` | +0.9667 | `UNAVAILABLE` | -0.0126 | +0.2881 | 0.80 | 0.00 | **+0.2305** | vol_conf +2.42; mom20 +1.83; beta +1.64 | vol_stability -1.40; dd60 -0.96; sector_lead -0.94 | `L-TI-MSFT`,`L-RM-MSFT` |
| PCAR | `UNAVAILABLE` | +0.8621 | `UNAVAILABLE` | +0.1952 | +0.2879 | 0.80 | 0.00 | **+0.2303** | beta +1.64; ma_align +1.29; macd +1.05 | rate_sens -0.52; sector_lead -0.36 | `L-TI-PCAR`,`L-RM-PCAR` |

## Metric availability

| Metric Group | Sourceable Count | UNAVAILABLE Count | DQ / Confidence Effect | Notes |
|---|---|---|---|---|
| Technical / price | 512 | 0 | none | 100% coverage; drives `Tech_Z` |
| Risk / return (beta, TE, vol, DD) | 512 | 0 | none | 100% coverage; drives `Macro_Z`, sigma, Sortino |
| Sizing (Kelly) | 512 | 0 | none | derived from mu / sigma |
| Earnings distance | 512 | 0 | penalty input | complete 28-day forward sweep, 0 transport failures |
| Sector / market cap | 510 | 2 | negligible | Nasdaq screener |
| **Fundamental** | 0 | **512** | **DQ -> 0.80; blocks thresholds 2/3/4** | no universe-scale XBRL path wired |
| **Sentiment / positioning** | 0 | **512** | **DQ -> 0.80; blocks thresholds 2/3/4** | no universe-scale analyst/SI path wired |
| Options IV30 | 0 | 512 | sigma chain falls to step 2 | no options feed |

No score above cites a metric absent from `01_preflight.md`, and **no missing metric is described as
neutral or supportive** — `Fund_Z` and `Sent_Z` are carried as `0.00 (UNAVAILABLE)` in the arithmetic
and reported as `UNAVAILABLE` everywhere else.

## Technical indicator summary (top 20)

| Ticker | TD9 D/W/M | RSI14 D/W/M | MACD State D/W/M | MACD Hist D/W/M | MA Align D/W/M | Mom 20/60 (d) | RS20/RS60 vs SPY | Vol Ratio 20d | Indicator Ledger |
|---|---|---|---|---|---|---|---|---|---|
| DXCM | S5/S4/S2 | 72.6/67.8/53.5 | ABOVE/ABOVE/ABOVE | +1.095/+1.835/+2.988 | BULL/BULL/MIXE | +20.63%/+44.65% | +19.78%/+41.14% | 1.80x | `L-TI-DXCM` |
| BMY | S9/S7/S2 | 71.8/68.5/65.5 | ABOVE/ABOVE/ABOVE | +0.449/+0.641/+1.775 | BULL/BULL/BULL | +15.47%/+17.00% | +14.62%/+13.49% | 2.63x | `L-TI-BMY` |
| BEN | S7/S1/S8 | 66.1/74.3/71.8 | BULL_X/ABOVE/ABOVE | +0.123/+0.178/+1.399 | BULL/BULL/BULL | +2.32%/+14.23% | +1.47%/+10.72% | 1.56x | `L-TI-BEN` |
| BAX | S7/S9/S3 | 76.4/73.6/51.7 | ABOVE/ABOVE/ABOVE | +0.473/+0.989/+1.345 | BULL/MIXE/MIXE | +24.45%/+65.57% | +23.60%/+62.06% | 1.44x | `L-TI-BAX` |
| WTW | S7/S7/S2 | 81.6/68.4/60.8 | ABOVE/ABOVE/BELOW | +4.419/+10.103/-1.842 | BULL/MIXE/BULL | +18.76%/+35.84% | +17.91%/+32.33% | 1.33x | `L-TI-WTW` |
| COO | S5/S1/S2 | 63.3/55.8/46.2 | BULL_X/ABOVE/BULL_X | +0.073/+1.201/+0.148 | BULL/MIXE/BEAR | +2.23%/+21.45% | +1.38%/+17.94% | 1.24x | `L-TI-COO` |
| BBY | B2/S9/S4 | 56.3/65.1/58.9 | BELOW/ABOVE/ABOVE | -0.399/+2.067/+2.041 | BULL/BULL/BULL | +9.29%/+47.19% | +8.44%/+43.68% | 1.20x | `L-TI-BBY` |
| FTNT | S4/S9/S6 | 61.3/77.7/78.4 | BELOW/ABOVE/ABOVE | -0.497/+2.620/+7.979 | BULL/BULL/BULL | +0.53%/+81.45% | -0.32%/+77.94% | 1.08x | `L-TI-FTNT` |
| ROST | S7/S4/S9 | 71.0/69.1/76.4 | ABOVE/BULL_X/ABOVE | +2.307/+0.608/+7.710 | BULL/BULL/BULL | +19.66%/+10.70% | +18.81%/+7.19% | 1.04x | `L-TI-ROST` |
| NTAP | S9/S5/S5 | 68.0/74.3/71.5 | ABOVE/ABOVE/ABOVE | +1.101/+3.407/+7.758 | BULL/BULL/BULL | +12.18%/+64.20% | +11.33%/+60.69% | 0.76x | `L-TI-NTAP` |
| KKR | S1/S6/S3 | 65.8/55.3/49.3 | ABOVE/ABOVE/BELOW | +0.620/+2.102/-4.218 | BULL/MIXE/MIXE | +11.03%/+5.93% | +10.18%/+2.42% | 1.53x | `L-TI-KKR` |
| IQV | B1/S7/S3 | 66.4/66.3/57.0 | ABOVE/ABOVE/ABOVE | +2.258/+7.206/+4.904 | BULL/MIXE/MIXE | +13.30%/+32.24% | +12.45%/+28.73% | 1.12x | `L-TI-IQV` |
| ARES | S2/S3/S3 | 69.3/57.4/51.6 | ABOVE/ABOVE/BELOW | +1.288/+2.876/-4.428 | BULL/MIXE/MIXE | +13.74%/+13.00% | +12.89%/+9.49% | 1.66x | `L-TI-ARES` |
| TGT | S6/S2/S9 | 69.5/68.2/65.0 | ABOVE/ABOVE/ABOVE | +0.865/+1.018/+7.155 | BULL/BULL/MIXE | +18.44%/+15.80% | +17.59%/+12.29% | 1.27x | `L-TI-TGT` |
| REGN | S5/S7/S1 | 76.4/60.4/52.8 | ABOVE/ABOVE/ABOVE | +10.048/+9.677/+11.429 | BULL/MIXE/MIXE | +16.84%/+5.45% | +15.99%/+1.94% | 1.06x | `L-TI-REGN` |
| ZBRA | S6/S7/S4 | 68.0/63.4/50.5 | ABOVE/ABOVE/ABOVE | +2.450/+7.272/+4.292 | BULL/MIXE/MIXE | +7.90%/+26.93% | +7.05%/+23.42% | 1.82x | `L-TI-ZBRA` |
| VEEV | S6/S6/S2 | 63.8/56.8/47.4 | ABOVE/ABOVE/BELOW | +0.746/+7.283/-5.742 | BULL/MIXE/MIXE | +7.42%/+23.24% | +6.57%/+19.73% | 1.66x | `L-TI-VEEV` |
| GRMN | S6/S6/S2 | 79.9/73.1/69.9 | ABOVE/ABOVE/ABOVE | +6.668/+5.465/+5.252 | BULL/BULL/BULL | +24.28%/+26.06% | +23.43%/+22.55% | 0.86x | `L-TI-GRMN` |
| MSFT | S5/S4/S2 | 78.3/64.0/57.0 | ABOVE/ABOVE/BELOW | +10.413/+9.913/-4.491 | BULL/MIXE/BULL | +26.09%/+18.06% | +25.24%/+14.55% | 1.74x | `L-TI-MSFT` |
| PCAR | B2/S9/S2 | 59.7/66.7/66.6 | ABOVE/ABOVE/ABOVE | +0.193/+1.324/+1.743 | BULL/BULL/BULL | +4.88%/+13.70% | +4.03%/+10.19% | 1.23x | `L-TI-PCAR` |

RS20/RS60 are shown as **diagnostics only** — they no longer occupy a `Tech_Z` metric slot.

## Sleeves and thresholds

| Sleeve | Count | Basis |
|---|---|---|
| Ranked total (pctl >= 60) | 205 | mu Calibration Table floor |
| Percentile >= 80 (investable *band*) | 103 | threshold 1 only |
| **Clearing all five Evidence Thresholds** | **0** | thresholds 2, 3 and 4 fail for every name |
| Published prediction records | 24 | first 24 post-penalty ranks, contiguous 1–24 |
| Rejection log (pctl < 60) | 307 | not ranked in either sleeve |

### Why zero names are investable

| Evidence threshold | Result | Reason |
|---|---|---|
| 1. Adjusted-score pctl >= 80th | **PASS** | 103 names qualify |
| 2. >= 3 of 4 factor families non-negative | **FAIL** | `Fund_Z` and `Sent_Z` are `UNAVAILABLE` universe-wide; `rules.md § Family Aggregation` forbids counting an unavailable family toward this threshold, so **at most 2 of 4** can ever qualify |
| 3. No family > 50% of total conviction | **FAIL** | with only Technical (0.30) and Macro (0.15) live, Technical carries 0.30/0.45 = **66.67%** of live conviction for every name |
| 4. Data completeness >= 85% | **FAIL** | DQ multiplier is 0.80 < 0.85 |
| 5. No hard stop from § Stop Criteria | **PASS** | none triggered |

Thresholds 2, 3 and 4 are **arithmetically unsatisfiable** while two of four families have no fetch
path. No amount of price action changes that, which is why every package since 2026-07-01 has been
non-`GO`. The fix is engineering (Phase 2 of the `Fund_Z`/`Sent_Z` plan), not scoring.

## mu assignment

Every `mu` comes from the `rules.md` mu Calibration Table band for the name's percentile; no
per-name adjustment was applied, so no ±2pp reason is owed.

| Pctl band | Prior mu | Names |
|---|---|---|
| >= 95 | +6.0% | 26 |
| 90 – 95 | +5.0% | 26 |
| 85 – 90 | +4.0% | 25 |
| 80 – 85 | +3.0% | 26 |
| 70 – 80 | +2.0% | 51 |
| 60 – 70 | +1.0% | 51 |

## Penalties

| Penalty | Rule | Names affected |
|---|---|---|
| Earnings inside 14 calendar days: `-0.10` | `rules.md § Risk Controls` | **153** of 512 scored (1 inside the published 24) |
| 30d realized vol > 2x sector median | `rules.md § Risk Controls` | 0 — no name breached the multiple |
| `0.25 x Kelly` < 2% NAV | `rules.md § Risk Controls` | 0 of the pctl>=80 pool |

Because the earnings sweep grounds the **entire** universe, ranks are post-penalty and contiguous
1–24 in the published set — there are no ungrounded names to skip, so the "skip ungrounded" rule
retired on 2026-07-29 stays retired.

## Hallucination-prevention checklist

| Check | Result |
|---|---|
| Every numeric `entry_price` has `price_date` + `price_tag` | PASS — all 24, `HISTORICAL`, 2026-08-03 |
| Every numeric metric cites Source Ledger rows | PASS — `L-PX-*`, `L-TI-*`, `L-RM-*`, `L-EA-*` |
| Every `Adj Score` has a full score trace | PASS — shown inline per name |
| Missing metrics marked `UNAVAILABLE`, not neutral | PASS |
| `target_price = entry_price x (1 + mu)` | PASS — re-derived in the verification pass |
| Every sigma has a stated source | PASS — `REALIZED_VOL_30D` |
| No investable name has `price_tag = UNAVAILABLE` | PASS — vacuous, the investable set is empty |
| `mu`/`sigma` derive from the architecture | PASS — mu from the calibration band, sigma from the fallback chain |
| No live-sounding wording without ledger support | PASS |
