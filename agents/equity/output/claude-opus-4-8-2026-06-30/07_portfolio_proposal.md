# 07 Portfolio Proposal — NO_TRADE (Constraint-Infeasible)

Run `claude-opus-4-8` · 2026-06-30 · **No portfolio is published.** This artifact documents the mandatory constraint-feasibility pre-check and the computed evidence for `NO_TRADE`.

## Constraint Feasibility Pre-Check (before any sizing)

Per `agents.md § Portfolio Construction Task 0` (Track B, 2026-06-10, HUMAN_REVIEW), the achievable sleeve-beta range and sector shares of the investable set are computed from already-fetched inputs **before** drafting weights.

### Two independent NO_TRADE triggers

**Trigger A — investable count < 5 (NO_TRADE #1).** Only **4 names** clear the full investability gate (UNH, V, LLY, BAC; 05 §Investability Gate). The minimum investable set is 5. The other four ≥80th-pctl names (AMD, CAT, MU, GE) fail the "no single family > 50% of conviction" rule — they are momentum-only, and three are exhausted high-beta semis/cyclicals (TD9-9, RSI 86–92, beta 1.9–4.2). Forcing them in to reach a count would violate the gate and "prefer fewer names over lower-quality names."

**Trigger B — beta band infeasible under the protected 5% cap (NO_TRADE #6).** Portfolio beta to SPY must be in **[0.90, 1.10]**. Maximum achievable long-only beta under the 5% single-name cap (put 5% on each positive-beta investable name; `max Σ wᵢβᵢ`, wᵢ ≤ 0.05):

| Candidate set | Max achievable portfolio beta (5% cap) | vs 0.90 floor |
|---|---|---|
| Full-gate investable (UNH, V, LLY, BAC) | **0.027** | infeasible (−0.87) |
| All ≥80th-pctl (8 names, incl. AMD/MU/CAT/GE) | **0.588** | infeasible (−0.31) |
| All ranked ≥60th-pctl (15 names) | **0.751** | infeasible (−0.15) |
| 20 highest-adj names equal-weight 5% | 0.897 | only reaches floor by sizing **sub-investable-grade** names (gate violation) |

The investable-grade quality names all have **low or negative 60d beta** (UNH −0.16, V −0.01, LLY 0.22, BAC 0.32; L202) because, over the trailing 60 sessions, defensives rallied while SPY chopped/rotated — a rotation-distorted realized beta. The only high-beta names are the exhausted semis (MU 4.16, AMD 3.87) and cyclicals (CAT 1.93, GE 1.25), which fail the quality gate. **There is no 5–10-name combination of investable-grade names that lands in [0.90, 1.10].** This is a structural infeasibility of the *investable set's composition* (→ NO_TRADE), not a data/process-integrity failure (which would be HALTED).

### Other constraints (not binding — confirms beta is the sole blocker)

| Constraint | Cap | Computed (investable-grade set) | Status |
|---|---|---|---|
| Avg pairwise correlation | < 0.45 | **0.05** (UNH/V/LLY/BAC, 60d) / 0.08 (top-8) | far inside |
| Single-name weight | ≤ 5% | feasible | inside |
| Sector concentration | ≤ 30% | Financials 2, Health Care 2 of 4 (50% Health Care if only 4) | would bind at small N, moot |
| 95th-pctl 1m drawdown | ≤ 8% | low (σ-weighted; all low-vol names) | inside |

Correlation, drawdown, and single-name caps are all satisfiable — only the **beta floor** is infeasible. A book of these uncorrelated low-beta quality names would be a fine *low-beta* portfolio (~0.03–0.20 beta), but that is outside the mandated band and the band may not be relaxed by autonomous mutation (`rules.md § Protected Rules` item 5).

## Why not force a portfolio

- Adding the exhausted high-beta semis (MU/AMD) purely as beta ballast would (a) violate the investability gate they already failed, (b) blow up portfolio σ and tail risk (MU VaR95 −55%, CVaR95 −69%), and (c) concentrate Information Technology > 30% (MU+AMD+… semis). Rejected.
- Levering the low-beta book to raise beta is not available (long-only, no leverage in scope) and would not change beta (cash/leverage scales exposure, the band is on realized beta to SPY).
- The honest output is **NO_TRADE**: the inputs are valid and a high-quality *thesis* exists, but no constraint-compliant sized portfolio does.

## What a (non-compliant) expression of the thesis would have been

For the record only — **not published, not sized**: an equal-weight low-beta quality basket UNH/V/LLY/BAC (+ monitoring SO/LIN/JPM) would carry expected book σ ≈ 4–5% (1m), avg pairwise corr ≈ 0.05, portfolio beta ≈ 0.10, and a blended mu ≈ +4.5% — attractive on a *standalone* risk-adjusted basis but rejected by the 0.90 beta floor. These names are published instead as **paper monitoring forecasts** (15) so the thesis is settled on 2026-07-28.

## Failure Rule Invoked

Constraints cannot be met without dropping below the minimum investable count or breaching the protected beta band → **NO_TRADE** (never force a portfolio). Escalation to the risk committee (08) for confirmation, and to evolution (13) because this is the **16th consecutive cross-model NO_TRADE in this environment** driven by the same beta-band-vs-rotation mechanism — a structural calibration signal, not a one-day result.
