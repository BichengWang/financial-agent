# Risk Review

**Date:** 2026-05-29  
**Committee Decision:** `REJECT_FOR_GO / APPROVE_FOR_REVIEW_ONLY`  
**Final Publication Recommendation:** `REVIEW_ONLY`

## Top Concerns

1. **Missing risk engine blocks live sizing.** Portfolio beta, pairwise correlation, tracking error, and 95th-percentile drawdown are all `N/A`; approving a live basket would require fabricated risk metrics.
2. **AI factor crowding is high.** The selected names span chips, networking, cloud, and power, but most still depend on the same AI capex cycle.
3. **Near-term event risk is controlled only by exclusion.** `AVGO` reports on June 3, 2026 and is excluded from the review sleeve; `ORCL` is also kept out because its likely earnings window falls inside the near-term risk window.

## Rule Check

| Rule | Result | Committee View |
| --- | --- | --- |
| No fabricated data | Pass | Missing fields are labeled `N/A`. |
| Full-universe percentile validation | Fail | Sample-relative only. |
| Max single-name 5% | Pass in review sleeve | Not enough for live approval. |
| Max sector 30% | Pass in review sleeve | Factor crowding still high. |
| Beta 0.90-1.10 | Unknown | Blocks `GO`. |
| Avg pairwise correlation <0.45 | Unknown | Blocks `GO`. |
| 95th-percentile drawdown <=8% | Unknown | Blocks `GO`. |
| Event risk <=2 names inside 14 days | Pass after excluding `AVGO` and `ORCL` | Monitor only. |

## Required Fixes Before Any Future `GO`

1. Wire a validated beta/correlation/drawdown data source.
2. Run a full eligible U.S. universe screen rather than a hand-sampled large-cap set.
3. Add event-risk handling for names inside 14 calendar days of earnings.
4. Add options IV/skew and short-interest data, or explicitly keep confidence capped.

## Final Decision

Publish the full package as `REVIEW_ONLY`. The research is useful for watchlist management, but it is not suitable as a live trade recommendation.
