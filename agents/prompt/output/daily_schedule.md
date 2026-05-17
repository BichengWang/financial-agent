# Daily Run Schedule

Use Eastern Time and skip U.S. market holidays unless you are explicitly running a simulation.

## Standard Weekday Cadence

| Time | Stage | Owner | Required Output |
|---|---|---|---|
| 06:30 | Run manifest and preflight start | Orchestrator | `00_run_manifest.md` |
| 06:33 | Prior-month reflection checkpoint | Orchestrator | `00_run_manifest.md` (embedded reflection summary) |
| 06:35 | Data freshness and regime assessment | Data and Regime Agent | `01_preflight.md`, `02_regime_and_data.md`, `03_universe_summary.md` |
| 06:50 | Factor scoring and ranking | Factor Scoring Agent | `04_factor_scores.md`, `05_top_candidates.md` |
| 07:10 | Portfolio construction | Portfolio Construction Agent | `06_portfolio_proposal.md` |
| 07:20 | Risk committee review | Risk Committee Agent | `07_risk_review.md` |
| 07:30 | Final publish decision | Orchestrator | `08_final_report.md` (must include `MoM Reflection`) |
| 12:15 | Midday exception review | Orchestrator or Risk Committee Agent | `09_midday_monitor.md` |
| 15:45 | Pre-close check | Orchestrator | `10_preclose_check.md` |
| 16:20 | Close log and outcome capture | Orchestrator | `11_close_log.md` |
| 17:00 | Daily evolution pass | Evolution Agent | `12_evolution_log.md` |

## Weekly And Monthly Cadence

| Time | Stage | Owner | Required Output |
|---|---|---|---|
| Friday 17:15 | Weekly parameter review | Evolution Agent | `13_weekly_review.md` |
| Last trading day of month 17:30 | Structural review | Evolution Agent | `14_monthly_review.md` |

## Scheduling Rules

1. The 07:30 publish slot is the default final recommendation time.
2. The prior-month reflection happens before new factor scoring and does not create a standalone file.
3. If the run is `NO_TRADE` or `HALTED`, still publish the output package on schedule.
4. Midday and pre-close reviews do not change the morning thesis unless a stop criterion is triggered.
5. The evolution pass never edits protected rules automatically.

## Minimum Daily Deliverables

Every weekday run must produce at least:

1. Run manifest.
2. Embedded prior-month reflection.
3. Regime and preflight note.
4. Top candidates or explicit no-trade logic.
5. Portfolio proposal or no-trade decision.
6. Risk review.
7. Final report.
8. Close log.
9. Evolution log.
