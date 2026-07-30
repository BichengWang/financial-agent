# 14 — Weekly Review — 2026-07-30

**Not applicable — `Thursday`.**

`runbook.md § Cadence` schedules the weekly parameter review for **Friday after the close**
(17:15 ET). 2026-07-30 is a Thursday, so this run does not own it.
Created rather than omitted per `runbook.md § Output Location and Naming` rule 4.

The next weekly review is due **2026-07-31**, which is also the **last trading day of July** and
therefore owns the month-end structural review (`16_monthly_review.md`) as well.

Items this run hands forward to that review:

1. **Rank-order inversion** — weighted-mean rank IC -0.1975 over n=347;
   19 of
   23 vintages ≤ 0. Track A `DEFERRED`
   (`eff_n`=1 < 3, rises 2026-08-05).
   `10_midday_monitor.md` carries a same-session out-of-sample example.
2. **`MARKET_FORECAST` mu category error** — direction accuracy 16.4% over
   n=63; `mu = beta x SPY_mu` cannot express a bearish high-beta view. Track A `DEFERRED`
   (`eff_n`=1 < 3, rises 2026-08-09).
3. **`Fund_Z`/`Sent_Z` promotion (Phase 2)** — the only change that would let any run reach
   `GO`. Not a calibration question and not `eff_n`-gated.
