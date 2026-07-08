# 07 Portfolio Proposal

No live portfolio is proposed. The scoreable list is a monitoring sleeve only because the GO gate fails on earnings-date and non-price factor evidence.

## Constraint Feasibility Pre-Check

| Check | Result | Evidence |
| --- | --- | --- |
| Minimum investable names | FAIL | 0 names pass full investability; top technical names lack earnings/fundamental/sentiment evidence. |
| Average pairwise correlation, paper top 10 | 0.25 | Computed from 60d fetched returns, but not used for live sizing. |
| Average beta, paper top 10 | 1.83 | High beta concentration would require revision even if GO data were present. |
| Drawdown proxy, paper top 10 | 35.39% | Mean one-name sigma proxy × 1.65; exceeds the 8% portfolio drawdown target before diversification. |

## Per-Position Recommendation Metrics Table

| Ticker | Entry Price | Price Date | Price Tag | Target Price | Target Date | mu | sigma | Sigma Source | Sharpe | Sortino | IR | Kelly 0.25 | VaR95 | CVaR95 | Max DD60 | TD9 D/W/M | RSI14 D/W/M | MACD D/W/M | 70% CI Lo | 70% CI Hi | Score Trace | Ledger Rows |
| --- | ---: | --- | --- | ---: | --- | ---: | ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- | --- | ---: | ---: | --- | --- |
| DDOG | 256.84 | 2026-07-08 | DELAYED | 272.25 | 2026-08-05 | 6.00% | 18.34% | REALIZED_VOL_30D | 0.33 | 0.93 | 0.24 | 5.00% | -24.26% | -31.77% | -20.51% | BUY_SETUP_2/SELL_SETUP_2/SELL_SETUP_3 | 65.05/72.46/73.13 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | 223.27 | 321.23 | (0.30*0.00 + 0.30*5.33 + 0.25*0.00 + 0.15*0.00)*0.78 - 0.06 | L026,L027 |
| DELL | 431.44 | 2026-07-08 | DELAYED | 457.32 | 2026-08-05 | 6.00% | 33.12% | REALIZED_VOL_30D | 0.18 | 0.64 | 0.18 | 5.00% | -48.65% | -62.23% | -20.63% | SELL_SETUP_1/SELL_SETUP_1/SELL_SETUP_5 | 60.67/80.8/86.77 | BELOW_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | 308.70 | 605.95 | (0.30*0.00 + 0.30*4.96 + 0.25*0.00 + 0.15*0.00)*0.78 - 0.07 | L028,L029 |
| PANW | 321.02 | 2026-07-08 | DELAYED | 340.28 | 2026-08-05 | 6.00% | 17.69% | REALIZED_VOL_30D | 0.34 | 0.76 | 0.38 | 5.00% | -23.19% | -30.44% | -13.30% | BUY_SETUP_2/SELL_SETUP_9/SELL_SETUP_3 | 59.09/71.83/70.37 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | 281.22 | 399.34 | (0.30*0.00 + 0.30*4.32 + 0.25*0.00 + 0.15*0.00)*0.78 - 0.06 | L030,L031 |
| CRWD | 189.52 | 2026-07-08 | DELAYED | 200.89 | 2026-08-05 | 6.00% | 16.27% | REALIZED_VOL_30D | 0.37 | 0.83 | 0.40 | 5.00% | -20.85% | -27.52% | -17.55% | BUY_SETUP_1/SELL_SETUP_2/SELL_SETUP_3 | 62.43/71.48/71.9 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | 168.82 | 232.97 | (0.30*0.00 + 0.30*3.92 + 0.25*0.00 + 0.15*0.00)*0.78 - 0.06 | L032,L033 |
| MU | 937.60 | 2026-07-08 | DELAYED | 993.86 | 2026-08-05 | 6.00% | 36.54% | REALIZED_VOL_30D | 0.16 | 0.35 | 0.15 | 5.00% | -54.30% | -69.28% | -22.74% | BUY_SETUP_5/BUY_SETUP_1/SELL_SETUP_9 | 46.21/65.77/75.29 | BELOW_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | 637.52 | 1350.21 | (0.30*0.00 + 0.30*3.78 + 0.25*0.00 + 0.15*0.00)*0.78 - 0.07 | L034,L035 |
| HUM | 402.05 | 2026-07-08 | DELAYED | 426.17 | 2026-08-05 | 6.00% | 11.23% | REALIZED_VOL_30D | 0.53 | 1.39 | 0.48 | 5.00% | -12.54% | -17.14% | -5.56% | BUY_SETUP_2/SELL_SETUP_9/SELL_SETUP_3 | 72.13/77.0/61.4 | BELOW_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | 379.20 | 473.14 | (0.30*0.00 + 0.30*3.81 + 0.25*0.00 + 0.15*0.00)*0.78 - 0.08 | L036,L037 |
| FTNT | 155.92 | 2026-07-08 | DELAYED | 165.28 | 2026-08-05 | 6.00% | 12.82% | REALIZED_VOL_30D | 0.47 | 1.00 | 0.36 | 5.00% | -15.15% | -20.41% | -7.54% | BUY_SETUP_1/SELL_SETUP_9/SELL_SETUP_5 | 61.71/83.23/77.21 | BELOW_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | 144.49 | 186.06 | (0.30*0.00 + 0.30*3.58 + 0.25*0.00 + 0.15*0.00)*0.78 - 0.07 | L038,L039 |
| AMD | 512.41 | 2026-07-08 | DELAYED | 543.16 | 2026-08-05 | 6.00% | 23.72% | REALIZED_VOL_30D | 0.25 | 0.49 | 0.21 | 5.00% | -33.13% | -42.86% | -16.61% | BUY_SETUP_2/SELL_SETUP_9/SELL_SETUP_4 | 50.57/71.78/73.74 | BELOW_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | 416.76 | 669.56 | (0.30*0.00 + 0.30*3.46 + 0.25*0.00 + 0.15*0.00)*0.78 - 0.07 | L040,L041 |
| MRNA | 74.52 | 2026-07-08 | DELAYED | 78.99 | 2026-08-05 | 6.00% | 23.39% | REALIZED_VOL_30D | 0.26 | 0.61 | 0.27 | 5.00% | -32.59% | -42.18% | -18.40% | SELL_SETUP_8/SELL_SETUP_5/SELL_SETUP_8 | 66.3/70.25/54.94 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | 60.86 | 97.12 | (0.30*0.00 + 0.30*3.28 + 0.25*0.00 + 0.15*0.00)*0.78 - 0.06 | L042,L043 |
| AXON | 602.40 | 2026-07-08 | DELAYED | 638.54 | 2026-08-05 | 6.00% | 21.36% | REALIZED_VOL_30D | 0.28 | 0.82 | 0.30 | 5.00% | -29.25% | -38.01% | -20.10% | SELL_SETUP_9/SELL_SETUP_7/SELL_SETUP_2 | 69.58/60.91/55.68 | ABOVE_SIGNAL/ABOVE_SIGNAL/BELOW_SIGNAL | 504.71 | 772.38 | (0.30*0.00 + 0.30*3.30 + 0.25*0.00 + 0.15*0.00)*0.78 - 0.07 | L044,L045 |

## Excluded-Name Rationale

Every ranked name is excluded from live sizing for the same process reason: missing earnings calendar plus missing fundamental/revision and sentiment/positioning feeds. The paper sleeve remains useful for future settlement, not execution.
