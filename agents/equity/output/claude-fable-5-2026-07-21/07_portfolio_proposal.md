# 07 Portfolio Proposal — 2026-07-21 (claude-fable-5)

## Task 0 — Constraint Feasibility Pre-Check (before any sizing)

Per `agents.md § Portfolio Construction Agent Prompt` Task 0 (Track B, 2026-06-10, HUMAN_REVIEW): compute the investable set's achievable sleeve-beta range and per-sector shares under the single-name cap **before** drafting any weights.

- **Investable set is empty** (see `05` — evidence threshold #2 unsatisfiable). There is no set to size.
- Even treating the top-20 monitoring sleeve as a hypothetical candidate pool for feasibility purposes: **mean beta −0.175**, range [−0.973, +0.732], with 10 of 20 names carrying `|beta| < 0.5`. The required portfolio beta band is **0.90-1.10**. No feasible weighting of this candidate pool — long-only, single-name capped at 5% — can bring portfolio beta within 30-plus points of the required band; the pool is structurally low-beta/defensive by construction (that is exactly what the current Macro_Z proxy rewards in a NEUTRAL/HIGH_VOL-watch regime).
- **Earnings concentration:** 5 of the top-20 names carry earnings inside the buffered window (ADP, EG, UNP, DOC, PSX) — exceeds the 2-name NO_TRADE downgrade trigger (`rules.md § Downgrade to NO_TRADE` #4) independently of the beta-feasibility finding.

**Recommendation: NO_TRADE, immediately, without drafting weights or spending the revision pass** — per Task 0's explicit instruction and `rules.md § Portfolio Construction Agent Prompt § Failure Rule`.

## Required Output (N/A — no portfolio drafted)

Weights, expected Sharpe/Sortino/IR/tracking error/expected beta/VaR95/CVaR95/95th-pctl drawdown, sector concentration table, factor exposure summary, and correlation matrix are all **N/A** — a portfolio was never drafted because the feasibility pre-check failed before any sizing step, and because the underlying investable set is structurally empty (evidence threshold #2, `05`).

## Excluded-Name Rationale

Every name in the eligible universe is excluded from any `GO` portfolio for the same structural reason: Fund_Z and Sent_Z are UNAVAILABLE for scoring universe-wide, so no name can ever satisfy "≥3 of 4 factor families non-negative." This is disclosed once here rather than repeated per name.

## Grounding Notes

Beta, 30d realized vol, and 60d drawdown were computed and are ledger-backed (`01`, `05`) for all 513/514 eligible names with sufficient history — the `N/A - no validated engine` state that `rules.md § Computed Risk Analytics` prohibits does **not** apply here; the analytics exist, they simply describe a portfolio that cannot meet the beta band.
