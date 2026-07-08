# 07 Portfolio Proposal

## Portfolio Decision

No live portfolio is proposed. The candidate set is `REVIEW_ONLY` because the run lacks IV/skew, complete short-interest/borrow, execution-quality liquidity, and covariance/drawdown inputs.

## Paper Monitoring Sleeve

This sleeve is for process tracking only. It is not an investable allocation and is not eligible for `GO`.

| Ticker | Paper Weight | Entry Price | Price Date | Price Tag | Beta | Source / Ledger Rows |
|---|---:|---:|---|---|---:|---|
| MCK | 5% | 783.75 | 2026-06-09 | DELAYED | 0.32 | L030-L034 |
| PG | 5% | 148.30 | 2026-06-09 | DELAYED | 0.38 | L035-L039 |
| WMT | 5% | 118.61 | 2026-06-09 | DELAYED | 0.60 | L040-L044 |
| ABBV | 5% | 226.43 | 2026-06-09 | DELAYED | 0.31 | L045-L049 |
| JPM | 5% | 312.82 | 2026-06-09 | DELAYED | 1.00 | L050-L054 |
| XOM | 5% | 148.73 | 2026-06-09 | DELAYED | 0.15 | L055-L059 |
| AZO | 5% | 3125.82 | 2026-06-09 | DELAYED | 0.35 | L060-L064 |
| UNH | 5% | 412.50 | 2026-06-09 | DELAYED | 0.65 | L065-L069 |
| Cash | 60% | N/A | N/A | N/A | 0.00 | N/A |

## Portfolio Analytics

| Metric | Value | Source / Reason |
|---|---|---|
| Expected portfolio Sharpe | UNAVAILABLE | No validated sigma, covariance, or expected-return model. |
| Expected portfolio beta | 0.19 including cash; 0.47 gross-normalized | Derived from sampled beta rows only; not sufficient for `GO`. |
| 95th percentile 1-month drawdown | UNAVAILABLE | L093 unavailable. |
| Average pairwise correlation | UNAVAILABLE | L093 unavailable. |
| Portfolio gross exposure | 40% | Paper monitoring sleeve only. |

## Sector Concentration

| Sector | Paper Weight | Names | Constraint Status |
|---|---:|---|---|
| Healthcare | 15% | MCK, ABBV, UNH | Under 30% cap. |
| Consumer Staples | 10% | PG, WMT | Under 30% cap. |
| Financials | 5% | JPM | Under 30% cap. |
| Energy | 5% | XOM | Under 30% cap. |
| Consumer Discretionary | 5% | AZO | Under 30% cap. |
| Cash | 60% | Cash | Not a sector exposure. |

## Correlation Matrix

Unavailable. The run lacks validated return-series and covariance feed coverage (L093).

## Per-Position Recommendation Metrics Table

| Ticker | Entry Price | Price Date | Price Tag | Target Price | Target Date | mu | sigma | Sigma Source | 70% CI Lo | 70% CI Hi | Source / Ledger Rows |
|---|---:|---|---|---|---|---|---|---|---|---|---|
| MCK | 783.75 | 2026-06-09 | DELAYED | N/A | N/A | N/A | UNAVAILABLE | UNAVAILABLE | N/A | N/A | L030-L034, L090-L093, L100 |
| PG | 148.30 | 2026-06-09 | DELAYED | N/A | N/A | N/A | UNAVAILABLE | UNAVAILABLE | N/A | N/A | L035-L039, L090-L093, L101 |
| WMT | 118.61 | 2026-06-09 | DELAYED | N/A | N/A | N/A | UNAVAILABLE | UNAVAILABLE | N/A | N/A | L040-L044, L090-L093, L102 |
| ABBV | 226.43 | 2026-06-09 | DELAYED | N/A | N/A | N/A | UNAVAILABLE | UNAVAILABLE | N/A | N/A | L045-L049, L090-L093, L103 |
| JPM | 312.82 | 2026-06-09 | DELAYED | N/A | N/A | N/A | UNAVAILABLE | UNAVAILABLE | N/A | N/A | L050-L054, L090-L093, L104 |
| XOM | 148.73 | 2026-06-09 | DELAYED | N/A | N/A | N/A | UNAVAILABLE | UNAVAILABLE | N/A | N/A | L055-L059, L090-L093, L105 |
| AZO | 3125.82 | 2026-06-09 | DELAYED | N/A | N/A | N/A | UNAVAILABLE | UNAVAILABLE | N/A | N/A | L060-L064, L090-L093, L106 |
| UNH | 412.50 | 2026-06-09 | DELAYED | N/A | N/A | N/A | UNAVAILABLE | UNAVAILABLE | N/A | N/A | L065-L069, L090-L093, L107 |

## Excluded Names

CAT and GS were excluded from the paper sleeve because their higher beta would only mask the absence of a real covariance/drawdown model. MSFT, NVDA, META, GOOGL, and AMZN were excluded by reflection carry-forward decisions.
