# 00 — Run Manifest · 2026-08-14

> **AMENDED 2026-08-22.** This package was written on 2026-08-14 but the session truncated before
> `12`, `13`, `14` and before `git pr`, so it sat uncommitted for eight days. It is committed on
> 2026-08-22 alongside that day's run, because its 149 settlements are canonical rows in the
> settlement ledger the 2026-08-22 package publishes. Three artifact-checklist rows below
> over-claimed artifacts that were never written and are corrected in place, preserving the original
> claim as *(was "Published")*. `13_evolution_log.md` has been backfilled. **No analytical content,
> price, score, or prediction in this package has been altered.**

| Field | Value |
|---|---|
| Run date | `2026-08-14` (Friday, a full trading session) |
| Price basis | `2026-08-14` close — final at every vendor |
| Fire window | 2026-08-15 01:36 ET (Saturday), post-close on the 2026-08-14 session |
| Model | `claude-opus-5` |
| Run mode | Post-close, full pipeline |
| Data mode | `DELAYED` — every price fetched this run; no real-time feed wired |
| Status target | `GO` |
| **Final status** | **`NO_TRADE`** |
| Regime | `BULL` |
| Universe | `INDEX_UNION_PCTL (n=511)` |
| Published names | 24 (monitoring sleeve only — no investable set) |
| Target date | `2026-09-11` (`run_date + 28d`) |

## Run-date convention

The scheduled task fired at **2026-08-15 01:36 ET (Saturday), post-close on the 2026-08-14 session** — after midnight Eastern, so the Eastern
calendar date was already Saturday 2026-08-15 while the local (Pacific) wall clock still read
Friday 2026-08-14. The run is dated **`2026-08-14`** because that is the date of the session
this package analyses and settles against: every price, indicator, score and settlement in it
is a 2026-08-14-close artifact. Dating it 2026-08-15 would label a fresh post-close run as a
weekend run that adds no market information, and would leave a completed trading day with no
package. This extends the 2026-08-07 precedent (a pipeline that *crossed* midnight kept its
fire date) to a run that *started* after midnight ET.

## State transitions

`PRECHECK -> REFLECTION -> DATA_OK -> TECHNICALS_OK -> SCORED -> PORTFOLIO_DRAFT ->
RISK_REVIEW -> PUBLISHED -> CLOSE_LOGGED -> EVOLUTION_REVIEW`

No stage halted. `PORTFOLIO_DRAFT` terminated at the Task-0 feasibility pre-check with
`NO_TRADE` on evidence thresholds, so no weights were drafted and the revision budget was
untouched.

## Agents executed

Orchestrator (manifest, preflight, reflection, publication) · Data and Regime · Factor
Scoring · Portfolio Construction (Task-0 pre-check only) · Risk Committee · Evolution.

## Reflection baseline

| Field | Value |
|---|---|
| Baseline folder | `agents/equity/output/claude-opus-5-2026-07-24` |
| Baseline flag | **`NONE`** — same-model, in-window, no gap |
| Selection | Step 2 rule 3: window `[2026-06-30, 2026-07-24]`, target `2026-07-17`; the only same-model folder in-window, delta 7d (not `> 7d`, so no `BASELINE_WINDOW_GAP`); age 21d, exactly at the 21-day floor |
| Tie-break (rule 8) | **Not triggered** — one same-model in-window candidate. Two cross-model folders sit at delta 0d (`claude-fable-5-2026-07-17`, `gpt-5-2026-07-17`) but rule 3 (same model) precedes rule 4 (cross-model), so they are not tied candidates. Both are reported in `02 § 1` anyway. |

## Prediction settlement summary

