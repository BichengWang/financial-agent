# 07 Portfolio Proposal — 2026-07-30

## Decision

**NO PORTFOLIO / NO_TRADE.** Constraint feasibility ends before sizing: zero names pass the factor-family evidence threshold. The equal-weight sleeve below is a monitoring diagnostic, not a proposed allocation.

| Diagnostic | Value | Limit | Pass |
| --- | ---: | ---: | --- |
| Beta to SPY | -0.3886 | 0.90-1.10 | False |
| Average pairwise correlation | 0.3049 | <0.45 | True |
| 95th-pctl drawdown | 8.87% | <=8% | False |
| Largest sector | 25.00% | <=30% | True |
| Event names | 0 | <=2 | True |
| Factor-family gate | 0 investable | >=5 | False |

Expected monitoring diagnostics: Sharpe 1.057, Sortino 2.048, IR 1.203, tracking error 5.15%, VaR95 -2.87%, CVaR95 -5.07%. [L019]

## Per-position Recommendation Metrics Table

All values below are inherited from factor scoring; no portfolio-stage recomputation is introduced.

| Ticker | Entry Price | Price Date | Price Tag | Target Price | Target Date | mu | sigma | Sigma Source | Sharpe | Sortino | IR | Kelly 0.25 | VaR95 | CVaR95 | Max DD60 | TD9 D/W/M | RSI14 D/W/M | MACD D/W/M | 70% CI Lo | 70% CI Hi | Score Trace | Ledger Rows |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PAYX | 116.33 | 2026-07-30 | DELAYED | 123.31 | 2026-08-27 | 6.00% | 10.66% | REALIZED_VOL_30D | 0.533 | 0.925 | 0.690 | 5.00% | -11.59% | -15.96% | -6.35% | SELL_SETUP_4/SELL_SETUP_9/SELL_SETUP_2 | 62.36/67.85/52.47 | ABOVE_SIGNAL/ABOVE_SIGNAL/BELOW_SIGNAL | 110.41 | 136.21 | (0.30×0.000 Fund[UNAVAILABLE] + 0.30×+1.203 + 0.25×0.000 Sent[UNAVAILABLE] + 0.15×+0.705)×0.80−0.00=+0.373 | L046,L002,L009-L019,L023,L024 |
| TRV | 375.99 | 2026-07-30 | DELAYED | 398.55 | 2026-08-27 | 6.00% | 10.08% | REALIZED_VOL_30D | 0.564 | 1.300 | 0.830 | 5.00% | -10.63% | -14.77% | -5.96% | BUY_SETUP_1/SELL_SETUP_9/SELL_SETUP_9 | 63.4/73.11/75.96 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | 359.13 | 437.97 | (0.30×0.000 Fund[UNAVAILABLE] + 0.30×+1.141 + 0.25×0.000 Sent[UNAVAILABLE] + 0.15×+0.748)×0.80−0.00=+0.364 | L047,L002,L009-L019,L023,L024 |
| CTAS | 206.79 | 2026-07-30 | DELAYED | 219.20 | 2026-08-27 | 6.00% | 10.68% | REALIZED_VOL_30D | 0.532 | 0.965 | 0.683 | 5.00% | -11.62% | -16.00% | -7.19% | SELL_SETUP_5/SELL_SETUP_6/SELL_SETUP_1 | 63.25/65.43/58.58 | ABOVE_SIGNAL/ABOVE_SIGNAL/BELOW_SIGNAL | 196.23 | 242.16 | (0.30×0.000 Fund[UNAVAILABLE] + 0.30×+1.208 + 0.25×0.000 Sent[UNAVAILABLE] + 0.15×+0.555)×0.80−0.00=+0.357 | L048,L002,L009-L019,L023,L024 |
| WTW | 336.05 | 2026-07-30 | DELAYED | 356.21 | 2026-08-27 | 6.00% | 10.09% | REALIZED_VOL_30D | 0.563 | 1.567 | 0.680 | 5.00% | -10.65% | -14.79% | -6.88% | SELL_SETUP_5/SELL_SETUP_6/SELL_SETUP_1 | 80.24/67.19/59.88 | ABOVE_SIGNAL/ABOVE_SIGNAL/BELOW_SIGNAL | 320.94 | 391.49 | (0.30×0.000 Fund[UNAVAILABLE] + 0.30×+1.152 + 0.25×0.000 Sent[UNAVAILABLE] + 0.15×+0.637)×0.80−0.00=+0.353 | L049,L002,L009-L019,L023,L024 |
| ADP | 263.87 | 2026-07-30 | DELAYED | 279.70 | 2026-08-27 | 6.00% | 10.52% | REALIZED_VOL_30D | 0.540 | 1.046 | 0.707 | 5.00% | -11.35% | -15.66% | -7.49% | SELL_SETUP_4/SELL_SETUP_6/SELL_SETUP_2 | 63.66/64.75/54.52 | ABOVE_SIGNAL/ABOVE_SIGNAL/BELOW_SIGNAL | 250.84 | 308.56 | (0.30×0.000 Fund[UNAVAILABLE] + 0.30×+1.083 + 0.25×0.000 Sent[UNAVAILABLE] + 0.15×+0.697)×0.80−0.00=+0.344 | L050,L002,L009-L019,L023,L024 |
| AON | 366.57 | 2026-07-30 | DELAYED | 388.56 | 2026-08-27 | 6.00% | 9.81% | REALIZED_VOL_30D | 0.579 | 1.042 | 0.853 | 5.00% | -10.18% | -14.20% | -6.75% | SELL_SETUP_4/SELL_SETUP_6/SELL_SETUP_1 | 56.99/61.08/56.62 | ABOVE_SIGNAL/ABOVE_SIGNAL/BELOW_SIGNAL | 351.18 | 425.95 | (0.30×0.000 Fund[UNAVAILABLE] + 0.30×+1.016 + 0.25×0.000 Sent[UNAVAILABLE] + 0.15×+0.761)×0.80−0.00=+0.335 | L051,L002,L009-L019,L023,L024 |
| PCG | 17.78 | 2026-07-30 | DELAYED | 18.85 | 2026-08-27 | 6.00% | 6.84% | REALIZED_VOL_30D | 0.831 | 1.316 | 0.832 | 5.00% | -5.29% | -8.09% | -5.71% | BUY_SETUP_1/SELL_SETUP_4/SELL_SETUP_1 | 57.7/57.83/55.37 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | 17.58 | 20.11 | (0.30×0.000 Fund[UNAVAILABLE] + 0.30×+0.914 + 0.25×0.000 Sent[UNAVAILABLE] + 0.15×+0.884)×0.80−0.00=+0.325 | L052,L002,L009-L019,L023,L024 |
| LH | 315.53 | 2026-07-30 | DELAYED | 334.46 | 2026-08-27 | 6.00% | 8.03% | REALIZED_VOL_30D | 0.707 | 1.526 | 0.862 | 5.00% | -7.25% | -10.54% | -6.20% | SELL_SETUP_6/SELL_SETUP_6/SELL_SETUP_1 | 74.23/69.03/65.18 | ABOVE_SIGNAL/ABOVE_SIGNAL/BULLISH_CROSS | 308.11 | 360.82 | (0.30×0.000 Fund[UNAVAILABLE] + 0.30×+0.934 + 0.25×0.000 Sent[UNAVAILABLE] + 0.15×+0.685)×0.80−0.00=+0.306 | L053,L002,L009-L019,L023,L024 |
| BBY | 87.82 | 2026-07-30 | DELAYED | 93.09 | 2026-08-27 | 6.00% | 8.79% | REALIZED_VOL_30D | 0.646 | 1.115 | 0.450 | 5.00% | -8.51% | -12.11% | -8.93% | SELL_SETUP_5/SELL_SETUP_9/SELL_SETUP_3 | 64.65/67.87/60.52 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | 85.06 | 101.12 | (0.30×0.000 Fund[UNAVAILABLE] + 0.30×+1.116 + 0.25×0.000 Sent[UNAVAILABLE] + 0.15×+0.302)×0.80−0.00=+0.304 | L054,L002,L009-L019,L023,L024 |
| INCY | 122.99 | 2026-07-30 | DELAYED | 130.37 | 2026-08-27 | 6.00% | 11.87% | REALIZED_VOL_30D | 0.478 | 1.228 | 0.556 | 5.00% | -13.59% | -18.46% | -9.50% | SELL_SETUP_5/SELL_SETUP_9/SELL_SETUP_2 | 61.32/69.03/75.22 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | 115.18 | 145.56 | (0.30×0.000 Fund[UNAVAILABLE] + 0.30×+1.083 + 0.25×0.000 Sent[UNAVAILABLE] + 0.15×+0.324)×0.80−0.00=+0.299 | L055,L002,L009-L019,L023,L024 |
| MRSH | 191.51 | 2026-07-30 | DELAYED | 203.00 | 2026-08-27 | 6.00% | 9.94% | REALIZED_VOL_30D | 0.572 | 1.061 | 0.841 | 5.00% | -10.40% | -14.47% | -6.28% | SELL_SETUP_4/SELL_SETUP_6/SELL_SETUP_1 | 64.6/62.79/51.43 | ABOVE_SIGNAL/ABOVE_SIGNAL/BELOW_SIGNAL | 183.21 | 222.80 | (0.30×0.000 Fund[UNAVAILABLE] + 0.30×+0.815 + 0.25×0.000 Sent[UNAVAILABLE] + 0.15×+0.842)×0.80−0.00=+0.297 | L056,L002,L009-L019,L023,L024 |
| AWK | 136.81 | 2026-07-30 | DELAYED | 145.02 | 2026-08-27 | 6.00% | 7.52% | REALIZED_VOL_30D | 0.756 | 1.297 | 1.000 | 5.00% | -6.40% | -9.49% | -5.59% | SELL_SETUP_5/BUY_SETUP_1/SELL_SETUP_1 | 60.12/57.43/53.38 | ABOVE_SIGNAL/ABOVE_SIGNAL/BULLISH_CROSS | 134.32 | 155.72 | (0.30×0.000 Fund[UNAVAILABLE] + 0.30×+0.735 + 0.25×0.000 Sent[UNAVAILABLE] + 0.15×+0.940)×0.80−0.00=+0.289 | L057,L002,L009-L019,L023,L024 |
| BXP | 71.67 | 2026-07-30 | DELAYED | 75.97 | 2026-08-27 | 6.00% | 8.53% | REALIZED_VOL_30D | 0.666 | 1.042 | 0.768 | 5.00% | -8.08% | -11.58% | -5.33% | SELL_SETUP_5/SELL_SETUP_9/SELL_SETUP_2 | 63.93/66.33/57.24 | ABOVE_SIGNAL/ABOVE_SIGNAL/BULLISH_CROSS | 69.61 | 82.33 | (0.30×0.000 Fund[UNAVAILABLE] + 0.30×+0.895 + 0.25×0.000 Sent[UNAVAILABLE] + 0.15×+0.574)×0.80−0.00=+0.284 | L058,L002,L009-L019,L023,L024 |
| BRO | 70.87 | 2026-07-30 | DELAYED | 75.12 | 2026-08-27 | 6.00% | 12.34% | REALIZED_VOL_30D | 0.460 | 0.851 | 0.674 | 5.00% | -14.36% | -19.42% | -6.59% | SELL_SETUP_4/SELL_SETUP_9/SELL_SETUP_1 | 58.37/54.68/43.68 | ABOVE_SIGNAL/ABOVE_SIGNAL/BELOW_SIGNAL | 66.03 | 84.22 | (0.30×0.000 Fund[UNAVAILABLE] + 0.30×+0.858 + 0.25×0.000 Sent[UNAVAILABLE] + 0.15×+0.613)×0.80−0.00=+0.280 | L059,L002,L009-L019,L023,L024 |
| SJM | 122.21 | 2026-07-30 | DELAYED | 129.54 | 2026-08-27 | 6.00% | 10.19% | REALIZED_VOL_30D | 0.557 | 0.818 | 0.654 | 5.00% | -10.82% | -15.00% | -8.42% | SELL_SETUP_9/SELL_SETUP_3/SELL_SETUP_1 | 61.72/66.62/58.44 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | 116.59 | 142.50 | (0.30×0.000 Fund[UNAVAILABLE] + 0.30×+0.806 + 0.25×0.000 Sent[UNAVAILABLE] + 0.15×+0.714)×0.80−0.00=+0.279 | L060,L002,L009-L019,L023,L024 |
| BAX | 26.75 | 2026-07-30 | DELAYED | 28.36 | 2026-08-27 | 6.00% | 14.01% | REALIZED_VOL_30D | 0.406 | 0.733 | 0.489 | 5.00% | -17.11% | -22.86% | -7.19% | SELL_SETUP_5/SELL_SETUP_9/SELL_SETUP_2 | 75.93/71.02/49.58 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | 24.46 | 32.25 | (0.30×0.000 Fund[UNAVAILABLE] + 0.30×+1.205 + 0.25×0.000 Sent[UNAVAILABLE] + 0.15×-0.087)×0.80−0.00=+0.279 | L061,L002,L009-L019,L023,L024 |
| AAPL | 333.43 | 2026-07-30 | DELAYED | 353.44 | 2026-08-27 | 6.00% | 9.45% | REALIZED_VOL_30D | 0.601 | 0.958 | 0.729 | 5.00% | -9.60% | -13.48% | -12.71% | SELL_SETUP_5/SELL_SETUP_5/SELL_SETUP_3 | 61.66/69.18/70.3 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | 320.65 | 386.22 | (0.30×0.000 Fund[UNAVAILABLE] + 0.30×+1.072 + 0.25×0.000 Sent[UNAVAILABLE] + 0.15×+0.148)×0.80−0.00=+0.275 | L062,L002,L009-L019,L023,L024 |
| SYK | 348.04 | 2026-07-30 | DELAYED | 368.92 | 2026-08-27 | 6.00% | 11.93% | REALIZED_VOL_30D | 0.476 | 0.724 | 0.618 | 5.00% | -13.69% | -18.58% | -8.77% | SELL_SETUP_5/SELL_SETUP_1/SELL_SETUP_1 | 62.65/56.03/51.09 | ABOVE_SIGNAL/ABOVE_SIGNAL/BELOW_SIGNAL | 325.74 | 412.11 | (0.30×0.000 Fund[UNAVAILABLE] + 0.30×+0.919 + 0.25×0.000 Sent[UNAVAILABLE] + 0.15×+0.416)×0.80−0.00=+0.270 | L063,L002,L009-L019,L023,L024 |
| PM | 192.00 | 2026-07-30 | DELAYED | 203.52 | 2026-08-27 | 6.00% | 9.67% | REALIZED_VOL_30D | 0.587 | 0.910 | 0.708 | 5.00% | -9.96% | -13.92% | -10.01% | BUY_SETUP_1/SELL_SETUP_3/SELL_SETUP_1 | 54.74/63.14/68.57 | ABOVE_SIGNAL/ABOVE_SIGNAL/BULLISH_CROSS | 184.21 | 222.83 | (0.30×0.000 Fund[UNAVAILABLE] + 0.30×+0.823 + 0.25×0.000 Sent[UNAVAILABLE] + 0.15×+0.582)×0.80−0.00=+0.267 | L064,L002,L009-L019,L023,L024 |
| RTX | 214.38 | 2026-07-30 | DELAYED | 227.24 | 2026-08-27 | 6.00% | 9.47% | REALIZED_VOL_30D | 0.600 | 1.191 | 0.703 | 5.00% | -9.62% | -13.50% | -5.58% | SELL_SETUP_7/SELL_SETUP_9/SELL_SETUP_1 | 69.69/67.52/75.2 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | 206.13 | 248.35 | (0.30×0.000 Fund[UNAVAILABLE] + 0.30×+0.813 + 0.25×0.000 Sent[UNAVAILABLE] + 0.15×+0.587)×0.80−0.00=+0.266 | L065,L002,L009-L019,L023,L024 |

