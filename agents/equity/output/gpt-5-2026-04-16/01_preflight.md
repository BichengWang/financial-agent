# Preflight

**Date:** 2026-04-16
**Run Status:** `DATA_OK`
**Publication Constraint:** `REVIEW_ONLY`

## Coverage Summary

| Data Class | Status | Tag | Notes |
| --- | --- | --- | --- |
| `SPY` / `QQQ` benchmark pages | Available | `LIVE` | Public quote pages captured on or near April 16, 2026 |
| Sampled single-name prices | Available for top names | `LIVE` | `AVGO`, `NVDA`, `META`, `MSFT`, `GEV` sourced from recent public quote pages |
| Official earnings / IR pages | Partial | `DELAYED` | Confirmed for `JPM`, `BAC`, `GEV`; estimated on quote pages for some tech names |
| Recent earnings and company updates | Available | `DELAYED` | Official press releases for `NVDA`, `MSFT`, `GEV`; public-market coverage for `AVGO` and `META` |
| Full eligible universe screen | Missing | `N/A` | No full cross-sectional U.S. screen performed |
| Name-level beta / correlation / drawdown feed | Missing | `N/A` | No validated portfolio-risk dataset in workspace |
| 20-day ADV calculations for the full universe | Missing | `N/A` | Only sampled liquidity checks were feasible |

## Benchmark Snapshot

| Ticker | Price | Day Change | Tag | Timestamp Context |
| --- | ---: | --- | --- | --- |
| `SPY` | 659.22 | +0.04% close / +2.65% pre-market | `LIVE` | Yahoo Finance page, April 7 close and April 8 pre-market view |
| `QQQ` | 610.19 | +0.68% close / +0.17% overnight | `LIVE` | Yahoo Finance page, April 9 close and overnight view |
| `NVDA` | 177.89 | +2.87% | `LIVE` | Yahoo Finance page, 11:17:58 AM EDT on April 16 |
| `AVGO` | 396.72 | +4.20% | `LIVE` | Yahoo Finance page, close snapshot carried on April 16 crawl |
| `META` | 671.58 | +1.37% | `LIVE` | Yahoo Finance page, prior close carried on April 16 crawl |

## Validation Result

- Data lineage is strong enough to rank a sampled watchlist and articulate a 2-6 week thesis set.
- Data lineage is not strong enough to approve live position sizing under the prompt's portfolio-control rules.
- No fabricated fields were inserted; portfolio-risk metrics remain explicitly marked illustrative or missing.

## Preflight Decision

Proceed to ranking, but lock the run to `REVIEW_ONLY` because the sampled universe, mixed quote timestamps, and missing risk feed are all disqualifying for live deployment.

## Source Notes

- [SPY quote page](https://finance.yahoo.com/quote/SPY/)
- [QQQ quote page](https://finance.yahoo.com/quote/QQQ/)
- [NVIDIA quote page](https://finance.yahoo.com/quote/NVDA/)
- [Broadcom quote page](https://finance.yahoo.com/quote/AVGO/)
- [Meta quote page](https://finance.yahoo.com/quote/META/)
