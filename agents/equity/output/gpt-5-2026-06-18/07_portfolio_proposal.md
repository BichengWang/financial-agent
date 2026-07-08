# 07 Portfolio Proposal

## Constraint Feasibility Pre-Check

Portfolio status: `NO_TRADE`.

The investable-grade set contains 7 names. At the protected 5% single-name NAV cap, max gross exposure is 35.00% and max achievable NAV beta is **0.494**, compared with the required 0.90-1.10 band. Per the 2026-06-10 Track B instruction, construction stops before drafting executable weights when feasibility fails.

| Metric | Value | Limit | Result |
| --- | --- | --- | --- |
| Investable names | 7 | >= 5 | PASS |
| Max gross at 5% cap | 35.00% | no explicit minimum | Informational |
| Max NAV beta at cap | 0.494 | 0.90-1.10 | FAIL |
| Avg pairwise corr at cap | 0.335 | < 0.45 | PASS |
| 95th-pctl 1m drawdown at cap | 4.47% | <= 8.00% | PASS |

## Sector Concentration at Cap

| Sector | Max NAV Share at 5% Cap |
| --- | --- |
| Communication Services | 5.00% |
| Financials | 5.00% |
| Health Care | 10.00% |
| Industrials | 10.00% |
| Materials | 5.00% |

## Correlation Matrix

| Ticker | CAT | GOOGL | GS | GE | LLY | FCX | UNH |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CAT | 1.00 | 0.51 | 0.60 | 0.54 | 0.45 | 0.51 | 0.03 |
| GOOGL | 0.51 | 1.00 | 0.45 | 0.48 | 0.52 | 0.30 | 0.22 |
| GS | 0.60 | 0.45 | 1.00 | 0.58 | 0.31 | 0.63 | 0.05 |
| GE | 0.54 | 0.48 | 0.58 | 1.00 | 0.31 | 0.38 | -0.11 |
| LLY | 0.45 | 0.52 | 0.31 | 0.31 | 1.00 | 0.23 | 0.13 |
| FCX | 0.51 | 0.30 | 0.63 | 0.38 | 0.23 | 1.00 | -0.06 |
| UNH | 0.03 | 0.22 | 0.05 | -0.11 | 0.13 | -0.06 | 1.00 |

## Per-Position Recommendation Metrics

| Ticker | Entry Price | Price Date | Price Tag | Target Price | Target Date | mu | sigma | Sigma Source | Sharpe | Sortino | IR | Kelly 0.25 | VaR95 | CVaR95 | Max DD60 | TD9 D/W | 70% CI Lo | 70% CI Hi | Score Trace | Ledger Rows |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CAT | 988.58 | 2026-06-18 | LIVE | 1047.89 | 2026-07-16 | +6.0% | 12.29% | REALIZED_VOL_30D | 0.49 | 0.86 | 0.24 | 5.00% | -14.27% | -19.31% | -8.97% | SELL_SETUP_4/SELL_SETUP_3 | 921.58 | 1174.21 | RawAdjZ=(0.30*0.81+0.30*1.44+0.25*0.95+0.15*1.09)*0.90-0.00=0.97; Adj Score=100.0 sampled pct | L139,L140,L141,L142,L143,L144 |
| GOOGL | 367.90 | 2026-06-18 | LIVE | 389.97 | 2026-07-16 | +6.0% | 8.30% | REALIZED_VOL_30D | 0.72 | 1.18 | 0.37 | 5.00% | -7.69% | -11.09% | -11.48% | SELL_SETUP_4/BUY_SETUP_4 | 358.23 | 421.72 | RawAdjZ=(0.30*2.34+0.30*0.13+0.25*0.84+0.15*0.12)*0.90-0.00=0.87; Adj Score=97.1 sampled pct | L043,L044,L045,L046,L047,L048 |
| GS | 1102.11 | 2026-06-18 | LIVE | 1157.21 | 2026-07-16 | +5.0% | 10.01% | REALIZED_VOL_30D | 0.50 | 0.93 | 0.30 | 5.00% | -11.52% | -15.62% | -8.36% | SELL_SETUP_5/SELL_SETUP_9 | 1042.49 | 1271.93 | RawAdjZ=(0.30*0.19+0.30*1.24+0.25*1.18+0.15*0.73)*0.90-0.00=0.75; Adj Score=94.1 sampled pct | L109,L110,L111,L112,L113,L114 |
| GE | 359.12 | 2026-06-18 | LIVE | 377.07 | 2026-07-16 | +5.0% | 10.04% | REALIZED_VOL_30D | 0.50 | 0.71 | 0.20 | 5.00% | -11.57% | -15.69% | -13.12% | SELL_SETUP_6/SELL_SETUP_5 | 339.56 | 414.58 | RawAdjZ=(0.30*0.46+0.30*1.23+0.25*0.32+0.15*1.03)*0.90-0.00=0.67; Adj Score=91.2 sampled pct | L145,L146,L147,L148,L149,L150 |
| LLY | 1102.12 | 2026-06-18 | LIVE | 1146.20 | 2026-07-16 | +4.0% | 9.02% | REALIZED_VOL_30D | 0.44 | 0.97 | 0.26 | 5.00% | -10.88% | -14.58% | -10.89% | BUY_SETUP_5/SELL_SETUP_9 | 1042.81 | 1249.59 | RawAdjZ=(0.30*0.75+0.30*0.82+0.25*0.66+0.15*0.64)*0.90-0.00=0.66; Adj Score=88.2 sampled pct | L121,L122,L123,L124,L125,L126 |
| FCX | 68.59 | 2026-06-18 | LIVE | 71.33 | 2026-07-16 | +4.0% | 15.71% | REALIZED_VOL_30D | 0.25 | 0.32 | -0.10 | 5.00% | -21.92% | -28.37% | -21.02% | SELL_SETUP_6/SELL_SETUP_5 | 60.13 | 82.54 | RawAdjZ=(0.30*0.39+0.30*1.19+0.25*0.48+0.15*0.40)*0.90-0.00=0.59; Adj Score=85.3 sampled pct | L169,L170,L171,L172,L173,L174 |
| UNH | 402.22 | 2026-06-18 | LIVE | 414.29 | 2026-07-16 | +3.0% | 7.58% | REALIZED_VOL_30D | 0.40 | 0.77 | 0.25 | 5.00% | -9.51% | -12.62% | -6.06% | BUY_SETUP_2/SELL_SETUP_9 | 382.57 | 446.01 | RawAdjZ=(0.30*0.61+0.30*0.88+0.25*0.09+0.15*0.56)*0.90-0.00=0.50; Adj Score=82.4 sampled pct | L127,L128,L129,L130,L131,L132 |

## Excluded Names

Monitor names are excluded from a `GO` portfolio because they fall below the investable threshold, lack sufficient family support, or carry high-beta/high-volatility exceptions. No sub-threshold name is admitted solely to repair portfolio beta.
