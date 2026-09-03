# 06 — Top Candidates · 2026-09-03

Inherited from `05` with **no new facts**. Investable set: **0 names**. Monitoring sleeve:
**24 names**, ranks 1-24 contiguous.

## Why the investable set is empty

| Gate | Result |
|---|---|
| Evidence threshold 1 — percentile >= 80th | **passes**; the whole published sleeve sits at or above the 95.46th percentile |
| Evidence threshold 2 — >= 3 of 4 families non-negative | **fails universe-wide**: `Fund_Z` and `Sent_Z` are `UNAVAILABLE` for every name (L021, L022), so at most 2 of 4 families can ever be non-negative today |
| Evidence threshold 3 — no family above 50% of conviction | **fails by construction**: with two families live the composite is `0.30*Tech_Z + 0.15*Macro_Z`, i.e. Technical carries 66.7% |
| Evidence threshold 4 — data completeness >= 85% | **fails**: two of four families unsourceable puts completeness at 80%, which is also the data-quality multiplier (0.80, L020) |
| Evidence threshold 5 — no hard stop | **passes**; no hard-halt criterion fires (`03 § Stop-rule check`) |

Thresholds 2, 3 and 4 all fail for the same single cause — no fetch path is wired for the
fundamental and sentiment families — so no ranking outcome could have produced an investable name
today. That is a **capability gap**, not a market judgment, and it is why the status is `NO_TRADE`
rather than `REVIEW_ONLY`: the data that *is* required is fully grounded (`01` GO-Gate Table), and
the candidate set simply does not clear the bar.

It is worth stating what is **not** the blocker this run. The sleeve-beta band is
**feasible** (-0.6671 to +1.4337
against the 0.90-1.10 band, `L016`), unlike 2026-08-22 and 2026-08-27 where it was provably
infeasible. Feasibility is recomputed every run; neither narrative may be reused.

## Monitoring sleeve (24 names)

Each row carries the compact score trace, the key financial metrics and the technical indicator
states needed to see why the name cleared the ranking floor and missed the investable threshold.