## Kelly and per-name exclusion audit

The 5% single-name cap binds for 20/20 monitoring names, but cap-binding does not create an allocation: the factor-family gate fails first, so every proposed weight remains zero.

| Ticker | Uncapped 0.25 Kelly | 5% Capped Kelly | Cap Binds | Proposed Weight | Exclusion Rationale | Rows |
| --- | --- | --- | --- | --- | --- | --- |
| PAYX | 186.15% | 5.00% | YES | 0.00% | only 2/4 factor families available; threshold #2; one family >50% of available conviction; threshold #3 | L046,L017-L019,L023,L024 |
| TRV | 271.16% | 5.00% | YES | 0.00% | only 2/4 factor families available; threshold #2; one family >50% of available conviction; threshold #3 | L047,L017-L019,L023,L024 |
| CTAS | 187.09% | 5.00% | YES | 0.00% | only 2/4 factor families available; threshold #2; one family >50% of available conviction; threshold #3 | L048,L017-L019,L023,L024 |
| WTW | 184.75% | 5.00% | YES | 0.00% | only 2/4 factor families available; threshold #2; one family >50% of available conviction; threshold #3 | L049,L017-L019,L023,L024 |
| ADP | 194.30% | 5.00% | YES | 0.00% | only 2/4 factor families available; threshold #2; one family >50% of available conviction; threshold #3 | L050,L017-L019,L023,L024 |
| AON | 285.00% | 5.00% | YES | 0.00% | only 2/4 factor families available; threshold #2; one family >50% of available conviction; threshold #3 | L051,L017-L019,L023,L024 |
| PCG | 283.00% | 5.00% | YES | 0.00% | only 2/4 factor families available; threshold #2; one family >50% of available conviction; threshold #3 | L052,L017-L019,L023,L024 |
| LH | 308.92% | 5.00% | YES | 0.00% | only 2/4 factor families available; threshold #2; one family >50% of available conviction; threshold #3 | L053,L017-L019,L023,L024 |
| BBY | 88.42% | 5.00% | YES | 0.00% | only 2/4 factor families available; threshold #2; one family >50% of available conviction; threshold #3 | L054,L017-L019,L023,L024 |
| INCY | 125.18% | 5.00% | YES | 0.00% | only 2/4 factor families available; threshold #2; one family >50% of available conviction; threshold #3 | L055,L017-L019,L023,L024 |
| MRSH | 272.71% | 5.00% | YES | 0.00% | only 2/4 factor families available; threshold #2; one family >50% of available conviction; threshold #3 | L056,L017-L019,L023,L024 |
| AWK | 397.97% | 5.00% | YES | 0.00% | only 2/4 factor families available; threshold #2; one family >50% of available conviction; threshold #3 | L057,L017-L019,L023,L024 |
| BXP | 250.45% | 5.00% | YES | 0.00% | only 2/4 factor families available; threshold #2; one family >50% of available conviction; threshold #3 | L058,L017-L019,L023,L024 |
| BRO | 173.13% | 5.00% | YES | 0.00% | only 2/4 factor families available; threshold #2; one family >50% of available conviction; threshold #3 | L059,L017-L019,L023,L024 |
| SJM | 165.73% | 5.00% | YES | 0.00% | only 2/4 factor families available; threshold #2; one family >50% of available conviction; threshold #3 | L060,L017-L019,L023,L024 |
| BAX | 104.01% | 5.00% | YES | 0.00% | only 2/4 factor families available; threshold #2; one family >50% of available conviction; threshold #3 | L061,L017-L019,L023,L024 |
| AAPL | 229.00% | 5.00% | YES | 0.00% | only 2/4 factor families available; threshold #2; one family >50% of available conviction; threshold #3 | L062,L017-L019,L023,L024 |
| SYK | 152.29% | 5.00% | YES | 0.00% | only 2/4 factor families available; threshold #2; one family >50% of available conviction; threshold #3 | L063,L017-L019,L023,L024 |
| PM | 198.94% | 5.00% | YES | 0.00% | only 2/4 factor families available; threshold #2; one family >50% of available conviction; threshold #3 | L064,L017-L019,L023,L024 |
| RTX | 204.91% | 5.00% | YES | 0.00% | only 2/4 factor families available; threshold #2; one family >50% of available conviction; threshold #3 | L065,L017-L019,L023,L024 |

