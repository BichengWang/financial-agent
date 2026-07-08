# 07 Portfolio Proposal

## Constraint Feasibility Pre-Check

The investable-grade set is CAT, GOOGL, GE, LLY, FCX, GS, BAC. At the protected 5% single-name cap, maximum gross exposure is 35.00% and maximum NAV beta is 0.522, below the required 0.90-1.10 band. The run therefore publishes `NO_TRADE`; no executable weights are approved.

## Max-Cap Diagnostic Basket (Not Approved)

| Ticker | Weight | Entry Price | Price Date | Price Tag | Target Price | Target Date | mu | sigma | Sigma Source | Sharpe | Sortino | IR | Kelly 0.25 | VaR95 | CVaR95 | Max DD60 | TD9 D/W/M | RSI14 D/W/M | MACD D/W/M | 70% CI Lo | 70% CI Hi | Score Trace | Ledger Rows |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CAT | 5.00% | 994.45 | 2026-06-24 | DELAYED | 1054.12 | 2026-07-22 | +6.0% | 12.41% | REALIZED_VOL_30D | 0.48 | 0.82 | 0.30 | 5.00% | -14.48% | -19.57% | -8.97% | SELL_SETUP_7/SELL_SETUP_4/SELL_SETUP_9 | 62.59/82.4/84.71 | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | 925.72 | 1182.51 | RawAdjZ=(0.30*0.83+0.30*1.54+0.25*1.00+0.15*1.38)*0.90-0.00=1.05; Adj Score=100.0 sampled pct | L142,L143,L144,L145,L146,L147,L148 |
| GOOGL | 5.00% | 345.29 | 2026-06-24 | DELAYED | 366.01 | 2026-07-22 | +6.0% | 8.88% | REALIZED_VOL_30D | 0.68 | 1.07 | 0.44 | 5.00% | -8.66% | -12.30% | -14.24% | BUY_SETUP_3/BUY_SETUP_5/SELL_SETUP_3 | 36.98/53.14/66.3 | BELOW_SIGNAL/BELOW_SIGNAL/ABOVE_SIGNAL | 334.10 | 397.91 | RawAdjZ=(0.30*2.27+0.30*-0.33+0.25*1.88+0.15*0.73)*0.90-0.00=1.05; Adj Score=97.1 sampled pct | L016,L017,L018,L019,L020,L021,L022 |
| GE | 5.00% | 365.88 | 2026-06-24 | DELAYED | 384.17 | 2026-07-22 | +5.0% | 9.94% | REALIZED_VOL_30D | 0.50 | 0.71 | 0.28 | 5.00% | -11.39% | -15.47% | -13.12% | SELL_SETUP_9/SELL_SETUP_6/SELL_SETUP_2 | 73.3/67.1/74.2 | ABOVE_SIGNAL/ABOVE_SIGNAL/BULLISH_CROSS | 346.37 | 421.98 | RawAdjZ=(0.30*0.76+0.30*1.40+0.25*1.08+0.15*0.95)*0.90-0.00=0.96; Adj Score=94.1 sampled pct | L149,L150,L151,L152,L153,L154,L155 |
| LLY | 5.00% | 1117.26 | 2026-06-24 | DELAYED | 1173.12 | 2026-07-22 | +5.0% | 8.45% | REALIZED_VOL_30D | 0.59 | 1.21 | 0.41 | 5.00% | -8.94% | -12.40% | -10.89% | SELL_SETUP_1/SELL_SETUP_9/SELL_SETUP_2 | 58.05/62.14/64.91 | BELOW_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | 1074.99 | 1271.26 | RawAdjZ=(0.30*1.18+0.30*0.98+0.25*0.94+0.15*0.30)*0.90-0.00=0.84; Adj Score=91.2 sampled pct | L121,L122,L123,L124,L125,L126,L127 |
| FCX | 5.00% | 61.84 | 2026-06-24 | DELAYED | 64.31 | 2026-07-22 | +4.0% | 16.78% | REALIZED_VOL_30D | 0.24 | 0.31 | -0.05 | 5.00% | -23.69% | -30.57% | -21.02% | BUY_SETUP_3/BUY_SETUP_1/BUY_SETUP_1 | 42.05/52.16/60.69 | BELOW_SIGNAL/BEARISH_CROSS/ABOVE_SIGNAL | 53.52 | 75.11 | RawAdjZ=(0.30*1.38+0.30*-0.18+0.25*1.54+0.15*0.34)*0.90-0.00=0.72; Adj Score=88.2 sampled pct | L212,L213,L214,L215,L216,L217,L218 |
| GS | 5.00% | 1076.91 | 2026-06-24 | DELAYED | 1119.99 | 2026-07-22 | +4.0% | 10.16% | REALIZED_VOL_30D | 0.39 | 0.76 | 0.26 | 5.00% | -12.76% | -16.92% | -8.36% | BUY_SETUP_1/SELL_SETUP_9/SELL_SETUP_9 | 58.79/72.57/79.22 | BEARISH_CROSS/ABOVE_SIGNAL/ABOVE_SIGNAL | 1006.25 | 1233.73 | RawAdjZ=(0.30*0.26+0.30*1.39+0.25*0.18+0.15*1.04)*0.90-0.10=0.53; Adj Score=85.3 sampled pct | L107,L108,L109,L110,L111,L112,L113 |
| BAC | 5.00% | 57.73 | 2026-06-24 | DELAYED | 59.46 | 2026-07-22 | +3.0% | 5.47% | REALIZED_VOL_30D | 0.55 | 0.90 | 0.40 | 5.00% | -6.03% | -8.27% | -8.38% | SELL_SETUP_9/SELL_SETUP_4/SELL_SETUP_1 | 72.51/63.29/65.94 | ABOVE_SIGNAL/ABOVE_SIGNAL/BULLISH_CROSS | 56.18 | 62.75 | RawAdjZ=(0.30*0.30+0.30*1.23+0.25*0.13+0.15*0.26)*0.90-0.00=0.48; Adj Score=82.4 sampled pct | L100,L101,L102,L103,L104,L105,L106 |

