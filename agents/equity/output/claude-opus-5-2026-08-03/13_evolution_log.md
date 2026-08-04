# 13 — Evolution Log — 2026-08-03

## Run context

| Field | Value |
|---|---|
| Run date | 2026-08-03 (Monday), post-close fire 2026-08-03 20:08 ET, basis 2026-08-03 |
| Final status | `NO_TRADE` |
| Regime | `BULL` |
| Evaluation window | 2026-07-27 … 2026-08-03 (trailing 7 days, all models) |
| Packages reviewed | **10** — {'NO_TRADE': 10} |
| Ledger status | `EQUITY_ALPHA` n=515, `eff_n`=1 · `MARKET_FORECAST` n=90, `eff_n`=1 |
| Baseline flag | `CROSS_MODEL_BASELINE` (2-way tie resolved by rule 8) |
| Due inventory / conflicts | 0 / 0 |

## What worked

- **A post-close fire is as clean as pre-open, and settles more.** At 2026-08-03 20:08 ET the 2026-08-03 close was
  final at all three vendors, so technicals, entry prices *and* settlements share one basis, and
  same-day `TARGET_DATE_CLOSE` settlement is available — 39 of the 88 keys
  settled that way instead of waiting a day. 27/27 published symbols agreed within
  0.0788%, zero confirmation re-reads.
- **The post-close vendor field rules were confirmed, and they differ from both other fire windows.**
  Under `POST_MKT`, CNBC `last` gated on `last_time` == basis is the official close while
  `previous_day_closing` returns T-1; Nasdaq `secondaryData` gated on the `Closed at` marker is the
  close while `primaryData` is the after-hours tape (SPY primary 758.25 vs close 757.64). Recorded in `01`.
- **Settlement was frictionless.** 88 due keys, 0 unsettleable, 0 conflicts, `due_inventory: 0`
  on the verification pass.
- **Full-universe earnings grounding held.** 28/28 business days
  swept, 0 transport failures, so absence is positive evidence and published ranks are
  contiguous 1–24.
- **Rule 8 fired for the fourth time and the conclusion was invariant** — a 2-way tie with a
  6.1pp hit-rate spread, both books far below the healthy floor.
- **The scheduled `Tech_Z` deduplication shipped on time**, on the exact run date it was stamped for.

## What failed

- **The settled batch was poor again:** 19/76 = 25.00% equity direction hits, mean z
  -0.8561.
- **Rank-order inversion persists** — weighted-mean rank IC -0.0879 over n=515, non-positive in
  20 of 32 vintages.
- **`MARKET_FORECAST` remains badly calibrated** — 22.09% over n=90.
- **A drawdown-polarity defect reached the scoring engine and was caught only by an explicit
  reproduction test** — see the diagnosis below.
- **Non-`GO` again**, for the same structural reason as every package since 2026-07-01.

## Primary diagnosis: **output clarity** (specifically, reproducibility of the disclosed methodology)

Not factor calibration this time. The dominant *new* finding is that `05_factor_scores.md`'s
methodology disclosure — which the 2026-07-27 log correctly identified as the strongest available
verification tool, precisely because a later run can rebuild the engine from it — is **not actually
sufficient to rebuild the engine**. Rebuilding from it this run produced:

| Quantity | Reproduction quality |
|---|---|
| Entry prices | 18/20 exact to the cent (NTAP, PFG differ $0.03) |
| `Tech_Z` | all 20 within 0.03 absolute — effectively reproduced |
| `Macro_Z` | mean absolute error 0.092, **max 0.293** — not reproduced |
| `max_drawdown_60d` polarity | **inverted** on the first rebuild |

Two concrete failures, both traceable to the same gap:

1. **Sign convention.** `05` says the drawdown metric is "60d max drawdown (negated)". Since
   `max_drawdown_60d` is *already* stored as a signed negative number, "negated" reads naturally as
   "apply a negation", which inverts the metric so that deeper drawdowns score **better**. The
   rebuild did exactly that. It was caught only because the reproduction test compared against the
   prior package's published driver z-scores, where MSFT's `dd60 -0.96` had the opposite sign to the
   rebuild's `+0.94`.
2. **Window/definition ambiguity.** `05` says "realized-vol stability (30d/60d, negated)" without
   stating the stdev convention, the scaling, or whether "60d" means the trailing 60 sessions or the
   30 sessions preceding the last 30. Three plausible readings were tested; the best fit still leaves
   a max error of 0.29 in `Macro_Z`, i.e. ~0.035 of `Adj Score` — enough to move ranks materially.

This is a grounding-adjacent defect, not a cosmetic one. A methodology disclosure that cannot
reconstruct its own numbers cannot serve as the verification instrument the system relies on, and it
silently invites exactly the polarity class of bug that hit this run.

## Proposed change (exactly one) — **Track B**

**Require `05_factor_scores.md` to carry a normative Metric Definition Table.**

### Current problem

Stated above, with the two measured failures and the artifact that exposed them
(`claude-opus-5-2026-08-01/05_factor_scores.md § Scoring architecture actually executed`, compared
against a rebuild from that section alone).

