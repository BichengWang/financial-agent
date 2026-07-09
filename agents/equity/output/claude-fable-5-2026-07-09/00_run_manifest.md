# 00 Run Manifest

| Field | Value |
| --- | --- |
| Date | 2026-07-09 (Thursday — live session) |
| Model | claude-fable-5 |
| Run mode | Scheduled-task run of `investments/equity/daily_investment_system/main.md`, executed ~10:15–14:45 ET (the 07:27 pre-open slot has no active scheduler job — runbook §Scheduler) |
| Data mode | **LIVE** (intraday prints, two-source verified + IBKR brokerage MCP corroboration — 07-02..07-08 precedent) |
| Status target | GO if live-data portfolio constraints pass; otherwise NO_TRADE |
| Final status | **NO_TRADE** |
| Retrieved at | Universe bars fetched twice: 2026-07-09T14:30:05Z–14:47:49Z, then **refetched 2026-07-09T18:36:05Z–18:36:18Z** after intraday drift vs the cross-check source (up to 3.06% over ~4h) — downstream uses the refetch; both passes **521/521 OK (sixth and seventh consecutive zero-failure fetches)**, 8-worker threaded. Nasdaq cross-check 2026-07-09T18:36:22Z–18:36:23Z (max divergence 0.121% (TTWO), all <1%, 40 symbols). IBKR MCP live snapshots 2026-07-09T18:36:41Z (SPY 751.23 / QQQ 723.19 / SOXX 586.73, `is_close: false`, max divergence 0.008%) |
| Agents executed | Orchestrator, Data/Regime, Factor Scoring, Portfolio Construction (pre-check only), Risk Committee (APPROVE), Evolution |
| Outstanding blockers | Fundamental + Sentiment families unwired → evidence threshold #2 unsatisfiable (**9th consecutive run**; Track B proposal pending HUMAN_REVIEW, 9th escalation — see 13). New: weighted rank IC ≤ 0 trigger at n=29 → MEDIUM confidence freeze recorded (non-binding; see 02/13) |
| Reflection baseline | `investments/equity/output/claude-fable-5-2026-06-10` |
| Baseline flag | SAME_MODEL_BASELINE (window 2026-05-25..2026-06-18, target 2026-06-11; baseline 1d from target; folder 29d old, ≥21d invariant satisfied). Sub-21d folders used only as short-window cross-checks |
| Prediction settlement summary | **17 settled — second pass, first cross-model** (gpt-5 2026-06-11 vintage, target_date 2026-07-09): 9 HIT / 8 MISS on alpha; 14 IN_CI, 3 OUT_CI_LOW (CVX, AMT, ORCL); vintage rank IC **+0.348**, mean z -0.185. Rolling cumulative (n=29): hit rate 51.7%, CI coverage 72.4%, mean z -0.218, weighted rank IC **-0.007** (per-vintage -0.51 / +0.348 — §Priority Override honored in 13). Scanned **36** ledgers, **702** OPEN records; next due **2026-07-12 (20 records → n=49)** |
| Source Ledger coverage | OBSERVED 49; DERIVED 135; INFERRED 23; ILLUSTRATIVE 0; UNAVAILABLE 0 (207 rows) |
| Status eligibility | All 5 Required inputs grounded → GO-eligible on data; **NO_TRADE on evidence thresholds** (0 investable < 5, stop criterion #1 — family-coverage gate) |
| Core ETF Market Forecast Block | PRESENT — SPY, QQQ, SOXX in 03 + three MARKET_FORECAST records (with `mu_derivation`) in 15 |
| Universe | 515 union; **513 eligible** (SATS structural exclusion carried; FDXF 30 bars); INDEX_UNION_PCTL (n=513); sampled fallback NOT used |
| rf note | ^IRX fresh same-day print 3.688% (LIVE, L006); ratios use rf_1m 0.307% |

## State Transition Log

`PRECHECK -> REFLECTION (17 settled) -> DATA_OK (incl. mid-run refetch after drift check) -> TECHNICALS_OK -> SCORED -> PORTFOLIO_DRAFT (feasibility pre-check -> NO_TRADE, no weights drafted) -> RISK_REVIEW (APPROVE) -> PUBLISHED (NO_TRADE) -> EVOLUTION_REVIEW` (pre-close/close checkpoints pending at publication — run precedes the 16:00 ET close)

## GO-Gate Table (Required inputs only)

| Required Input | Status | Evidence | Blocks GO? |
| --- | --- | --- | --- |
| Grounded entry price | PASS | Live intraday prints: Yahoo refetch (18:36:18Z) + Nasdaq last-sale cross-check (18:36:22Z–18:36:23Z) max divergence 0.121% (TTWO) on all 40 checked symbols; IBKR MCP live corroboration on the ETFs (0.008%) | No |
| ~60 trading days history | PASS | 5y daily bars through the live 2026-07-09 session for 521/521 fetched symbols | No |
| Sigma via fallback chain | PASS | REALIZED_VOL_30D for every published name and ETF | No |
| Next earnings date | PASS | Cadence estimates ESTIMATED (±5d) for the ~76-name shortlist; **28 names inside the ≤19d buffered window penalized -0.10** (Q2 season opened today: DAL reported pre-market; banks 07-14..07-17) | No |
| Index-union universe | PASS | 503∪101−89 = 515; support artifacts published | No |

GO is unavailable on evidence threshold #2, not on Required inputs: with Fundamental and Sentiment UNAVAILABLE universe-wide, no name can show 3-of-4 non-negative families → investable set empty → **NO_TRADE** (stop criterion #1).

## Enhancing Inputs Missing (caps, never GO blockers)

Options IV/skew, short interest/borrow, bid-ask tape, analyst-revision tape, institutional-flow, fundamental feed → DQ 0.80, confidence LOW, family contributions 0.00 (UNAVAILABLE).

## Artifact Checklist

| Artifact | Status |
| --- | --- |
| 00–09 | PRESENT |
| 10_midday_monitor.md | PRESENT (run published ~14:45 ET; covers the 12:15 checkpoint retroactively) |
| 11_preclose_check.md / 12_close_log.md | PENDING NOTES (no scheduler job; run published mid-afternoon) |
| 13_evolution_log.md | PRESENT (Track A calibration proposal per §Priority Override — REJECT / NO_CHANGE_ACCEPTED) |
| 14_weekly_review.md | N/A NOTE (Thursday; next Friday 2026-07-10) |
| 15_predictions.json (23 EQUITY_ALPHA + 3 MARKET_FORECAST, **17 settlements**) | PRESENT — publishing gate satisfied |
| 16_monthly_review.md | N/A NOTE (month-end 2026-07-31) |
| eligible_universe.txt / universe_summary.json / technical_indicators.json (518 records, 2026-07-09T18:36:52Z) | PRESENT |
