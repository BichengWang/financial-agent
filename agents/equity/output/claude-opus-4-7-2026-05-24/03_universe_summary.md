# 03 Universe Summary

⚠️ ILLUSTRATIVE — NOT LIVE DATA. Universe filter is run against the model's training-data reference state of U.S.-listed equities. Counts are reference-state estimates tagged `ILLUSTRATIVE_REF`.

## Filter Configuration

Inclusion (from `research_system.md` §Universe Construction → Inclusion):

| Filter | Threshold |
|---|---|
| Listing | U.S. primary exchange |
| Market cap | > $2B |
| 20-day average daily dollar volume | > $20M |
| Price | > $5 |
| Listing age | > 6 months |

Exclusion:

- Thin ADRs / low-liquidity U.S. listings
- Halted or pending-delisting securities
- Bid-ask spread > 50 bps
- Trading on < 80% of sessions in the trailing 60 days
- Unresolved corporate-action ambiguity

## Universe Counts (Reference-State Estimates)

| Bucket | Count | Tag |
|---|---|---|
| Investable starting universe (Russell 3000 ∪ S&P 1500) | ~3,200 | `ILLUSTRATIVE_REF` |
| Pass market-cap > $2B | ~1,800 | `ILLUSTRATIVE_REF` |
| Pass 20D ADV > $20M | ~1,200 | `ILLUSTRATIVE_REF` |
| Pass price > $5 | ~1,180 | `ILLUSTRATIVE_REF` |
| Pass listing age > 6 months | ~1,150 | `ILLUSTRATIVE_REF` |
| Pass spread / liquidity exclusions | ~1,100 | `ILLUSTRATIVE_REF` |
| **Eligible after exclusions** | **~1,100** | `ILLUSTRATIVE_REF` |

## Rejection Log (Reference-State Patterns)

| Reason code | Approx count | Examples (illustrative) |
|---|---|---|
| `REASON_MCAP_BELOW_2B` | ~1,400 | Many small-cap names |
| `REASON_LIQ_THIN` | ~600 | Thin ADRs, micro-cap biotech |
| `REASON_PRICE_LT_5` | ~20 | Sub-$5 names |
| `REASON_LISTING_AGE` | ~30 | Recent IPOs, SPAC-de-SPAC |
| `REASON_SPREAD_GT_50BPS` | ~50 | Low-volume mid-caps |

These are reference-state distribution shapes, not today's tape. They are shown so the universe filter is auditable.

## Sector Coverage Of Eligible Universe (Reference-State)

| Sector (GICS L1) | Eligible names (approx) | Reference-state median 30D vol |
|---|---|---|
| Communication Services | ~50 | Mid-20s |
| Consumer Discretionary | ~140 | Mid-20s |
| Consumer Staples | ~60 | Mid-teens |
| Energy | ~70 | High-20s |
| Financials | ~210 | Low-20s |
| Health Care | ~190 | Mid-20s |
| Industrials | ~180 | Low-20s |
| Information Technology | ~140 | High-20s |
| Materials | ~50 | Mid-20s |
| Real Estate | ~70 | Mid-20s |
| Utilities | ~50 | Mid-teens |

Total: ~1,100 reference-state-eligible names.

## Stop-Criteria Cross-Check

- §Hard Halt item 4 (universe too small): not triggered — ample eligible names.
- §Downgrade To No-Trade item 1 (fewer than 5 investable): not triggered.

## Handoff Note → Factor Scoring Agent

> Eligible universe is ~1,100 reference-state names. Apply the four factor families, the `0.80` data quality multiplier, and the standard penalties. Surface a top-20 by adjusted score and an investable subset of 5-10 names. Cap confidence at `MEDIUM`.
