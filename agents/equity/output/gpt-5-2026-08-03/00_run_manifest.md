# 00 — Run Manifest — 2026-08-03

| Field | Value |
| --- | --- |
| Run date | 2026-08-03 (Monday) |
| Fired/completed at | 2026-08-03T20:43:31-04:00 |
| Model | `gpt-5` |
| Run mode | Post-close full pipeline; completed 2026-08-03 close |
| Data mode | `DELAYED_PARTIAL` |
| Status target | `GO` |
| Final status | **`HALTED`** |
| Regime | `BULL` |
| Universe | S&P 500 ∪ Nasdaq-100 = 515; 511 technically scoreable, 4 rejected; valid equity ranking halted |
| Percentile label | INDEX_UNION_PCTL (n=511) |
| Forecast target date | 2026-08-31 |
| Data-quality multiplier | 0.80 |

## Why `HALTED`

The completed-price and history analysis is grounded, but 15 of 20 provisional equity names
have neither a confirmed next earnings date nor a permitted cadence estimate. This is 75% of
the provisional selection and triggers Hard Halt criterion #3 (>20% unresolved critical
inputs). The equity score, percentile, target, and portfolio tables are retained only as
pre-halt diagnostics; they are not valid rankings, predictions, or trade instructions.

| # | Threshold | Result |
| --- | --- | --- |
| 1 | Adjusted-score percentile ≥80 | PASS — 102/511 names |
| 2 | ≥3 of 4 families non-negative | FAIL — only Technical and Macro are available |
| 3 | No family >50% of conviction | FAIL — Technical is 66.7% of available family weight |
| 4 | Data completeness ≥85% | FAIL — DQ multiplier is 0.80 |
| 5 | No hard stop | FAIL — Hard Halt #3; 15/20 provisional names (75%) have unresolved Required earnings dates |

## GO-Gate Table — Required inputs

| # | Required input | State | Evidence |
| --- | --- | --- | --- |
| 1 | Grounded entry price | GROUNDED | 23/23 provisional equity/ETF inputs passed two-source <1% checks; max divergence 0.078750% |
| 2 | ~60d price history + SPY | GROUNDED | 519/519 fetched; 518/519 end 2026-08-03; FDXF is the disclosed stale/short-history exclusion |
| 3 | sigma fallback chain | GROUNDED | REALIZED_VOL_30D for all 20 monitoring names and SPY/QQQ/SOXX |
| 4 | next earnings date | **UNAVAILABLE FOR 15/20 PROVISIONAL NAMES** | 5 confirmed, 0 cadence-estimated, 15 unresolved after a complete 31-business-day Nasdaq sweep |
| 5 | index-union universe | GROUNDED | build_index_universe.py → 515 names (503 S&P; 101 Nasdaq-100; 89 overlap) |

Missing options IV/skew, short-interest/borrow, bid-ask tape, analyst revisions, ownership flow, and promoted full-universe Fundamental/Sentiment data are **Enhancing** gaps. The missing earnings dates are a separate Required-input failure.

## Reflection baseline

| Field | Value |
| --- | --- |
| Baseline path | `agents/equity/output/gpt-5-2026-07-06` |
| Baseline flag | none — valid same-model baseline; no exception flag applies |
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
| OBSERVED | 119 |
| DERIVED | 182 |
| INFERRED | 0 |
| ILLUSTRATIVE | 0 |
| UNAVAILABLE | 17 |

## Execution and artifacts

State machine: `PRECHECK → REFLECTION → DATA_PARTIAL → HALTED`. Agents executed:
Orchestrator, Reflection, Data/Regime, deterministic technical compute, Factor Scoring,
Portfolio Construction feasibility pre-check, Risk Committee, Evolution. Revision passes: 0.

Durable package: `00, 01, 02, 03, 04, 05, 06, 07, 08, 09, 13, 15`. Checkpoints `10`–`12` did not run and are
omitted; `14` is Friday-only and `16` month-end-only. Working histories, manifests, universe
files, and full technical packs remain under gitignored `.work/`.

## Outstanding blockers

1. Fifteen of 20 provisional equity names lack a confirmed or cadence-estimated earnings date.
2. `Fund_Z` and `Sent_Z` remain unavailable at required universe coverage.
3. Weighted rank IC is -0.0879 and both record types remain at `eff_n=1`.
4. A future run must populate cadence estimates, reapply earnings penalties, and rescore before publishing equity predictions.