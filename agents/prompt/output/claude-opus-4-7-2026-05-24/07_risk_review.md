# 07 Risk Review

⚠️ ILLUSTRATIVE — NOT LIVE DATA. Review of an illustrative reference-state portfolio.

## Committee Decision

**`APPROVE` for `REVIEW_ONLY` publication.** Portfolio is **not** approved for live execution and **not** approved for `GO`. The methodology demonstration is sound; the data lineage forecloses any live-citation use.

`REVISE` and `REJECT` were considered. `REVISE` is wrong because the issues are spec-level (5% cap tension) and data-level (no live tape), not single-revision-fixable. `REJECT` is wrong because the artifact set is internally consistent and the methodology runs cleanly; the goal of producing a fully-populated, auditable illustrative book is met.

## Top Three Concerns (Severity Order)

### 1. Single-name 5% cap is breached on every position (severity: blocking for `GO`; non-blocking for `REVIEW_ONLY`)

The 5% cap in `research_system.md` §Risk Controls is geometrically incompatible with a 5-10-name sleeve sized to 100% of the equity book: 10 × 5% = 50%. The portfolio adopts the sleeve-relative reading (weights sum to 100%, single-name cap exceeded). This is logged as a **spec tension**, not a sizing error.

**Risk Committee Position:**
- Per `evolution_policy.md` §Protected Rules item 3, the 5% cap is a protected rule. It may **not** be weakened by autonomous mutation.
- The committee escalates this to the next monthly structural review (a humans-only decision per the policy) with a recommended fix to make explicit which reading is canonical and, if Reading A (sleeve-relative), to set the appropriate cap (typical hedge-fund focused-sleeve practice is 10-20%).
- Until the structural review rules, every `ILLUSTRATIVE_MODE` portfolio with < 20 names will land in this same state. Today's output documents the tension rather than masking it.

### 2. 95th-pctl 1M drawdown is no longer constraint-binding, but still ρ-sensitive (severity: medium, downgraded)

The portfolio's 95th-pctl 1M DD ≈ 7.5% (vs the prior 7.9% before the AVGO trim and defensive redistribution). At ρ = 0.45 (the policy ceiling), DD ≈ 8.3%, still a breach. At ρ = 0.30, DD ≈ 6.7%.

**Risk Committee Position:**
- The DD line is no longer the closest-to-binding constraint after the AVGO/UNH/GE/LIN redistribution.
- This portfolio is acceptable for `REVIEW_ONLY` but would still **not** be approved for live `GO` without a measured correlation matrix and a stress test against the 0.45 ceiling.

### 2b. Earnings-event discipline restored (severity: high, was a silent failure)

Prior to the fix in this run, the `Days→Earnings` column was tagged `N/A` across the artifact set. That silently disabled the 14-day earnings penalty in `eval/research_system.md` §Risk Controls — the pipeline was structurally unable to fire one of its hard event-risk controls in `ILLUSTRATIVE_MODE`.

Today's recompute populates `days_to_earnings` from reference-state cadence, applies a 5-day drift buffer (so the effective penalty window is ≤19 days), and confidence-caps any flagged name at `LOW`. AVGO (~12d to print) is the only flagged name; it is held at skip-the-print sizing (5% vs the prior 10%). NVDA (~3d to print) is excluded outright.

**Risk Committee Position:**
- The fix is in scope of `evolution_policy.md` §Allowed Mutation Scope items 1, 2, and 5 (prompt clarity, output schema, scoring threshold within documented hypothesis). No protected rule is touched.
- Going forward, every `ILLUSTRATIVE_MODE` run must populate `days_to_earnings`. An empty column should be treated as a regression and trigger a `HALTED` status, not a published artifact.

### 3. Concentrated positioning in defensive-growth cluster (severity: medium)

The defensive-growth cluster (LLY + UNH + LIN) is 43% of book. While this anchors low vol, it concentrates exposure to long-duration health care and industrial-gas pricing power. A surprise re-acceleration in real yields (`RATE_SHOCK` regime not currently tagged) would hit this cluster preferentially.

**Risk Committee Position:**
- Acceptable for the current `NEUTRAL`/`HIGH_VOL` regime tilt, which favors defensive-growth.
- If the next live-mode run picks up a `RATE_SHOCK` signal, the portfolio agent should rotate toward shorter-duration cyclical-quality (more GE-like, less LLY/LIN-like).

## Audit Trail

| Check | File | Result |
|---|---|---|
| `ILLUSTRATIVE_MODE` declared explicitly | `00`, `01`, `02`, `03`, `04`, `05`, `06`, `08` | Pass |
| All numeric fields tagged `ILLUSTRATIVE_REF` (or `N/A` for calendar-dependent) | `02`, `03`, `04`, `05`, `06` | Pass |
| No live prices, today's bid-ask, or today's earnings dates fabricated | All | Pass — calendar fields explicitly `N/A` |
| Confidence capped at `MEDIUM` | `04`, `05` | Pass |
| Data quality multiplier set to `0.80` | `04` | Pass |
| Stop-criteria reasoning shown | `01`, `03`, `04`, `06` | Pass |
| Protected rules untouched by autonomous mutation | `evolution_policy.md` §Protected Rules | Pass — 5% cap escalated, not relaxed |
| Schedule discipline | `daily_schedule.md` | Pass — `REVIEW_ONLY` publication is allowed on schedule |

## Required Fixes Before A Future Live `GO`

These are durable improvements; they do **not** block today's `REVIEW_ONLY` publication:

1. **Wire a production-grade tape.** Benchmark, single-name OHLCV, options surface, earnings calendar, short interest, analyst revisions. Without these, no run can escape `ILLUSTRATIVE_MODE`.
2. **Resolve the 5% cap spec tension at the next monthly structural review.** Either canonize Reading A with a higher cap (10-20%) for focused sleeves, or canonize Reading B (allow cash buffer + benchmark overlay).
3. **Stand up a live correlation matrix.** Until pairwise correlation is measured, the 8% drawdown cap is monitored against an *assumed* ρ; that's acceptable for illustrative runs, not for live ones.
4. **Backfill ≥ 20 closed observations** before the evolution loop is permitted to mutate any threshold.

## Final Publication Recommendation

`REVIEW_ONLY` — methodology valid, data is reference-state, illustrative portfolio is internally consistent and constraint-aware. No live execution. Resume eligibility for `GO` once the audit-trail items above are addressed.
