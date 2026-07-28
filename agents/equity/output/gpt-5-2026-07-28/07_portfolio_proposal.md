# 07 Portfolio Proposal — 2026-07-28

## Task 0 — Feasibility verdict

**NO PORTFOLIO / NO WEIGHTS.** Investable count is 0 because every name fails the 3-of-4 family and 85% completeness gates. It is therefore prohibited to optimize or size a sleeve. The pctl80 pool's maximum attainable beta at a 5% cap is 0.889447, below the 0.90 floor, but this is corroborating only. Equal-weighting the published monitors also fails the 30% sector cap: Industrials is 35%.

| Constraint | Observed | Limit | Result |
|---|---|---|---|
| Investable names | 0 | minimum 5 | FAIL — binding |
| Beta, pctl80 best case | 0.889447 | 0.90–1.10 | FAIL — corroborating |
| Average pairwise correlation, top10 | 0.193146 | <0.45 | PASS diagnostic |
| Industrials equal-weight share | 35% | ≤30% | FAIL |
| Earnings penalty-window names | MET, PRU, MPC | maximum 2 | FAIL diagnostic |
| Unpenalized earnings bands overlapping target | SJM, BBY | horizon-risk disclosure | FLAG diagnostic |

Portfolio Sharpe, Sortino, IR, tracking error, beta, VaR95, CVaR95, drawdown, and Kelly allocation are **NOT APPLICABLE — no portfolio was constructed**. Per-name metrics remain available in `05`; quarter-Kelly caps are diagnostic and do not authorize weights.

## Published-monitor sector diagnostic

| Sector | Names | Equal-weight share | Cap result |
|---|---|---|---|
| Consumer Discretionary | 1 | 5.00% | PASS |
| Consumer Staples | 2 | 10.00% | PASS |
| Energy | 1 | 5.00% | PASS |
| Financials | 5 | 25.00% | PASS |
| Health Care | 2 | 10.00% | PASS |
| Industrials | 7 | 35.00% | FAIL >30% |
| Real Estate | 2 | 10.00% | PASS |

## Top-10 correlation diagnostic

| Ticker | BBY | CSX | DGX | IQV | MET | PAYX | RTX | SJM | TRV | UNP |
|---|---|---|---|---|---|---|---|---|---|---|
| BBY | 1.0000 | -0.1336 | -0.0031 | 0.3612 | 0.0696 | 0.0462 | -0.0252 | 0.1213 | -0.0857 | -0.1920 |
| CSX | -0.1336 | 1.0000 | 0.3951 | 0.0804 | 0.2805 | -0.0072 | 0.1713 | -0.0597 | 0.1829 | 0.8261 |
| DGX | -0.0031 | 0.3951 | 1.0000 | 0.3998 | 0.1094 | 0.1999 | 0.5100 | 0.3952 | 0.3486 | 0.4071 |
| IQV | 0.3612 | 0.0804 | 0.3998 | 1.0000 | -0.0103 | 0.3182 | 0.1730 | 0.1725 | -0.0372 | 0.0912 |
| MET | 0.0696 | 0.2805 | 0.1094 | -0.0103 | 1.0000 | 0.3653 | 0.2261 | 0.2285 | 0.4055 | 0.4012 |
| PAYX | 0.0462 | -0.0072 | 0.1999 | 0.3182 | 0.3653 | 1.0000 | 0.0358 | 0.3599 | 0.2539 | 0.1627 |
| RTX | -0.0252 | 0.1713 | 0.5100 | 0.1730 | 0.2261 | 0.0358 | 1.0000 | 0.1186 | 0.1578 | 0.1683 |
| SJM | 0.1213 | -0.0597 | 0.3952 | 0.1725 | 0.2285 | 0.3599 | 0.1186 | 1.0000 | 0.2412 | 0.1305 |
| TRV | -0.0857 | 0.1829 | 0.3486 | -0.0372 | 0.4055 | 0.2539 | 0.1578 | 0.2412 | 1.0000 | 0.3310 |
| UNP | -0.1920 | 0.8261 | 0.4071 | 0.0912 | 0.4012 | 0.1627 | 0.1683 | 0.1305 | 0.3310 | 1.0000 |

