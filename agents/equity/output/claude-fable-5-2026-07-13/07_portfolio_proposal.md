# 07 Portfolio Proposal — 2026-07-13

## §0 Constraint Feasibility Pre-Check (before any sizing)

Input: the investable set from 05 — **empty** (family-coverage gate: 2/4 sourceable families means no name meets evidence threshold #2). Per the pre-check rule (Track B, 2026-06-10) and rules.md §Stop Criteria Downgrade #1 (fewer than 5 investable names), the run goes **NO_TRADE without drafting weights** — no revision pass is spent.

Documentation of the counterfactual (from already-fetched inputs, no new facts): had the family gate not bound, the top-10 by Adj Score carries a weighted 60d beta ≈ 0.66 (range -0.16 AIZ to 1.40 CRWD; 8 of 10 below 0.90) — the sleeve-beta range achievable under the 5% single-name cap is ~0.5-0.9, **below the protected 0.90 floor** without adding the event-gated banks or high-beta growth names the score ranks lower; sector shares at equal weight would put Health Care ≈ 30% at the cap boundary. The construction infeasibility is composition-driven (defensive leaderboard), the same shape as the 06-10 baseline's NO_TRADE — this is a persistent regime artifact, not noise.

## Positions

None. No weights table is emitted on a NO_TRADE run; emitting an empty-but-formatted portfolio would misrepresent a decision as an omission.

## Per-Position Recommendation Metrics

Not applicable (no positions). The 24 monitoring-sleeve Recommendation Metrics Blocks — entry/target/CI/mu/sigma/ratios/Kelly/indicator states with ledger rows — are published in full in the 05 ranked table and `15_predictions.json`; nothing is recomputed here.

## Portfolio Analytics

Not computed — no portfolio exists. Beta/correlation/drawdown engines ran at the name level (L0xx rows) and are available: this is a construction abstention, not an `N/A - no validated engine` state.

## Excluded-Name Rationale

Every scored name is excluded for exactly one of: (1) family-coverage gate (all 24 published names — evidence threshold #2 unreachable at 2/4 families); (2) event gate (UNH, GE, banks wave 07-14..07-17 — confirmed prints ≤4d); (3) sub-60 percentile floor (rejection-log names incl. the 8 confirmed DROPs); (4) rank cut (NTAP/SWK/ZBRA/MNST at 95.5-96.1 pctl, outside top-20 + carry-forward publication set).
