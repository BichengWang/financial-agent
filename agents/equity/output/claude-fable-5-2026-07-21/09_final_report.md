```text
══════════════════════════════════════════════════════
QUANTITATIVE EQUITY SELECTION REPORT — 2026-07-21
Run Status: NO_TRADE
Classification: INTERNAL — INVESTMENT COMMITTEE USE
══════════════════════════════════════════════════════
```

## Executive Summary

All five Required-for-GO inputs are grounded (Yahoo v8 chart bulk fetch succeeded cleanly for the first time in six sessions, 521/521 symbols), and the leaderboard is clean and fully ledger-backed, but the run again publishes **NO_TRADE**: the structural Fund_Z/Sent_Z gate makes the ≥3-of-4-families evidence threshold mathematically unreachable (16th consecutive session), and independently, the top-20 candidate pool's own composition — mean beta −0.175 against the required 0.90-1.10 band, plus 5 of 20 names with earnings inside the buffered window — would make any portfolio infeasible even if the family gate were lifted. Regime remains **NEUTRAL with a HIGH_VOL watch** (VIX 18.65, SPY rangebound below its 20/50-day MAs), unchanged since 2026-07-17. Twenty fully-specified monitoring predictions plus the three core-ETF market forecasts are published in `15_predictions.json` for future settlement.

## MoM Reflection Summary

Baseline `claude-fable-5-2026-06-10` (`BASELINE_WINDOW_GAP`, 13d off target). Its top-5 basket went 2/5 on alpha over the 41-day window (MCK +2.89pp, UNH +1.16pp HIT; COST −7.13pp, WMT −9.25pp, CVX −2.34pp MISS); monitor-sleeve standout ABBV posted the single best alpha in the whole basket (+10.34pp) and is **PROMOTE**d. No predictions became newly due this run (`due_inventory = 0`); canonical settlement ledger unchanged at 175 EQUITY_ALPHA + 30 MARKET_FORECAST settlements. Rolling calibration: EQ hit rate 51.4%, CI coverage 77.1% (healthy band), mean z −0.236, rank IC −0.049 (triggers a MEDIUM confidence cap that is structurally moot — see `05`). Details: `02`.

## Market Regime Assessment

| Metric | Observation | Source | Implication |
|---|---|---|---|
| Regime | **NEUTRAL** with HIGH_VOL watch (unchanged 4th session) | SPY 742.09, below MA20 744.79 and MA50 744.55; VIX 18.65 < 20 trigger | Favor low-vol/defensive tilt; no regime-driven weight change |
| Breadth | 60.5% of eligible universe above own MA50 | `03` | Constructive, argues against BEAR |
| Vol trend | SPY 30d rvol 4.52% vs 2.68% prior window — rising | `03` | Watch-level, not yet HIGH_VOL |
| Data quality | DELAYED, 1 of 514 UNAVAILABLE (FDXF), DQ ×0.80 | `01` ledger | GO-eligible on data; NO_TRADE on evidence thresholds + portfolio feasibility |

## Core ETF Market Forecast

| ETF | Entry (07-20) | mu | sigma | Target (08-18) | 70% CI | Confidence |
|---|---|---|---|---|---|---|
| SPY | 742.09 | +0.50% | 4.52% | 745.80 | 710.90–780.71 | MEDIUM |
| QQQ | 696.06 | +0.37% | 8.87% | 698.61 | 634.38–762.83 | LOW |
| SOXX | 524.14 | +0.37% | 22.00% | 526.06 | 406.13–646.00 | LOW |

QQQ/SOXX mu shrunk from their beta-scaled raw values (−0.50pp, −1.50pp respectively) on persistent negative 20d relative strength vs SPY — a repeat of the 07-20 pattern, not a fresh deterioration. Full derivation: `03`.

## Ranked Candidates (compact)

Top 5 of the 20-name monitoring sleeve (full table: `05`/`06`):

| Rank | Ticker | Entry | Pctl | Adj Score | mu | Confidence | Key Risk |
|---|---|---|---|---|---|---|---|
| 1 | TRV | 368.50 | 100.0 | +0.3921 | +5.0% | LOW | RSI/TD-9 exhaustion flag |
| 2 | SCHW | 102.54 | 99.8 | +0.3697 | +6.0% | LOW | Fund/Sent gate only |
| 3 | MTB | 249.44 | 99.6 | +0.3534 | +6.0% | LOW | Fund/Sent gate only |
| 4 | PAYX | — | 99.4 | +0.3471 | +5.0% | LOW | Fund/Sent gate only |
| 5 | ADP | — | 99.2 | +0.3422 | +6.0% | LOW | Earnings 8 days out |

Investable subset: **empty** (evidence threshold #2 unsatisfiable — see `05`).

## Portfolio Analytics / No-Trade Rationale

No portfolio drafted. Task-0 feasibility pre-check (`07`) found the candidate pool's mean beta (−0.175) irreconcilable with the 0.90-1.10 band under any long-only, 5%-capped weighting, and 5 of 20 names carry earnings inside the buffered window (exceeds the 2-name concentration trigger). Risk Committee: **APPROVE** the NO_TRADE conclusion; 15-point integrity checklist clean (`08`).

## Assumptions and Limitations

- Fund_Z/Sent_Z are UNAVAILABLE for scoring (structural, universe-wide); SHADOW diagnostics exist and ran clean on today's top-20 shortlist but cover only 3.9% of the eligible universe, far under the 70% promotion bar.
- All prices are `DELAYED` (2026-07-20 close, fetched intraday on 07-21 with today's partial bar trimmed before use) — a single-source fetch (Yahoo v8) this session; no independent cross-check source was run.
- Sortino uses proper downside deviation (negative daily returns only, last 30d, scaled) per `rules.md`'s definition — corrected this run from a prior-session placeholder that reused total sigma; see `13`.
- Enhancing feeds (options IV, short interest, bid-ask, analyst-revision tape, institutional flow, GICS sector) remain unwired — confidence/exposure caps applied throughout, never a GO blocker by themselves.
- 14 of the top-60 earnings-shortlist names carry `ESTIMATED post-print cadence (±5d)` dates (+91 days from a confirmed mid-July print cluster) rather than vendor-confirmed dates.

## Next Scheduled Review

Per `runbook.md § Cadence`: next full pre-open run 07:27 ET next trading day (2026-07-22) — no scheduler currently active; this session ran as a manual/scheduled-task trigger. Daily evolution review folded into `13` below.
