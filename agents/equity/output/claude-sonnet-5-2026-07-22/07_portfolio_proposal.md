# 07 Portfolio Proposal — 2026-07-22

## Constraint Feasibility Pre-Check (Task 0)

**Investable set size: 0.** Per `agents.md § Portfolio Construction Agent Prompt` Task 0, the constraint-feasibility pre-check must run before any weights are drafted. With zero names clearing `INVESTABLE_GRADE` (see `05_factor_scores.md` — evidence threshold #2, "at least 3 of 4 factor families non-negative," is structurally unreachable while Fund_Z/Sent_Z remain `SHADOW`-only), there is no feasible beta band, sector allocation, or correlation structure to compute a portfolio over. Per `rules.md § Stop Criteria`, "Downgrade to NO_TRADE" condition #1 ("Fewer than 5 names pass the investable threshold") applies immediately and mechanically — **no weights are drafted, and no revision pass is spent** on this run, consistent with the Task 0 instruction to recommend `NO_TRADE` immediately with computed evidence rather than proceed to sizing.

## Secondary Infeasibility Evidence (informational, not the binding cause)

Even setting aside the family-coverage gate, the 26-name monitoring sleeve published in `05`/`06` would face at least one hard-cap breach if ever treated as a candidate set:

- **Sector concentration:** Financials represent 8 of 26 names (30.8%) — TRV, SCHW, MCO, USB, MTB, BAC, JPM, V — already at or above the 30% single-sector cap (`rules.md § Risk Controls`) before any weighting is applied, and before considering that a cap-respecting subset would still need to clear beta and correlation constraints.
- **Earnings concentration:** 13 of 26 names carry an earnings-window penalty this cycle (event risk inside 14 calendar days, several confirmed for tomorrow — TMO). `rules.md § Downgrade to NO_TRADE` condition #4 flags event risk as too concentrated above 2 names with earnings inside 14 days; this sleeve is far past that threshold.
- **Elevated realized vol / beta:** several of the highest-scoring names (CRWD sigma 15.9%, PANW sigma 15.7%) sit inside the semiconductor/growth high-vol pocket flagged in `03_regime_and_data.md`, which would pressure both the portfolio drawdown estimate and the 0.90–1.10 beta band if a broad-beta name like a bank (BAC beta 0.24, JPM beta 0.30) had to offset them.

None of this changes the outcome — the family-coverage gate alone is sufficient and binding — but it is disclosed because a future run that promotes Fund_Z/Sent_Z (per `rules.md § SHADOW Diagnostic Tooling` Phase 2) should not assume today's top-ranked-by-technical-score names would automatically form a feasible portfolio.

## Required Output

- **Weights:** none published (no investable set).
- **Expected Sharpe/Sortino/IR/tracking error/beta/VaR95/CVaR95/95th-pctl drawdown:** `N/A — no candidate set` (not `N/A - no validated engine`; the computation engine itself is fully validated and was exercised for every individual name in `05`/`06` — there is simply nothing to aggregate into a portfolio).
- **Sector concentration table / factor exposure summary / correlation matrix:** not computed — would require an investable set as the input.
- **Excluded-name rationale:** every name in the 514-name scored universe is excluded from `INVESTABLE_GRADE` for the identical structural reason (evidence threshold #2); per-name exclusion detail for the top-ranked names is in `05_factor_scores.md § Score Attribution` and `§ Near-miss rejection list`.

## Failure Rule Applied

Per `rules.md § Portfolio Construction Agent Prompt § Failure Rule`: "If constraints cannot be met without dropping below the minimum investable count, recommend `NO_TRADE` — never force a portfolio." Recommendation: **`NO_TRADE`**.
