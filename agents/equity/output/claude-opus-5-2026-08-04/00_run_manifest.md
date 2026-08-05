# 00 — Run Manifest — 2026-08-04

| Field | Value |
|---|---|
| Run date | 2026-08-04 (Tuesday) |
| Fire window | **INTRADAY** — 2026-08-04T12:05:00-04:00 (CNBC `curmktstatus` = `REG_MKT`) |
| Price / indicator basis | **2026-08-03 completed close** (last completed session) |
| Model | `claude-opus-5` |
| Run mode | Full pipeline (stages 0–6) + midday checkpoint |
| Data mode | **`DELAYED`** — all five Required inputs grounded |
| Status target | `GO` |
| **Final status** | **`NO_TRADE`** |
| Regime | `BULL` |
| Scored universe | 512 of 515 (`INDEX_UNION_PCTL (n=512)`) |
| Published prediction records | 24 `EQUITY_ALPHA` + 3 `MARKET_FORECAST` |
| Reflection baseline | `agents/equity/output/claude-fable-5-2026-07-07` |
| Baseline flag | **`CROSS_MODEL_BASELINE`** (2-way tie at delta 0d, resolved by `agents.md` rule 8) |
| Settlements this run | **48** (42 `EQUITY_ALPHA`, 6 `MARKET_FORECAST`) |
| Due inventory / conflicts after settlement | 0 / 0 |

## Basis note — shared with the prior package

This run fires intraday, so the newest completed close is 2026-08-03 — **the same basis
`claude-opus-5-2026-08-03` used**. The cross-sectional ranking therefore carries no new price
information versus that package. What this run does add is a full settlement layer (48 keys
matured today), a fresh MoM baseline, and the same-basis reproduction test that the
2026-08-03 Track B requires. This is stated plainly rather than presented as a new market read.

## GO-Gate Table — Required inputs (only these may block `GO`)

| # | Required input (`rules.md § Input Classification`) | State | Evidence |
|---|---|---|---|
| 1 | Grounded entry price (Price Sourcing Standard) | **PASS** | 28/28 symbols, 3 independent sources, max deviation 0.0000% |
| 2 | ~60 trading days of price history per name + SPY | **PASS** | 519/519 symbols fetched; modal 1255 daily bars |
| 3 | `sigma` via the Sigma Fallback Chain | **PASS** | `REALIZED_VOL_30D` for all 512 scored names (chain step 2) |
| 4 | Next earnings date | **PASS** | complete forward sweep, 28/28 business days, 0 transport failures |
| 5 | S&P 500 ∪ Nasdaq-100 index union | **PASS** | `build_index_universe.py` → 515 tickers |

**All five Required inputs are grounded.** `NO_TRADE` is therefore driven by the Evidence
Thresholds in `rules.md`, not by a data failure.

## Enhancing inputs missing (caps only — never `GO` blockers)

| Enhancing input | State | Effect |
|---|---|---|
| Options IV / skew | `UNAVAILABLE` | sigma chain falls to step 2 (`REALIZED_VOL_30D`) |
| Short interest / borrow | `UNAVAILABLE` | `Sent_Z` unavailable → DQ 0.80 |
| Analyst revision tape | `UNAVAILABLE` | `Sent_Z` unavailable → DQ 0.80 |
| Bid-ask spread tape | `UNAVAILABLE` | liquidity screen falls back to dollar volume |
| Institutional ownership flow | `UNAVAILABLE` | no effect on ranking |
| Fundamental XBRL at universe scale | `UNAVAILABLE` | `Fund_Z` unavailable → DQ 0.80 |

## Prediction settlement summary

| Record type | Settled this run | Direction hits | IN_CI | Mean z |
|---|---|---|---|---|
| `EQUITY_ALPHA` | 42 | 14/42 = 33.33% | 23/42 | -0.7494 |
| `MARKET_FORECAST` | 6 | 2/6 = 33.33% | 6/6 | -0.1574 |

All 48 keys settle under **`TARGET_EQ_RUN_DATE`**: every due `target_date` equals the run
date and this run executes before that session's close, so `rules.md § Settlement Rules` requires the
latest completed close (2026-08-03). No intraday print was used.

## Canonical rolling calibration (from `settlement_ledger.py`)

| Record type | Raw n | 28-day `eff_n` | Hit rate | CI coverage | Mean z | Track A gate |
|---|---|---|---|---|---|---|
| `EQUITY_ALPHA` | 515 | 1 | 39.81% | 69.90% | -0.5191 | `INSUFFICIENT_EFFECTIVE_N` |
| `MARKET_FORECAST` | 90 | 1 | 22.09% | 81.11% | -0.6253 | `INSUFFICIENT_EFFECTIVE_N` |

