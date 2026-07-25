# 07 Portfolio Proposal — 2026-07-24

## Decision: NO_TRADE — no weights proposed

Two **independent** reasons, either sufficient on its own. The second is new evidence produced by this stage and is not merely a restatement of the scoring gap.

## Task 0 — Constraint Feasibility Pre-Check (executed before any sizing)

Per `agents.md § Portfolio Construction Agent § Tasks` #0 (Track B, 2026-06-10): compute the achievable sleeve-beta range and per-sector shares from already-fetched inputs *before* drafting weights. If the beta band or sector caps are infeasible for any weighting, recommend `NO_TRADE` immediately with the computed evidence and do not spend the revision pass.

The pre-check is run on the top 10 ranked names — the set that would form any 5–10 name portfolio.

### Beta band — INFEASIBLE

60-day betas vs SPY (ledger row L140 lineage; `DERIVED`, 60 aligned daily returns):

| Ticker | TRV | PAYX | DGX | UNP | PCG | RTX | NSC | GD | CSX | CTAS |
|---|---|---|---|---|---|---|---|---|---|---|
| Beta | −0.693 | −0.638 | −0.568 | −0.164 | −0.268 | −0.040 | −0.107 | +0.008 | +0.114 | −0.288 |

- **Equal-weight sleeve beta: −0.264.**
- The **highest** beta available in the top 10 is CSX at **+0.114**.
- Required band: **0.90 to 1.10**.

There is no non-negative weighting of these names that reaches 0.90. The maximum attainable beta is bounded above by the largest single beta (+0.114), which is **short of the band's floor by roughly 0.79**. Adding the rest of the 26-name sleeve does not help: the entire published set is drawn from the same low/negative-beta defensive cohort. Fixing this would require importing high-beta names that the scoring ranks in the bottom half of the universe — i.e. weakening the selection to satisfy a risk constraint, which is precisely what `rules.md` forbids ("Never weaken risk limits to force a publishable portfolio", and its converse).

This is the direct portfolio-level consequence of the regime documented in `03`: **40.9% of the universe now carries a negative 60-day beta**, and the rotation has put the best-scoring names entirely inside that group.

### Sector concentration — INFEASIBLE

| GICS Sector | Names | Count | Share of a 26-name equal-weight sleeve | 30% cap |
|---|---|---|---|---|
| Industrials | PAYX, UNP, RTX, NSC, GD, CSX, LMT, TMO | 8 | 30.8% | **BREACH** |
| Finance | TRV, BNY, MTB, MET, HIG, BAC, JPM | 7 | 26.9% | ok |
| UNAVAILABLE | CTAS, PM, AAPL, LLY | 4 | 15.4% | ok |
| Health Care | DGX, UNH | 2 | 7.7% | ok |
| Energy | MPC, VLO | 2 | 7.7% | ok |
| Utilities | PCG | 1 | 3.8% | ok |
| Consumer Discretionary | PKG | 1 | 3.8% | ok |
| Consumer Staples | SJM | 1 | 3.8% | ok |

Industrials is **30.8%** of an equal-weight 26-name sleeve against a **30% hard cap**, and the concentration is far worse in the top 10 that would actually be held: **6 of 10 names (60%) are Industrials** (PAYX, UNP, RTX, NSC, GD, CSX). Bringing Industrials under 30% in a 10-name book means holding at most 3 of them, which forces roughly half the top-10 out of the portfolio and drops the count below the 5-name minimum once the other constraints bind.

### Constraints that do pass

| Constraint | Cap | Computed (top 10, equal weight) | Status |
|---|---|---|---|
| Average pairwise correlation | < 0.45 | **0.261** (max pair 0.945, min −0.038) | **Pass** |
| 95th-pctl 1-month drawdown | ≤ 8% | **7.51%** (`1.65 × portfolio σ₁ₘ`, σ₁ₘ = 4.55%, normality stated) | **Pass** (thin margin) |
| Single-name weight | ≤ 5% | 5% cap binds for every name (`0.25×Kelly` ≫ 0.05 throughout) | **Pass** |
| `0.25 × Kelly > 0` | required | positive for all 26 | **Pass** |

The average pairwise correlation of 0.261 is comfortably inside the cap, but it understates the true shared exposure — every name is an expression of the same defensive-rotation trade, and the single 0.945 pair (the rail names) shows where the crowding sits. Factor crowding is flagged: more than half the sleeve loads on the same low-beta/defensive factor, which `rules.md § Risk Controls` requires be reported.

### Correlation matrix (top 10, 60 aligned sessions, log returns)