## Sector table

| Sector | Equal-weight diagnostic share | 30% cap | Ledger |
| --- | --- | --- | --- |
| Consumer Discretionary | 5.00% | PASS | L019 |
| Consumer Staples | 10.00% | PASS | L019 |
| Financials | 25.00% | PASS | L019 |
| Health Care | 20.00% | PASS | L019 |
| Industrials | 20.00% | PASS | L019 |
| Information Technology | 5.00% | PASS | L019 |
| Real Estate | 5.00% | PASS | L019 |
| Utilities | 10.00% | PASS | L019 |

## Factor exposure summary

Because every proposed position weight is 0.00%, proposed portfolio exposure is zero for every family. The sourceable Technical and Macro families remain monitoring diagnostics only.

| Factor | Availability in 20-name monitor | Proposed-weight exposure | Monitoring role | Ledger |
| --- | --- | --- | --- | --- |
| Fundamental | 0/20 — UNAVAILABLE | UNAVAILABLE — no production family or portfolio | Structural DQ/confidence gap | L019,L023,L046-L065 |
| Technical | 20/20 sourceable | 0.000 — sum(0 weights × z) | Scored monitoring diagnostic | L014,L019,L046-L065 |
| Sentiment | 0/20 — UNAVAILABLE | UNAVAILABLE — no production family or portfolio | Structural DQ/confidence gap | L019,L024,L046-L065 |
| Macro | 20/20 sourceable | 0.000 — sum(0 weights × z) | Scored monitoring diagnostic | L014,L019,L046-L065 |

