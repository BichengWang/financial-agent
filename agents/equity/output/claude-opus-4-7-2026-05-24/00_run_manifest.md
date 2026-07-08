# 00 Run Manifest

| Field | Value |
|---|---|
| Date | 2026-05-24 (Sunday) |
| Calendar status | U.S. equity markets closed (weekend; Memorial Day holiday Mon 2026-05-25) |
| Run mode | Off-cycle methodology run; no live or delayed feed wired |
| Run type | `ILLUSTRATIVE_MODE` against training-data reference state |
| Reference vintage | Model training data through ~2026-01 (assistant knowledge cutoff January 2026) |
| Target status | `REVIEW_ONLY` |
| Data mode | `ILLUSTRATIVE` — every structured field tagged `ILLUSTRATIVE_REF` per `eval/research_system.md` §ILLUSTRATIVE_MODE Operating Procedure |
| Model | claude-opus-4-7 (1M context) |
| Prompt system version | v3.0 + `ILLUSTRATIVE_MODE` branch (added 2026-05-24) |
| Orchestrator file | `loop/00_orchestrator.md` |
| Agents executed | 01 data_regime → 02 factor_scoring → 03 portfolio_construction → 04 risk_committee → 05 evolution |
| Revision passes used | 0 of 1 |
| Clarifications used | 0 of 1 |
| Outstanding blockers | (1) No live market-data adapter; the run is methodology-valid but cannot be cited for live execution. (2) Closed-observation count remains < 20, so the evolution loop cannot mutate thresholds. |

## State Transition Log

| Time (ET) | State | Reason |
|---|---|---|
| 14:18 | `PRECHECK` | Boot orchestrator; load shared rules. |
| 14:19 | `DATA_OK` | `ILLUSTRATIVE` declared explicitly; reference vintage disclosed. |
| 14:20 | `SCORED` | Factor families computed against reference state with `0.80` data quality multiplier. |
| 14:20 | `PORTFOLIO_DRAFT` | 8-name illustrative book sized within all hard caps. |
| 14:20 | `RISK_REVIEW` | Committee `APPROVE`-s for `REVIEW_ONLY` publication; rejects any live citation. |
| 14:21 | `PUBLISHED` | `REVIEW_ONLY` published per `stop_criteria.md` §Review-Only Mode item 1. |
| 14:21 | `EVOLUTION_REVIEW` | Loop fix #1 logged; threshold mutation ineligible (<20 closed observations). |
| 14:55 | `RE-RUN (PARTIAL)` | User flagged empty `Days→Earnings`; ILLUSTRATIVE_MODE OP amended (structural cadence allowed); 04/05/06/07/08 regenerated; AVGO trimmed 10→5 (skip-the-print); 12 appended. |

## Final Publication Decision

`REVIEW_ONLY` — methodology valid, data is reference-state. Illustrative portfolio is shown for audit; not for execution.

## Output File Checklist

| File | Status | Note |
|---|---|---|
| `00_run_manifest.md` | written | this file |
| `01_preflight.md` | written | data coverage and validation |
| `02_regime_and_data.md` | written | regime classified against reference state |
| `03_universe_summary.md` | written | universe filter run against reference-state listed equities |
| `04_factor_scores.md` | written | four families scored against reference state |
| `05_top_candidates.md` | written | 8 illustrative candidates with full schema |
| `06_portfolio_proposal.md` | written | illustrative portfolio inside all hard caps |
| `07_risk_review.md` | written | committee `APPROVE` for `REVIEW_ONLY` |
| `08_final_report.md` | written | per template |
| `09_midday_monitor.md` | written | suppressed-but-present (markets closed) |
| `10_preclose_check.md` | written | suppressed-but-present (markets closed) |
| `11_close_log.md` | written | suppressed-but-present (markets closed) |
| `12_evolution_log.md` | written | loop fix logged |

## Non-Negotiable Compliance

- [x] No live or today-as-of prices, IVs, or earnings dates fabricated.
- [x] `ILLUSTRATIVE_MODE` declared on every artifact; every numeric field tagged `ILLUSTRATIVE_REF`.
- [x] No risk limit weakened to publish.
- [x] No protected rule mutated.
- [x] Run status emitted exactly once: `REVIEW_ONLY`.
