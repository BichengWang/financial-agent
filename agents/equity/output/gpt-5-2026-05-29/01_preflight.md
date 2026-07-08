# Preflight

**Date:** 2026-05-29  
**Preflight Result:** `PASS_FOR_REVIEW_ONLY`  
**Recommended Status:** `REVIEW_ONLY`

## Data Coverage Summary

| Data Class | Coverage | Freshness | Lineage | Decision |
| --- | --- | --- | --- | --- |
| Benchmark quotes | `SPY`, `QQQ`, `IWM`, `DIA` | 2026-05-29 delayed public snapshot | Stooq | Usable for review |
| Candidate quotes | 28 sampled liquid U.S.-listed names | 2026-05-29 delayed public snapshot | Stooq | Usable for review |
| Volatility regime | `VIX` close 15.32 on 2026-05-29 | Same day | Cboe CSV | Usable |
| Rates | 10Y Treasury 4.45% on 2026-05-28; 2Y 3.99% on 2026-05-28 | One business day stale | FRED | Usable |
| Credit | ICE BofA corporate OAS 0.73 on 2026-05-28 | One business day stale | FRED | Usable |
| Company catalysts | Official or indexed releases for main candidates | March-May 2026 | Company / SEC / indexed release pages | Usable |
| Beta / covariance / drawdown | Not wired | N/A | N/A | Blocks `GO` |
| Options IV / skew | Not wired | N/A | N/A | Blocks high conviction |

## Validation Summary

The preflight confirms enough evidence to run the research loop and produce a concrete monitoring list. It does not confirm enough execution-grade data for live position sizing.

Key validation points:

1. Public quote snapshots returned current prices and volume for the sampled universe.
2. Cboe and FRED macro inputs are internally consistent with a lower-volatility, constructive tape.
3. The next FOMC meeting is June 16-17, 2026, outside the immediate 14-day candidate event window.
4. `AVGO` has a near-term June 3, 2026 earnings event and must be penalized.

## Stop-Criteria Check

| Criterion | Result | Action |
| --- | --- | --- |
| Benchmark data missing | No; public quote data available | Continue |
| Data lineage unclear | No for quotes/macro; yes for risk model | Downgrade to `REVIEW_ONLY` |
| >20% top candidates missing critical inputs | Yes for risk-model fields | Withhold `GO` |
| Universe too small | Sampled, not full universe | Continue as review-only |
| Portfolio constraints verifiable | No | No live portfolio |

## Handoff

Proceed to regime classification and factor scoring, but all tables must be read as delayed-data research output. The run is not eligible for `GO` until beta, correlation, drawdown, and event-risk data are sourced.

