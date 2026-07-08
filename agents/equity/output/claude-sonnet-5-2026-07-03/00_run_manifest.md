# 00 Run Manifest

| Field | Value |
| --- | --- |
| Date | 2026-07-03 (Friday) |
| Model | claude-sonnet-5 |
| Run mode | Manual automation run of `investments/equity/daily_investment_system/main.md` |
| Data mode | DELAYED_PARTIAL |
| Status target | GO if delayed-data portfolio constraints pass; otherwise NO_TRADE |
| Final status | **NO_TRADE** |
| Retrieved at | 2026-07-03T12:19:00Z (price snapshots); 2026-07-03T12:17:24Z (technical indicator compute) |
| Market-session note | Friday run. IBKR `get_price_snapshot` "last" prints (is_close=true) used as entry prices, dated 2026-07-03. 5-year daily history via IBKR `get_price_history` through 2026-07-02 close used for technical indicators and risk metrics. |
| Agents executed | Orchestrator, Data/Regime, Factor Scoring, Portfolio Construction, Risk Committee, Evolution |
| Outstanding blockers | (1) No cross-sectional fundamental or sentiment/positioning feed is wired this session — Fund_Z and Sent_Z are UNAVAILABLE for the full sampled universe, so no name can clear the "≥3 of 4 factor families non-negative" evidence threshold. (2) Yahoo Finance (the `technical_indicators.py` built-in fetch) is blocked by this session's egress policy (proxy returned 403 on `query2.finance.yahoo.com`); IBKR was used as the sole grounded price source instead. (3) A per-name fetch budget constraint meant the full 515-name index-union universe could not be individually price-history-fetched via IBKR within this session; a documented 30-name Sampled Universe Protocol fallback was used for technicals/scoring (§ below), while `eligible_universe.txt` itself (515 names, no network needed) materialized successfully. (4) Next-earnings dates were sourced via WebSearch only for the top-12 ranked names (scope-limited); the remaining 18 sampled names carry `next_earnings_date = UNAVAILABLE`. |
| Reflection baseline | `investments/equity/output/gpt-5-2026-06-07` |
| Baseline flag | CROSS_MODEL_BASELINE (no prior `claude-sonnet-5` folder exists at any age; closest same-window folder is a different model) |
| Prediction settlement summary | 0 settled (earliest open `target_date` across all scanned ledgers is 2026-07-08); scanned 22 prior `15_predictions.json` files (395 prediction records) |
| Source Ledger coverage | OBSERVED 69; DERIVED 93; INFERRED 2; ILLUSTRATIVE 0; UNAVAILABLE 18 (rows 1–164, see `01_preflight.md`) |
| Status eligibility | Required inputs #1 (entry price), #2 (history), #3 (sigma), #5 (index-union universe) grounded; Required input #4 (earnings date) grounded for 12/30 sampled names only, UNAVAILABLE for the rest — one Required input partially missing → `DELAYED_PARTIAL`. Even where all Required inputs are grounded, the run cannot reach `GO` because Fund_Z/Sent_Z are UNAVAILABLE universe-wide, which caps every name below the 3-of-4-family evidence threshold. |
| Core ETF Market Forecast Block | Present for SPY, QQQ, SOXX (see `03_regime_and_data.md`) |

## State Transition Log

`PRECHECK -> REFLECTION -> DATA_OK -> TECHNICALS_OK -> SCORED -> PORTFOLIO_DRAFT -> RISK_REVIEW -> PUBLISHED -> CLOSE_LOGGED -> EVOLUTION_REVIEW`

