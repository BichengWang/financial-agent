# 14 Weekly Review — 2026-07-28

**Not due — 2026-07-28 is a Tuesday.**

`runbook.md § Cadence` schedules the weekly parameter review for **Friday 17:15 ET**. The next one is
due **2026-07-31**, which is also the last trading day of July and therefore carries the month-end
structural review (`16`).

Two items from this run should be carried into that review:

1. **The `eff_n` question is answered and no longer needs structural review.** The 2026-07-27 package
   queued "if `eff_n` can never rise under this cadence, the gate itself needs review, not the
   parameters." It can rise: `EQUITY_ALPHA` `eff_n` reaches 2 on **2026-08-05** and
   `MARKET_FORECAST` on **2026-08-09**, both now emitted directly by
   `settlement_ledger.py` (Track B accepted today, see `13`). The gate is a startup transient, not a
   design flaw. **The structural review should drop this item** and instead schedule the Track A
   calibration work for early September, when a third window opens.
2. **The `MARKET_FORECAST` mu formula is the highest-value Track A change waiting on that gate**
   (20.83% hit rate over n=48). It should be drafted now and applied the moment
   `eff_n ≥ 3`, not started then.
