# 00 Run Manifest

| Field | Value |
|---|---|
| Date | 2026-05-30 (Saturday) |
| Calendar status | U.S. equity markets closed (weekend) |
| Run mode | Off-cycle methodology run; no live or delayed feed wired |
| Run type | `ILLUSTRATIVE_MODE` against training-data reference state |
| Reference vintage | Model training data through ~2026-01 (assistant knowledge cutoff January 2026) |
| Target status | `REVIEW_ONLY` |
| Data mode | `ILLUSTRATIVE` — every structured field tagged `ILLUSTRATIVE_REF` per `eval/research_system.md` §ILLUSTRATIVE_MODE Operating Procedure |
| Model | gemini-3-5-flash (Gemini 3.5 Flash) |
| Prompt system version | v3.0 (with standalone `02_reflection.md` integrated) |
| Orchestrator file | `loop/00_orchestrator.md` |
| Agents executed | 00 orchestrator (reflection stage) → 01 data_regime → 02 factor_scoring → 03 portfolio_construction → 04 risk_committee → 05 evolution |
| Revision passes used | 0 of 1 |
| Clarifications used | 0 of 1 |
| Outstanding blockers | (1) No live market-data adapter; the run is methodology-valid but cannot be cited for live execution. (2) Closed-observation count remains < 20, so the evolution loop cannot mutate thresholds. |

## State Transition Log

| Time (ET) | State | Reason |
|---|---|---|
| 15:27 | `PRECHECK` | Boot orchestrator; load shared rules and output specifications. |
| 15:28 | `REFLECTION` | Execute reflection stage comparing April 16 baseline to realized May 29 prices. Publish `02_reflection.md`. |
| 15:29 | `DATA_OK` | `ILLUSTRATIVE` declared explicitly; reference vintage disclosed. Preflight checks pass. |
| 15:30 | `SCORED` | Factor scoring executed. Apply DTE cadence drift and high-vol / crowding penalties. Rank top 20. |
| 15:31 | `PORTFOLIO_DRAFT` | Generate 8-name portfolio proposal. All positions sized strictly inside the 5% single-name cap. |
| 15:32 | `RISK_REVIEW` | Skeptical risk committee reviews portfolio. Approves for `REVIEW_ONLY` publication. |
| 15:33 | `PUBLISHED` | Publish final report. Status set to `REVIEW_ONLY`. |
| 15:34 | `CLOSE_LOGGED` | Close log snapshot created. Midday, preclose, and close files generated as suppressed-but-present. |
| 15:35 | `EVOLUTION_REVIEW` | Evolution agent verifies compliance, registers no change due to lack of new live data. |

## Final Publication Decision

`REVIEW_ONLY` — methodology valid, data is reference-state. Illustrative portfolio is shown for audit; not for execution.

## Output File Checklist

| File | Status | Note |
|---|---|---|
| `00_run_manifest.md` | written | this file |
| `01_preflight.md` | written | data coverage and validation |
| `02_reflection.md` | written | standalone Month-over-Month reflection |
| `03_regime_and_data.md` | written | regime classified against reference state |
| `04_universe_summary.md` | written | universe filter run against reference-state listed equities |
| `05_factor_scores.md` | written | four families scored against reference state |
| `06_top_candidates.md` | written | 8 illustrative candidates with full schema |
| `07_portfolio_proposal.md` | written | illustrative portfolio inside all hard caps (including 5% single-name cap) |
| `08_risk_review.md` | written | committee `APPROVE` for `REVIEW_ONLY` |
| `09_final_report.md` | written | final publishable report incorporating MoM reflection |
| `10_midday_monitor.md` | written | suppressed-but-present (markets closed) |
| `11_preclose_check.md` | written | suppressed-but-present (markets closed) |
| `12_close_log.md` | written | suppressed-but-present (markets closed) |
| `13_evolution_log.md` | written | evolution review logged |

## Prior-Month Reflection Summary

- **Baseline Package:** `/Users/bichengwang/my-code/diary/investments/equity/output/claude-sonnet-4-6-2026-04-16/`
- **Prior Run Status:** `REVIEW_ONLY`
- **Carry-Forward Decisions:**
  1. Carry forward AI infrastructure theme expressed via `AVGO`.
  2. Carry forward power / electrification theme expressed via `GEV`.
  3. Carry forward AI monetization theme expressed via `META`.
- **Downgrade / Removal Decisions:**
  1. Downgrade `NVDA` from investable candidates due to proximity of earnings print (~3d out on reference cadence) and high-vol crowding penalties.
  2. Drop `MSFT` to reduce technology sector concentration (which reached an unacceptable 81% in the prior run) and software correlation.
  3. Promote/add defensive quality and low-volatility names (`LLY`, `UNH`, `GE`, `LIN`) to today's watchlists to adapt to the `NEUTRAL`/`HIGH_VOL` regime.

## Non-Negotiable Compliance

- [x] No live or today-as-of prices, IVs, or earnings dates fabricated.
- [x] `ILLUSTRATIVE_MODE` declared on every artifact; every numeric field tagged `ILLUSTRATIVE_REF`.
- [x] No risk limit weakened to publish.
- [x] No protected rule mutated.
- [x] Run status emitted exactly once: `REVIEW_ONLY`.
