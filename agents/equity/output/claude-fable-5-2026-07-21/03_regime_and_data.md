# 03 Regime and Data — 2026-07-21 (claude-fable-5)

## Data Mode Declaration

**DELAYED.** All prices are the 2026-07-20 official session closes fetched this run: Yahoo v8 chart API bulk fetch, 521/521 symbols (515-name index-union + SPY/QQQ/SOXX/TLT/^VIX/^IRX), 8-worker threaded, ~37 seconds wall time, zero failures on the first pass (two per-symbol repairs applied before scoring: `SATS`→refetched under its renamed ticker `ECHO`; `L` refetched after a transient empty-CSV race — see `01` L007-L009). This is a session-over-session change: Yahoo had been 429-blocked for the five prior sessions (2026-07-13 through 07-20), forcing a Nasdaq-bulk-primary path; this run's probe and full bulk fetch both succeeded cleanly, so Yahoo is treated as primary again pending confirmation it holds tomorrow. VIX and the risk-free proxy (^IRX) came from the same Yahoo fetch (L011-L012). All five Required inputs grounded (L001-L010); no ILLUSTRATIVE content. The run fired while the market was open (~15:10-15:30 ET); the partial 2026-07-21 intraday bar was fetched then trimmed from all 521 series before any computation, so entry prices and analytics use the last **completed** close only.

## Regime Classification: NEUTRAL — with HIGH_VOL watch (unchanged from 07-17/07-20)

| Evidence | Value | Ledger |
|---|---|---|
| SPY vs MAs | 742.09 below MA20 744.79 and MA50 744.55 (−0.36%/−0.33%) | L014-L016 |
| VIX | 18.65 (< 20 watch trigger); 20d mean 17.12 | L012-L013 |
| Breadth | 60.5% of eligible universe (311/514) above own MA50 — still constructive | L020 |
| Vol regime | SPY 30d rvol (1m) 4.52% vs 2.68% prior window — rising | L017-L018 |
| Leadership | Financials/insurers/transports/staples dominate the cross-section (see `05`); semis remain in a ~20% drawdown from the 60d high | 05 leaderboard |

The HIGH_VOL trigger (VIX > 20 while SPY holds below both MAs) has not fired. Breadth above 55% and the absence of a sustained SPY drawdown argue against BEAR. NEUTRAL stands, consistent with every session since 2026-07-17 — this is now a four-session-old regime call, not a fresh read.

## Core ETF Market Forecast Block

mu derivation: SPY = NEUTRAL regime prior +0.50% (unadjusted). QQQ = beta 1.732 × 0.50% = +0.87% raw, adjusted −0.50pp (within the ±1.5pp band) on continued deteriorating relative strength — 20d QQQ/SPY −5.40% (L021-L022), price below both MAs, rvol roughly double the SPY level. SOXX = beta 3.733 × 0.50% = +1.87% raw, adjusted −1.50pp (band limit) on 20d SOXX/SPY −17.41%, 60d-high drawdown −19.98%, rvol 22.0%. Betas are 60d fetched-return regressions (`DERIVED`, cite L021-L023); both adjustments repeat the identical direction and magnitude the 07-20 run applied — the semis/growth underperformance versus the broad market has not resolved in one session.

| ETF | Entry Price | Price Date | Price Tag | Trend (20d/50d) | 30d RVol | Beta vs SPY | mu | sigma | Sigma Source | Target Price | Target Date | 70% CI Lo | 70% CI Hi | Confidence | Ledger Rows |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SPY | 742.09 | 2026-07-20 | DELAYED | below MA20 744.79, below MA50 744.55 | 4.52% | 1.000 | +0.50% | 4.52% | REALIZED_VOL_30D | 745.80 | 2026-08-18 | 710.90 | 780.71 | MEDIUM | L014,L017 |
| QQQ | 696.06 | 2026-07-20 | DELAYED | below MA20 716.12, below MA50 719.01 | 8.87% | 1.732 | +0.37% | 8.87% | REALIZED_VOL_30D | 698.61 | 2026-08-18 | 634.38 | 762.83 | LOW | L021,L022 |
| SOXX | 524.14 | 2026-07-20 | DELAYED | below MA20 580.38, below MA50 566.72 | 22.00% | 3.733 | +0.37% | 22.00% | REALIZED_VOL_30D | 526.06 | 2026-08-18 | 406.13 | 646.00 | LOW | L023,L024 |

Relative strength: QQQ/SPY 20d −5.40% / 60d +1.91%; SOXX/SPY 20d −17.41% / 60d +17.05% (L021,L023) — the 60d ratios still carry the spring melt-up; the 20d ratios say growth/semis leadership remains broken through July. Regime-consistency check: a NEUTRAL call with defensives/financials leading and the highest-beta sleeve still ~20% off its 60d high is internally consistent; the forecast block's positive-but-shrunk mus reflect the regime prior, not conviction (SPY MEDIUM, QQQ/SOXX LOW, unchanged confidence pattern from 07-20).

## Event Concentration Flags

- **Earnings cluster:** of the top-20 published names, 5 sit inside the buffered 14-19 day window (`ADP` 8d, `EG` 8d, `UNP` 2d, `DOC` 14d, `PSX` 15d/estimated-buffered). NO_TRADE downgrade trigger #4 (> 2 names in-window) independently binds any portfolio drawn from this leaderboard.
- **Vendor-empty cluster:** 14 of the top-60 shortlist returned no forward date from the Nasdaq vendor ("hasn't provided us with the upcoming earnings report date") — predominantly financials/insurers (TRV, SCHW, MTB, BAC, STT, USB, RF, WRB, EFX, ABT, DHR, PAYX, CTAS, MRSH) that most plausibly already printed in the mid-July window; carried as `ESTIMATED post-print cadence (±5d)` at +91 days (≈2026-10-16), which places them outside any earnings penalty window this run.
- **FOMC:** late-July meeting (~2026-07-28/29, structural cadence) sits inside every target horizon.

## Universe Handoff

`build_index_universe.py`: 515-name union (503 S&P 500 + 101 Nasdaq-100, 89 overlap; caches fetched 2026-06-21 — stale-cache rule applied, refresh is maintenance not fallback) → `universe_summary.json` (L001-L004). Eligible after filters: **514** (price > $5, ADV20 > $20M, ≥ 60 bars; FDXF excluded at insufficient history — L006). Full list + SPY/QQQ/SOXX handed to `technical_indicators.py` (517/518 OK). Percentile label: `INDEX_UNION_PCTL (n=514)`.

## Ledger Coverage Gaps Affecting Scoring

Fund_Z and Sent_Z are UNAVAILABLE universe-wide for scoring (L030) — SHADOW diagnostics ran clean on today's top-20 shortlist (100% sourceable both families, `fundamental_diagnostics.json` / `sentiment_diagnostics.json`) but remain unpromoted: coverage is 20/514 names (~3.9% of the eligible universe), far under the 70%-universe-sourceability bar `rules.md § Financial Metrics and Score Attribution` requires before any metric may contribute to `Adj Score`. Effect: DQ 0.80, max 2 of 4 families sourceable, evidence threshold #2 unsatisfiable → structural NO_TRADE gate (16th consecutive scoring run since the gate was first identified). GICS sector labels are not carried in the constituent caches; sector references downstream are `INFERRED` and no sector cap is exercised (no portfolio is drafted). Handoff to Factor Scoring: proceed, full metric pack, calibration feedback from `02 §0` binds (rank IC ≤ 0 → MEDIUM cap, structurally moot since LOW already binds).