| Rank | Ticker | Company | Sector | Entry | Adj Score | Pctl | Score Trace | mu | sigma | Target | 70% CI | Beta | Sharpe | IR | Kelly 0.25 | Max DD60 | TD9 D/W/M | RSI14 D/W/M | MACD D/W/M | Days to Earnings | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | VLO | Valero Energy Corporation Common S | Energy | 370.69 | +0.3727 | 100.00 | (0.30x`UNAVL` + 0.30x+1.4152 + 0.25x`UNAVL` + 0.15x+0.2756) x 0.80 - 0.00 = +0.3727 | +6.00% | 8.44% | 392.93 | 360.41 - 425.45 | -0.3804 | +0.6742 | +0.6754 | +2.1080 | -8.65% | SELL_SETUP_5 / SELL_SETUP_9 / SELL_SETUP_9 | 75.26 / 78.49 / 87.07 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | none in 37d | MEDIUM |
| 2 | SPGI | S&P Global Inc. Common Stock | Finance | 450.58 | +0.3607 | 99.80 | (0.30x`UNAVL` + 0.30x+1.0592 + 0.25x`UNAVL` + 0.15x+0.8874) x 0.80 - 0.00 = +0.3607 | +6.00% | 7.75% | 477.61 | 441.29 - 513.93 | +0.0145 | +0.7338 | +0.6046 | +2.4969 | -11.40% | SELL_SETUP_1 / SELL_SETUP_3 / SELL_SETUP_3 | 63.17 / 57.77 / 52.49 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `BELOW_SIGNAL` | none in 37d | MEDIUM |
| 3 | PFG | Principal Financial Group Inc Comm | Finance | 118.51 | +0.3554 | 99.61 | (0.30x`UNAVL` + 0.30x+1.2136 + 0.25x`UNAVL` + 0.15x+0.5348) x 0.80 - 0.00 = +0.3554 | +6.00% | 7.54% | 125.62 | 116.32 - 134.92 | +0.2053 | +0.7541 | +0.7718 | +2.6369 | -6.16% | SELL_SETUP_1 / SELL_SETUP_1 / SELL_SETUP_9 | 68.60 / 70.87 / 74.48 | `BULLISH_CROSS` / `BULLISH_CROSS` / `ABOVE_SIGNAL` | none in 37d | MEDIUM |
| 4 | GILD | Gilead Sciences Inc. Common Stock | Health Care | 151.19 | +0.3390 | 99.41 | (0.30x`UNAVL` + 0.30x+1.1288 + 0.25x`UNAVL` + 0.15x+0.5676) x 0.80 - 0.00 = +0.3390 | +6.00% | 7.45% | 160.26 | 148.54 - 171.98 | +0.0885 | +0.7631 | +0.6767 | +2.7005 | -5.17% | SELL_SETUP_3 / SELL_SETUP_5 / SELL_SETUP_2 | 68.29 / 68.28 / 71.99 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | none in 37d | MEDIUM |
| 5 | AMP | Ameriprise Financial Inc. Common S | Finance | 565.08 | +0.3354 | 99.21 | (0.30x`UNAVL` + 0.30x+0.8574 + 0.25x`UNAVL` + 0.15x+1.0804) x 0.80 - 0.00 = +0.3354 | +6.00% | 5.43% | 598.98 | 567.08 - 630.89 | +0.4205 | +1.0475 | +0.7892 | +5.0880 | -5.34% | SELL_SETUP_1 / SELL_SETUP_9 / SELL_SETUP_3 | 59.50 / 69.99 / 62.87 | `BELOW_SIGNAL` / `ABOVE_SIGNAL` / `BULLISH_CROSS` | none in 37d | MEDIUM |
| 6 | IQV | IQVIA Holdings Inc. Common Stock | Health Care | 271.62 | +0.3349 | 99.01 | (0.30x`UNAVL` + 0.30x+1.4310 + 0.25x`UNAVL` + 0.15x-0.0713) x 0.80 - 0.00 = +0.3349 | +6.00% | 13.80% | 287.92 | 248.93 - 326.91 | -0.3776 | +0.4121 | +0.5338 | +0.7874 | -9.92% | SELL_SETUP_2 / SELL_SETUP_9 / SELL_SETUP_4 | 75.17 / 75.13 / 63.49 | `BELOW_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | none in 37d | MEDIUM |
| 7 | RVTY | Revvity Inc. Common Stock | Industrials | 130.63 | +0.3329 | 98.82 | (0.30x`UNAVL` + 0.30x+1.3888 + 0.25x`UNAVL` + 0.15x-0.0035) x 0.80 - 0.00 = +0.3329 | +6.00% | 9.28% | 138.47 | 125.86 - 151.08 | +0.3067 | +0.6126 | +0.5309 | +1.7404 | -6.38% | SELL_SETUP_9 / SELL_SETUP_5 / SELL_SETUP_4 | 68.62 / 72.12 / 60.61 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | none in 37d | MEDIUM |
| 8 | TECH | Bio-Techne Corp Common Stock | Health Care | 72.45 | +0.3192 | 98.62 | (0.30x`UNAVL` + 0.30x+0.7951 + 0.25x`UNAVL` + 0.15x+1.0699) x 0.80 - 0.00 = +0.3192 | +6.00% | 0.99% | 76.80 | 76.05 - 77.55 | +0.6375 | +5.7278 | +0.3635 | +152.1345 | -4.02% | SELL_SETUP_1 / SELL_SETUP_9 / SELL_SETUP_4 | 66.10 / 65.94 / 55.46 | `BELOW_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | none in 37d | MEDIUM |
| 9 | PSX | Phillips 66 Common Stock | Energy | 254.66 | +0.3190 | 98.42 | (0.30x`UNAVL` + 0.30x+1.3457 + 0.25x`UNAVL` + 0.15x-0.0329) x 0.80 - 0.00 = +0.3190 | +6.00% | 8.27% | 269.94 | 248.03 - 291.85 | -0.6267 | +0.6876 | +0.8271 | +2.1924 | -8.57% | SELL_SETUP_5 / SELL_SETUP_9 / SELL_SETUP_9 | 74.81 / 78.77 / 81.33 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | none in 37d | MEDIUM |
| 10 | STT | State Street Corporation Common St | Finance | 193.94 | +0.3157 | 98.22 | (0.30x`UNAVL` + 0.30x+0.9025 + 0.25x`UNAVL` + 0.15x+0.8260) x 0.80 - 0.00 = +0.3157 | +6.00% | 7.01% | 205.58 | 191.44 - 219.71 | +0.7401 | +0.8115 | +0.7057 | +3.0534 | -5.65% | SELL_SETUP_1 / SELL_SETUP_9 / SELL_SETUP_9 | 60.03 / 82.05 / 88.94 | `BELOW_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | none in 37d | MEDIUM |
| 11 | GEN | Gen Digital Inc. Common Stock | Technology | 31.33 | +0.3148 | 98.03 | (0.30x`UNAVL` + 0.30x+1.2613 + 0.25x`UNAVL` + 0.15x+0.1009) x 0.80 - 0.00 = +0.3148 | +6.00% | 9.25% | 33.21 | 30.20 - 36.22 | +0.4304 | +0.6150 | +0.5329 | +1.7541 | -7.85% | SELL_SETUP_9 / SELL_SETUP_9 / SELL_SETUP_5 | 67.86 / 69.20 / 62.25 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | none in 37d | MEDIUM |
| 12 | ICE | Intercontinental Exchange Inc. Com | Finance | 164.59 | +0.3113 | 97.83 | (0.30x`UNAVL` + 0.30x+0.8835 + 0.25x`UNAVL` + 0.15x+0.8271) x 0.80 - 0.00 = +0.3113 | +6.00% | 6.24% | 174.47 | 163.78 - 185.15 | -0.0545 | +0.9113 | +0.7777 | +3.8510 | -13.00% | SELL_SETUP_1 / SELL_SETUP_8 / SELL_SETUP_2 | 68.48 / 61.15 / 54.65 | `BELOW_SIGNAL` / `ABOVE_SIGNAL` / `BELOW_SIGNAL` | none in 37d | MEDIUM |
| 13 | BNY | The Bank of New York Mellon Corpor | Finance | 164.33 | +0.3027 | 97.63 | (0.30x`UNAVL` + 0.30x+0.7190 + 0.25x`UNAVL` + 0.15x+1.0849) x 0.80 - 0.00 = +0.3027 | +6.00% | 5.32% | 174.19 | 165.10 - 183.28 | +0.5101 | +1.0692 | +0.7909 | +5.3014 | -5.69% | SELL_SETUP_1 / SELL_SETUP_9 / SELL_SETUP_9 | 60.86 / 77.20 / 91.64 | `BELOW_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | none in 37d | MEDIUM |
| 14 | DE | Deere & Company Common Stock | Industrials | 694.41 | +0.2997 | 97.44 | (0.30x`UNAVL` + 0.30x+1.3196 + 0.25x`UNAVL` + 0.15x-0.1415) x 0.80 - 0.00 = +0.2997 | +6.00% | 11.08% | 736.07 | 656.09 - 816.06 | +0.4694 | +0.5135 | +0.5087 | +1.2229 | -9.25% | SELL_SETUP_4 / SELL_SETUP_5 / SELL_SETUP_9 | 68.67 / 65.74 / 67.59 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | none in 37d | MEDIUM |
| 15 | JNJ | Johnson & Johnson Common Stock | Health Care | 278.43 | +0.2946 | 97.24 | (0.30x`UNAVL` + 0.30x+0.9583 + 0.25x`UNAVL` + 0.15x+0.5388) x 0.80 - 0.00 = +0.2946 | +6.00% | 6.07% | 295.14 | 277.56 - 312.71 | -0.7306 | +0.9372 | +1.1075 | +4.0734 | -7.57% | SELL_SETUP_3 / SELL_SETUP_5 / SELL_SETUP_9 | 65.95 / 69.40 / 79.82 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | none in 37d | MEDIUM |
| 16 | VRTX | Vertex Pharmaceuticals Incorporate | Health Care | 557.96 | +0.2822 | 97.04 | (0.30x`UNAVL` + 0.30x+0.9749 + 0.25x`UNAVL` + 0.15x+0.4020) x 0.80 - 0.00 = +0.2822 | +6.00% | 8.22% | 591.44 | 543.74 - 639.14 | +0.1882 | +0.6919 | +0.6570 | +2.2198 | -11.12% | SELL_SETUP_3 / SELL_SETUP_5 / SELL_SETUP_3 | 67.51 / 69.51 / 64.46 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | none in 37d | MEDIUM |
| 17 | MPC | Marathon Petroleum Corporation Com | Energy | 387.71 | +0.2800 | 96.84 | (0.30x`UNAVL` + 0.30x+1.2621 + 0.25x`UNAVL` + 0.15x-0.1906) x 0.80 - 0.00 = +0.2800 | +6.00% | 10.42% | 410.97 | 368.95 - 452.99 | -0.4642 | +0.5458 | +0.7050 | +1.3813 | -7.84% | SELL_SETUP_7 / SELL_SETUP_9 / SELL_SETUP_8 | 77.86 / 79.52 / 86.54 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | none in 37d | MEDIUM |
| 18 | WFC | Wells Fargo & Company Common Stock | Finance | 89.19 | +0.2688 | 96.65 | (0.30x`UNAVL` + 0.30x+0.7511 + 0.25x`UNAVL` + 0.15x+0.7379) x 0.80 - 0.00 = +0.2688 | +6.00% | 6.13% | 94.54 | 88.85 - 100.23 | +0.4222 | +0.9274 | +0.8075 | +3.9883 | -5.88% | SELL_SETUP_7 / SELL_SETUP_2 / SELL_SETUP_4 | 61.84 / 58.56 / 65.31 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `BELOW_SIGNAL` | none in 37d | MEDIUM |
| 19 | ELV | Elevance Health Inc. Common Stock | Health Care | 414.78 | +0.2675 | 96.45 | (0.30x`UNAVL` + 0.30x+0.6114 + 0.25x`UNAVL` + 0.15x+1.0062) x 0.80 - 0.00 = +0.2675 | +6.00% | 6.68% | 439.67 | 410.86 - 468.47 | +0.1601 | +0.8517 | +0.5512 | +3.3635 | -12.64% | SELL_SETUP_3 / SELL_SETUP_4 / SELL_SETUP_6 | 62.76 / 61.87 / 55.81 | `ABOVE_SIGNAL` / `BELOW_SIGNAL` / `ABOVE_SIGNAL` | none in 37d | MEDIUM |
| 20 | RJF | Raymond James Financial Inc. Commo | Finance | 181.10 | +0.2628 | 96.25 | (0.30x`UNAVL` + 0.30x+0.7020 + 0.25x`UNAVL` + 0.15x+0.7863) x 0.80 - 0.00 = +0.2628 | +6.00% | 6.56% | 191.97 | 179.61 - 204.32 | +0.4144 | +0.8671 | +0.7735 | +3.4868 | -6.10% | SELL_SETUP_1 / SELL_SETUP_9 / SELL_SETUP_3 | 59.09 / 66.38 / 63.10 | `BELOW_SIGNAL` / `ABOVE_SIGNAL` / `BULLISH_CROSS` | none in 37d | MEDIUM |
| 21 | DELL | Dell Technologies Inc. Class C Com | Technology | 516.39 | +0.2605 | 96.06 | (0.30x`UNAVL` + 0.30x+1.4805 + 0.25x`UNAVL` + 0.15x-0.7900) x 0.80 - 0.00 = +0.2605 | +6.00% | 24.80% | 547.37 | 414.21 - 680.53 | +2.7270 | +0.2294 | +0.0271 | +0.2440 | -19.09% | SELL_SETUP_2 / SELL_SETUP_7 / SELL_SETUP_7 | 62.55 / 71.51 / 85.88 | `BULLISH_CROSS` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | none in 37d | MEDIUM |
| 22 | BIIB | Biogen Inc. Common Stock | Health Care | 224.51 | +0.2558 | 95.86 | (0.30x`UNAVL` + 0.30x+0.7022 + 0.25x`UNAVL` + 0.15x+0.7276) x 0.80 - 0.00 = +0.2558 | +6.00% | 7.62% | 237.98 | 220.18 - 255.78 | +0.0234 | +0.7462 | +0.5327 | +2.5817 | -11.39% | SELL_SETUP_2 / SELL_SETUP_5 / SELL_SETUP_9 | 63.50 / 68.75 / 61.91 | `ABOVE_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | none in 37d | MEDIUM |
| 23 | PRU | Prudential Financial Inc. Common S | Finance | 123.20 | +0.2552 | 95.66 | (0.30x`UNAVL` + 0.30x+0.7051 + 0.25x`UNAVL` + 0.15x+0.7169) x 0.80 - 0.00 = +0.2552 | +6.00% | 5.73% | 130.59 | 123.26 - 137.93 | +0.3048 | +0.9932 | +0.9266 | +4.5747 | -5.30% | SELL_SETUP_1 / SELL_SETUP_1 / SELL_SETUP_4 | 60.95 / 68.44 / 64.68 | `BELOW_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | none in 37d | MEDIUM |
| 24 | SCHW | Charles Schwab Corporation (The) C | Finance | 110.38 | +0.2540 | 95.46 | (0.30x`UNAVL` + 0.30x+0.6887 + 0.25x`UNAVL` + 0.15x+0.7391) x 0.80 - 0.00 = +0.2540 | +6.00% | 5.57% | 117.00 | 110.61 - 123.39 | -0.0491 | +1.0216 | +0.9099 | +4.8394 | -5.36% | SELL_SETUP_2 / SELL_SETUP_9 / SELL_SETUP_3 | 57.13 / 68.58 / 67.90 | `BELOW_SIGNAL` / `ABOVE_SIGNAL` / `ABOVE_SIGNAL` | none in 37d | MEDIUM |

