# 00 Run Manifest — 2026-07-22

## Run Identity

- **Run date:** 2026-07-22 (Wednesday)
- **Model:** claude-sonnet-5
- **Fire time:** ~16:42 ET (after the 16:00 ET close; no pre-open run fired for this model today)
- **Run mode:** At-close full-pipeline publish (`00`–`09`, `13`, `15` per `runbook.md`, plus a real `12_close_log.md` since the run executes after today's close). `10_midday_monitor.md` and `11_preclose_check.md` are stubbed N/A (those checkpoints never fired today). `14_weekly_review.md` is stubbed N/A (today is Wednesday, not Friday). `16_monthly_review.md` is stubbed N/A (not the last trading day of July).
- **Data mode:** `DELAYED` — public endpoints only (no brokerage feed wired for equities); Nasdaq quote-info official-close prices and Nasdaq bulk historical + IBKR MCP cross-checks, all fetched this run.
- **Status target vs final status:** Target was `GO`/`REVIEW_ONLY` pending evidence; **final status is `NO_TRADE`** (see `§ Status Rationale`).

## Price Basis Disclosure

Two distinct price bases were used and are labeled throughout:

1. **Technical/analytics basis (2026-07-21 close):** Nasdaq's bulk historical endpoint (`api.nasdaq.com/api/quote/{sym}/historical`) does not publish the same-day close for hours after the 16:00 ET bell (confirmed precedent from the 2026-07-17 run, reconfirmed today). All 5-year daily bars, `technical_indicators.json`, beta, realized vol, drawdown, momentum, and relative-strength figures are computed through **2026-07-21** (the most recent close in the bulk fetch at run time).
2. **Entry-price basis (2026-07-22 official close):** for the three core ETFs, all 26 named candidates in `05`/`06`/`07` (new `EQUITY_ALPHA`/`MARKET_FORECAST` predictions being created today), and for settling today's 17 matured predictions, prices were fetched individually via `api.nasdaq.com/api/quote/{sym}/info`, using only rows where `secondaryData.lastTradeTimestamp` carries the `"Closed at Jul 22, 2026 4:00 PM ET"` marker (the documented same-day-official-close pattern). This is one trading day more current than the technical basis and is disclosed per name in the Source Ledger. For the 17 settlements specifically, this required the `TARGET_DATE_CLOSE` declaration (`timing_flag` + timezone-aware `settled_at` ≥ 16:00 ET) — see `§ Prediction Settlement Summary`.

## Reflection Baseline

- **Baseline folder:** `agents/equity/output/gpt-5-2026-06-24` (cross-model; run_date 2026-06-24 sits exactly on the target `run_date - 28d`).
- **Flag:** `CROSS_MODEL_BASELINE` (no same-model `claude-sonnet-5` folder falls inside the 2026-06-07 to 2026-07-01 MoM window; `claude-sonnet-5-2026-07-02`/`-07-03` are outside the window). Window gap = 0 days from target.

## Prediction Settlement Summary

`settlement_ledger.py` run against all packages in `agents/equity/output/` (`--as-of 2026-07-22`): 17 predictions were due today (all from `gpt-5-2026-06-24`, vintage 2026-06-24, target_date 2026-06-24+28d=2026-07-22). **All 17 settled at today's (2026-07-22) official close** using the `TARGET_DATE_CLOSE` mechanism (`timing_flag = TARGET_DATE_CLOSE` + timezone-aware `settled_at` ≥ 16:00 ET) — this Track B change was accepted during a **concurrent gpt-5 run today** (main commit `51c7777`, rebased onto mid-run); this run's own first draft mis-applied the pre-existing unconditional same-day prohibition before discovering the fix on rebase and adopting it. Verified via `settlement_ledger.py`: `due_inventory` 17 → 0, 0 conflicts.

- 14 `EQUITY_ALPHA`: **10 HIT / 4 MISS (71.4% hit rate this batch)**; 9 `IN_CI`, 2 `OUT_CI_HIGH`, 3 `OUT_CI_LOW` — see `02_reflection.md § 0` for the exact per-name breakdown.
- 3 `MARKET_FORECAST` (SPY/QQQ/SOXX): SPY HIT, QQQ MISS, SOXX MISS.
- Rolling canonical totals **before** today's batch (from `settlement_manifest.json`, all models/history): 175 canonical `EQUITY_ALPHA` settlements (hit rate 51.43%, CI coverage 77.14%, mean z −0.236), 30 canonical `MARKET_FORECAST` settlements (hit rate 20.0%, CI coverage 60.0%), weighted rank IC −0.0489 across 12 vintages with ≥12 observations each. **Including today's 17 new canonical settlements** (verified via a second `settlement_ledger.py` pass after publishing `15_predictions.json`): 189 equity (hit rate 52.91%, CI coverage 76.19%, mean z −0.213), 33 market forecast; weighted rank IC moves to **−0.0980** across 13 vintages — today's single-vintage rank IC is a statistically significant **−0.712** (Spearman, p=0.004, n=14): a good hit rate (71.4%) alongside a badly inverted rank order. See `13_evolution_log.md`.
- **Calibration feedback binding today:** rank IC ≤ 0 over ≥ 20 settled equity predictions (189 ≥ 20) → confidence capped at `MEDIUM` per `rules.md § Rolling Calibration Metrics`. In practice every ranked name today is already forced to `LOW` by the independent structural family-coverage gap below, so this cap is non-binding in effect but is logged as active per the audit requirement. CI coverage 76.19% is inside the healthy 55–85% band, so no sigma-widening override fires.

## GO-Gate Table (Required Inputs Only)

| # | Required Input | Status | Evidence |
|---|---|---|---|
| 1 | Grounded entry price (Price Sourcing Standard) | **GROUNDED** | Nasdaq quote-info official-close fetch (2026-07-22, `retrieved_at` ~20:4x–21:0xZ) for every new candidate/ETF entry price and for today's 17 matured-prediction settlements (via the `TARGET_DATE_CLOSE` mechanism — see `§ Prediction Settlement Summary`); IBKR `get_price_snapshot` cross-check on SPY (748.23 AH print vs 747.48 official close, 0.1% apart, consistent with documented AH-vs-close artifact) |
| 2 | ~60 trading days fetched history per name + SPY | **GROUNDED** | 518/519 tickers fetched via threaded Nasdaq bulk historical (1,253–1,255 daily bars each, 2021-07-22 through 2026-07-21); BF-B fetched via IBKR `get_price_history` (1,253 bars); only `FDXF` excluded (38 bars, recent spinoff, fails both the 60-bar minimum and the >6-month listing-age inclusion filter) |
| 3 | `sigma` via Sigma Fallback Chain | **GROUNDED** | `REALIZED_VOL_30D` computed for all 514 sourceable names + 3 core ETFs from the fetched daily bars |
| 4 | Next earnings date (confirmed or cadence-estimated) | **GROUNDED for the published candidate set** | `api.nasdaq.com/api/analyst/{sym}/earnings-date` fetched for the top-35-by-score + 14 reflection carry-forwards (48 names), plus a bounded second pass (+6 names: MCO, WAT, USB, MTB, INCY, SNA) after post-penalty re-ranking pulled them into the top 20; a further 9 unfetched near-miss entrants (CTAS, A, EBAY, WELL, UNP, EIX, KHC, AMP, LH) are excluded-with-disclosure from the published Ranked Candidate Table rather than treated as penalty-free, per the bounded-second-pass convention (not fetched universe-wide — earnings preflight is scoped to the shortlist, per `agents.md`) |
| 5 | S&P 500 ∪ Nasdaq-100 index-union universe | **GROUNDED** | `build_index_universe.py` succeeded: 503 S&P 500 + 101 Nasdaq-100, 89 overlap, 515 union (cache `fetched_at` 2026-06-21, reused per `rules.md § Index-Union Universe Protocol` #5) |

All five Required inputs are grounded. Missing **Enhancing** inputs (options IV/skew, short interest, bid-ask tape, analyst revision tape, institutional flow) reduce the data-quality multiplier and cap confidence, per `rules.md § Input Classification`, but do not themselves block `GO`.

## Status Rationale

`NO_TRADE` is driven entirely by **evidence threshold #2** (`rules.md § Evidence Thresholds`): "At least 3 of 4 factor families are non-negative." `Fund_Z` and `Sent_Z` remain `SHADOW`-only and structurally `UNAVAILABLE` at scoring scope today (the Phase-2 bulk promotion described in `rules.md § SHADOW Diagnostic Tooling` has not been attempted) — with only `Tech_Z`/`Macro_Z` ever countable, no name can reach 3-of-4 regardless of score. This is the same structural gap disclosed in every dated package since at least 2026-07-15; it is **not** a data-integrity halt (all Required inputs are grounded — see the GO-Gate Table) and **not** a new finding this run. Stop Criteria's `NO_TRADE` condition #1 ("Fewer than 5 names pass the investable threshold") applies mechanically: **0 names** clear `INVESTABLE_GRADE` because none can ever clear the 3-of-4-families gate. 26 names (20 organic top-ranked + 6 binding reflection carry-forwards) are published to the monitoring sleeve with full `mu`/`sigma`/target/CI per `rules.md § Sigma Fallback Chain`, so every ranked name remains settleable.

## Artifact Checklist

| Artifact | Status |
|---|---|
| `00_run_manifest.md` | Published (this file) |
| `01_preflight.md` | Published — Source Ledger |
| `02_reflection.md` | Published — settlement + MoM table |
| `03_regime_and_data.md` | Published — regime + Core ETF Market Forecast Block |
| `04_universe_summary.md` | Published |
| `05_factor_scores.md` | Published |
| `06_top_candidates.md` | Published |
| `07_portfolio_proposal.md` | Published — `NO_TRADE` rationale |
| `08_risk_review.md` | Published |
| `09_final_report.md` | Published |
| `10_midday_monitor.md` | Stub — checkpoint did not fire today |
| `11_preclose_check.md` | Stub — checkpoint did not fire today |
| `12_close_log.md` | Published — real content (run fires after today's close) |
| `13_evolution_log.md` | Published |
| `14_weekly_review.md` | Stub — not Friday |
| `15_predictions.json` | Published — 26 `EQUITY_ALPHA` + 3 `MARKET_FORECAST` records + 17 settlements |
| `16_monthly_review.md` | Stub — not month-end |
| `eligible_universe.txt` | Published — 515 tickers |
| `universe_summary.json` | Published |
| `technical_indicators.json` | Published — 518 tickers (SPY/QQQ/SOXX + 515 universe, ex-FDXF) |
| `settlement_manifest.json` | Published — canonical settlement ledger output |
| `run_computed_manifest.json` | Published — consolidated computed-analytics support artifact |

## Core ETF Market Forecast Block Status

Present in `03_regime_and_data.md`; SPY, QQQ, SOXX all grounded at `DELAYED` (technical basis 2026-07-21, entry price 2026-07-22 official close). No `UNAVAILABLE` fields.
