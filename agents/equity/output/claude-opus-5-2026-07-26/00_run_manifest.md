# 00 Run Manifest — 2026-07-26

## Run Identity

- **Run date:** 2026-07-26 (**Sunday** — U.S. equity markets closed all day; last completed session was Friday 2026-07-24)
- **Model:** claude-opus-5
- **Fire time:** ~16:40 ET, scheduled task `daily-investment-system`
- **Run mode:** Weekend full-pipeline publish (`00`–`09`, `13`, `15` per `runbook.md`). `10`/`11`/`12` are stubbed N/A — no intraday, pre-close, or close checkpoint can fire on a day with no session. `14_weekly_review.md` is stubbed N/A (the Friday review for this week was published in full by `claude-opus-5-2026-07-24`). `16_monthly_review.md` is stubbed N/A (the last trading day of July 2026 is Friday 2026-07-31).
- **Data mode:** `DELAYED` — public endpoints only, no live brokerage equity feed. All bars fetched this run.
- **Status target vs final status:** target was `REVIEW_ONLY`/`NO_TRADE` pending evidence; **final status is `NO_TRADE`** (see `§ Status Rationale`).

## Price Basis Disclosure

**Single price basis: the 2026-07-24 official close for every name.** No U.S. equity session has occurred since that close, so the Friday close is simultaneously the most recent tape and the correct entry basis — there is no T-1 / same-day split to reconcile, and nothing about this basis is stale in the sense `rules.md § REVIEW_ONLY` #1 contemplates.

**Grounding strength:** every settlement price and every core-ETF entry price was confirmed by **three independent sources** — stockanalysis.com, `api.nasdaq.com` bulk historical, and `quote.cnbc.com` — agreeing **to the cent (max pairwise difference 0.0000%)** on all 17 settled names plus SPY/QQQ/SOXX. CNBC's `last_time` field reads `2026-07-24` on every symbol, confirming these are Friday closes and not a stale or after-hours tape. See `01_preflight.md § Price Verification`.

## Return Basis — Change From Prior Runs (Track B, this run)

Return-derived metrics (momentum, relative strength, realized vol, downside vol, beta, tracking error, drawdown) and the entire `technical_indicators.json` pack are computed from **adjusted closes** (splits, spin-offs and dividends), while `entry_price`, `target_price` and both CI bounds use the **unadjusted 2026-07-24 close** a trader would actually transact at.

Prior runs computed returns from unadjusted vendor closes. That silently injected mechanical corporate-action gaps into the return series. Concretely, on this exact same price basis the 2026-07-24 package carried **HON at 30-day realized vol 0.4428 and 60-day momentum −42.90%**; both were artifacts of the Honeywell distribution around 2026-06-29, which the Nasdaq series left unadjusted. On the adjusted basis HON is **0.1147 and +9.49%** — the published sigma was inflated 4.6×.

The change is not confined to those names: the corporate-action correction is large but narrow (3 names vs the prior package), while the dividend component shifts most of the book slightly, since momentum and relative strength become total-return measures. Median 60d-momentum shift 0.375pp; median rank move 2 places; the top-30 retains 28 of 30 members. See `13_evolution_log.md` for the full diagnosis, measured scope, and the accepted change.

## Reflection Baseline

- **Baseline folder:** `agents/equity/output/gpt-5-2026-06-28`
- **Flag:** `CROSS_MODEL_BASELINE` — the only `claude-opus-5` folder in existence is `claude-opus-5-2026-07-24`, which is 2 days old and therefore barred by the ≥21-day invariant.
- Window `2026-06-11 → 2026-07-05`, target `2026-06-28`. 31 folders sit in-window; `gpt-5-2026-06-28` is an **exact hit at 0 days from target**. Baseline age 28 days, satisfying the ≥21-day invariant.
- This baseline is also the vintage whose 17 predictions matured today, so `02 § 0` (settlement) and `02 § 2` (MoM table) are computed from the same forecast cohort rather than two loosely-related ones.

## Prediction Settlement Summary

`settlement_ledger.py --output-dir agents/equity/output --as-of 2026-07-26`:

