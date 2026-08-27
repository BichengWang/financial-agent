# 06 — Top Candidates · 2026-08-27

Inherited from `05` with **no new facts**. Investable set: **0 names**. Monitoring sleeve:
**24 names**, ranks 1–24 contiguous.

## Why the investable set is empty

| Gate | Result |
|---|---|
| Evidence threshold 1 — percentile >= 80th | passes; the whole published sleeve sits at or above the 95.47th percentile |
| Evidence threshold 2 — >= 3 of 4 families non-negative | **fails universe-wide**: `Fund_Z` and `Sent_Z` are `UNAVAILABLE` for every name (L021, L022), so at most 2 of 4 families can ever be non-negative today |
| Evidence threshold 3 — no family above 50% of conviction | **fails by construction**: with two families live the composite is `0.30*Tech_Z + 0.15*Macro_Z`, i.e. Technical carries 66.7% |
| Evidence threshold 4 — data completeness >= 85% | **fails**: two of four families unsourceable puts completeness at 80%, which is also the data-quality multiplier (0.80, L020) |
| Evidence threshold 5 — no hard stop | passes; no hard-halt criterion fires (`03`) |

Thresholds 2, 3 and 4 all fail for the same single cause — no fetch path is wired for the
fundamental and sentiment families — so no ranking outcome could have produced an investable name
today. That is a **capability gap**, not a market judgment, and it is why the status is `NO_TRADE`
rather than `REVIEW_ONLY`: the data that *is* required is fully grounded (`01` GO-Gate Table), and
the candidate set simply does not clear the bar.

## Monitoring sleeve (24 names)

Each row carries the compact score trace, the key financial metrics and the technical indicator
states needed to see why the name cleared the ranking floor and missed the investable threshold.

