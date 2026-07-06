# 07 Portfolio Proposal

## Constraint Feasibility Pre-Check (Task 0 — before any sizing)

Input: investable set from 05. **The investable set is EMPTY** (0 names pass evidence threshold #2 with 2/4 families sourceable; threshold requires 3 of 4 non-negative). Stop criterion `NO_TRADE #1` (fewer than 5 investable names) fires immediately — **no weights drafted, no revision pass spent**, per the Track B pre-check rule (2026-06-10, HUMAN_REVIEW).

Recommendation: **NO_TRADE**.

## Feasibility Diagnostics (informational, from already-fetched inputs)

Had the 23-name monitoring sleeve been investable, the achievable envelope from fetched inputs would be: sleeve beta range ~0.16–1.46 per name (cap-weighted feasible inside the 0.90–1.10 band via mixing); sector counts below — Health Care at 6/23 (26%) and IT at 5/23 (22%) fit under the 30% cap with the 5% single-name cap binding every position (all Kelly 0.25 >= 5% NAV):

| Sector (INFERRED) | Names | Share |
|---|---|---|
| Health Care | 6 | 26% of sleeve |
| Information Technology | 5 | 22% of sleeve |
| Industrials | 3 | 13% of sleeve |
| Financials | 3 | 13% of sleeve |
| Communication Services | 2 | 9% of sleeve |
| Consumer Staples | 2 | 9% of sleeve |
| Real Estate | 1 | 4% of sleeve |
| Materials | 1 | 4% of sleeve |

These diagnostics are not a proposal; they document that today's block is the family-coverage gate, not portfolio-constraint infeasibility.

## Per-Position Recommendation Metrics

Inherited unchanged from 05 (single source; no recomputation) — see the Ranked Candidate Table there, columns Entry through CI bounds, with score traces and ledger rows.

## Excluded Names

DROP-bound (02 §5): MCK, COST, WMT, CVX, XOM, MU, NVDA, GOOGL. DOWNGRADE-bound: UNH (earnings ~9d, -0.15 penalties, 5th day out). Near-miss ranks 21-30: see 05.