## Portfolio Analytics

| Metric | Value | Lineage |
| --- | --- | --- |
| Gross exposure | 35.00% | 5% cap times 7 names |
| Expected NAV return | +1.65% | sum(weight x mu) |
| Expected beta | 0.522 | sum(weight x beta) |
| Average pairwise correlation | 0.393 | 60d fetched daily returns |
| Portfolio sigma | 2.75% | sqrt(w covariance w) scaled to 1m |
| VaR95 | -2.89% | parametric normal return-space estimate |
| CVaR95 | -4.02% | parametric normal return-space estimate |
| 95th-pctl drawdown | 4.54% | 1.65 x portfolio sigma |

## Sector Table

| Sector | Weight | Names |
| --- | --- | --- |
| Industrials | 10.00% | CAT, GE |
| Communication Services | 5.00% | GOOGL |
| Health Care | 5.00% | LLY |
| Materials | 5.00% | FCX |
| Financials | 10.00% | GS, BAC |

## Correlation Matrix

|  | CAT | GOOGL | GE | LLY | FCX | GS | BAC |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CAT | 1.00 | 0.42 | 0.50 | 0.42 | 0.52 | 0.58 | 0.33 |
| GOOGL | 0.42 | 1.00 | 0.44 | 0.47 | 0.29 | 0.39 | 0.23 |
| GE | 0.50 | 0.44 | 1.00 | 0.28 | 0.33 | 0.53 | 0.49 |
| LLY | 0.42 | 0.47 | 0.28 | 1.00 | 0.21 | 0.27 | 0.15 |
| FCX | 0.52 | 0.29 | 0.33 | 0.21 | 1.00 | 0.65 | 0.33 |
| GS | 0.58 | 0.39 | 0.53 | 0.27 | 0.65 | 1.00 | 0.44 |
| BAC | 0.33 | 0.23 | 0.49 | 0.15 | 0.33 | 0.44 | 1.00 |

## Excluded-Name Rationale

Monitoring names are excluded because admitting sub-threshold names to repair beta would violate the factor-scoring threshold. Raising weights above 5% would violate the protected single-name cap.
