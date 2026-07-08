# Factor Scores

**Date:** 2026-06-07  
**Scoring mode:** Sample-relative, evidence-weighted  
**Data mode:** `MIXED_DELAYED`  
**Publication constraint:** `REVIEW_ONLY`

## Method

Family scores use a 1-5 scale.

- Fundamental: recent earnings/guidance quality, balance-sheet quality, margin visibility.
- Technical / price: June 5 relative strength versus `SPY`, `QQQ`, and sector context.
- Sentiment / positioning: catalyst durability and crowding risk; options/short-interest unavailable.
- Macro / regime: fit with `HIGH_VOL / RATE_SHOCK` conditions.

Formula:

`Composite = 0.30*Fundamental + 0.30*Technical + 0.25*Sentiment + 0.15*Macro`

`Adjusted Score = Composite * 20 * Data Quality Multiplier - Penalties`

No candidate receives `HIGH` confidence because options, short-interest, full universe, and validated portfolio-risk data are unavailable.

## Ranked Table

| Rank | Ticker | Fund. | Tech. | Sent. | Macro | DQ | Penalty | Adjusted | Sample Pctl | Completeness | Verdict |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | `AZO` | 4.2 | 4.8 | 4.0 | 4.3 | 0.88 | 0.0 | 78.4 | 100 | 88% | Candidate |
| 2 | `UNH` | 4.0 | 4.7 | 4.0 | 4.4 | 0.87 | 0.0 | 76.3 | 98 | 87% | Candidate |
| 3 | `MCK` | 4.3 | 4.4 | 4.1 | 4.3 | 0.87 | 0.0 | 76.0 | 96 | 87% | Candidate |
| 4 | `JPM` | 4.3 | 4.3 | 4.0 | 4.4 | 0.87 | 0.0 | 75.5 | 94 | 87% | Candidate |
| 5 | `XOM` | 4.1 | 4.4 | 3.9 | 4.6 | 0.86 | 0.0 | 74.1 | 92 | 86% | Candidate |
| 6 | `CAT` | 4.1 | 4.5 | 3.8 | 4.2 | 0.86 | 0.0 | 73.1 | 90 | 86% | Candidate |
| 7 | `WMT` | 4.2 | 4.0 | 3.9 | 4.4 | 0.86 | 0.0 | 72.4 | 88 | 86% | Candidate |
| 8 | `ABBV` | 4.0 | 4.3 | 3.8 | 4.2 | 0.86 | 0.0 | 71.8 | 86 | 86% | Candidate |
| 9 | `GS` | 4.1 | 4.0 | 3.8 | 4.3 | 0.86 | 0.0 | 71.0 | 84 | 86% | Candidate |
| 10 | `PG` | 4.0 | 4.0 | 3.7 | 4.4 | 0.85 | 0.0 | 69.5 | 82 | 85% | Candidate |
| 11 | `GE` | 4.2 | 3.8 | 3.7 | 4.0 | 0.85 | 0.0 | 68.1 | 80 | 85% | Near miss |
| 12 | `CVX` | 4.0 | 4.1 | 3.6 | 4.5 | 0.85 | 0.0 | 68.0 | 78 | 85% | Near miss |
| 13 | `BAC` | 3.8 | 4.3 | 3.6 | 4.4 | 0.84 | 0.0 | 67.9 | 76 | 84% | Near miss |
| 14 | `C` | 3.7 | 4.5 | 3.5 | 4.2 | 0.84 | 0.0 | 67.6 | 74 | 84% | Near miss |
| 15 | `COST` | 4.3 | 3.6 | 3.8 | 4.2 | 0.85 | 0.0 | 67.4 | 72 | 85% | Near miss |
| 16 | `ORLY` | 4.0 | 4.1 | 3.6 | 4.0 | 0.84 | 0.0 | 66.5 | 70 | 84% | Near miss |
| 17 | `EOG` | 3.9 | 4.0 | 3.5 | 4.4 | 0.84 | 0.0 | 66.3 | 68 | 84% | Near miss |
| 18 | `RTX` | 4.0 | 3.6 | 3.6 | 4.0 | 0.84 | 0.0 | 64.1 | 66 | 84% | Near miss |
| 19 | `LLY` | 4.5 | 3.4 | 3.6 | 3.7 | 0.84 | 0.0 | 64.0 | 64 | 84% | Near miss |
| 20 | `AMAT` | 4.1 | 3.6 | 3.5 | 3.3 | 0.84 | 0.0 | 62.2 | 62 | 84% | Near miss |

## Recommended Threshold-Clearing Subset For Review

`AZO`, `UNH`, `MCK`, `JPM`, `XOM`, `CAT`, `WMT`, `ABBV`, `GS`, `PG`

This is not a live-investable subset. It clears the sampled review screen, but the run lacks full-universe percentiles and validated risk analytics.

## Driver Note

The current leaderboard is driven by:

1. Defensive relative strength: `AZO`, `UNH`, `MCK`, `WMT`, `ABBV`, `PG`.
2. Higher-rate beneficiaries: `JPM`, `GS`.
3. Inflation/energy hedge: `XOM`.
4. Selective cyclicals with relative strength: `CAT`.

## Signal Decay Notes

- Financials can decay quickly if yields reverse after CPI/FOMC.
- Energy leadership is partly macro/geopolitical and can unwind with oil.
- Defensive healthcare/staples can underperform if the market snaps back into high-beta growth.
- `AZO` and `CAT` have strong price leadership but are economically sensitive, so confidence remains `MEDIUM`.
