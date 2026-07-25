# 00 Run Manifest — 2026-07-24

## Run Identity

- **Run date:** 2026-07-24 (Friday)
- **Model:** claude-opus-5
- **Fire time:** ~23:17 ET — roughly 7¼ hours after the 16:00 ET close. No earlier checkpoint fired for this model today.
- **Run mode:** Post-close full-pipeline publish (`00`–`09`, `13`, `15` per `runbook.md`), plus a real `12_close_log.md` and a real `14_weekly_review.md` (Friday after close). `10_midday_monitor.md` and `11_preclose_check.md` are stubbed N/A — those checkpoints never fired. `16_monthly_review.md` is stubbed N/A (2026-07-24 is not the last trading day of July; 2026-07-31 is).
- **Data mode:** `DELAYED` — public endpoints only, no live brokerage equity feed. All bars fetched this run.
- **Status target vs final status:** target was `GO`/`REVIEW_ONLY` pending evidence; **final status is `NO_TRADE`** (see `§ Status Rationale`).

## Price Basis Disclosure

**Single price basis this run: the 2026-07-24 official close for every name.** Because the run fired ~7 hours after the bell, Nasdaq's bulk historical endpoint had already published the same-day close — unlike the 2026-07-17 and 2026-07-22 at-close runs (~16:4x ET fires), which had to split into a T-1 technical basis plus a separate same-day quote-info entry-price fetch. Technical indicators, beta, realized vol, drawdown, momentum, relative strength, entry prices, and CI bounds are therefore all computed from one consistent 2026-07-24 bar set. This removes the cross-basis reconciliation caveat that the last two at-close packages carried.

**Grounding strength:** every published entry price was confirmed by **three independent sources** — Nasdaq bulk historical, stockanalysis.com, and cnbc.com — agreeing **to the cent (max pairwise difference 0.000%)** on all 26 candidates and all 3 core ETFs. See `01_preflight.md § Price Verification` and `price_verification.json`. This exceeds the Price Sourcing Standard's two-source requirement.

## Reflection Baseline