### Proposed change

`05` must include, in addition to today's family/weight table, one row per metric slot with these
columns:

`Metric slot | Family | Source field | Window | Transform before z-score | Polarity (higher-is-better after transform) | Winsorization`

Rules the table must satisfy:

- **Polarity is stated as the post-transform direction**, never as an instruction word like
  "negated". A reader must be able to answer "does a larger raw value help or hurt?" without knowing
  the sign convention of the stored field.
- **Every window is given in explicit units** ("trailing 60 daily sessions", not "60d") and every
  stdev states population vs sample and the scaling factor.
- The table is normative: if it and the running code disagree, the code is wrong or the table is
  wrong, and the run must say which.

### Hypothesis (explicit and falsifiable)

If the table is present, an independent rebuild of the engine from `05` alone will reproduce a prior
same-basis package's `Tech_Z` and `Macro_Z` to within **0.01 absolute** for every published name.
**Falsifiable:** the next run that performs a same-basis reproduction check reports the max absolute
`Tech_Z` and `Macro_Z` error; if either exceeds 0.01 with the table in place, the table is
insufficient and this change is reverted in favour of publishing the scoring code path itself.

### Validation — Track B three-condition standard

1. **Explicit problem statement citing the artifact that exposed it** — yes, with two measured
   reproduction failures and the specific ambiguous phrases.
2. **Cannot weaken a protected rule or grounding gate** — confirmed. It adds disclosure. It changes
   no factor weight, threshold, mu table, sizing parameter or protected cap, and it cannot make any
   previously-ungrounded value publishable.
3. **Logged with a `HUMAN_REVIEW` flag, effective next run** — yes; see the decision block.

This run's `05` already contains the required content in prose form (sign convention for
`max_drawdown_60d` is now stated explicitly), so the change is a formalization of something already
demonstrated to be necessary, not a speculative addition.

### Decision: **ACCEPT** — `HUMAN_REVIEW`, effective next run (2026-08-04)

## Effect of the previously-accepted change, measured

The 2026-08-01 `Tech_Z` deduplication was applied for the first time in this package, exactly on its
stamped effective date. Re-measured identity on today's universe: `z(rs20)` vs `z(mom20)` and
`z(rs60)` vs `z(mom60)` both differ by **4.4409e-16**, reproducing the original finding. Turnover
against the legacy 8-slot engine, run side by side on identical inputs:

| Statistic | 2026-08-01 estimate (07-31 cross-section) | Measured today |
|---|---|---|
| Top-24 overlap | 19/24 | **13/24** |
| Top-30 overlap | 24/30 | **18/30** |
| Median rank move | 12 places | **31 places** |
| Max rank move | 82 places | 138 places |

The effect is roughly twice the earlier estimate. That estimate was measured on a different day's
cross-section and was never a forecast of today's; the correct reading is that the deduplication's
impact scales with how concentrated momentum happens to be. Rank IC for the deduplicated engine
cannot be evaluated until `eff_n >= 3` (projected 2026-08-05 for the first
increment, early September for the gate), per the falsifiability condition recorded on 2026-08-01.

## Deferred observations (recorded, not proposed — one change per run)

1. **`MARKET_FORECAST` mu derivation is a category error.** `mu = beta x SPY_mu` conflates
   co-movement magnitude with expected-return direction; today it produced SOXX
   +7.06% before the band trim. Hit rate 22.09% over n=90.
   **Track A** (Core ETF mu prior table) -> **`DEFER`**, `eff_n` = 1 < 3. Fourth consecutive log.
2. **Rank-order inversion.** Rank IC -0.0879 over n=515. The deduplication shipped this run is
   the first structural attempt at the cause and cannot be judged yet. **Track A** for any weighting
   change -> **`DEFER`**.
3. **`Fund_Z`/`Sent_Z` universe-scale tooling** remains the single highest-value open item and is an
   engineering task, not a prompt mutation.
4. **The naive top-20 sleeve failed the 8% drawdown cap** (8.50%) and sat well below
   the beta floor (+0.5323), while the *attainable* beta range
   [-0.5565, +1.4240] is comfortably feasible. Recorded as
   evidence that rank-ordered selection and constraint satisfaction pull in different directions.

## Freeze-criteria check

No freeze. This run **accepts** a change, so the "three consecutive cycles reject all changes" clause
does not trigger. No accepted change has yet worsened out-of-sample performance — the last three
accepted changes (2026-07-29 calendar sweep, 2026-07-30 tie-break rule, 2026-08-01 `Tech_Z`
deduplication) are grounding, process and arithmetic-correctness fixes; the third is now live and
under an explicit falsifiability condition. No oscillation: no parameter has been moved back and forth.

## Effective next step

Add the Metric Definition Table to `05` from the 2026-08-04 run onward, and have the next run that
performs a same-basis reproduction check report the max absolute `Tech_Z` and `Macro_Z` errors
against the 0.01 threshold. Continue holding all Track A calibration work until
`eff_n >= 3`.
