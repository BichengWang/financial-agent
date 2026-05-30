# Daily Output Specification

Every run writes to a dated folder:

`output/{model-name}-{YYYY-MM-DD}/`

Example:

`output/claude-opus-4-6-2026-03-16/`

## Required File Layout

| File | Purpose |
|---|---|
| `00_run_manifest.md` | Start time, mode, data status, orchestrator state, and embedded prior-month reflection summary |
| `01_preflight.md` | Data coverage, freshness, validation summary |
| `02_regime_and_data.md` | Regime label, evidence, macro context |
| `03_universe_summary.md` | Universe counts, exclusions, rejection reasons |
| `04_factor_scores.md` | Ranked factor output and score methodology notes |
| `05_top_candidates.md` | Investable candidates and near misses |
| `06_portfolio_proposal.md` | Weights, sizing logic, portfolio analytics |
| `07_risk_review.md` | Risk committee decision and concerns |
| `08_final_report.md` | Final publishable report, including a fuller month-over-month reflection |
| `09_midday_monitor.md` | Midday exception log |
| `10_preclose_check.md` | Pre-close confirmation or escalation |
| `11_close_log.md` | Close snapshot, realized notes, open questions |
| `12_evolution_log.md` | Daily self-evolution review |

Optional on review windows:

| File | Purpose |
|---|---|
| `13_weekly_review.md` | Friday post-close parameter review |
| `14_monthly_review.md` | Structural review and broader prompt changes |

## File-Level Requirements

### `00_run_manifest.md`

Must include:

- Date
- Run mode
- Top-level status target
- Data mode
- Agents executed
- Outstanding blockers
- `Prior-Month Reflection` section with:
  - baseline package path,
  - prior run status,
  - carry-forward decisions,
  - downgrade / removal decisions

### `08_final_report.md`

Must include:

1. Header with date and run status.
2. Executive summary.
3. `MoM Reflection` section tying the prior-month run to the current thesis.
4. Regime assessment.
5. Candidate table.
6. Portfolio analytics or no-trade rationale.
7. Assumptions and limitations.
8. Next scheduled review time.

### `12_evolution_log.md`

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

The prior-month reflection is mandatory when a same-model package from roughly one month earlier exists, but it must be embedded inside existing artifacts rather than written to a standalone new file.
