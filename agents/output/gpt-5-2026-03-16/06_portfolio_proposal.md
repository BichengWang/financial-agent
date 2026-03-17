# Portfolio Proposal

**Date:** 2026-03-16
**Status:** `REVIEW_ONLY`
**Decision:** No executable live portfolio approved

## Why No Live Portfolio

The portfolio construction prompt requires:

- portfolio beta inside `0.90-1.10`,
- average pairwise correlation below `0.45`,
- 95th percentile 1-month drawdown at or below `8%`,
- auditable volatility and earnings-risk fields.

Those inputs are not fully available in-source for this run.

## Paper-Trade Monitor Basket

This is a monitoring basket only. It is not a live sizing recommendation.

| Ticker | Role | Monitor Weight |
| --- | --- | ---: |
| `GEV` | Electrification / industrial power leader | 18% |
| `ETN` | Data-center electrical / backlog industrial | 17% |
| `GE` | Aerospace and industrial breadth diversifier | 15% |
| `META` | AI platform monetization leader | 15% |
| `CRM` | Enterprise AI software monitor | 12% |
| `NVDA` | AI compute leader | 12% |
| `AVGO` | AI connectivity and custom silicon leader | 11% |

## Constraint Check On Paper Basket

| Constraint | Result | Status |
| --- | --- | --- |
| Max single-name weight 5% | Violated intentionally in paper basket | `N/A - not live` |
| Max 30% per sector | Semis at 23%, industrials at 50% if `GEV`/`ETN`/`GE` grouped | `N/A - not live` |
| Beta / drawdown / correlation | Not calculated from validated risk feed | `N/A - missing input` |

## Construction Conclusion

The construction stage cannot approve a live book without inventing risk numbers. Under the prompt rules, that means the only defensible publication is `REVIEW_ONLY`.
