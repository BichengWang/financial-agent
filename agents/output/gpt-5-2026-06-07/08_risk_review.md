# Risk Review

**Date:** 2026-06-07  
**Committee decision:** `REJECT_FOR_GO / APPROVE_FOR_REVIEW_ONLY`  
**Final publication recommendation:** `REVIEW_ONLY`

## Top Concerns

1. **Live risk analytics are still missing.** The proposal cannot validate portfolio beta, pairwise correlation, tracking error, or 95th-percentile one-month drawdown.
2. **Macro event risk is high.** CPI on June 10 and FOMC on June 16-17 can reverse the current financials/energy/defensive rotation or deepen the growth drawdown.
3. **The universe is sampled, not exhaustive.** The candidate set is useful as a watchlist, but sample-relative percentiles do not satisfy the prompt's full-universe investability standard.

## Rule Check

| Rule | Result | Committee View |
| --- | --- | --- |
| No fabricated data | Pass | Missing fields are labeled `N/A`; candidate scores are sample-relative. |
| Full-universe percentile validation | Fail | Sampled 60-equity universe only. |
| Data completeness >= 85% | Partial | Public candidate evidence passes; risk model completeness fails. |
| Max single-name 5% | Pass | Review-only sleeve caps every name at 5%. |
| Max sector 30% | Pass | Largest sector is healthcare at 15%. |
| Beta 0.90-1.10 | Unknown | Blocks `GO`. |
| Avg pairwise correlation < 0.45 | Unknown | Blocks `GO`. |
| 95th-percentile 1M drawdown <= 8% | Unknown | Blocks `GO`. |
| Event risk concentration | Pass in sleeve | `ORCL` excluded; no selected candidate has confirmed earnings inside 14 days from current evidence. |

## Required Fixes Before Any Future `GO`

1. Wire a durable quote source that includes live/delayed bid/ask, ADV, and corporate-action handling.
2. Add a validated risk model for beta, pairwise correlation, residual tracking error, and one-month drawdown.
3. Add options IV/skew and short-interest inputs or explicitly keep all confidence capped.
4. Replace the sampled universe with a reproducible full U.S. equity screen.
5. Resolve the artifact-numbering mismatch between `main.md` and `daily_output_spec.md`.

## Final Decision

The research package is publishable as `REVIEW_ONLY`. A live `GO` would require inventing risk data, so it is rejected.
