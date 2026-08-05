# 05 — Factor Scores — 2026-08-04

Universe **512** scored names · label **`INDEX_UNION_PCTL (n=512)`** ·
basis 2026-08-03 completed close.

## Scoring architecture actually executed

`Adj Score = (0.30*Fund_Z + 0.30*Tech_Z + 0.25*Sent_Z + 0.15*Macro_Z) * DQ - Penalties`

| Family | Weight | State | Sourceable metric slots |
|---|---|---|---|
| Fundamental | 0.30 | **`UNAVAILABLE`** | 0 — contributes `0.00 (UNAVAILABLE)` |
| Technical / Price | 0.30 | `AVAILABLE` | **6** — `mom20`, `mom60`, `ma_align`, `macd`, `vol_conf`, `dd60` |
| Sentiment / Positioning | 0.25 | **`UNAVAILABLE`** | 0 — contributes `0.00 (UNAVAILABLE)` |
| Macro / Regime | 0.15 | `AVAILABLE` | **4** — `beta`, `sector_lead`, `rate_sens`, `vol_stability` |

Each family z-score is the **equal-weighted mean** of its metric z-scores, computed
cross-sectionally over the 512 scored names, per `rules.md § Family Aggregation`.

**Data-quality multiplier = 0.80** ("notable coverage gaps"): two of four families are
unavailable universe-wide. Only two families carry information, so the live score is
`(0.30*Tech_Z + 0.15*Macro_Z) * 0.80` — stated plainly rather than hidden behind a composite.

## Metric Definition Table (normative)

**New this run** — the Track B change accepted in `claude-opus-5-2026-08-03/13_evolution_log.md`,
stamped effective 2026-08-04, is live in this package. This table is **normative**: if it and the
running code disagree, one of them is wrong and the run must say which. Polarity is stated as the
**post-transform direction** — never as an instruction word like "negated" — so a reader can answer
"does a larger raw value help or hurt?" without knowing the sign convention of the stored field.

| Metric slot | Family | Source field | Window | Transform before z-score | Polarity (higher-is-better after transform) | Winsorization |
|---|---|---|---|---|---|---|
| `mom20` | Technical | `technical_indicators.json` `daily.momentum_20d_pct` | trailing 20 daily sessions | none (percent) | **higher raw value is better** | 5th/95th pctl |
| `mom60` | Technical | `daily.momentum_60d_pct` | trailing 60 daily sessions | none (percent) | **higher raw value is better** | 5th/95th pctl |
| `ma_align` | Technical | `daily.ma_alignment` + `weekly.ma_alignment` | daily and weekly blocks | encode `BULLISH=+1, MIXED=0, BEARISH=-1`, then mean of the two | **higher raw value is better** | 5th/95th pctl |
| `macd` | Technical | `daily.macd_state` + `weekly.macd_state` | daily and weekly blocks | encode `BULLISH_CROSS=+2, ABOVE_SIGNAL=+1, ON_SIGNAL=0, BELOW_SIGNAL=-1, BEARISH_CROSS=-2`, then mean of the two | **higher raw value is better** | 5th/95th pctl |
| `vol_conf` | Technical | `daily.volume_ratio_20d` | trailing 20 daily sessions | none (ratio) | **higher raw value is better** | 5th/95th pctl |
| `dd60` | Technical | worst peak-to-trough of adjusted closes | the **61 most recent daily closes** (= the 60 most recent daily return intervals) | none — the field is **already stored as a signed negative number** (e.g. `-0.1386` for a 13.86% drawdown) | **higher raw value is better** (a shallower, i.e. less negative, drawdown scores higher). Do **not** apply a negation. | 5th/95th pctl |
| `beta` | Macro | regression slope of daily adjusted returns vs SPY | trailing 60 daily return intervals; `cov(r, r_SPY, ddof=0) / var(r_SPY)` | `-abs(beta - 1.0)` | **higher transformed value is better** (beta closest to 1.0 scores highest) | 5th/95th pctl |
| `sector_lead` | Macro | `daily.momentum_60d_pct` of every scored member of the name's sector | trailing 60 daily sessions | **median** across the sector's members, then broadcast to each member (so it is constant within a sector) | **higher transformed value is better** | 5th/95th pctl |
| `rate_sens` | Macro | regression slope of daily adjusted returns vs **TLT** | trailing 60 daily return intervals; `cov(r, r_TLT, ddof=0) / var(r_TLT)` | `-abs(beta_TLT)` | **higher transformed value is better** (lower absolute rate sensitivity scores higher) | 5th/95th pctl |
| `vol_stability` | Macro | daily adjusted returns | `vol30` = **population** stdev (`ddof=0`) of the trailing 30 daily returns × `sqrt(21)`; `vol60` = population stdev of the trailing 60 daily returns × `sqrt(21)` | `-(vol30 / vol60)` | **higher transformed value is better** (vol contracting relative to its own 60-day base scores higher) | 5th/95th pctl |

**Shared conventions, stated once:**

- **Input basis.** Every metric above is computed from **adjusted** closes (Track B 2026-07-26).
  Entry, target and CI prices use **raw** closes. `technical_indicators.py` is fed the adjusted tree.
- **z-score.** Winsorize the raw (post-transform) cross-section at the 5th and 95th percentiles by
  clipping, then subtract the mean and divide by the **population** standard deviation (`ddof=0`) *of
  the clipped series*. Negating before or after this transform is arithmetically identical, because
  clipping is symmetric under negation.
- **Family aggregation.** Equal-weighted arithmetic mean of the family's slot z-scores.
- **Relative strength is not a slot.** `rs20`/`rs60` are computed, displayed and ledgered as
  diagnostics only (Track B effective 2026-08-03, now codified in `rules.md`).

## Same-basis reproduction check — the falsifiability test this change owes

