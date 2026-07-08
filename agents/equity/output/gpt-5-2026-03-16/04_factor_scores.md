# Factor Scores

**Date:** 2026-03-16
**Scoring Mode:** Sample-relative, evidence-weighted
**Important Limitation:** Percentiles are relative to the 16-name sampled universe, not the full eligible U.S. universe.

## Method

Family scores use a `1-5` scale.

- **Fundamental:** recent earnings/guidance quality, EPS/PE context, backlog or revenue trajectory
- **Technical:** same-day price leadership and alignment with leading sectors
- **Sentiment / Positioning:** freshness of catalysts, official company updates, post-earnings momentum
- **Macro / Regime:** fit with today's bullish leadership and the 2-6 week macro backdrop

Formula:

`Composite = 0.30*Fundamental + 0.30*Technical + 0.25*Sentiment + 0.15*Macro`

`Adjusted Score = (Composite * 20 * Data Quality Multiplier) - Penalties`

## Ranked Table

| Rank | Ticker | Fund. | Tech. | Sent. | Macro | DQ | Penalty | Adjusted | Sample Pctl | Completeness | Verdict |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | `GEV` | 4.5 | 5.0 | 4.0 | 5.0 | 0.90 | 0.0 | 83.3 | 100 | 88% | Sample-pass |
| 2 | `NVDA` | 4.5 | 4.5 | 5.0 | 4.5 | 0.90 | 0.0 | 83.3 | 94 | 87% | Sample-pass |
| 3 | `META` | 4.5 | 5.0 | 4.5 | 4.0 | 0.90 | 0.0 | 81.9 | 88 | 86% | Sample-pass |
| 4 | `ETN` | 4.5 | 4.0 | 4.0 | 4.5 | 0.95 | 0.0 | 80.8 | 81 | 89% | Sample-pass |
| 5 | `AVGO` | 4.5 | 4.0 | 4.5 | 4.5 | 0.92 | 0.0 | 80.5 | 75 | 86% | Sample-pass |
| 6 | `GE` | 4.5 | 4.0 | 3.5 | 4.5 | 0.95 | 0.0 | 78.9 | 69 | 88% | Near miss |
| 7 | `CRM` | 4.5 | 4.5 | 4.0 | 3.5 | 0.92 | 0.0 | 76.8 | 63 | 86% | Near miss |
| 8 | `LRCX` | 4.0 | 5.0 | 3.0 | 4.5 | 0.90 | 2.0 | 70.9 | 56 | 84% | Near miss |
| 9 | `AMZN` | 4.5 | 4.0 | 4.0 | 4.0 | 0.88 | 0.0 | 73.0 | 50 | 84% | Near miss |
| 10 | `MSFT` | 4.5 | 3.5 | 4.0 | 4.0 | 0.90 | 0.0 | 72.0 | 44 | 85% | Near miss |
| 11 | `ANET` | 4.5 | 4.0 | 3.5 | 4.0 | 0.88 | 0.0 | 70.4 | 38 | 83% | Near miss |
| 12 | `GOOGL` | 4.5 | 3.5 | 3.5 | 3.5 | 0.90 | 0.0 | 68.4 | 31 | 85% | Near miss |
| 13 | `GS` | 4.0 | 4.0 | 3.0 | 4.0 | 0.88 | 0.0 | 65.1 | 25 | 82% | Reject |
| 14 | `JPM` | 4.0 | 3.5 | 3.0 | 4.0 | 0.90 | 0.0 | 63.9 | 19 | 82% | Reject |
| 15 | `PANW` | 4.0 | 2.5 | 3.0 | 3.5 | 0.90 | 0.0 | 57.6 | 13 | 81% | Reject |
| 16 | `WMT` | 4.0 | 1.5 | 2.5 | 2.5 | 0.90 | 0.0 | 49.5 | 6 | 83% | Reject |

## Driver Note

The current leaderboard is driven by three clusters:

1. AI infrastructure leadership: `NVDA`, `AVGO`
2. Power / electrification / industrial backlog: `GEV`, `ETN`, `GE`
3. AI-enabled platform monetization: `META`, `CRM`

## Important Interpretation

The top five clear the sample-relative ranking bar. They do not clear the prompt's full-universe execution bar because the universe itself is incomplete.