## Correlation matrix

| Ticker | PAYX | TRV | CTAS | WTW | ADP | AON | PCG | LH | BBY | INCY | MRSH | AWK | BXP | BRO | SJM | BAX | AAPL | SYK | PM | RTX | Ledger |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PAYX | 1.00 | 0.30 | 0.59 | 0.50 | 0.94 | 0.68 | -0.01 | 0.28 | 0.09 | 0.10 | 0.74 | 0.38 | 0.23 | 0.73 | 0.43 | 0.23 | 0.12 | 0.47 | 0.27 | 0.03 | L019 |
| TRV | 0.30 | 1.00 | 0.31 | 0.29 | 0.29 | 0.47 | 0.15 | 0.38 | -0.07 | 0.30 | 0.46 | 0.47 | 0.08 | 0.51 | 0.25 | 0.10 | 0.13 | 0.22 | 0.36 | 0.17 | L019 |
| CTAS | 0.59 | 0.31 | 1.00 | 0.37 | 0.59 | 0.64 | 0.14 | 0.36 | 0.15 | 0.26 | 0.61 | 0.44 | 0.43 | 0.64 | 0.53 | 0.34 | 0.34 | 0.51 | 0.35 | 0.20 | L019 |
| WTW | 0.50 | 0.29 | 0.37 | 1.00 | 0.61 | 0.71 | 0.14 | 0.52 | -0.10 | 0.14 | 0.68 | 0.34 | 0.08 | 0.66 | 0.25 | 0.58 | 0.08 | 0.38 | 0.09 | 0.18 | L019 |
| ADP | 0.94 | 0.29 | 0.59 | 0.61 | 1.00 | 0.76 | -0.01 | 0.32 | 0.05 | 0.11 | 0.77 | 0.36 | 0.23 | 0.79 | 0.39 | 0.26 | 0.16 | 0.47 | 0.24 | 0.06 | L019 |
| AON | 0.68 | 0.47 | 0.64 | 0.71 | 0.76 | 1.00 | 0.13 | 0.50 | -0.03 | 0.36 | 0.88 | 0.51 | 0.21 | 0.88 | 0.46 | 0.35 | 0.29 | 0.50 | 0.36 | 0.27 | L019 |
| PCG | -0.01 | 0.15 | 0.14 | 0.14 | -0.01 | 0.13 | 1.00 | 0.16 | 0.00 | 0.28 | 0.17 | 0.52 | -0.03 | 0.11 | 0.23 | 0.32 | 0.12 | 0.27 | 0.40 | -0.08 | L019 |
| LH | 0.28 | 0.38 | 0.36 | 0.52 | 0.32 | 0.50 | 0.16 | 1.00 | 0.07 | 0.39 | 0.37 | 0.57 | 0.23 | 0.44 | 0.38 | 0.52 | -0.04 | 0.48 | 0.29 | 0.37 | L019 |
| BBY | 0.09 | -0.07 | 0.15 | -0.10 | 0.05 | -0.03 | 0.00 | 0.07 | 1.00 | 0.16 | 0.00 | -0.05 | 0.20 | 0.07 | 0.14 | 0.16 | 0.05 | 0.07 | -0.12 | -0.05 | L019 |
| INCY | 0.10 | 0.30 | 0.26 | 0.14 | 0.11 | 0.36 | 0.28 | 0.39 | 0.16 | 1.00 | 0.34 | 0.27 | 0.14 | 0.33 | 0.23 | 0.24 | 0.05 | 0.30 | 0.21 | 0.12 | L019 |
| MRSH | 0.74 | 0.46 | 0.61 | 0.68 | 0.77 | 0.88 | 0.17 | 0.37 | 0.00 | 0.34 | 1.00 | 0.49 | 0.26 | 0.91 | 0.51 | 0.38 | 0.21 | 0.55 | 0.25 | 0.20 | L019 |
| AWK | 0.38 | 0.47 | 0.44 | 0.34 | 0.36 | 0.51 | 0.52 | 0.57 | -0.05 | 0.27 | 0.49 | 1.00 | 0.24 | 0.51 | 0.55 | 0.36 | 0.07 | 0.45 | 0.56 | 0.12 | L019 |
| BXP | 0.23 | 0.08 | 0.43 | 0.08 | 0.23 | 0.21 | -0.03 | 0.23 | 0.20 | 0.14 | 0.26 | 0.24 | 1.00 | 0.31 | 0.27 | 0.45 | 0.17 | 0.34 | 0.07 | 0.14 | L019 |
| BRO | 0.73 | 0.51 | 0.64 | 0.66 | 0.79 | 0.88 | 0.11 | 0.44 | 0.07 | 0.33 | 0.91 | 0.51 | 0.31 | 1.00 | 0.49 | 0.36 | 0.17 | 0.51 | 0.30 | 0.21 | L019 |
| SJM | 0.43 | 0.25 | 0.53 | 0.25 | 0.39 | 0.46 | 0.23 | 0.38 | 0.14 | 0.23 | 0.51 | 0.55 | 0.27 | 0.49 | 1.00 | 0.36 | -0.08 | 0.48 | 0.45 | 0.09 | L019 |
| BAX | 0.23 | 0.10 | 0.34 | 0.58 | 0.26 | 0.35 | 0.32 | 0.52 | 0.16 | 0.24 | 0.38 | 0.36 | 0.45 | 0.36 | 0.36 | 1.00 | 0.10 | 0.55 | 0.16 | 0.14 | L019 |
| AAPL | 0.12 | 0.13 | 0.34 | 0.08 | 0.16 | 0.29 | 0.12 | -0.04 | 0.05 | 0.05 | 0.21 | 0.07 | 0.17 | 0.17 | -0.08 | 0.10 | 1.00 | 0.11 | 0.11 | 0.10 | L019 |
| SYK | 0.47 | 0.22 | 0.51 | 0.38 | 0.47 | 0.50 | 0.27 | 0.48 | 0.07 | 0.30 | 0.55 | 0.45 | 0.34 | 0.51 | 0.48 | 0.55 | 0.11 | 1.00 | 0.40 | 0.25 | L019 |
| PM | 0.27 | 0.36 | 0.35 | 0.09 | 0.24 | 0.36 | 0.40 | 0.29 | -0.12 | 0.21 | 0.25 | 0.56 | 0.07 | 0.30 | 0.45 | 0.16 | 0.11 | 0.40 | 1.00 | 0.09 | L019 |
| RTX | 0.03 | 0.17 | 0.20 | 0.18 | 0.06 | 0.27 | -0.08 | 0.37 | -0.05 | 0.12 | 0.20 | 0.12 | 0.14 | 0.21 | 0.09 | 0.14 | 0.10 | 0.25 | 0.09 | 1.00 | L019 |

## Recommendation metrics

The table above is the mandatory inherited recommendation pack. Universe-level exclusions remain in `04_universe_summary.md`; the Kelly table records the position-level rationale for every published monitor.
