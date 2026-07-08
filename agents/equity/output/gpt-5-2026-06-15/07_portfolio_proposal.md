# 07 Portfolio Proposal

## Constraint Feasibility Pre-Check

Portfolio status: `NO_TRADE`.

The investable-grade set contains 7 names. At the protected 5% single-name NAV cap, max gross exposure is 35.0% and max achievable NAV beta is **0.459**, below the required 0.90-1.10 band. Per the 2026-06-10 Track B instruction, construction stops before drafting weights.

| Metric | Value | Limit | Result |
|---|---:|---:|---|
| Investable names | 7 | >= 5 | PASS |
| Max gross at 5% cap | 35.0% | no explicit minimum | Informational |
| Max NAV beta at cap | 0.459 | 0.90-1.10 | FAIL |
| Avg pairwise corr at cap | 0.315 | < 0.45 | PASS |
| 95th-pctl 1m drawdown at cap | 4.22% | <= 8.00% | PASS |

## Sector Concentration at Cap

| Sector | Max NAV Share at 5% Cap |
|---|---:|
| Financials | 10.0% |
| Health Care | 10.0% |
| Industrials | 10.0% |
| Materials | 5.0% |

## Per-Position Recommendation Metrics

| Ticker | Entry Price | Price Date | Price Tag | Target Price | Target Date | mu | sigma | Sigma Source | 70% CI Lo | 70% CI Hi | Ledger Rows |
|---|---:|---|---|---:|---|---:|---:|---|---:|---:|---|
| CAT | 936.27 | 2026-06-15 | DELAYED | 992.45 | 2026-07-13 | +6.0% | 12.5% | REALIZED_VOL_30D | 870.50 | 1114.40 | L153,L154,L155,L156,L157 |
| GE | 344.38 | 2026-06-15 | DELAYED | 361.60 | 2026-07-13 | +5.0% | 11.5% | REALIZED_VOL_30D | 320.40 | 402.80 | L158,L159,L160,L161,L162 |
| FCX | 70.13 | 2026-06-15 | DELAYED | 73.64 | 2026-07-13 | +5.0% | 16.5% | REALIZED_VOL_30D | 61.63 | 85.64 | L183,L184,L185,L186,L187 |
| LLY | 1129.51 | 2026-06-15 | DELAYED | 1174.69 | 2026-07-13 | +4.0% | 9.0% | REALIZED_VOL_30D | 1069.53 | 1279.85 | L133,L134,L135,L136,L137 |
| UNH | 413.07 | 2026-06-15 | DELAYED | 429.60 | 2026-07-13 | +4.0% | 7.5% | REALIZED_VOL_30D | 397.27 | 461.92 | L138,L139,L140,L141,L142 |
| BAC | 56.03 | 2026-06-15 | DELAYED | 57.71 | 2026-07-13 | +3.0% | 6.5% | REALIZED_VOL_30D | 53.95 | 61.47 | L113,L114,L115,L116,L117 |
| GS | 1079.29 | 2026-06-15 | DELAYED | 1111.67 | 2026-07-13 | +3.0% | 10.4% | REALIZED_VOL_30D | 994.98 | 1228.36 | L118,L119,L120,L121,L122 |

## Excluded Names

Monitor names are excluded from a `GO` portfolio because they fall below the investable threshold, lack sufficient family support, or carry high-beta/high-volatility exceptions. Admitting them solely to repair beta would violate the scoring and risk rules.
