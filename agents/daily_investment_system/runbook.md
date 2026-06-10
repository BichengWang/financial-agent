# Runbook — Schedule, Scheduler, and Output Specification

Single source of truth for run timing, the scheduling mechanism, and the dated artifact package. Eastern Time throughout.

## Cadence (weekdays)

| Time (ET) | Stage | Owner | Output | Scheduled? |
|---|---|---|---|---|
| 07:27 | Pre-open publish — full pipeline | Orchestrator | `00`–`09`, `13`, `15` | **No job active** — recreate per § Scheduler |
| 12:15 | Midday monitor | Orchestrator | `10_midday_monitor.md` | No (manual) |
| 15:45 | Pre-close check | Orchestrator | `11_preclose_check.md` | No |
| 16:20 | Close log | Orchestrator | `12_close_log.md` | No |
| 17:00 | Daily evolution review | Evolution Agent | `13_evolution_log.md` (if not folded into 07:27) | No |
| Fri 17:15 | Weekly parameter review | Evolution Agent | `14_weekly_review.md` | No |
| Month-end 17:30 | Structural review | Evolution Agent | `16_monthly_review.md` | No |

Rules: U.S. market holidays still publish an `ILLUSTRATIVE_MODE` `REVIEW_ONLY` artifact set — no skipped days in the audit trail. `NO_TRADE` / `REVIEW_ONLY` / `HALTED` runs still publish on schedule. Midday and pre-close reviews change nothing unless a stop criterion fires.

## Scheduler

- **Current: none active.** The last durable job (`56841f5d`, created 2026-05-24 on the previous machine) expired; `.claude/scheduled_tasks.json` is empty. Runs are manual until recreated.
- **Recreate:** Claude Code `CronCreate`, cron `27 7 * * 1-5`, durable, with a self-contained prompt that executes `investments/equity/daily_investment_system/main.md` (repo-relative — never hardcode a `/Users/...` machine path; that killed the previous job).
- Recurring `CronCreate` jobs auto-expire **7 days** after creation → recreate weekly. Jobs fire only while the REPL is idle; recurring jobs do not catch up missed fires. 07:27 (off-minute) avoids minute-zero pile-up.
- **Permanent promotion path:** (1) macOS launchd plist invoking `claude -p` on the repo-relative `main.md` — survives reboots, no expiry; (2) GitHub Actions cron that commits the dated folder back — doubles as a regression harness for the prompt stack.

## Output Location and Naming

Every run writes to `investments/equity/output/{model-name}-{YYYY-MM-DD}/` (repo-relative; `../output/` from this directory). `{model-name}` is the executing model's id (e.g. `gpt-5`, `claude-fable-5`); the date is the actual run date.

1. Two-digit prefixes keep files ordered.
2. Never overwrite a previous date's folder.
3. A halted run still creates the folder and publishes every completed artifact.
4. A file that does not apply is created with a one-line explanation, never omitted.

## Artifact Table

| # | File | Owner | Required |
|---|---|---|---|
| 00 | `00_run_manifest.md` | Orchestrator | Always |
| 01 | `01_preflight.md` | Orchestrator | Always — mandatory Source Ledger |
| 02 | `02_reflection.md` | Orchestrator (Reflection stage) | Always — settlement + MoM table |
| 03 | `03_regime_and_data.md` | Data/Regime Agent | Always |
| 04 | `04_universe_summary.md` | Factor Scoring Agent | Always |
| 05 | `05_factor_scores.md` | Factor Scoring Agent | Always |
| 06 | `06_top_candidates.md` | Portfolio Construction Agent | Always |
| 07 | `07_portfolio_proposal.md` | Portfolio Construction Agent | Always |
| 08 | `08_risk_review.md` | Risk Committee Agent | Always |
| 09 | `09_final_report.md` | Orchestrator | Always |
| 10–12 | midday / preclose / close | Orchestrator | Scheduled checkpoints |
| 13 | `13_evolution_log.md` | Evolution Agent | Always |
| 14 | `14_weekly_review.md` | Evolution Agent | Friday after close |
| 15 | `15_predictions.json` | Orchestrator | **Always when any name is ranked — publishing gate** |
| 16 | `16_monthly_review.md` | Evolution Agent | Last trading day of month |

## Per-Artifact Requirements

