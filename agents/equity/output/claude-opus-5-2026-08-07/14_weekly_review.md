# 14 — Weekly Parameter Review · week ending 2026-08-07

Friday after-close review per `runbook.md § Cadence`. Broader changes are permitted at this
cadence; protected rules always bind.

## Roster — packages in the trailing 7 days

| Package | Model | Date | Final status | Predictions | Numbered artifacts |
|---|---|---|---|---|---|
| `claude-opus-5-2026-08-01` | claude-opus-5 | 2026-08-01 | NO_TRADE | 27 | 17 |
| `claude-opus-5-2026-08-03` | claude-opus-5 | 2026-08-03 | NO_TRADE | 27 | 12 |
| `claude-opus-5-2026-08-04` | claude-opus-5 | 2026-08-04 | NO_TRADE | 27 | 13 |
| `claude-opus-5-2026-08-06` | claude-opus-5 | 2026-08-06 | *(none published)* | 27 | 6 |
| `claude-opus-5-2026-08-07` | claude-opus-5 | 2026-08-07 | *(none published)* | 27 | 1 |
| `gpt-5-2026-08-03` | gpt-5 | 2026-08-03 | HALTED | 3 | 12 |

| Metric | Value |
|---|---|
| Distinct run dates | 5 |
| Distinct models | 2 |
| Packages with a published `09` status | 4 |
| `GO` runs this week | **0** |
| `NO_TRADE` runs | 3 |
| `HALTED` runs | 1 |
| Incomplete / truncated packages | 2 |

**Zero `GO` runs again this week**, extending the streak that began before July. The cause has
not moved: `Fund_Z` and `Sent_Z` are unavailable universe-wide, which makes two of the four
evidence thresholds unsatisfiable regardless of market conditions or candidate quality.

## Parameter review

| Parameter group | Current | Evidence this week | Change? |
|---|---|---|---|
| Family weights (0.30/0.30/0.25/0.15) | unchanged | two families dark; reweighting the live two is Track A and gated | **No** |
| mu Calibration Table | unchanged | mean z -0.5328 says mu is over-forecast, but `eff_n = 2 < 3` | **No — DEFER** |
| Core ETF mu prior table | unchanged | MF hit rate 25.96% over n=108; the `beta x SPY_mu` mapping is a known category error | **No — DEFER** |
| Confidence calibration | unchanged | rank IC <= 0 already caps everything at MEDIUM via the existing rule; no change needed | **No** |
| Sigma sourcing | `REALIZED_VOL_30D` | CI coverage 69.36% sits inside the healthy 55–85% band | **No** |
| `Tech_Z` slot set (6 distinct inputs) | unchanged since 2026-08-03 | no evidence this week against the dedupe | **No** |

Every calibration parameter is either healthy or blocked on `eff_n`. The one change accepted
this week is the Track B settlement-validator fix in `13_evolution_log.md`.

## Calibration state

| Metric | `EQUITY_ALPHA` | `MARKET_FORECAST` | Healthy | Reading |
|---|---|---|---|---|
| raw `n` | 643 | 108 | >= 20 for Track A | satisfied |
| 28-day `eff_n` | 2 | 1 | >= 3 for Track A | **blocking** |
| Hit rate | 39.04% | 25.96% | > 50% | **failing** |
| CI coverage | 69.36% | 84.26% | 55–85% | equity healthy; MF too wide |
| Mean z | -0.5328 | -0.5285 | -0.5 to +0.5 | at the edge |
| Rank IC (weighted mean) | -0.0430 | n/a | > 0 | **failing** |

The `MARKET_FORECAST` CI coverage of 84.26% is **above** the 85% ceiling,
which `rules.md` reads as uninformatively wide intervals that should be tightened. That is a
Track A change to sigma sourcing and is gated at `eff_n = 1`. Logged as a standing
observation for the first review that clears the gate.

## Structural items carried forward

| # | Item | First raised | Status |
|---|---|---|---|
| 1 | `Fund_Z`/`Sent_Z` Phase 2 (bulk XBRL + threaded sentiment across the universe) | 2026-07-15 plan | **open** — the single blocker on every `GO` |
| 2 | `beta x SPY_mu` ETF mu mapping is a category error | 2026-07-24 | **open** — Track A, gated at MF `eff_n = 1` |
| 3 | Rank-order inversion in a trend-dominated `Tech_Z` | 2026-07-22 | **open** — Track A, gated at EQ `eff_n = 2` |
| 4 | No 2026-08-05 package in the audit trail | 2026-08-06 | **open** — not resolvable retroactively without fabricating a vintage |
| 5 | Truncated 2026-08-06 package | this run | **addressed** — backfilled in this PR with explicit banners |
| 6 | Constituent caches 47 days stale | ongoing | open — maintenance task; used as-is per `rules.md` rule 5 |

## Next week

The `eff_n` projections put EQ Track A eligibility at
`2026-09-03` (eff_n -> 3 requires a further window beyond
that) and MF at `2026-08-09`, which has now passed and is
**pending confirmation** on the next run that settles. Until one of those clears, the daily loop
should keep publishing settleable forecasts and avoid parameter churn — which is exactly what
`rules.md § Anti-Overfitting Rules` prescribes.
