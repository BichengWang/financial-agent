# 07 Portfolio Proposal — 2026-07-27

## Decision: `NO_TRADE`

**No weights are proposed.** The Task-0 constraint-feasibility pre-check required by
`agents.md § Portfolio Construction` failed before any sizing, so per that stage's own instruction the
run recommends `NO_TRADE` immediately with the computed evidence rather than drafting weights and
burning the revision pass.

## Task 0 — Constraint Feasibility Pre-Check

`rules.md § Risk Controls` requires portfolio beta to SPY in **0.90–1.10** with a **5% single-name
cap**. A long book whose weights sum to 1.00 under a 5% cap therefore holds **at least 20 names**, and
its maximum attainable beta is the mean of the 20 highest available betas.

| Pool | n | Max attainable portfolio beta | vs 0.90 floor |
|---|---:|---:|---|
| Published monitoring sleeve, 10 highest-beta names | 24 | +0.2044 | **infeasible** |
| Published sleeve, equal-weight top-10 by rank | 10 | -0.2838 | **infeasible** |
| **Entire ≥80th-percentile pool, 20 highest-beta names** | **103** | **+0.8519** | **infeasible** |
| Highest single-name beta anywhere in the ≥80th-pctl pool | — | +1.5300 | one name cannot carry a book |

**The band is unreachable, not merely awkward.** Even granting the counterfactual that the family-
coverage gates were cleared and all 103 names at or above the 80th percentile were
investable, the most aggressive legal weighting reaches beta
+0.8519 — short of the 0.90 floor. Holding
fewer names cannot help: it would breach the 5% single-name cap, and any cash weighting lowers beta
further.

**Root cause.** 41.25% of the 514-name universe carries
negative 60-day beta (L015), and this run's leaderboard is a low-beta defensive screen by construction
(L053). The names that score best are structurally the ones with the least market exposure. This is
the same mechanism the 2026-07-24 package documented; the negative-beta share has not receded.

Per `rules.md § Stop Criteria`, this is **`NO_TRADE` #6** — "publishing would require … violating the
beta band; the investable set is structurally infeasible" — and explicitly *not* `HALTED` #5, because
the cause is the composition of the candidate set, not process or data integrity.

## Portfolio Analytics — Computed as Evidence, Not as a Proposal

`rules.md § Computed Risk Analytics` forbids `N/A - no validated engine` when history is fetchable, so
these are computed for the equal-weight top-10 sleeve to show exactly which caps bind. **This is a
diagnostic, not a recommendation, and no position is taken.**

| Analytic | Value | Cap | Status |
|---|---|---|---|
| Portfolio beta to SPY | **-0.2838** | 0.90 – 1.10 | **BREACH** (below floor) |
| Average pairwise correlation | 0.2784 | < 0.45 | passes |
| Highest pairwise correlation | 0.9454 (UNP/NSC) | — | crowding flag: two Class-I rails |
| Portfolio sigma, 1 month | 4.71% | — | from the fetched 60-day covariance matrix |
| 95th-pctl 1-month drawdown | 7.77% | ≤ 8% | passes (parametric, `1.65 × σ`, normality assumed) |
| Largest sector share | Industrials 60% | ≤ 30% | **BREACH** |
| Expected residual return (mean `mu`) | +6.00% | — | L027 |
| Mean tracking error, 1 month | 7.93% | — | L016 |
| Implied sleeve IR | 0.7571 | — | `mu / TE`, L016, L027 |
| `0.25 × Kelly` cap-binding names | 10 of 10 | 5% NAV | all cap-bound; none has `0.25 × Kelly ≤ 0` |

**Two caps breach and two pass.** Notably, correlation (0.2784) and drawdown
(7.77%) are comfortably inside their limits — this sleeve is genuinely well-diversified and
low-risk. What disqualifies it is the *beta floor* and *sector concentration*, i.e. it is too
defensive and too concentrated in Industrials, not too risky. Stating that precisely matters: the
blocker is a mandate-fit problem, not a risk-control failure.

### Correlation Matrix — top-10 sleeve, 60-day daily returns (L003, L015)

