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
| support | `eligible_universe.txt` | Orchestrator / `build_index_universe.py` | Required before price-history fetch and factor scoring |
| support | `universe_summary.json` | Orchestrator / `build_index_universe.py` | Required before price-history fetch and factor scoring |
| support | `technical_indicators.json` | Orchestrator / `technical_indicators.py` | Required whenever fetched price history exists |

## Per-Artifact Requirements

### `00_run_manifest.md`
Date, run mode, data mode, status target and final status, agents executed, outstanding blockers; reflection baseline path + flag (`NO_PRIOR_BASELINE` / `CROSS_MODEL_BASELINE` / `BASELINE_WINDOW_GAP` / `NO_VALID_MOM_BASELINE`); prediction-settlement summary (count settled, or `NO_PREDICTION_LEDGER`); Source Ledger coverage counts (observed/derived/inferred/illustrative/unavailable) and status eligibility; **GO-Gate Table** — one row per Required input from `rules.md § Input Classification`, each grounded or failed-with-attempt, with missing Enhancing inputs listed separately as confidence/exposure caps (never as GO blockers); artifact checklist including `eligible_universe.txt`, `universe_summary.json`, `technical_indicators.json`, `15_predictions.json`, and the Core ETF Market Forecast Block status (present, or fields `UNAVAILABLE` with documented fetch attempts).

### `01_preflight.md`
Source Ledger before any agent uses facts downstream. Schema:

| artifact | field | ticker/entity | value | unit | observation_date | source | freshness_tag | claim_type | used_by |
|---|---|---|---|---|---|---|---|---|---|

Allowed `freshness_tag` / `claim_type` values: `rules.md § Source Ledger Contract` (single source). Derived rows cite formula + input rows; a critical field with no source is `UNAVAILABLE`, never estimated. Any score-attribution metric used in `Adj Score`, penalties, confidence, or sizing must have a ledger row; unavailable metrics must be recorded as `UNAVAILABLE` when material. Technical indicator rows must cite both the underlying price-history row and `technical_indicators.json` / `technical_indicators.py` formula lineage.

### `technical_indicators.json`
Support artifact generated by:

```bash
python3 investments/equity/daily_investment_system/technical_indicators.py ...
```

It must include all core ETFs and every eligible-universe ticker handed off by Data/Regime when fetched price history exists. The artifact carries `generated_at`, `benchmark`, formula definitions, per-ticker source metadata, daily indicators, weekly indicators, and monthly indicators. Downstream markdown tables never introduce a technical indicator value absent from this artifact and the Source Ledger.

### `eligible_universe.txt` / `universe_summary.json`

Support artifacts generated by:

```bash
python3 investments/equity/daily_investment_system/build_index_universe.py ...
```

`eligible_universe.txt` is the exact S&P 500 ∪ Nasdaq-100 ticker list used for equity candidate ranking. `universe_summary.json` records source cache paths, cache timestamps, S&P 500 count, Nasdaq-100 count, overlap count, and union count. `04_universe_summary.md` must report these counts and label ranks `INDEX_UNION_PCTL (n=XX)` when this path succeeds.

### `02_reflection.md`
Standalone MoM reflection, sections in order. Every price, return, regime, and thesis-validation claim cites `01` ledger rows or is `UNAVAILABLE` / explicitly `INFERRED`.

0. **Prediction Settlement** — settled table `Ticker | Vintage | Entry | Target Date | mu | Realized Return | SPY Return | Alpha | Direction | CI Result | z`; `MARKET_FORECAST` settlements (core ETFs) sit in the same table with `SPY Return` / `Alpha` = `N/A` and direction scored on raw return per `rules.md § Settlement Rules`; rolling calibration metrics (or `INSUFFICIENT_SETTLED_N`) with the market-forecast line reported separately; which prior `15_predictions.json` files were scanned.
1. **Prior Run Summary** — date, model, final status, regime, portfolio or basket, top-5 scores.
2. **MoM Price & Return Table** — `| Ticker | Prior Date | Prior Price | Current Date | Current Price | MoM Return | SPY Return | Alpha | Hit/Miss | Notes |`. Hit/Miss is alpha-based per `rules.md § Settlement Rules`; `Neutral` applies to position-P&L accounting only and is never a substitute for forecast scoring — a name ranked in a `REVIEW_ONLY` run is still a forecast. State `IN_CI`/`OUT_CI` when a CI was recorded. `APPROX - sourced` only with source + observation date; otherwise `UNAVAILABLE`.
3. **Theme-Level Performance** — validated / partial / failed per prior theme, with evidence.
4. **Regime Shift Assessment** — prior vs current regime and factor-weight implications.
5. **Carry-Forward Decisions** — `| Ticker/Theme | Prior Score | Prior Thesis | MoM Return | Decision | Rationale |`; decisions `CARRY` / `DOWNGRADE` / `DROP` / `PROMOTE`. Binding on factor scoring when ledger-backed; `DROP` names stay out of today's scored set absent new ledger evidence.
6. **Sign-Off** — freshness tag per price used, reflection confidence (HIGH/MEDIUM/LOW) with rationale, structural issues found.

### `03_regime_and_data.md`
Data-mode declaration, regime classification with cited evidence, event-concentration flags, universe handoff — and the **Core ETF Market Forecast Block** (`rules.md § Core ETF Market Forecast`), one row each for SPY, QQQ, SOXX:

