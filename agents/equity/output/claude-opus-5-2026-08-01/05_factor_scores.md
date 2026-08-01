# 05 — Factor Scores — 2026-08-01

Universe **513** scored names · label **`INDEX_UNION_PCTL (n=513)`** ·
basis 2026-07-31.

## Scoring architecture actually executed

`Adj Score = (0.30*Fund_Z + 0.30*Tech_Z + 0.25*Sent_Z + 0.15*Macro_Z) * DQ - Penalties`

| Family | Weight | State | Sourceable metrics |
|---|---|---|---|
| Fundamental | 0.30 | **`UNAVAILABLE`** | 0 — contributes `0.00 (UNAVAILABLE)` |
| Technical / Price | 0.30 | `AVAILABLE` | 8 slots: 20d & 60d momentum, RS20 & RS60 vs SPY, MA alignment (d+w), MACD state (d+w), 20d volume ratio, 60d max drawdown (negated) |
| Sentiment / Positioning | 0.25 | **`UNAVAILABLE`** | 0 — contributes `0.00 (UNAVAILABLE)` |
| Macro / Regime | 0.15 | `AVAILABLE` | 4: 60d beta (distance from 1.0, negated), sector RS60 leadership, rate sensitivity vs TLT (\|beta\| negated), realized-vol stability (30d/60d, negated) |

Each family z-score is the equal-weighted mean of its metric z-scores, computed
cross-sectionally over the 513 scored names after winsorizing at the
5th/95th percentiles (`factor_scoring.winsorize`), per `rules.md § Family Aggregation`.

State encodings used (disclosed so this run is reproducible):
MA alignment `BULLISH=+1, MIXED=0, BEARISH=−1`, averaged over daily+weekly.
MACD state `BULLISH_CROSS=+2, ABOVE_SIGNAL=+1, ON_SIGNAL=0, BELOW_SIGNAL=−1,
BEARISH_CROSS=−2`, averaged over daily+weekly.

**Data-quality multiplier = 0.80** ("notable coverage gaps"): two of four
families are unavailable universe-wide. Only 2 of 4 families carry information, so the
effective score is `(0.30*Tech_Z + 0.15*Macro_Z) * 0.80` — stated plainly
rather than hidden behind a composite number.

### ⚠ Duplicate-signal finding (new this run)

`technical_indicators.py` defines relative strength as
`relative_strength = momentum − benchmark_momentum` (see `add_relative_strength`, line 432).
Subtracting SPY's momentum is a **constant shift across every name**, and a constant shift
does not change a cross-sectional z-score. Measured on this run's universe:

| Identity | Max abs difference over 513 names |
|---|---|
| `z(rs20)` vs `z(mom20)` | **4.44e-16** |
| `z(rs60)` vs `z(mom60)` | **4.44e-16** |

Those are floating-point zero. `Tech_Z` therefore has **8 slots but only 6 distinct
signals**, and momentum occupies 4 of the 8 — so momentum carries **50%** of `Tech_Z`
instead of the 25% the metric list implies, and **33.3%** of the live composite
rather than 16.7%. The scores published below use the established
(un-deduplicated) engine so this package stays comparable with the ranked series that
preceded it; the fix is logged as an accepted Track B change in `13`, effective next run,
with its measured impact.

## Calibration feedback binding (read before scoring)

From `02 § 0`: weighted-mean rank IC **-0.1314** over n=439 settled
`EQUITY_ALPHA` records. `agents.md § Calibration Feedback Binding` therefore **caps all
confidence at `MEDIUM`**, applied to every record in this package. CI coverage is
70.16% (inside 55–85%), so the wider-sigma rule does **not** trigger and
sigma stays `REALIZED_VOL_30D`.

## Ranked candidates (top 20 of 205 ranked)

