# 07 Portfolio Proposal — 2026-07-20 (claude-fable-5)

## Constraint Feasibility Pre-Check (Task 0 — before any sizing)

**Result: NO_TRADE. No weights drafted; the revision pass is not spent.**

1. **Structural family gate (binding):** the investable set is empty before construction — evidence threshold #2 (≥3 of 4 non-negative families) cannot be met with Fund_Z/Sent_Z UNAVAILABLE universe-wide (L012). 15th consecutive scoring run; escalation standing in 13.
2. **Beta band infeasibility (computed evidence):** published top-20 60d betas: mean **+0.103**, min −0.758, max +0.691, 15/20 below 0.5 (run_computed_manifest.json). A 0.90–1.10 sleeve beta is unreachable from this cross-section under the 5% single-name cap without diluting into names that fail the rank bar — the same failure mode the 06-10 vintage demonstrated.
3. **Event concentration (downgrade trigger #4):** 12 of 33 published names carry earnings inside the buffered 14-day window (CSX/MCO 2d, UNP/SNA/WST 3d, UPS/IQV 8d, ADP/CHRW 9d, AAPL 10d, FRT 11d, MNST est. 17d≤19 buffer) — far past the >2-name trigger.
4. Correlation is NOT a blocker: top-10 mean pairwise 60d correlation 0.208 < 0.45 cap.

## Per-Position Recommendation Metrics

Inherited unchanged from 05's ranked table (33 rows, full blocks: entry/target/CI/mu/sigma/Sharpe/Sortino/IR/Kelly/VaR/CVaR/DD/TD9/RSI/MACD/traces/ledger rows). No recomputation performed here.

## Portfolio-Level Analytics

Not computed — no portfolio exists. Feasibility evidence above is the required output for a NO_TRADE recommendation (rules.md §Portfolio Construction Task 0). Portfolio sigma/VaR/drawdown formulas stand ready per §Computed Risk Analytics when a sleeve becomes constructible.

## Excluded-Name Rationale

Every scored name is excluded from positioning by the structural gate. Within the published sleeve, the notable exclusions from any hypothetical book: the 12 earnings-window names (event gate), TRV/ADP/PAYX/KHC/MET (negative or near-zero betas — band infeasibility drivers), CTAS/IQV/JBHT (rvol ≥ 10.2% with penalty-adjusted mu ≤ +6% → weakest mu/sigma). ABBV/HUM/DVA/MCK/LIN: not published (05 rejection log, 04 disclosure).
