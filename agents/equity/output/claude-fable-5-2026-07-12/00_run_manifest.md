# 00 Run Manifest

| Field | Value |
| --- | --- |
| Date | 2026-07-12 (**Sunday — U.S. markets closed**; last completed session Friday 2026-07-10; next session Monday 2026-07-13) |
| Model | claude-fable-5 |
| Run mode | Scheduled-task run of `investments/equity/daily_investment_system/main.md` (runbook holiday rule extended to the closed weekend: publish a full REVIEW_ONLY set, no skipped days — 07-04/07-05 precedent) |
| Data mode | **DELAYED** — official 2026-07-10 closes fetched this run at 2026-07-12T12:29:10Z–12:29:55Z (≤1-day lag vs the last completed session) |
| Status target | REVIEW_ONLY (weekend — no executable session) |
| Final status | **REVIEW_ONLY** |
| Retrieved at | 2026-07-12T12:29:10Z–12:29:55Z (**521/521 universe+ETF+macro bars, zero failures — the 07-11 Yahoo throttling did not recur**; 8-worker threaded); Nasdaq /quote chart cross-check 12:54–12:55Z (**0.0000% divergence on all 24 published names + SPY/QQQ/SOXX**); IBKR MCP closed-market snapshots 12:57Z returned the 2026-07-09 prior-session closes exactly (SPY 751.71 / QQQ 723.28 / SOXX 581.70, `is_close: true` — fourth consecutive reproduction); Nasdaq earnings-date endpoint 12:43Z (66 shortlist symbols, **confirmed dates**) |
| Agents executed | Orchestrator, Data/Regime, Factor Scoring, Portfolio Construction (pre-check only), Risk Committee (APPROVE), Evolution |
| Outstanding blockers | Fundamental + Sentiment families unwired → evidence threshold #2 unsatisfiable (**10th consecutive run**; standing Track B escalation continues — see 13) |
| Reflection baseline | `investments/equity/output/claude-fable-5-2026-06-10` |
| Baseline flag | SAME_MODEL_BASELINE (window 2026-05-28..2026-06-21, target 2026-06-14; baseline 4d from target; folder 32d old, ≥21d invariant satisfied). Sub-21d folders used only as short-window cross-checks |
| Prediction settlement summary | **20 settled — the decisive wave flagged by the last three evolution logs** (gpt-5 2026-06-14 vintage, target_date 2026-07-12, WEEKEND_TARGET treatment per 01/02): 17 EQUITY_ALPHA — 11 HIT / 6 MISS, 15 IN_CI / 2 OUT_CI_LOW (AMT, PLD), vintage rank IC **+0.554**, mean z -0.028; plus the **first 3 MARKET_FORECAST settlements** (SPY HIT, QQQ HIT, SOXX MISS — all IN_CI). Rolling cumulative (n=46): hit rate **56.5%**, CI coverage **78.3%**, mean z **-0.148**, weighted rank IC **+0.200** → the IC≤0 MEDIUM-freeze trigger **cleared on settled evidence**. Scanned **41** ledgers, **824** OPEN rows; next due 2026-08-04 (07-04 vintages) |
| Source Ledger coverage | OBSERVED 118; DERIVED 133; INFERRED 1; ILLUSTRATIVE 0; UNAVAILABLE 0 (252 rows) |
| Status eligibility | All 5 Required inputs grounded to the last completed session → data-eligible; REVIEW_ONLY by the weekend/holiday rule (family gate would independently force NO_TRADE on a trading day) |
| Core ETF Market Forecast Block | PRESENT — SPY, QQQ, SOXX in 03 + three MARKET_FORECAST records (with `mu_derivation`) in 15 |
| Universe | 515 union; **513 eligible** (SATS structural-stale, FDXF 31 bars; **BF-B re-admitted** — the 07-11 vendor gap did not recur); INDEX_UNION_PCTL (n=513); sampled fallback NOT used |
| rf note | ^IRX fresh 2026-07-10 print 3.695% (DELAYED, L006); ratios use rf_1m 0.308% |

## State Transition Log

`PRECHECK -> REFLECTION (20 settled) -> DATA_OK -> TECHNICALS_OK -> SCORED -> PORTFOLIO_DRAFT (feasibility pre-check -> REVIEW_ONLY/weekend) -> RISK_REVIEW (APPROVE) -> PUBLISHED (REVIEW_ONLY) -> EVOLUTION_REVIEW`

## GO-Gate Table (Required inputs only)

| Required Input | Status | Evidence | Blocks GO? |
| --- | --- | --- | --- |
| Grounded entry price | PASS | Official 07-10 closes: Yahoo threaded fetch (zero failures) + Nasdaq cross-check 0.0000% on all 27 checked symbols | No |
| ~60 trading days history | PASS | 5y daily bars through 2026-07-10 for 521/521 fetched symbols | No |
| Sigma via fallback chain | PASS | REALIZED_VOL_30D for every published name and ETF | No |
| Next earnings date | PASS | **Confirmed Nasdaq announcements for 66 shortlist symbols** (upgrade from cadence estimates); 28 names penalized inside the ≤14d window; DAL cadence-estimated (post-print 07-09) | No |
| Index-union universe | PASS | 503∪101−89 = 515; support artifacts published | No |

GO is unavailable on the weekend rule and evidence threshold #2 (2/4 families sourceable), not on Required inputs.

## Enhancing Inputs Missing (caps, never GO blockers)

Options IV/skew, short interest/borrow, bid-ask tape, analyst-revision tape, institutional-flow, fundamental feed → DQ 0.80, confidence LOW, family contributions 0.00 (UNAVAILABLE), gross cap 50% on any future GO day.

## Artifact Checklist

| Artifact | Status |
| --- | --- |
| 00–09 | PRESENT |
| 10_midday_monitor.md / 11_preclose_check.md / 12_close_log.md | N/A NOTES (markets closed — no checkpoints) |
| 13_evolution_log.md | PRESENT (one Track B change ACCEPTED: confirmed-earnings-date fetch adopted; HUMAN_REVIEW) |
| 14_weekly_review.md | N/A NOTE (Sunday; notes the missed Friday 07-10 review — truncated session; next due Friday 2026-07-17) |
| 15_predictions.json (24 EQUITY_ALPHA + 3 MARKET_FORECAST, **20 settlements**) | PRESENT — publishing gate satisfied |
| 16_monthly_review.md | N/A NOTE (month-end 2026-07-31) |
| eligible_universe.txt / universe_summary.json / technical_indicators.json (521 records, 519 OK, 2026-07-12T12:30:39Z) | PRESENT |

## Audit-Trail Note (repo state)

The claude-fable-5 **07-10 and 07-11 scheduled sessions truncated mid-run** and their partial dated folders were never committed (07-10: 01–04, 10, 11, 15, 16 + support; 07-11: 02, 03 + support). Both partial folders are committed alongside this package for audit-trail continuity per runbook §Output rule 3 (a halted run still publishes every completed artifact); their daily PRs were covered by codex-model runs (#21, #22).
