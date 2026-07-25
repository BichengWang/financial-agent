# 14 Weekly Parameter Review — week ending 2026-07-24 (Friday)

Real weekly review per `runbook.md § Cadence` (Fri 17:15 slot; this run fired ~23:17 ET after the close). Broader changes are permitted at this cadence; protected rules always bind.

## Week in Review (2026-07-17 → 2026-07-24)

| Instrument | 07-17 | 07-24 | Week |
|---|---|---|---|
| SPY | 743.29 | 738.93 | **−0.59%** |
| QQQ | 695.33 | 684.23 | **−1.60%** |
| SOXX | 521.81 | 527.01 | **+1.00%** |
| TLT | 84.52 | 83.25 | −1.50% |
| ^VIX | 18.77 | 18.58 | −1.01% |

**Universe (514 names): median +0.04%, mean +0.03%, 51.0% positive.** The typical S&P/NDX constituent went precisely nowhere while the cap-weighted index fell 0.59% and the Nasdaq proxy fell 1.60%.

| Best 5 | | Worst 5 | |
|---|---|---|---|
| SMCI | +24.5% | TSLA | −17.8% |
| WAB | +15.4% | ROL | −14.5% |
| LMT | +14.5% | MRNA | −12.5% |
| DLR | +14.5% | MSCI | −12.4% |
| IP | +12.2% | CHRW | −10.5% |

A 42-point spread between the best and worst names in a week when the median stock was flat. **Dispersion, not direction, is this week's defining feature** — and it is the same fact the regime section, the leaderboard, and the portfolio-infeasibility finding are all describing from different angles.

Note SOXX finished the week *up* 1.00% despite Friday's −4.40% session, so the semis unwind is being delivered in violent, uneven bursts rather than a steady slide. That is worth carrying forward: a single-session move of that size inside a positive week is characteristic of a market repricing a narrow group repeatedly, not one that has settled on a new level.

## Parameter Review

Nothing in the parameter set was mutated this week beyond the change logged in `13_evolution_log.md`.

| Parameter block | Status | Basis |
|---|---|---|
| Family weights (0.30 / 0.30 / 0.25 / 0.15) | **Unchanged** | Two of four families remain `UNAVAILABLE`; re-weighting the two that work would be fitting around a tooling gap, not a signal finding |
| mu Calibration Table | **Unchanged** | Track A gate: `n=189` nominally clears ≥20, but `eff_n = 1`. No change is adjudicable |
| Core ETF mu prior table | **Unchanged — but formally queued** | Root cause diagnosed this run (beta-as-return-multiplier); two candidate replacements tested and rejected. Blocked on `eff_n ≥ 3` |
| Sigma sourcing (`REALIZED_VOL_30D`) | **Unchanged** | CI coverage 76.19% (equity) sits inside the healthy 55–85% band; no widening or tightening warranted |
| Confidence calibration | **Unchanged** | Rank-IC cap is doing its job; every name is independently `LOW` |
| Risk limits (5% name, 30% sector, 0.90–1.10 beta, 0.45 corr, 8% drawdown) | **Unchanged — protected** | The beta band bound hard this week and was *not* relaxed. That is the system working |
| Penalty schedule | **Unchanged** | Earnings penalty fired on 7 of 26 published names as intended |

## Weekly Calibration Position

| Metric | EQUITY_ALPHA | MARKET_FORECAST | Healthy |
|---|---|---|---|
| n | 189 | 33 | ≥10 |
| **eff_n** (new, this run) | **1** | **1** | ≥3 for Track A |
| Hit rate | 52.91% | 21.21% | >50% |
| CI coverage | 76.19% | 63.64% | 55–85% |
| Mean z | −0.213 | −0.731 | ±0.5 |
| Rank IC | −0.0939 | n/a | >0 |

Nothing settled this week after 2026-07-22, so these figures are unchanged from Wednesday's package. The material development is not a new number but a new *understanding* of the existing ones: the effective independent sample behind every one of them is a single overlapping cohort (`13 § The finding that both rejections expose`).

**Practical consequence for next week:** the 17 keys maturing 2026-07-26 and the 29 published today (target 2026-08-21) are the first forecasts that will begin to open a *second* independent window. `eff_n` should reach 2 within roughly a month and 3 shortly after — which is when the queued Core ETF mu change becomes testable for real.

## Cross-Model Observations

Nine consecutive `NO_TRADE` packages across `gpt-5`, `claude-fable-5`, `claude-sonnet-5` and now `claude-opus-5`, every one citing the same `Fund_Z`/`Sent_Z` blocker. There is no model-selection or prompt-interpretation variance left to explain here: **the system is tooling-blocked, and has been for at least nine packages.**

The concurrency conventions continue to hold up — this run rebased onto `main` at `709a1ba` before starting, found the workspace clean, and observed no competing 07-24 package. An empty `run/gpt-5-2026-07-24` local branch exists with no commits and no diff against `main`, consistent with an aborted session; it was left untouched rather than deleted, since it is another session's artifact.

## Actions for Next Week

1. **Apply the accepted Track B change** (`eff_n` in `settlement_ledger.py` rolling metrics + the Track A gate). Effective next run, flagged `HUMAN_REVIEW`.
2. **Settle the 17 keys maturing 2026-07-26** under `WEEKEND_TARGET` at the verified 2026-07-24 close; confirm `due_inventory` 17 → 0, 0 conflicts.
3. **2026-07-31 structural review** (`16_monthly_review.md`, month-end): take up the queued regime→prior mapping review with the effective-sample finding as its starting point, and consider the `|mu| < 0.5%` FLAT_CALL escape.
4. **Escalate Phase 2 of the SHADOW promotion.** This is the ninth consecutive package blocked on it. Every other improvement in this system is downstream of a gate that no run has attempted to open. It is engineering work, not an evolution-policy change, and it should be scheduled explicitly rather than re-noted weekly.
5. **Watch the rotation for regime invalidation.** SOXX retains a +16.3% 60-day cushion against SPY; if that is surrendered while breadth deteriorates, the `NEUTRAL` label needs revisiting.
