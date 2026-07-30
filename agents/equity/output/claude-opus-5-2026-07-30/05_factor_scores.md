# 05 — Factor Scores — 2026-07-30

Universe **513** scored names · label **`INDEX_UNION_PCTL (n=513)`** · basis 2026-07-29.

## Scoring architecture actually executed

`Adj Score = (0.30*Fund_Z + 0.30*Tech_Z + 0.25*Sent_Z + 0.15*Macro_Z) * DQ - Penalties`

| Family | Weight | State | Sourceable metrics |
|---|---|---|---|
| Fundamental | 0.30 | **`UNAVAILABLE`** | 0 — contributes `0.00 (UNAVAILABLE)` |
| Technical / Price | 0.30 | `AVAILABLE` | 8: 20d & 60d momentum, RS20 & RS60 vs SPY, MA alignment (d+w), MACD state (d+w), 20d volume ratio, 60d max drawdown (negated) |
| Sentiment / Positioning | 0.25 | **`UNAVAILABLE`** | 0 — contributes `0.00 (UNAVAILABLE)` |
| Macro / Regime | 0.15 | `AVAILABLE` | 4: 60d beta, sector RS60 leadership, rate sensitivity vs TLT (|beta| negated), realized-vol stability (30d/60d, negated) |

Each family z-score is the equal-weighted mean of its metric z-scores, computed
cross-sectionally over the 513 scored names after winsorizing at the 5th/95th percentiles
(`factor_scoring.winsorize`), per `rules.md § Family Aggregation`.

**Data-quality multiplier = 0.80** ("notable coverage gaps"): two of four
families are unavailable universe-wide. Only 2 of 4 families
carry information, so the effective score is driven by
`(0.30*Tech_Z + 0.15*Macro_Z) * 0.80` — a fact stated plainly rather than
hidden behind a composite number.

## Calibration feedback binding (read before scoring)

From `02 § 0`: rank IC weighted mean **-0.1975** over n=347 settled `EQUITY_ALPHA`
records. `agents.md § Calibration Feedback Binding` therefore **caps all confidence at
`MEDIUM`**, applied to every record in this package. CI coverage is
72.05% (inside 55–85%), so the wider-sigma rule does **not** trigger and
sigma stays `REALIZED_VOL_30D`.

## Ranked candidates (top 20 of 205 ranked)

