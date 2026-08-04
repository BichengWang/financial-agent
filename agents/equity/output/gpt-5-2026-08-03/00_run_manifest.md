# 00 — Run Manifest — 2026-08-03

| Field | Value |
| --- | --- |
| Run date | 2026-08-03 (Monday) |
| Fired/completed at | 2026-08-03T20:43:31-04:00 |
| Model | `gpt-5` |
| Run mode | Post-close full pipeline; completed 2026-08-03 close |
| Data mode | `DELAYED` |
| Status target | `GO` |
| Final status | **`NO_TRADE`** |
| Regime | `BULL` |
| Universe | S&P 500 ∪ Nasdaq-100 = 515; 511 scored, 4 rejected |
| Percentile label | INDEX_UNION_PCTL (n=511) |
| Forecast target date | 2026-08-31 |
| Data-quality multiplier | 0.80 |

## Why `NO_TRADE`

The full-universe run is grounded and auditable, but no name can clear all five evidence
thresholds while `Fund_Z` and `Sent_Z` remain unpromoted and `UNAVAILABLE`. The accepted
2026-08-01 Track B correction is active today: `Tech_Z` uses six distinct signals and keeps
RS20/RS60 as diagnostics instead of double-counting momentum.

| # | Threshold | Result |
| --- | --- | --- |
| 1 | Adjusted-score percentile ≥80 | PASS — 102/511 names |
| 2 | ≥3 of 4 families non-negative | FAIL — only Technical and Macro are available |
| 3 | No family >50% of conviction | FAIL — Technical is 66.7% of available family weight |
| 4 | Data completeness ≥85% | FAIL — DQ multiplier is 0.80 |
| 5 | No hard stop | PASS — no integrity halt |

## GO-Gate Table — Required inputs

| # | Required input | State | Evidence |
| --- | --- | --- | --- |
| 1 | Grounded entry price | GROUNDED | 23/23 published equity/ETF closes passed two-source <1% checks; max divergence 0.078750% |
| 2 | ~60d price history + SPY | GROUNDED | 519/519 fetched; 518/519 end 2026-08-03; FDXF is the disclosed stale/short-history exclusion |
| 3 | sigma fallback chain | GROUNDED | REALIZED_VOL_30D for all 20 monitoring names and SPY/QQQ/SOXX |
| 4 | next earnings date | GROUNDED | Complete Nasdaq forward sweep: 31 business days; every universe name classified as event or no-print-in-window |
| 5 | index-union universe | GROUNDED | build_index_universe.py → 515 names (503 S&P; 101 Nasdaq-100; 89 overlap) |

Missing options IV/skew, short-interest/borrow, bid-ask tape, analyst revisions, ownership
flow, and promoted full-universe Fundamental/Sentiment data are **Enhancing** gaps. They cap
confidence/exposure; they are not misclassified as Required-input blockers.

## Reflection baseline

| Field | Value |
| --- | --- |
| Baseline path | `agents/equity/output/gpt-5-2026-07-06` |
| Baseline flag | `SAME_MODEL_BASELINE` |
| Target/window | target 2026-07-06; window 2026-06-19…2026-07-13 |
| Tie disclosure | Exact-date tie with `claude-fable-5-2026-07-06`; same-model criterion selects gpt-5; both books are reported in 02 |

## Prediction settlement summary

| Field | Value |
| --- | --- |
| Settled this run | 88 (76 EQUITY_ALPHA; 12 MARKET_FORECAST) |
| Timing cohorts | 49 WEEKEND_TARGET rows at 2026-07-31 close; 39 TARGET_DATE_CLOSE rows at completed 2026-08-03 close |
| Canonical state | 515 equity + 90 market; due=0; conflicts=0 |

| Record type | raw n | 28d eff_n | Hit rate | CI coverage | Mean z | Track A gate |
| --- | --- | --- | --- | --- | --- | --- |
| EQUITY_ALPHA | 515 | 1 | 39.81% | 69.90% | -0.5191 | INSUFFICIENT_EFFECTIVE_N |
| MARKET_FORECAST | 90 | 1 | 22.09% | 81.11% | -0.6253 | INSUFFICIENT_EFFECTIVE_N |

## Source Ledger coverage

| claim_type | Rows |
| --- | --- |
| OBSERVED | 134 |
| DERIVED | 71 |
| INFERRED | 0 |
| ILLUSTRATIVE | 0 |
| UNAVAILABLE | 2 |

## Execution and artifacts

State machine: `PRECHECK → REFLECTION → DATA_OK → TECHNICALS_OK → SCORED →
PORTFOLIO_DRAFT → RISK_REVIEW → NO_TRADE → EVOLUTION_REVIEW`. Agents executed:
Orchestrator, Reflection, Data/Regime, deterministic technical compute, Factor Scoring,
Portfolio Construction feasibility pre-check, Risk Committee, Evolution. Revision passes: 0.

Durable package: `00, 01, 02, 03, 04, 05, 06, 07, 08, 09, 13, 15`. Checkpoints `10`–`12` did not run and are
omitted; `14` is Friday-only and `16` month-end-only. Working histories, manifests, universe
files, and full technical packs remain under gitignored `.work/`.

## Outstanding blockers

1. `Fund_Z` and `Sent_Z` remain unavailable at the required ≥70% universe coverage.
2. Weighted rank IC remains -0.0879; confidence is capped at `MEDIUM`.
3. Both record types remain at `eff_n=1`; Track A changes are ineligible.
