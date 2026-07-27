# 07 Portfolio Proposal — 2026-07-27

## Decision

**`NO_TRADE`. No portfolio is proposed and no weights were drafted.**

Per `agents.md § Portfolio Construction Agent — Task 0` (Track B, 2026-06-10, `HUMAN_REVIEW`), the constraint feasibility pre-check runs **before any sizing**. It fails on the beta band. Combined with an empty investable set, this run recommends `NO_TRADE` immediately and spends none of its revision budget.

## Task 0 — Constraint Feasibility Pre-Check

Computed from already-fetched inputs (L016, L021, L141, L142). No optimizer was run.

### Beta band — **INFEASIBLE**

`rules.md § Risk Controls` requires portfolio beta to SPY between **0.90 and 1.10** (a protected rule). Maximum attainable sleeve beta is `Σ 0.05 × β_i` over the highest-beta names available, under the 5% single-name cap:

| Candidate set | Max attainable beta @ 5% cap | Required band | Verdict |
|---|---|---|---|
| Top-10 ranked | **−0.1593** | 0.90 – 1.10 | **INFEASIBLE** |
| Best 10 of the 24 published | **+0.1038** | 0.90 – 1.10 | **INFEASIBLE** |
| Best 20 of the 24 published | **−0.1272** | 0.90 – 1.10 | **INFEASIBLE** |

The gap is not marginal — the best case falls short of the band's lower edge by roughly **0.80 beta**. There is no weighting of this candidate set that reaches 0.90.

**Root cause (L142):** **212 of 514 names (41.2%) carry negative 60-day beta**, and the scoring architecture's disclosed defensive Macro polarity (L140) actively rewards low beta. The ranking therefore concentrates precisely in the names that cannot carry a compliant book. The published set averages **−0.247** beta with **19 of 24 names negative**.

| Ticker | 60d Beta | Ticker | 60d Beta | Ticker | 60d Beta |
|---|---|---|---|---|---|
| PKG | +0.8111 | WAB | +0.8056 | BNY | +0.5661 |
| CSX | +0.1130 | TMO | +0.0977 | MET | -0.0057 |
| GD | -0.0187 | RTX | -0.0609 | NSC | -0.0999 |
| EQR | -0.1333 | UNP | -0.1639 | PCG | -0.2596 |
| CTAS | -0.2905 | MPC | -0.4388 | LMT | -0.4594 |
| PM | -0.5405 | HIG | -0.5748 | DGX | -0.5759 |
| PAYX | -0.6143 | TRV | -0.7014 | VLO | -0.7372 |
| SJM | -0.7559 | WRB | -0.9218 | CB | -0.9767 |

**For completeness:** the *unconstrained* universe can reach the band — the 20 highest-beta names in the 514 would produce +4.07 at a 5% cap, far above it. The band is reachable only by selecting names that do not clear the score threshold. That is exactly the trade-off `NO_TRADE` #6 exists to prevent: "publishing would require overconcentration in one sector or factor family, or violating the beta band — the investable set is structurally infeasible."

### Sector concentration — **BREACH**

`rules.md § Risk Controls`: maximum **30%** in one GICS sector (a protected rule). Under equal weighting of the 24 published names (L021):

| GICS Sector | Names | Share under equal weight | vs 30% cap |
|---|---|---|---|
| Industrials | 9 | 37.5% | **BREACH** |
| Financials | 6 | 25.0% | ok |
| Health Care | 2 | 8.3% | ok |
| Energy | 2 | 8.3% | ok |
| Consumer Staples | 2 | 8.3% | ok |
| Utilities | 1 | 4.2% | ok |
| Real Estate | 1 | 4.2% | ok |
| Materials | 1 | 4.2% | ok |

Industrials breach the cap before any optimizer runs. This is fixable by dropping names — unlike the beta failure — but it compounds it: trimming Industrials removes the very names carrying the strongest `Tech_Z`.

### Average pairwise correlation — **PASS**

`rules.md § Risk Controls`: average pairwise correlation must remain **below 0.45**.

