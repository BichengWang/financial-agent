# 07 Portfolio Proposal

## Constraint Feasibility Pre-Check

Portfolio status: `NO_TRADE`.

The investable-grade set contains 6 names. At the protected 5% single-name NAV cap, max gross exposure is 30.0% and max achievable NAV beta is **0.378**, compared with the required 0.90-1.10 band. Per the 2026-06-10 Track B instruction, construction stops before drafting weights when feasibility fails.

| Metric | Value | Limit | Result |
| --- | --- | --- | --- |
| Investable names | 6 | >= 5 | PASS |
| Max gross at 5% cap | 30.0% | no explicit minimum | Informational |
| Max NAV beta at cap | 0.378 | 0.90-1.10 | FAIL |
| Avg pairwise corr at cap | 0.499 | < 0.45 | FAIL |
| 95th-pctl 1m drawdown at cap | 3.67% | <= 8.00% | PASS |

## Sector Concentration at Cap

| Sector | Max NAV Share at 5% Cap |
| --- | --- |
| Communication Services | 5.0% |
| Financials | 15.0% |
| Industrials | 10.0% |

## Correlation Matrix

| Ticker | GS | JPM | CAT | BAC | GE | GOOGL |
| --- | --- | --- | --- | --- | --- | --- |
| GS | 1.00 | 0.61 | 0.60 | 0.48 | 0.58 | 0.44 |
| JPM | 0.61 | 1.00 | 0.50 | 0.77 | 0.51 | 0.31 |
| CAT | 0.60 | 0.50 | 1.00 | 0.37 | 0.54 | 0.47 |
| BAC | 0.48 | 0.77 | 0.37 | 1.00 | 0.52 | 0.32 |
| GE | 0.58 | 0.51 | 0.54 | 0.52 | 1.00 | 0.47 |
| GOOGL | 0.44 | 0.31 | 0.47 | 0.32 | 0.47 | 1.00 |

## Per-Position Recommendation Metrics

| Ticker | Entry Price | Price Date | Price Tag | Target Price | Target Date | mu | sigma | Sigma Source | Sharpe | Sortino | IR | Kelly 0.25 | VaR95 | CVaR95 | Max DD60 | TD9 D/W | 70% CI Lo | 70% CI Hi | Score Trace | Ledger Rows |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| GS | 1099.14 | 2026-06-17 | DELAYED | 1165.09 | 2026-07-15 | +6.0% | 10.08% | REALIZED_VOL_30D | 0.60 | 1.11 | 0.46 | 5.0% | -10.63% | -14.76% | -8.36% | SELL_SETUP_4/SELL_SETUP_9 | 1049.89 | 1280.28 | RawAdjZ=(0.30*0.24+0.30*1.48+0.25*0.32+0.15*1.36)*0.90-0.00=0.72; Adj Score=100.0 sampled pct | L127,L128,L129,L130,L131,L132 |
| JPM | 333.46 | 2026-06-17 | DELAYED | 350.13 | 2026-07-15 | +5.0% | 7.17% | REALIZED_VOL_30D | 0.70 | 1.36 | 0.61 | 5.0% | -6.83% | -9.77% | -6.72% | SELL_SETUP_5/SELL_SETUP_2 | 325.26 | 375.00 | RawAdjZ=(0.30*0.35+0.30*1.00+0.25*1.14+0.15*0.23)*0.90-0.00=0.65; Adj Score=94.1 sampled pct | L115,L116,L117,L118,L119,L120 |
| CAT | 955.92 | 2026-06-17 | DELAYED | 1003.72 | 2026-07-15 | +5.0% | 12.14% | REALIZED_VOL_30D | 0.41 | 0.71 | 0.14 | 5.0% | -15.03% | -20.00% | -8.97% | SELL_SETUP_3/BUY_SETUP_1 | 883.06 | 1124.37 | RawAdjZ=(0.30*0.00+0.30*1.00+0.25*0.49+0.15*1.62)*0.90-0.00=0.60; Adj Score=91.2 sampled pct | L151,L152,L153,L154,L155,L156 |
| BAC | 56.53 | 2026-06-17 | DELAYED | 58.79 | 2026-07-15 | +4.0% | 6.22% | REALIZED_VOL_30D | 0.64 | 1.10 | 0.49 | 5.0% | -6.26% | -8.80% | -8.38% | SELL_SETUP_9/SELL_SETUP_2 | 55.14 | 62.45 | RawAdjZ=(0.30*0.42+0.30*1.03+0.25*0.65+0.15*0.37)*0.90-0.00=0.58; Adj Score=88.2 sampled pct | L121,L122,L123,L124,L125,L126 |
| GE | 357.03 | 2026-06-17 | DELAYED | 371.31 | 2026-07-15 | +4.0% | 11.27% | REALIZED_VOL_30D | 0.35 | 0.56 | 0.10 | 5.0% | -14.60% | -19.22% | -13.12% | SELL_SETUP_5/SELL_SETUP_4 | 329.45 | 413.17 | RawAdjZ=(0.30*-0.08+0.30*1.28+0.25*0.53+0.15*0.96)*0.90-0.00=0.57; Adj Score=85.3 sampled pct | L157,L158,L159,L160,L161,L162 |
| GOOGL | 363.79 | 2026-06-17 | DELAYED | 374.70 | 2026-07-15 | +3.0% | 8.53% | REALIZED_VOL_30D | 0.35 | 0.55 | -0.01 | 5.0% | -11.08% | -14.58% | -11.48% | SELL_SETUP_3/BUY_SETUP_3 | 342.42 | 406.98 | RawAdjZ=(0.30*1.20+0.30*-0.11+0.25*0.53+0.15*0.93)*0.90-0.00=0.54; Adj Score=82.4 sampled pct | L043,L044,L045,L046,L047,L048 |

## Excluded Names

Monitor names are excluded from a `GO` portfolio because they fall below the investable threshold, lack sufficient family support, sit too close to an estimated earnings window, or carry high-beta/high-volatility exceptions. No sub-threshold name is admitted solely to repair portfolio beta.