| State | Result | Notes |
| --- | --- | --- |
| `PRECHECK` | Pass with caveats | IBKR MCP tools (`get_price_history`, `get_price_snapshot`, `search_contracts`) connected and grounded; Yahoo Finance blocked by egress policy (documented). |
| `REFLECTION` | Complete | Settlement: 0 due. MoM baseline: `gpt-5-2026-06-07` (CROSS_MODEL_BASELINE), 6 of 10 prior watchlist names re-priced this run (`01` ledger rows), 4 UNAVAILABLE (not in this run's fetch scope). |
| `DATA_OK` | Complete with documented fallback | `build_index_universe.py` succeeded (515 tickers, no network required). Price-history fetch used the Sampled Universe Protocol (30 names: 14 direct carry-forward names + 16 largest-liquid GICS-sector names) because Yahoo is blocked and per-name IBKR fetch for 515 names is infeasible in-session. |
| `TECHNICALS_OK` | Complete | `technical_indicators.py --history-dir` run against IBKR-sourced CSVs for SPY/QQQ/SOXX + 30 sampled names; 33/33 `status: OK`. |
| `SCORED` | Complete | Tech_Z and Macro_Z computed cross-sectionally (n=30); Fund_Z and Sent_Z UNAVAILABLE. 12 names clear the ≥60th-percentile ranking floor; 0 clear the "≥3 of 4 families non-negative" investable gate. |
| `PORTFOLIO_DRAFT` | Not attempted | Zero investable names supplied by Factor Scoring; Portfolio Construction's feasibility pre-check short-circuits to `NO_TRADE` per `agents.md § Portfolio Construction Agent Prompt` Task 0. |
| `RISK_REVIEW` | Complete | Risk Committee reviewed the monitoring sleeve and the NO_TRADE rationale; `APPROVE`d publication as `NO_TRADE`. |
| `PUBLISHED` | Complete | Full 00–09, 13, 14 (Friday), 15 package created. |
| `CLOSE_LOGGED` | Placeholder | 10/11/12 are scheduled intraday checkpoints; this is a single off-schedule manual run. |
| `EVOLUTION_REVIEW` | Complete | One Track B proposal logged in `13_evolution_log.md`; weekly review in `14_weekly_review.md`. |

## GO-Gate Table

| Required Input | Status | Evidence | Blocks GO? |
| --- | --- | --- | --- |
| Grounded entry price | PASS | All 30 sampled names + SPY/QQQ/SOXX priced via IBKR `get_price_snapshot` this run (rows L020+, see `01`). | No |
| ~60 trading days history | PASS | 1,254 daily bars (5y) per name via IBKR `get_price_history`, saved to `price_history_csv/`. | No |
| Sigma via fallback chain | PASS | `REALIZED_VOL_30D` computed from IBKR daily closes for all 30 sampled names + 3 ETFs. | No |
| Next earnings date | PARTIAL FAIL | Sourced (WebSearch, cross-checked) for the top-12 ranked names only; UNAVAILABLE for the other 18 sampled names — documented fetch-scope limitation, not a failed attempt. | Yes — forces `DELAYED_PARTIAL` / caps status below `GO` |
| S&P 500 ∪ Nasdaq-100 index-union universe | PASS (with documented technicals fallback) | `build_index_universe.py` wrote 515 tickers to `eligible_universe.txt` (no network needed). Price-history/technical-indicator computation used the 30-name Sampled Universe Protocol instead of the full 515, because Yahoo Finance is blocked and per-name IBKR fetch at 515-name scale is infeasible this session. Labeled `SAMPLED_PCTL (n=30)` throughout per `rules.md § Sampled Universe Protocol`. | Caps final status; documented in `00/01/03/04/08/13` |

## Enhancing Inputs Missing

Options IV/skew, short interest/borrow, bid-ask spread tape, analyst-revision tape, institutional ownership flow, and a full cross-sectional fundamental feed are unavailable this session (no such MCP tool or grounded source wired). These are Enhancing, not GO blockers by themselves — but because they leave `Fund_Z` and `Sent_Z` completely UNAVAILABLE (not just degraded), **no name can satisfy the "≥3 of 4 factor families non-negative" evidence threshold** (`rules.md § Evidence Thresholds` item 2), independent of the earnings-date and sampled-universe gaps above. This is the primary driver of today's `NO_TRADE`.

## Artifact Checklist

| Artifact | Status |
| --- | --- |
| 00_run_manifest.md | PRESENT |
| 01_preflight.md | PRESENT |
| 02_reflection.md | PRESENT |
| 03_regime_and_data.md | PRESENT |
| 04_universe_summary.md | PRESENT |
| 05_factor_scores.md | PRESENT |
| 06_top_candidates.md | PRESENT |
| 07_portfolio_proposal.md | PRESENT |
| 08_risk_review.md | PRESENT |
| 09_final_report.md | PRESENT |
| 10_midday_monitor.md | PLACEHOLDER (off-schedule single run) |
| 11_preclose_check.md | PLACEHOLDER (off-schedule single run) |
| 12_close_log.md | PLACEHOLDER (off-schedule single run) |
| 13_evolution_log.md | PRESENT |
| 14_weekly_review.md | PRESENT (today is Friday) |
| 15_predictions.json | PRESENT |
| 16_monthly_review.md | PLACEHOLDER (not last trading day of month) |
| eligible_universe.txt | PRESENT (515 tickers) |
| universe_summary.json | PRESENT |
| sampled_universe.txt | PRESENT (30-name Sampled Universe Protocol list) |
| technical_indicators.json | PRESENT (33 records: SPY, QQQ, SOXX + 30 sampled names) |
| price_history_csv/ | PRESENT (33 CSVs, IBKR-sourced 5y daily bars) |
