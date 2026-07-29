# 07 Portfolio Proposal — 2026-07-29

**No portfolio is proposed. Final construction state: NO_TRADE.**

The factor stage produced zero investable equities, so sizing is prohibited. An equal-weight 5%-per-name monitoring diagnostic is shown only to test feasibility; it is not an execution proposal.

## Constraint feasibility pre-check

| Metric | Value | Finding |
|---|---|---|
| Expected return | 6.00% | Equal-weight monitoring diagnostic |
| Beta vs SPY | -0.386 | FAIL; required 0.90–1.10 |
| Portfolio sigma (1m) | 5.00% | Derived from 60d covariance |
| Sharpe | 1.136 | Diagnostic only |
| Sortino | 1.932 | Diagnostic only |
| Information ratio | 1.293 | Diagnostic only |
| Tracking error | 4.79% | Derived |
| VaR95 return-space | -2.25% | Normality assumed |
| CVaR95 return-space | -4.31% | Normality assumed |
| 95th-pctl drawdown | 8.25% | FAIL; cap 8% |
| Average pairwise correlation | 0.287 | PASS; cap 0.45 |
| Required-input completeness | 100.00% | PASS; threshold 85% |
| Buffered earnings events | 1 | PASS; WTW |

The beta band, drawdown cap, sector cap, factor-family threshold, and max-family-conviction rule fail before sizing. Required-input completeness and the event-count rule pass. No revision pass can manufacture missing factor families.

## Sector diagnostic

| Sector | Names | Equal-weight share | 30% cap |
|---|---|---|---|
| Consumer Staples | 3 | 15.00% | PASS |
| Financials | 7 | 35.00% | FAIL |
| Health Care | 2 | 10.00% | PASS |
| Industrials | 7 | 35.00% | FAIL |
| Real Estate | 1 | 5.00% | PASS |

## Correlation matrix — monitoring diagnostic