| Field | Value |
|---|---|
| Settled this run | **149** (131 `EQUITY_ALPHA` + 18 `MARKET_FORECAST`) |
| Timing conventions | 100 `ORDINARY` · 49 `TARGET_DATE_CLOSE` |
| Due inventory after write | **0** · conflicts **0** |
| Canonical `EQUITY_ALPHA` | raw `n` = **950** · 28d `eff_n` = **2** |
| Canonical `MARKET_FORECAST` | raw `n` = **150** · 28d `eff_n` = **2** |
| Track A eligibility | **False** — `INSUFFICIENT_EFFECTIVE_N` (needs `eff_n >= 3`) |

`eff_n` reached **2** for both record types this run, confirming the falsifiable projection
made on 2026-07-28 (which predicted `EQUITY_ALPHA` `eff_n -> 2` on 2026-08-05). The next
increment is projected for **2026-09-03**
(`EQUITY_ALPHA`) and **2026-09-07**
(`MARKET_FORECAST`), at which point Track A calibration work becomes eligible for the first
time.

## GO-Gate Table — Required inputs

| Required input (`rules.md § Input Classification`) | Status | Evidence | Blocks `GO`? |
|---|---|---|---|
| 1. Grounded entry price (Price Sourcing Standard) | **GROUNDED** | 137/137 price-date checks across 3 independent vendors, max deviation 0.000000% | No |
| 2. ~60 trading days of history per name + SPY | **GROUNDED** | 519/519 symbols x 5y daily bars (median 1,255 bars) | No |
| 3. `sigma` via the Sigma Fallback Chain | **GROUNDED** | `REALIZED_VOL_30D` for all 511 scored names and all 3 core ETFs | No |
| 4. Next earnings date | **GROUNDED** | forward calendar sweep, 26/26 business days, complete | No |
| 5. S&P 500 ∪ Nasdaq-100 index union | **GROUNDED** | `build_index_universe.py` -> 515 tickers | No |

**All five Required inputs are grounded.** `NO_TRADE` is therefore *not* a data-availability
verdict — it is an evidence-threshold verdict (see below).

### Enhancing inputs (caps, never blockers)

| Enhancing input | Status | Effect (never a `GO` blocker) |
|---|---|---|
| Options IV / skew | `UNAVAILABLE` | no feed wired; sigma falls to `REALIZED_VOL_30D` |
| Short interest / borrow | `UNAVAILABLE` | contributes to `Sent_Z` being `UNAVAILABLE` |
| Bid-ask spread tape | `UNAVAILABLE` | 50bp exclusion filter cannot be applied |
| Analyst revision tape | `UNAVAILABLE` | contributes to `Sent_Z` being `UNAVAILABLE` |
| Institutional ownership flow | `UNAVAILABLE` | contributes to `Sent_Z` being `UNAVAILABLE` |
| Fundamental feed (revisions, margins, FCF) | `UNAVAILABLE` | `Fund_Z` `UNAVAILABLE` universe-wide; the binding constraint this run |

## Why `NO_TRADE`

`rules.md § Evidence Thresholds` requires all five conditions. With `Fund_Z` and `Sent_Z`
`UNAVAILABLE` universe-wide, three of them are **arithmetically unsatisfiable** by any name:

| # | Threshold | Attainable this run | Satisfiable? |
|---|---|---|---|
| 1 | Adjusted-score pctl >= 80th | pctl up to 100.00 | Yes |
| 2 | >= 3 of 4 families non-negative | at most **2** (Technical, Macro) | **No** |
| 3 | No family > 50% of conviction | Technical carries 0.30/0.45 = **66.7%** | **No** |
| 4 | Data completeness >= 85% | DQ **0.80** = 80% | **No** |
| 5 | No hard stop from `§ Stop Criteria` | none triggered | Yes |

Portfolio feasibility is **not** the cause: the sleeve-beta band is attainable
([-0.2791, +1.5397]
spans the 0.90–1.10 band), correlation and drawdown both pass. See `07` and `08`.

## Outstanding blockers

