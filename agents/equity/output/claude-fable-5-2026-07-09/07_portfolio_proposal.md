# 07 Portfolio Proposal

## Constraint Feasibility Pre-Check (Task 0 — before any sizing)

**Input condition failed upstream: the investable set is EMPTY** (05: family-coverage gate — at most 2 of 4 factor families sourceable universe-wide → evidence threshold #2 unsatisfiable → stop criterion #1, fewer than 5 investable names). Portfolio construction therefore terminates at the pre-check with **NO_TRADE**; no weights drafted, no revision pass spent (Track B procedure, 2026-06-10, HUMAN_REVIEW).

For the record, had the gate not bound, the sleeve-level feasibility snapshot from already-fetched inputs (ledger rows L070–L207) would be:

- **Achievable sleeve beta range** (60d regression betas of the 23 monitored names): single-name betas span ~0.1–1.7; an equal-weight top-10 sits near ~0.75 — below the 0.90 floor without deliberately overweighting the high-beta legs (AXON, DELL, DDOG, PANW, CRWD), which the 5% single-name cap limits. The defensive tilt that tops the leaderboard remains structurally hard to fit inside the 0.90–1.10 band — same conclusion as 07-08.
- **Sector shares under the 5% cap**: IT 7 names / HC 6 / Financials 4 — a 10-name book drawn from the top of the board would breach or press the 30% sector cap in IT or HC without reaching deep into lower percentiles.
- **Event risk**: only DAL (reported this morning) and FFIV (18d) carry the earnings flag inside the published sleeve — below the >2-names-inside-14d NO_TRADE trigger on its own.

## Required Output

No portfolio: **NO_TRADE**. Per-position Recommendation Metrics are carried in full in 05/06 (inherited, not recomputed). Portfolio-level Sharpe/Sortino/IR/TE/VaR/CVaR/drawdown, correlation matrix, and sector weights are N/A — no weights exist to aggregate; emitting sleeve-level analytics as if sized would fabricate a book that was never proposed.

## Excluded-Name Rationale

Every eligible name outside the published 23: below the top-20 adjusted-score cut or outside carry-forward bindings (near-miss list in 05). Every published name: excluded from investability by the family-coverage gate alone.
