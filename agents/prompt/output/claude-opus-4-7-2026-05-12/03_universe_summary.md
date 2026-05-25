# 03 Universe Summary

## Status

⚠️ ILLUSTRATIVE — NOT LIVE DATA. The eligible universe cannot be constructed without live exchange/listing data. The figures below are placeholder counts to validate the artifact contract, not real screening output.

## Universe Counts (Illustrative)

| Stage | Count | Tag |
|---|---:|---|
| All U.S.-listed common equities | ~6000 | ILLUSTRATIVE |
| After listing/exchange filter | ~5400 | ILLUSTRATIVE |
| After market cap > $2B | ~2200 | ILLUSTRATIVE |
| After ADV > $20M | ~1500 | ILLUSTRATIVE |
| After price > $5 | ~1480 | ILLUSTRATIVE |
| After listing age > 6M | ~1450 | ILLUSTRATIVE |
| After active-day & spread filter | ~1400 | ILLUSTRATIVE |
| **Eligible universe** | **~1400** | ILLUSTRATIVE |

## Rejection Categories (Illustrative Distribution)

| Category | Count | Notes |
|---|---:|---|
| Sub-cap | ~3200 | Cap < $2B |
| Thin liquidity | ~700 | ADV < $20M or spread > 50 bps |
| Penny / sub-$5 | ~20 | Price gate |
| Recent IPO / SPAC < 6M | ~30 | Listing age |
| Active-day shortfall | ~50 | < 80% active in trailing 60 sessions |
| Pending corporate action | N/A | No M&A/spin-off feed available |
| ADRs with thin U.S. liquidity | N/A | No exchange-routing flag feed |

## Event Concentration

- Earnings calendar feed: **N/A**. Cannot compute event clustering.
- Per `eval/stop_criteria.md` §Downgrade To No-Trade item 4, event-cluster control is unverifiable, which independently supports `REVIEW_ONLY` framing.

## Handoff to Factor Scoring

Universe is structurally well-defined but not populated with real names today. Factor scoring will operate against an illustrative micro-universe (mega-cap names) purely to exercise the schema. Investable promotion is disabled.