This run shares the 2026-08-03 basis with `claude-opus-5-2026-08-03` and scores an **identical
512-name universe** (same 3 rejections: BF-B, FDXF, Q), so any difference in `Tech_Z` or
`Macro_Z` is **definitional, not compositional**. That makes it the exact test the 2026-08-03 log
specified: rebuild from the prior `05` alone and report the max absolute error against **0.01**.

| Quantity | Max abs error | Mean abs error | Threshold | Result |
|---|---|---|---|---|
| `Tech_Z` | **0.0001** | 0.0001 | 0.01 | **PASS** |
| `Macro_Z` | **0.0487** | 0.0176 | 0.01 | **FAIL** |

Per-slot error against the prior package's published driver z-scores:

| Metric slot | Names compared | Max abs error | Mean abs error | Verdict |
|---|---|---|---|---|
| `rate_sens` | 7 | 0.1951 | 0.1054 | **not reproduced** |
| `sector_lead` | 19 | 0.0060 | 0.0039 | reproduced |
| `vol_conf` | 11 | 0.0050 | 0.0023 | reproduced |
| `mom20` | 12 | 0.0049 | 0.0033 | reproduced |
| `vol_stability` | 13 | 0.0047 | 0.0022 | reproduced |
| `ma_align` | 5 | 0.0045 | 0.0045 | reproduced |
| `beta` | 10 | 0.0044 | 0.0015 | reproduced |
| `macd` | 9 | 0.0042 | 0.0020 | reproduced |
| `dd60` | 6 | 0.0042 | 0.0023 | reproduced |
| `mom60` | 11 | 0.0035 | 0.0015 | reproduced |

**Reading of this result.** `Tech_Z` reproduces to 0.0001 — effectively exact.
`Macro_Z` fails, and the failure is **isolated to a single slot**: `rate_sens` at
0.1951, while every other Macro slot lands at ≤
0.0060. Two conventions were pinned by
fitting the prior package's own published driver values:

1. **`dd60` window** — the prior engine used the **61 most recent closes** (60 return intervals), not
   60 closes. Fitted max error 0.0042 versus 0.0292 on 60 closes. This run adopts 61 closes so the
   published series stays continuous, and the table above states it explicitly. Adopting it moved
   `Tech_Z` reproduction from 0.0120 to 0.0001.
2. **`rate_sens`** — **not pinned.** Thirteen plausible conventions were tested (`beta` vs
   `correlation`; 30/60/120/252-day windows; adjusted vs raw closes; negate-before vs negate-after).
   The best fit remains this run's definition at max error 0.1951; none
   reached 0.01. The prior disclosure simply does not determine the convention.

This is exactly the defect the change was written to fix, now measured precisely instead of estimated
— and it is the strongest possible evidence *for* the table rather than against it. The honest scope
note is that the test above evaluates the **prior package's prose**, since the table did not yet
exist when that package was written. The table's own test is owed by the **next run that shares a
basis with this one**, which can rebuild from the section above and should reach ≤0.01 on both
families, `rate_sens` included.

## Calibration feedback binding (read before scoring)

From `02 § 0`: weighted-mean rank IC **-0.0879** over n=515 settled `EQUITY_ALPHA` records,
non-positive in **20 of 32** vintages.
`agents.md § Calibration Feedback Binding` therefore **caps all confidence at `MEDIUM`**, applied to
every record in this package. CI coverage is 69.90% (inside 55–85%), so the
wider-sigma rule does **not** trigger and sigma stays `REALIZED_VOL_30D`.

## Ranked candidates (top 20 of 205 ranked)

