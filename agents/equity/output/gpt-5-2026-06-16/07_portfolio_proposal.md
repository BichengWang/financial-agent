# 07 Portfolio Proposal

## Constraint Feasibility Pre-Check

Portfolio status: `NO_TRADE`.

The investable-grade set contains 6 names. At the protected 5% single-name NAV cap, max gross exposure is 30.0% and max achievable NAV beta is **0.370**, below the required 0.90-1.10 band. Per the 2026-06-10 Track B instruction, construction stops before drafting weights.

| Metric | Value | Limit | Result |
|---|---|---|---|
| Investable names | 6 | >= 5 | PASS |
| Max gross at 5% cap | 30.0% | no explicit minimum | Informational |
| Max NAV beta at cap | 0.370 | 0.90-1.10 | FAIL |
| Avg pairwise corr at cap | 0.339 | < 0.45 | PASS |
| 95th-pctl 1m drawdown at cap | 3.66% | <= 8.00% | PASS |

## Sector Concentration at Cap

| Sector | Max NAV Share at 5% Cap |
|---|---|
| Communication Services | 5.0% |
| Financials | 5.0% |
| Health Care | 10.0% |
| Industrials | 10.0% |

## Correlation Matrix

| Ticker | GOOGL | CAT | LLY | UNH | GE | GS |
|---|---|---|---|---|---|---|
| GOOGL | 1.00 | 0.48 | 0.53 | 0.20 | 0.49 | 0.44 |
| CAT | 0.48 | 1.00 | 0.46 | 0.03 | 0.55 | 0.61 |
| LLY | 0.53 | 0.46 | 1.00 | 0.12 | 0.33 | 0.31 |
| UNH | 0.20 | 0.03 | 0.12 | 1.00 | -0.08 | 0.03 |
| GE | 0.49 | 0.55 | 0.33 | -0.08 | 1.00 | 0.57 |
| GS | 0.44 | 0.61 | 0.31 | 0.03 | 0.57 | 1.00 |

## Per-Position Recommendation Metrics

| Ticker | Entry Price | Price Date | Price Tag | Target Price | Target Date | mu | sigma | Sigma Source | Sharpe | Sortino | IR | Kelly 0.25 | VaR95 | CVaR95 | Max DD60 | TD9 D/W | 70% CI Lo | 70% CI Hi | Score Trace | Ledger Rows |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| GOOGL | 374.82 | 2026-06-16 | DELAYED | 397.31 | 2026-07-14 | +6.0% | 8.3% | REALIZED_VOL_30D | 0.72 | 1.12 | 0.33 | 5.0% | -7.8% | -11.2% | -11.5% | SELL_SETUP_1/BUY_SETUP_4 | 364.82 | 429.81 | RawAdjZ=(0.30*3.02+0.30*0.04+0.25*1.66+0.15*0.58)*0.90-0.00=1.28; Adj Score=100.0 sampled pct | L043,L044,L045,L046,L047,L048 |
| CAT | 952.35 | 2026-06-16 | DELAYED | 1009.49 | 2026-07-14 | +6.0% | 12.5% | REALIZED_VOL_30D | 0.48 | 0.87 | 0.20 | 5.0% | -14.6% | -19.7% | -9.0% | SELL_SETUP_1/SELL_SETUP_3 | 885.81 | 1133.17 | RawAdjZ=(0.30*0.67+0.30*1.14+0.25*0.76+0.15*0.68)*0.90-0.00=0.75; Adj Score=97.1 sampled pct | L151,L152,L153,L154,L155,L156 |
| LLY | 1124.32 | 2026-06-16 | DELAYED | 1180.53 | 2026-07-14 | +5.0% | 9.0% | REALIZED_VOL_30D | 0.56 | 1.21 | 0.35 | 5.0% | -9.8% | -13.4% | -10.9% | BUY_SETUP_2/SELL_SETUP_9 | 1075.84 | 1285.22 | RawAdjZ=(0.30*0.72+0.30*1.10+0.25*1.05+0.15*0.03)*0.90-0.00=0.73; Adj Score=94.1 sampled pct | L133,L134,L135,L136,L137,L138 |
| UNH | 408.65 | 2026-06-16 | DELAYED | 429.08 | 2026-07-14 | +5.0% | 7.5% | REALIZED_VOL_30D | 0.67 | 1.25 | 0.47 | 5.0% | -7.4% | -10.5% | -6.1% | BUY_SETUP_1/SELL_SETUP_9 | 397.20 | 460.96 | RawAdjZ=(0.30*0.18+0.30*1.94+0.25*0.74+0.15*-0.23)*0.90-0.00=0.71; Adj Score=91.2 sampled pct | L139,L140,L141,L142,L143,L144 |
| GE | 348.80 | 2026-06-16 | DELAYED | 362.75 | 2026-07-14 | +4.0% | 11.4% | REALIZED_VOL_30D | 0.35 | 0.57 | 0.05 | 5.0% | -14.9% | -19.6% | -13.1% | SELL_SETUP_3/SELL_SETUP_5 | 321.27 | 404.23 | RawAdjZ=(0.30*0.24+0.30*0.94+0.25*0.97+0.15*0.57)*0.90-0.00=0.61; Adj Score=88.2 sampled pct | L157,L158,L159,L160,L161,L162 |
| GS | 1093.58 | 2026-06-16 | DELAYED | 1126.39 | 2026-07-14 | +3.0% | 10.4% | REALIZED_VOL_30D | 0.29 | 0.56 | -0.08 | 5.0% | -14.1% | -18.4% | -8.4% | SELL_SETUP_2/SELL_SETUP_9 | 1008.36 | 1244.42 | RawAdjZ=(0.30*-0.09+0.30*1.36+0.25*0.53+0.15*0.57)*0.90-0.00=0.54; Adj Score=82.4 sampled pct | L127,L128,L129,L130,L131,L132 |

## Excluded Names

Monitor names are excluded from a `GO` portfolio because they fall below the investable threshold, lack sufficient family support, sit too close to an estimated earnings window, or carry high-beta/high-volatility exceptions.
