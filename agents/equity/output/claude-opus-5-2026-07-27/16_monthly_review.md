# 16 Monthly Review — 2026-07-27

**Not applicable to this run.**

`runbook.md § Cadence` schedules the structural review for the **last trading day of the month at
17:30 ET**. 2026-07-27 is a Monday in the final week of July; the last trading day of July 2026 is
**Friday 2026-07-31**. Created per `runbook.md § Output Location and Naming` rule 4 rather than
omitted.

Items this run contributes to the 2026-07-31 structural review:

1. **The `NO_TRADE` streak is infrastructural.** Every package in the trailing 7-day window, across
   every model, published `NO_TRADE` for the same reason: `Fund_Z` and `Sent_Z` have no universe-scale
   fetch path, so Evidence Thresholds #2, #3 and #4 are unpassable by construction. The fix is Phase 2
   of `agents/equity/plan/2026-07-15-claude-fable-5-top-priority.md` (bulk EDGAR `companyfacts.zip`
   plus threaded Nasdaq sentiment across all 514 names) — an engineering task, not a calibration one,
   and the highest-value change available to this system.
2. **`eff_n` stuck at 1** despite n=231, which gates every Track A proposal
   indefinitely. Needs a decision at the structural level: change the run/vintage cadence so target
   windows stop overlapping, or revisit the gate.
3. **Portfolio beta-band reachability.** With 41.25% of the
   universe at negative 60-day beta and a defensive leaderboard, the 0.90–1.10 band has now been
   unreachable on multiple runs (2026-07-24, 2026-07-27). Worth asking whether a long-only book selected by
   this scoring stack can ever satisfy that band in a rotation regime, or whether the interaction
   between the two is itself the finding. The band is a **protected rule** — any change requires human
   approval and must not be made autonomously.
4. **Bulk price-history redundancy has degraded to one source.** Yahoo 429-blocked on 8 of the last 14
   sessions; Nasdaq bulk-historical served a bot-challenge page this session. Only stockanalysis.com
   remains for bulk history, with CNBC and IBKR as per-symbol verification.
