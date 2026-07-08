# Portfolio Proposal

**Date:** 2026-05-29  
**Status:** `REVIEW_ONLY`  
**Decision:** No executable live portfolio approved

## Portfolio Construction Conclusion

The factor stack identifies a credible monitoring basket, but the construction agent cannot approve a live portfolio without validated beta, covariance, and drawdown inputs. The correct output is a capped review-only sleeve for human inspection.

## Review-Only Monitoring Sleeve

This sleeve respects the 5% single-name cap on paper, but it is not a live allocation recommendation.

| Ticker | Role | Review Weight | Confidence | Notes |
| --- | --- | ---: | --- | --- |
| `NVDA` | AI compute leader | 5% | `MEDIUM` | Strongest current evidence |
| `MSFT` | AI/cloud platform quality | 5% | `MEDIUM` | Quality anchor |
| `GEV` | Power/electrification | 5% | `MEDIUM` | Diversifies away from pure software/chips |
| `PLTR` | Applied AI software | 5% | `MEDIUM` | High momentum, high valuation |
| `ANET` | AI networking | 5% | `MEDIUM` | Infrastructure adjacency |
| `GOOGL` | Cloud/search AI platform | 5% | `MEDIUM` | Platform diversification |
| Cash / unallocated | Risk reserve | 70% | N/A | Required because this is review-only |

## Required Portfolio Analytics

| Metric | Result | Status |
| --- | --- | --- |
| Expected portfolio Sharpe | `N/A - missing risk feed` | Blocks `GO` |
| Expected portfolio beta | `N/A - missing beta engine` | Blocks `GO` |
| 95th-percentile 1-month drawdown | `N/A - missing drawdown model` | Blocks `GO` |
| Avg pairwise correlation | `N/A - missing covariance model` | Blocks `GO` |
| Max single-name weight | 5% | Pass on review sleeve |
| Max sector concentration | Information Technology 20% of gross capital | Pass on review sleeve, but AI-factor crowding remains |
| Earnings inside 14 days | None in the sleeve | `AVGO` excluded for this reason |

## Sector Concentration Table

| Sector / Exposure | Names | Gross Weight |
| --- | --- | ---: |
| Information Technology | `NVDA`, `MSFT`, `PLTR`, `ANET` | 20% |
| Industrials / Power | `GEV` | 5% |
| Communication Services | `GOOGL` | 5% |
| Cash / unallocated | N/A | 70% |

## Factor Exposure Summary

| Factor | Exposure | Risk Note |
| --- | --- | --- |
| AI infrastructure | High | Main crowding risk |
| AI platform/cloud monetization | High | Capex ROI debate can hit several names at once |
| Power/electrification | Moderate | Diversifying but still tied to AI data-center demand |
| Financials/value | Low | No current allocation |
| Healthcare/defensive | Low | No current allocation |

## Correlation Matrix

Validated pairwise correlations are unavailable. Qualitative cluster risk is high among `NVDA`, `AVGO`, `ANET`, `MSFT`, `GOOGL`, and `AMZN` because they all depend on continued AI infrastructure spending.

## Excluded Names

| Ticker | Reason Left Out |
| --- | --- |
| `ORCL` | Expected early-June earnings event and leverage/capex scrutiny. |
| `AVGO` | June 3 earnings event inside 14 days, despite strong MoM validation. |
| `AMZN` | Strong AWS evidence but below sample-relative 80th-percentile threshold. |
| `CRM` | Current move may be short-lived post-earnings repricing. |
| `META` | Negative MoM return versus prior run. |
| `ETN` | Secondary to `GEV` for current power/electrification expression. |
| `AMD` | Cleaner AI compute exposure available through `NVDA`. |
