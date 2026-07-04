# 00 Run Manifest

| Field | Value |
| --- | --- |
| Date | 2026-07-02 |
| Model | claude-sonnet-5 |
| Run mode | Manual automation run of `investments/equity/daily_investment_system/main.md` (first run for this model — no durable scheduler active, per `runbook.md § Scheduler`) |
| Data mode | `DELAYED` |
| Status target | `GO` if the sampled-universe evidence cleared all thresholds; downgraded per actual evidence |
| Final status | **`NO_TRADE`** |
| Retrieved at | 2026-07-02T12:03–12:17Z (IBKR MCP fetch window) |
| Market-session note | Thursday, U.S. cash market open at fetch time (live intraday quotes captured for SPY/QQQ/SOXX and 10 of 12 monitoring names). |
| Agents executed | Orchestrator (Reflection, universe build, technicals dispatch), Data/Regime, Factor Scoring, Portfolio Construction, Risk Committee, Evolution |
| Outstanding blockers | Fundamental and Sentiment/Positioning factor families UNAVAILABLE (no feed connected); earnings-calendar feed UNAVAILABLE; Yahoo Finance web fallback blocked by organizational egress policy; full 515-name index-union price-history fetch infeasible this session — Sampled Universe Protocol (n=30) used instead |
| Reflection baseline | `investments/equity/output/gpt-5-2026-06-07/` |
| Baseline flag | `CROSS_MODEL_BASELINE` |
| Prediction settlement summary | 0 settled; scanned 20 prior `15_predictions.json` ledgers (352 total OPEN records); earliest open `target_date` is 2026-07-08 |
| Source Ledger coverage | 146 rows total — OBSERVED 58, DERIVED 87, INFERRED 1, ILLUSTRATIVE 0, UNAVAILABLE 0 (material gaps declared at the family/field level, not as blank ledger rows) |
| Status eligibility | Required price/history/sigma inputs grounded for all 30 sampled names; index-union universe list materialized (515) but not price-fetched in full; earnings-date Required input UNAVAILABLE for all names; factor-family Evidence Threshold fails structurally (max 2 of 4 sourceable) — both are genuine Required-input/Evidence-Threshold blocks, not misapplied Enhancing-input caution |
| Core ETF Market Forecast Block | Present for SPY, QQQ, SOXX (`03_regime_and_data.md`), all IBKR-grounded LIVE entry prices |

## State Transition Log

| State | Result | Notes |
| --- | --- | --- |
| `PRECHECK` | Pass with caveats | IBKR MCP connected and functional; Yahoo Finance web fallback confirmed blocked (403, organizational egress policy) |
| `REFLECTION` | Complete | No same-model baseline exists; selected `gpt-5-2026-06-07` as `CROSS_MODEL_BASELINE`; 0 predictions settled (none due) |
| `DATA_OK` | Complete with disclosed gap | `build_index_universe.py` succeeded (515 names); full-universe price-history fetch infeasible — Sampled Universe Protocol invoked (30 names, all IBKR-grounded) |
| `TECHNICALS_OK` | Complete | `technical_indicators.py` run twice: 515-name attempt failed 515/515 on Yahoo block (documented, not published as final artifact); 33-name (30 sampled + 3 core ETF) run via IBKR-sourced CSV history-dir succeeded 33/33 |
| `SCORED` | Complete | 30 names scored on Technical + Macro families only (Fundamental/Sentiment UNAVAILABLE); 0 names clear the investable Evidence Threshold; 12 names (SAMPLED_PCTL ≥ 60) populate a LOW-confidence monitoring sleeve |
| `PORTFOLIO_DRAFT` | Not attempted — investable set empty | Per Portfolio Construction Agent's Task 0 pre-check, no weights are drafted when the investable set is empty; `07_portfolio_proposal.md` documents this explicitly |
| `RISK_REVIEW` | `APPROVE` | No revision requested; `NO_TRADE` affirmed as the correct conclusion, not a defect |
| `PUBLISHED` | Complete | Full `00`–`09`, `13`, `15` package published; `15_predictions.json` exists before publication per the publishing gate |
| `CLOSE_LOGGED` | N/A this run | `10`/`11`/`12` are scheduled-checkpoint artifacts, not part of the 07:27 pre-open publish; see Artifact Checklist |
| `EVOLUTION_REVIEW` | Complete | Track B proposal (Yahoo-block connectivity-probe procedure) logged as `DEFER`/`HUMAN_REVIEW` in `13_evolution_log.md`; no Track A change (0 settled predictions) |

## GO-Gate Table (Required Inputs Only)

| Required Input | Status | Evidence | Blocks GO? |
| --- | --- | --- | --- |
| Grounded entry price | PASS (for 30 sampled + 3 ETFs) | IBKR MCP `get_price_history`/`get_price_snapshot`, retrieved_at timestamps logged | No |
| ~60 trading days history | PASS | 1,253 daily bars (5y) for all 33 names | No |
| Sigma via fallback chain | PASS | `REALIZED_VOL_30D` computed from fetched 30d daily returns for all 12 monitoring names | No |
| Next earnings date | **FAIL** | No earnings-calendar feed connected; `UNAVAILABLE` for all 30 names, no cadence estimate possible | **Yes** |
| S&P 500 ∪ Nasdaq-100 index-union universe | Materialized but not price-fetched in full | `build_index_universe.py` succeeded (515 names); Sampled Universe Protocol (30 names) used for scoring per documented fetch-infeasibility trigger | **Yes** (structurally, via the resulting factor-family Evidence Threshold failure — see below) |

## Enhancing Inputs Missing (caps, never GO blockers by themselves)

Options IV/skew, short interest/borrow, bid-ask spread tape, analyst-revision tape, institutional ownership flow are all unavailable this session. These alone would only cap confidence and gross exposure, per `rules.md § Input Classification` — they are **not** cited as the reason for `NO_TRADE` here. The actual blockers are the two Required-input-level failures in the GO-Gate Table above, plus the independent factor-family Evidence Threshold (Fundamental and Sentiment families UNAVAILABLE, capping every name at 2 of 4 supportive families against the required 3-of-4 — see `05_factor_scores.md`/`08_risk_review.md`).

## Artifact Checklist

| Artifact | Status |
| --- | --- |
| 00_run_manifest.md | PRESENT |
| 01_preflight.md | PRESENT (146-row Source Ledger) |
| 02_reflection.md | PRESENT |
| 03_regime_and_data.md | PRESENT |
| 04_universe_summary.md | PRESENT |
| 05_factor_scores.md | PRESENT |
| 06_top_candidates.md | PRESENT |
| 07_portfolio_proposal.md | PRESENT (no positions — investable set empty) |
| 08_risk_review.md | PRESENT (`APPROVE`) |
| 09_final_report.md | PRESENT |
| 10_midday_monitor.md | NOT APPLICABLE — pre-open publish only; no scheduled midday checkpoint run this session |
| 11_preclose_check.md | NOT APPLICABLE — same reason |
| 12_close_log.md | NOT APPLICABLE — same reason |
| 13_evolution_log.md | PRESENT (`DEFER`, `HUMAN_REVIEW` flag) |
| 15_predictions.json | PRESENT (12 `EQUITY_ALPHA` + 3 `MARKET_FORECAST` = 15 records; valid JSON) |
| eligible_universe.txt | PRESENT (515 tickers) |
| universe_summary.json | PRESENT |
| sampled_universe.txt | PRESENT (30 tickers — supplementary, documents the Sampled Universe Protocol fallback set) |
| technical_indicators.json | PRESENT (33/33 OK — 30 sampled names + SPY/QQQ/SOXX, IBKR-sourced) |