| | TRV | PAYX | DGX | UNP | PCG | RTX | NSC | GD | CSX | CTAS |
|---|---|---|---|---|---|---|---|---|---|---|
| **TRV** | 1.00 | 0.21 | 0.40 | 0.37 | 0.17 | 0.19 | 0.36 | 0.06 | 0.23 | 0.26 |
| **PAYX** | 0.21 | 1.00 | 0.14 | 0.16 | 0.01 | -0.00 | 0.11 | 0.24 | -0.01 | 0.50 |
| **DGX** | 0.40 | 0.14 | 1.00 | 0.45 | 0.02 | 0.51 | 0.46 | 0.19 | 0.44 | 0.35 |
| **UNP** | 0.37 | 0.16 | 0.45 | 1.00 | 0.12 | 0.22 | 0.94 | 0.13 | 0.82 | 0.35 |
| **PCG** | 0.17 | 0.01 | 0.02 | 0.12 | 1.00 | -0.04 | 0.13 | 0.06 | 0.00 | 0.20 |
| **RTX** | 0.19 | -0.00 | 0.51 | 0.22 | -0.04 | 1.00 | 0.26 | 0.52 | 0.23 | 0.21 |
| **NSC** | 0.36 | 0.11 | 0.46 | 0.94 | 0.13 | 0.26 | 1.00 | 0.09 | 0.84 | 0.29 |
| **GD** | 0.06 | 0.24 | 0.19 | 0.13 | 0.06 | 0.52 | 0.09 | 1.00 | 0.11 | 0.20 |
| **CSX** | 0.23 | -0.01 | 0.44 | 0.82 | 0.00 | 0.23 | 0.84 | 0.11 | 1.00 | 0.22 |
| **CTAS** | 0.26 | 0.50 | 0.35 | 0.35 | 0.20 | 0.21 | 0.29 | 0.20 | 0.22 | 1.00 |

## Reason 2 — The Investable Set Is Empty

Independently of feasibility, `05`/`06` produced **0 investable names** of 514. Evidence thresholds #2 (≥3 of 4 families non-negative) and #4 (data completeness ≥85%) fail for every name in the universe because `Fund_Z` and `Sent_Z` are `UNAVAILABLE`.

`rules.md § Downgrade to NO_TRADE` conditions met:

| # | Condition | Met? |
|---|---|---|
| 1 | Fewer than 5 names pass the investable threshold | **Yes — 0 pass** |
| 4 | More than 2 names with earnings inside 14 calendar days | **Yes — 7 of 26 published** |
| 6 | Publishing would require overconcentration in one sector or factor family, or violating the beta band — structurally infeasible | **Yes — beta band and Industrials cap, per Task 0** |

Conditions 2, 3 and 5 are **not** met: the best candidates do clear the 80th percentile, average pairwise correlation is 0.261 (below 0.45), and the estimated 95th-percentile drawdown is 7.51% (below 8%).

Per `rules.md § Hard Halt Criteria` #5, an infeasible portfolio escalates to `HALTED` only when the cause is process or data integrity. Here the cause is **the composition of the investable set** — a real market condition, cleanly measured — which routes to `NO_TRADE`, not `HALTED`. The revision pass was **not** spent, exactly as Task 0 directs.

## Portfolio Analytics

Not produced: there is no portfolio. Weights, expected Sharpe/Sortino/IR, tracking error, expected beta, VaR95/CVaR95 and drawdown are `N/A — NO_TRADE, no positions proposed`. This is not the forbidden `N/A - no validated engine`: the engine ran, produced the numbers above, and those numbers are what proves the portfolio infeasible. Per-position metrics for all 26 monitoring names are carried in full in `05` and `06`.

## Excluded Names — Rationale

| Group | Names | Why excluded from any portfolio |
|---|---|---|
| Entire investable set | all 514 | Evidence thresholds #2 and #4 fail universe-wide |
| Top-10 high-scorers | TRV, PAYX, DGX, UNP, PCG, RTX, NSC, GD, CSX, CTAS | Even if investable, cannot be assembled inside the 0.90–1.10 beta band (max attainable ≈ +0.11) |
| Industrials block | PAYX, UNP, RTX, NSC, GD, CSX, LMT, TMO | 60% of the top 10; only ~3 could be held under the 30% cap |
| Earnings-window names | GD, VLO, MPC, MET, HIG, AAPL, LLY | Report inside 14 days → −0.10 penalty, `LOW` confidence, event risk concentrated |
| `02` DROP names | CAT, GOOGL, GE, GS, EQIX, CVX, NVDA, FCX, V | Carry-forward decision `DROP`; held out of the scored set |
| Bounded-second-pass entrants | GL, FFIV, ESS, VRSK, INCY, DUK, ABBV, WST, PSA, TRGP, ITW, HWM, EA, MCK, STT, HUM | Entered the top 40 only after post-penalty re-ranking; earnings date not fetched → Required input #4 ungrounded |

## Recommendation to Risk Committee

**`NO_TRADE`.** Do not force a portfolio. The scoring stage cannot certify any name investable, and the construction stage independently establishes that this leaderboard is not assemblable inside the beta band or the sector cap. Both findings are computed and ledger-backed, and neither was worked around.