Weighted-mean rank IC **-0.0879** over 515 settled `EQUITY_ALPHA` records
(20 of 32 vintages non-positive) →
`agents.md § Calibration Feedback Binding` **caps every confidence label at `MEDIUM`**.

`eff_n` remains **1** for both record types. The 2026-07-28 projection that `EQUITY_ALPHA` `eff_n`
increments on **2026-08-05**
(43 pending) is **not yet falsified** —
today is 2026-08-04, one day before that date.

## Source Ledger coverage

| Coverage class | Count | Status eligibility |
|---|---|---|
| Grounded entry prices (published set + core ETFs) | 28 | `GO`-eligible |
| Scored names with complete technical pack | 512 | `GO`-eligible |
| Scored names with grounded earnings distance | 512 | `GO`-eligible |
| Names with `Fund_Z` sourceable | 0 | blocks thresholds 2/3/4 |
| Names with `Sent_Z` sourceable | 0 | blocks thresholds 2/3/4 |

## Durable artifact checklist

| Artifact | State |
|---|---|
| `00_run_manifest.md` | Published |
| `01_preflight.md` | Published |
| `02_reflection.md` | Published |
| `03_regime_and_data.md` | Published |
| `04_universe_summary.md` | Published |
| `05_factor_scores.md` | Published |
| `06_top_candidates.md` | Published |
| `07_portfolio_proposal.md` | Published |
| `08_risk_review.md` | Published |
| `09_final_report.md` | Published |
| `10_midday_monitor.md` | Published — intraday fire, checkpoint ran |
| `11_preclose_check.md` | Omitted — stage did not run (`runbook.md` rule 4) |
| `12_close_log.md` | Omitted — stage did not run (`runbook.md` rule 4) |
| `13_evolution_log.md` | Published |
| `15_predictions.json` | Published — 24 `EQUITY_ALPHA` + 3 `MARKET_FORECAST` + 48 settlements |
| `14_weekly_review.md` | Not owed — Friday artifact |
| `16_monthly_review.md` | Not owed — month-end artifact |

## Working-data checklist (gitignored `.work/`, never published)

| Working artifact | Result |
|---|---|
| `build_index_universe.py` | **OK** — 515 tickers (503 S&P 500, 101 Nasdaq-100, 89 overlap) |
| Constituent cache dates | S&P 500 `2026-06-21T21:05:56Z` · Nasdaq-100 `2026-06-21T21:05:56Z` (44 days old; used as-is per `rules.md § Index-Union Universe Protocol` rule 5) |
| `technical_indicators.py` | **OK** — 519 symbols, daily/weekly/monthly pack |
| stockanalysis 5Y bulk history | **OK** — 519/519 in 16.6s, 0 failures |
| `settlement_ledger.py` | **OK** — 960 candidate rows, 48 due, 0 conflicts |
| Nasdaq screener (market cap + sector) | **OK** — 7095 rows |
| Forward earnings calendar sweep | **OK** — 28 business days 2026-08-04…2026-09-10, 0 failures |
| Risk-free rate | **OK (fallback)** — 3.75% from US Treasury daily_treasury_bill_rates (13-wk bank discount); FRED `fredgraph.csv` timed out |
| VIX | **OK** — 15.86 on 08/03/2026 (cdn.cboe.com VIX_History.csv) |
| IBKR MCP snapshot | **FAILED** — connector connection invalidated; documented, not fatal (3 web sources already agree exactly) |

## Core ETF Market Forecast Block

**Present and complete** — SPY, QQQ, SOXX in `03_regime_and_data.md`, summarized in `09`, with three
`MARKET_FORECAST` records in `15_predictions.json` carrying `benchmark: "NONE"`,
`benchmark_price: null`, `adj_score: null` per `rules.md`.

## Outstanding blockers

1. **`Fund_Z` and `Sent_Z` are `UNAVAILABLE` universe-wide** — makes evidence thresholds 2, 3 and 4
   arithmetically unsatisfiable. Engineering task (Phase 2 of the `Fund_Z`/`Sent_Z` plan), not a
   prompt mutation. Sole cause of every non-`GO` package since 2026-07-01.
2. **Rank-order inversion** — weighted-mean rank IC -0.0879; all confidence capped `MEDIUM`.
3. **`eff_n` = 1** — no Track A calibration change is eligible until `eff_n >= 3`.