| Rank | Ticker | Company | Entry | Price Date | Tag | Adj Score | Score Trace | Pctl | Beta | 30d RVol | Sharpe | Sortino | IR | Kelly 0.25 | VaR95 | CVaR95 | Max DD60 | TD9 D/W/M | RSI14 D/W/M | MACD D/W/M | Days to Earn | mu | sigma | Sigma Source | Target | Target Date | 70% CI Lo | 70% CI Hi | Ledger | Metric Ledger | Conf | Primary Thesis | Key Risk |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **DXCM** | DexCom Inc. Common Stock | 87.31 | 2026-08-03 | `HISTORICAL` | **+0.4319** | `(0.3*0.00(UA) + 0.3*+1.4253 + 0.25*0.00(UA) + 0.15*+0.7489) * 0.80 - 0.00 = +0.4319` | 100.00 | +0.205 | 15.33% | 0.371 | 0.892 | 0.394 | 63.79% | -19.30% | -25.59% | -13.86% | S5/S4/S2 | 72.6/67.8/53.5 | ABOVE/ABOVE/ABOVE | none in 28d sweep | +6.0% | 15.33% | `REALIZED_VOL_30D` | 92.55 | 2026-09-01 | 78.62 | 106.47 | `L-PX-DXCM` | `L-TI-DXCM`,`L-RM-DXCM`,`L-EA-DXCM` | MEDIUM | Health Care name on the deduplicated Tech_Z (`INFERRED`) | rank-order inversion risk (see § Calibration) |
| 2 | **BMY** | Bristol-Myers Squibb Company | 65.47 | 2026-08-03 | `HISTORICAL` | **+0.3993** | `(0.3*0.00(UA) + 0.3*+1.3624 + 0.25*0.00(UA) + 0.15*+0.6030) * 0.80 - 0.00 = +0.3993` | 99.80 | -0.203 | 8.67% | 0.656 | 1.156 | 0.781 | 199.73% | -8.30% | -11.85% | -9.32% | S9/S7/S2 | 71.8/68.5/65.5 | ABOVE/ABOVE/ABOVE | none in 28d sweep | +6.0% | 8.67% | `REALIZED_VOL_30D` | 69.40 | 2026-09-01 | 63.50 | 75.30 | `L-PX-BMY` | `L-TI-BMY`,`L-RM-BMY`,`L-EA-BMY` | MEDIUM | Health Care name on the deduplicated Tech_Z (`INFERRED`) | rank-order inversion risk (see § Calibration) |
| 3 | **BEN** | Franklin Resources Inc. Comm | 35.24 | 2026-08-03 | `HISTORICAL` | **+0.3616** | `(0.3*0.00(UA) + 0.3*+1.0970 + 0.25*0.00(UA) + 0.15*+0.8196) * 0.80 - 0.00 = +0.3616` | 99.61 | +1.095 | 8.12% | 0.700 | 1.098 | 0.557 | 227.30% | -7.40% | -10.73% | -6.42% | S7/S1/S8 | 66.1/74.3/71.8 | BULL_X/ABOVE/ABOVE | none in 28d sweep | +6.0% | 8.12% | `REALIZED_VOL_30D` | 37.35 | 2026-09-01 | 34.38 | 40.33 | `L-PX-BEN` | `L-TI-BEN`,`L-RM-BEN`,`L-EA-BEN` | MEDIUM | Finance name on the deduplicated Tech_Z (`INFERRED`) | rank-order inversion risk (see § Calibration) |
| 4 | **BAX** | Baxter International Inc. Co | 28.10 | 2026-08-03 | `HISTORICAL` | **+0.3335** | `(0.3*0.00(UA) + 0.3*+1.2327 + 0.25*0.00(UA) + 0.15*+0.3136) * 0.80 - 0.00 = +0.3335` | 99.41 | +0.644 | 14.23% | 0.400 | 0.930 | 0.380 | 74.07% | -17.48% | -23.32% | -7.19% | S7/S9/S3 | 76.4/73.6/51.7 | ABOVE/ABOVE/ABOVE | none in 28d sweep | +6.0% | 14.23% | `REALIZED_VOL_30D` | 29.79 | 2026-09-01 | 25.63 | 33.94 | `L-PX-BAX` | `L-TI-BAX`,`L-RM-BAX`,`L-EA-BAX` | MEDIUM | Health Care name on the deduplicated Tech_Z (`INFERRED`) | rank-order inversion risk (see § Calibration) |
| 5 | **WTW** | Willis Towers Watson Public  | 341.63 | 2026-08-03 | `HISTORICAL` | **+0.3279** | `(0.3*0.00(UA) + 0.3*+1.1885 + 0.25*0.00(UA) + 0.15*+0.3555) * 0.80 - 0.00 = +0.3279` | 99.22 | -0.367 | 9.85% | 0.578 | 1.911 | 0.738 | 154.71% | -10.25% | -14.28% | -6.18% | S7/S7/S2 | 81.6/68.4/60.8 | ABOVE/ABOVE/BELOW | none in 28d sweep | +6.0% | 9.85% | `REALIZED_VOL_30D` | 362.13 | 2026-09-01 | 327.14 | 397.11 | `L-PX-WTW` | `L-TI-WTW`,`L-RM-WTW`,`L-EA-WTW` | MEDIUM | Finance name on the deduplicated Tech_Z (`INFERRED`) | rank-order inversion risk (see § Calibration) |
| 6 | **COO** | The Cooper Companies Inc. Co | 74.23 | 2026-08-03 | `HISTORICAL` | **+0.2807** | `(0.3*0.00(UA) + 0.3*+0.8387 + 0.25*0.00(UA) + 0.15*+0.6620) * 0.80 - 0.00 = +0.2807` | 99.02 | -0.380 | 8.75% | 0.650 | 1.093 | 0.737 | 195.83% | -8.44% | -12.03% | -7.67% | S5/S1/S2 | 63.3/55.8/46.2 | BULL_X/ABOVE/BULL_X | 36 | +6.0% | 8.75% | `REALIZED_VOL_30D` | 78.68 | 2026-09-01 | 71.93 | 85.44 | `L-PX-COO` | `L-TI-COO`,`L-RM-COO`,`L-EA-COO` | MEDIUM | Health Care name on the deduplicated Tech_Z (`INFERRED`) | rank-order inversion risk (see § Calibration) |
| 7 | **BBY** | Best Buy Co. Inc. Common Sto | 85.25 | 2026-08-03 | `HISTORICAL` | **+0.2682** | `(0.3*0.00(UA) + 0.3*+0.8677 + 0.25*0.00(UA) + 0.15*+0.4994) * 0.80 - 0.00 = +0.2682` | 98.83 | +0.421 | 8.14% | 0.699 | 1.341 | 0.401 | 226.45% | -7.43% | -10.77% | -8.93% | B2/S9/S4 | 56.3/65.1/58.9 | BELOW/ABOVE/ABOVE | 23 | +6.0% | 8.14% | `REALIZED_VOL_30D` | 90.37 | 2026-09-01 | 83.15 | 97.58 | `L-PX-BBY` | `L-TI-BBY`,`L-RM-BBY`,`L-EA-BBY` | MEDIUM | Consumer Discretionary name on the deduplicated Tech_Z (`INFERRED`) | rank-order inversion risk (see § Calibration) |
| 8 | **FTNT** | Fortinet Inc. Common Stock | 163.21 | 2026-08-03 | `HISTORICAL` | **+0.2642** | `(0.3*0.00(UA) + 0.3*+0.5853 + 0.25*0.00(UA) + 0.15*+1.0311) * 0.80 - 0.00 = +0.2642` | 98.63 | +0.968 | 10.70% | 0.531 | 1.713 | 0.257 | 130.99% | -11.66% | -16.04% | -10.10% | S4/S9/S6 | 61.3/77.7/78.4 | BELOW/ABOVE/ABOVE | none in 28d sweep | +6.0% | 10.70% | `REALIZED_VOL_30D` | 173.00 | 2026-09-01 | 154.84 | 191.17 | `L-PX-FTNT` | `L-TI-FTNT`,`L-RM-FTNT`,`L-EA-FTNT` | MEDIUM | Technology name on the deduplicated Tech_Z (`INFERRED`) | rank-order inversion risk (see § Calibration) |
| 9 | **ROST** | Ross Stores Inc. Common Stoc | 252.91 | 2026-08-03 | `HISTORICAL` | **+0.2598** | `(0.3*0.00(UA) + 0.3*+0.9090 + 0.25*0.00(UA) + 0.15*+0.3469) * 0.80 - 0.00 = +0.2598` | 98.43 | +0.219 | 8.84% | 0.643 | 0.755 | 0.564 | 191.85% | -8.59% | -12.22% | -13.03% | S7/S4/S9 | 71.0/69.1/76.4 | ABOVE/BULL_X/ABOVE | 16 | +6.0% | 8.84% | `REALIZED_VOL_30D` | 268.08 | 2026-09-01 | 244.83 | 291.34 | `L-PX-ROST` | `L-TI-ROST`,`L-RM-ROST`,`L-EA-ROST` | MEDIUM | Consumer Discretionary name on the deduplicated Tech_Z (`INFERRED`) | rank-order inversion risk (see § Calibration) |
| 10 | **NTAP** | NetApp Inc. Common Stock | 182.92 | 2026-08-03 | `HISTORICAL` | **+0.2572** | `(0.3*0.00(UA) + 0.3*+0.7563 + 0.25*0.00(UA) + 0.15*+0.6306) * 0.80 - 0.00 = +0.2572` | 98.24 | +1.439 | 12.08% | 0.471 | 0.756 | 0.176 | 102.71% | -13.94% | -18.89% | -15.81% | S9/S5/S5 | 68.0/74.3/71.5 | ABOVE/ABOVE/ABOVE | 22 | +6.0% | 12.08% | `REALIZED_VOL_30D` | 193.90 | 2026-09-01 | 170.91 | 216.89 | `L-PX-NTAP` | `L-TI-NTAP`,`L-RM-NTAP`,`L-EA-NTAP` | MEDIUM | Technology name on the deduplicated Tech_Z (`INFERRED`) | rank-order inversion risk (see § Calibration) |
| 11 | **IQV** | IQVIA Holdings Inc. Common S | 233.36 | 2026-08-03 | `HISTORICAL` | **+0.2484** | `(0.3*0.00(UA) + 0.3*+0.9478 + 0.25*0.00(UA) + 0.15*+0.1746) * 0.80 - 0.00 = +0.2484` | 98.04 | -0.211 | 15.39% | 0.369 | 1.226 | 0.461 | 63.29% | -19.40% | -25.71% | -10.23% | B1/S7/S3 | 66.4/66.3/57.0 | ABOVE/ABOVE/ABOVE | none in 28d sweep | +6.0% | 15.39% | `REALIZED_VOL_30D` | 247.36 | 2026-09-01 | 210.00 | 284.72 | `L-PX-IQV` | `L-TI-IQV`,`L-RM-IQV`,`L-EA-IQV` | MEDIUM | Health Care name on the deduplicated Tech_Z (`INFERRED`) | rank-order inversion risk (see § Calibration) |
| 12 | **KKR** | KKR & Co. Inc. Common Stock | 106.56 | 2026-08-03 | `HISTORICAL` | **+0.2457** | `(0.3*0.00(UA) + 0.3*+0.7839 + 0.25*0.00(UA) + 0.15*+0.4798) * 0.80 - 0.00 = +0.2457` | 97.85 | +1.273 | 10.42% | 0.546 | 1.026 | 0.409 | 138.26% | -11.19% | -15.46% | -13.08% | S1/S6/S3 | 65.8/55.3/49.3 | ABOVE/ABOVE/BELOW | none in 28d sweep | +6.0% | 10.42% | `REALIZED_VOL_30D` | 112.95 | 2026-09-01 | 101.41 | 124.50 | `L-PX-KKR` | `L-TI-KKR`,`L-RM-KKR`,`L-EA-KKR` | MEDIUM | Finance name on the deduplicated Tech_Z (`INFERRED`) | rank-order inversion risk (see § Calibration) |
| 13 | **REGN** | Regeneron Pharmaceuticals In | 759.24 | 2026-08-03 | `HISTORICAL` | **+0.2406** | `(0.3*0.00(UA) + 0.3*+0.5290 + 0.25*0.00(UA) + 0.15*+0.9472) * 0.80 - 0.00 = +0.2406` | 97.65 | +0.320 | 9.40% | 0.605 | 1.341 | 0.521 | 169.92% | -9.50% | -13.36% | -16.84% | S5/S7/S1 | 76.4/60.4/52.8 | ABOVE/ABOVE/ABOVE | none in 28d sweep | +6.0% | 9.40% | `REALIZED_VOL_30D` | 804.79 | 2026-09-01 | 730.61 | 878.98 | `L-PX-REGN` | `L-TI-REGN`,`L-RM-REGN`,`L-EA-REGN` | MEDIUM | Health Care name on the deduplicated Tech_Z (`INFERRED`) | rank-order inversion risk (see § Calibration) |
| 14 | **TGT** | Target Corporation Common St | 149.35 | 2026-08-03 | `HISTORICAL` | **+0.2392** | `(0.3*0.00(UA) + 0.3*+1.0498 + 0.25*0.00(UA) + 0.15*-0.1059) * 0.80 - 0.00 = +0.2392` | 97.46 | -0.164 | 10.03% | 0.567 | 0.973 | 0.617 | 149.12% | -10.55% | -14.66% | -10.69% | S6/S2/S9 | 69.5/68.2/65.0 | ABOVE/ABOVE/ABOVE | 15 | +6.0% | 10.03% | `REALIZED_VOL_30D` | 158.31 | 2026-09-01 | 142.73 | 173.89 | `L-PX-TGT` | `L-TI-TGT`,`L-RM-TGT`,`L-EA-TGT` | MEDIUM | Consumer Discretionary name on the deduplicated Tech_Z (`INFERRED`) | rank-order inversion risk (see § Calibration) |
| 15 | **ZBRA** | Zebra Technologies Corporati | 291.64 | 2026-08-03 | `HISTORICAL` | **+0.2381** | `(0.3*0.00(UA) + 0.3*+1.0511 + 0.25*0.00(UA) + 0.15*+0.7149) * 0.80 - 0.10 = +0.2381` | 97.26 | +1.396 | 11.19% | 0.508 | 1.285 | 0.247 | 119.83% | -12.46% | -17.05% | -16.64% | S6/S7/S4 | 68.0/63.4/50.5 | ABOVE/ABOVE/ABOVE | 0 | +6.0% | 11.19% | `REALIZED_VOL_30D` | 309.14 | 2026-09-01 | 275.20 | 343.07 | `L-PX-ZBRA` | `L-TI-ZBRA`,`L-RM-ZBRA`,`L-EA-ZBRA` | LOW | Industrials name on the deduplicated Tech_Z (`INFERRED`) | prints in 0d — penalised, confidence capped |
| 16 | **ARES** | Ares Management Corporation  | 138.57 | 2026-08-03 | `HISTORICAL` | **+0.2357** | `(0.3*0.00(UA) + 0.3*+0.8771 + 0.25*0.00(UA) + 0.15*+0.2102) * 0.80 - 0.00 = +0.2357` | 97.06 | +1.722 | 13.46% | 0.423 | 0.816 | 0.249 | 82.80% | -16.21% | -21.73% | -20.28% | S2/S3/S3 | 69.3/57.4/51.6 | ABOVE/ABOVE/BELOW | none in 28d sweep | +6.0% | 13.46% | `REALIZED_VOL_30D` | 146.88 | 2026-09-01 | 127.49 | 166.28 | `L-PX-ARES` | `L-TI-ARES`,`L-RM-ARES`,`L-EA-ARES` | MEDIUM | Finance name on the deduplicated Tech_Z (`INFERRED`) | rank-order inversion risk (see § Calibration) |
| 17 | **MSFT** | Microsoft Corporation Common | 487.65 | 2026-08-03 | `HISTORICAL` | **+0.2351** | `(0.3*0.00(UA) + 0.3*+0.9667 + 0.25*0.00(UA) + 0.15*+0.0259) * 0.80 - 0.00 = +0.2351` | 96.87 | +1.066 | 16.05% | 0.354 | 1.521 | 0.301 | 58.20% | -20.49% | -27.07% | -23.38% | S5/S4/S2 | 78.3/64.0/57.0 | ABOVE/ABOVE/BELOW | none in 28d sweep | +6.0% | 16.05% | `REALIZED_VOL_30D` | 516.91 | 2026-09-01 | 435.49 | 598.33 | `L-PX-MSFT` | `L-TI-MSFT`,`L-RM-MSFT`,`L-EA-MSFT` | MEDIUM | Technology name on the deduplicated Tech_Z (`INFERRED`) | rank-order inversion risk (see § Calibration) |
| 18 | **GRMN** | Garmin Ltd. Common Stock (Sw | 304.76 | 2026-08-03 | `HISTORICAL` | **+0.2350** | `(0.3*0.00(UA) + 0.3*+1.0202 + 0.25*0.00(UA) + 0.15*-0.0819) * 0.80 - 0.00 = +0.2350` | 96.67 | +0.173 | 15.28% | 0.372 | 1.365 | 0.462 | 64.23% | -19.21% | -25.48% | -7.03% | S6/S6/S2 | 79.9/73.1/69.9 | ABOVE/ABOVE/ABOVE | none in 28d sweep | +6.0% | 15.28% | `REALIZED_VOL_30D` | 323.05 | 2026-09-01 | 274.61 | 371.48 | `L-PX-GRMN` | `L-TI-GRMN`,`L-RM-GRMN`,`L-EA-GRMN` | MEDIUM | Industrials name on the deduplicated Tech_Z (`INFERRED`) | rank-order inversion risk (see § Calibration) |
| 19 | **VEEV** | Veeva Systems Inc. Class A C | 206.25 | 2026-08-03 | `HISTORICAL` | **+0.2334** | `(0.3*0.00(UA) + 0.3*+0.9041 + 0.25*0.00(UA) + 0.15*+0.1367) * 0.80 - 0.00 = +0.2334` | 96.48 | -0.004 | 12.76% | 0.446 | 1.061 | 0.451 | 92.10% | -15.06% | -20.29% | -18.82% | S6/S6/S2 | 63.8/56.8/47.4 | ABOVE/ABOVE/BELOW | 22 | +6.0% | 12.76% | `REALIZED_VOL_30D` | 218.62 | 2026-09-01 | 191.25 | 246.00 | `L-PX-VEEV` | `L-TI-VEEV`,`L-RM-VEEV`,`L-EA-VEEV` | MEDIUM | Technology name on the deduplicated Tech_Z (`INFERRED`) | rank-order inversion risk (see § Calibration) |
| 20 | **PCAR** | PACCAR Inc. Common Stock | 132.06 | 2026-08-03 | `HISTORICAL` | **+0.2324** | `(0.3*0.00(UA) + 0.3*+0.8620 + 0.25*0.00(UA) + 0.15*+0.2126) * 0.80 - 0.00 = +0.2324` | 96.28 | +1.034 | 8.90% | 0.639 | 1.440 | 0.502 | 189.46% | -8.68% | -12.33% | -5.86% | B2/S9/S2 | 59.7/66.7/66.6 | ABOVE/ABOVE/ABOVE | none in 28d sweep | +6.0% | 8.90% | `REALIZED_VOL_30D` | 139.98 | 2026-09-01 | 127.76 | 152.20 | `L-PX-PCAR` | `L-TI-PCAR`,`L-RM-PCAR`,`L-EA-PCAR` | MEDIUM | Consumer Discretionary name on the deduplicated Tech_Z (`INFERRED`) | rank-order inversion risk (see § Calibration) |

## Score attribution — all 24 published names

`rules.md § Financial Metrics and Score Attribution` requires an `Adj Score` explanation for every
**ranked or monitored** equity, so this table spans all 24 names carrying a prediction
record — not just the top 20 shown in the ranked-candidate schema above.

| Ticker | Fund_Z | Tech_Z | Sent_Z | Macro_Z | Composite_Z | DQ | Penalties | Adj Score | Top Positive Drivers | Top Negative Drivers | Metric Ledger |
|---|---|---|---|---|---|---|---|---|---|---|---|
| DXCM | `UNAVAILABLE` | +1.4253 | `UNAVAILABLE` | +0.7489 | +0.5399 | 0.80 | 0.00 | **+0.4319** | vol_conf +2.42; sector_lead +1.93; mom60 +1.86 | vol_stability -0.55 | `L-TI-DXCM`,`L-RM-DXCM` |
| BMY | `UNAVAILABLE` | +1.3624 | `UNAVAILABLE` | +0.6030 | +0.4992 | 0.80 | 0.00 | **+0.3993** | vol_conf +2.42; sector_lead +1.93; mom20 +1.83 | vol_stability -0.34; beta -0.28 | `L-TI-BMY`,`L-RM-BMY` |
| BEN | `UNAVAILABLE` | +1.0970 | `UNAVAILABLE` | +0.8196 | +0.4521 | 0.80 | 0.00 | **+0.3616** | vol_conf +1.80; macd +1.68; beta +1.64 | INSUFFICIENT_SOURCEABLE_DRIVERS | `L-TI-BEN`,`L-RM-BEN` |
| BAX | `UNAVAILABLE` | +1.2327 | `UNAVAILABLE` | +0.3136 | +0.4169 | 0.80 | 0.00 | **+0.3335** | sector_lead +1.93; mom60 +1.86; mom20 +1.83 | rate_sens -0.98; vol_stability -0.89 | `L-TI-BAX`,`L-RM-BAX` |
| WTW | `UNAVAILABLE` | +1.1885 | `UNAVAILABLE` | +0.3555 | +0.4099 | 0.80 | 0.00 | **+0.3279** | mom60 +1.86; mom20 +1.83; sector_lead +1.42 | beta -0.57; vol_stability -0.44 | `L-TI-WTW`,`L-RM-WTW` |
| COO | `UNAVAILABLE` | +0.8387 | `UNAVAILABLE` | +0.6620 | +0.3509 | 0.80 | 0.00 | **+0.2807** | sector_lead +1.93; macd +1.68; mom60 +1.33 | beta -0.59 | `L-TI-COO`,`L-RM-COO` |
| BBY | `UNAVAILABLE` | +0.8677 | `UNAVAILABLE` | +0.4994 | +0.3352 | 0.80 | 0.00 | **+0.2682** | vol_stability +2.32; mom60 +1.86; ma_align +1.29 | rate_sens -0.78; sector_lead -0.35; macd -0.20 | `L-TI-BBY`,`L-RM-BBY` |
| FTNT | `UNAVAILABLE` | +0.5853 | `UNAVAILABLE` | +1.0311 | +0.3303 | 0.80 | 0.00 | **+0.2642** | vol_stability +2.32; mom60 +1.86; beta +1.64 | sector_lead -0.94; macd -0.20; mom20 -0.11 | `L-TI-FTNT`,`L-RM-FTNT` |
| ROST | `UNAVAILABLE` | +0.9090 | `UNAVAILABLE` | +0.3469 | +0.3247 | 0.80 | 0.00 | **+0.2598** | mom20 +1.83; macd +1.68; ma_align +1.29 | sector_lead -0.35; vol_conf -0.00 | `L-TI-ROST`,`L-RM-ROST` |
| NTAP | `UNAVAILABLE` | +0.7563 | `UNAVAILABLE` | +0.6306 | +0.3215 | 0.80 | 0.00 | **+0.2572** | vol_stability +2.32; mom60 +1.86; mom20 +1.42 | vol_conf -0.97; sector_lead -0.94; dd60 -0.11 | `L-TI-NTAP`,`L-RM-NTAP` |
| IQV | `UNAVAILABLE` | +0.9478 | `UNAVAILABLE` | +0.1746 | +0.3105 | 0.80 | 0.00 | **+0.2484** | sector_lead +1.93; mom60 +1.86; mom20 +1.56 | vol_stability -0.73; beta -0.30; rate_sens -0.20 | `L-TI-IQV`,`L-RM-IQV` |
| KKR | `UNAVAILABLE` | +0.7839 | `UNAVAILABLE` | +0.4798 | +0.3071 | 0.80 | 0.00 | **+0.2457** | vol_conf +1.69; sector_lead +1.42; beta +1.34 | rate_sens -0.46; vol_stability -0.38 | `L-TI-KKR`,`L-RM-KKR` |
| REGN | `UNAVAILABLE` | +0.5290 | `UNAVAILABLE` | +0.9472 | +0.3008 | 0.80 | 0.00 | **+0.2406** | sector_lead +1.93; mom20 +1.83; macd +1.05 | dd60 -0.22 | `L-TI-REGN`,`L-RM-REGN` |
| TGT | `UNAVAILABLE` | +1.0498 | `UNAVAILABLE` | -0.1059 | +0.2991 | 0.80 | 0.00 | **+0.2392** | mom20 +1.83; ma_align +1.29; macd +1.05 | sector_lead -0.35; beta -0.21; rate_sens -0.12 | `L-TI-TGT`,`L-RM-TGT` |
| ZBRA | `UNAVAILABLE` | +1.0511 | `UNAVAILABLE` | +0.7149 | +0.4226 | 0.80 | 0.10 | **+0.2381** | vol_conf +2.42; mom60 +1.77; vol_stability +1.69 | dd60 -0.20; sector_lead -0.17 | `L-TI-ZBRA`,`L-RM-ZBRA` |
| ARES | `UNAVAILABLE` | +0.8771 | `UNAVAILABLE` | +0.2102 | +0.2947 | 0.80 | 0.00 | **+0.2357** | vol_conf +2.14; mom20 +1.62; sector_lead +1.42 | vol_stability -0.65; dd60 -0.61; rate_sens -0.49 | `L-TI-ARES`,`L-RM-ARES` |
| MSFT | `UNAVAILABLE` | +0.9667 | `UNAVAILABLE` | +0.0259 | +0.2939 | 0.80 | 0.00 | **+0.2351** | vol_conf +2.42; mom20 +1.83; beta +1.64 | vol_stability -1.40; dd60 -0.96; sector_lead -0.94 | `L-TI-MSFT`,`L-RM-MSFT` |
| GRMN | `UNAVAILABLE` | +1.0202 | `UNAVAILABLE` | -0.0819 | +0.2938 | 0.80 | 0.00 | **+0.2350** | mom20 +1.83; mom60 +1.70; ma_align +1.29 | vol_stability -1.55; vol_conf -0.62; sector_lead -0.17 | `L-TI-GRMN`,`L-RM-GRMN` |
| VEEV | `UNAVAILABLE` | +0.9041 | `UNAVAILABLE` | +0.1367 | +0.2917 | 0.80 | 0.00 | **+0.2334** | vol_conf +2.14; mom60 +1.47; macd +1.05 | sector_lead -0.94; dd60 -0.45 | `L-TI-VEEV`,`L-RM-VEEV` |
| PCAR | `UNAVAILABLE` | +0.8620 | `UNAVAILABLE` | +0.2126 | +0.2905 | 0.80 | 0.00 | **+0.2324** | beta +1.64; ma_align +1.29; macd +1.05 | rate_sens -0.45; sector_lead -0.35 | `L-TI-PCAR`,`L-RM-PCAR` |
| LH | `UNAVAILABLE` | +0.8202 | `UNAVAILABLE` | +0.2744 | +0.2872 | 0.80 | 0.00 | **+0.2298** | sector_lead +1.93; ma_align +1.29; mom60 +1.21 | vol_stability -0.84; vol_conf -0.49; beta -0.11 | `L-TI-LH`,`L-RM-LH` |
| COF | `UNAVAILABLE` | +0.6323 | `UNAVAILABLE` | +0.6141 | +0.2818 | 0.80 | 0.00 | **+0.2255** | macd +1.68; beta +1.64; sector_lead +1.42 | rate_sens -0.77; vol_conf -0.28 | `L-TI-COF`,`L-RM-COF` |
| HIG | `UNAVAILABLE` | +0.7213 | `UNAVAILABLE` | +0.3871 | +0.2745 | 0.80 | 0.00 | **+0.2196** | sector_lead +1.42; ma_align +1.29; rate_sens +1.07 | beta -1.02 | `L-TI-HIG`,`L-RM-HIG` |
| WSM | `UNAVAILABLE` | +0.8938 | `UNAVAILABLE` | +0.0258 | +0.2720 | 0.80 | 0.00 | **+0.2176** | mom60 +1.86; beta +1.60; ma_align +1.29 | rate_sens -2.24; sector_lead -0.35; vol_conf -0.21 | `L-TI-WSM`,`L-RM-WSM` |

## Metric availability

| Metric Group | Sourceable Count | `UNAVAILABLE` Count | DQ / Confidence Effect | Notes |
|---|---|---|---|---|
| Technical / price | 512 | 0 | none | 100% coverage; drives `Tech_Z` |
| Risk / return (beta, TE, vol, DD) | 512 | 0 | none | 100% coverage; drives `Macro_Z`, sigma, Sortino |
| Sizing (Kelly) | 512 | 0 | none | derived from mu / sigma |
| Earnings distance | 512 | 0 | penalty input | complete 28-day forward sweep, 0 transport failures |
| Sector / market cap | 512 | 0 | none | Nasdaq screener; the 2 vendor gaps were rejected pre-scoring |
| **Fundamental** | 0 | 512 | **DQ → 0.80; blocks thresholds 2/3/4** | no universe-scale XBRL path wired |
| **Sentiment / positioning** | 0 | 512 | **DQ → 0.80; blocks thresholds 2/3/4** | no universe-scale analyst/SI path wired |
| Options IV30 | 0 | 512 | sigma chain falls to step 2 | no options feed |

No score above cites a metric absent from `01_preflight.md`, and **no missing metric is described as
neutral or supportive** — `Fund_Z` and `Sent_Z` are carried as `0.00 (UNAVAILABLE)` in the arithmetic
and reported as `UNAVAILABLE` everywhere else.

## Technical indicator summary — all 24 published names

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
| IQV | B1/S7/S3 | 66.4/66.3/57.0 | ABOVE/ABOVE/ABOVE | +2.258/+7.206/+4.904 | BULL/MIXE/MIXE | +13.30%/+32.24% | +12.45%/+28.73% | 1.12x | `L-TI-IQV` |
| KKR | S1/S6/S3 | 65.8/55.3/49.3 | ABOVE/ABOVE/BELOW | +0.620/+2.102/-4.218 | BULL/MIXE/MIXE | +11.03%/+5.93% | +10.18%/+2.42% | 1.53x | `L-TI-KKR` |
| REGN | S5/S7/S1 | 76.4/60.4/52.8 | ABOVE/ABOVE/ABOVE | +10.048/+9.677/+11.429 | BULL/MIXE/MIXE | +16.84%/+5.45% | +15.99%/+1.94% | 1.06x | `L-TI-REGN` |
| TGT | S6/S2/S9 | 69.5/68.2/65.0 | ABOVE/ABOVE/ABOVE | +0.865/+1.018/+7.155 | BULL/BULL/MIXE | +18.44%/+15.80% | +17.59%/+12.29% | 1.27x | `L-TI-TGT` |
| ZBRA | S6/S7/S4 | 68.0/63.4/50.5 | ABOVE/ABOVE/ABOVE | +2.450/+7.272/+4.292 | BULL/MIXE/MIXE | +7.90%/+26.93% | +7.05%/+23.42% | 1.82x | `L-TI-ZBRA` |
| ARES | S2/S3/S3 | 69.3/57.4/51.6 | ABOVE/ABOVE/BELOW | +1.288/+2.876/-4.428 | BULL/MIXE/MIXE | +13.74%/+13.00% | +12.89%/+9.49% | 1.66x | `L-TI-ARES` |
| MSFT | S5/S4/S2 | 78.3/64.0/57.0 | ABOVE/ABOVE/BELOW | +10.413/+9.913/-4.491 | BULL/MIXE/BULL | +26.09%/+18.06% | +25.24%/+14.55% | 1.74x | `L-TI-MSFT` |
| GRMN | S6/S6/S2 | 79.9/73.1/69.9 | ABOVE/ABOVE/ABOVE | +6.668/+5.465/+5.252 | BULL/BULL/BULL | +24.28%/+26.06% | +23.43%/+22.55% | 0.86x | `L-TI-GRMN` |
| VEEV | S6/S6/S2 | 63.8/56.8/47.4 | ABOVE/ABOVE/BELOW | +0.746/+7.283/-5.742 | BULL/MIXE/MIXE | +7.42%/+23.24% | +6.57%/+19.73% | 1.66x | `L-TI-VEEV` |
| PCAR | B2/S9/S2 | 59.7/66.7/66.6 | ABOVE/ABOVE/ABOVE | +0.193/+1.324/+1.743 | BULL/BULL/BULL | +4.88%/+13.70% | +4.03%/+10.19% | 1.23x | `L-TI-PCAR` |
| LH | B1/S7/S2 | 65.4/66.2/63.5 | ABOVE/ABOVE/ABOVE | +2.127/+5.033/+2.986 | BULL/BULL/BULL | +8.10%/+19.98% | +7.25%/+16.47% | 0.90x | `L-TI-LH` |
| COF | S6/S2/S3 | 64.7/60.4/59.8 | BULL_X/ABOVE/BELOW | +0.504/+3.462/-2.761 | BULL/MIXE/BULL | +5.41%/+13.04% | +4.56%/+9.53% | 0.96x | `L-TI-COF` |
| HIG | B1/S7/S2 | 58.6/61.0/65.0 | ABOVE/ABOVE/BELOW | +0.030/+0.996/-0.733 | BULL/BULL/BULL | +3.82%/+7.56% | +2.97%/+4.05% | 1.22x | `L-TI-HIG` |
| WSM | S1/S2/S3 | 63.1/65.0/68.4 | ABOVE/ABOVE/ABOVE | +0.726/+3.107/+2.511 | BULL/BULL/BULL | +7.49%/+29.03% | +6.64%/+25.52% | 0.98x | `L-TI-WSM` |

RS20/RS60 are **diagnostics only** — they occupy no `Tech_Z` metric slot.

## Sleeves and thresholds

| Sleeve | Count | Basis |
|---|---|---|
| Ranked total (pctl ≥ 60) | 205 | mu Calibration Table floor |
| Percentile ≥ 80 (investable *band*) | 103 | threshold 1 only |
| **Clearing all five Evidence Thresholds** | **0** | thresholds 2, 3 and 4 fail for every name |
| Published prediction records | 24 | first 24 post-penalty ranks, contiguous 1–24 |
| Rejection log (pctl < 60) | 307 | not ranked in either sleeve |

### Why zero names are investable

| Evidence threshold | Result | Reason |
|---|---|---|
| 1. Adjusted-score pctl ≥ 80th | **PASS** | 103 names qualify |
| 2. ≥ 3 of 4 factor families non-negative | **FAIL** | `Fund_Z` and `Sent_Z` are `UNAVAILABLE` universe-wide; `rules.md § Family Aggregation` forbids counting an unavailable family, so **at most 2 of 4** can ever qualify |
| 3. No family > 50% of total conviction | **FAIL** | with only Technical (0.30) and Macro (0.15) live, Technical carries 0.30/0.45 = **66.67%** of live conviction for every name |
| 4. Data completeness ≥ 85% | **FAIL** | DQ multiplier is 0.80 < 0.85 |
| 5. No hard stop from § Stop Criteria | **PASS** | none triggered |

Thresholds 2, 3 and 4 are **arithmetically unsatisfiable** while two of four families have no fetch
path. No amount of price action changes that, which is why every package since 2026-07-01 has been
non-`GO`. The fix is engineering (Phase 2 of the `Fund_Z`/`Sent_Z` plan), not scoring.

## mu assignment

Every `mu` comes from the `rules.md` mu Calibration Table band for the name's percentile. **No
per-name adjustment was applied**, so no ±2pp reason is owed.

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
| Earnings inside 14 calendar days: `-0.10` | `rules.md § Risk Controls` | **142** of 512 scored (1 inside the published 24) |
| 30d realized vol > 2x sector median | `rules.md § Risk Controls` | 0 — no name breached the multiple |
| `0.25 x Kelly` < 2% NAV | `rules.md § Risk Controls` | 0 of the pctl≥80 pool |

Because the earnings sweep grounds the **entire** universe, ranks are post-penalty and contiguous
1–24 in the published set — there are no ungrounded names to skip, so the "skip ungrounded"
rule retired on 2026-07-29 stays retired.

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
| Every metric slot has a normative definition | PASS — Metric Definition Table above (new this run) |
