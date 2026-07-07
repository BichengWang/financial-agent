# 00 Run Manifest

| Field | Value |
| --- | --- |
| Date | 2026-07-07 (Tuesday — live session) |
| Model | claude-fable-5 |
| Run mode | Scheduled-task run of `investments/equity/daily_investment_system/main.md`, executed midday ~11:53–12:30 ET (the 07:27 pre-open slot has no active scheduler job — runbook §Scheduler) |
| Data mode | **LIVE** (intraday prints, two-source verified + brokerage MCP corroboration — 07-02/07-06 precedent) |
| Status target | GO if live-data portfolio constraints pass; otherwise NO_TRADE |
| Final status | **NO_TRADE** |
| Retrieved at | 2026-07-07T15:52:47Z–16:02:07Z (universe bars, 521/521 OK — fourth consecutive zero-failure fetch); 2026-07-07T16:05:51Z–16:06:15Z Nasdaq cross-check (max divergence 0.772% (AXON), all < 1%); 2026-07-07T16:02:26Z IBKR MCP live snapshots (SPY 747.78 / QQQ 710.23 / SOXX 548.85, `is_close: false`, max divergence 0.168%) |
| Agents executed | Orchestrator, Data/Regime, Factor Scoring, Portfolio Construction (pre-check only), Risk Committee, Evolution |
| Outstanding blockers | Fundamental + Sentiment families unwired → evidence threshold #2 unsatisfiable (7th consecutive run; Track B proposal pending HUMAN_REVIEW, 7th escalation — see 13) |
| Reflection baseline | `investments/equity/output/claude-fable-5-2026-06-10` |
| Baseline flag | SAME_MODEL_BASELINE (window 2026-05-23..2026-06-16, target 2026-06-09; baseline 1d from target; folder 27d old, >=21d invariant satisfied). Sub-21d folders used only as short-window cross-checks |
| Prediction settlement summary | 0 settled — no OPEN prediction has target_date <= 2026-07-07; scanned **32** prior ledgers, **605** OPEN records; earliest due **2026-07-08** (this model's 2026-06-10 vintage, 12 records — settle on tomorrow's run) |
| Source Ledger coverage | OBSERVED 55; DERIVED 126; INFERRED 23; ILLUSTRATIVE 0; UNAVAILABLE 0 (204 rows) |
| Status eligibility | All 5 Required inputs grounded → GO-eligible on data; **NO_TRADE on evidence thresholds** (0 investable < 5, stop criterion #1 — family-coverage gate) |
| Core ETF Market Forecast Block | PRESENT — SPY, QQQ, SOXX in 03 + three MARKET_FORECAST records (with `mu_derivation` blocks) in 15 |
| Universe | 515 union; **513 eligible** (SATS stale last bar 2026-07-02, FDXF 28 bars); INDEX_UNION_PCTL (n=513); sampled fallback NOT used |
| rf note | ^IRX fresh same-day print 3.725% (LIVE, cited); ratios use rf_1m 0.310% |

## State Transition Log

`PRECHECK -> REFLECTION -> DATA_OK -> TECHNICALS_OK -> SCORED -> PORTFOLIO_DRAFT (feasibility pre-check -> NO_TRADE, no weights drafted) -> RISK_REVIEW (APPROVE) -> PUBLISHED (NO_TRADE) -> EVOLUTION_REVIEW` (pre-close/close checkpoints pending at publication — run precedes the 16:00 ET close)

## GO-Gate Table (Required inputs only)

| Required Input | Status | Evidence | Blocks GO? |
| --- | --- | --- | --- |
| Grounded entry price | PASS | Live intraday prints: Yahoo chart fetch (2026-07-07T16:02:07Z) + Nasdaq last-sale cross-check (2026-07-07T16:05:51Z–16:06:15Z) max divergence 0.772% (AXON) on all 34 checked symbols; IBKR MCP live corroboration on the ETFs (0.168%) | No |
| ~60 trading days history | PASS | 5y daily bars through the live 2026-07-07 session for 521/521 fetched symbols | No |
| Sigma via fallback chain | PASS | REALIZED_VOL_30D for every published name and ETF | No |
| Next earnings date | PASS | Cadence estimates ESTIMATED (±5d) for the 80-name shortlist; **35 names inside the <=19d buffered window penalized -0.10** (Q2 season opens: banks/airlines 07-09..07-17); DAL (~2d) nearest in sleeve | No |
| Index-union universe | PASS | 503∪101−89 = 515; support artifacts published | No |

GO is unavailable on evidence threshold #2, not on Required inputs: with Fundamental and Sentiment UNAVAILABLE universe-wide, no name can show 3-of-4 non-negative families → investable set empty → **NO_TRADE** (stop criterion #1).

## Enhancing Inputs Missing (caps, never GO blockers)

Options IV/skew, short interest/borrow, bid-ask tape, analyst-revision tape, institutional-flow, fundamental feed → DQ 0.80, confidence LOW, family contributions 0.00 (UNAVAILABLE).

## Artifact Checklist

| Artifact | Status |
| --- | --- |
| 00–09 | PRESENT |
| 10_midday_monitor.md | PRESENT (run overlapped the 12:15 checkpoint) |
| 11_preclose_check.md / 12_close_log.md | PENDING NOTES (no scheduler job; run published midday) |
| 13_evolution_log.md | PRESENT |
| 14_weekly_review.md | N/A NOTE (Tuesday; next Friday 2026-07-10) |
| 15_predictions.json (22 EQUITY_ALPHA + 3 MARKET_FORECAST, settlements []) | PRESENT — publishing gate satisfied |
| 16_monthly_review.md | N/A NOTE (month-end 2026-07-31) |
| eligible_universe.txt / universe_summary.json / technical_indicators.json (518 records, 2026-07-07T16:02:20Z) | PRESENT |
