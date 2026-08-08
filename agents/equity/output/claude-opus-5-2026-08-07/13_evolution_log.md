# 13 — Evolution Log · 2026-08-07

## Run context

| Field | Value |
|---|---|
| Run date / model | `2026-08-07` / `claude-opus-5` |
| Final status | `NO_TRADE` |
| Regime | `BULL` |
| Evaluation window | trailing 7 calendar days, all models (2026-07-31 … 2026-08-07) |
| Ledger status | EQ raw `n`=643, `eff_n`=2; MF raw `n`=108, `eff_n`=1 |
| Track A eligibility | **False** — `INSUFFICIENT_EFFECTIVE_N` (needs `eff_n >= 3`) |
| Baseline flag | `CROSS_MODEL_BASELINE` |

### Packages in the review window

| Package | Model | Date | Final status | Predictions | Numbered artifacts |
|---|---|---|---|---|---|
| `claude-opus-5-2026-08-01` | claude-opus-5 | 2026-08-01 | NO_TRADE | 27 | 17 |
| `claude-opus-5-2026-08-03` | claude-opus-5 | 2026-08-03 | NO_TRADE | 27 | 12 |
| `claude-opus-5-2026-08-04` | claude-opus-5 | 2026-08-04 | NO_TRADE | 27 | 13 |
| `claude-opus-5-2026-08-06` | claude-opus-5 | 2026-08-06 | *(none published)* | 27 | 6 |
| `claude-opus-5-2026-08-07` | claude-opus-5 | 2026-08-07 | *(none published)* | 27 | 1 |
| `gpt-5-2026-08-03` | gpt-5 | 2026-08-03 | HALTED | 3 | 12 |

`claude-opus-5-2026-08-06` carries only 6 numbered artifacts and no `09_final_report.md`: that
session truncated after writing `00`–`04` and `15`. Its manifest claims artifacts that were
never written. It is addressed in this PR by backfill rather than left as a silent gap.

## What worked

1. **Post-close firing produced the cleanest grounding of the series.** 519/519 symbols in
   12.2s, 518 last bars on the basis date, **zero** ex-dividend `c != a` splits
   on the basis bar, and 27/27 published prices agreeing to
   **0.0000%** across three independent vendors with zero confirmation
   re-reads. Entry prices, technical indicators and settlement prices all rest on one completed
   close — the run date's own.
2. **The forward earnings sweep held.** 26/26
   business days, zero transport failures, whole universe grounded, so the published set is
   contiguous ranks 1–24 with no "skip ungrounded" gaps.
3. **The Task 0 feasibility pre-check earned its place again.** It caught the
   9.15% drawdown breach and the
   41.67% Consumer Discretionary concentration before any sizing
   work — and it correctly reported the beta band as **feasible** for the sixth consecutive
   run, against the stale 2026-07-27 "provably infeasible" narrative.

## What failed

1. **The whole settlement queue was deferred by a clock technicality** — the subject of this
   run's proposed change, below.
2. **Direction accuracy remains the core unsolved problem.** 39.04% hit rate
   over 643 settled records with CI coverage 69.36% inside the healthy
   band: the intervals are honest, the rank order is not. The diagnostic settlement of the
   2026-07-10 vintage reproduced it exactly — both tied books produced negative mean alpha in a
   +2.43% tape.
3. **`eff_n` still gates every Track A fix.** The two changes that would actually address the
   rank inversion — replacing the `beta x SPY_mu` ETF mapping and reweighting the composite —
   are both Track A and both blocked at `eff_n = 2 < 3`.

## Primary diagnosis

**Source grounding** — specifically, the settlement-timing validator. The scoring machinery,
price grounding and artifact generation all behaved correctly this run; the one thing that went
wrong was that a correct settlement, computed from the correct close, was rejected for the
wrong reason.

## Proposed change (exactly one)

**Track B — widen the `TARGET_DATE_CLOSE` validator to accept any `settled_at` at or after the
target-date close, rather than only one on the target date's own calendar day.**

