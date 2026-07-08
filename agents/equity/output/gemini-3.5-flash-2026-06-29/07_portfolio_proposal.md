# 07 Portfolio Proposal

## Constraint Feasibility Pre-Check

The investable-grade set is CAT, LLY, GOOGL, UNH, GE, BAC, JPM. At the protected 5% single-name cap, maximum gross exposure is 35.00% and maximum NAV beta is 0.280, below the required 0.90-1.10 band. The run therefore publishes `NO_TRADE`; no executable weights are approved.

## Max-Cap Diagnostic Basket (Not Approved)

| Ticker | Weight | Entry Price | Price Date | Price Tag | Target Price | Target Date | mu | sigma | Sigma Source | Sharpe | Sortino | IR | Kelly 0.25 | VaR95 | CVaR95 | Max DD60 | TD9 D/W/M | RSI14 D/W/M | MACD D/W/M | 70% CI Lo | 70% CI Hi | Score Trace | Ledger Rows |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CAT | 5.00% | 997.47 | 2026-06-26 | DELAYED | 1057.32 | 2026-07-27 | +6.0% | 14.20% | REALIZED_VOL_30D | 0.42 | 0.76 | 0.37 | 5.00% | -17.42% | -23.24% | -8.97% | BUY_SETUP_1/SELL_SETUP_4/SELL_SETUP_9 | 58.51/82.55/84.78 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | 910.05 | 1204.59 | RawAdjZ=(0.30*1.85+0.30*1.77+0.25*2.18+0.15*1.16)*0.90-0.00=1.63; Adj Score=100.0 sampled pct | L135,L136,L137,L138,L139,L140,L141 |
| LLY | 5.00% | 1208.12 | 2026-06-26 | DELAYED | 1280.61 | 2026-07-27 | +6.0% | 9.87% | REALIZED_VOL_30D | 0.61 | 1.45 | 0.53 | 5.00% | -10.28% | -14.32% | -10.89% | SELL_SETUP_3/SELL_SETUP_9/SELL_SETUP_2 | 72.35/68.25/68.12 | BELOW_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | 1156.65 | 1404.56 | RawAdjZ=(0.30*1.09+0.30*1.13+0.25*1.16+0.15*0.72)*0.90-0.00=0.96; Adj Score=97.0 sampled pct | L114,L115,L116,L117,L118,L119,L120 |
| GOOGL | 5.00% | 337.39 | 2026-06-26 | DELAYED | 354.26 | 2026-07-27 | +5.0% | 8.13% | REALIZED_VOL_30D | 0.61 | 0.91 | 0.42 | 5.00% | -8.42% | -11.75% | -16.20% | BUY_SETUP_5/BUY_SETUP_5/SELL_SETUP_3 | 33.27/50.84/64.7 | BELOW_SIGNAL/BELOW_SIGNAL/ABOVE_SIGNAL | 325.72 | 382.80 | RawAdjZ=(0.30*1.85+0.30*-0.84+0.25*2.18+0.15*1.17)*0.90-0.00=0.92; Adj Score=93.9 sampled pct | L016,L017,L018,L019,L020,L021,L022 |
| UNH | 5.00% | 427.89 | 2026-06-26 | DELAYED | 449.28 | 2026-07-27 | +5.0% | 7.50% | REALIZED_VOL_30D | 0.67 | 1.53 | 0.54 | 5.00% | -7.37% | -10.45% | -6.06% | SELL_SETUP_4/SELL_SETUP_9/SELL_SETUP_3 | 71.55/69.37/53.44 | BULLISH_CROSS/ABOVE_SIGNAL/ABOVE_SIGNAL | 415.91 | 482.66 | RawAdjZ=(0.30*0.87+0.30*1.77+0.25*-0.03+0.15*1.05)*0.90-0.00=0.85; Adj Score=90.9 sampled pct | L121,L122,L123,L124,L125,L126,L127 |
| GE | 5.00% | 369.00 | 2026-06-26 | DELAYED | 383.76 | 2026-07-27 | +4.0% | 9.80% | REALIZED_VOL_30D | 0.41 | 0.57 | 0.26 | 5.00% | -12.18% | -16.20% | -13.12% | SELL_SETUP_9/SELL_SETUP_6/SELL_SETUP_2 | 72.81/67.69/74.51 | ABOVE_SIGNAL/ABOVE_SIGNAL/BULLISH_CROSS | 346.14 | 421.38 | RawAdjZ=(0.30*0.53+0.30*1.77+0.25*0.30+0.15*1.17)*0.90-0.00=0.85; Adj Score=87.9 sampled pct | L142,L143,L144,L145,L146,L147,L148 |
| BAC | 5.00% | 57.88 | 2026-06-26 | DELAYED | 59.62 | 2026-07-27 | +3.0% | 5.18% | REALIZED_VOL_30D | 0.58 | 0.91 | 0.47 | 5.00% | -5.55% | -7.67% | -8.38% | SELL_SETUP_9/SELL_SETUP_4/SELL_SETUP_1 | 71.05/63.55/66.08 | ABOVE_SIGNAL/ABOVE_SIGNAL/BULLISH_CROSS | 56.50 | 62.73 | RawAdjZ=(0.30*0.78+0.30*1.45+0.25*-0.22+0.15*0.52)*0.90-0.10=0.52; Adj Score=84.8 sampled pct | L093,L094,L095,L096,L097,L098,L099 |
| JPM | 5.00% | 329.05 | 2026-06-26 | DELAYED | 338.92 | 2026-07-27 | +3.0% | 6.92% | REALIZED_VOL_30D | 0.43 | 0.85 | 0.42 | 5.00% | -8.42% | -11.26% | -6.72% | BUY_SETUP_1/SELL_SETUP_4/SELL_SETUP_1 | 60.27/61.15/68.2 | ABOVE_SIGNAL/ABOVE_SIGNAL/BELOW_SIGNAL | 315.24 | 362.60 | RawAdjZ=(0.30*0.50+0.30*1.12+0.25*-0.01+0.15*0.24)*0.90-0.10=0.37; Adj Score=81.8 sampled pct | L086,L087,L088,L089,L090,L091,L092 |