```
due_inventory: 0     conflicts: 0     conflicted_rows: 0
canonical_equity_alpha_settlements: 203   (was 189 before this run)
canonical_market_forecast_settlements: 36 (was 33)
audit_only_rows: 145     rejected_rows: 87     total_candidate_rows: 471
```

**17 predictions matured and were settled this run** — 14 `EQUITY_ALPHA` + 3 `MARKET_FORECAST`, all from vintage `gpt-5-2026-06-28`, all with `target_date = 2026-07-26`. Because that target date is a **Sunday**, every one settles under the `WEEKEND_TARGET` exception at the last trading close at or before target: the **2026-07-24 close**. This is exactly the maturity the 07-24 manifest predicted would fall to "the next run". A second `--as-of 2026-07-26` pass after writing `15_predictions.json` returns `due_inventory: 0, conflicts: 0`.

**Rolling calibration (from `settlement_manifest.json § rolling_metrics`, all models, full history, post-settlement):**

| Metric | EQUITY_ALPHA (n=203) | MARKET_FORECAST (n=36) | Healthy range |
|---|---|---|---|
| Hit rate | 52.22% | **22.22%** | > 50% |
| CI coverage | 75.37% | 66.67% | 55–85% |
| Mean z | −0.2001 | **−0.7047** | −0.5 to +0.5 |
| Rank IC (weighted mean, 14 vintages) | **−0.1282** | n/a | > 0 |
| **`eff_n` (28-day non-overlapping windows)** | **1** | **1** | ≥ 3 for Track A |

**Calibration feedback binding this run:**

- **Rank IC ≤ 0 over ≥ 20 settled equity predictions** (−0.1282, n=203) → all confidence capped at `MEDIUM`. Every published name is independently forced to `LOW` by the family-coverage gap, so the cap is non-binding in effect but is logged as active.
- CI coverage 75.37% sits inside the healthy band → **no sigma-widening override fires**.
- **`eff_n = 1` for both record types → no Track A calibration proposal is eligible this run.** Adding 17 settlements moved raw `n` from 189→203 but left `eff_n` at 1, because the new target date (2026-07-26) is only 18 days after the earliest settled target date in the pool — inside the same 28-day window. This is the effective-N gate accepted on 2026-07-24 working exactly as intended.

## GO-Gate Table (Required Inputs Only)

| # | Required Input | Status | Evidence |
|---|---|---|---|
| 1 | Grounded entry price (Price Sourcing Standard) | **GROUNDED** | 2026-07-24 close for all 24 published names + SPY/QQQ/SOXX; the 17 settlement names verified by 3 independent sources at 0.0000% max difference (ledger rows L001–L030) |
| 2 | ~60 trading days fetched history per name + SPY | **GROUNDED** | 514/515 union names fetched (185–1,255 daily bars each, 2021-07-26 → 2026-07-24) plus SPY/QQQ/SOXX/TLT. Only `FDXF` excluded (40 bars from 2026-05-28; fails the >6-month listing-age filter) |
| 3 | `sigma` via Sigma Fallback Chain | **GROUNDED** | `REALIZED_VOL_30D` computed for all 514 names + 3 core ETFs from the fetched adjusted bars. No options feed wired → `IV30` skipped per the chain; step 2 succeeded universe-wide so `SECTOR_MEDIAN` was never needed |
| 4 | Next earnings date (confirmed or cadence-estimated) | **GROUNDED for all 24 published names** | 56 names fetched across two bounded passes; 34 `CONFIRMED` from `api.nasdaq.com/api/analyst/{sym}/earnings-date`, 22 resolved by the 2026-07-24 vendor-empty rule. 6 third-pass entrants (MTB, AON, ESS, ITW, WM, JNJ) were **excluded from publication** rather than published penalty-free |
| 5 | Index-union universe from `build_index_universe.py` | **GROUNDED** | 515 tickers (503 S&P 500, 101 Nasdaq-100, 89 overlap) from caches stamped `2026-06-21T21:05:56Z`; `universe_summary.json` |

**All five Required inputs are grounded.** No Required input blocks this run.