- **Baseline folder:** `agents/equity/output/gpt-5-2026-06-24`
- **Flag:** `CROSS_MODEL_BASELINE` — no `claude-opus-5` folder exists anywhere (this is the model's first run in this system), so no same-model folder can fall in the MoM window.
- Window `2026-06-09 → 2026-07-03`, target `2026-06-26`. 29 folders sit in-window. `gpt-5-2026-06-24` is 2 days from target; `gpt-5-2026-06-28` ties at 2 days and the tie was broken toward the **earlier** date (more settled forward history). Baseline age 30 days, satisfying the ≥21-day invariant.

## Prediction Settlement Summary

`settlement_ledger.py --output-dir agents/equity/output --as-of 2026-07-24`:

```
due_inventory: 0     conflicts: 0     conflicted_rows: 0
canonical_equity_alpha_settlements: 189
canonical_market_forecast_settlements: 33
audit_only_rows: 145     rejected_rows: 87     total_candidate_rows: 454
```

**No prediction matured on or before 2026-07-24, so this run settles nothing and publishes `"settlements": []` with a note.** This is a genuine empty set, not a missed scan: the last matured target date was 2026-07-22 (settled in full by the two 07-22 runs), and the next maturities are 17 keys dated 2026-07-26 — a Sunday, which will settle under `WEEKEND_TARGET` at the 2026-07-24 close on the *next* run, since `target_date 2026-07-26 > run_date 2026-07-24` today. Verified by an explicit `--as-of 2026-07-24` pass; note that `settlement_ledger.py` defaults `as_of` to the max package run_date, so the explicit flag is required (2026-07-20 precedent).

**Rolling calibration (from `settlement_manifest.json § rolling_metrics`, all models, full history):**

| Metric | EQUITY_ALPHA (n=189) | MARKET_FORECAST (n=33) | Healthy range |
|---|---|---|---|
| Hit rate | 52.91% | **21.21%** | > 50% |
| CI coverage | 76.19% | 63.64% | 55–85% |
| Mean z | −0.213 | **−0.731** | −0.5 to +0.5 |
| Rank IC (weighted mean, 13 vintages) | **−0.0939** | n/a | > 0 |

**Calibration feedback binding this run:**

- **Rank IC ≤ 0 over ≥ 20 settled equity predictions** (−0.0939, n=189) → all confidence capped at `MEDIUM` per `rules.md § Rolling Calibration Metrics`. In practice every published name is already forced to `LOW` by the independent family-coverage gap, so the cap is non-binding in effect but is logged as active.
- CI coverage 76.19% sits inside the healthy band, so **no sigma-widening override fires**.
- The `MARKET_FORECAST` line is reported separately and never pooled with the equity metrics, as required.

**Material caveat established this run:** the raw `n` values above are pseudo-replicated. All 222 canonical settlements originate from a single overlapping forecast cohort — MF vintages span 2026-06-14→06-24 resolving into 2026-07-12→07-22; EQ vintages span 2026-06-10→06-24 resolving into 2026-07-08→07-22. Grouped into non-overlapping 28-day target windows, the **effective independent sample is 1 window for each type**, not 33 and 189. This is the subject of this run's accepted Track B change (`13_evolution_log.md`).

## GO-Gate Table (Required Inputs Only)

| # | Required Input | Status | Evidence |
|---|---|---|---|
| 1 | Grounded entry price (Price Sourcing Standard) | **GROUNDED** | 2026-07-24 close for all 26 candidates + SPY/QQQ/SOXX, confirmed by 3 independent sources to 0.000% max difference (`price_verification.json`, ledger rows L001–L029) |
| 2 | ~60 trading days fetched history per name + SPY | **GROUNDED** | 514/515 union names fetched (1,255–1,307 daily bars each, 2021-07 → 2026-07-24) via threaded Nasdaq bulk historical; BRK-B recovered as `BRK.B`, BF-B via IBKR `get_price_history` conid 4931 (1,255 bars), SATS fetched under its `ECHO` rename. Only `FDXF` excluded (41 bars from 2026-05-27; fails both the 60-bar minimum and the >6-month listing-age filter) |
| 3 | `sigma` via Sigma Fallback Chain | **GROUNDED** | `REALIZED_VOL_30D` computed for all 514 sourceable names + 3 core ETFs from the fetched bars. No options feed is wired, so `IV30` is skipped per the chain; step 2 succeeded universe-wide, so `SECTOR_MEDIAN` was never needed |
| 4 | Next earnings date (confirmed or cadence-estimated) | **GROUNDED for the published set** | `api.nasdaq.com/api/analyst/{sym}/earnings-date` fetched for 52 names (top-40 pre-penalty + 14 baseline carry-forwards), then a **bounded second pass** of 24 more names pulled into the top-40 by post-penalty re-ranking. 48 CONFIRMED; 22 vendor-empty resolved by print-signature analysis (see `01 § Earnings Resolution`). 16 further entrants that appeared only after the second re-rank are **excluded with disclosure** rather than published penalty-free |
| 5 | S&P 500 ∪ Nasdaq-100 index-union universe | **GROUNDED** | `build_index_universe.py` succeeded with default cache paths: 503 S&P 500 + 101 Nasdaq-100, 89 overlap, **515 union**; caches `fetched_at` 2026-06-21, reused per `rules.md § Index-Union Universe Protocol` #5 |

All five Required inputs are grounded. Missing **Enhancing** inputs — options IV/skew, short interest/borrow, bid-ask tape, analyst revision tape, institutional ownership flow — reduce the data-quality multiplier to 0.80 and cap confidence, but per `rules.md § Input Classification` they are **not** `GO` blockers and were not treated as such.

## Status Rationale

`NO_TRADE`, driven entirely by **evidence threshold #2** (`rules.md § Evidence Thresholds`): "At least 3 of 4 factor families are non-negative."

`Fund_Z` and `Sent_Z` remain `SHADOW`-only and structurally `UNAVAILABLE` at scoring scope. `rules.md § SHADOW Diagnostic Tooling` permits citing `fundamental_diagnostics.py` / `sentiment_diagnostics.py` as diagnostics but forbids folding them into `Adj Score`, the evidence-threshold count, or the confidence label until a run promotes the family — and promotion still requires the 70%-of-universe sourceability bar from `§ Financial Metrics and Score Attribution`, which needs the plan's Phase 2 (bulk `companyfacts.zip` + threaded Nasdaq fetch across ~514 names). That has not been attempted, and this run did not attempt it either.

With only `Tech_Z` and `Macro_Z` ever countable, **no name can reach 3-of-4 regardless of its score**. `NO_TRADE` condition #1 ("Fewer than 5 names pass the investable threshold") therefore applies mechanically: **0 of 514 names clear investable grade**. This is the same structural gap disclosed in every dated package since at least 2026-07-15. It is **not** a data-integrity halt — all five Required inputs are grounded — and **not** a new finding.

26 names are published to the monitoring sleeve with full `mu` / `sigma` / target / CI per the Sigma Fallback Chain, so every ranked name remains settleable. Publishing a forecast that can be scored later is how this system earns the evidence it needs; abstaining silently would not be caution, it would be a publishing failure.

## Artifact Checklist

| Artifact | Status |
|---|---|
| `00_run_manifest.md` | Published (this file) |
| `01_preflight.md` | Published — Source Ledger, 133 rows |
| `02_reflection.md` | Published — settlement block + MoM table |
| `03_regime_and_data.md` | Published — regime + Core ETF Market Forecast Block |
| `04_universe_summary.md` | Published |
| `05_factor_scores.md` | Published |
| `06_top_candidates.md` | Published |
| `07_portfolio_proposal.md` | Published — `NO_TRADE` rationale + feasibility pre-check |
| `08_risk_review.md` | Published |
| `09_final_report.md` | Published |
| `10_midday_monitor.md` | Stub — checkpoint did not fire |
| `11_preclose_check.md` | Stub — checkpoint did not fire |
| `12_close_log.md` | Published — real content (post-close fire) |
| `13_evolution_log.md` | Published — 1 Track B ACCEPT, 2 Track A REJECT |
| `14_weekly_review.md` | Published — real content (Friday after close) |
| `15_predictions.json` | Published — 26 `EQUITY_ALPHA` + 3 `MARKET_FORECAST`, `settlements: []` with note |
| `16_monthly_review.md` | Stub — not month-end |
| `eligible_universe.txt` | Published — 515 tickers |
| `universe_summary.json` | Published |
| `technical_indicators.json` | Published — 518 records (515 union + SPY/QQQ/SOXX), 517 OK / 1 UNAVAILABLE |
| `settlement_manifest.json` | Published — canonical settlement ledger output |
| `run_computed_manifest.json` | Published — consolidated computed-analytics support artifact |
| `price_verification.json` | Published — 3-source entry-price verification |

## Core ETF Market Forecast Block Status

Present in `03_regime_and_data.md`. SPY, QQQ, SOXX all grounded at `DELAYED` on the 2026-07-24 close. No `UNAVAILABLE` fields. Three `MARKET_FORECAST` records written to `15_predictions.json`.

## Outstanding Blockers

1. **`Fund_Z` / `Sent_Z` universe-scale promotion (Phase 2)** — the single blocker standing between this system and any `GO`. Unchanged.
2. **Rank IC ≤ 0** — confidence capped at `MEDIUM` system-wide until a corrective change passes evolution policy. Two candidate corrections were tested and rejected this run; see `13_evolution_log.md`.
3. **No same-model baseline for `claude-opus-5`** — resolves naturally once this model has a folder ≥21 days old.
