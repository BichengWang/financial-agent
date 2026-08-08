# 00 — Run Manifest

| Field | Value |
|---|---|
| Run date | `2026-08-07` (Friday) |
| Model | `claude-opus-5` |
| Fire window | **POST-CLOSE** — 22:02 ET, ~6h after the close |
| Price basis | **2026-08-07** — the same-day completed close |
| Run mode | Scheduled daily run |
| Data mode | `DELAYED` |
| Status target | `GO` |
| **Final status** | **`NO_TRADE`** |
| Reflection baseline | `agents/equity/output/claude-fable-5-2026-07-10` |
| Baseline flag | `CROSS_MODEL_BASELINE` |
| Universe | S&P 500 union Nasdaq-100 index union, `INDEX_UNION_PCTL (n=511)` |

## Fire window and price basis

The run fired at 22:02 ET on 2026-08-07, about six hours after the close. At that hour the
same-day close is final at every vendor: 518
of 519 symbols carry **2026-08-07** as their last bar, so every entry price,
technical indicator and settlement price in this package rests on one internally consistent
completed close — the run date's own. The single exception is documented under
§ Universe rejections.

Zero symbols carried an ex-dividend `c != a` split on the basis bar, so the raw/adjusted
reconciliation that has complicated several prior packages does not arise this run.

## Settlement deferral — 0 of 50 due keys settled

| Field | Value |
|---|---|
| Due keys at `--as-of 2026-08-07` | 50 |
| Priced and scored (diagnostic) | 50 |
| **Published as canonical settlements** | **0** |
| Still due after this run | 50 |
| Conflicts | 0 |
| Rejected rows contributed by this run | 0 |

All 50 due keys carry `target_date == run_date == 2026-08-07` (vintage `2026-07-10`;
44 `EQUITY_ALPHA` + 6 `MARKET_FORECAST`, from `claude-fable-5` and `gpt-5`). A post-close
fire normally settles these under `TARGET_DATE_CLOSE`. This run could not, and the reason is
mechanical rather than evidential: **the pipeline started at 22:02 ET and its settlement pass
ran after midnight**, so a truthful `settled_at` falls on `2026-08-08`. The validator in
`settlement_ledger.py:577` requires `settled_at.date() == target_date` *in addition to* the
16:00 ET floor, and rejects a timestamp that is merely *later* than the target-date close.

All 50 were priced at the grounded 2026-08-07 close and scored; the results are reported as a
diagnostic in `02 § 0` and drive this run's MoM analysis. They are **not** written as canonical
rows, because `rules.md § Canonical Settlement Ledger` item 5 is explicit that such keys are
reported as due and the validator is not loosened without a logged change. They settle
`ORDINARY` on the next run at the same close, so **no settlement evidence is lost** — it is
deferred by one run. The validator fix is this run's Track B proposal in `13_evolution_log.md`.

### Canonical rolling calibration

| Record type | raw `n` | 28-day `eff_n` | Hit rate | CI coverage | Mean z | Track A eligible? |
|---|---|---|---|---|---|---|
| `EQUITY_ALPHA` | 643 | **2** | 39.04% | 69.36% | -0.5328 | False — `INSUFFICIENT_EFFECTIVE_N` |
| `MARKET_FORECAST` | 108 | 1 | 25.96% | 84.26% | -0.5285 | False — `INSUFFICIENT_EFFECTIVE_N` |

Both are unchanged from the 2026-08-06 package because this run added no canonical
settlements. `EQUITY_ALPHA` `eff_n` stays at 2 (windows
['2026-07-08', '2026-08-05']); the next window opens
`2026-09-02` with
24 predictions pending, incrementing
on `2026-09-03`. `MARKET_FORECAST` `eff_n` was projected
to increment on `2026-08-09` — that projection is
**still pending, not yet falsified**: the 6 MF keys that would have moved it are exactly the
ones deferred above.

Weighted-mean rank IC across vintages: **-0.0430**.

## GO-Gate Table — Required inputs

