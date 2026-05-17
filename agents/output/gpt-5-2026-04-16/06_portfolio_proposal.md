# Portfolio Proposal

**Date:** 2026-04-16
**Status:** `REVIEW_ONLY`
**Decision:** No executable live portfolio approved

## Why No Live Portfolio

The portfolio-construction prompt requires:

- portfolio beta inside `0.90-1.10`,
- average pairwise correlation below `0.45`,
- 95th-percentile 1-month drawdown at or below `8%`,
- auditable earnings-risk fields across the final basket.

Those inputs are not fully available in-source for this run, and the top-ranked basket also clusters three names inside the April 29 earnings window.

## Paper-Trade Monitor Basket

This is a monitoring basket only. It is not a live sizing recommendation.

| Ticker | Role | Monitor Weight |
| --- | --- | ---: |
| `AVGO` | Custom silicon / AI networking leader | 22% |
| `META` | AI monetization plus infrastructure demand | 20% |
| `NVDA` | AI compute leader | 20% |
| `GEV` | Power and electrification beneficiary | 19% |
| `MSFT` | AI/cloud platform quality anchor | 19% |

## Constraint Check On Paper Basket

| Constraint | Result | Status |
| --- | --- | --- |
| Max single-name weight 5% | Violated intentionally in paper basket | `N/A - not live` |
| Max 30% per sector | Tech / comms concentration would exceed a live tolerance | `N/A - not live` |
| Beta / correlation / drawdown | Not calculated from validated risk feed | `N/A - missing input` |
| Event concentration <= 2 names inside 14 days | Fails with `META`, `GEV`, `MSFT` | `FAIL` |

## Construction Conclusion

The construction stage cannot approve a live book without inventing risk numbers or ignoring event concentration. Under the prompt rules, the only defensible publication is `REVIEW_ONLY`.