**Current problem.** `settlement_ledger.py:577` required
`settled_at_et.date() == target_date and settled_at_et.time() >= 16:00`. This run fired at
22:02 ET and its settlement pass executed after midnight, so a truthful `settled_at` of
`2026-08-08T01:30:38-04:00` was rejected — even though it is *strictly stronger* evidence that
the completed 16:00 close was used than a 16:05 stamp would be. The artifact that exposed it is
this run's own `settlement_manifest.json`: all 50 due keys landed in `rejected_candidates` with
the reason string quoted in `02 § 0`. The module docstring already stated the intended rule as
"at or after 16:00 ET"; the extra calendar-date pin was implementation drift from the documented
intent.

**Hypothesis (explicit and falsifiable).** Replacing the same-date test with
`settled_at_et >= datetime.combine(target_date, 16:00, America/New_York)` admits exactly the
settlements that used a completed target-date close and no others. Falsifiable prediction: the
next post-close run settles its due queue with `due_inventory` dropping to 0 and
`rejected_rows` unchanged at 87. If any *additional* row is admitted, or any currently-canonical
settlement changes, the change is wrong and reverts.

**Validation.**

| Test | Result |
|---|---|
| Cannot weaken a protected rule or grounding gate | **Confirmed.** `price_date == target_date` and the explicit `TARGET_DATE_CLOSE` declaration are both still required; only the upper bound on the timestamp is removed. Pre-close and unlabeled same-day prints remain rejected. |
| Retroactive scope on the existing corpus | **Zero rows.** 0 of the 87 currently-rejected rows are rejected by the calendar-date condition, so no historical candidate changes status. |
| Manifest diff before vs after the edit | **Byte-identical** on `summary`, `rolling_metrics`, `canonical_settlements` and `due_inventory` — verified by re-running the ledger against both versions. |
| Existing test suite | 80/80 pass unchanged. |
| New regression test | `test_target_date_close_valid_when_settled_after_midnight` added, encoding this run's exact timestamp; 81/81 pass. |

Track B requires no statistical holdout — there is no scoring math to validate — and the
Acceptance Standard's IR/hit-rate/drawdown/turnover clauses do not apply, because the change
cannot alter any score, weight, forecast or position. It changes only which settlement rows the
normalizer admits.

**Decision: `ACCEPT`** · `HUMAN_REVIEW` · **effective next run (2026-08-08)**.

The code edit and its regression test ship in this PR. This run's own 50 keys are **not**
retro-settled under the new rule — they stay due and settle `ORDINARY` on the next run at the
same close, which keeps this package's ledger state exactly what the pre-change code produced
and avoids re-scoring mid-series.

**Scope, stated honestly.** This fix does not recover the 50 keys — they would have settled next
run regardless, since the next run date will exceed their target date. What it prevents is the
recurring case: any post-close run whose pipeline takes long enough to cross midnight silently
defers its entire settlement queue by a day, which delays `eff_n` growth and therefore delays
Track A eligibility. Given that `eff_n` is the single gate blocking every performance fix this
system has diagnosed, an avoidable one-day slip in settlement timing is worth closing.

## Changes considered and not proposed

| Candidate | Track | Why not this run |
|---|---|---|
| Replace `mu_ETF = beta x SPY_mu` with a trend/RS-based mapping | A | gated at MF `eff_n = 1 < 3`; two variants were already tested and rejected on 2026-07-24. Recorded as a standing observation, `DEFER`. |
| Reweight the composite away from a trend-only `Tech_Z` | A | gated at EQ `eff_n = 2 < 3`; also cannot be fixed by a monotonic transform since the failure is rank-order, not magnitude. |
| Promote `Fund_Z`/`Sent_Z` from SHADOW | B | blocked by the 70%-of-universe coverage bar in `rules.md`, which needs Phase 2 of the plan (bulk `companyfacts.zip` + threaded sentiment fetch). Not a wording change. |
| Refresh the 47-day-old constituent caches | — | maintenance, not an evolution change; `rules.md` rule 5 explicitly says stale caches are used as-is and logged. |

One Track B per run is the limit, and the settlement validator is the one that blocked real work
today.

## Effective next step

The next run should: (1) confirm `due_inventory` reaches 0 with `rejected_rows` still 87,
falsifying or confirming the change above; (2) re-check whether MF `eff_n` increments now that
its projected date of `2026-08-09` has passed — that
projection is still pending, not yet falsified; and (3) run the same-basis reproduction test
owed by the Metric Definition Table if it shares the 2026-08-07 basis.
