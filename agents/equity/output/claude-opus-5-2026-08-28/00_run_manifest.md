# 00 — Run Manifest · 2026-08-28 *(backfilled)*

> **BACKFILLED 2026-09-03** — the 2026-08-28 scheduled run wrote `01`-`07` and `15_predictions.json`
> and then truncated before publishing this artifact. It is reconstructed here from that package's
> **own committed data** (`01`-`07`, `15_predictions.json`) by the 2026-09-03 run. No analytical content
> is invented: anything the truncated run never persisted is marked `UNAVAILABLE` rather than
> recomputed from a different basis. No prediction record was added, altered, or removed.

| Field | Value |
|---|---|
| Run date | **2026-08-28** (Friday) |
| Model | `claude-opus-5` |
| Fire window | 22:08 ET — post-close |
| Run mode | scheduled daily run, full pipeline, **truncated after `15_predictions.json`** |
| Data mode | `DELAYED` |
| Price basis | 2026-08-28 completed close |
| **Final status** | **`NO_TRADE`** |
| Universe label | `INDEX_UNION_PCTL (n=510)` |
| Reflection baseline | see `02` |

## GO-Gate Table (Required inputs only)

Carried from `01`, which records all five Required inputs as grounded.

| # | Required input | Status |
|---|---|---|
| 1 | Grounded entry price per the Price Sourcing Standard | **PASS** — 27/27 published symbols on three independent sources at 0.0000% max deviation |
| 2 | ~60 trading days of fetched history per name and for SPY | **PASS** — 518/519 symbols x 5Y daily in 12.7s |
| 3 | sigma via the Sigma Fallback Chain | **PASS** — `REALIZED_VOL_30D` on all 27 records |
| 4 | Next earnings date — confirmed or cadence-estimated | **PASS** — see `01`/`05` |
| 5 | Index-union universe from `build_index_universe.py` | **PASS** — 510 names scored |

**All five Required inputs grounded; the run is `NO_TRADE` on candidate quality.** Enhancing inputs
missing (caps, not blockers): options IV/skew, short interest/borrow, bid-ask tape, analyst
revision tape, institutional flow.

## Prediction settlement summary

| Quantity | Value |
|---|---|
| Settled this run | 0 — `settlements: []` by design (`02 § 0`) |
| Due inventory | 2 (both `EQR`, `UNSETTLEABLE_CORPORATE_ACTION`) |
| Conflicts | 0 |
| Canonical rolling `EQUITY_ALPHA` | raw n 1355, 28-day eff_n 2 |
| Canonical rolling `MARKET_FORECAST` | raw n 201, 28-day eff_n 2 |

## Core ETF Market Forecast Block

| ETF | Record written | mu | sigma |
|---|---|---|---|
| SPY | yes | +2.00% | 3.38% |
| QQQ | yes | +2.48% | 5.98% |
| SOXX | yes | +5.36% | 14.57% |

## Durable artifact checklist

Composed on 2026-09-03 by listing the package directory — not composed in advance, which is what
produced the over-claim this backfill corrects.

| Artifact | State | Note |
|---|---|---|
| 00_run_manifest.md | **MISSING** | reconstructed from the package's own committed data |
| 01_preflight.md | **Published** | written by the 2026-08-28 run |
| 02_reflection.md | **Published** | written by the 2026-08-28 run |
| 03_regime_and_data.md | **Published** | written by the 2026-08-28 run |
| 04_universe_summary.md | **Published** | written by the 2026-08-28 run |
| 05_factor_scores.md | **Published** | written by the 2026-08-28 run |
| 06_top_candidates.md | **Published** | written by the 2026-08-28 run |
| 07_portfolio_proposal.md | **Published** | written by the 2026-08-28 run |
| 08_risk_review.md | **Backfilled 2026-09-03** | reconstructed from the package's own committed data |
| 09_final_report.md | **Backfilled 2026-09-03** | reconstructed from the package's own committed data |
| 13_evolution_log.md | **Backfilled 2026-09-03** | reconstructed from the package's own committed data |
| 15_predictions.json | **Published** | written by the 2026-08-28 run |

| Artifact | State | Note |
|---|---|---|
| `10_midday_monitor.md` | not published | checkpoint did not run |
| `11_preclose_check.md` | not published | checkpoint did not run |
| `12_close_log.md` | not published | checkpoint did not run |
| `14_weekly_review.md` | **not published** | 2026-08-28 was a Friday and owed one; deliberately not backfilled because its census would be taken from the 2026-09-03 vantage point (see `13`) |

## Outstanding blockers

| # | Blocker |
|---|---|
| 1 | `Fund_Z` and `Sent_Z` `UNAVAILABLE` universe-wide — the sole reason this run and every run since July is `NO_TRADE` |
| 2 | Two `EQR` prediction keys can never settle (corporate action) |
| 3 | **The run truncated.** `08`, `09` and `13` were reconstructed on 2026-09-03; `14` was not. |