| ETF | Entry Price | Price Date | Price Tag | Trend (20d/50d) | 30d RVol | Beta vs SPY | mu | sigma | Sigma Source | Target Price | Target Date | 70% CI Lo | 70% CI Hi | Confidence | Ledger Rows |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|

Plus relative-strength notes (`QQQ/SPY`, `SOXX/SPY` over 20d/60d) and a one-line regime-consistency check. ETF rows are a market-forecast sleeve — never candidates, never universe members.

### `04_universe_summary.md`
Universe construction, inclusion/exclusion log, index-union counts from `universe_summary.json`, sampled-universe disclosure only when the emergency fallback is used, and metric coverage summary. The coverage summary must state which `rules.md § Financial Metrics and Score Attribution` inputs are sourceable across the eligible universe, which are `UNAVAILABLE`, and which missing inputs affect data quality rather than GO eligibility. It must separately report daily/weekly/monthly technical indicator coverage for TD-9, RSI(14), MACD(12,26,9), MA alignment, momentum, volume ratio, and relative strength.

### `05_factor_scores.md`
Primary home for `Adj Score` explainability. Must include:

- Ranked candidate table using the schema in `agents.md § Factor Scoring Agent Prompt`, including `Sharpe`, `Sortino`, `IR`, `Kelly 0.25`, `VaR95`, `CVaR95`, `Max DD60`, `TD9 D/W/M`, `RSI14 D/W/M`, `MACD D/W/M`, `Score Trace`, and `Metric Ledger Rows`.
- Score attribution table: `Ticker | Fund_Z | Tech_Z | Sent_Z | Macro_Z | Composite_Z | DQ | Penalties | Adj Score | Top Positive Drivers | Top Negative Drivers | Metric Ledger Rows`.
- Metric availability table: `Metric Group | Sourceable Count | UNAVAILABLE Count | DQ / Confidence Effect | Notes`.
- Technical indicator summary table: `Ticker | TD9 D/W/M | RSI14 D/W/M | MACD State D/W/M | MACD Hist D/W/M | MA Alignment D/W/M | 20/60 Mom D/W/M | RS20/60 vs SPY D/W/M | Indicator Ledger Rows`.
- No score may cite a metric not present in `01_preflight.md`; no missing metric may be described as neutral or supportive.

### `06_top_candidates.md`
Top candidates and monitoring sleeve summary inherited from `05`, with no new facts. It must carry a compact score trace per name and enough key financial metrics and technical indicator states for a reader to understand why each candidate cleared or missed the investable threshold.

### `07_portfolio_proposal.md`
Portfolio construction output. Must inherit the per-position recommendation metrics, technical indicator states, and score traces from `05`; any recomputation requires a formula and Source Ledger row. Include portfolio-level Sharpe, Sortino, Information Ratio, tracking error, VaR95, CVaR95, 95th-pctl drawdown, Kelly cap-binding notes, correlation matrix, sector table, and excluded-name rationale.

### `08_risk_review.md`
Risk committee decision and checks. Must explicitly review price/target lineage, sigma lineage, score attribution, metric ledger coverage, Kelly threshold handling, technical indicator lineage and interpretation, Source Ledger completeness, GO-blocking discipline, and prediction-record completeness.

### `09_final_report.md`
Header banner:

```text
══════════════════════════════════════════════════════
QUANTITATIVE EQUITY SELECTION REPORT — [YYYY-MM-DD]
Run Status: [GO | NO_TRADE | REVIEW_ONLY | HALTED]
Classification: INTERNAL — INVESTMENT COMMITTEE USE
══════════════════════════════════════════════════════
```

Then: executive summary (≤ 5 sentences); MoM Reflection Summary (summarizes `02`, introduces no new facts); regime table (regime, data quality, key macro risk — with ledger rows); core ETF market forecast table (SPY / QQQ / SOXX, summarizing `03` — no new facts); ranked candidate table with compact score traces, key financial metrics, and compact technical indicator states; portfolio analytics or no-trade rationale; assumptions and limitations; next scheduled review. The final report summarizes score attribution from `05` and may not introduce new metrics or facts.

### `13_evolution_log.md`
Run context (date, status, regime, evaluation window, ledger status, baseline flag); what worked / what failed; primary diagnosis (one of: data quality, regime classification, factor calibration, portfolio construction, risk review, output clarity, source grounding); exactly one proposed change with **Track A/B classification** per `rules.md § Evolution Policy`; hypothesis; validation (Track A: holdout/IR/hit-rate/drawdown/turnover deltas; Track B: the three-condition standard); decision `ACCEPT` / `REJECT` / `DEFER` / `NO_CHANGE_ACCEPTED`; effective next step.

### `15_predictions.json`
Required whenever any name is ranked — investable or monitoring sleeve, **every** run status including `REVIEW_ONLY` and `ILLUSTRATIVE` — or whenever the Core ETF Market Forecast Block is produced. One record per ranked name per `rules.md § Prediction Ledger`, plus the three core ETF `MARKET_FORECAST` records (SPY, QQQ, SOXX); plus a `settlements` block with every prediction settled this run (or `"settlements": []` and a `NO_PREDICTION_LEDGER` note). New equity records include the backward-compatible `score_explainability` object with technical indicator fields when sourceable; market-forecast records may set it to `null`. Valid JSON, no markdown wrapper. A run that ranks names is not publishable without this file.
