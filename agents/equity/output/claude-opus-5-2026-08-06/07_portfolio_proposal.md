# 07 — Portfolio Proposal *(backfilled)*

> **BACKFILLED 2026-08-07.** The 2026-08-06 session truncated after writing `00`-`04` and `15_predictions.json`; this artifact was reconstructed on 2026-08-07 from that folder's own committed data (`15_predictions.json` plus `00`-`04`) and from nothing else. Figures that the truncated session never persisted are marked `UNAVAILABLE` rather than recomputed: the 2026-08-06 run used the 2026-08-05 close as its basis, so substituting a later run's numbers would misstate what that run actually saw. No prediction record was created, altered or settled.

## Decision: `NO_TRADE` — no weights were proposed

## Task 0 — constraint feasibility pre-check

The truncated session recorded its feasibility result in `00_run_manifest.md`; that recorded
figure is cited here rather than recomputed.

| Constraint | Cap / band | As recorded by the 2026-08-06 run | Result |
|---|---|---|---|
| Portfolio beta to SPY | 0.90 – 1.10 | attainable sleeve beta -0.2803 … +1.4145 (`00 § Evidence thresholds`) | **FEASIBLE** |
| Minimum investable count | >= 5 | 0 names cleared the evidence thresholds | **FAIL** |
| Average pairwise correlation | < 0.45 | **UNAVAILABLE** — not persisted | unknown |
| 95th-pctl 1-month drawdown | <= 8% | **UNAVAILABLE** — not persisted | unknown |
| Max sector concentration | <= 30% | **UNAVAILABLE** — sector table not persisted | unknown |

The 2026-08-06 manifest states plainly that the beta band was feasible that run —
"the fifth consecutive run where the 2026-07-27 'provably infeasible' narrative would have been
wrong" — so `NO_TRADE` did **not** rest on feasibility. It rested on the evidence thresholds.

## Portfolio analytics

**`UNAVAILABLE`.** The correlation matrix, portfolio sigma and 95th-percentile drawdown were
never written to a durable artifact before the session truncated, and the `.work/` directory is
gitignored. Per-position analytics (beta, tracking error, Sharpe, Sortino, IR, Treynor, VaR95,
CVaR95, 60d max drawdown, Kelly) **were** persisted per name and appear in `05`.

## Failure rule

`agents.md § Portfolio Construction` failure rule applied: the investable count was 0, below the
minimum of 5, so the agent recommended **`NO_TRADE`** without forcing a portfolio.