| Ticker | PAYX | ADP | TRV | MRSH | BRO | INCY | RTX | IQV | CTAS | KO | VLTO | PM | SCHW | ITW | WELL | UNP | RJF | AMP | WTW | SJM |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| PAYX | 1.00 | 0.94 | 0.28 | 0.70 | 0.67 | 0.06 | 0.04 | 0.39 | 0.54 | 0.40 | 0.55 | 0.23 | 0.33 | 0.11 | 0.06 | 0.14 | 0.19 | 0.21 | 0.71 | 0.38 |
| ADP | 0.94 | 1.00 | 0.29 | 0.73 | 0.73 | 0.10 | 0.07 | 0.42 | 0.55 | 0.38 | 0.56 | 0.21 | 0.37 | 0.06 | 0.02 | 0.14 | 0.25 | 0.24 | 0.78 | 0.34 |
| TRV | 0.28 | 0.29 | 1.00 | 0.47 | 0.48 | 0.24 | 0.15 | 0.02 | 0.27 | 0.17 | 0.27 | 0.29 | 0.08 | 0.06 | 0.44 | 0.31 | 0.15 | 0.09 | 0.43 | 0.25 |
| MRSH | 0.70 | 0.73 | 0.47 | 1.00 | 0.90 | 0.33 | 0.22 | 0.44 | 0.58 | 0.50 | 0.54 | 0.23 | 0.34 | 0.09 | 0.24 | 0.22 | 0.29 | 0.25 | 0.87 | 0.47 |
| BRO | 0.67 | 0.73 | 0.48 | 0.90 | 1.00 | 0.27 | 0.24 | 0.45 | 0.62 | 0.47 | 0.60 | 0.23 | 0.29 | 0.16 | 0.21 | 0.23 | 0.26 | 0.24 | 0.87 | 0.46 |
| INCY | 0.06 | 0.10 | 0.24 | 0.33 | 0.27 | 1.00 | 0.09 | 0.46 | 0.20 | 0.43 | 0.29 | 0.16 | 0.02 | 0.16 | 0.36 | 0.06 | 0.11 | 0.05 | 0.23 | 0.21 |
| RTX | 0.04 | 0.07 | 0.15 | 0.22 | 0.24 | 0.09 | 1.00 | 0.13 | 0.22 | -0.03 | 0.22 | 0.06 | 0.32 | 0.26 | 0.12 | 0.16 | 0.27 | 0.26 | 0.21 | 0.11 |
| IQV | 0.39 | 0.42 | 0.02 | 0.44 | 0.45 | 0.46 | 0.13 | 1.00 | 0.37 | 0.27 | 0.45 | 0.01 | 0.17 | 0.30 | -0.06 | -0.00 | 0.13 | 0.16 | 0.41 | 0.18 |
| CTAS | 0.54 | 0.55 | 0.27 | 0.58 | 0.62 | 0.20 | 0.22 | 0.37 | 1.00 | 0.35 | 0.50 | 0.28 | 0.19 | 0.41 | 0.26 | 0.29 | 0.23 | 0.29 | 0.53 | 0.51 |
| KO | 0.40 | 0.38 | 0.17 | 0.50 | 0.47 | 0.43 | -0.03 | 0.27 | 0.35 | 1.00 | 0.38 | 0.46 | 0.15 | 0.29 | 0.36 | 0.15 | 0.09 | 0.07 | 0.43 | 0.57 |
| VLTO | 0.55 | 0.56 | 0.27 | 0.54 | 0.60 | 0.29 | 0.22 | 0.45 | 0.50 | 0.38 | 1.00 | 0.32 | 0.24 | 0.44 | 0.21 | 0.22 | 0.22 | 0.16 | 0.56 | 0.30 |
| PM | 0.23 | 0.21 | 0.29 | 0.23 | 0.23 | 0.16 | 0.06 | 0.01 | 0.28 | 0.46 | 0.32 | 1.00 | 0.14 | 0.10 | 0.32 | 0.14 | -0.00 | 0.00 | 0.20 | 0.43 |
| SCHW | 0.33 | 0.37 | 0.08 | 0.34 | 0.29 | 0.02 | 0.32 | 0.17 | 0.19 | 0.15 | 0.24 | 0.14 | 1.00 | 0.02 | 0.02 | 0.00 | 0.73 | 0.67 | 0.40 | 0.05 |
| ITW | 0.11 | 0.06 | 0.06 | 0.09 | 0.16 | 0.16 | 0.26 | 0.30 | 0.41 | 0.29 | 0.44 | 0.10 | 0.02 | 1.00 | 0.18 | 0.35 | 0.24 | 0.31 | 0.09 | 0.12 |
| WELL | 0.06 | 0.02 | 0.44 | 0.24 | 0.21 | 0.36 | 0.12 | -0.06 | 0.26 | 0.36 | 0.21 | 0.32 | 0.02 | 0.18 | 1.00 | 0.40 | 0.09 | 0.10 | 0.13 | 0.43 |
| UNP | 0.14 | 0.14 | 0.31 | 0.22 | 0.23 | 0.06 | 0.16 | -0.00 | 0.29 | 0.15 | 0.22 | 0.14 | 0.00 | 0.35 | 0.40 | 1.00 | 0.07 | 0.13 | 0.21 | 0.11 |
| RJF | 0.19 | 0.25 | 0.15 | 0.29 | 0.26 | 0.11 | 0.27 | 0.13 | 0.23 | 0.09 | 0.22 | -0.00 | 0.73 | 0.24 | 0.09 | 0.07 | 1.00 | 0.84 | 0.38 | -0.04 |
| AMP | 0.21 | 0.24 | 0.09 | 0.25 | 0.24 | 0.05 | 0.26 | 0.16 | 0.29 | 0.07 | 0.16 | 0.00 | 0.67 | 0.31 | 0.10 | 0.13 | 0.84 | 1.00 | 0.34 | -0.07 |
| WTW | 0.71 | 0.78 | 0.43 | 0.87 | 0.87 | 0.23 | 0.21 | 0.41 | 0.53 | 0.43 | 0.56 | 0.20 | 0.40 | 0.09 | 0.13 | 0.21 | 0.38 | 0.34 | 1.00 | 0.36 |
| SJM | 0.38 | 0.34 | 0.25 | 0.47 | 0.46 | 0.21 | 0.11 | 0.18 | 0.51 | 0.57 | 0.30 | 0.43 | 0.05 | 0.12 | 0.43 | 0.11 | -0.04 | -0.07 | 0.36 | 1.00 |