**Enhancing inputs missing** (per `rules.md § Input Classification` these are confidence/exposure caps, *never* `GO` blockers): options IV/skew, short interest & borrow, bid-ask spread tape, analyst revision tape, institutional ownership flow. Their absence sets the data-quality multiplier to 0.80 and would cap gross exposure at 50% in a `GO` run.

## Status Rationale

**Final status: `NO_TRADE`**, under `rules.md § Downgrade to NO_TRADE` #1 (fewer than 5 names pass the investable threshold) and #6 (the set is structurally infeasible).

Two independent, individually sufficient blockers:

1. **Evidence threshold #2 fails for all 514 names.** `Fund_Z` and `Sent_Z` are `UNAVAILABLE` universe-wide — no fetch path is wired and the SHADOW tooling is explicitly not promoted (`rules.md § SHADOW Diagnostic Tooling`). Only 2 of 4 families are available, so "≥3 of 4 non-negative" is unreachable by construction. Best case in the universe is 2 non-negative (200 names).
2. **Evidence threshold #4 fails for all 514 names.** Data completeness is 0.80 < 0.85.

A third, independent blocker sits downstream: the **Task-0 portfolio feasibility pre-check fails on beta**. 41.2% of the universe carries negative 60-day beta, and the top-10 ranked names have a *maximum attainable* sleeve beta of **−0.159** under the 5% single-name cap against the mandatory 0.90–1.10 band. Even if the family gap were closed tomorrow, this candidate set could not be sized into a compliant portfolio.

**Why `NO_TRADE` and not `REVIEW_ONLY`.** The weekend precedent (`gpt-5-2026-07-04`, `gpt-5-2026-07-05`, `claude-fable-5-2026-07-04/05`) published `REVIEW_ONLY`, and that reading is available here. I depart from it deliberately: `REVIEW_ONLY` is defined by data that is "too stale or weak for positioning", but this run's data is neither — all five Required inputs are grounded on the most recent close that exists, verified three ways to the cent. The binding constraint is **candidate quality and portfolio feasibility**, which is precisely what `NO_TRADE` denotes. Labelling a fully-grounded run `REVIEW_ONLY` because it happened to fire on a Sunday would misattribute a structural evidence failure to a data failure. This is the eleventh consecutive `NO_TRADE` and the reason has not changed.

**What this run adds that 2026-07-24 could not.** No session has traded since that package, so the leaderboard is materially the same set of names. The new information is entirely in the settlement and calibration layer — 17 matured forecasts scored, `n` 189→203, and the first out-of-sample read on the `gpt-5-2026-06-28` cohort (rank IC **−0.591**) — plus the corporate-action return-basis correction described above. The re-score is published as a full package because `runbook.md` allows no gaps in the audit trail, and because recomputing the same basis through an independent code path is itself a regression test: **all 514 closes reproduced exactly**, and the only *materially* different derived metrics versus the prior package were the 3 corporate-action names.

## Source Ledger Coverage

| claim_type | Count | Notes |
|---|---|---|
| `OBSERVED` | 34 | 17 three-source verified closes, VIX, risk-free, TLT, universe counts, 24 sector labels (rolled up), earnings dates |
| `DERIVED` | 21 | vol, downside vol, beta, tracking error, drawdown, momentum, RS, ratios, Kelly, CI bounds, z-scores, settlement arithmetic |
| `INFERRED` | 4 | regime call, defensive Macro polarity, thesis lines, vendor-empty earnings resolutions |
| `ILLUSTRATIVE` | 0 | not in illustrative mode |
| `UNAVAILABLE` | 3 | `Fund_Z`, `Sent_Z`, the full Enhancing input block |

**Status eligibility:** ledger coverage is sufficient for `GO`; the blockers are the evidence thresholds and portfolio feasibility, not grounding.

## Agents Executed

