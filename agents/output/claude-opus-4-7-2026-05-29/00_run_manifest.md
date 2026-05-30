# 00 Run Manifest

| Field | Value |
|---|---|
| Date | 2026-05-29 (Friday) |
| Timezone | America/New_York |
| Calendar status | U.S. equity markets **open** (Memorial Day was Mon 2026-05-25); this is the 4th trading day of the post-holiday week and the Friday weekly-review day |
| Run mode | `SCHEDULED_DAILY` — cron `56841f5d`, 07:27 ET pre-open publish slot, weekdays |
| Run type | `ILLUSTRATIVE_MODE` against training-data reference state (no live or delayed market-data adapter wired) |
| Reference vintage | Model training data through ~2026-01 (assistant knowledge cutoff January 2026) |
| Target status | `REVIEW_ONLY` |
| Data mode | `ILLUSTRATIVE` — every structured field tagged `ILLUSTRATIVE_REF` per `eval/research_system.md` §ILLUSTRATIVE_MODE Operating Procedure |
| Model | claude-opus-4-7 (1M context, `/effort max`) |
| Prompt system version | v3.0 + `ILLUSTRATIVE_MODE` branch (committed 2026-05-24) |
| Orchestrator file | `loop/00_orchestrator.md` |
| Agents executed | Reflection (orchestrator-owned) → 01 data_regime → 02 factor_scoring → 03 portfolio_construction → 04 risk_committee → 05 evolution |
| Revision passes used | 0 of 1 |
| Clarifications used | 0 of 1 |
| Outstanding blockers | (1) No live market-data adapter; the run is methodology-valid but cannot be cited for live execution. (2) Closed-observation count remains < 20, so the evolution loop cannot mutate thresholds. (3) Spec tension between `main.md` (14-file layout, standalone `02_reflection.md`) and `daily_output_spec.md` (13-file layout, embedded reflection) — escalated, see §Spec Tensions. |

## State Transition Log

| Time (ET) | State | Reason |
|---|---|---|
| 07:27 | `PRECHECK` | Cron fired; orchestrator loaded shared rules and daily schedule. |
| 07:27 | `REFLECTION` | Same-model MoM baseline (`2026-05-12`) loaded; 5-day cross-check baseline (`2026-05-24`) loaded; `02_reflection.md` published with mandatory MoM and carry-forward tables. |
| 07:28 | `DATA_OK` | `ILLUSTRATIVE` declared explicitly; reference vintage disclosed in `01_preflight.md`. |
| 07:28 | `SCORED` | Factor families computed against reference state with `0.80` data-quality multiplier; AVGO buffered-earnings-window flag re-applied (~7d to reference Q2 print). |
| 07:29 | `PORTFOLIO_DRAFT` | 7-name illustrative book (AVGO dropped for event-risk discipline) sized within all hard caps except the documented 5% single-name cap tension. |
| 07:29 | `RISK_REVIEW` | Committee `APPROVE`-s for `REVIEW_ONLY` publication; reinforces no live citation. |
| 07:30 | `PUBLISHED` | `REVIEW_ONLY` published per `stop_criteria.md` §Review-Only Mode item 1 and `research_system.md` §ILLUSTRATIVE_MODE OP item 5. |
| 07:30 | `CLOSE_LOGGED` | Suppressed-but-present intraday artifacts (10/11/12) written; close log will be filled by the 16:20 ET scheduled checkpoint when wired. |
| 07:30 | `EVOLUTION_REVIEW` | Daily evolution review folded into pre-open publish; Friday weekly-review hook noted; mutation ineligible (closed-observation count < 20). |

## Final Publication Decision

`REVIEW_ONLY` — methodology valid, data is reference-state. Illustrative portfolio is shown for audit; not for execution.

## Prior-Month Reflection (Summary)

Full table lives in `02_reflection.md`. Headline:

- **Primary same-model baseline**: `prompt/output/claude-opus-4-7-2026-05-12/` (17 days prior; closest available to the "approximately one month prior" target). That baseline was a structurally pre-`ILLUSTRATIVE_MODE` run with empty candidate tables, so price-level MoM is `UNAVAILABLE`; the carry-forward is *process* MoM only.
- **5-day cross-check baseline**: `prompt/output/claude-opus-4-7-2026-05-24/` (5 days prior, first run after the `ILLUSTRATIVE_MODE` operating-procedure fix). 8 names: META, LLY, NFLX, NOW, UNH, AVGO, GE, LIN. Price-level MoM is `UNAVAILABLE` against today (no live feed); thesis-level carry-forward is the binding decision.
- **Carry-forward decisions** (binding inputs to `02_factor_scoring_agent.md`):
  - `CARRY` × 7: META, LLY, NFLX, NOW, UNH, GE, LIN.
  - `DROP` × 1: **AVGO** — reference fiscal Q2 print at ~7d (was ~12d on 05-24), now deeper inside the 19-day buffered earnings window. Event-risk discipline supersedes skip-the-print sizing at this proximity. Re-rate post-print at next run on or after 2026-06-08.
  - `PROMOTE` × 0: no new names added today; the 05-24 near-miss list (NVDA, MSFT, TMO, INTU, PGR, CDNS, ADBE) was reviewed but none cleared the crowding test relative to the existing book.