### `00_run_manifest.md`
Date, run mode, data mode, status target and final status, agents executed, outstanding blockers; reflection baseline path + flag (`NO_PRIOR_BASELINE` / `CROSS_MODEL_BASELINE` / `BASELINE_WINDOW_GAP` / `NO_VALID_MOM_BASELINE`); prediction-settlement summary (count settled, or `NO_PREDICTION_LEDGER`); Source Ledger coverage counts (observed/derived/inferred/illustrative/unavailable) and status eligibility; **GO-Gate Table** — one row per Required input from `rules.md § Input Classification`, each grounded or failed-with-attempt, with missing Enhancing inputs listed separately as confidence/exposure caps (never as GO blockers); artifact checklist including `15_predictions.json`.

### `01_preflight.md`
Source Ledger before any agent uses facts downstream. Schema:

| artifact | field | ticker/entity | value | unit | observation_date | source | freshness_tag | claim_type | used_by |
|---|---|---|---|---|---|---|---|---|---|

Allowed `freshness_tag` / `claim_type` values: `rules.md § Source Ledger Contract` (single source). Derived rows cite formula + input rows; a critical field with no source is `UNAVAILABLE`, never estimated.

### `02_reflection.md`
Standalone MoM reflection, sections in order. Every price, return, regime, and thesis-validation claim cites `01` ledger rows or is `UNAVAILABLE` / explicitly `INFERRED`.

0. **Prediction Settlement** — settled table `Ticker | Vintage | Entry | Target Date | mu | Realized Return | SPY Return | Alpha | Direction | CI Result | z`; rolling calibration metrics (or `INSUFFICIENT_SETTLED_N`); which prior `15_predictions.json` files were scanned.
1. **Prior Run Summary** — date, model, final status, regime, portfolio or basket, top-5 scores.
2. **MoM Price & Return Table** — `| Ticker | Prior Date | Prior Price | Current Date | Current Price | MoM Return | SPY Return | Alpha | Hit/Miss | Notes |`. Hit/Miss is alpha-based per `rules.md § Settlement Rules`; `Neutral` applies to position-P&L accounting only and is never a substitute for forecast scoring — a name ranked in a `REVIEW_ONLY` run is still a forecast. State `IN_CI`/`OUT_CI` when a CI was recorded. `APPROX - sourced` only with source + observation date; otherwise `UNAVAILABLE`.
3. **Theme-Level Performance** — validated / partial / failed per prior theme, with evidence.
4. **Regime Shift Assessment** — prior vs current regime and factor-weight implications.
5. **Carry-Forward Decisions** — `| Ticker/Theme | Prior Score | Prior Thesis | MoM Return | Decision | Rationale |`; decisions `CARRY` / `DOWNGRADE` / `DROP` / `PROMOTE`. Binding on factor scoring when ledger-backed; `DROP` names stay out of today's scored set absent new ledger evidence.
6. **Sign-Off** — freshness tag per price used, reflection confidence (HIGH/MEDIUM/LOW) with rationale, structural issues found.

### `09_final_report.md`
Header banner:

```text
══════════════════════════════════════════════════════
QUANTITATIVE EQUITY SELECTION REPORT — [YYYY-MM-DD]
Run Status: [GO | NO_TRADE | REVIEW_ONLY | HALTED]
Classification: INTERNAL — INVESTMENT COMMITTEE USE
══════════════════════════════════════════════════════
```

Then: executive summary (≤ 5 sentences); MoM Reflection Summary (summarizes `02`, introduces no new facts); regime table (regime, data quality, key macro risk — with ledger rows); ranked candidate table; portfolio analytics or no-trade rationale; assumptions and limitations; next scheduled review.

### `13_evolution_log.md`
Run context (date, status, regime, evaluation window, ledger status, baseline flag); what worked / what failed; primary diagnosis (one of: data quality, regime classification, factor calibration, portfolio construction, risk review, output clarity, source grounding); exactly one proposed change with **Track A/B classification** per `rules.md § Evolution Policy`; hypothesis; validation (Track A: holdout/IR/hit-rate/drawdown/turnover deltas; Track B: the three-condition standard); decision `ACCEPT` / `REJECT` / `DEFER` / `NO_CHANGE_ACCEPTED`; effective next step.

### `15_predictions.json`
Required whenever any name is ranked — investable or monitoring sleeve, **every** run status including `REVIEW_ONLY` and `ILLUSTRATIVE`. One record per ranked name per `rules.md § Prediction Ledger`; plus a `settlements` block with every prediction settled this run (or `"settlements": []` and a `NO_PREDICTION_LEDGER` note). Valid JSON, no markdown wrapper. A run that ranks names is not publishable without this file.