| Stage | Agent | Artifact | Outcome |
|---|---|---|---|
| 0 | Orchestrator — Reflection | `02` | 17 settled, `due_inventory: 0`, `conflicts: 0` |
| 1 | Data & Regime | `03`, `eligible_universe.txt`, `universe_summary.json` | `DELAYED`; regime `NEUTRAL`; 515-name union, 514 scored |
| 2 | Technical indicator compute | `technical_indicators.json` | 518 records, all `status: OK`, all `as_of: 2026-07-24` |
| 3 | Factor Scoring | `04`, `05` | 514 ranked; 0 investable; 24 published to the monitoring sleeve |
| 4 | Portfolio Construction | `06`, `07` | Task-0 feasibility pre-check failed on beta → `NO_TRADE` recommended before any sizing |
| 5 | Risk Committee | `08` | `APPROVE` the `NO_TRADE` publication; 0 revision passes used |
| 6 | Evolution | `13` | 1 Track B change **ACCEPTED** (adjusted-close return basis) |

**State machine:** `PRECHECK → REFLECTION → DATA_OK → TECHNICALS_OK → SCORED → PORTFOLIO_DRAFT(pre-check failed) → RISK_REVIEW → PUBLISHED → NO_TRADE`. No `HALTED` condition arose. Revision budget unused (0 of 1).

## Artifact Checklist

| Artifact | Status |
|---|---|
| `00_run_manifest.md` | ✅ this file |
| `01_preflight.md` | ✅ Source Ledger, 30 rows + verification table |
| `02_reflection.md` | ✅ settlement + MoM + carry-forward |
| `03_regime_and_data.md` | ✅ incl. Core ETF Market Forecast Block |
| `04_universe_summary.md` | ✅ |
| `05_factor_scores.md` | ✅ |
| `06_top_candidates.md` | ✅ |
| `07_portfolio_proposal.md` | ✅ no-trade rationale + feasibility evidence |
| `08_risk_review.md` | ✅ |
| `09_final_report.md` | ✅ |
| `10_midday_monitor.md` | ✅ stub — N/A, market closed |
| `11_preclose_check.md` | ✅ stub — N/A, market closed |
| `12_close_log.md` | ✅ stub — N/A, market closed |
| `13_evolution_log.md` | ✅ 1 Track B ACCEPTED |
| `14_weekly_review.md` | ✅ stub — N/A, not Friday |
| `15_predictions.json` | ✅ **24 EQUITY_ALPHA + 3 MARKET_FORECAST + 17 settlements** |
| `16_monthly_review.md` | ✅ stub — N/A, not last trading day of month |
| `eligible_universe.txt` | ✅ 515 tickers |
| `universe_summary.json` | ✅ |
| `technical_indicators.json` | ✅ 518 records |
| `settlement_manifest.json` | ✅ `due_inventory: 0` |
| `run_computed_manifest.json` | ✅ support artifact — every table in this package is generated from it |
| `price_verification.json` | ✅ 17 symbols × 3 sources |

**Core ETF Market Forecast Block:** present and complete (SPY, QQQ, SOXX) in `03`, summarized in `09`, with three `MARKET_FORECAST` records in `15_predictions.json`.

## Outstanding Blockers

1. **`Fund_Z` / `Sent_Z` unavailable universe-wide.** The single highest-value unblock in the system; requires Phase 2 of `agents/equity/plan/2026-07-15-claude-fable-5-top-priority.md` (bulk `companyfacts.zip` + threaded Nasdaq fetch to ≥70% universe coverage). Eleven consecutive `NO_TRADE` runs trace to this.
2. **`eff_n = 1`.** No Track A calibration change can be validated until forecasts resolve into ≥3 non-overlapping 28-day windows — roughly 2026-08-21 and 2026-09-18 at the current cadence.
3. **MARKET_FORECAST calibration remains broken** (22.22% hit rate, mean z −0.705). Root cause diagnosed 2026-07-24 (`mu_ETF = beta × SPY_mu` is a category error); both candidate fixes were tested and rejected, and no further Track A attempt is permitted at `eff_n = 1`.
4. **Vendor-empty earnings signature rule is loose.** Observed this run: EQR and PKG tripped the "print-like signature" test on volume alone (1.97× and 2.13× median) with 1-day moves of 0.01% — a flat tape is not a print. Logged as an observation in `13`; not this run's Track B change.