| Set | Avg pairwise correlation (60d daily returns) | Cap | Verdict |
|---|---|---|---|
| Top-10 ranked | **0.2749** | < 0.45 | **PASS** |

This is the one portfolio constraint the set satisfies comfortably. It is worth reading carefully rather than as good news: low pairwise correlation alongside a −0.247 average beta and a single dominant factor means these names are *individually* diversified in daily noise while sharing one large directional macro exposure. Correlation of residuals is not the same as diversification of the bet.

### Event concentration — **BREACH**

`rules.md § Downgrade to NO_TRADE` #4: more than **2** names with earnings inside 14 calendar days.

| Name | Next earnings | Days | Source |
|---|---|---|---|
| GD | 2026-07-29 | 2 | CONFIRMED (L022) |
| VLO | 2026-07-30 | 3 | CONFIRMED (L022) |
| MPC | 2026-08-04 | 8 | CONFIRMED (L022) |
| MET | 2026-08-05 | 9 | CONFIRMED (L022) |
| HIG | print week | ≤ 19 buffered | `ESTIMATED_PRINT_WEEK (±5d)` (L024) |

**5 names against a limit of 2** — an independent `NO_TRADE` trigger even if beta, sector and the family gap were all resolved.

## Constraint Summary

| Constraint | Limit | Achievable | Status |
|---|---|---|---|
| Investable count | ≥ 5 names | **0** | **FAIL** |
| Portfolio beta to SPY | 0.90 – 1.10 | max **−0.159** (top-10) | **FAIL** |
| Max single-name weight | 5% | n/a | not reached |
| Max sector concentration | 30% | Industrials **37.5%** | **FAIL** |
| Avg pairwise correlation | < 0.45 | **0.275** | PASS |
| 95th-pctl 1-month drawdown | ≤ 8% | not computed — no portfolio exists to compute it on | n/a |
| Names with earnings ≤ 14d | ≤ 2 | **5** | **FAIL** |

**Four independent failures.** Any one of them alone forces `NO_TRADE`.

## Portfolio Analytics

**Not computed — deliberately, and this is not an `N/A - no validated engine` evasion.**

`rules.md § Computed Risk Analytics` requires beta, pairwise correlation, portfolio sigma, 95th-percentile drawdown, tracking error, VaR/CVaR and 60-day max drawdown to be *computed* whenever price history is fetchable, and forbids emitting portfolio-level `N/A` when the fetch succeeds. The fetch did succeed, and the analytics that constrain the decision **are** computed and published above: beta per name (L016), max attainable sleeve beta (L141), the 60-day correlation matrix summary, per-name tracking error, VaR95/CVaR95, max DD60 and Sharpe/Sortino/IR — all in `05` for all 24 names.

What is absent is *portfolio-level* aggregation, and that is absent because **there is no portfolio**: weights were never drafted, since Task 0 mandates stopping before sizing when the pre-check fails. Aggregating `w'Σw` over a weight vector that does not and cannot exist would be a fabricated number, not an analytic.

## Excluded Names

| Group | Count | Rationale |
|---|---|---|
| Entire investable set | 0 published | No name clears evidence thresholds #2 and #4; 22 of 24 also breach #3 |
| 6 third-pass entrants (MTB, AON, ESS, ITW, WM, JNJ) | excluded from publication | Entered only after the bounded second earnings pass; excluded by process control. Audit-only current lookups are not introduced after the pass limit |
| 8 prior-vintage names (CAT, GOOGL, FCX, SHW, GS, GE, CVX, EQIX) | rejection log | Below the 60th-percentile ranking floor; `DROP` per `02 § 5` |
| 490 remaining universe names | not ranked or below cut | Below the top-30 publication cut or below the 60th-percentile floor |

## Recommendation to Risk Committee

**Publish `NO_TRADE`.** The investable set is empty on evidence grounds, and the ranked set is separately infeasible on beta, sector concentration and event concentration. No revision pass is requested — a second pass cannot manufacture a fundamental or sentiment factor, and cannot move a −0.159 maximum attainable beta into a 0.90–1.10 band.