1. **`Fund_Z` / `Sent_Z` unwired at universe scale** — the single cause of every `NO_TRADE`
   since July. Phase 2 of `agents/equity/plan/2026-07-15-claude-fable-5-top-priority.md`
   (bulk `companyfacts.zip` + threaded Nasdaq fetch across all 511 names) remains unattempted;
   the shadow tooling covers ~4.7% of the universe against a 70% bar.
2. **`eff_n = 2 < 3`** — blocks every Track A calibration fix until
   2026-09-03.
3. **Missing packages for 2026-08-11, 2026-08-12, 2026-08-13** — three trading days with no
   package from any model. Not backfilled (that would require retroactive `OPEN` prediction
   records); recorded in `13` and `14`.

## Core ETF Market Forecast Block

**Produced** — `03 § Core ETF Market Forecast Block`, one row each for SPY, QQQ, SOXX, with
all three `MARKET_FORECAST` records written to `15_predictions.json`.

## Durable artifact checklist

| Artifact | Status | Note |
|---|---|---|
| `00_run_manifest.md` | Published | this file |
| `01_preflight.md` | Published | Source Ledger, 122 rows |
| `02_reflection.md` | Published | settlement + MoM vs `claude-opus-5-2026-07-24` |
| `03_regime_and_data.md` | Published | regime `BULL`; Core ETF Market Forecast Block |
| `04_universe_summary.md` | Published | 511 scored / 4 rejected |
| `05_factor_scores.md` | Published | ranked table + attribution for all 24 |
| `06_top_candidates.md` | Published | monitoring sleeve summary |
| `07_portfolio_proposal.md` | Published | no-trade rationale + feasibility evidence |
| `08_risk_review.md` | Published | committee decision `NO_TRADE` |
| `09_final_report.md` | Published | `Run Status: NO_TRADE` |
| `10_midday_monitor.md` | Not created | no midday checkpoint ran (post-close fire) |
| `11_preclose_check.md` | Not created | no pre-close checkpoint ran (post-close fire) |
| `12_close_log.md` | **Not written** *(was "Published")* | session truncated before this stage; not backfilled — an observation artifact for a moment never observed (see `13`) |
| `13_evolution_log.md` | **BACKFILLED 2026-08-22** *(was "Published")* | session truncated before this stage; reconstructed from this package's own data, `NO_CHANGE_ACCEPTED` |
| `14_weekly_review.md` | **Not written** *(was "Published")* | session truncated before this stage; not backfilled — its census would have to be taken from a later vantage point (see `13`) |
| `15_predictions.json` | Published | 24 `EQUITY_ALPHA` + 3 `MARKET_FORECAST` + 149 settlements |
| `16_monthly_review.md` | Not created | not the last trading day of August |

## Working-data checklist

| Working artifact (`.work/`, gitignored) | Result | Detail |
|---|---|---|
| `eligible_universe.txt` / `universe_summary.json` | **OK** | 503 S&P 500 ∪ 101 Nasdaq-100, 89 overlap -> 515 union; caches fetched 2026-06-21 (54 days stale) |
| `technical_indicators.json` | **OK** | 519 symbols, daily/weekly/monthly blocks, benchmark SPY |
| `run_computed_manifest.json` | **OK** | 511 scored records + winsor bounds + ETF block |
| `settlement_manifest.json` | **OK** | due_inventory 0, conflicts 0 |
| `settlements_this_run.json` | **OK** | 149 rows, 0 skipped |
| `price_verification.json` | **OK** | 137/137 grounded, max dev 0.000000% |
| `portfolio_analysis.json` | **OK** | Task-0 feasibility + naive top-20 EW analytics |
| `reflection_data.json` | **OK** | 26 EQ + 3 MF MoM rows |
| stockanalysis raw/adj CSV history trees | **OK — not committed** | ~72MB; regenerable from `stockanalysis_history_manifest.json` (source URL, retrieval timestamp, per-symbol bar counts, last raw/adj closes, ex-div flags) |
