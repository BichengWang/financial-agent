# 16 Monthly Review — 2026-07-26

**N/A — not the last trading day of the month.** `runbook.md § Cadence` schedules the structural review for the **last trading day of the month at 17:30 ET**. For July 2026 that is **Friday 2026-07-31**. 2026-07-26 is a Sunday, five days early.

Created per `runbook.md § Output Location and Naming` #4 rather than omitted.

## Carried Forward to the 2026-07-31 Structural Review

Recorded here so the agenda is not reconstructed from scratch:

1. **Unblock `Fund_Z` / `Sent_Z` — top priority.** Eleven consecutive `NO_TRADE` runs across every model trace to these two families being `UNAVAILABLE` universe-wide, which makes evidence threshold #2 unreachable by construction and #4 unreachable by arithmetic. This is an engineering task — Phase 2 of `agents/equity/plan/2026-07-15-claude-fable-5-top-priority.md` (bulk SEC `companyfacts.zip` + threaded Nasdaq fetch to ≥70% universe coverage) — not a prompt-evolution task. It should be ranked ahead of all calibration work, which is gated at `eff_n = 1` regardless. (`13 § Escalation`)

2. **Rank-order inversion.** Two statistically significant inversions now recorded (−0.712 on 2026-07-22; **−0.5912, p=0.026** on 2026-07-26), pooled weighted mean −0.1282 over n=203. The structural review should confirm that the standing mu-shrink proposal is formally retired: a monotonic transform cannot reorder a ranking, and the pooled magnitude metrics (mean z −0.2001, CI coverage 75.37%) are healthy. The testable replacement hypothesis is that a family polarity — most likely the disclosed defensive Macro polarity (L140) — carries the wrong sign in this regime. Still Track A, still gated until `eff_n ≥ 3` (~2026-09-18).

3. **`MARKET_FORECAST` mu derivation.** `mu = beta × SPY_mu` is a category error (2026-07-24 diagnosis); 22.22% hit rate, mean z −0.7047 over n=36. Two fixes tested and rejected. Today SOXX produced a `FLAT_CALL` at +0.320% while sitting −19.54% below its 60-day high. Needs a structural rethink, not another parameter tweak.

4. **Earnings-signature rule tightening.** The vendor-empty `OR volume ≥1.8×` branch fired on ~0.01% price moves for EQR and PKG this run. Track B, deferred only because the one-per-run budget was spent on the return-basis fix. (`13 § Observations` #2)

5. **Vendor availability.** Yahoo `v8/finance/chart` has been HTTP 429 in 7 of the last 13 sessions. The stockanalysis + Nasdaq + CNBC triangle has been reliable and now also supplies the adjusted-close basis; the structural review should consider formally demoting Yahoo from "primary" in the runbook to match observed practice.

- Next structural review: **2026-07-31**, 17:30 ET.