| Rank | Ticker | Company | Entry | Price Date | Tag | Adj Score | Score Trace | Pctl | Beta | 30d RVol | Sharpe | Sortino | IR | Kelly 0.25 | VaR95 | CVaR95 | Max DD60 | TD9 D/W/M | RSI14 D/W/M | MACD D/W/M | Days to Earn | mu | sigma | Sigma Source | Target | Target Date | 70% CI Lo | 70% CI Hi | Ledger | Metric Ledger | Conf | Primary Thesis | Key Risk |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **DXCM** | DexCom Inc. Common Stock | 83.45 | 2026-07-31 | `HISTORICAL` | **+0.4564** | `(0.3*0.00(UA) + 0.3*+1.5779 + 0.25*0.00(UA) + 0.15*+0.6479) * 0.80 - 0.00 = +0.4564` | 99.90 | +0.110 | 14.99% | 0.380 | 0.893 | 0.413 | 66.71% | -18.74% | -24.89% | -13.86% | S4/S3/S1 | 68.5/64.9/51.8 | BULL_X/ABOVE/ABOVE | none in 37d | +6.00% | 14.99% | `REALIZED_VOL_30D` | 88.46 | 2026-08-29 | 75.44 | 101.47 | `L-PX-DXCM` | `L-TI-DXCM`,`L-RM-DXCM`,`L-EA-DXCM` | MEDIUM | Health Care momentum/RS leader (`INFERRED`) | rank-order inversion risk (see § Calibration) |
| 2 | **NTAP** | NetApp Inc. Common Stock | 178.53 | 2026-07-31 | `HISTORICAL` | **+0.3886** | `(0.3*0.00(UA) + 0.3*+1.1075 + 0.25*0.00(UA) + 0.15*+1.0229) * 0.80 - 0.00 = +0.3886` | 99.71 | +1.306 | 12.18% | 0.467 | 0.757 | 0.188 | 101.13% | -14.09% | -19.09% | -15.81% | S9/S4/S4 | 64.9/73.0/70.7 | ABOVE/ABOVE/ABOVE | 25 | +6.00% | 12.18% | `REALIZED_VOL_30D` | 189.24 | 2026-08-29 | 166.63 | 211.85 | `L-PX-NTAP` | `L-TI-NTAP`,`L-RM-NTAP`,`L-EA-NTAP` | MEDIUM | Technology momentum/RS leader (`INFERRED`) | rank-order inversion risk (see § Calibration) |
| 3 | **WTW** | Willis Towers Watson Public  | 335.92 | 2026-07-31 | `HISTORICAL` | **+0.3653** | `(0.3*0.00(UA) + 0.3*+1.3954 + 0.25*0.00(UA) + 0.15*+0.2534) * 0.80 - 0.00 = +0.3653` | 99.51 | -0.499 | 10.10% | 0.563 | 1.830 | 0.761 | 146.93% | -10.67% | -14.81% | -6.18% | S6/S6/S1 | 80.1/67.2/59.9 | ABOVE/ABOVE/BELOW | none in 37d | +6.00% | 10.10% | `REALIZED_VOL_30D` | 356.08 | 2026-08-29 | 320.78 | 391.37 | `L-PX-WTW` | `L-TI-WTW`,`L-RM-WTW`,`L-EA-WTW` | MEDIUM | Finance momentum/RS leader (`INFERRED`) | rank-order inversion risk (see § Calibration) |
| 4 | **BAX** | Baxter International Inc. Co | 26.16 | 2026-07-31 | `HISTORICAL` | **+0.3559** | `(0.3*0.00(UA) + 0.3*+1.3448 + 0.25*0.00(UA) + 0.15*+0.2760) * 0.80 - 0.00 = +0.3559` | 99.32 | +0.462 | 13.28% | 0.429 | 0.931 | 0.426 | 85.08% | -15.91% | -21.35% | -7.19% | S6/S9/S2 | 70.8/69.9/48.7 | ABOVE/ABOVE/ABOVE | none in 37d | +6.00% | 13.28% | `REALIZED_VOL_30D` | 27.73 | 2026-08-29 | 24.12 | 31.34 | `L-PX-BAX` | `L-TI-BAX`,`L-RM-BAX`,`L-EA-BAX` | MEDIUM | Health Care momentum/RS leader (`INFERRED`) | rank-order inversion risk (see § Calibration) |
| 5 | **FTNT** | Fortinet Inc. Common Stock | 161.95 | 2026-07-31 | `HISTORICAL` | **+0.3458** | `(0.3*0.00(UA) + 0.3*+0.7972 + 0.25*0.00(UA) + 0.15*+1.2875) * 0.80 - 0.00 = +0.3458` | 99.12 | +0.948 | 10.70% | 0.532 | 1.715 | 0.259 | 131.09% | -11.65% | -16.04% | -10.10% | S3/S9/S5 | 60.1/77.2/78.2 | BELOW/ABOVE/ABOVE | none in 37d | +6.00% | 10.70% | `REALIZED_VOL_30D` | 171.67 | 2026-08-29 | 153.65 | 189.68 | `L-PX-FTNT` | `L-TI-FTNT`,`L-RM-FTNT`,`L-EA-FTNT` | MEDIUM | Technology momentum/RS leader (`INFERRED`) | rank-order inversion risk (see § Calibration) |
| 6 | **HPQ** | HP Inc. Common Stock | 27.27 | 2026-07-31 | `HISTORICAL` | **+0.3442** | `(0.3*0.00(UA) + 0.3*+1.0894 + 0.25*0.00(UA) + 0.15*+0.6895) * 0.80 - 0.00 = +0.3442` | 98.93 | +0.358 | 11.66% | 0.488 | 0.822 | 0.312 | 110.34% | -13.24% | -18.02% | -24.35% | S6/S3/S3 | 62.6/63.9/54.2 | ABOVE/ABOVE/BULL_X | 25 | +6.00% | 11.66% | `REALIZED_VOL_30D` | 28.91 | 2026-08-29 | 25.60 | 32.21 | `L-PX-HPQ` | `L-TI-HPQ`,`L-RM-HPQ`,`L-EA-HPQ` | MEDIUM | Technology momentum/RS leader (`INFERRED`) | rank-order inversion risk (see § Calibration) |
| 7 | **REGN** | Regeneron Pharmaceuticals In | 762.63 | 2026-07-31 | `HISTORICAL` | **+0.3138** | `(0.3*0.00(UA) + 0.3*+0.8666 + 0.25*0.00(UA) + 0.15*+0.8816) * 0.80 - 0.00 = +0.3138` | 98.73 | +0.413 | 9.35% | 0.609 | 1.303 | 0.501 | 171.65% | -9.42% | -13.26% | -16.84% | S4/S6/B5 | 78.1/61.0/53.0 | ABOVE/BULL_X/ABOVE | none in 37d | +6.00% | 9.35% | `REALIZED_VOL_30D` | 808.39 | 2026-08-29 | 734.25 | 882.53 | `L-PX-REGN` | `L-TI-REGN`,`L-RM-REGN`,`L-EA-REGN` | MEDIUM | Health Care momentum/RS leader (`INFERRED`) | rank-order inversion risk (see § Calibration) |
| 8 | **BMY** | Bristol-Myers Squibb Company | 65.31 | 2026-07-31 | `HISTORICAL` | **+0.3127** | `(0.3*0.00(UA) + 0.3*+1.0699 + 0.25*0.00(UA) + 0.15*+0.4658) * 0.80 - 0.00 = +0.3127` | 98.54 | -0.229 | 9.01% | 0.632 | 1.179 | 0.787 | 184.80% | -8.87% | -12.56% | -9.32% | S9/S6/S1 | 71.4/68.3/65.4 | ABOVE/ABOVE/ABOVE | none in 37d | +6.00% | 9.01% | `REALIZED_VOL_30D` | 69.23 | 2026-08-29 | 63.11 | 75.35 | `L-PX-BMY` | `L-TI-BMY`,`L-RM-BMY`,`L-EA-BMY` | MEDIUM | Health Care momentum/RS leader (`INFERRED`) | rank-order inversion risk (see § Calibration) |
| 9 | **GRMN** | Garmin Ltd. Common Stock (Sw | 293.78 | 2026-07-31 | `HISTORICAL` | **+0.2981** | `(0.3*0.00(UA) + 0.3*+1.3248 + 0.25*0.00(UA) + 0.15*-0.1651) * 0.80 - 0.00 = +0.2981` | 98.34 | +0.163 | 15.09% | 0.377 | 1.366 | 0.464 | 65.83% | -18.91% | -25.10% | -7.03% | S5/S5/S1 | 77.0/70.8/68.4 | ABOVE/BULL_X/BULL_X | none in 37d | +6.00% | 15.09% | `REALIZED_VOL_30D` | 311.41 | 2026-08-29 | 265.29 | 357.53 | `L-PX-GRMN` | `L-TI-GRMN`,`L-RM-GRMN`,`L-EA-GRMN` | MEDIUM | Industrials momentum/RS leader (`INFERRED`) | rank-order inversion risk (see § Calibration) |
| 10 | **BBY** | Best Buy Co. Inc. Common Sto | 86.26 | 2026-07-31 | `HISTORICAL` | **+0.2835** | `(0.3*0.00(UA) + 0.3*+0.8927 + 0.25*0.00(UA) + 0.15*+0.5768) * 0.80 - 0.00 = +0.2835` | 98.15 | +0.531 | 8.41% | 0.677 | 1.286 | 0.386 | 212.06% | -7.88% | -11.33% | -8.93% | B1/S9/S3 | 59.5/66.7/59.7 | BEAR_X/ABOVE/ABOVE | 26 | +6.00% | 8.41% | `REALIZED_VOL_30D` | 91.44 | 2026-08-29 | 83.89 | 98.98 | `L-PX-BBY` | `L-TI-BBY`,`L-RM-BBY`,`L-EA-BBY` | MEDIUM | Consumer Discretionary momentum/RS leader (`INFERRED`) | rank-order inversion risk (see § Calibration) |
| 11 | **LH** | Labcorp Holdings Inc. Common | 309.20 | 2026-07-31 | `HISTORICAL` | **+0.2821** | `(0.3*0.00(UA) + 0.3*+1.0742 + 0.25*0.00(UA) + 0.15*+0.2025) * 0.80 - 0.00 = +0.2821` | 97.95 | -0.091 | 8.04% | 0.708 | 1.649 | 0.875 | 232.02% | -7.27% | -10.56% | -6.20% | S7/S6/S1 | 67.3/67.3/64.1 | ABOVE/ABOVE/BULL_X | none in 37d | +6.00% | 8.04% | `REALIZED_VOL_30D` | 327.75 | 2026-08-29 | 301.90 | 353.61 | `L-PX-LH` | `L-TI-LH`,`L-RM-LH`,`L-EA-LH` | MEDIUM | Health Care momentum/RS leader (`INFERRED`) | rank-order inversion risk (see § Calibration) |
| 12 | **IQV** | IQVIA Holdings Inc. Common S | 235.02 | 2026-07-31 | `HISTORICAL` | **+0.2763** | `(0.3*0.00(UA) + 0.3*+1.0860 + 0.25*0.00(UA) + 0.15*+0.1303) * 0.80 - 0.00 = +0.2763` | 97.76 | -0.189 | 15.50% | 0.367 | 1.229 | 0.458 | 62.43% | -19.58% | -25.93% | -10.23% | S7/S6/S2 | 68.0/67.2/57.4 | ABOVE/ABOVE/BULL_X | none in 37d | +6.00% | 15.50% | `REALIZED_VOL_30D` | 249.12 | 2026-08-29 | 211.24 | 287.01 | `L-PX-IQV` | `L-TI-IQV`,`L-RM-IQV`,`L-EA-IQV` | MEDIUM | Health Care momentum/RS leader (`INFERRED`) | rank-order inversion risk (see § Calibration) |
| 13 | **GM** | General Motors Company Commo | 88.86 | 2026-07-31 | `HISTORICAL` | **+0.2704** | `(0.3*0.00(UA) + 0.3*+1.0383 + 0.25*0.00(UA) + 0.15*+0.1770) * 0.80 - 0.00 = +0.2704` | 97.56 | +1.297 | 9.09% | 0.626 | 1.787 | 0.377 | 181.46% | -9.00% | -12.73% | -10.27% | S9/S2/S1 | 68.3/65.1/70.6 | ABOVE/BULL_X/ABOVE | none in 37d | +6.00% | 9.09% | `REALIZED_VOL_30D` | 94.19 | 2026-08-29 | 85.79 | 102.59 | `L-PX-GM` | `L-TI-GM`,`L-RM-GM`,`L-EA-GM` | MEDIUM | Industrials momentum/RS leader (`INFERRED`) | rank-order inversion risk (see § Calibration) |
| 14 | **BEN** | Franklin Resources Inc. Comm | 33.86 | 2026-07-31 | `HISTORICAL` | **+0.2641** | `(0.3*0.00(UA) + 0.3*+0.6888 + 0.25*0.00(UA) + 0.15*+0.8235) * 0.80 - 0.00 = +0.2641` | 97.37 | +1.042 | 7.48% | 0.761 | 1.125 | 0.585 | 268.06% | -6.34% | -9.41% | -6.42% | S6/B3/S7 | 58.3/70.9/70.1 | BELOW/ABOVE/ABOVE | none in 37d | +6.00% | 7.48% | `REALIZED_VOL_30D` | 35.89 | 2026-08-29 | 33.26 | 38.53 | `L-PX-BEN` | `L-TI-BEN`,`L-RM-BEN`,`L-EA-BEN` | MEDIUM | Finance momentum/RS leader (`INFERRED`) | rank-order inversion risk (see § Calibration) |
| 15 | **STT** | State Street Corporation Com | 184.16 | 2026-07-31 | `HISTORICAL` | **+0.2524** | `(0.3*0.00(UA) + 0.3*+0.7631 + 0.25*0.00(UA) + 0.15*+0.5768) * 0.80 - 0.00 = +0.2524` | 97.17 | +0.844 | 7.88% | 0.723 | 1.303 | 0.694 | 241.71% | -7.00% | -10.23% | -5.65% | B4/S9/S9 | 59.1/85.3/87.6 | BELOW/ABOVE/ABOVE | none in 37d | +6.00% | 7.88% | `REALIZED_VOL_30D` | 195.21 | 2026-08-29 | 180.12 | 210.30 | `L-PX-STT` | `L-TI-STT`,`L-RM-STT`,`L-EA-STT` | MEDIUM | Finance momentum/RS leader (`INFERRED`) | rank-order inversion risk (see § Calibration) |
| 16 | **PCAR** | PACCAR Inc. Common Stock | 132.68 | 2026-07-31 | `HISTORICAL` | **+0.2503** | `(0.3*0.00(UA) + 0.3*+0.9250 + 0.25*0.00(UA) + 0.15*+0.2355) * 0.80 - 0.00 = +0.2503` | 96.98 | +1.131 | 8.91% | 0.639 | 1.415 | 0.483 | 189.13% | -8.69% | -12.35% | -5.86% | B1/S9/S1 | 61.1/67.8/67.1 | ABOVE/ABOVE/ABOVE | none in 37d | +6.00% | 8.91% | `REALIZED_VOL_30D` | 140.64 | 2026-08-29 | 128.35 | 152.93 | `L-PX-PCAR` | `L-TI-PCAR`,`L-RM-PCAR`,`L-EA-PCAR` | MEDIUM | Consumer Discretionary momentum/RS leader (`INFERRED`) | rank-order inversion risk (see § Calibration) |
| 17 | **AMP** | Ameriprise Financial Inc. Co | 545.84 | 2026-07-31 | `HISTORICAL` | **+0.2497** | `(0.3*0.00(UA) + 0.3*+0.7589 + 0.25*0.00(UA) + 0.15*+0.5631) * 0.80 - 0.00 = +0.2497` | 96.78 | +0.310 | 7.79% | 0.730 | 1.526 | 0.760 | 246.95% | -6.86% | -10.06% | -7.46% | S6/S7/S1 | 69.9/69.7/60.7 | ABOVE/ABOVE/BELOW | none in 37d | +6.00% | 7.79% | `REALIZED_VOL_30D` | 578.59 | 2026-08-29 | 534.35 | 622.83 | `L-PX-AMP` | `L-TI-AMP`,`L-RM-AMP`,`L-EA-AMP` | MEDIUM | Finance momentum/RS leader (`INFERRED`) | rank-order inversion risk (see § Calibration) |
| 18 | **PFG** | Principal Financial Group In | 113.73 | 2026-07-31 | `HISTORICAL` | **+0.2472** | `(0.3*0.00(UA) + 0.3*+0.9124 + 0.25*0.00(UA) + 0.15*+0.2351) * 0.80 - 0.00 = +0.2472` | 96.59 | -0.033 | 7.18% | 0.793 | 1.008 | 0.980 | 291.33% | -5.84% | -8.78% | -6.16% | S5/S9/S9 | 58.8/68.8/74.6 | BULL_X/ABOVE/ABOVE | none in 37d | +6.00% | 7.18% | `REALIZED_VOL_30D` | 120.55 | 2026-08-29 | 112.07 | 129.04 | `L-PX-PFG` | `L-TI-PFG`,`L-RM-PFG`,`L-EA-PFG` | MEDIUM | Finance momentum/RS leader (`INFERRED`) | rank-order inversion risk (see § Calibration) |
| 19 | **MMM** | 3M Company Common Stock | 176.28 | 2026-07-31 | `HISTORICAL` | **+0.2424** | `(0.3*0.00(UA) + 0.3*+0.8308 + 0.25*0.00(UA) + 0.15*+0.3588) * 0.80 - 0.00 = +0.2424` | 96.39 | +0.404 | 8.93% | 0.638 | 1.874 | 0.678 | 188.18% | -8.73% | -12.39% | -7.90% | B1/S2/S1 | 64.8/66.2/64.8 | ABOVE/ABOVE/BELOW | none in 37d | +6.00% | 8.93% | `REALIZED_VOL_30D` | 186.86 | 2026-08-29 | 170.49 | 203.22 | `L-PX-MMM` | `L-TI-MMM`,`L-RM-MMM`,`L-EA-MMM` | MEDIUM | Health Care momentum/RS leader (`INFERRED`) | rank-order inversion risk (see § Calibration) |
| 20 | **MSFT** | Microsoft Corporation Common | 464.72 | 2026-07-31 | `HISTORICAL` | **+0.2393** | `(0.3*0.00(UA) + 0.3*+0.8434 + 0.25*0.00(UA) + 0.15*+0.3078) * 0.80 - 0.00 = +0.2393` | 96.20 | +0.937 | 15.69% | 0.363 | 1.522 | 0.325 | 60.93% | -19.89% | -26.32% | -23.38% | S4/S3/S1 | 74.5/60.6/54.8 | ABOVE/ABOVE/BELOW | none in 37d | +6.00% | 15.69% | `REALIZED_VOL_30D` | 492.60 | 2026-08-29 | 416.77 | 568.44 | `L-PX-MSFT` | `L-TI-MSFT`,`L-RM-MSFT`,`L-EA-MSFT` | MEDIUM | Technology momentum/RS leader (`INFERRED`) | rank-order inversion risk (see § Calibration) |

## Score attribution

| Ticker | Fund_Z | Tech_Z | Sent_Z | Macro_Z | Composite_Z | DQ | Penalties | Adj Score | Top Positive Drivers | Top Negative Drivers | Metric Ledger |
|---|---|---|---|---|---|---|---|---|---|---|---|
| DXCM | `UNAVAILABLE` | +1.5779 | `UNAVAILABLE` | +0.6479 | +0.5705 | 0.80 | 0.00 | **+0.4564** | vol_conf +2.45; mom20 +1.94; rs20 +1.94 | vol_stability -0.50 | `L-TI-DXCM`,`L-RM-DXCM` |
| NTAP | `UNAVAILABLE` | +1.1075 | `UNAVAILABLE` | +1.0229 | +0.4857 | 0.80 | 0.00 | **+0.3886** | vol_stability +2.25; mom20 +1.94; rs20 +1.94 | vol_conf -1.09; dd60 -0.11 | `L-TI-NTAP`,`L-RM-NTAP` |
| WTW | `UNAVAILABLE` | +1.3954 | `UNAVAILABLE` | +0.2534 | +0.4566 | 0.80 | 0.00 | **+0.3653** | mom20 +1.94; rs20 +1.94; mom60 +1.86 | beta -0.73; vol_stability -0.53 | `L-TI-WTW`,`L-RM-WTW` |
| BAX | `UNAVAILABLE` | +1.3448 | `UNAVAILABLE` | +0.2760 | +0.4448 | 0.80 | 0.00 | **+0.3559** | mom20 +1.94; rs20 +1.94; mom60 +1.86 | vol_stability -0.73; rate_sens -0.70 | `L-TI-BAX`,`L-RM-BAX` |
| FTNT | `UNAVAILABLE` | +0.7972 | `UNAVAILABLE` | +1.2875 | +0.4323 | 0.80 | 0.00 | **+0.3458** | vol_stability +2.25; mom60 +1.86; rs60 +1.86 | macd -0.10 | `L-TI-FTNT`,`L-RM-FTNT` |
| HPQ | `UNAVAILABLE` | +1.0894 | `UNAVAILABLE` | +0.6895 | +0.4302 | 0.80 | 0.00 | **+0.3442** | vol_stability +2.25; mom20 +1.94; rs20 +1.94 | dd60 -1.07; rate_sens -0.43 | `L-TI-HPQ`,`L-RM-HPQ` |
| REGN | `UNAVAILABLE` | +0.8666 | `UNAVAILABLE` | +0.8816 | +0.3922 | 0.80 | 0.00 | **+0.3138** | mom20 +1.94; rs20 +1.94; sector_lead +1.67 | dd60 -0.22 | `L-TI-REGN`,`L-RM-REGN` |
| BMY | `UNAVAILABLE` | +1.0699 | `UNAVAILABLE` | +0.4658 | +0.3909 | 0.80 | 0.00 | **+0.3127** | sector_lead +1.67; mom20 +1.54; rs20 +1.54 | vol_stability -0.66; beta -0.29 | `L-TI-BMY`,`L-RM-BMY` |
| GRMN | `UNAVAILABLE` | +1.3248 | `UNAVAILABLE` | -0.1651 | +0.3727 | 0.80 | 0.00 | **+0.2981** | mom20 +1.94; rs20 +1.94; mom60 +1.64 | vol_stability -1.54; sector_lead -0.58 | `L-TI-GRMN`,`L-RM-GRMN` |
| BBY | `UNAVAILABLE` | +0.8927 | `UNAVAILABLE` | +0.5768 | +0.3543 | 0.80 | 0.00 | **+0.2835** | vol_stability +2.25; mom60 +1.86; rs60 +1.86 | rate_sens -0.80; macd -0.73; vol_conf -0.45 | `L-TI-BBY`,`L-RM-BBY` |
| LH | `UNAVAILABLE` | +1.0742 | `UNAVAILABLE` | +0.2025 | +0.3526 | 0.80 | 0.00 | **+0.2821** | sector_lead +1.67; ma_align +1.32; rs60 +1.23 | vol_stability -0.98; beta -0.06 | `L-TI-LH`,`L-RM-LH` |
| IQV | `UNAVAILABLE` | +1.0860 | `UNAVAILABLE` | +0.1303 | +0.3454 | 0.80 | 0.00 | **+0.2763** | mom60 +1.86; rs60 +1.86; mom20 +1.69 | vol_stability -0.80; vol_conf -0.54; beta -0.22 | `L-TI-IQV`,`L-RM-IQV` |
| GM | `UNAVAILABLE` | +1.0383 | `UNAVAILABLE` | +0.1770 | +0.3381 | 0.80 | 0.00 | **+0.2704** | mom20 +1.94; rs20 +1.94; ma_align +1.32 | rate_sens -0.87; sector_lead -0.58; vol_conf -0.45 | `L-TI-GM`,`L-RM-GM` |
| BEN | `UNAVAILABLE` | +0.6888 | `UNAVAILABLE` | +0.8235 | +0.3302 | 0.80 | 0.00 | **+0.2641** | vol_conf +2.45; beta +1.62; ma_align +1.32 | mom20 -0.14; rs20 -0.14; macd -0.10 | `L-TI-BEN`,`L-RM-BEN` |
| STT | `UNAVAILABLE` | +0.7631 | `UNAVAILABLE` | +0.5768 | +0.3154 | 0.80 | 0.00 | **+0.2524** | mom60 +1.54; rs60 +1.54; beta +1.50 | vol_conf -1.15; vol_stability -0.83; macd -0.10 | `L-TI-STT`,`L-RM-STT` |
| PCAR | `UNAVAILABLE` | +0.9250 | `UNAVAILABLE` | +0.2355 | +0.3128 | 0.80 | 0.00 | **+0.2503** | beta +1.54; mom20 +1.37; rs20 +1.37 | vol_conf -0.77; rate_sens -0.51; sector_lead -0.12 | `L-TI-PCAR`,`L-RM-PCAR` |
| AMP | `UNAVAILABLE` | +0.7589 | `UNAVAILABLE` | +0.5631 | +0.3121 | 0.80 | 0.00 | **+0.2497** | mom20 +1.44; rs20 +1.44; macd +1.15 | vol_conf -0.86; vol_stability -0.61 | `L-TI-AMP`,`L-RM-AMP` |
| PFG | `UNAVAILABLE` | +0.9124 | `UNAVAILABLE` | +0.2351 | +0.3090 | 0.80 | 0.00 | **+0.2472** | vol_conf +1.90; ma_align +1.32; macd +1.15 | vol_stability -1.14 | `L-TI-PFG`,`L-RM-PFG` |
| MMM | `UNAVAILABLE` | +0.8308 | `UNAVAILABLE` | +0.3588 | +0.3031 | 0.80 | 0.00 | **+0.2424** | sector_lead +1.67; mom60 +1.50; rs60 +1.50 | vol_conf -1.21; vol_stability -1.02 | `L-TI-MMM`,`L-RM-MMM` |
| MSFT | `UNAVAILABLE` | +0.8434 | `UNAVAILABLE` | +0.3078 | +0.2992 | 0.80 | 0.00 | **+0.2393** | mom20 +1.94; rs20 +1.94; vol_conf +1.73 | vol_stability -1.33; dd60 -0.96; ma_align -0.37 | `L-TI-MSFT`,`L-RM-MSFT` |

## Metric availability

| Metric Group | Sourceable Count | UNAVAILABLE Count | DQ / Confidence Effect | Notes |
|---|---|---|---|---|
| Technical / price | 513 | 0 | none | 100% coverage; drives `Tech_Z` |
| Risk / return (beta, TE, vol, DD) | 513 | 0 | none | 100% coverage; drives `Macro_Z`, sigma, Sortino |
| Sizing (Kelly) | 513 | 0 | none | Derived from mu/sigma |
| Earnings distance | 513 | 0 | penalty input | Complete calendar sweep; 30/30 cross-validated |
| Sector / market cap | 511 / 513 | 2 / 0 | negligible | 2 names lack a sector label |
| **Fundamental** | **0** | **513** | **DQ → 0.80; blocks threshold 2** | No universe-scale XBRL path wired |
| **Sentiment / positioning** | **0** | **513** | **DQ → 0.80; blocks threshold 2** | No universe-scale analyst/SI path wired |
| Options IV30 | 0 | 513 | sigma chain falls to step 2 | No options feed |

No score below cites a metric absent from `01_preflight.md`, and **no missing metric is
described as neutral or supportive** — `Fund_Z` and `Sent_Z` are carried as
`0.00 (UNAVAILABLE)` in the arithmetic and reported as `UNAVAILABLE` everywhere else.

## Technical indicator summary (top 20)

| Ticker | TD9 D/W/M | RSI14 D/W/M | MACD State D/W/M | MACD Hist D/W/M | MA Align D/W/M | Mom 20/60 (d) | RS20/RS60 vs SPY | Vol Ratio 20d | Indicator Ledger |
|---|---|---|---|---|---|---|---|---|---|
| DXCM | S4/S3/S1 | 68.5/64.9/51.8 | BULL_X/ABOVE/ABOVE | +0.515/+1.352/+2.053 | BULL/BULL/MIXE | +17.12%/+40.30% | +16.82%/+36.82% | 2.49x | `L-TI-DXCM` |
| NTAP | S9/S4/S4 | 64.9/73.0/70.7 | ABOVE/ABOVE/ABOVE | +0.716/+3.363/+6.582 | BULL/BULL/BULL | +16.15%/+56.88% | +15.85%/+53.40% | 0.74x | `L-TI-NTAP` |
| WTW | S6/S6/S1 | 80.1/67.2/59.9 | ABOVE/ABOVE/BELOW | +3.940/+8.305/-5.656 | BULL/MIXE/BULL | +17.36%/+29.94% | +17.06%/+26.46% | 1.45x | `L-TI-WTW` |
| BAX | S6/S9/S2 | 70.8/69.9/48.7 | ABOVE/ABOVE/ABOVE | +0.345/+0.805/+0.869 | BULL/MIXE/MIXE | +15.50%/+56.26% | +15.20%/+52.78% | 1.35x | `L-TI-BAX` |
| FTNT | S3/S9/S5 | 60.1/77.2/78.2 | BELOW/ABOVE/ABOVE | -1.067/+3.199/+6.918 | BULL/BULL/BULL | +3.65%/+80.10% | +3.35%/+76.62% | 1.14x | `L-TI-FTNT` |
| HPQ | S6/S3/S3 | 62.6/63.9/54.2 | ABOVE/ABOVE/BULL_X | +0.313/+0.514/+0.239 | BULL/MIXE/MIXE | +24.35%/+30.51% | +24.05%/+27.03% | 1.31x | `L-TI-HPQ` |
| REGN | S4/S6/B5 | 78.1/61.0/53.0 | ABOVE/BULL_X/ABOVE | +8.831/+5.028/+8.067 | BULL/MIXE/MIXE | +16.56%/+8.76% | +16.26%/+5.28% | 1.47x | `L-TI-REGN` |
| BMY | S9/S6/S1 | 71.4/68.3/65.4 | ABOVE/ABOVE/ABOVE | +0.459/+0.453/+1.661 | BULL/BULL/MIXE | +12.35%/+15.97% | +12.05%/+12.49% | 1.34x | `L-TI-BMY` |
| GRMN | S5/S5/S1 | 77.0/70.8/68.4 | ABOVE/BULL_X/BULL_X | +5.927/+2.963/+2.851 | BULL/BULL/BULL | +22.40%/+25.76% | +22.10%/+22.28% | 1.15x | `L-TI-GRMN` |
| BBY | B1/S9/S3 | 59.5/66.7/59.7 | BEAR_X/ABOVE/ABOVE | -0.169/+2.359/+1.514 | BULL/BULL/BULL | +10.60%/+52.62% | +10.30%/+49.14% | 0.96x | `L-TI-BBY` |
| LH | S7/S6/S1 | 67.3/67.3/64.1 | ABOVE/ABOVE/BULL_X | +2.707/+4.648/+1.953 | BULL/BULL/BULL | +7.74%/+20.58% | +7.44%/+17.10% | 1.39x | `L-TI-LH` |
| IQV | S7/S6/S2 | 68.0/67.2/57.4 | ABOVE/ABOVE/BULL_X | +2.823/+6.736/+3.035 | BULL/MIXE/MIXE | +13.51%/+33.22% | +13.21%/+29.74% | 0.93x | `L-TI-IQV` |
| GM | S9/S2/S1 | 68.3/65.1/70.6 | ABOVE/BULL_X/ABOVE | +1.299/+0.291/+1.577 | BULL/BULL/BULL | +16.92%/+16.94% | +16.62%/+13.46% | 0.96x | `L-TI-GM` |
| BEN | S6/B3/S7 | 58.3/70.9/70.1 | BELOW/ABOVE/ABOVE | -0.010/+0.132/+1.327 | BULL/BULL/BULL | -0.73%/+12.28% | -1.03%/+8.80% | 2.55x | `L-TI-BEN` |
| STT | B4/S9/S9 | 59.1/85.3/87.6 | BELOW/ABOVE/ABOVE | -0.902/+2.261/+6.141 | BULL/BULL/BULL | +7.89%/+24.48% | +7.59%/+21.00% | 0.72x | `L-TI-STT` |
| PCAR | B1/S9/S1 | 61.1/67.8/67.1 | ABOVE/ABOVE/ABOVE | +0.444/+1.261/+1.465 | BULL/BULL/BULL | +11.03%/+17.34% | +10.73%/+13.86% | 0.85x | `L-TI-PCAR` |
| AMP | S6/S7/S1 | 69.9/69.7/60.7 | ABOVE/ABOVE/BELOW | +0.513/+10.753/-4.860 | BULL/MIXE/BULL | +11.59%/+15.00% | +11.29%/+11.52% | 0.82x | `L-TI-AMP` |
| PFG | S5/S9/S9 | 58.8/68.8/74.6 | BULL_X/ABOVE/ABOVE | +0.057/+0.539/+2.856 | BULL/BULL/BULL | +2.58%/+13.65% | +2.28%/+10.17% | 1.77x | `L-TI-PFG` |
| MMM | B1/S2/S1 | 64.8/66.2/64.8 | ABOVE/ABOVE/BELOW | +1.241/+2.624/-0.375 | BULL/MIXE/BULL | +9.87%/+24.07% | +9.57%/+20.59% | 0.70x | `L-TI-MMM` |
| MSFT | S4/S3/S1 | 74.5/60.6/54.8 | ABOVE/ABOVE/BELOW | +7.460/+5.340/-9.248 | MIXE/MIXE/BULL | +19.01%/+13.21% | +18.71%/+9.73% | 1.71x | `L-TI-MSFT` |

## Penalties applied

41 of 205 ranked names carry the 14-day earnings penalty; 1 of them sit inside the published top 24.

| Ticker | Rank | Penalty | Reason | Confidence effect |
|---|---|---|---|---|
| PRU | 21 | −0.10 | earnings in 3d (<=14d): -0.10 | capped `LOW` |
| MET | 25 | −0.10 | earnings in 4d (<=14d): -0.10 | capped `LOW` |
| ZBRA | 29 | −0.10 | earnings in 3d (<=14d): -0.10 | capped `LOW` |
| VTRS | 33 | −0.10 | earnings in 5d (<=14d): -0.10 | capped `LOW` |
| CPAY | 46 | −0.10 | earnings in 4d (<=14d): -0.10 | capped `LOW` |
| DVA | 48 | −0.10 | earnings in 3d (<=14d): -0.10 | capped `LOW` |
| HST | 61 | −0.10 | earnings in 4d (<=14d): -0.10 | capped `LOW` |
| AIZ | 64 | −0.10 | earnings in 3d (<=14d): -0.10 | capped `LOW` |
| GEN | 66 | −0.10 | earnings in 5d (<=14d): -0.10 | capped `LOW` |
| DDOG | 85 | −0.10 | earnings in 5d (<=14d): -0.10 | capped `LOW` |
| SOLV | 92 | −0.10 | earnings in 4d (<=14d): -0.10 | capped `LOW` |
| DOC | 99 | −0.10 | earnings in 3d (<=14d): -0.10 | capped `LOW` |
| AMGN | 104 | −0.10 | earnings in 3d (<=14d): -0.10 | capped `LOW` |
| AFL | 115 | −0.10 | earnings in 5d (<=14d): -0.10 | capped `LOW` |
| AMCR | 119 | −0.10 | earnings in 11d (<=14d): -0.10 | capped `LOW` |
| BDX | 126 | −0.10 | earnings in 5d (<=14d): -0.10 | capped `LOW` |
| CDW | 127 | −0.10 | earnings in 4d (<=14d): -0.10 | capped `LOW` |
| CCEP | 129 | −0.10 | earnings in 3d (<=14d): -0.10 | capped `LOW` |
| PSX | 130 | −0.10 | earnings in 4d (<=14d): -0.10 | capped `LOW` |
| EA | 134 | −0.10 | earnings in 3d (<=14d): -0.10 | capped `LOW` |

## Investable subset — **EMPTY**

No name is investable. `rules.md § Evidence Thresholds` requires **all five** conditions;
three fail for every name in the universe:

| # | Threshold | Result | Why |
|---|---|---|---|
| 1 | Pctl ≥ 80 | PASS | 103 names qualify |
| 2 | ≥ 3 of 4 families non-negative | **FAIL** | Only 2 families are `AVAILABLE`; a maximum of 2 can be non-negative |
| 3 | No family > 50% of conviction | **FAIL** | `Tech_Z` carries 66.7% of live weight |
| 4 | Data completeness ≥ 85% | **FAIL** | DQ 0.80 |
| 5 | No hard stop | PASS | none triggered |

Thresholds 2–4 are all downstream of the same root cause: two factor families have no fetch
path. This is **not** a market call — it would fail identically in any regime — and it is
the same blocker recorded since 2026-07-15.

## Monitoring sleeve (published)

The top **24** ranked names are published as `MONITORING`-sleeve forecasts in
`15_predictions.json`. They carry full `mu`/`sigma`/CI so they remain **settleable** — per
`rules.md § Sigma Fallback Chain`, emitting a monitor list without forecasts is a publishing
failure, not caution. Ranks are **contiguous 1–24** because the calendar sweep
grounded 100% of the universe, so the older "skip ungrounded names" rule has nothing to skip.

Sector spread of the published set: {'Health Care': 8, 'Technology': 4, 'Finance': 6, 'Industrials': 3, 'Consumer Discretionary': 3}.
Percentile range 95.42 … 99.90.

## Near-miss rejection list (ranks 25–30)

| Rank | Ticker | Adj Score | Pctl | Tech_Z | Macro_Z | Days to Earn | Why not published |
|---|---|---|---|---|---|---|---|
| 25 | MET | +0.2277 | 95.22 | +1.1293 | +0.4720 | 4 | below the 24-name publication cut |
| 26 | DGX | +0.2231 | 95.03 | +0.9143 | +0.0306 | none in 37d | below the 24-name publication cut |
| 27 | RJF | +0.2228 | 94.83 | +0.5813 | +0.6939 | none in 37d | below the 24-name publication cut |
| 28 | TRV | +0.2217 | 94.64 | +1.0292 | -0.2106 | none in 37d | below the 24-name publication cut |
| 29 | ZBRA | +0.2211 | 94.44 | +1.0642 | +0.5472 | 3 | below the 24-name publication cut |
| 30 | MTD | +0.2177 | 94.25 | +0.5875 | +0.6391 | none in 37d | below the 24-name publication cut |

## What drives the leaderboard — and why that is a warning

With `Fund_Z` and `Sent_Z` unavailable, `Tech_Z` carries 66.7% of live composite
weight and `Macro_Z` the remaining 33.3%. `Tech_Z` is built from trend-persistence
metrics — and, per the duplicate finding above, half its weight is momentum measured twice.
The leaderboard is therefore, mechanically, **a ranked list of the last 60 days' winners**.

That is precisely the construction that inverts through a rotation, and the settled record
now says so directly: weighted-mean rank IC **-0.1314** across 28 vintages,
negative in 20 of them, while CI coverage stays
healthy at 70.16%. The system's uncertainty estimates are well calibrated;
its ordering is not.

Today's leaderboard is led by Health Care (8 of 24) and
Finance (6 of 24) — defensive and value leadership, consistent
with `03`'s observation that QQQ and SOXX are both below their moving averages while SPY is
above. Read these 24 names as *what the current engine ranks highest*, not as
conviction. They are published to stay auditable and settleable.
