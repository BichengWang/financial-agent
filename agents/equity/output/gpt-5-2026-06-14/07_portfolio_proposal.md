# 07 Portfolio Proposal

## Constraint Feasibility Pre-Check

`NO_TRADE` recommendation before sizing. The investable set contains 8 names; at the 5% single-name cap the maximum gross exposure is 40.0% NAV and the maximum positive beta contribution is **0.384**. Required portfolio beta is 0.90-1.10, so no capped long-only combination can satisfy the protected beta band.

| Metric | Value | Limit | Result |
|---|---:|---:|---|
| Investable names | 8 | 5-10 desired | PASS |
| Maximum NAV beta at 5% cap | 0.384 | 0.90-1.10 | FAIL |
| Equal-weight sleeve beta, normalized | 0.959 | Diagnostic only | PASS if normalized, but not implementable under NAV cap |
| Average pairwise correlation | 0.253 | <0.45 | PASS |
| Parametric 95% 1m drawdown at max 5% weights | 3.83% | <=8.0% | PASS |
| Maximum sector exposure at 5% weights | 15.0% NAV | <=30.0% | PASS |

## Sector Concentration at Max 5% Weights

| Sector | Exposure |
|---|---:|
| Financials | 15.0% NAV |
| Health Care | 15.0% NAV |
| Industrials | 5.0% NAV |
| Information Technology | 5.0% NAV |

## Per-Position Recommendation Metrics

| Ticker | Entry Price | Price Date | Price Tag | Target Price | Target Date | mu | sigma | Sigma Source | 70% CI Lo | 70% CI Hi | Ledger Rows |
|---|---:|---|---|---:|---|---:|---:|---|---:|---:|---|
| LLY | 1133.00 | 2026-06-12 | DELAYED | 1200.98 | 2026-07-12 | 6.0% | 9.2% | REALIZED_VOL_30D | 1093.16 | 1308.80 | L133,L135,L224 |
| GE | 335.30 | 2026-06-12 | DELAYED | 355.42 | 2026-07-12 | 6.0% | 11.5% | REALIZED_VOL_30D | 315.46 | 395.38 | L158,L160,L225 |
| BAC | 56.02 | 2026-06-12 | DELAYED | 58.82 | 2026-07-12 | 5.0% | 6.4% | REALIZED_VOL_30D | 55.07 | 62.57 | L113,L115,L226 |
| GS | 1062.75 | 2026-06-12 | DELAYED | 1115.89 | 2026-07-12 | 5.0% | 10.4% | REALIZED_VOL_30D | 1000.61 | 1231.17 | L118,L120,L227 |
| ANET | 163.24 | 2026-06-12 | DELAYED | 169.77 | 2026-07-12 | 4.0% | 19.3% | REALIZED_VOL_30D | 137.07 | 202.47 | L043,L045,L228 |
| UNH | 408.52 | 2026-06-12 | DELAYED | 424.86 | 2026-07-12 | 4.0% | 7.5% | REALIZED_VOL_30D | 392.87 | 456.85 | L138,L140,L229 |
| ABBV | 227.73 | 2026-06-12 | DELAYED | 234.56 | 2026-07-12 | 3.0% | 6.2% | REALIZED_VOL_30D | 219.93 | 249.20 | L148,L150,L230 |
| JPM | 320.72 | 2026-06-12 | DELAYED | 330.34 | 2026-07-12 | 3.0% | 6.7% | REALIZED_VOL_30D | 308.09 | 352.59 | L108,L110,L231 |

## Excluded Names

AMD, CAT, FCX, and SOXX-linked beta could increase portfolio beta, but AMD fails the 3-of-4 factor-family threshold and CAT/FCX are below the investable percentile bar. The run cannot admit sub-threshold names solely to repair beta.