## Per-position recommendation metrics

| Ticker | Entry | Date | Tag | Target | mu | sigma | Sharpe | Sortino | IR | Kelly cap | VaR95 | CVaR95 | MaxDD60 | TD9 D/W/M | RSI D/W/M | MACD D/W/M | CI | Score Trace | Ledger |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| RTX | $218.42 | 2026-07-27 | HISTORICAL | $231.53 | +6.00% | 9.36% | 0.6071 | 1.1112 | 0.7014 | 5.00% | -9.44% | -13.28% | -5.58% | SELL_SETUP_4/SELL_SETUP_9/SELL_SETUP_1 | 77.3/69.2/76.0 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | $210.26 to $252.79 | (0.30×UNAV + 0.30×1.211 + 0.25×UNAV + 0.15×0.609)×0.80−0.00=0.3637 | L010–L032,L045 |
| TRV | $390.35 | 2026-07-27 | HISTORICAL | $413.77 | +6.00% | 9.15% | 0.6208 | 1.8101 | 0.8771 | 5.00% | -9.10% | -12.86% | -5.96% | SELL_SETUP_7/SELL_SETUP_9/SELL_SETUP_9 | 81.7/80.2/77.5 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | $376.61 to $450.93 | (0.30×UNAV + 0.30×0.853 + 0.25×UNAV + 0.15×0.832)×0.80−0.00=0.3045 | L010–L032,L046 |
| PAYX | $115.48 | 2026-07-27 | HISTORICAL | $122.41 | +6.00% | 9.15% | 0.6212 | 1.3872 | 0.7236 | 5.00% | -9.09% | -12.85% | -6.35% | SELL_SETUP_1/SELL_SETUP_9/SELL_SETUP_2 | 67.5/66.2/51.3 | ABOVE_SIGNAL/ABOVE_SIGNAL/BELOW_SIGNAL | $111.42 to $133.40 | (0.30×UNAV + 0.30×0.840 + 0.25×UNAV + 0.15×0.783)×0.80−0.00=0.2956 | L010–L032,L047 |
| SJM | $121.05 | 2026-07-27 | HISTORICAL | $128.31 | +6.00% | 9.49% | 0.5987 | 1.1542 | 0.6501 | 5.00% | -9.66% | -13.55% | -8.42% | SELL_SETUP_8/SELL_SETUP_3/SELL_SETUP_1 | 64.8/65.8/57.8 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | $116.36 to $140.26 | (0.30×UNAV + 0.30×0.771 + 0.25×UNAV + 0.15×0.721)×0.80−0.00=0.2715 | L010–L032,L048 |
| CSX | $51.80 | 2026-07-27 | HISTORICAL | $54.91 | +6.00% | 7.42% | 0.7658 | 1.4337 | 0.8689 | 5.00% | -6.24% | -9.29% | -4.20% | SELL_SETUP_3/SELL_SETUP_9/SELL_SETUP_9 | 64.1/72.1/75.4 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | $50.91 to $58.91 | (0.30×UNAV + 0.30×0.752 + 0.25×UNAV + 0.15×0.729)×0.80−0.00=0.2680 | L010–L032,L049 |
| DGX | $231.84 | 2026-07-27 | HISTORICAL | $245.75 | +6.00% | 9.45% | 0.6012 | 2.0694 | 0.8294 | 5.00% | -9.59% | -13.47% | -6.22% | SELL_SETUP_8/SELL_SETUP_6/SELL_SETUP_6 | 75.0/69.8/69.5 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | $222.96 to $268.54 | (0.30×UNAV + 0.30×0.727 + 0.25×UNAV + 0.15×0.753)×0.80−0.00=0.2649 | L010–L032,L050 |
| IQV | $213.22 | 2026-07-27 | HISTORICAL | $226.01 | +6.00% | 11.29% | 0.5033 | 1.0474 | 0.4797 | 5.00% | -12.63% | -17.26% | -10.23% | SELL_SETUP_3/SELL_SETUP_6/SELL_SETUP_2 | 65.6/60.9/53.5 | BELOW_SIGNAL/ABOVE_SIGNAL/BULLISH_CROSS | $200.98 to $251.05 | (0.30×UNAV + 0.30×0.975 + 0.25×UNAV + 0.15×0.176)×0.80−0.00=0.2551 | L010–L032,L051 |
| BBY | $88.45 | 2026-07-27 | HISTORICAL | $93.76 | +6.00% | 8.94% | 0.6357 | 1.1828 | 0.4372 | 5.00% | -8.75% | -12.41% | -8.93% | SELL_SETUP_2/SELL_SETUP_9/SELL_SETUP_3 | 71.0/68.3/61.0 | BULLISH_CROSS/ABOVE_SIGNAL/ABOVE_SIGNAL | $85.53 to $101.98 | (0.30×UNAV + 0.30×0.948 + 0.25×UNAV + 0.15×0.205)×0.80−0.00=0.2520 | L010–L032,L052 |
| MET | $95.19 | 2026-07-27 | HISTORICAL | $100.90 | +6.00% | 7.04% | 0.8070 | 1.2328 | 0.9176 | 5.00% | -5.62% | -8.50% | -4.77% | SELL_SETUP_2/SELL_SETUP_9/SELL_SETUP_4 | 68.0/71.3/67.9 | BULLISH_CROSS/ABOVE_SIGNAL/BULLISH_CROSS | $93.93 to $107.87 | (0.30×UNAV + 0.30×1.043 + 0.25×UNAV + 0.15×0.803)×0.80−0.10=0.2468 | L010–L032,L053 |
| UNP | $299.30 | 2026-07-27 | HISTORICAL | $317.26 | +6.00% | 7.63% | 0.7448 | 1.1720 | 0.8175 | 5.00% | -6.59% | -9.72% | -7.58% | SELL_SETUP_3/SELL_SETUP_6/SELL_SETUP_9 | 62.5/67.5/67.3 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | $293.51 to $341.01 | (0.30×UNAV + 0.30×0.655 + 0.25×UNAV + 0.15×0.714)×0.80−0.00=0.2429 | L010–L032,L054 |
| IVZ | $30.11 | 2026-07-27 | HISTORICAL | $31.92 | +6.00% | 11.00% | 0.5168 | 0.8160 | 0.6304 | 5.00% | -12.14% | -16.65% | -11.40% | SELL_SETUP_4/SELL_SETUP_4/SELL_SETUP_9 | 60.7/65.0/69.2 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | $28.47 to $35.36 | (0.30×UNAV + 0.30×1.164 + 0.25×UNAV + 0.15×-0.320)×0.80−0.00=0.2411 | L010–L032,L055 |
| PRU | $121.89 | 2026-07-27 | HISTORICAL | $129.20 | +6.00% | 6.16% | 0.9221 | 1.9237 | 1.0053 | 5.00% | -4.17% | -6.70% | -2.66% | SELL_SETUP_2/SELL_SETUP_9/SELL_SETUP_2 | 72.4/70.9/64.5 | ABOVE_SIGNAL/ABOVE_SIGNAL/BULLISH_CROSS | $121.39 to $137.02 | (0.30×UNAV + 0.30×0.996 + 0.25×UNAV + 0.15×0.787)×0.80−0.10=0.2334 | L010–L032,L056 |
| NSC | $343.35 | 2026-07-27 | HISTORICAL | $363.95 | +6.00% | 7.24% | 0.7852 | 1.3475 | 0.8589 | 5.00% | -5.94% | -8.91% | -7.86% | SELL_SETUP_3/SELL_SETUP_6/SELL_SETUP_4 | 64.2/66.0/66.4 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | $338.11 to $389.79 | (0.30×UNAV + 0.30×0.613 + 0.25×UNAV + 0.15×0.716)×0.80−0.00=0.2330 | L010–L032,L057 |
| ITW | $284.82 | 2026-07-27 | HISTORICAL | $301.91 | +6.00% | 6.66% | 0.8537 | 1.7161 | 0.9586 | 5.00% | -4.98% | -7.71% | -5.65% | SELL_SETUP_3/SELL_SETUP_8/SELL_SETUP_1 | 66.4/64.1/60.8 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | $282.19 to $321.63 | (0.30×UNAV + 0.30×0.614 + 0.25×UNAV + 0.15×0.663)×0.80−0.00=0.2269 | L010–L032,L058 |
| CTAS | $210.98 | 2026-07-27 | HISTORICAL | $223.64 | +6.00% | 10.29% | 0.5524 | 1.2641 | 0.6819 | 5.00% | -10.97% | -15.19% | -7.19% | SELL_SETUP_2/SELL_SETUP_6/SELL_SETUP_1 | 75.2/67.3/59.7 | ABOVE_SIGNAL/ABOVE_SIGNAL/BELOW_SIGNAL | $201.07 to $246.21 | (0.30×UNAV + 0.30×0.673 + 0.25×UNAV + 0.15×0.539)×0.80−0.00=0.2262 | L010–L032,L059 |
| EXR | $148.29 | 2026-07-27 | HISTORICAL | $157.19 | +6.00% | 6.36% | 0.8941 | 1.7968 | 0.9211 | 5.00% | -4.49% | -7.09% | -5.45% | SELL_SETUP_2/BUY_SETUP_2/SELL_SETUP_1 | 55.3/56.6/55.0 | BULLISH_CROSS/ABOVE_SIGNAL/ABOVE_SIGNAL | $147.39 to $166.99 | (0.30×UNAV + 0.30×0.510 + 0.25×UNAV + 0.15×0.847)×0.80−0.00=0.2240 | L010–L032,L060 |
| MPC | $312.35 | 2026-07-27 | HISTORICAL | $331.09 | +6.00% | 9.46% | 0.6009 | 1.0463 | 0.6321 | 5.00% | -9.60% | -13.48% | -9.09% | BUY_SETUP_3/SELL_SETUP_6/SELL_SETUP_6 | 69.7/73.8/81.2 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | $300.37 to $361.81 | (0.30×UNAV + 0.30×1.050 + 0.25×UNAV + 0.15×0.583)×0.80−0.10=0.2221 | L010–L032,L061 |
| WELL | $248.34 | 2026-07-27 | HISTORICAL | $263.24 | +6.00% | 6.89% | 0.8252 | 1.4757 | 0.8431 | 5.00% | -5.36% | -8.19% | -11.26% | SELL_SETUP_9/SELL_SETUP_6/SELL_SETUP_4 | 67.6/69.6/77.1 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | $245.46 to $281.03 | (0.30×UNAV + 0.30×0.521 + 0.25×UNAV + 0.15×0.772)×0.80−0.00=0.2176 | L010–L032,L062 |
| CB | $358.91 | 2026-07-27 | HISTORICAL | $380.44 | +6.00% | 8.03% | 0.7080 | 1.3337 | 1.1227 | 5.00% | -7.24% | -10.53% | -6.57% | SELL_SETUP_3/BUY_SETUP_1/SELL_SETUP_9 | 59.4/64.6/69.3 | BULLISH_CROSS/ABOVE_SIGNAL/ABOVE_SIGNAL | $350.49 to $410.40 | (0.30×UNAV + 0.30×0.416 + 0.25×UNAV + 0.15×0.969)×0.80−0.00=0.2161 | L010–L032,L063 |
| PM | $195.66 | 2026-07-27 | HISTORICAL | $207.40 | +6.00% | 9.26% | 0.6140 | 1.2925 | 0.7233 | 5.00% | -9.27% | -13.07% | -10.01% | SELL_SETUP_2/SELL_SETUP_3/SELL_SETUP_1 | 62.0/65.6/69.5 | ABOVE_SIGNAL/ABOVE_SIGNAL/BULLISH_CROSS | $188.57 to $226.23 | (0.30×UNAV + 0.30×0.548 + 0.25×UNAV + 0.15×0.603)×0.80−0.00=0.2039 | L010–L032,L064 |

Excluded names were left out for failed evidence gates or unresolved earnings lineage, never to force constraints to pass.
