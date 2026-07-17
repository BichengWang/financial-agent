# Portfolio Proposal — NO_TRADE

## Constraint Feasibility Pre-Check

The evidence threshold produces zero investable names before sizing. In addition, six monitor names have literal earnings dates inside 14 calendar days, and the required +/-5-day buffer for estimated dates raises the event-window count to nine, above the permitted limit of two (L213,L222,L240,L249,L267,L276,L285,L312,L321). A protected-constraint portfolio cannot be formed from a zero-name investable set, so the workflow stops without consuming the revision pass. No weights, covariance matrix, or portfolio risk statistics are fabricated.

## Proposed Weights

| Ticker | Weight | Reason |
| --- | --- | --- |
| N/A | 0.00% | No investable names |

## Portfolio Analytics

| Metric | Value | Reason |
| --- | --- | --- |
| Expected Sharpe | NOT APPLICABLE | No portfolio |
| Expected Sortino | NOT APPLICABLE | No portfolio |
| Information Ratio | NOT APPLICABLE | No portfolio |
| Tracking Error | NOT APPLICABLE | No portfolio |
| Beta | NOT APPLICABLE | No portfolio |
| VaR95 / CVaR95 | NOT APPLICABLE | No portfolio |
| 95th-pctl one-month drawdown | NOT APPLICABLE | No portfolio |
| Average pairwise correlation | NOT APPLICABLE | No portfolio |

## Sector and Factor Exposure

| Exposure | Value | Reason |
| --- | --- | --- |
| Sector concentration | NOT APPLICABLE | No positions |
| Factor crowding | NOT APPLICABLE | No positions; monitor scores are Technical-only |

## Correlation Matrix

`NOT APPLICABLE — no investable names and no proposed weights.` Individual completed histories are retained for forecast settlement and diagnostics; they are not assembled into a fictitious portfolio.

## Excluded-Name Rationale

| Ticker | Adj Score | Reason |
| --- | --- | --- |
| CRWD | 0.363 | Fails 3-of-4, completeness, and factor-concentration gates |
| PANW | 0.295 | Fails 3-of-4, completeness, and factor-concentration gates |
| DDOG | 0.281 | Fails 3-of-4, completeness, and factor-concentration gates |
| MNST | 0.274 | Fails 3-of-4, completeness, and factor-concentration gates |
| BBY | 0.247 | Fails 3-of-4, completeness, and factor-concentration gates |
| BAC | 0.236 | Fails 3-of-4, completeness, and factor-concentration gates |
| MPC | 0.215 | Fails 3-of-4, completeness, and factor-concentration gates |
| PSX | 0.207 | Fails 3-of-4, completeness, and factor-concentration gates |
| GEN | 0.203 | Fails 3-of-4, completeness, and factor-concentration gates |
| UNP | 0.201 | Fails 3-of-4, completeness, and factor-concentration gates |
| INCY | 0.194 | Fails 3-of-4, completeness, and factor-concentration gates |
| NTAP | 0.191 | Fails 3-of-4, completeness, and factor-concentration gates |
| AAPL | 0.185 | Fails 3-of-4, completeness, and factor-concentration gates |
| DOC | 0.178 | Fails 3-of-4, completeness, and factor-concentration gates |
| VLO | 0.175 | Fails 3-of-4, completeness, and factor-concentration gates |
| DG | 0.172 | Fails 3-of-4, completeness, and factor-concentration gates |
| HPQ | 0.167 | Fails 3-of-4, completeness, and factor-concentration gates |
| CHRW | 0.167 | Fails 3-of-4, completeness, and factor-concentration gates |
| IQV | 0.157 | Fails 3-of-4, completeness, and factor-concentration gates |
| VEEV | 0.156 | Fails 3-of-4, completeness, and factor-concentration gates |

The 5% single-name, 30% sector, 0.90–1.10 beta, 0.45 correlation, and 8% drawdown limits remain unchanged; none was weakened to force a proposal.
