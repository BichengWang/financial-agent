# 13 — Evolution Log — 2026-08-01

## Run context

| Field | Value |
|---|---|
| Run date | 2026-08-01 (Saturday), basis 2026-07-31 |
| Final status | `NO_TRADE` |
| Regime | `BULL` |
| Evaluation window | 2026-07-25 … 2026-08-01 (trailing 7 days, all models) |
| Packages reviewed | **9** — {'NO_TRADE': 8, 'NO_09_ARTIFACT': 1} |
| Ledger status | `EQUITY_ALPHA` n=439, `eff_n`=1 · `MARKET_FORECAST` n=78, `eff_n`=1 |
| Baseline flag | `CROSS_MODEL_BASELINE` (2-way tie resolved by rule 8) |
| Due inventory / conflicts | 0 / 0 |

## What worked

- **Weekend fire on a Friday close is a clean basis.** 519/519 symbols in
  31.8s with **one** distinct last-bar date across the entire universe, and
  0 ex-dividend artifacts
  on the basis bar. No reconciliation pass was needed anywhere.
- **Three-source price grounding with zero re-reads.** 77/77 names
  agreed within 0.0661%. The CNBC weekend
  field rule (`last`, gated on `last_time` date == basis) worked exactly as the closed-market
  case predicts, without the 2026-07-27 intraday inversion applying.
- **Settlement was frictionless.** 107 due keys, 0
  unsettleable, 0 conflicts, `due_inventory: 0` on re-run. The
  two-cohort split (`ORDINARY` for Friday targets, `WEEKEND_TARGET` for Saturday targets)
  needed no special handling.
- **Full-universe earnings grounding held.** Complete sweep
  (26/26 days, 0 transport failures),
  30/30 cross-validated against the per-name endpoint with zero
  disagreements, and published ranks are contiguous 1–24.
- **Rule 8 (MoM tie-break) worked and, this time, showed robustness.** The
  2-way tie resolved deterministically and the two books differed by only
  1.7pp
  of hit rate — the conclusion is invariant, which is worth recording precisely because the
  two prior firings of this rule found 48pp and 40.7pp spreads.

## What failed

- **The settled batch was poor:** 20/92 = 21.7% equity direction hits, mean z
  -0.9090.
- **Rank-order inversion persists** — weighted-mean rank IC -0.1314 over n=439,
  negative in 20 of 28 vintages.
- **`MARKET_FORECAST` remains badly calibrated** — 20.27% over n=78, and
  the `BULL` regime exposed the `beta × SPY_mu` category error in the bullish
  direction (SOXX formula mu +7.34%).
- **Eleventh-plus consecutive non-`GO`** — and, per `16`, July closed with **zero** `GO` runs
  across all models.

## Primary diagnosis: **factor calibration** (specifically, factor *construction*)

Not data quality — every Required input was grounded this run. The defect is in how
`Tech_Z` is assembled.

## Proposed change (exactly one) — **Track B**

**Deduplicate the relative-strength metrics inside `Tech_Z`.**

### Current problem

`technical_indicators.py::add_relative_strength` (line 432) computes
`relative_strength_20d = momentum_20d − benchmark_momentum_20d`. Because SPY's momentum is
the **same scalar for every name**, this is a constant shift, and a constant shift leaves a
cross-sectional z-score unchanged. The factor engine nonetheless feeds `mom20`, `mom60`,
`rs20` and `rs60` in as four independent metrics of eight.

Measured on this run's 513-name universe:

| Identity | Max abs difference |
|---|---|
| `z(rs20)` vs `z(mom20)` | **4.441e-16** |
| `z(rs60)` vs `z(mom60)` | **4.441e-16** |

Floating-point zero. `Tech_Z` advertises 8 metrics but carries **6 distinct signals**, and
momentum occupies 4 of the 8 slots — **33.3%** of live composite weight instead
of the **16.7%** the metric list implies.

The artifact that exposed it: this run's `05_factor_scores.md` scoring-architecture section,
cross-checked against `claude-opus-5-2026-07-30/run_computed_manifest.json`, where the stored
`tech_components` for every name already showed `mom20 == rs20` and `mom60 == rs60` to full
printed precision. The defect has been silently active in every package built on this engine.

### Proposed change

Within `Tech_Z`, drop `rs20` and `rs60` as separate metric slots. `Tech_Z` becomes the
equal-weighted mean of **6** metric z-scores: `mom20`, `mom60`, `ma_align (d+w)`,
`macd (d+w)`, `vol_conf`, `dd60`. Relative strength continues to be **computed, displayed and
ledgered** in `05`/`06` as a diagnostic — it is genuinely informative to a human reader — it
simply stops being counted twice in the arithmetic.