## Portfolio Analytics

| Metric | Value | Lineage |
| --- | --- | --- |
| Gross exposure | 35.00% | 5% cap times investable names |
| Expected NAV return | +1.6% | sum(weight x mu) |
| Expected beta | 0.280 | sum(weight x beta) |
| Average pairwise correlation | 0.227 | 60d fetched daily returns |
| Portfolio sigma | 2.00% | sqrt(w covariance w) scaled to 1m |
| VaR95 | -1.69% | parametric normal return-space estimate |
| CVaR95 | -2.51% | parametric normal return-space estimate |
| 95th-pctl drawdown | 3.29% | 1.65 x portfolio sigma |

## Sector Table

| Sector | Weight | Names |
| --- | --- | --- |
| Industrials | 10.00% | CAT, GE |
| Health Care | 10.00% | LLY, UNH |
| Communication Services | 5.00% | GOOGL |
| Financials | 10.00% | BAC, JPM |

## Correlation Matrix

|  | CAT | LLY | GOOGL | UNH | GE | BAC | JPM |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CAT | 1.00 | 0.26 | 0.37 | -0.05 | 0.45 | 0.30 | 0.42 |
| LLY | 0.26 | 1.00 | 0.36 | 0.11 | 0.23 | 0.06 | 0.08 |
| GOOGL | 0.37 | 0.36 | 1.00 | 0.08 | 0.41 | 0.17 | 0.15 |
| UNH | -0.05 | 0.11 | 0.08 | 1.00 | -0.19 | -0.08 | -0.04 |
| GE | 0.45 | 0.23 | 0.41 | -0.19 | 1.00 | 0.48 | 0.46 |
| BAC | 0.30 | 0.06 | 0.17 | -0.08 | 0.48 | 1.00 | 0.72 |
| JPM | 0.42 | 0.08 | 0.15 | -0.04 | 0.46 | 0.72 | 1.00 |

## Excluded-Name Rationale

Monitoring names are excluded because admitting sub-threshold names to repair beta would violate the factor-scoring threshold. Raising weights above 5% would violate the protected single-name cap.