- **Theme-level**: defensive-growth tilt validated (relative; reference-state only); AI-capex single-name crowding remains the principal book risk; the 05-24 near-print AVGO sizing now resolves to drop.

## Spec Tensions (Surfaced, Not Relaxed)

Per `eval/evolution_policy.md` §Protected Rules, neither item below is mutated by today's run.

1. **Output-spec layout** — `main.md` mandates a 14-file layout (`00`-`13`) with `02_reflection.md` as a **standalone** artifact (added in v3.0). `daily_output_spec.md` still describes a 13-file layout (`00`-`12`) with reflection **embedded** in `00` and `08`. The 05-12 and 05-24 runs followed the 13-file layout; the 2026-05-29 gpt-5 run already in `investments/equity/output/` followed the 14-file layout. Today's claude-opus-4-7 run follows the **14-file `main.md` layout** because today's cron prompt explicitly directs me to execute `main.md`. Resolution: file-purpose merge in `daily_output_spec.md` at the next monthly structural review — humans-only because it touches the output schema visible to downstream tooling.
2. **5% single-name cap (Protected Rule 3)** — Still geometrically incompatible with a 5-10-name sleeve sized to 100% of NAV. Today's portfolio breaches the cap on every position (max 22% LIN). The 05-24 escalation stands; no autonomous mutation.

## Output File Checklist

| File | Status | Note |
|---|---|---|
| `00_run_manifest.md` | written | this file |
| `01_preflight.md` | written | data coverage and validation, reference-vintage disclosed |
| `02_reflection.md` | written | **standalone MoM reflection per `main.md` §Reflection Stage; mandatory carry-forward table** |
| `03_regime_and_data.md` | written | regime classified against reference state |
| `04_universe_summary.md` | written | universe filter run against reference-state listed equities |
| `05_factor_scores.md` | written | four families scored against reference state; AVGO buffered-earnings penalty re-applied |
| `06_top_candidates.md` | written | 7 illustrative candidates with full schema (AVGO dropped) |
| `07_portfolio_proposal.md` | written | 7-name illustrative portfolio inside all hard caps except 5% cap tension |
| `08_risk_review.md` | written | committee `APPROVE` for `REVIEW_ONLY` |
| `09_final_report.md` | written | per template, with embedded MoM reflection cross-reference |
| `10_midday_monitor.md` | written | suppressed-but-present (no live feed) |
| `11_preclose_check.md` | written | suppressed-but-present (no live feed) |
| `12_close_log.md` | written | suppressed-but-present (no live feed) |
| `13_evolution_log.md` | written | daily evolution + Friday weekly-review hook; `NO_CHANGE_ACCEPTED` for thresholds |

## Non-Negotiable Compliance

- [x] No live or today-as-of prices, IVs, or earnings dates fabricated.
- [x] `ILLUSTRATIVE_MODE` declared on every artifact; every numeric field tagged `ILLUSTRATIVE_REF` or `N/A` per the structural-cadence vs intra-day-live split in `research_system.md` §ILLUSTRATIVE_MODE OP item 3.
- [x] No risk limit weakened to publish.
- [x] No protected rule in `evolution_policy.md` §Protected Rules mutated.
- [x] 14-day earnings policy wired through the buffered 19-day window; AVGO dropped at ~7d to print.
- [x] Run status emitted exactly once: `REVIEW_ONLY`.
- [x] No Slack/external messaging triggered (cron prompt item 7).

## Next Review

- 12:15 ET — `10_midday_monitor.md` exception review (suppressed-but-present today; no live feed).
- 15:45 ET — `11_preclose_check.md`.
- 16:20 ET — `12_close_log.md`.
- 17:00 ET — daily evolution review folded into `13_evolution_log.md` (already published in this pre-open run).
- **17:15 ET — `13_weekly_review.md`** is the Friday-cadence checkpoint per `daily_schedule.md`. Conditioned on at least one live run having produced realized data; today's condition is **not met**, so the weekly review is documented in `13_evolution_log.md` Addendum and a standalone `13_weekly_review.md` is **not** emitted.
- Next scheduled live attempt: Mon 2026-06-01 07:27 ET pre-open publish slot, contingent on a wired data feed.
