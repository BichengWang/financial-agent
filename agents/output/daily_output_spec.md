# Daily Output Specification

Every run writes to a dated folder:

`output/{model-name}-{YYYY-MM-DD}/`

Example:

`output/claude-opus-4-6-2026-03-16/`

## Required File Layout

| File | Purpose |
|---|---|
| `00_run_manifest.md` | Start time, mode, data status, orchestrator state, and artifact checklist |
| `01_preflight.md` | Data coverage, freshness, validation summary, and mandatory Source Ledger |
| `02_reflection.md` | Standalone month-over-month reflection and carry-forward decisions |
| `03_regime_and_data.md` | Regime label, evidence, macro context |
| `04_universe_summary.md` | Universe counts, exclusions, rejection reasons |
| `05_factor_scores.md` | Ranked factor output and score methodology notes |
| `06_top_candidates.md` | Investable candidates and near misses |
| `07_portfolio_proposal.md` | Weights, sizing logic, portfolio analytics |
| `08_risk_review.md` | Risk committee decision and concerns |
| `09_final_report.md` | Final publishable report, including a summary of `02_reflection.md` |
| `10_midday_monitor.md` | Midday exception log |
| `11_preclose_check.md` | Pre-close confirmation or escalation |
| `12_close_log.md` | Close snapshot, realized notes, open questions |
| `13_evolution_log.md` | Daily self-evolution review |

Optional on review windows:

| File | Purpose |
|---|---|
| `14_weekly_review.md` | Friday post-close parameter review |
| `15_monthly_review.md` | Structural review and broader prompt changes |

## File-Level Requirements

### `00_run_manifest.md`

Must include:

- Date
- Run mode
- Top-level status target
- Data mode
- Agents executed
- Outstanding blockers
- selected reflection baseline path and any baseline flag:
  - `NO_PRIOR_BASELINE`,
  - `CROSS_MODEL_BASELINE`,
  - `BASELINE_WINDOW_GAP`
- Source Ledger coverage summary:
  - count of observed, derived, inferred, illustrative, and unavailable rows,
  - unresolved critical fields,
  - whether the run is eligible for `GO`, `REVIEW_ONLY`, `NO_TRADE`, or `HALTED`

### `01_preflight.md`

Must include a `Source Ledger` section before any agent uses facts downstream.

Required schema:

| artifact | field | ticker/entity | value | unit | observation_date | source | freshness_tag | claim_type | used_by |
|---|---|---|---|---|---|---|---|---|---|

Allowed `freshness_tag` values:

- `LIVE`
- `DELAYED`
- `OFFICIAL_FILING`
- `HISTORICAL`
- `ILLUSTRATIVE_REF`
- `UNAVAILABLE`

Allowed `claim_type` values:

- `OBSERVED`
- `DERIVED`
- `INFERRED`
- `ILLUSTRATIVE`
- `UNAVAILABLE`

Each derived row must name its formula and input ledger rows in `source` or `used_by`. If a critical field has no source, set `value = UNAVAILABLE` rather than estimating.

### `02_reflection.md`

Must include the six required reflection sections from `../prompt/main.md`. Every price, return, regime observation, and thesis-validation claim must cite Source Ledger rows or be marked `UNAVAILABLE`.

### `09_final_report.md`

Must include:

1. Header with date and run status.
2. Executive summary.
3. `MoM Reflection Summary` section summarizing `02_reflection.md`, not replacing it.
4. Regime assessment.
5. Candidate table.
6. Portfolio analytics or no-trade rationale.
7. Assumptions and limitations.
8. Next scheduled review time.

### `13_evolution_log.md`

Must include:

- What went wrong or right.
- Proposed change.
- Test method.
- Test result.
- Decision.
- Effective date if accepted.

## Output Naming Rules

1. Use two-digit numeric prefixes to keep files ordered.
2. Do not overwrite previous dates.
3. If a run halts early, still create the model-date folder and publish all completed artifacts.
4. If a file does not apply, create it with a short explanation instead of omitting it.

## Daily Schedule To Output Mapping

Each scheduled stage in `daily_schedule.md` must map to a concrete artifact in the dated output folder. This ensures the daily run is auditable even when the result is `NO_TRADE` or `HALTED`.

The prior-month reflection is always a standalone `02_reflection.md` artifact. It may also be summarized in `00_run_manifest.md` and `09_final_report.md`, but those summaries do not replace the standalone artifact.
