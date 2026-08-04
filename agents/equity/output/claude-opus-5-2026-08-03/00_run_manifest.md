# 00 — Run Manifest — 2026-08-03

| Field | Value |
|---|---|
| Run date | 2026-08-03 (Monday) |
| Fired at | 2026-08-03 20:08 ET — **post-close**, the 2026-08-03 close is final at every vendor |
| Model | `claude-opus-5` |
| Run mode | Scheduled daily run, full pipeline |
| Data mode | `DELAYED` — every quote fetched this run; no real-time feed is wired |
| Price basis | 2026-08-03 completed close — technicals, entry prices and settlements share **one** basis |
| Status target | `GO` |
| **Final status** | **`NO_TRADE`** |
| Regime | `BULL` |
| Target date | 2026-08-31 (`run_date + 28d`) |
| Reflection baseline | `agents/equity/output/claude-fable-5-2026-07-06` |
| Baseline flag | `CROSS_MODEL_BASELINE` |
| Universe | 512 scored of 515 index-union names |
| Data-quality multiplier | 0.80 |

## State transitions

`PRECHECK -> REFLECTION -> DATA_OK -> TECHNICALS_OK -> SCORED -> PORTFOLIO_DRAFT -> RISK_REVIEW -> NO_TRADE -> EVOLUTION_REVIEW`

No stage halted. `NO_TRADE` is reached at the evidence-threshold gate, before portfolio sizing.

## Agents executed

| Stage | Agent | Artifacts | Result |
|---|---|---|---|
| 0 | Orchestrator — Reflection | `02` | 88 predictions settled, 0 conflicts |
| 1 | Data and Regime | `03`, working universe files | regime `BULL`, 512 names handed off |
| 2 | `technical_indicators.py` | working indicator pack | 519 symbols, daily/weekly/monthly |
| 3 | Factor Scoring | `04`, `05` | 205 names ranked, 103 at pctl >= 80 |
| 4 | Portfolio Construction | `06`, `07` | Task-0 feasibility computed; no sizing (thresholds fail) |
| 5 | Risk Committee | `08` | `NO_TRADE` recommendation |
| 6 | Evolution | `13` | one Track B change proposed |

## GO-Gate Table — Required inputs (the only possible blockers)

| Required input | State | Evidence |
|---|---|---|
| Grounded entry price (Price Sourcing Standard) | PASS | 27/27 published symbols grounded on 3 independent sources; max deviation 0.0788% |
| ~60 trading days of fetched history per name and for SPY | PASS | 519/519 symbols, 183.4s, 0 failures; modal history 1,255 daily bars (5y) |
| sigma via the Sigma Fallback Chain | PASS | REALIZED_VOL_30D computed for all 512 scored names (step 2; no options feed, so IV30 unavailable) |
| Next earnings date | PASS | Complete forward calendar sweep, 28/28 business days, 0 transport failures; 195 names with a dated print, remainder NO_PRINT_IN_WINDOW |
| S&P 500 union Nasdaq-100 index-union universe | PASS | build_index_universe.py succeeded: 515 tickers (503 SPX, 101 NDX, 89 overlap) |

**No Required input is missing.** `NO_TRADE` is therefore *not* a data-availability outcome — it is
driven by the Evidence Thresholds in `rules.md`, detailed in `05` and `08`.

## Enhancing inputs (caps, never blockers)

| Enhancing input | State | Effect |
|---|---|---|
| Options IV / skew | MISSING | sigma falls to REALIZED_VOL_30D; confidence capped MEDIUM |
| Short interest / borrow | MISSING | contributes to Sent_Z being UNAVAILABLE |
| Bid-ask spread tape | MISSING | 50bps exclusion filter cannot be applied directly; ADV proxy used |
| Analyst revision tape | MISSING | contributes to Sent_Z being UNAVAILABLE |
| Institutional ownership flow | MISSING | contributes to Sent_Z being UNAVAILABLE |
| Full-universe fundamental feed (XBRL at scale) | MISSING | Fund_Z UNAVAILABLE universe-wide |

Per `rules.md § Input Classification`, none of these may block `GO`. They lower the data-quality
multiplier to 0.80 and cap confidence at `MEDIUM`.

## Prediction settlement summary