## Near-miss rejection log (ranks 25-34)

Names immediately below the published cut. They are ranked but not published; their percentiles
still sit in the investable band, so the cut is a publication-width convention, not a quality
threshold.

| Rank | Ticker | Sector | Adj Score | Pctl | Tech_Z | Macro_Z | Why not published |
|---|---|---|---|---|---|---|---|
| 25 | MDT | Health Care | +0.2532 | 95.27 | +0.6199 | +0.8701 | below the 24-name publication cut |
| 26 | DGX | Health Care | +0.2519 | 95.07 | +0.6534 | +0.7925 | below the 24-name publication cut |
| 27 | BMY | Health Care | +0.2513 | 94.87 | +0.6345 | +0.8252 | below the 24-name publication cut |
| 28 | C | Finance | +0.2513 | 94.67 | +0.6966 | +0.7011 | below the 24-name publication cut |
| 29 | PFE | Health Care | +0.2484 | 94.48 | +0.7585 | +0.5529 | below the 24-name publication cut |
| 30 | T | Telecommunications | +0.2484 | 94.28 | +0.8277 | +0.4144 | below the 24-name publication cut |
| 31 | NOW | Technology | +0.2478 | 94.08 | +1.0119 | +0.0411 | below the 24-name publication cut |
| 32 | JPM | Finance | +0.2477 | 93.89 | +0.6007 | +0.8628 | below the 24-name publication cut |
| 33 | CEG | Utilities | +0.2410 | 93.69 | +0.9165 | +0.1754 | below the 24-name publication cut |
| 34 | MET | Finance | +0.2385 | 93.49 | +0.7064 | +0.5751 | below the 24-name publication cut |

## Sector distribution of the published sleeve

| Sector | Names | Share of sleeve |
|---|---|---|
| Finance | 10 | 41.67% |
| Health Care | 7 | 29.17% |
| Energy | 3 | 12.50% |
| Industrials | 2 | 8.33% |
| Technology | 2 | 8.33% |
