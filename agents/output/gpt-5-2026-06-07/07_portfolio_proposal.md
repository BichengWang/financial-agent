# Portfolio Proposal

**Date:** 2026-06-07  
**Proposal type:** Review-only paper monitoring sleeve  
**Publication status:** `REVIEW_ONLY`

## Construction Decision

No live portfolio is proposed. The following is a paper monitoring sleeve to track whether the regime-rotation thesis holds into CPI and FOMC. Position weights are capped at 5% and remain below a live recommendation threshold because risk analytics are not validated.

## Review-Only Weights

| Ticker | Sector / Group | Review Weight | Sizing Note |
| --- | --- | ---: | --- |
| `AZO` | Consumer Discretionary / defensive retail | 5% | Relative-strength leader; do not chase above cap. |
| `UNH` | Healthcare | 5% | Defensive rebound exposure. |
| `MCK` | Healthcare | 5% | Lower-beta healthcare distributor. |
| `JPM` | Financials | 5% | Higher-rate beneficiary. |
| `XOM` | Energy | 5% | Inflation/oil hedge. |
| `CAT` | Industrials | 5% | Cyclical relative strength. |
| `WMT` | Consumer Staples | 5% | Defensive consumer ballast. |
| `ABBV` | Healthcare | 5% | Defensive healthcare balance. |
| `GS` | Financials | 5% | Capital-markets/financials exposure. |
| `PG` | Consumer Staples | 5% | Low-beta defensive ballast. |
| Cash / unallocated | N/A | 50% | Required because this is not a live GO. |

## Portfolio Analytics

| Metric | Value | Tag | Committee View |
| --- | --- | --- | --- |
| Gross exposure | 50% | `REVIEW_ONLY` | Paper monitoring only. |
| Max single-name weight | 5% | `RULE_CHECK` | Meets hard cap. |
| Sector concentration | Healthcare 15%, Financials 10%, Staples 10%, Energy 5%, Industrials 5%, Discretionary 5% | `REVIEW_ONLY` | Under 30% cap. |
| Expected portfolio beta | `N/A - missing validated beta feed` | `N/A` | Blocks `GO`. |
| Expected portfolio Sharpe | `N/A - no validated residual risk model` | `N/A` | Blocks `GO`. |
| 95th-percentile 1M drawdown | `N/A - no validated drawdown engine` | `N/A` | Blocks `GO`. |
| Average pairwise correlation | `N/A - no validated correlation matrix` | `N/A` | Blocks `GO`. |

## Heuristic Correlation Map

This table is qualitative and not approved for live risk validation.

| Pair Group | Expected Relationship | Use |
| --- | --- | --- |
| Healthcare vs energy | Low/medium | Helps diversify macro drivers. |
| Staples vs financials | Low/medium | Defensive ballast against rate cyclicality. |
| `JPM` / `GS` | Medium/high | Limit financials to 10% total. |
| `UNH` / `MCK` / `ABBV` | Medium | Limit healthcare to 15% total. |
| `AZO` / `WMT` / `PG` | Medium | Consumer exposure split across staples and repair retail. |

## Excluded Names

`NVDA`, `AVGO`, `AMD`, `MU`, `PLTR`, `APP`, `COIN`, `HOOD`, and `CRWV` were excluded because the June 5 tape punished high-beta crowded growth. `ORCL` was excluded for June 10 earnings. `MSFT`, `GOOGL`, `GEV`, and `ANET` remain on structural watch but do not lead the current rotation sleeve.

## Portfolio Recommendation

Publish this as a review-only tracking sleeve. Do not treat it as a live executable portfolio until beta, correlation, drawdown, options, short-interest, and execution-quality liquidity inputs are wired.