| Rank | Ticker | Company | Sector | Entry | Adj Score | Pctl | Score Trace | mu | sigma | Target | 70% CI | Beta | Sharpe | IR | Kelly 0.25 | Max DD60 | TD9 D/W/M | RSI14 D/W/M | MACD D/W/M | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | SJM | The J.M. Smucker Company Common St | Consumer Staples | 131.84 | +0.3392 | 100.00 | (0.30x`UNAVL` + 0.30x+1.4397 + 0.25x`UNAVL` + 0.15x-0.0531) x 0.80 - 0.00 = +0.3392 | +6.00% | 8.68% | 139.75 | 127.85 – 151.65 | -0.6986 | 0.6559 | 0.7058 | 1.9916 | -8.42% | SELL_SETUP_9 / SELL_SETUP_7 / SELL_SETUP_2 | 72.13 / 74.47 / 62.99 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | MEDIUM |
| 2 | RVTY | Revvity Inc. Common Stock | Industrials | 129.71 | +0.3357 | 99.80 | (0.30x`UNAVL` + 0.30x+1.3875 + 0.25x`UNAVL` + 0.15x+0.0221) x 0.80 - 0.00 = +0.3357 | +6.00% | 9.93% | 137.49 | 124.10 – 150.89 | +0.4440 | 0.5733 | 0.4929 | 1.5216 | -6.38% | SELL_SETUP_7 / SELL_SETUP_4 / SELL_SETUP_3 | 72.24 / 71.60 / 60.14 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | MEDIUM |
| 3 | GILD | Gilead Sciences Inc. Common Stock | Health Care | 148.86 | +0.2983 | 99.61 | (0.30x`UNAVL` + 0.30x+0.8990 + 0.25x`UNAVL` + 0.15x+0.6874) x 0.80 - 0.00 = +0.2983 | +6.00% | 7.47% | 157.79 | 146.22 – 169.36 | +0.1043 | 0.7616 | 0.6795 | 2.6852 | -5.96% | SELL_SETUP_9 / SELL_SETUP_4 / SELL_SETUP_1 | 69.18 / 66.84 / 71.11 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `BULLISH_CROSS` | MEDIUM |
| 4 | BLK | BlackRock Inc. Common Stock | Finance | 1167.57 | +0.2977 | 99.41 | (0.30x`UNAVL` + 0.30x+0.7774 + 0.25x`UNAVL` + 0.15x+0.9256) x 0.80 - 0.00 = +0.2977 | +6.00% | 6.76% | 1237.62 | 1155.49 – 1319.76 | +0.8465 | 0.8416 | 0.5806 | 3.2784 | -10.14% | SELL_SETUP_5 / SELL_SETUP_9 / SELL_SETUP_2 | 61.03 / 62.38 / 61.23 | `BELOW_SIGNAL` / `ABOVE_SIGNAL` / `BELOW_SIGNAL` | MEDIUM |
| 5 | AMGN | Amgen Inc. Common Stock | Health Care | 436.99 | +0.2949 | 99.21 | (0.30x`UNAVL` + 0.30x+1.0188 + 0.25x`UNAVL` + 0.15x+0.4200) x 0.80 - 0.00 = +0.2949 | +6.00% | 7.75% | 463.21 | 427.99 – 498.43 | +0.1414 | 0.7346 | 0.7285 | 2.4978 | -5.05% | BUY_SETUP_1 / SELL_SETUP_9 / SELL_SETUP_2 | 68.94 / 74.38 / 71.79 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | MEDIUM |
| 6 | JNJ | Johnson & Johnson Common Stock | Health Care | 265.77 | +0.2918 | 99.02 | (0.30x`UNAVL` + 0.30x+0.9190 + 0.25x`UNAVL` + 0.15x+0.5937) x 0.80 - 0.00 = +0.2918 | +6.00% | 6.20% | 281.72 | 264.57 – 298.86 | -0.7412 | 0.9179 | 1.1124 | 3.9001 | -7.57% | BUY_SETUP_1 / SELL_SETUP_4 / SELL_SETUP_9 | 54.62 / 63.93 / 77.55 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | MEDIUM |
| 7 | RMD | ResMed Inc. Common Stock | Health Care | 235.76 | +0.2915 | 98.82 | (0.30x`UNAVL` + 0.30x+0.9423 + 0.25x`UNAVL` + 0.15x+0.5445) x 0.80 - 0.00 = +0.2915 | +6.00% | 9.85% | 249.91 | 225.74 – 274.07 | +0.1495 | 0.5776 | 0.5375 | 1.5446 | -12.68% | SELL_SETUP_7 / SELL_SETUP_5 / SELL_SETUP_1 | 66.40 / 59.71 / 51.93 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `BELOW_SIGNAL` | MEDIUM |
| 8 | A | Agilent Technologies Inc. Common S | Industrials | 157.69 | +0.2907 | 98.62 | (0.30x`UNAVL` + 0.30x+1.2053 + 0.25x`UNAVL` + 0.15x+0.0121) x 0.80 - 0.00 = +0.2907 | +6.00% | 8.26% | 167.15 | 153.60 – 180.70 | +0.3635 | 0.6891 | 0.6450 | 2.1981 | -10.15% | BUY_SETUP_3 / SELL_SETUP_8 / SELL_SETUP_4 | 70.27 / 69.14 / 60.38 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | MEDIUM |
| 9 | VEEV | Veeva Systems Inc. Class A Common  | Technology | 282.13 | +0.2901 | 98.43 | (0.30x`UNAVL` + 0.30x+1.3802 + 0.25x`UNAVL` + 0.15x-0.3429) x 0.80 - 0.00 = +0.2901 | +6.00% | 16.61% | 299.06 | 250.31 – 347.80 | +0.4655 | 0.3427 | 0.3424 | 0.5435 | -16.28% | SELL_SETUP_1 / SELL_SETUP_9 / SELL_SETUP_2 | 79.57 / 73.59 / 60.55 | `BULLISH_CROSS` / `ABOVE_SIGNAL` / `BELOW_SIGNAL` | MEDIUM |
| 10 | NWSA | News Corporation Class A Common St | Consumer Discretionary | 31.19 | +0.2868 | 98.23 | (0.30x`UNAVL` + 0.30x+1.2435 + 0.25x`UNAVL` + 0.15x-0.0965) x 0.80 - 0.00 = +0.2868 | +6.00% | 8.39% | 33.06 | 30.34 – 35.78 | -0.3845 | 0.6784 | 0.8330 | 2.1303 | -9.72% | SELL_SETUP_9 / SELL_SETUP_8 / SELL_SETUP_3 | 71.28 / 69.40 / 62.49 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `BELOW_SIGNAL` | MEDIUM |
| 11 | FTNT | Fortinet Inc. Common Stock | Technology | 172.78 | +0.2842 | 98.03 | (0.30x`UNAVL` + 0.30x+1.0794 + 0.25x`UNAVL` + 0.15x+0.2095) x 0.80 - 0.00 = +0.2842 | +6.00% | 12.43% | 183.15 | 160.81 – 205.49 | +1.1979 | 0.4578 | 0.3310 | 0.9703 | -10.40% | SELL_SETUP_3 / SELL_SETUP_2 / SELL_SETUP_6 | 64.73 / 75.31 / 80.05 | `BULLISH_CROSS` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | MEDIUM |
| 12 | STT | State Street Corporation Common St | Finance | 193.37 | +0.2784 | 97.83 | (0.30x`UNAVL` + 0.30x+0.7371 + 0.25x`UNAVL` + 0.15x+0.8453) x 0.80 - 0.00 = +0.2784 | +6.00% | 6.74% | 204.97 | 191.42 – 218.52 | +0.6448 | 0.8449 | 0.7246 | 3.3046 | -5.65% | SELL_SETUP_3 / SELL_SETUP_9 / SELL_SETUP_9 | 62.10 / 81.83 / 88.76 | `BULLISH_CROSS` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | MEDIUM |
| 13 | BNY | The Bank of New York Mellon Corpor | Finance | 162.24 | +0.2774 | 97.64 | (0.30x`UNAVL` + 0.30x+0.6397 + 0.25x`UNAVL` + 0.15x+1.0325) x 0.80 - 0.00 = +0.2774 | +6.00% | 5.60% | 171.97 | 162.52 – 181.43 | +0.4917 | 1.0161 | 0.7819 | 4.7788 | -5.69% | SELL_SETUP_3 / SELL_SETUP_9 / SELL_SETUP_9 | 57.46 / 75.98 / 91.33 | `BELOW_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | MEDIUM |
| 14 | SCHW | Charles Schwab Corporation (The) C | Finance | 108.05 | +0.2760 | 97.44 | (0.30x`UNAVL` + 0.30x+0.8276 + 0.25x`UNAVL` + 0.15x+0.6445) x 0.80 - 0.00 = +0.2760 | +6.00% | 5.68% | 114.53 | 108.15 – 120.92 | -0.1050 | 1.0017 | 0.9387 | 4.6448 | -5.36% | BUY_SETUP_2 / SELL_SETUP_9 / SELL_SETUP_2 | 51.69 / 64.25 / 66.76 | `BELOW_SIGNAL` / `ABOVE_SIGNAL` / `BULLISH_CROSS` | MEDIUM |
| 15 | NWS | News Corporation Class B Common St | Consumer Discretionary | 35.32 | +0.2752 | 97.24 | (0.30x`UNAVL` + 0.30x+1.1709 + 0.25x`UNAVL` + 0.15x-0.0487) x 0.80 - 0.00 = +0.2752 | +6.00% | 8.74% | 37.44 | 34.23 – 40.65 | -0.4122 | 0.6512 | 0.7939 | 1.9632 | -10.48% | SELL_SETUP_9 / SELL_SETUP_8 / SELL_SETUP_3 | 70.10 / 67.64 / 61.99 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `BELOW_SIGNAL` | MEDIUM |
| 16 | VRTX | Vertex Pharmaceuticals Incorporate | Health Care | 547.55 | +0.2724 | 97.05 | (0.30x`UNAVL` + 0.30x+0.9129 + 0.25x`UNAVL` + 0.15x+0.4441) x 0.80 - 0.00 = +0.2724 | +6.00% | 8.43% | 580.40 | 532.39 – 628.41 | +0.1165 | 0.6752 | 0.6633 | 2.1103 | -11.12% | BUY_SETUP_1 / SELL_SETUP_4 / SELL_SETUP_2 | 65.06 / 68.87 / 63.34 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `BULLISH_CROSS` | MEDIUM |
| 17 | BAC | Bank of America Corporation Common | Finance | 61.17 | +0.2701 | 96.85 | (0.30x`UNAVL` + 0.30x+0.7732 + 0.25x`UNAVL` + 0.15x+0.7048) x 0.80 - 0.00 = +0.2701 | +6.00% | 4.79% | 64.84 | 61.80 – 67.88 | +0.3191 | 1.1895 | 1.0138 | 6.5499 | -5.62% | BUY_SETUP_1 / BUY_SETUP_2 / SELL_SETUP_3 | 43.15 / 62.35 / 70.00 | `BELOW_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | MEDIUM |
| 18 | MPC | Marathon Petroleum Corporation Com | Energy | 363.54 | +0.2670 | 96.65 | (0.30x`UNAVL` + 0.30x+1.3078 + 0.25x`UNAVL` + 0.15x-0.3904) x 0.80 - 0.00 = +0.2670 | +6.00% | 10.59% | 385.35 | 345.33 – 425.37 | -0.2006 | 0.5378 | 0.6252 | 1.3387 | -9.09% | SELL_SETUP_2 / SELL_SETUP_9 / SELL_SETUP_7 | 69.54 / 76.64 / 85.17 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | MEDIUM |
| 19 | CRL | Charles River Laboratories Interna | Health Care | 296.41 | +0.2641 | 96.46 | (0.30x`UNAVL` + 0.30x+0.9789 + 0.25x`UNAVL` + 0.15x+0.2429) x 0.80 - 0.00 = +0.2641 | +6.00% | 13.32% | 314.19 | 273.15 – 355.24 | +0.5021 | 0.4275 | 0.4094 | 0.8460 | -6.38% | SELL_SETUP_7 / SELL_SETUP_9 / SELL_SETUP_3 | 73.88 / 77.28 / 67.05 | `BEARISH_CROSS` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | MEDIUM |
| 20 | BMY | Bristol-Myers Squibb Company Commo | Health Care | 66.95 | +0.2633 | 96.26 | (0.30x`UNAVL` + 0.30x+0.6392 + 0.25x`UNAVL` + 0.15x+0.9162) x 0.80 - 0.00 = +0.2633 | +6.00% | 6.73% | 70.97 | 66.28 – 75.65 | +0.0222 | 0.8463 | 0.7006 | 3.3151 | -5.71% | BUY_SETUP_1 / SELL_SETUP_9 / SELL_SETUP_2 | 60.33 / 68.54 / 66.75 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | MEDIUM |
| 21 | TGT | Target Corporation Common Stock | Consumer Discretionary | 165.93 | +0.2614 | 96.06 | (0.30x`UNAVL` + 0.30x+1.1096 + 0.25x`UNAVL` + 0.15x-0.0407) x 0.80 - 0.00 = +0.2614 | +6.00% | 8.64% | 175.89 | 160.97 – 190.80 | +0.0147 | 0.6586 | 0.6193 | 2.0080 | -10.69% | SELL_SETUP_7 / SELL_SETUP_5 / SELL_SETUP_9 | 68.99 / 75.58 / 70.45 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | MEDIUM |
| 22 | TECH | Bio-Techne Corp Common Stock | Health Care | 72.48 | +0.2568 | 95.87 | (0.30x`UNAVL` + 0.30x+0.4908 + 0.25x`UNAVL` + 0.15x+1.1583) x 0.80 - 0.00 = +0.2568 | +6.00% | 1.18% | 76.83 | 75.94 – 77.72 | +0.6904 | 4.8104 | 0.3459 | 107.1161 | -4.02% | SELL_SETUP_2 / SELL_SETUP_9 / SELL_SETUP_3 | 69.49 / 65.96 / 55.49 | `BELOW_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | MEDIUM |
| 23 | PFE | Pfizer Inc. Common Stock | Health Care | 28.02 | +0.2556 | 95.67 | (0.30x`UNAVL` + 0.30x+0.7495 + 0.25x`UNAVL` + 0.15x+0.6313) x 0.80 - 0.00 = +0.2556 | +6.00% | 5.92% | 29.70 | 27.97 – 31.43 | +0.0138 | 0.9609 | 0.9310 | 4.2741 | -9.69% | BUY_SETUP_1 / SELL_SETUP_6 / SELL_SETUP_1 | 65.39 / 66.78 / 58.24 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | MEDIUM |
| 24 | ABT | Abbott Laboratories Common Stock | Health Care | 111.59 | +0.2554 | 95.47 | (0.30x`UNAVL` + 0.30x+0.6296 + 0.25x`UNAVL` + 0.15x+0.8693) x 0.80 - 0.00 = +0.2554 | +6.00% | 6.24% | 118.29 | 111.04 – 125.53 | -0.4252 | 0.9119 | 0.7271 | 3.8493 | -7.18% | BUY_SETUP_2 / SELL_SETUP_9 / SELL_SETUP_2 | 57.65 / 60.30 / 50.65 | `BELOW_SIGNAL` / `ABOVE_SIGNAL` / `BELOW_SIGNAL` | MEDIUM |

Confidence is `MEDIUM` for all 24 — capped by the negative aggregate rank IC binding in
`05`, not chosen per name. No name carries an earnings penalty: the complete forward sweep
(L010) reads `NO_PRINT_IN_WINDOW` for every published ticker.

## Near-miss rejection notes

Names ranked below the 60th percentile are not ranked in either sleeve and appear only in the
rejection accounting (`rules.md § mu Calibration Table`). Of the 509 scored names,
204 sit at or above the 60th percentile and are
therefore rankable; this package publishes the top 24 of them, matching the sleeve size used
by the recent claude-opus-5 packages.

Two names carried forward from the `claude-opus-5-2026-07-30` baseline
survive into today's sleeve: `FTNT`, `SJM`. The other
22 were `DOWNGRADE`d or `DROP`ped on
today's percentile (`02 § 5`).
