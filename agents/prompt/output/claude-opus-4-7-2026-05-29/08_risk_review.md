# 08 Risk Review

⚠️ ILLUSTRATIVE — NOT LIVE DATA. Committee decision is conditioned on the methodology demonstration; not a live execution approval.

## Committee Decision

**`APPROVE`** for publication as `REVIEW_ONLY`. The methodology is internally consistent, the carry-forward decision (AVGO drop) is correctly driven by the reference cadence + 19-day buffered earnings window, and all hard caps are honored except the documented 5% single-name cap tension which is being escalated rather than relaxed. The committee does **not** authorize live execution and reinforces the orchestrator's `REVIEW_ONLY` publication status. Per `eval/research_system.md` §ILLUSTRATIVE_MODE OP item 5, `GO` is foreclosed by the data-lineage state.

## Top Three Concerns (Severity Order)

### 1. The 5% Single-Name Cap Tension Persists And Is Now Marginally Worse

The 5% cap in `research_system.md` §Risk Controls is breached on **every** position; max breach is LIN at 22.0% (up from 21.0% on 05-24, +1pp from AVGO pro-rata redistribution). This is a Protected Rule (item 3 in `evolution_policy.md`); autonomous mutation is forbidden.

- **Disposition**: surfaced, not relaxed. Escalated to the next monthly structural review with the same Option A (raise cap to focused-sleeve range, 15-20%) / Option B (canonize NAV-relative with cash overlay) framing recorded on 05-24.
- **Risk-committee position**: the spec issue is *structural*, not a sizing error. The portfolio construction agent has executed the only feasible 7-name allocation under any consistent reading of the constraint set. Today's escalation is appropriate.
- **What the committee will NOT accept**: a future run that silently waives the cap, fabricates a reading not currently in the spec, or "round-trips" the cap to a higher value via prompt mutation. Any such change must come from a human structural review.

### 2. Defensive Cluster Concentration Is Now 48.5% Of Weights

The defensive-growth cluster (LLY + UNH + LIN) is now 48.5% of the book (up from 46% on 05-24), driven by the pro-rata redistribution of AVGO's 5%. This is **not** a sector breach (sector cap is GICS L1, max 30%; defensive growth spans Health Care + Materials) but it is a thematic / factor concentration risk.

- **Factor-crowding test (`research_system.md` §Risk Controls Portfolio Level)**: no single factor family contributes > 50% of total conviction. Pass. Defensive concentration is a *thematic* concentration, not a *factor-family* concentration.
- **Stress scenario**: a sudden risk-on rotation that punishes low-vol / defensive-growth names would hit the book harder than on 05-24. Magnitude: a 1-sigma factor flip on the defensive-quality factor would cost the book ~70-80 bps over 1M (reference-state estimate).
- **Disposition**: accepted as the side-effect of the AVGO drop. The alternative (add NVDA at 5%) re-introduces AI-capex crowding that the AVGO drop just relieved.

### 3. Correlation-Realization Sensitivity Is Unchanged But Binding

A correlation realization at the 0.45 cap (vs 0.36 estimate) would push 95th-pctl 1M DD to ≈ 8.5%, just over the 8% cap. This sensitivity was the second reason the 05-24 run remained `REVIEW_ONLY`; it remains the second reason today.

- **Required for `GO` eligibility**: a live correlation matrix (not a reference-state estimate). Today is `ILLUSTRATIVE_MODE`; `GO` is foreclosed regardless.
- **Disposition**: documented; live-mode runs must validate the correlation estimate against actual rolling 60-day pairwise correlations before any `GO` publication.

## Non-Fabrication Audit

| Check | Result |
|---|---|
| Today's spot prices fabricated? | No — every `Price` cell is `N/A` or absent; weights are sleeve-relative |
| Today's bid-ask / IV30 fabricated? | No — all `N/A` |
| Earnings dates fabricated? | No — populated from reference quarterly cadence with `±5d` drift band; correctly used to trigger the AVGO drop |
| Realized 5-day returns invented to claim "Hit / Miss"? | No — all `Hit / Miss` entries in `02_reflection.md` §2 are `Neutral` because `REVIEW_ONLY` baselines mean no positions were taken; price cells are `UNAVAILABLE` |
| Live macro fields fabricated? | No — today's SPY/VIX/TLT/DXY all `N/A` |
| Protected rules autonomously mutated? | No — 5% cap escalated, not relaxed |

## Reading Cross-Check Against Stop Criteria

| Stop-criterion class | Triggered? | Disposition |
|---|---|---|
| `HALTED` item 1 (no live data AND not in `ILLUSTRATIVE_MODE`) | ✗ | Mode declared. |
| `HALTED` item 6 (committee finds fabricated / contradictory evidence) | ✗ | Committee finds no fabrication; evidence is internally consistent for a reference-state methodology run. |
| `NO_TRADE` item 1 (< 5 names) | ✗ | 7 names. |
| `NO_TRADE` item 4 (> 2 names with earnings inside 14d) | ✗ | 0 names inside the window. |
| `NO_TRADE` item 5 (DD > 8%) | ✗ | 7.3% estimate. |
| `REVIEW_ONLY` item 1 (stale / delayed data; methodology valid) | ✓ | This is the publish path. |

## Required Fixes Before This Could Be Live-Eligible

| Fix | Owner |
|---|---|
| Wire a live or delayed market-data adapter | Engineering / infra |
| Resolve the 5% single-name cap tension via monthly structural review (Option A or B) | Human reviewer |
| Validate reference-state correlation matrix against live rolling 60D pairwise corrs | Data agent (live mode) |
| Verify today's bid-ask, IV30, and short-interest delta for the seven names | Live-mode preflight |

## Final Publication Recommendation

**`REVIEW_ONLY`** — published per `stop_criteria.md` §Review-Only Mode item 1 and `research_system.md` §ILLUSTRATIVE_MODE OP item 5. The committee does **not** authorize live execution.

## Forward Guard (For Monthly Review)

The committee endorses today's evolution-log forward guard: an empty `Days→Earnings` column in any future candidate table should trigger `HALTED`, not a silent `REVIEW_ONLY` publication. This guard is **not** auto-applied today (changing the committee's escalation logic is structural and warrants human review per the prior 05-24 evolution log).
