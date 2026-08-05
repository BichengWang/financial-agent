# 07 — Portfolio Proposal — 2026-08-04

## Outcome: **no portfolio proposed** — `NO_TRADE`

The investable set is **empty** (0 names clear the Evidence Thresholds), so
`agents.md § Portfolio Construction — Failure Rule` applies: recommend `NO_TRADE`, never force a
portfolio. No weights are drafted and the single revision pass is **not** spent.

## Task 0 — constraint feasibility pre-check (run before any sizing)

Per `agents.md § Portfolio Construction` task 0 (Track B, 2026-06-10), feasibility is computed from
already-fetched inputs *before* sizing. The 5% single-name cap forces **≥20 names**, so the
attainable sleeve-beta range is bounded by the mean of the 20 highest and 20 lowest betas in the
pctl≥80 pool.

| Constraint | Attainable range / value | Cap | Feasible? |
|---|---|---|---|
| Sleeve beta to SPY | [-0.5413, +1.3472] | 0.90 – 1.10 | **FEASIBLE** |
| Pool size (pctl ≥ 80) | 103 names | ≥ 20 required by the 5% cap | **FEASIBLE** |

**The beta band is feasible — for the fifth consecutive run.** The "provably infeasible" narrative
from 2026-07-27 would be wrong here and is not reused; feasibility is recomputed every run.
`NO_TRADE` is driven by evidence breadth, not by constraint geometry.

## Naive top-20 equal-weight reference sleeve (diagnostic, not a proposal)

Constructed only to show where a rank-ordered sleeve *would* land against the hard caps. It is not
proposed, and no name here is investable.

| Portfolio metric | Value | Cap (`rules.md § Risk Controls`) | Result |
|---|---|---|---|
| Expected beta to SPY | +0.5323 | 0.90 – 1.10 | **FAIL** — far below the floor |
| 95th-pctl 1-month drawdown | 8.50% | ≤ 8% | **FAIL** |
| Average pairwise correlation | 0.1482 | < 0.45 | PASS |
| Max sector concentration | 30.0% | ≤ 30% | PASS (at the cap) |
| Portfolio sigma (1-month) | 5.15% | — | input to the drawdown estimate |

Two caps fail **independently of the evidence thresholds**: the sleeve's beta of
+0.5323 sits far below the 0.90 floor, and the 95th-percentile drawdown of
8.50% breaches the 8% cap. Either alone is a `NO_TRADE` trigger
(`rules.md § Downgrade to NO_TRADE` #5 and #6). Note the tension this exposes: the attainable beta
range comfortably contains the band, but **rank-ordered selection walks straight out of it** — the
score keeps picking low-beta defensives.

Drawdown method: parametric `1.65 x portfolio_sigma_1m`, where portfolio sigma is
`sqrt(w' Σ w) x sqrt(21)` from the 60-day fetched adjusted-return covariance matrix, equal weights.
Normality is assumed and stated.

## Sector table (naive sleeve)

| Sector | Weight | vs 30% cap |
|---|---|---|
| Health Care | 30.0% | PASS |
| Finance | 20.0% | PASS |
| Consumer Discretionary | 20.0% | PASS |
| Technology | 20.0% | PASS |
| Industrials | 10.0% | PASS |

## Per-position recommendation metrics

**Not applicable** — no positions are proposed. The full per-name metric block for every monitored
name (entry, target, CI, mu, sigma, Sharpe, Sortino, IR, Kelly, VaR/CVaR, drawdown, TD-9, RSI, MACD,
score trace, ledger rows) is published in `05_factor_scores.md` and `06_top_candidates.md`, and every
name carries a settleable record in `15_predictions.json`.

## Excluded-name rationale

| Exclusion class | Count | Rationale |
|---|---|---|
| All scored names | 512 | no name clears Evidence Thresholds 2/3/4; the investable set is empty by construction |
| Names below the 60th percentile | 307 | below the mu Calibration Table floor — not ranked in either sleeve |
| Names rejected pre-scoring | 3 | universe filters — see `04` rejection log |
