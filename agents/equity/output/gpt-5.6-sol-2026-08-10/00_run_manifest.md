# 00 — Run Manifest

| Field | Value |
|---|---|
| Run date | `2026-08-10` (Monday) |
| Model | `gpt-5.6-sol` |
| Fire window | **POST-CLOSE** — started about 23:45 ET; completed after midnight |
| Price basis | **2026-08-10 completed regular-session close** |
| Run mode | Scheduled daily run |
| Data mode | `DELAYED` |
| Status target | `GO` |
| **Final status** | **`NO_TRADE`** |
| Reflection baseline | `agents/equity/output/gpt-5-2026-07-13` |
| Baseline flag | `CROSS_MODEL_BASELINE` — same GPT family, different exact model id |
| Universe | `INDEX_UNION_PCTL (n=511)` from a 515-name index union |

## Outcome

All five Required inputs are grounded, but the investable evidence gate is arithmetically
unsatisfiable: only Technical and Macro are available, Technical supplies 66.67% of live family
weight, and DQ is 0.80. The diagnostic top-20 also breaches the 8% drawdown cap (9.22%)
and the 30% sector cap (35%). The package therefore publishes 20
settleable monitoring forecasts and three core ETF forecasts, but no positions.

## Prediction settlement

The pre-run normalizer found 200 due keys across target dates August 7-10. All 200 were
grounded and published: 50 `ORDINARY`, 73 `WEEKEND_TARGET`, and 77
`TARGET_DATE_CLOSE`. The post-run canonical state is 951 settlements (819 equity, 132 market),
0 due, 0 conflicts, and 87 rejected historical candidates [L017-L018,L028].

| Type | raw n | 28d eff_n | Hit rate | CI coverage | Mean z | Track A eligible |
| --- | --- | --- | --- | --- | --- | --- |
| EQUITY_ALPHA | 819 | 2 | 39.19% | 71.06% | -0.5085 | No — INSUFFICIENT_EFFECTIVE_N |
| MARKET_FORECAST | 132 | 2 | 27.34% | 87.12% | -0.4707 | No — INSUFFICIENT_EFFECTIVE_N |

Weighted mean equity rank IC is **-0.0518**; confidence is capped and the
calibration change is deferred because `eff_n=2<3` [L028,L031].

## GO-Gate Table

| Input / threshold | Class | Evidence | Result |
| --- | --- | --- | --- |
| Grounded entry prices | Required | 23/23 across StockAnalysis and CNBC; max deviation 0.0000% [L016] | PASS |
| ~60 sessions history per name + SPY | Required | 511 scored names have >=372 bars; SPY 1255 [L001-L002] | PASS |
| Sigma fallback chain | Required | REALIZED_VOL_30D for all 23 forecasts [L201-L220,L601-L603] | PASS |
| Next earnings date | Required | 28/28 forward dates swept; 14/14 unconfirmed top names cadence-estimated [L012-L014,L033] | PASS |
| Index-union universe | Required | 515 names from helper; 511 scored [L008-L010] | PASS |
| Factor-family breadth | Evidence threshold | 2/4 available; maximum support is 2 [L022-L023] | FAIL |
| Maximum family share | Evidence threshold | Technical 0.30/0.45 live weight = 66.67% >50% | FAIL |
| Data completeness | Evidence threshold | DQ 0.80 <0.85 [L021] | FAIL |

### Enhancing inputs (caps only)

Options IV/skew, short-interest/borrow, analyst revisions, bid-ask tape, institutional-flow
data, `Fund_Z`, and `Sent_Z` are unavailable. They reduce confidence and DQ; none is misused as
a Required-input blocker [L021-L023].

## Source Ledger coverage and status eligibility

The ledger contains 136 rows: run/global rows, 100 per-name price/sigma/risk/earnings/score rows,
and three core-ETF blocks. Every downstream price, sigma, risk statistic, factor input,
technical state, earnings tag, target and confidence decision maps to those rows. Required-input
coverage permits `GO`; evidence thresholds and protected portfolio limits force `NO_TRADE`.

## Working-data checklist

| Working artifact | Result | Detail |
| --- | --- | --- |
| eligible_universe / summary | SUCCESS | 515 union; caches 2026-06-21; 511 scored |
| StockAnalysis raw + adjusted trees | SUCCESS | 519/519, zero failures; 3 basis-date raw/adjusted dividend differences handled |
| technical_indicators.json | SUCCESS | 518 requested; 517 OK; FDXF unavailable |
| earnings sweep + cadence | SUCCESS | 28/28 dates; 60 confirmed; 14/14 top-name estimates; 25 penalized |
| entry-price verification | SUCCESS | 23/23; max deviation 0.0000% |
| settlement verification | SUCCESS | 82 ticker/date comparisons for 41 symbols; max deviation 0.0000% |
| settlement ledger | SUCCESS | 951 canonical; due 0; conflicts 0; rejected 87 |
| VIX / Treasury | SUCCESS | VIX 15.46; 13-week bank discount 3.74% |

## Core ETF Market Forecast Block

| ETF | Forecast | mu | sigma | Confidence |
| --- | --- | --- | --- | --- |
| SPY | Yes | 2.00% | 3.75% | MEDIUM |
| QQQ | Yes | 3.42% | 7.23% | MEDIUM |
| SOXX | Yes | 6.95% | 17.78% | MEDIUM |

The default target is 2026-09-07 (`run_date+28d`), a market holiday. Forecasts retain that
date and will settle at the last close at or before it under `WEEKEND_TARGET` [L029].

## Artifacts

| Artifact | Status |
| --- | --- |
| 00_run_manifest.md | Published |
| 01_preflight.md | Published |
| 02_reflection.md | Published |
| 03_regime_and_data.md | Published |
| 04_universe_summary.md | Published |
| 05_factor_scores.md | Published |
| 06_top_candidates.md | Published |
| 07_portfolio_proposal.md | Published |
| 08_risk_review.md | Published |
| 09_final_report.md | Published |
| 12_close_log.md | Published |
| 13_evolution_log.md | Published |
| 15_predictions.json | Published |
| 10_midday_monitor.md | Omitted — no midday checkpoint |
| 11_preclose_check.md | Omitted — no pre-close checkpoint |
| 14_weekly_review.md | Omitted — Monday |
| 16_monthly_review.md | Omitted — not month-end |

## Agents and state transitions

`Orchestrator -> Reflection -> Data/Regime -> Technical -> Factor Scoring -> Portfolio ->
Risk Committee -> Evolution`.

`PRECHECK -> REFLECTION -> DATA_OK -> TECHNICALS_OK -> SCORED -> PORTFOLIO_DRAFT ->
RISK_REVIEW -> PUBLISHED`; final status **`NO_TRADE`**.

## Outstanding blockers

1. `Fund_Z` and `Sent_Z` have no production universe-scale fetch/scoring path.
2. Equity and market-forecast calibration each have only two independent 28-day windows.
3. The naive monitor sleeve exceeds protected drawdown and sector caps; it is diagnostic only.