## Per-position recommendation metrics

| Ticker | Entry | Target | Target Date | mu | sigma | Sharpe | Sortino | IR | Kelly 0.25 capped | VaR95 | CVaR95 | Max DD60 | TD9 D/W/M | RSI14 D/W/M | MACD D/W/M | 70% CI | Score Trace | Ledger |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| PAYX | $118.87 | $126.00 | 2026-08-26 | 6.00% | 9.57% | 0.594 | 0.824 | 0.702 | 5.00% | -9.78% | -13.71% | -6.35% | SELL_SETUP_2/SELL_SETUP_9/SELL_SETUP_2 | 73.0/69.7/53.9 | ABOVE_SIGNAL/ABOVE_SIGNAL/BELOW_SIGNAL | $114.18–$137.83 | F=U0 T=1.090 S=U0 M=0.726 ×DQ=0.80 −P=0.00 → 0.349 | L045 |
| ADP | $264.17 | $280.02 | 2026-08-26 | 6.00% | 9.83% | 0.578 | 0.902 | 0.704 | 5.00% | -10.22% | -14.25% | -7.49% | SELL_SETUP_2/SELL_SETUP_6/SELL_SETUP_2 | 69.2/64.8/54.6 | BULLISH_CROSS/ABOVE_SIGNAL/BELOW_SIGNAL | $253.02–$307.02 | F=U0 T=1.045 S=U0 M=0.686 ×DQ=0.80 −P=0.00 → 0.333 | L046 |
| TRV | $397.22 | $421.05 | 2026-08-26 | 6.00% | 9.16% | 0.620 | 1.082 | 0.877 | 5.00% | -9.12% | -12.88% | -5.96% | SELL_SETUP_8/SELL_SETUP_9/SELL_SETUP_9 | 83.3/81.2/78.1 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | $383.20–$458.91 | F=U0 T=0.928 S=U0 M=0.840 ×DQ=0.80 −P=0.00 → 0.324 | L047 |
| MRSH | $192.19 | $203.72 | 2026-08-26 | 6.00% | 9.42% | 0.603 | 0.827 | 0.843 | 5.00% | -9.55% | -13.41% | -6.28% | SELL_SETUP_2/SELL_SETUP_6/SELL_SETUP_1 | 70.5/63.2/51.8 | BULLISH_CROSS/ABOVE_SIGNAL/BELOW_SIGNAL | $184.88–$222.56 | F=U0 T=0.896 S=U0 M=0.853 ×DQ=0.80 −P=0.00 → 0.317 | L048 |
| BRO | $73.65 | $78.07 | 2026-08-26 | 6.00% | 11.35% | 0.501 | 0.795 | 0.664 | 5.00% | -12.72% | -17.38% | -9.33% | SELL_SETUP_2/SELL_SETUP_9/SELL_SETUP_1 | 69.1/57.9/45.6 | BULLISH_CROSS/ABOVE_SIGNAL/BELOW_SIGNAL | $69.38–$86.76 | F=U0 T=1.013 S=U0 M=0.554 ×DQ=0.80 −P=0.00 → 0.310 | L049 |
| INCY | $129.93 | $137.73 | 2026-08-26 | 6.00% | 12.72% | 0.447 | 0.571 | 0.571 | 5.00% | -14.99% | -20.21% | -9.50% | SELL_SETUP_3/SELL_SETUP_9/SELL_SETUP_2 | 76.8/72.7/77.3 | BULLISH_CROSS/ABOVE_SIGNAL/ABOVE_SIGNAL | $120.53–$154.92 | F=U0 T=1.171 S=U0 M=0.228 ×DQ=0.80 −P=0.00 → 0.308 | L050 |
| RTX | $218.58 | $231.69 | 2026-08-26 | 6.00% | 9.33% | 0.609 | 0.716 | 0.708 | 5.00% | -9.40% | -13.23% | -5.58% | SELL_SETUP_5/SELL_SETUP_9/SELL_SETUP_1 | 77.4/69.2/76.0 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | $210.47–$252.92 | F=U0 T=0.884 S=U0 M=0.616 ×DQ=0.80 −P=0.00 → 0.286 | L051 |
| IQV | $242.94 | $257.52 | 2026-08-26 | 6.00% | 15.75% | 0.361 | 0.685 | 0.403 | 5.00% | -19.98% | -26.44% | -10.23% | SELL_SETUP_4/SELL_SETUP_6/SELL_SETUP_2 | 79.5/69.1/58.9 | BULLISH_CROSS/ABOVE_SIGNAL/BULLISH_CROSS | $217.73–$297.30 | F=U0 T=1.332 S=U0 M=-0.284 ×DQ=0.80 −P=0.00 → 0.286 | L052 |
| CTAS | $214.90 | $227.79 | 2026-08-26 | 6.00% | 9.87% | 0.576 | 0.783 | 0.679 | 5.00% | -10.29% | -14.34% | -7.19% | SELL_SETUP_3/SELL_SETUP_6/SELL_SETUP_1 | 77.3/68.8/60.7 | ABOVE_SIGNAL/ABOVE_SIGNAL/BELOW_SIGNAL | $205.73–$249.86 | F=U0 T=0.878 S=U0 M=0.568 ×DQ=0.80 −P=0.00 → 0.279 | L053 |
| KO | $88.27 | $93.57 | 2026-08-26 | 6.00% | 8.07% | 0.704 | 0.857 | 0.954 | 5.00% | -7.32% | -10.63% | -6.23% | SELL_SETUP_3/SELL_SETUP_1/SELL_SETUP_9 | 67.0/69.1/73.3 | BULLISH_CROSS/ABOVE_SIGNAL/ABOVE_SIGNAL | $86.16–$100.98 | F=U0 T=0.689 S=U0 M=0.900 ×DQ=0.80 −P=0.00 → 0.273 | L054 |
| VLTO | $98.47 | $104.38 | 2026-08-26 | 6.00% | 7.64% | 0.744 | 0.877 | 0.861 | 5.00% | -6.60% | -9.73% | -7.33% | SELL_SETUP_2/SELL_SETUP_6/SELL_SETUP_1 | 70.2/60.4/57.6 | BULLISH_CROSS/ABOVE_SIGNAL/UNAVAILABLE | $96.56–$112.20 | F=U0 T=0.660 S=U0 M=0.813 ×DQ=0.80 −P=0.00 → 0.256 | L055 |
| PM | $200.17 | $212.18 | 2026-08-26 | 6.00% | 9.30% | 0.611 | 0.658 | 0.722 | 5.00% | -9.35% | -13.17% | -10.01% | SELL_SETUP_3/SELL_SETUP_3/SELL_SETUP_1 | 65.7/67.8/70.6 | ABOVE_SIGNAL/ABOVE_SIGNAL/BULLISH_CROSS | $192.81–$231.55 | F=U0 T=0.668 S=U0 M=0.607 ×DQ=0.80 −P=0.00 → 0.233 | L056 |
| SCHW | $105.97 | $112.33 | 2026-08-26 | 6.00% | 7.57% | 0.751 | 0.755 | 0.834 | 5.00% | -6.49% | -9.59% | -7.62% | SELL_SETUP_2/SELL_SETUP_9/SELL_SETUP_1 | 69.8/66.9/65.6 | BULLISH_CROSS/ABOVE_SIGNAL/BELOW_SIGNAL | $103.99–$120.67 | F=U0 T=0.578 S=U0 M=0.780 ×DQ=0.80 −P=0.00 → 0.232 | L057 |
| ITW | $295.16 | $312.87 | 2026-08-26 | 6.00% | 7.14% | 0.795 | 0.875 | 0.957 | 5.00% | -5.79% | -8.72% | -5.65% | SELL_SETUP_4/SELL_SETUP_8/SELL_SETUP_1 | 72.9/68.3/63.0 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | $290.94–$334.80 | F=U0 T=0.675 S=U0 M=0.582 ×DQ=0.80 −P=0.00 → 0.232 | L058 |
| WELL | $243.57 | $258.18 | 2026-08-26 | 6.00% | 7.11% | 0.799 | 0.845 | 0.858 | 5.00% | -5.73% | -8.64% | -11.26% | BUY_SETUP_1/SELL_SETUP_6/SELL_SETUP_4 | 60.3/66.1/76.3 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | $240.18–$276.19 | F=U0 T=0.501 S=U0 M=0.789 ×DQ=0.80 −P=0.00 → 0.215 | L059 |
| UNP | $294.45 | $312.12 | 2026-08-26 | 6.00% | 7.72% | 0.736 | 0.767 | 0.820 | 5.00% | -6.74% | -9.91% | -7.58% | SELL_SETUP_4/SELL_SETUP_6/SELL_SETUP_9 | 57.1/64.4/66.4 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | $288.47–$335.77 | F=U0 T=0.521 S=U0 M=0.725 ×DQ=0.80 −P=0.00 → 0.212 | L060 |
| RJF | $177.18 | $187.81 | 2026-08-26 | 6.00% | 7.32% | 0.777 | 1.034 | 0.790 | 5.00% | -6.07% | -9.07% | -10.90% | SELL_SETUP_3/SELL_SETUP_8/SELL_SETUP_1 | 73.3/67.2/62.0 | BULLISH_CROSS/ABOVE_SIGNAL/BELOW_SIGNAL | $174.33–$201.29 | F=U0 T=0.628 S=U0 M=0.467 ×DQ=0.80 −P=0.00 → 0.207 | L061 |
| AMP | $546.62 | $579.42 | 2026-08-26 | 6.00% | 7.84% | 0.725 | 0.871 | 0.818 | 5.00% | -6.94% | -10.15% | -7.46% | SELL_SETUP_3/SELL_SETUP_7/SELL_SETUP_1 | 72.8/69.9/60.9 | ABOVE_SIGNAL/ABOVE_SIGNAL/BELOW_SIGNAL | $534.85–$623.99 | F=U0 T=0.582 S=U0 M=0.545 ×DQ=0.80 −P=0.00 → 0.205 | L062 |
| WTW | $316.16 | $335.13 | 2026-08-26 | 6.00% | 9.18% | 0.619 | 0.988 | 0.786 | 5.00% | -9.14% | -12.90% | -6.88% | SELL_SETUP_3/SELL_SETUP_6/SELL_SETUP_1 | 73.9/62.2/56.5 | ABOVE_SIGNAL/ABOVE_SIGNAL/BELOW_SIGNAL | $304.96–$365.30 | F=U0 T=0.841 S=U0 M=0.839 ×DQ=0.80 −P=0.10 → 0.202 | L063 |
| SJM | $123.04 | $130.42 | 2026-08-26 | 6.00% | 9.56% | 0.594 | 0.562 | 0.652 | 5.00% | -9.78% | -13.70% | -8.42% | SELL_SETUP_9/SELL_SETUP_3/SELL_SETUP_1 | 67.2/67.2/58.7 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | $118.19–$142.66 | F=U0 T=0.465 S=U0 M=0.725 ×DQ=0.80 −P=0.00 → 0.199 | L064 |

Excluded names were left out because of binding reflection `DROP` decisions or lower post-penalty scores. The published 20 remain monitoring forecasts only.
