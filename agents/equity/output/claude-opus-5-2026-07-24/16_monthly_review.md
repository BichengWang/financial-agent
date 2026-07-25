# 16 Monthly Structural Review — 2026-07-24

**N/A — not the last trading day of the month.**

`runbook.md § Cadence` schedules the structural review for the last trading day of the month at 17:30 ET. July 2026's last trading day is **Friday 2026-07-31**, one week from today. This file is created rather than omitted, per `runbook.md § Output Location and Naming` #4.

The Friday weekly parameter review that *is* due today is published in full in `14_weekly_review.md`.

## Queued for the 2026-07-31 structural review

1. **Core ETF mu prior table — beta-as-return-multiplier.** Root cause fully diagnosed in `13_evolution_log.md` (2026-07-24): `mu_ETF = beta × SPY_mu` cannot express a bearish view on a high-beta ETF because the ±1.5pp adjustment band is far narrower than the beta-amplified base. Result: 100% of 33 market forecasts carried positive mu; 21% of realized returns were positive; SOXX went 0-for-11. Two candidate replacements (beta damping, own-trend amplification) were tested and rejected — neither moved the hit rate off 21.2%. **Blocked on `eff_n ≥ 3`** under the Track B gate accepted 2026-07-24.
2. **The regime→prior mapping review**, queued since 2026-07-20, now to be conducted with the effective-sample finding as its starting point rather than against pseudo-replicated `n`.
3. **The `|mu| < 0.5%` FLAT_CALL escape.** A forecast can currently avoid direction scoring entirely by landing inside the flat band — used legitimately by today's SPY forecast (mu exactly 0.00%), but it weakens the calibration record.
4. **`Fund_Z` / `Sent_Z` Phase 2 promotion.** Nine consecutive `NO_TRADE` packages across four model families are blocked on this single gate. Engineering work per `agents/equity/plan/2026-07-15-claude-fable-5-top-priority.md`, not an evolution-policy change.
5. **Tech_Z / Macro_Z non-independence.** In a rotation the highest-relative-strength names are largely the lowest-beta names, so the two available families co-move and evidence threshold #3 passes arithmetically while being questionable in substance (`08 § Concern 2`).
