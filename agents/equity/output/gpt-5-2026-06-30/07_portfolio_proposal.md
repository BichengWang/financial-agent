# 07 Portfolio Proposal

## Constraint Feasibility Pre-Check

The investable-grade set is GOOGL, CAT, UNH, GE, LLY, BAC. At the protected 5% single-name cap, maximum gross exposure is 30.00% and maximum achievable NAV beta using positive-beta investable names is 0.263, below the required 0.90-1.10 band. The run therefore publishes `NO_TRADE`; no executable weights are approved.

## Max-Cap Diagnostic Basket (Not Approved)

| Ticker | Weight | Entry Price | Price Date | Price Tag | Target Price | Target Date | mu | sigma | Sigma Source | Sharpe | Sortino | IR | Kelly 0.25 | VaR95 | CVaR95 | Max DD60 | TD9 D/W/M | RSI14 D/W/M | MACD D/W/M | 70% CI Lo | 70% CI Hi | Score Trace | Ledger Rows |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| GOOGL | 5.00% | 354.50 | 2026-06-30 | LIVE | 375.77 | 2026-07-28 | +6.0% | 9.30% | REALIZED_VOL_30D | 0.65 | 1.07 | 0.62 | 5.00% | -9.34% | -13.15% | -16.20% | SELL_SETUP_2/BUY_SETUP_6/SELL_SETUP_3 | 46.13/55.35/68.28 | BELOW_SIGNAL/BELOW_SIGNAL/ABOVE_SIGNAL | 341.49 | 410.05 | RawAdjZ=(0.30*3.58+0.30*-0.18+0.25*3.88+0.15*0.87)*0.90-0.00=1.91; Adj Score=100.0 sampled pct | L016,L017,L018,L019,L020,L021,L022 |
| CAT | 5.00% | 1068.61 | 2026-06-30 | LIVE | 1132.73 | 2026-07-28 | +6.0% | 14.19% | REALIZED_VOL_30D | 0.42 | 0.74 | 0.46 | 5.00% | -17.41% | -23.23% | -8.97% | SELL_SETUP_2/SELL_SETUP_5/SELL_SETUP_9 | 65.66/85.71/86.19 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | 975.03 | 1290.42 | RawAdjZ=(0.30*-0.41+0.30*2.10+0.25*1.33+0.15*2.26)*0.90-0.00=1.06; Adj Score=97.0 sampled pct | L135,L136,L137,L138,L139,L140,L141 |
| UNH | 5.00% | 416.76 | 2026-06-30 | LIVE | 437.60 | 2026-07-28 | +5.0% | 7.62% | REALIZED_VOL_30D | 0.66 | 1.52 | 0.54 | 5.00% | -7.57% | -10.69% | -6.06% | SELL_SETUP_6/SELL_SETUP_9/SELL_SETUP_3 | 61.71/65.60/52.44 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | 404.59 | 470.61 | RawAdjZ=(0.30*0.06+0.30*1.70+0.25*0.41+0.15*2.08)*0.90-0.00=0.85; Adj Score=93.9 sampled pct | L121,L122,L123,L124,L125,L126,L127 |
| GE | 5.00% | 373.64 | 2026-06-30 | LIVE | 392.32 | 2026-07-28 | +5.0% | 8.98% | REALIZED_VOL_30D | 0.56 | 0.73 | 0.44 | 5.00% | -9.82% | -13.50% | -13.12% | SELL_SETUP_9/SELL_SETUP_7/SELL_SETUP_2 | 74.57/68.65/74.97 | ABOVE_SIGNAL/ABOVE_SIGNAL/BULLISH_CROSS | 357.42 | 427.21 | RawAdjZ=(0.30*0.09+0.30*1.43+0.25*0.74+0.15*1.65)*0.90-0.00=0.80; Adj Score=90.9 sampled pct | L142,L143,L144,L145,L146,L147,L148 |
| LLY | 5.00% | 1206.62 | 2026-06-30 | LIVE | 1254.89 | 2026-07-28 | +4.0% | 10.04% | REALIZED_VOL_30D | 0.40 | 0.97 | 0.36 | 5.00% | -12.57% | -16.68% | -10.89% | SELL_SETUP_5/SELL_SETUP_9/SELL_SETUP_2 | 67.94/67.92/68.04 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | 1128.89 | 1380.89 | RawAdjZ=(0.30*0.09+0.30*1.24+0.25*0.94+0.15*1.14)*0.90-0.00=0.73; Adj Score=87.9 sampled pct | L114,L115,L116,L117,L118,L119,L120 |
| BAC | 5.00% | 57.24 | 2026-06-30 | LIVE | 58.95 | 2026-07-28 | +3.0% | 5.33% | REALIZED_VOL_30D | 0.56 | 0.93 | 0.50 | 5.00% | -5.79% | -7.98% | -8.38% | BUY_SETUP_2/SELL_SETUP_5/SELL_SETUP_1 | 64.73/61.62/65.47 | ABOVE_SIGNAL/ABOVE_SIGNAL/BULLISH_CROSS | 55.78 | 62.12 | RawAdjZ=(0.30*0.99+0.30*0.91+0.25*0.43+0.15*0.54)*0.90-0.10=0.58; Adj Score=84.8 sampled pct | L093,L094,L095,L096,L097,L098,L099 |

## Portfolio Analytics

| Metric | Value | Lineage |
| --- | --- | --- |
| Gross exposure | 30.00% | 5% cap times investable names |
| Expected NAV return | +1.45% | sum(weight x mu) |
| Expected beta | 0.255 | sum(weight x beta) for diagnostic basket |
| Maximum achievable NAV beta | 0.263 | sum(5% x positive beta) across investable names |
| Average pairwise correlation | 0.180 | 60d fetched daily returns |
| Portfolio sigma | 1.77% | sqrt(w covariance w) scaled to 1m |
| VaR95 | -1.47% | parametric normal return-space estimate |
| CVaR95 | -2.20% | parametric normal return-space estimate |
| 95th-pctl drawdown | 2.92% | 1.65 x portfolio sigma |

## Sector Table

| Sector | Weight | Names |
| --- | --- | --- |
| Communication Services | 5.00% | GOOGL |
| Financials | 5.00% | BAC |
| Health Care | 10.00% | UNH, LLY |
| Industrials | 10.00% | CAT, GE |

## Correlation Matrix

|  | GOOGL | CAT | UNH | GE | LLY | BAC |
| --- | --- | --- | --- | --- | --- | --- |
| GOOGL | 1.00 | 0.37 | 0.03 | 0.40 | 0.34 | 0.14 |
| CAT | 0.37 | 1.00 | -0.08 | 0.43 | 0.22 | 0.27 |
| UNH | 0.03 | -0.08 | 1.00 | -0.20 | 0.10 | -0.06 |
| GE | 0.40 | 0.43 | -0.20 | 1.00 | 0.19 | 0.49 |
| LLY | 0.34 | 0.22 | 0.10 | 0.19 | 1.00 | 0.07 |
| BAC | 0.14 | 0.27 | -0.06 | 0.49 | 0.07 | 1.00 |

## Excluded-Name Rationale

Monitoring names are excluded because admitting sub-threshold names to repair beta would violate the factor-scoring threshold. Raising weights above 5% would violate the protected single-name cap.
