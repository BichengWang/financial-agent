# 12 Evolution Log

## Run Context

| Field | Value |
|---|---|
| Date | 2026-05-24 |
| Run status | `REVIEW_ONLY` |
| Regime | `NEUTRAL` with `HIGH_VOL` tilt (reference-state) |
| Evaluation window | None — no realized observations available; closed-observation count remains < 20 |

## What Worked

- Loop ran end-to-end against reference-state inputs; no agent returned an empty artifact.
- Risk committee correctly distinguished the 5% single-name cap *spec tension* from a sizing error and escalated it instead of trying to fix it autonomously.
- All numeric fields tagged `ILLUSTRATIVE_REF`; calendar-dependent fields tagged `N/A`. Non-fabrication contract preserved by **disclosed reference state + banner tags**, not by suppressing output.

## What Failed (And Was Fixed Today)

**Loop bug fixed (in scope of `evolution_policy.md` §Allowed Mutation Scope items 1-3):** Prior `ILLUSTRATIVE_MODE` runs (e.g., 2026-05-12, plus the first pass of today's run before the user flagged it) collapsed every artifact to empty `N/A`. Root cause: `eval/research_system.md` §Non-Fabrication Contract told agents what *not* to do, but the loop had no `ILLUSTRATIVE_MODE` operating procedure to tell them what to do *instead*. Result: factor agent emitted no scores, portfolio agent emitted no weights, final report had no tickers. The methodology was effectively dead-code in offline runs.

**Fix applied** (no protected rule touched):

1. `eval/research_system.md` — added §`ILLUSTRATIVE_MODE Operating Procedure` (5-rule procedure: concrete output, banner-tagged, auditable reference vintage, confidence capped at `MEDIUM`, fixed `0.80` DQ multiplier, `REVIEW_ONLY` publication).
2. `loop/01_data_regime_agent.md` — added `ILLUSTRATIVE_MODE` branch: declare reference vintage, classify regime against reference state, build non-empty universe.
3. `loop/02_factor_scoring_agent.md` — added `ILLUSTRATIVE_MODE` branch: run full ranking against reference state, fixed DQ multiplier, cap confidence at `MEDIUM`, surface 5-10 names. Empty tables explicitly forbidden.
4. `loop/03_portfolio_construction_agent.md` — added `ILLUSTRATIVE_MODE` branch: build a real portfolio inside all hard caps; orchestrator publishes `REVIEW_ONLY`. Empty weights explicitly forbidden.

These edits clarify wording and sequencing within the allowed mutation scope. **No protected rule** in `evolution_policy.md` §Protected Rules is weakened. In particular, the 5% single-name cap (item 3) is **not** modified — instead, the run *surfaces* a long-standing tension between the 5% cap and the 5-10-name sleeve construction and escalates it to the next monthly structural review.

## Primary Diagnosis

**Output clarity** (loop-level). The fix is structural: a missing operating procedure for an explicitly-supported mode. No factor calibration, regime classification, or risk-review change is proposed today.

## Proposed Change (For Monthly Review, Not Autonomous Adoption)

**Spec tension to resolve at the next monthly structural review:** the 5% single-name cap is geometrically incompatible with a 5-10-name sleeve sized to 100% of equity NAV (10 × 5% = 50%). Two consistent readings exist (sleeve-relative vs NAV-relative). Both are infeasible against the rest of the constraint set as currently written.

Recommended structural-review options:

- **Option A**: Canonize sleeve-relative and raise the single-name cap to 10-20% (typical focused-sleeve practice).
- **Option B**: Canonize NAV-relative, accept that the equity sleeve is a fraction of NAV, and add a benchmark / cash overlay rule so portfolio beta can stay in the 0.90-1.10 band.

Either is a humans-only decision per `evolution_policy.md` §Protected Rules. Today's run does **not** make this change; it documents the tension.

## Hypothesis

The loop fix should change `ILLUSTRATIVE_MODE` runs from "empty REVIEW_ONLY" to "populated, internally consistent, audit-friendly REVIEW_ONLY," with no impact on live-mode behavior. Falsifiable check: a future live run must continue to publish `GO` / `NO_TRADE` / `HALTED` exactly as before; only `ILLUSTRATIVE_MODE` runs change shape.

## Validation Method

| Check | Result |
|---|---|
| Holdout window used | None — fix changes presentation in `ILLUSTRATIVE_MODE`, not ranking logic in live mode |
| IR delta | `N/A` — no portfolio is sized in live mode by this change |
| Hit-rate delta | `N/A` |
| Drawdown delta | `N/A` |
| Turnover delta | `N/A` |
| Schema integrity (file purposes per `daily_output_spec.md`) | Pass — file purposes unchanged |
| Protected-rule check | Pass — none of the 8 protected rules in `evolution_policy.md` §Protected Rules are touched |
| Non-fabrication contract | Pass — preserved by reference-vintage disclosure + `ILLUSTRATIVE_REF` tagging |

## Decision

- Loop fix (`ILLUSTRATIVE_MODE` operating procedure + three agent-prompt branches): **`ACCEPT`**. In scope of `evolution_policy.md` §Allowed Mutation Scope items 1, 2, 3.
- 5% single-name cap structural tension: **`DEFER`** to next monthly structural review (humans-only per protected rules).
- All other thresholds, weights, and scoring logic: **`NO_CHANGE_ACCEPTED`** (closed-observation count < 20, per `stop_criteria.md` §Self-Evolution Stop item 1).

## Effective Next-Step Instruction

- The four edited files take effect on the next run. Re-run on Tue 2026-05-26 (live or illustrative) to confirm `ILLUSTRATIVE_MODE` produces fully populated artifacts and live mode is unchanged.
- Add the 5% cap tension to the next monthly structural review agenda.
- Resume normal evolution candidacy (threshold/weight mutation) once a live data feed is wired and ≥ 20 closed observations exist.

---

## Addendum (same-day fix #2): Empty `Days→Earnings` silently disabled the 14d earnings penalty

User flagged that the `Days→Earnings` column was N/A across the artifact set. Root cause: the original ILLUSTRATIVE_MODE OP (committed earlier today) said *"calendar-dependent fields … remain N/A because the reference state cannot supply them."* That conflated two different field classes:

- **Structural cadence** (next earnings date, FOMC schedule, dividend dates, expiry calendar) — derivable from a stable historical pattern, reference-state knowable.
- **Intra-day live tape** (today's spot, today's bid-ask, today's IV30) — genuinely requires a feed.

Treating them identically silently disabled the 14-day earnings penalty in `eval/research_system.md` §Risk Controls. The penalty cannot fire if the column is N/A. AVGO (~12d to print on reference cadence as of 2026-05-24) was sized at 10% of the book in the prior pass with no event-risk markdown. NVDA (~3d) was excluded for crowding/correlation, not for the print.

### Fix applied

| File | Change | Mutation scope |
|---|---|---|
| `eval/research_system.md` | §ILLUSTRATIVE_MODE OP item 3 split into structural-cadence (allowed, must populate) vs intra-day live (N/A) | item 1 (prompt clarity) |
| `loop/02_factor_scoring_agent.md` | Required `days_to_earnings` from reference cadence with `±5d` drift; apply penalty at `≤19d`; `LOW` confidence cap inside the window | items 1, 5 (prompt clarity, scoring threshold within hypothesis) |
| `04_factor_scores.md` | DTE column populated; AVGO −0.10 ER penalty applied; rank table reordered (AVGO drops from #3 to #6 within the investable subset) | output schema (item 2) |
| `05_top_candidates.md` | DTE column populated; AVGO confidence `LOW`; thesis section flagged event-risk note | output schema (item 2) |
| `06_portfolio_proposal.md` | AVGO 10% → 5% skip-the-print; freed 5% redistributed UNH +2 / GE +2 / LIN +1; analytics recomputed (β 1.01→0.99, DD 7.9%→7.5%, max sector 23% Comm Svcs → 25% HC) | output schema (item 2) |
| `07_risk_review.md` | New §2b: earnings-event discipline restored; future empty DTE column should `HALTED`-fail, not silently publish | output schema (item 2) |
| `08_final_report.md` | Top-candidates table, portfolio analytics, sector concentration all updated | output schema (item 2) |

No protected rule in `evolution_policy.md` §Protected Rules is touched. The 14-day earnings policy and all hard caps are unchanged; the fix wires them up correctly in `ILLUSTRATIVE_MODE` instead of leaving them inert.

### Hypothesis (falsifiable)

Populating `days_to_earnings` from reference cadence reduces silent-failure risk in `ILLUSTRATIVE_MODE` runs without overstating data quality. Falsifiable check: any future case where the cadence-derived DTE is > 5 days off the actual print date for one of the eight names — would force widening the drift band beyond `±5d`.

### Validation

| Check | Result |
|---|---|
| Schema integrity (`daily_output_spec.md` file purposes) | Pass — file purposes unchanged |
| Protected-rule check | Pass |
| Non-fabrication contract | Pass — `±5d` band tagged in every populated cell; intra-day live fields still N/A |
| Penalty fires correctly | Pass — AVGO flagged at 12d, sized at 5% (skip-the-print); NVDA excluded for 3d print + crowding |
| Portfolio constraints | Pass — β 0.99, DD ~7.5%, sector cap honored |

### Decision

`ACCEPT` for the OP amendment + `02` agent prompt patch + downstream regeneration. In scope of `evolution_policy.md` §Allowed Mutation Scope items 1, 2, and 5.

### Forward Guard

Add to `loop/04_risk_committee_agent.md` at next monthly review: an empty `Days→Earnings` column in any candidate table should be treated as a regression and trigger `HALTED`, not a silent `REVIEW_ONLY` publication. Today's evolution log records this as a pending check; not auto-applied because changing the risk-committee escalation logic is structural, not output-schema, and warrants human review.