| Field | Value |
|---|---|
| Settled this run | **88** (76 `EQUITY_ALPHA`, 12 `MARKET_FORECAST`) |
| Timing cohorts | `WEEKEND_TARGET` 49 (Sunday 2026-08-02 targets) · `TARGET_DATE_CLOSE` 39 (same-day, post-close) |
| Conflicts | 0 |
| Due inventory after this run | **0** |
| Canonical `EQUITY_ALPHA` | raw `n` = **515**, 28-day `eff_n` = **1** |
| Canonical `MARKET_FORECAST` | raw `n` = **90**, 28-day `eff_n` = **1** |
| Track A calibration gate | **not eligible** — `INSUFFICIENT_EFFECTIVE_N` (needs `n >= 20` **and** `eff_n >= 3`) |

`eff_n` projection is unchanged and still on schedule: `EQUITY_ALPHA` increments to 2 on
**2026-08-05** (43 pending),
`MARKET_FORECAST` on **2026-08-09** (6 pending).

## Source Ledger coverage

| Class | Rows | Status |
|---|---|---|
| `OBSERVED` | 75 | entry prices, cross-vendor confirmations, earnings dates |
| `DERIVED` | 81 | indicators, risk analytics, scores, targets/CI |
| `INFERRED` | 25 | regime call and per-name thesis language |
| `UNAVAILABLE` | 1024 | `Fund_Z` and `Sent_Z` inputs, universe-wide |
| `ILLUSTRATIVE` | 0 | none — this is a live-data run |

Status eligibility: `DELAYED` data mode with all five Required inputs grounded is a valid `GO`
candidate under `rules.md § Input Classification`. It did not reach `GO` on evidence, not on data.

## Core ETF Market Forecast Block

**Produced** — SPY, QQQ, SOXX, in `03` with full analysis minimum, and as three
`MARKET_FORECAST` records in `15_predictions.json`.

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
| `13_evolution_log.md` | Published |
| `15_predictions.json` | Published |
| `10`–`12` checkpoints | Not created — single post-close fire, those checkpoints did not run |
| `14_weekly_review.md` | Not due — Friday artifact |
| `16_monthly_review.md` | Not due — month-end artifact |

## Working-data checklist (gitignored `.work/`, per the 2026-08-01 retention change)

| Working artifact | Result |
|---|---|
| `eligible_universe.txt` / `universe_summary.json` | OK — 515 tickers; caches fetched 2026-06-21 (43d stale, used as-is per `rules.md § Index-Union Universe Protocol` rule 5) |
| `stockanalysis_history_manifest.json` | OK — 519/519 symbols in 183.4s, 0 failures |
| `technical_indicators.json` | OK — 519 symbols, daily/weekly/monthly blocks |
| `earnings_calendar_sweep.json` | OK — 28/28 business days, sweep_complete=True |
| `settlement_manifest.json` | OK — 872 candidate rows, due_inventory 0 |
| `price_verification.json` | OK — 27 symbols, max deviation 0.0788%, 0 confirmation re-reads |
| `run_computed_manifest.json` | OK — 512 scored records + regime/ETF block |
| `portfolio_analysis.json` | OK — evidence thresholds, Task-0 feasibility, diagnostic sleeve |
| Raw/adjusted CSV history trees | Kept in scratchpad, **not committed** (~72MB); regenerable from `stockanalysis_history_manifest.json` |

## Outstanding blockers

1. **`Fund_Z` and `Sent_Z` are `UNAVAILABLE` universe-wide.** This alone makes evidence
   thresholds 2, 3 and 4 arithmetically unsatisfiable, so `GO` is unreachable for any name
   regardless of price action. Phase 2 of `agents/equity/plan/2026-07-15-claude-fable-5-top-priority.md`
   (bulk `companyfacts.zip` + threaded Nasdaq fetch at universe scale) is the fix, and it is an
   engineering task, not a prompt mutation.
2. **Rank-order inversion.** Weighted-mean rank IC -0.0879 over n=515, non-positive in
   20 of 32 vintages. `agents.md § Calibration Feedback Binding` caps every
   confidence label in this package at `MEDIUM`.
3. **`MARKET_FORECAST` mu derivation** remains the `beta x SPY_mu` category error
   (hit rate 22.09% over n=90). Track A, deferred: `eff_n` = 1 < 3.
