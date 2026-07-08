# Factor Scores

**Date:** 2026-04-16
**Scoring Mode:** Sample-relative, evidence-weighted
**Important Limitation:** Percentiles are relative to the 16-name sampled universe, not the full eligible U.S. universe.

## Method

Family scores use a `1-5` scale.

- **Fundamental:** recent earnings quality, margin durability, and balance-sheet / cash-flow quality from official or recent public materials
- **Technical:** current or recent quote-page strength relative to the sampled set
- **Sentiment / Positioning:** freshness of catalyst stack, earnings follow-through, and public-market narrative support
- **Macro / Regime:** fit with the current AI-led, still-constructive large-cap tape

Formula:

`Composite = 0.30*Fundamental + 0.30*Technical + 0.25*Sentiment + 0.15*Macro`

`Adjusted Score = (Composite * 20 * Data Quality Multiplier) - Penalties`

## Ranked Table

| Rank | Ticker | Fund. | Tech. | Sent. | Macro | DQ | Penalty | Adjusted | Sample Pctl | Completeness | Verdict |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | `AVGO` | 4.5 | 5.0 | 4.5 | 4.5 | 0.93 | 0.0 | 86.5 | 100 | 89% | Sample-pass |
| 2 | `META` | 4.5 | 4.5 | 4.5 | 4.5 | 0.92 | 0.0 | 82.8 | 94 | 88% | Sample-pass |
| 3 | `NVDA` | 4.5 | 4.5 | 4.5 | 4.0 | 0.92 | 0.0 | 81.9 | 88 | 88% | Sample-pass |
| 4 | `GEV` | 4.5 | 4.0 | 4.0 | 4.5 | 0.91 | 0.0 | 78.3 | 81 | 87% | Sample-pass |
| 5 | `MSFT` | 4.5 | 3.5 | 4.0 | 4.5 | 0.90 | 0.0 | 74.7 | 81 | 86% | Sample-pass |
| 6 | `AMZN` | 4.0 | 4.0 | 4.0 | 4.0 | 0.88 | 0.0 | 70.4 | 75 | 84% | Near miss |
| 7 | `JPM` | 4.5 | 3.5 | 4.0 | 3.5 | 0.88 | 0.0 | 69.5 | 69 | 85% | Near miss |
| 8 | `BAC` | 4.0 | 3.5 | 3.5 | 3.5 | 0.87 | 0.0 | 64.4 | 63 | 83% | Near miss |
| 9 | `WFC` | 4.0 | 3.0 | 3.5 | 3.5 | 0.87 | 1.0 | 60.8 | 56 | 83% | Near miss |
| 10 | `GS` | 4.0 | 3.0 | 3.5 | 3.5 | 0.87 | 1.0 | 60.8 | 50 | 83% | Near miss |
| 11 | `AMD` | 4.0 | 3.5 | 3.0 | 4.0 | 0.85 | 1.0 | 60.2 | 44 | 82% | Near miss |
| 12 | `GOOGL` | 4.0 | 3.0 | 3.0 | 4.0 | 0.88 | 1.0 | 60.6 | 38 | 84% | Near miss |
| 13 | `TSM` | 4.0 | 3.0 | 3.0 | 4.0 | 0.84 | 1.0 | 57.8 | 31 | 81% | Reject |
| 14 | `ETN` | 4.0 | 2.5 | 3.0 | 4.0 | 0.84 | 1.0 | 55.3 | 25 | 81% | Reject |
| 15 | `GE` | 4.0 | 2.5 | 2.5 | 4.0 | 0.84 | 1.0 | 52.8 | 19 | 81% | Reject |
| 16 | `ASML` | 4.0 | 2.0 | 2.5 | 3.5 | 0.84 | 1.0 | 47.7 | 13 | 80% | Reject |

## Driver Note

The leaderboard is driven by three clusters:

1. AI infrastructure and custom-silicon leadership: `AVGO`, `NVDA`
2. AI platform monetization and capex beneficiaries: `META`, `MSFT`
3. Power and electrification tied to data-center demand: `GEV`

## Important Interpretation

Five names clear the sample-relative bar, but the set still fails the prompt's live-deployment bar because:

1. it is not a full-universe ranking,
2. three of the five names sit inside a concentrated late-April earnings window, and
3. portfolio-risk controls remain unsourced.