| Required input (`rules.md § Input Classification`) | Status | Evidence | Blocks GO? |
|---|---|---|---|
| 1. Grounded entry price | **PASS** | 27/27 published symbols grounded on 3 independent sources; max deviation 0.0000% | No |
| 2. ~60 trading days of history per name + SPY | **PASS** | 511 scored names with >=61 daily bars (median 1255 bars); SPY 1255 bars | No |
| 3. sigma via the Sigma Fallback Chain | **PASS** | REALIZED_VOL_30D computed for all 24 published names and 3 core ETFs | No |
| 4. Next earnings date | **PASS** | Full-universe forward calendar sweep: 26/26 business days, zero transport failures -> sweep complete; 59 CONFIRMED_CALENDAR, remainder NO_PRINT_IN_WINDOW | No |
| 5. Index-union universe from `build_index_universe.py` | **PASS** | 515 names (503 S&P 500, 101 Nasdaq-100, 89 overlap) | No |

**All five Required inputs are grounded.** `NO_TRADE` is therefore *not* a data-availability
outcome — it is an evidence-threshold outcome, decided below.

### Enhancing inputs (caps only, never GO blockers)

| Enhancing input | Status | Effect (never a GO blocker) |
|---|---|---|
| Options IV / skew | UNAVAILABLE | No IV30 sigma source; REALIZED_VOL_30D used instead |
| Short interest / borrow | UNAVAILABLE | `Sent_Z` family UNAVAILABLE |
| Bid-ask spread tape | UNAVAILABLE | Spread exclusion filter cannot be applied; disclosed |
| Analyst revision tape | UNAVAILABLE | `Sent_Z` family UNAVAILABLE |
| Institutional ownership flow | UNAVAILABLE | `Sent_Z` family UNAVAILABLE |
| Fundamental fetch path (XBRL at universe scale) | UNAVAILABLE | `Fund_Z` family UNAVAILABLE — Phase 2 of the plan is not implemented |

## Evidence thresholds — the actual decision

| # | Evidence threshold | Required | This run | Result |
|---|---|---|---|---|
| 1 | Adjusted-score percentile >= 80th | >= 80.00 | 102 names at or above the 80th pctl | **PASS** |
| 2 | At least 3 of 4 factor families non-negative | >= 3 of 4 | 2 of 4 families available (Tech, Macro); Fund_Z and Sent_Z UNAVAILABLE universe-wide and do not count toward the threshold | **FAIL — unsatisfiable** |
| 3 | No single family > 50% of total conviction | <= 50% | Tech_Z carries 0.30 of the 0.45 live weight = 66.67% | **FAIL — unsatisfiable** |
| 4 | Data completeness >= 85% | >= 85% | DQ multiplier 0.80 (notable coverage gaps: 2 of 4 families missing) | **FAIL** |
| 5 | No hard stop from `rules.md § Stop Criteria` | none triggered | No hard-halt criterion triggered | **PASS** |

Thresholds 2 and 3 are **arithmetically unsatisfiable** while `Fund_Z` and `Sent_Z` are
UNAVAILABLE universe-wide: with only two live families the maximum attainable count is 2, and
Technical necessarily carries 0.30/0.45 = 66.67% of live conviction. No name in
any universe can clear them today, so no name is investable and the run is `NO_TRADE`.

