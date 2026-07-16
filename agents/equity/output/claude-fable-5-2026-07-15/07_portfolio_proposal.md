# 07 Portfolio Proposal — 2026-07-15

## §0 Constraint Feasibility Pre-Check → NO_TRADE (no sizing pass spent)

Per the Track B pre-check (2026-06-10, HUMAN_REVIEW): before any weight drafting, test whether an investable set exists and whether the hard caps are jointly feasible.

**Gate 1 — investable set exists: FAIL.** Evidence threshold #2 (≥3 of 4 factor families non-negative) is unmeetable with Fund_Z and Sent_Z `UNAVAILABLE` universe-wide (04, 05). Investable count = 0 < 5 minimum → **NO_TRADE** under Downgrade rule #1. This is the structural gate, 13th consecutive scoring run — unchanged since 07-01 and unresolvable at run level (standing HUMAN_REVIEW in 13).

**Gate 2 — caps feasibility (academic, for the record):** had the 2-family standard been accepted, the top-20 sleeve would still be event-compromised today: six of the top twenty (FFIV, FTNT, STT, WST, GS, MS, ELV) sit inside earnings windows — Downgrade rule #4 (max 2 names with earnings inside 14d) binds long before the beta band would. The non-event residue (DVA, CRWD, CVS, CRL, EXPD, NTAP, MPC, MNST, PANW, RVTY, GEN, DOC, DDOG) spans sleeve-beta ≈ −0.65 to +1.53 with healthcare-services concentration near the 30% sector cap — a constrained book would be buildable on that residue, but no such book is proposed while the family gate fails.

## Required Outputs (per runbook, under NO_TRADE)

- **Weights:** none — no portfolio is proposed.
- **Portfolio-level analytics:** N/A — no weights exist to aggregate. Per-name Sharpe/Sortino/IR/VaR95/CVaR95/Kelly/DD60 for every monitoring-sleeve name: 05 ranked table (formulas in 05 header; ledger rows per name).
- **Correlation matrix / sector table:** not computed for a non-existent book; the 60d return matrix for the published 24 is reproducible from the fetched history (L002) on demand.
- **Excluded names:** the entire ranked set is excluded from sizing by Gate 1; event-window names additionally by Gate 2. Sub-threshold and DROP names: 05 §Near-miss rejection list and 02 §5.

## Kelly / Cap Notes

All 24 published names carry `0.25 × Kelly` capped at 0.050 (the 5% single-name NAV cap binds for every name — raw Kelly range ≈ 1.1–22.8 at these mu/sigma pairs). No position was sized; the caps are reported so the monitoring-sleeve forecasts remain fully specified for future settlement.
