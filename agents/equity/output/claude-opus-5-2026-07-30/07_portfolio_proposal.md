# 07 — Portfolio Proposal — 2026-07-30

## Outcome: **no portfolio proposed — `NO_TRADE`**

The investable set handed over by factor scoring is **empty**, so there is nothing to size.
Per `agents.md § Portfolio Construction` the Task-0 feasibility pre-check still ran, because its
computed evidence is what makes the `NO_TRADE` decision auditable rather than asserted — and
because the feasibility question must be **re-answered every run**, not inherited.

## Task-0 constraint feasibility pre-check

Computed from already-fetched 60-day returns, before any sizing.

| Constraint | Computed | Cap / band | Verdict |
|---|---|---|---|
| Single-name weight | 5% cap ⇒ ≥ 20 positions | 5% | binding by construction |
| **Max attainable sleeve beta** | **+1.1258** | ≥ 0.90 floor | **FEASIBLE** |
| Min attainable sleeve beta | -0.7728 | ≤ 1.10 ceiling | FEASIBLE |
| Top-20 equal-weight beta | +0.0978 | 0.90–1.10 | outside band as-ranked |
| Avg pairwise correlation (top 20) | 0.1559 | < 0.45 | **PASS** |
| 95th-pctl 1-month drawdown (top 20, EW) | 8.55% | ≤ 8% | **FAIL** |
| Max sector weight (top 20, EW) | 25.0% (Industrials) | ≤ 30% | **PASS** |

**The beta band is feasible this run.** The 20 highest betas in the ≥80th-percentile pool
(+2.07, +2.01, +1.73, +1.67, +1.49, +1.43, +1.42, +1.22, …) average
**+1.1258**, which clears the 0.90 floor. This is a materially
different finding from 2026-07-27, when the same computation returned +0.8519 and *proved*
infeasibility. That narrative was **re-verified rather than reused**, exactly as the 2026-07-29
package warned.

So `NO_TRADE` here is **not** a feasibility verdict. It is an evidence verdict: the investable
set is empty before any constraint is consulted.

Two secondary observations, recorded for the record rather than as the decision basis:

1. The naive equal-weight top-20 sleeve has beta +0.0978 — far below
   the band. Reaching 0.90 would require abandoning rank order and selecting on beta, which the
   objective function does not authorise.
2. That same sleeve's 95th-percentile 1-month drawdown is
   8.55%, above the 8% cap — an independent `NO_TRADE`
   trigger (`rules.md § Downgrade to NO_TRADE` #5) had the run got that far.

## Portfolio analytics

| Analytic | Value |
|---|---|
| Weights | **none — no positions proposed** |
| Portfolio sigma (1m, top-20 EW reference) | 5.18% |
| 95th-pctl 1-month drawdown | 8.55% |
| Avg pairwise correlation | 0.1559 |
| Expected beta | +0.0978 |
| Expected Sharpe / Sortino / IR | `N/A` — no portfolio |
| Tracking error | `N/A` — no portfolio |

These reference figures are computed from the fetched covariance of the 20 top-ranked names and
are shown only to evidence the pre-check. They are **not** a shadow recommendation.

## Per-position recommendation metrics

`N/A` — no positions. Per-name metrics for the monitoring sleeve are in `06_top_candidates.md`,
inherited unchanged from `05`.

## Why excluded names were left out

Every name in the universe was excluded for the same universe-wide reason: with `Fund_Z` and
`Sent_Z` `UNAVAILABLE`, no name can satisfy Evidence Threshold 2 or 4. There is no name-specific
exclusion rationale to give, and inventing one would misrepresent the cause.

Per `rules.md`, constraints were never weakened to force a publishable portfolio, and fewer
names were preferred over lower-quality names — here that reduces to zero names.