**A second, independent `NO_TRADE` trigger fired this run.** The naive top-20 equal-weight
sleeve's 95th-percentile 1-month drawdown is **9.15%** against the
8.00% cap (`rules.md § Stop Criteria` downgrade #5), and the top-24 set is
41.67%
concentrated in Consumer Discretionary against the
30% sector cap. Either alone would force `NO_TRADE` even if the family thresholds were live.

**The beta band is feasible.** Attainable sleeve beta runs
-0.3876 … 1.3387 against
the 0.90–1.10 band — the **sixth consecutive run** where the 2026-07-27 "provably infeasible"
narrative would have been wrong. It is recomputed every run rather than inherited.

## Universe rejections

| Ticker | Reason | Detail |
|---|---|---|
| BF-B | `MARKET_CAP_UNAVAILABLE` | vendor marketCap field empty |
| EA | `DELISTED_OR_HALTED` | last bar 2026-08-04 != basis 2026-08-07 |
| FDXF | `LISTING_AGE` | 50 daily bars; first bar 2026-05-28 |
| Q | `INDICATOR_INCOMPLETE` | 195 daily bars; weekly/daily MA or MACD UNAVAILABLE |

`EA`'s last bar is 2026-08-04, three sessions stale, which corroborates
the delisting/halt first detected on 2026-08-06 rather than a transient fetch gap.

## Artifact checklist

| Artifact | Status |
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
| `12_close_log.md` | Published — post-close fire |
| `13_evolution_log.md` | Published |
| `14_weekly_review.md` | Published — Friday after close |
| `15_predictions.json` | Published |
| `10_midday_monitor.md` | Omitted — checkpoint did not run (single post-close fire) |
| `11_preclose_check.md` | Omitted — checkpoint did not run (single post-close fire) |
| `16_monthly_review.md` | Not owed — month-end artifact |

## Working-data checklist

| Working artifact (gitignored `.work/`) | Result | Detail |
|---|---|---|
| `eligible_universe.txt` / `universe_summary.json` | SUCCESS | 515 tickers; caches fetched_at 2026-06-21T21:05:56Z (S&P 500) and 2026-06-21T21:05:56Z (Nasdaq-100) |
| `stockanalysis_history_manifest.json` + `raw/` + `adj/` CSV trees | SUCCESS | 519/519 symbols, 0 failures, 12.2s elapsed |
| `technical_indicators.json` | SUCCESS | 519 symbols x daily/weekly/monthly blocks, computed on the adjusted-close tree |
| `earnings_sweep.json` | SUCCESS | 26/26 business days; sweep_complete=True |
| `price_verification.json` | SUCCESS | 27/27 grounded; 0 confirmation re-reads required |
| `run_computed_manifest.json` | SUCCESS | 511 scored, 4 rejected |
| `settlement_manifest.json` | SUCCESS | due_inventory 50, conflicts 0, rejected_rows 87 |
| `settlements_this_run.json` | DIAGNOSTIC ONLY | 50/50 due keys priced and scored, but **0 published as canonical rows** — see § Settlement deferral |
| `nasdaq_screener.json` | SUCCESS | market cap + sector for the universe (one call) |
| `VIX_History.csv` / `treasury_bills_2026.csv` | SUCCESS | VIX close 14.9; 13-week bank discount 3.72% |

## Core ETF Market Forecast Block

| ETF | Forecast produced? | mu | sigma | Confidence |
|---|---|---|---|---|
| SPY | Yes | +2.00% | 3.82% | MEDIUM |
| QQQ | Yes | +2.92% | 7.32% | MEDIUM |
| SOXX | Yes | +5.45% | 18.23% | MEDIUM |

Block produced in full — see `03_regime_and_data.md`.

## Agents executed

`Orchestrator (preflight + reflection)` -> `Data and Regime` -> `technical_indicators.py` ->
`Factor Scoring` -> `Portfolio Construction (Task 0 feasibility pre-check)` -> `Risk Committee`
-> `Evolution`.

State machine: `PRECHECK -> REFLECTION -> DATA_OK -> TECHNICALS_OK -> SCORED ->
PORTFOLIO_DRAFT -> RISK_REVIEW -> PUBLISHED` with final status **`NO_TRADE`**.

## Outstanding blockers

1. `Fund_Z` / `Sent_Z` UNAVAILABLE universe-wide — the single structural cause of every
   `NO_TRADE` in this series. Unblocking needs Phase 2 of
   `agents/equity/plan/2026-07-15-claude-fable-5-top-priority.md` (bulk `companyfacts.zip`
   + threaded Nasdaq sentiment fetch across all 511 names).
2. Track A calibration work stays gated at `eff_n = 2 < 3`.
3. 50 settlement keys deferred one run by the `TARGET_DATE_CLOSE` calendar-date condition
   (Track B proposed in `13_evolution_log.md`).
