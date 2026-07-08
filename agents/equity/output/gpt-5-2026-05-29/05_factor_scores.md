# Factor Scores

**Date:** 2026-05-29  
**Scoring Mode:** Sample-relative, evidence-weighted  
**Publication Constraint:** `REVIEW_ONLY`

## Method

Family scores use a `1-5` scale.

- **Fundamental:** recent revenue, margin, backlog, guidance, cash-flow quality
- **Technical / Price:** delayed quote snapshot, MoM validation where available, relative leadership
- **Sentiment / Positioning:** catalyst freshness, earnings reaction, narrative durability
- **Macro / Regime:** fit with AI-led low-volatility tape, rates sensitivity, sector leadership

Formula:

`Composite = 0.30*Fundamental + 0.30*Technical + 0.25*Sentiment + 0.15*Macro`

`Adjusted Score = Composite * 20 * Data Quality Multiplier - Penalties`

Penalties are in score points. Near-term earnings inside 14 days cap confidence at `LOW` unless event-specific risk is explicitly modeled; no such model is available today.

## Ranked Table

| Rank | Ticker | Fund. | Tech. | Sent. | Macro | DQ | Penalty | Adjusted | Sample Pctl | Completeness | Verdict |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | `NVDA` | 5.0 | 4.5 | 4.6 | 4.6 | 0.90 | 0.0 | 84.4 | 100 | 90% | Candidate |
| 2 | `MSFT` | 4.7 | 4.4 | 4.5 | 4.3 | 0.90 | 0.0 | 80.7 | 96 | 89% | Candidate |
| 3 | `GEV` | 4.8 | 4.0 | 4.5 | 4.6 | 0.89 | 0.0 | 79.6 | 93 | 88% | Candidate |
| 4 | `PLTR` | 4.5 | 4.8 | 4.7 | 3.8 | 0.84 | 2.0 | 73.3 | 89 | 85% | Candidate |
| 5 | `ANET` | 4.3 | 4.0 | 4.4 | 4.4 | 0.86 | 0.0 | 73.2 | 86 | 86% | Candidate |
| 6 | `GOOGL` | 4.6 | 3.4 | 4.2 | 4.2 | 0.88 | 0.0 | 72.9 | 82 | 87% | Candidate |
| 7 | `AMZN` | 4.4 | 3.7 | 4.2 | 4.0 | 0.87 | 0.0 | 72.2 | 79 | 86% | Near miss |
| 8 | `AVGO` | 4.8 | 4.5 | 4.6 | 4.4 | 0.90 | 10.0 | 72.0 | 75 | 89% | Event-risk carry |
| 9 | `ORCL` | 4.5 | 4.7 | 4.5 | 4.2 | 0.86 | 8.0 | 69.1 | 71 | 84% | Near miss |
| 10 | `GE` | 4.2 | 4.1 | 3.8 | 3.8 | 0.86 | 0.0 | 68.6 | 68 | 84% | Near miss |
| 11 | `CRM` | 3.9 | 4.8 | 3.8 | 3.4 | 0.84 | 2.0 | 65.8 | 64 | 82% | Near miss |
| 12 | `ETN` | 4.2 | 3.5 | 3.8 | 4.4 | 0.84 | 0.0 | 65.2 | 61 | 83% | Near miss |
| 13 | `CEG` | 4.0 | 3.6 | 3.8 | 4.2 | 0.83 | 0.0 | 64.1 | 57 | 81% | Near miss |
| 14 | `GS` | 4.1 | 4.1 | 3.4 | 3.1 | 0.84 | 0.0 | 63.8 | 54 | 82% | Near miss |
| 15 | `AMD` | 4.0 | 3.0 | 3.5 | 4.3 | 0.84 | 0.0 | 61.2 | 50 | 82% | Near miss |
| 16 | `JPM` | 4.3 | 3.1 | 3.5 | 3.2 | 0.84 | 0.0 | 61.1 | 46 | 82% | Near miss |
| 17 | `VST` | 3.8 | 3.1 | 3.8 | 4.0 | 0.82 | 0.0 | 60.6 | 43 | 80% | Near miss |
| 18 | `META` | 4.3 | 2.4 | 3.4 | 3.9 | 0.87 | 0.0 | 60.2 | 39 | 86% | Downgrade |
| 19 | `AAPL` | 4.0 | 2.7 | 3.0 | 3.4 | 0.86 | 0.0 | 57.5 | 36 | 84% | Reject |
| 20 | `TSM` | 4.2 | 2.8 | 3.2 | 3.3 | 0.82 | 1.0 | 56.7 | 32 | 80% | Reject |

## Recommended Threshold-Clearing Subset For Review

`NVDA`, `MSFT`, `GEV`, `PLTR`, `ANET`, `GOOGL`

This is a review-only subset. It is not live-investable because sample-relative percentiles and missing risk-model inputs fail the evidence threshold for `GO`. `AVGO` remains an event-risk carry watchlist name; `AMZN` remains a near miss.

## Driver Note

The leaderboard is driven by:

1. AI compute and infrastructure: `NVDA`, `AVGO`, `ANET`
2. AI cloud/platform monetization: `MSFT`, `GOOGL`, `AMZN`, `ORCL`
3. Applied AI software: `PLTR`
4. Power/electrification: `GEV`

## Signal Decay Notes

- `CRM` and `ORCL` show strong current price action, but the signal may decay quickly because it appears tied to near-term earnings/event repricing.
- `AVGO` remains fundamentally strong but must be treated as an event trade until after June 3, 2026.
- `PLTR` has strong momentum but high valuation/crowding risk, so confidence is capped at `MEDIUM`.