| | TRV | RTX | PAYX | DGX | UNP | PCG | CSX | TMO | NSC | WELL |
|---|---|---|---|---|---|---|---|---|---|---|
| **TRV** | 1.00 | 0.18 | 0.20 | 0.38 | 0.36 | 0.16 | 0.22 | -0.00 | 0.35 | 0.48 |
| **RTX** | 0.18 | 1.00 | -0.00 | 0.52 | 0.22 | -0.04 | 0.24 | 0.40 | 0.27 | 0.17 |
| **PAYX** | 0.20 | -0.00 | 1.00 | 0.14 | 0.16 | -0.00 | -0.01 | 0.17 | 0.10 | 0.07 |
| **DGX** | 0.38 | 0.52 | 0.14 | 1.00 | 0.46 | 0.01 | 0.45 | 0.63 | 0.47 | 0.43 |
| **UNP** | 0.36 | 0.22 | 0.16 | 0.46 | 1.00 | 0.12 | 0.82 | 0.25 | 0.95 | 0.38 |
| **PCG** | 0.16 | -0.04 | -0.00 | 0.01 | 0.12 | 1.00 | -0.00 | 0.02 | 0.12 | 0.46 |
| **CSX** | 0.22 | 0.24 | -0.01 | 0.45 | 0.82 | -0.00 | 1.00 | 0.34 | 0.85 | 0.27 |
| **TMO** | -0.00 | 0.40 | 0.17 | 0.63 | 0.25 | 0.02 | 0.34 | 1.00 | 0.25 | 0.15 |
| **NSC** | 0.35 | 0.27 | 0.10 | 0.47 | 0.95 | 0.12 | 0.85 | 0.25 | 1.00 | 0.37 |
| **WELL** | 0.48 | 0.17 | 0.07 | 0.43 | 0.38 | 0.46 | 0.27 | 0.15 | 0.37 | 1.00 |

The UNP/NSC pair at 0.9454 is the one genuine crowding flag: both are Class-I railroads
responding to the same freight cycle. In a sized book they would need to be treated as one position.

### Sector Concentration — full published sleeve

| Sector | Names | Share |
|---|---:|---:|
| Industrials | 10 | 41.7% |
| Finance | 4 | 16.7% |
| Energy | 3 | 12.5% |
| Health Care | 3 | 12.5% |
| Consumer Discretionary | 1 | 4.2% |
| Consumer Staples | 1 | 4.2% |
| Real Estate | 1 | 4.2% |
| Utilities | 1 | 4.2% |

### Factor Exposure Summary

| Exposure | Reading |
|---|---|
| Technical / Price | dominant — 0.30 of 0.45 available weight (66.7%), which trips Evidence Threshold #3 |
| Macro / Regime | 0.15 of 0.45 (33.3%), defensive polarity (L053) |
| Fundamental | `UNAVAILABLE` (L046) |
| Sentiment / Positioning | `UNAVAILABLE` (L047) |
| Factor crowding flag | **fires** — more than half the conviction loads on one family |

## Excluded Names and Why

| Group | Count | Reason |
|---|---:|---|
| Below the 60th-percentile ranking floor | 308 | not ranked in either sleeve; rejection log only (`rules.md § mu Calibration Table`) |
| Ranked but outside the 24-name publication cut | 182 | carry `mu`/`sigma` in `run_computed_manifest.json` but are not published as forecasts |
| Earnings never grounded, inside the top-30 | 8 | AON, ESS, ITW, WM, JNJ, DUK, CTVA, AMP — entered the top-30 only after the bounded earnings passes converged; **excluded rather than scored penalty-free** |
| Failed a universe filter | 1 | FDXF — see `04` |

## Per-Position Recommendation Metrics

**Not applicable — no positions.** Every name's full metric block (entry, price date, tag, target,
target date, `mu`, `sigma`, sigma source, Sharpe, Sortino, IR, `0.25 × Kelly`, VaR95, CVaR95,
MaxDD60, TD-9 D/W/M, RSI14 D/W/M, MACD D/W/M, both CI bounds, score trace, ledger rows) is published
in `05_factor_scores.md` for the monitoring sleeve. Nothing was recomputed here; no value in this
artifact is new.
