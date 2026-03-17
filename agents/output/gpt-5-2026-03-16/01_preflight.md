# Preflight

**Date:** 2026-03-16
**Run Status:** `DATA_OK`
**Publication Constraint:** `REVIEW_ONLY`

## Coverage Summary

| Data Class | Status | Tag | Notes |
| --- | --- | --- | --- |
| SPY / QQQ / DIA | Available | `LIVE` | Finance snapshots available at 2026-03-17 00:15 UTC |
| Sector leadership | Available | `LIVE` | `XLK`, `XLY`, `XLI`, `XLF`, `XLV`, `XLC`, `XLU`, `XLRE`, `XLP` |
| Sampled single-name prices | Available | `LIVE` | 16 liquid large-cap U.S. names |
| Market cap / PE / EPS | Available for most sample names | `LIVE` | Sufficient for sampled ranking |
| Confirmed next earnings webcast dates | Partial | `DELAYED` | Confirmed for `GE`, `GEV`; estimated or unconfirmed for some others |
| Full beta / correlation matrix | Missing | `N/A` | No validated feed in workspace |
| 30-day realized volatility | Missing | `N/A` | Not sourced name by name |
| Full eligible universe screen | Missing | `N/A` | No end-to-end U.S. screen performed |

## Benchmark Snapshot

| Ticker | Price | Day Change | Tag |
| --- | --- | --- | --- |
| `SPY` | 669.03 | +1.03% | `LIVE` |
| `QQQ` | 600.38 | +1.14% | `LIVE` |
| `DIA` | 470.30 | +0.83% | `LIVE` |
| `XLK` | 138.78 | +1.46% | `LIVE` |
| `XLY` | 112.20 | +1.22% | `LIVE` |
| `XLI` | 166.06 | +0.86% | `LIVE` |
| `XLF` | 49.30 | +0.85% | `LIVE` |
| `XLP` | 84.98 | +0.28% | `LIVE` |

## Validation Result

- Data lineage is clear enough to score a sampled watchlist.
- Data lineage is not strong enough to approve live position sizing under the prompt's own rules.
- No fabricated fields were inserted; missing portfolio-risk inputs remain explicitly marked missing.

## Preflight Decision

Proceed to ranking, but lock the run to `REVIEW_ONLY` unless a complete risk dataset becomes available.

## Source Notes

- Finance snapshots from the live market data tool.
- FOMC schedule from the Federal Reserve calendar: [March 2026 calendar](https://www.federalreserve.gov/newsevents/2026-march.htm)
