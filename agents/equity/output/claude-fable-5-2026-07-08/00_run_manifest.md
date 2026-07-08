# 00 Run Manifest

| Field | Value |
| --- | --- |
| Date | 2026-07-08 (Wednesday — live session) |
| Model | claude-fable-5 |
| Run mode | Scheduled-task run of `investments/equity/daily_investment_system/main.md`, executed ~13:40–14:15 ET (the 07:27 pre-open slot has no active scheduler job — runbook §Scheduler) |
| Data mode | **LIVE** (intraday prints, two-source verified + brokerage MCP corroboration — 07-02/07-06/07-07 precedent) |
| Status target | GO if live-data portfolio constraints pass; otherwise NO_TRADE |
| Final status | **NO_TRADE** |
| Retrieved at | 2026-07-08T17:46:59Z–17:48:35Z (universe bars, **521/521 OK — fifth consecutive zero-failure fetch**, 8-worker threaded); 2026-07-08T17:55:03Z–17:55:20Z Nasdaq cross-check (max divergence 0.28% (GOOGL), all < 1%, 35 symbols); 2026-07-08T17:54:28Z–17:54:43Z IBKR MCP live snapshots (SPY 744.54 / QQQ 708.71 / SOXX 560.30, `is_close: false`, max divergence 0.163%) |
| Agents executed | Orchestrator, Data/Regime, Factor Scoring, Portfolio Construction (pre-check only), Risk Committee (APPROVE), Evolution |
| Outstanding blockers | Fundamental + Sentiment families unwired → evidence threshold #2 unsatisfiable (**8th consecutive run**; Track B proposal pending HUMAN_REVIEW, 8th escalation — see 13) |
| Reflection baseline | `investments/equity/output/claude-fable-5-2026-06-10` |
| Baseline flag | SAME_MODEL_BASELINE (window 2026-05-24..2026-06-17, target 2026-06-10; baseline 0d from target; folder 28d old, >=21d invariant satisfied). Sub-21d folders used only as short-window cross-checks |
| Prediction settlement summary | **12 settled — first settlement pass in system history** (claude-fable-5 2026-06-10 vintage, target_date 2026-07-08): 6 HIT / 6 MISS on alpha; 7 IN_CI, 4 OUT_CI_LOW, 1 OUT_CI_HIGH. Rolling calibration (n=12): hit rate 50.0%, CI coverage 58.3%, mean z -0.265, rank IC **-0.51** (n<20 — no action threshold crossed). Scanned **34** ledgers, **653** OPEN records; next due **2026-07-09 (17 records)**, then 07-12 (20) |
| Source Ledger coverage | OBSERVED 44; DERIVED 130; INFERRED 23; ILLUSTRATIVE 0; UNAVAILABLE 0 (197 rows) |
| Status eligibility | All 5 Required inputs grounded → GO-eligible on data; **NO_TRADE on evidence thresholds** (0 investable < 5, stop criterion #1 — family-coverage gate) |
| Core ETF Market Forecast Block | PRESENT — SPY, QQQ, SOXX in 03 + three MARKET_FORECAST records (with `mu_derivation` blocks) in 15 |
| Universe | 515 union; **513 eligible** (SATS structural exclusion — 3rd stale session, delisting/halt suspected; FDXF 29 bars); INDEX_UNION_PCTL (n=513); sampled fallback NOT used |
| rf note | ^IRX fresh same-day print 3.725% (LIVE, L006); ratios use rf_1m 0.310% |

## State Transition Log

`PRECHECK -> REFLECTION (12 settled) -> DATA_OK -> TECHNICALS_OK -> SCORED -> PORTFOLIO_DRAFT (feasibility pre-check -> NO_TRADE, no weights drafted) -> RISK_REVIEW (APPROVE) -> PUBLISHED (NO_TRADE) -> EVOLUTION_REVIEW` (pre-close/close checkpoints pending at publication — run precedes the 16:00 ET close)

## GO-Gate Table (Required inputs only)

| Required Input | Status | Evidence | Blocks GO? |
| --- | --- | --- | --- |
| Grounded entry price | PASS | Live intraday prints: Yahoo chart fetch (2026-07-08T17:48:35Z) + Nasdaq last-sale cross-check (17:55:03Z–17:55:20Z) max divergence 0.28% (GOOGL) on all 35 checked symbols; IBKR MCP live corroboration on the ETFs (0.163%) | No |
| ~60 trading days history | PASS | 5y daily bars through the live 2026-07-08 session for 521/521 fetched symbols | No |
| Sigma via fallback chain | PASS | REALIZED_VOL_30D for every published name and ETF | No |
| Next earnings date | PASS | Cadence estimates ESTIMATED (±5d) for the 80-name shortlist; **34 names inside the <=19d buffered window penalized -0.10** (Q2 season opens tomorrow: DAL 07-09; banks 07-14..07-17) | No |
| Index-union universe | PASS | 503∪101−89 = 515; support artifacts published | No |

GO is unavailable on evidence threshold #2, not on Required inputs: with Fundamental and Sentiment UNAVAILABLE universe-wide, no name can show 3-of-4 non-negative families → investable set empty → **NO_TRADE** (stop criterion #1).

## Enhancing Inputs Missing (caps, never GO blockers)

Options IV/skew, short interest/borrow, bid-ask tape, analyst-revision tape, institutional-flow, fundamental feed → DQ 0.80, confidence LOW, family contributions 0.00 (UNAVAILABLE).

## Artifact Checklist

| Artifact | Status |
| --- | --- |
| 00–09 | PRESENT |
| 10_midday_monitor.md | PRESENT (run followed the 12:15 checkpoint; covers it retroactively at ~13:50 ET) |
| 11_preclose_check.md / 12_close_log.md | PENDING NOTES (no scheduler job; run published early afternoon) |
| 13_evolution_log.md | PRESENT |
| 14_weekly_review.md | N/A NOTE (Wednesday; next Friday 2026-07-10) |
| 15_predictions.json (23 EQUITY_ALPHA + 3 MARKET_FORECAST, **12 settlements**) | PRESENT — publishing gate satisfied |
| 16_monthly_review.md | N/A NOTE (month-end 2026-07-31) |
| eligible_universe.txt / universe_summary.json / technical_indicators.json (518 records, 2026-07-08T17:48:58Z) | PRESENT |