### Hypothesis (explicit and falsifiable)

Momentum's weight inside `Tech_Z` falls from 50% to 33.3%, and its share of the live
composite from 33.3% to 16.7%. Since the settled record shows
the composite's ordering is *anti*-correlated with realized alpha through rotations, and
since the over-weighted signal is precisely the trend-persistence one, reducing that
over-weighting should move rank IC toward zero from below. **Falsifiable:** if rank IC over
the next `eff_n ≥ 3` window is not higher than the concurrent un-deduplicated baseline, the
change is reverted.

### Validation — Track B three-condition standard

1. **Explicit problem statement citing the artifact that exposed it** — yes, above, with the
   measured identity and the source-code line.
2. **Cannot weaken a protected rule or grounding gate** — confirmed. It touches no protected
   rule from `rules.md § Evolution Policy`: no fabrication allowance, no `NO_TRADE`
   discipline change, no change to the 5% / 30% / beta-band / 0.45-correlation / 8%-drawdown
   caps, and no change to the mandatory-logging rule. It does not alter the 0.30/0.30/0.25/
   0.15 **family** weights — those are untouched; it corrects the *within-family* metric
   count so that `rules.md § Family Aggregation`'s "equal-weight available sourceable metric
   z-scores" is actually honoured rather than nominally honoured.
3. **Logged with a `HUMAN_REVIEW` flag, effective next run** — yes; see the decision block.

**Measured impact** (computed this run, both variants side by side):

| Statistic | Value |
|---|---|
| Top-24 published-set overlap | **19/24** |
| Top-30 overlap | **24/30** |
| Median rank move, all 513 names | **12 places** |
| 90th-pctl rank move | 37 places |
| Max rank move | 82 places |
| New rank-1 name | DXCM (was DXCM) — unchanged |

This is a **material** change, not a cosmetic one, and it is honest to say so: roughly a
quarter of the published set turns over. That is why it is scheduled for next run rather
than applied retroactively to this package.

### Why this is Track B and not Track A

Track A governs *performance parameter* changes — factor weights, thresholds, the mu tables,
confidence calibration, sizing. This proposal changes none of those. It removes a metric that
is mathematically identical to another metric already in the same average. The intended
specification ("equal-weight the family's sourceable metric z-scores") is unchanged; the
implementation was not meeting it. A Track A gate would be the wrong standard here, and it
would also be unmeetable — `eff_n` = 1 — which would leave a known arithmetic
defect in place indefinitely.

### Decision: **ACCEPT** — `HUMAN_REVIEW`, effective next run (2026-08-03)

Not applied to this package: the run is `NO_TRADE` regardless, so no capital is affected, and
re-scoring mid-series would break comparability with the ranked history for no benefit. The
defect is disclosed in `05` beside the scores it affects.

## Deferred observations (recorded, not proposed — one change per run)

1. **`MARKET_FORECAST` mu derivation is a category error.** `mu = beta × SPY_mu` conflates
   co-movement magnitude with expected-return direction. In a `BEAR`/`NEUTRAL` prior it makes
   bearish views unrepresentable; in today's `BULL` prior it produces SOXX
   +7.34%. Hit rate 20.27% over n=78.
   **Track A** (Core ETF mu prior table) → **`DEFER`**, `eff_n` = 1 < 3. Third
   consecutive log recording this.
2. **Rank-order inversion.** Rank IC -0.1314 over n=439. A mu shrink or sigma
   widen is a monotonic transform and cannot fix it — that proposal stays retired. The
   deduplication accepted above is the first structural attempt at the real cause. **Track A**
   for any weighting change → **`DEFER`**.
3. **`Fund_Z`/`Sent_Z` universe-scale tooling** is the single highest-value open item and is
   an engineering task, not a prompt mutation. See `16 § Structural finding 1`.

## Freeze-criteria check

No freeze. This run **accepts** a change, so the "three consecutive cycles reject all changes"
clause does not trigger. No accepted change has yet worsened out-of-sample performance
(the last two accepted changes — the 2026-07-29 calendar sweep and the 2026-07-30 tie-break
rule — are grounding/process improvements with no scoring math to degrade). No oscillation:
no parameter has been moved back and forth.

## Effective next step

Apply the `Tech_Z` deduplication in the 2026-08-03 run. Report rank IC for the deduplicated
engine against the un-deduplicated baseline once `eff_n ≥ 3` (projected early September) and
revert if it has not improved.
