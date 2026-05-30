# 04 Factor Scores

⚠️ ILLUSTRATIVE — NOT LIVE DATA. All numerical values below are placeholders. Use only to verify schema, ranking logic, and downstream artifact wiring. None of these scores constitutes a recommendation.

## Methodology Snapshot

- Per-signal pipeline: winsorize ±3σ → industry-group Z (sector-neutral) → average within family.
- Family weights: `0.30·F + 0.30·T + 0.25·S + 0.15·M`.
- Adjusted score: `Composite_Z · Data_Quality_Multiplier − Penalties`.
- Today's data quality multiplier: **0.70** (floor) — at the investability threshold; under `REVIEW_ONLY` no name will be promoted.

## Factor Family Coverage (Today)

| Family | Computable? | Notes |
|---|---|---|
| Fundamental | NO | No fundamentals feed; all signals `N/A`. |
| Technical | NO | No price/volume series; all signals `N/A`. |
| Sentiment | NO | No SI/skew/revisions/insider/13F feeds. |
| Macro | PARTIAL | Regime context illustrative only. |

Per `eval/research_system.md` §Evidence Thresholds item 2, at least 3-of-4 families must be non-negative for investable status. **0-of-4** are real today → no investable promotion possible.

## Top 20 (Illustrative — Schema Demonstration Only)

| Rank | Ticker | Z_F | Z_T | Z_S | Z_M | Composite | DQ Mult | Adjusted | Pctile |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | MSFT | +1.4 | +1.2 | +1.1 | +0.4 | +1.18 | 0.70 | +0.83 | 99 |
| 2 | NVDA | +1.6 | +1.3 | +0.7 | +0.2 | +1.18 | 0.70 | +0.83 | 99 |
| 3 | META | +1.3 | +1.2 | +1.0 | +0.3 | +1.13 | 0.70 | +0.79 | 98 |
| 4 | GOOGL | +1.2 | +1.0 | +0.9 | +0.4 | +1.02 | 0.70 | +0.71 | 97 |
| 5 | AMZN | +1.1 | +1.1 | +0.7 | +0.3 | +0.96 | 0.70 | +0.67 | 96 |
| 6 | AVGO | +1.2 | +0.9 | +0.6 | +0.2 | +0.89 | 0.70 | +0.62 | 95 |
| 7 | LLY | +1.4 | +0.5 | +0.4 | +0.0 | +0.79 | 0.70 | +0.55 | 94 |
| 8 | V | +0.9 | +0.7 | +0.5 | +0.4 | +0.69 | 0.70 | +0.48 | 92 |
| 9 | MA | +0.9 | +0.6 | +0.5 | +0.3 | +0.65 | 0.70 | +0.46 | 91 |
| 10 | UNH | +0.8 | +0.4 | +0.4 | +0.3 | +0.55 | 0.70 | +0.39 | 89 |
| 11–20 | … | … | … | … | … | … | 0.70 | … | 80–88 |

## Penalty Application Note

No earnings-window, vol, or stability penalties applied — required event/vol inputs are `N/A`, so penalties cannot be evaluated. This is itself a reason no name is investable today.

## Driver Note

Family contributions cannot be honestly described today; all underlying signals are placeholders. The shape of the leaderboard is a function of the illustrative ordering, not real factor evidence.

## Recommendation

Per `eval/stop_criteria.md` §Downgrade item 1 (fewer than 5 names pass investable threshold) and §Review-Only item 1, recommend **`REVIEW_ONLY`** to the orchestrator.