| Rank | Ticker | Company | Entry Price | Price Date | Price Tag | Adj Score | Pctl | Beta | 30d RVol | Sharpe | Sortino | IR | Kelly 0.25 | VaR95 | CVaR95 | Max DD60 | TD9 D/W/M | RSI14 D/W/M | MACD D/W/M | Days to Earnings | mu | sigma | Sigma Source | Target Price | Target Date | 70% CI Lo | 70% CI Hi | Confidence | Ledger Rows | Primary Thesis | Key Risk |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | GRMN | Garmin Ltd. Common Stock (Sw | 294.83 | 2026-07-29 | HISTORICAL | +0.3309 | 99.81 | +0.161 | 15.47% | 0.368 | 1.366 | 0.477 | 62.72% | -19.52% | -25.86% | -7.03% | S3/S5/S1 | 80.0/71.0/68.7 | ABOVE/BULL_X/BULL_X | 38 | +6.00% | 15.47% | REALIZED_VOL_30D | 312.52 | 2026-08-27 | 265.10 | 359.94 | MEDIUM | L-PX-GRMN, L-TI-GRMN, L-RM-GRMN | Industrials momentum/RS leader | rank-order inversion risk (see § Calibration) |
| 2 | BBY | Best Buy Co. Inc. Common Sto | 90.17 | 2026-07-29 | HISTORICAL | +0.3256 | 99.61 | +0.750 | 8.88% | 0.641 | 1.081 | 0.438 | 190.11% | -8.66% | -12.30% | -8.93% | S4/S9/S3 | 73.6/69.4/61.8 | ABOVE/ABOVE/ABOVE | 28 | +6.00% | 8.88% | REALIZED_VOL_30D | 95.58 | 2026-08-27 | 87.25 | 103.91 | MEDIUM | L-PX-BBY, L-TI-BBY, L-RM-BBY | Consumer Discretionary momentum/RS leader | rank-order inversion risk (see § Calibration) |
| 3 | IQV | IQVIA Holdings Inc. Common S | 247.56 | 2026-07-29 | HISTORICAL | +0.3169 | 99.42 | +0.152 | 15.86% | 0.359 | 0.968 | 0.401 | 59.67% | -20.16% | -26.66% | -10.23% | S5/S6/S2 | 80.8/70.0/59.6 | ABOVE/ABOVE/BULL_X | 38 | +6.00% | 15.86% | REALIZED_VOL_30D | 262.41 | 2026-08-27 | 221.59 | 303.23 | MEDIUM | L-PX-IQV, L-TI-IQV, L-RM-IQV | Health Care momentum/RS leader | rank-order inversion risk (see § Calibration) |
| 4 | NTAP | NetApp Inc. Common Stock | 173.23 | 2026-07-29 | HISTORICAL | +0.3116 | 99.22 | +1.420 | 12.82% | 0.444 | 0.718 | 0.292 | 91.30% | -15.15% | -20.40% | -15.81% | S7/S4/S4 | 60.6/71.4/69.8 | ABOVE/ABOVE/ABOVE | 27 | +6.00% | 12.82% | REALIZED_VOL_30D | 183.62 | 2026-08-27 | 160.53 | 206.72 | MEDIUM | L-PX-NTAP, L-TI-NTAP, L-RM-NTAP | Technology momentum/RS leader | rank-order inversion risk (see § Calibration) |
| 5 | BXP | BXP Inc. Common Stock | 72.97 | 2026-07-29 | HISTORICAL | +0.2946 | 99.03 | +0.347 | 8.51% | 0.669 | 0.984 | 0.764 | 207.22% | -8.04% | -11.53% | -5.33% | S4/S9/S2 | 70.3/67.9/58.2 | BULL_X/ABOVE/BULL_X | 38 | +6.00% | 8.51% | REALIZED_VOL_30D | 77.35 | 2026-08-27 | 70.89 | 83.80 | MEDIUM | L-PX-BXP, L-TI-BXP, L-RM-BXP | Real Estate momentum/RS leader | rank-order inversion risk (see § Calibration) |
| 6 | TRV | The Travelers Companies Inc. | 389.01 | 2026-07-29 | HISTORICAL | +0.2926 | 98.83 | -0.590 | 9.65% | 0.590 | 1.602 | 0.826 | 161.18% | -9.92% | -13.87% | -5.96% | S9/S9/S9 | 74.7/80.0/77.4 | ABOVE/ABOVE/ABOVE | 38 | +6.00% | 9.65% | REALIZED_VOL_30D | 412.35 | 2026-08-27 | 373.32 | 451.38 | MEDIUM | L-PX-TRV, L-TI-TRV, L-RM-TRV | Finance momentum/RS leader | rank-order inversion risk (see § Calibration) |
| 7 | INCY | Incyte Corp. Common Stock | 127.10 | 2026-07-29 | HISTORICAL | +0.2897 | 98.64 | -0.242 | 11.86% | 0.480 | 2.194 | 0.554 | 106.70% | -13.56% | -18.43% | -9.50% | S4/S9/S2 | 69.9/71.3/76.5 | ABOVE/ABOVE/ABOVE | 38 | +6.00% | 11.86% | REALIZED_VOL_30D | 134.73 | 2026-08-27 | 119.05 | 150.40 | MEDIUM | L-PX-INCY, L-TI-INCY, L-RM-INCY | Health Care momentum/RS leader | rank-order inversion risk (see § Calibration) |
| 8 | GEHC | GE HealthCare Technologies I | 71.90 | 2026-07-29 | HISTORICAL | +0.2831 | 98.44 | -0.256 | 14.84% | 0.383 | 0.817 | 0.521 | 68.10% | -18.49% | -24.57% | -8.17% | S2/S1/S1 | 68.8/54.3/49.2 | BULL_X/BULL_X/BELOW | 38 | +6.00% | 14.84% | REALIZED_VOL_30D | 76.21 | 2026-08-27 | 65.12 | 87.31 | MEDIUM | L-PX-GEHC, L-TI-GEHC, L-RM-GEHC | Health Care momentum/RS leader | rank-order inversion risk (see § Calibration) |
| 9 | FICO | Fair Isaac Corporation Commo | 1373.08 | 2026-07-29 | HISTORICAL | +0.2830 | 98.25 | -0.094 | 11.94% | 0.477 | 0.701 | 0.480 | 105.21% | -13.70% | -18.60% | -15.85% | S3/S5/S1 | 67.9/55.6/48.6 | ABOVE/ABOVE/BELOW | 38 | +6.00% | 11.94% | REALIZED_VOL_30D | 1455.46 | 2026-08-27 | 1284.96 | 1625.97 | MEDIUM | L-PX-FICO, L-TI-FICO, L-RM-FICO | Consumer Discretionary momentum/RS leader | rank-order inversion risk (see § Calibration) |
| 10 | ADP | Automatic Data Processing In | 273.37 | 2026-07-29 | HISTORICAL | +0.2802 | 98.05 | -0.729 | 10.15% | 0.560 | 1.307 | 0.698 | 145.46% | -10.76% | -14.92% | -7.49% | S3/S6/S2 | 73.5/67.5/56.7 | ABOVE/ABOVE/BELOW | 38 | +6.00% | 10.15% | REALIZED_VOL_30D | 289.77 | 2026-08-27 | 260.90 | 318.64 | MEDIUM | L-PX-ADP, L-TI-ADP, L-RM-ADP | Industrials momentum/RS leader | rank-order inversion risk (see § Calibration) |
| 11 | F | Ford Motor Company Common St | 15.28 | 2026-07-29 | HISTORICAL | +0.2777 | 97.86 | +1.730 | 7.95% | 0.716 | 1.604 | 0.382 | 237.39% | -7.12% | -10.37% | -23.39% | S4/S3/S1 | 66.3/59.5/60.0 | ABOVE/ABOVE/ABOVE | 38 | +6.00% | 7.95% | REALIZED_VOL_30D | 16.20 | 2026-08-27 | 14.93 | 17.46 | MEDIUM | L-PX-F, L-TI-F, L-RM-F | Industrials momentum/RS leader | rank-order inversion risk (see § Calibration) |
| 12 | HUM | Humana Inc. Common Stock | 365.41 | 2026-07-29 | HISTORICAL | +0.2763 | 97.66 | +0.620 | 10.98% | 0.518 | 0.715 | 0.440 | 124.40% | -12.12% | -16.62% | -10.75% | B5/B1/S3 | 41.5/64.3/57.8 | BELOW/ABOVE/ABOVE | 38 | +6.00% | 10.98% | REALIZED_VOL_30D | 387.33 | 2026-08-27 | 345.60 | 429.06 | MEDIUM | L-PX-HUM, L-TI-HUM, L-RM-HUM | Health Care momentum/RS leader | rank-order inversion risk (see § Calibration) |
| 13 | CPAY | Corpay Inc. Common Stock | 392.85 | 2026-07-29 | HISTORICAL | +0.2724 | 97.47 | +0.460 | 9.49% | 0.599 | 0.932 | 0.508 | 166.40% | -9.67% | -13.56% | -10.52% | S4/S3/S4 | 69.0/64.7/61.9 | ABOVE/ABOVE/BULL_X | 6 | +6.00% | 9.49% | REALIZED_VOL_30D | 416.42 | 2026-08-27 | 377.63 | 455.21 | LOW | L-PX-CPAY, L-TI-CPAY, L-RM-CPAY | Consumer Discretionary momentum/RS leader | earnings in 6d |
| 14 | PAYX | Paychex Inc. Common Stock | 122.13 | 2026-07-29 | HISTORICAL | +0.2701 | 97.27 | -0.613 | 9.89% | 0.576 | 1.339 | 0.697 | 153.50% | -10.31% | -14.36% | -6.35% | S3/S9/S2 | 76.1/71.8/55.5 | ABOVE/ABOVE/BELOW | 38 | +6.00% | 9.89% | REALIZED_VOL_30D | 129.46 | 2026-08-27 | 116.90 | 142.01 | MEDIUM | L-PX-PAYX, L-TI-PAYX, L-RM-PAYX | Industrials momentum/RS leader | rank-order inversion risk (see § Calibration) |
| 15 | FTNT | Fortinet Inc. Common Stock | 153.22 | 2026-07-29 | HISTORICAL | +0.2698 | 97.08 | +0.925 | 10.40% | 0.547 | 1.773 | 0.347 | 138.55% | -11.17% | -15.43% | -10.10% | S1/B1/S5 | 50.1/74.3/76.5 | BELOW/ABOVE/ABOVE | 38 | +6.00% | 10.40% | REALIZED_VOL_30D | 162.41 | 2026-08-27 | 145.83 | 178.99 | MEDIUM | L-PX-FTNT, L-TI-FTNT, L-RM-FTNT | Technology momentum/RS leader | rank-order inversion risk (see § Calibration) |
| 16 | SJM | The J.M. Smucker Company Com | 126.35 | 2026-07-29 | HISTORICAL | +0.2665 | 96.88 | -0.821 | 9.92% | 0.573 | 1.239 | 0.649 | 152.28% | -10.38% | -14.45% | -8.42% | S9/S3/S1 | 70.8/69.3/60.0 | ABOVE/ABOVE/ABOVE | 27 | +6.00% | 9.92% | REALIZED_VOL_30D | 133.93 | 2026-08-27 | 120.89 | 146.97 | MEDIUM | L-PX-SJM, L-TI-SJM, L-RM-SJM | Consumer Staples momentum/RS leader | rank-order inversion risk (see § Calibration) |
| 17 | MRSH | Marsh Common Stock | 197.59 | 2026-07-29 | HISTORICAL | +0.2531 | 96.69 | -0.909 | 9.62% | 0.591 | 1.300 | 0.838 | 161.94% | -9.88% | -13.83% | -6.28% | S3/S6/S1 | 74.1/65.8/53.6 | ABOVE/ABOVE/BELOW | 38 | +6.00% | 9.62% | REALIZED_VOL_30D | 209.45 | 2026-08-27 | 189.67 | 229.22 | MEDIUM | L-PX-MRSH, L-TI-MRSH, L-RM-MRSH | Finance momentum/RS leader | rank-order inversion risk (see § Calibration) |
| 18 | BRO | Brown & Brown Inc. Common St | 74.87 | 2026-07-29 | HISTORICAL | +0.2513 | 96.49 | -0.954 | 11.45% | 0.497 | 1.367 | 0.680 | 114.46% | -12.89% | -17.58% | -6.59% | S3/S9/S1 | 70.9/59.2/46.4 | ABOVE/ABOVE/BELOW | 38 | +6.00% | 11.45% | REALIZED_VOL_30D | 79.36 | 2026-08-27 | 70.45 | 88.28 | MEDIUM | L-PX-BRO, L-TI-BRO, L-RM-BRO | Finance momentum/RS leader | rank-order inversion risk (see § Calibration) |
| 19 | HPQ | HP Inc. Common Stock | 28.41 | 2026-07-29 | HISTORICAL | +0.2492 | 96.30 | +0.620 | 11.63% | 0.490 | 0.916 | 0.342 | 110.98% | -13.18% | -17.95% | -24.35% | S4/S3/S3 | 72.8/66.3/55.9 | ABOVE/ABOVE/BULL_X | 27 | +6.00% | 11.63% | REALIZED_VOL_30D | 30.11 | 2026-08-27 | 26.68 | 33.55 | MEDIUM | L-PX-HPQ, L-TI-HPQ, L-RM-HPQ | Technology momentum/RS leader | rank-order inversion risk (see § Calibration) |
| 20 | RTX | RTX Corporation Common Stock | 215.25 | 2026-07-29 | HISTORICAL | +0.2359 | 96.10 | -0.020 | 9.65% | 0.590 | 1.092 | 0.694 | 161.03% | -9.92% | -13.88% | -5.58% | S6/S9/S1 | 71.2/67.9/75.4 | ABOVE/ABOVE/ABOVE | 38 | +6.00% | 9.65% | REALIZED_VOL_30D | 228.17 | 2026-08-27 | 206.56 | 249.77 | MEDIUM | L-PX-RTX, L-TI-RTX, L-RM-RTX | Industrials momentum/RS leader | rank-order inversion risk (see § Calibration) |

## Score attribution

| Rank | Ticker | Fund_Z | Tech_Z | Sent_Z | Macro_Z | Composite_Z | DQ | Penalties | Adj Score | Top Positive Drivers | Top Negative Drivers | Metric Ledger Rows |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | GRMN | UNAVAILABLE | +1.4768 | UNAVAILABLE | -0.1964 | +0.4136 | 0.80 | 0.00 | +0.3309 | vol_conf z=+2.43; mom20 z=+1.67; rs20 z=+1.67 | macro:vol_stability z=-1.53; macro:beta z=-0.28; macro:sector_lead z=-0.01 | L-PX-GRMN, L-TI-GRMN, L-RM-GRMN |
| 2 | BBY | UNAVAILABLE | +1.1495 | UNAVAILABLE | +0.4140 | +0.4069 | 0.80 | 0.00 | +0.3256 | macro:vol_stability z=+2.21; mom60 z=+1.88; rs60 z=+1.88 | macro:rate_sens z=-0.77; vol_conf z=-0.43; macro:sector_lead z=-0.11 | L-PX-BBY, L-TI-BBY, L-RM-BBY |
| 3 | IQV | UNAVAILABLE | +1.2193 | UNAVAILABLE | +0.2027 | +0.3962 | 0.80 | 0.00 | +0.3169 | macro:sector_lead z=+1.91; mom60 z=+1.88; rs60 z=+1.88 | macro:vol_stability z=-0.54; macro:beta z=-0.29; macro:rate_sens z=-0.27 | L-PX-IQV, L-TI-IQV, L-RM-IQV |
| 4 | NTAP | UNAVAILABLE | +1.0287 | UNAVAILABLE | +0.5393 | +0.3895 | 0.80 | 0.00 | +0.3116 | macro:vol_stability z=+2.21; mom60 z=+1.88; rs60 z=+1.88 | macro:sector_lead z=-1.21; dd60 z=-0.10 | L-PX-NTAP, L-TI-NTAP, L-RM-NTAP |
| 5 | BXP | UNAVAILABLE | +1.1786 | UNAVAILABLE | +0.0981 | +0.3683 | 0.80 | 0.00 | +0.2946 | vol_conf z=+2.43; macd z=+1.46; mom60 z=+1.35 | macro:vol_stability z=-0.72; macro:beta z=-0.09 | L-PX-BXP, L-TI-BXP, L-RM-BXP |
| 6 | TRV | UNAVAILABLE | +1.3397 | UNAVAILABLE | -0.2414 | +0.3657 | 0.80 | 0.00 | +0.2926 | mom60 z=+1.64; rs60 z=+1.64; vol_conf z=+1.43 | macro:vol_stability z=-1.53; macro:beta z=-1.04 | L-PX-TRV, L-TI-TRV, L-RM-TRV |
| 7 | INCY | UNAVAILABLE | +1.1419 | UNAVAILABLE | +0.1306 | +0.3622 | 0.80 | 0.00 | +0.2897 | macro:sector_lead z=+1.91; rs60 z=+1.85; mom60 z=+1.85 | macro:beta z=-0.69; macro:vol_stability z=-0.51; macro:rate_sens z=-0.18 | L-PX-INCY, L-TI-INCY, L-RM-INCY |
| 8 | GEHC | UNAVAILABLE | +1.0793 | UNAVAILABLE | +0.2004 | +0.3538 | 0.80 | 0.00 | +0.2831 | vol_conf z=+2.43; macro:sector_lead z=+1.91; macd z=+1.46 | macro:vol_stability z=-1.53; macro:beta z=-0.70 | L-PX-GEHC, L-TI-GEHC, L-RM-GEHC |
| 9 | FICO | UNAVAILABLE | +1.0686 | UNAVAILABLE | +0.2211 | +0.3537 | 0.80 | 0.00 | +0.2830 | mom60 z=+1.88; rs60 z=+1.88; vol_conf z=+1.32 | macro:beta z=-0.54; macro:sector_lead z=-0.11; dd60 z=-0.10 | L-PX-FICO, L-TI-FICO, L-RM-FICO |
| 10 | ADP | UNAVAILABLE | +1.3346 | UNAVAILABLE | -0.3342 | +0.3502 | 0.80 | 0.00 | +0.2802 | vol_conf z=+1.89; mom20 z=+1.67; rs20 z=+1.67 | macro:beta z=-1.18; macro:vol_stability z=-0.46; macro:sector_lead z=-0.01 | L-PX-ADP, L-TI-ADP, L-RM-ADP |
| 11 | F | UNAVAILABLE | +0.8688 | UNAVAILABLE | +0.5764 | +0.3471 | 0.80 | 0.00 | +0.2777 | macro:vol_stability z=+2.21; rs60 z=+1.79; mom60 z=+1.79 | macro:rate_sens z=-1.21; dd60 z=-0.94; macro:sector_lead z=-0.01 | L-PX-F, L-TI-F, L-RM-F |
| 12 | HUM | UNAVAILABLE | +0.6167 | UNAVAILABLE | +1.0693 | +0.3454 | 0.80 | 0.00 | +0.2763 | vol_conf z=+2.43; macro:sector_lead z=+1.91; mom60 z=+1.88 | mom20 z=-0.95; rs20 z=-0.95; macd z=-0.20 | L-PX-HUM, L-TI-HUM, L-RM-HUM |
| 13 | CPAY | UNAVAILABLE | +1.3519 | UNAVAILABLE | +0.3998 | +0.4655 | 0.80 | 0.10 | +0.2724 | vol_conf z=+2.08; mom60 z=+1.62; rs60 z=+1.62 | macro:sector_lead z=-0.11 | L-PX-CPAY, L-TI-CPAY, L-RM-CPAY |
| 14 | PAYX | UNAVAILABLE | +1.2530 | UNAVAILABLE | -0.2554 | +0.3376 | 0.80 | 0.00 | +0.2701 | mom60 z=+1.88; rs60 z=+1.88; mom20 z=+1.67 | macro:beta z=-1.07; macro:vol_stability z=-0.41; macro:sector_lead z=-0.01 | L-PX-PAYX, L-TI-PAYX, L-RM-PAYX |
| 15 | FTNT | UNAVAILABLE | +0.8024 | UNAVAILABLE | +0.6435 | +0.3372 | 0.80 | 0.00 | +0.2698 | vol_conf z=+2.43; macro:vol_stability z=+2.21; mom60 z=+1.88 | macro:sector_lead z=-1.21; mom20 z=-0.25; rs20 z=-0.25 | L-PX-FTNT, L-TI-FTNT, L-RM-FTNT |
| 16 | SJM | UNAVAILABLE | +1.0146 | UNAVAILABLE | +0.1914 | +0.3331 | 0.80 | 0.00 | +0.2665 | mom60 z=+1.88; rs60 z=+1.88; ma_align z=+1.29 | macro:beta z=-1.28; vol_conf z=-0.38 | L-PX-SJM, L-TI-SJM, L-RM-SJM |
| 17 | MRSH | UNAVAILABLE | +1.1414 | UNAVAILABLE | -0.1734 | +0.3164 | 0.80 | 0.00 | +0.2531 | vol_conf z=+1.78; mom20 z=+1.53; rs20 z=+1.53 | macro:beta z=-1.37; macro:vol_stability z=-0.98 | L-PX-MRSH, L-TI-MRSH, L-RM-MRSH |
| 18 | BRO | UNAVAILABLE | +1.0666 | UNAVAILABLE | -0.0391 | +0.3141 | 0.80 | 0.00 | +0.2513 | mom60 z=+1.79; rs60 z=+1.79; mom20 z=+1.30 | macro:beta z=-1.37; macro:vol_stability z=-0.87 | L-PX-BRO, L-TI-BRO, L-RM-BRO |
| 19 | HPQ | UNAVAILABLE | +0.9482 | UNAVAILABLE | +0.1801 | +0.3115 | 0.80 | 0.00 | +0.2492 | macro:vol_stability z=+2.20; mom60 z=+1.88; rs60 z=+1.88 | macro:sector_lead z=-1.21; dd60 z=-1.05; macro:rate_sens z=-0.45 | L-PX-HPQ, L-TI-HPQ, L-RM-HPQ |
| 20 | RTX | UNAVAILABLE | +1.1231 | UNAVAILABLE | -0.2806 | +0.2949 | 0.80 | 0.00 | +0.2359 | mom60 z=+1.35; rs60 z=+1.35; ma_align z=+1.29 | macro:vol_stability z=-0.83; macro:beta z=-0.46; macro:sector_lead z=-0.01 | L-PX-RTX, L-TI-RTX, L-RM-RTX |

Worked example — **GRMN** (rank 1): (0.30*UNAVAIL + 0.30*+1.4768 + 0.25*UNAVAIL + 0.15*-0.1964) * 0.80 - 0.00 = +0.3309. Reading it: `Fund_Z` and
`Sent_Z` contribute nothing because they are `UNAVAILABLE` (not because they are neutral);
`Tech_Z` +1.4768 and `Macro_Z` -0.1964 carry the
whole score; the 0.80 multiplier then shrinks it for those same gaps.

## Metric availability

| Metric group | Sourceable | `UNAVAILABLE` | DQ / confidence effect | Notes |
|---|---|---|---|---|
| Momentum / RS / MA / MACD / RSI / TD-9 / volume | 513 | 0 | none | `technical_indicators.json` |
| Beta, tracking error, drawdown, VaR/CVaR, Kelly | 513 | 0 | none | DERIVED from 60d returns |
| Sharpe, Sortino, Treynor, Calmar | 513 | 0 | none | rf sourced (3.70% 13-week bill), so **not** `RAW_DIAGNOSTIC` |
| Earnings distance | 513 | 0 | penalty input | forward calendar sweep |
| Fundamental inputs | 0 | 513 | family `UNAVAILABLE`; DQ → 0.80 | blocks Evidence Threshold 2 |
| Sentiment inputs | 0 | 513 | family `UNAVAILABLE`; DQ → 0.80 | blocks Evidence Threshold 2 |
| Options IV30 | 0 | 513 | Enhancing only | sigma falls to chain step 2 |

**Sortino uses true downside deviation** — the standard deviation of *negative* daily returns
over the last 30 sessions scaled by `sqrt(21)` — not the total sigma used for Sharpe. (The
2026-07-17 and 2026-07-20 packages had these identical; the bug was fixed 2026-07-21 and the
correct definition is carried here.)

## Technical indicator summary (top 20)

| Ticker | TD9 D/W/M | RSI14 D/W/M | MACD State D/W/M | MACD Hist D/W/M | MA Align D/W/M | 20/60d Mom | RS20/60 vs SPY | Indicator Ledger Rows |
|---|---|---|---|---|---|---|---|---|
| GRMN | S3/S5/S1 | 80.0/71.0/68.7 | ABOVE/BULL_X/BULL_X | 3.399/3.030/2.848 | BULL/BULL/BULL | 24.1%/22.2% | 26.4%/20.7% | L-TI-GRMN |
| BBY | S4/S9/S3 | 73.6/69.4/61.8 | ABOVE/ABOVE/ABOVE | 0.209/2.609/1.749 | BULL/BULL/BULL | 18.8%/52.2% | 21.1%/50.7% | L-TI-BBY |
| IQV | S5/S6/S2 | 80.8/70.0/59.6 | ABOVE/ABOVE/BULL_X | 3.107/7.536/3.781 | BULL/UNAVAIL/UNAVAIL | 28.1%/56.9% | 30.4%/55.4% | L-TI-IQV |
| NTAP | S7/S4/S4 | 60.6/71.4/69.8 | ABOVE/ABOVE/ABOVE | 0.346/3.025/6.207 | BULL/BULL/BULL | 12.3%/55.0% | 14.6%/53.5% | L-TI-NTAP |
| BXP | S4/S9/S2 | 70.3/67.9/58.2 | BULL_X/ABOVE/BULL_X | 0.113/1.637/0.309 | BULL/UNAVAIL/BULL | 10.0%/24.2% | 12.4%/22.7% | L-TI-BXP |
| TRV | S9/S9/S9 | 74.7/80.0/77.4 | ABOVE/ABOVE/ABOVE | 3.343/8.700/6.106 | BULL/BULL/BULL | 17.8%/28.2% | 20.2%/26.7% | L-TI-TRV |
| INCY | S4/S9/S2 | 69.9/71.3/76.5 | ABOVE/ABOVE/ABOVE | 0.640/2.372/3.255 | BULL/BULL/BULL | 12.1%/31.1% | 14.4%/29.7% | L-TI-INCY |
| GEHC | S2/S1/S1 | 68.8/54.3/49.2 | BULL_X/BULL_X/BELOW | 0.509/0.653/-1.459 | BULL/UNAVAIL/UNAVAIL | 12.4%/17.9% | 14.7%/16.4% | L-TI-GEHC |
| FICO | S3/S5/S1 | 67.9/55.6/48.6 | ABOVE/ABOVE/BELOW | 9.423/40.928/-76.036 | BULL/UNAVAIL/UNAVAIL | 14.9%/32.6% | 17.2%/31.1% | L-TI-FICO |
| ADP | S3/S6/S2 | 73.5/67.5/56.7 | ABOVE/ABOVE/BELOW | 1.417/7.660/-4.771 | BULL/UNAVAIL/BULL | 22.1%/28.6% | 24.4%/27.1% | L-TI-ADP |
| F | S4/S3/S1 | 66.3/59.5/60.0 | ABOVE/ABOVE/ABOVE | 0.139/0.059/0.384 | UNAVAIL/BULL/BULL | 9.9%/30.2% | 12.2%/28.8% | L-TI-F |
| HUM | B5/B1/S3 | 41.5/64.3/57.8 | BELOW/ABOVE/ABOVE | -5.886/8.629/20.895 | UNAVAIL/BULL/UNAVAIL | -8.0%/56.8% | -5.7%/55.3% | L-TI-HUM |
| CPAY | S4/S3/S4 | 69.0/64.7/61.9 | ABOVE/ABOVE/BULL_X | 2.735/4.575/4.062 | BULL/BULL/BULL | 17.9%/27.9% | 20.2%/26.4% | L-TI-CPAY |
| PAYX | S3/S9/S2 | 76.1/71.8/55.5 | ABOVE/ABOVE/BELOW | 0.775/3.708/-1.976 | BULL/UNAVAIL/BULL | 25.5%/34.4% | 27.8%/32.9% | L-TI-PAYX |
| FTNT | S1/B1/S5 | 50.1/74.3/76.5 | BELOW/ABOVE/ABOVE | -2.082/2.642/6.322 | UNAVAIL/BULL/BULL | -0.3%/77.6% | 2.1%/76.1% | L-TI-FTNT |
| SJM | S9/S3/S1 | 70.8/69.3/60.0 | ABOVE/ABOVE/ABOVE | 1.136/2.119/2.293 | BULL/BULL/UNAVAIL | 12.3%/31.7% | 14.6%/30.3% | L-TI-SJM |
| MRSH | S3/S6/S1 | 74.1/65.8/53.6 | ABOVE/ABOVE/BELOW | 1.348/3.874/-3.010 | BULL/UNAVAIL/BULL | 19.2%/19.6% | 21.5%/18.1% | L-TI-MRSH |
| BRO | S3/S9/S1 | 70.9/59.2/46.4 | ABOVE/ABOVE/BELOW | 0.342/2.384/-3.599 | BULL/UNAVAIL/UNAVAIL | 16.7%/30.3% | 19.0%/28.8% | L-TI-BRO |
| HPQ | S4/S3/S3 | 72.8/66.3/55.9 | ABOVE/ABOVE/BULL_X | 0.446/0.586/0.309 | BULL/UNAVAIL/UNAVAIL | 29.5%/38.0% | 31.8%/36.6% | L-TI-HPQ |
| RTX | S6/S9/S1 | 71.2/67.9/75.4 | ABOVE/ABOVE/ABOVE | 2.021/2.708/1.801 | BULL/BULL/BULL | 13.4%/24.2% | 15.8%/22.8% | L-TI-RTX |

TD-9 `9` prints and RSI ≥ 70 / ≤ 30 are treated as exhaustion flags feeding `Tech_Z`, penalties
and confidence — never as standalone trade signals. MACD is counted supportive only where it
aligns with momentum and relative strength.

## Penalties applied

| Ticker | Rank | Penalty | Reason |
|---|---|---|---|
| CPAY | 13 | −0.10 | earnings in 6d (<=14d): -0.10 |
| DVA | 23 | −0.10 | earnings in 5d (<=14d): -0.10 |

## Investable subset

**Empty — zero names qualify.** This is the run's central result, so the arithmetic is shown
explicitly against `rules.md § Evidence Thresholds`:

| # | Threshold | Best available | Pass? |
|---|---|---|---|
| 1 | Adjusted-score percentile ≥ 80th | 99.81 (top name); 102 names ≥ 80th | **PASS** |
| 2 | ≥ 3 of 4 factor families non-negative | **2 of 4 families exist at all**; `Fund_Z`/`Sent_Z` are `UNAVAILABLE` and may not be counted | **FAIL** |
| 3 | No family > 50% of conviction | `Tech_Z` carries 0.30/0.45 = 66.7% of the live weight | **FAIL** |
| 4 | Data completeness ≥ 85% | DQ = 0.80 | **FAIL** |
| 5 | No hard stop from `§ Stop Criteria` | none triggered | PASS |

Three independent thresholds fail, all tracing to the same root cause. Fewer than 5 names pass
⇒ **`NO_TRADE`** per `rules.md § Downgrade to NO_TRADE` #1.

## Monitoring sleeve (published)

All **24** published records are monitoring-sleeve forecasts, not recommendations. They
carry full `mu`/`sigma`/CI so they are settleable — `REVIEW_ONLY`/`NO_TRADE` status governs what
may be executed, never whether a forecast is recorded. Ranks are contiguous **1–24**:
every name in the universe is earnings-grounded this run, so the "skip ungrounded names" rule
that shaped the 2026-07-27 and 2026-07-28 published sets does not apply.

## Near-miss rejection list (ranks 25–30)

| Rank | Ticker | Adj Score | Pctl | Why not investable |
|---|---|---|---|---|
| 25 | ABT | +0.2171 | 95.13 | below the 85% data-completeness bar (DQ 0.80) and only 2 of 4 families available |
| 26 | MMM | +0.2153 | 94.93 | below the 85% data-completeness bar (DQ 0.80) and only 2 of 4 families available |
| 27 | EXR | +0.2120 | 94.74 | below the 85% data-completeness bar (DQ 0.80) and only 2 of 4 families available |
| 28 | AON | +0.2105 | 94.54 | below the 85% data-completeness bar (DQ 0.80) and only 2 of 4 families available |
| 29 | GM | +0.2098 | 94.35 | below the 85% data-completeness bar (DQ 0.80) and only 2 of 4 families available |
| 30 | PM | +0.2009 | 94.15 | below the 85% data-completeness bar (DQ 0.80) and only 2 of 4 families available |

## What drives the leaderboard — and why that is a warning

The live weight sits 66.7% on `Tech_Z`, which is built from 20d/60d momentum and
relative strength. That is a **trend-persistence** signal: it necessarily ranks the last 60
days' winners first. Over the settlement window just closed, those winners were defensives
(semis collapsed -17.89%), so the leaderboard above is heavily defensive —
16 of the 24 published names carry a
60-day beta below 0.5, and 12 are outright
negative.

`10_midday_monitor.md` records what happened to exactly that book within an hour of this run
firing. It is the clearest available evidence for the rank-inversion diagnosis in `13`.
