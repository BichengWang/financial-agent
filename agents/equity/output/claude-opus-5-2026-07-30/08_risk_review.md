# 08 — Risk Review — 2026-07-30

**Committee decision: `APPROVE` for publication as `NO_TRADE`.**

No revision pass was requested or consumed. The package is internally consistent, fully
lineage-backed, and reaches the correct status. Approval covers *publication*, not the quality
of the underlying signal — which the committee judges poor and says so below.

## Checklist

| # | Check | Finding |
|---|---|---|
| 1 | Fabricated or weakly supported inputs | **None.** Every price two-source verified; core ETFs three-source. No estimated field anywhere; BF-B's missing market cap is `UNAVAILABLE`, not imputed. |
| 2 | Overfitting / unvalidated signal claims | **None introduced.** No parameter was tuned this run. The Track A calibration proposal is `DEFERRED` on `eff_n`=1, not quietly adopted. |
| 3 | Excessive event concentration | 2 published name(s) with earnings ≤14d, each penalised −0.10 and capped `LOW`. Below the >2-name `NO_TRADE` trigger. Broad market shows heavy clustering 2026-08-05/06 — flagged in `03`. |
| 4 | Correlation / sector crowding | Avg pairwise correlation 0.1559 < 0.45; max sector 25.0% < 30%. Both pass. |
| 5 | Portfolio beta drift | No portfolio. Feasibility **re-verified this run**: max attainable beta +1.1258 — the band is feasible, unlike 2026-07-27. The committee specifically checked that the prior "provably infeasible" language was not carried over. |
| 6 | Thesis quality vs stated confidence | Confidence capped `MEDIUM` universe-wide by the rank-IC binding, `LOW` where earnings ≤14d. No `HIGH` anywhere. Given rank IC -0.1975, even `MEDIUM` is generous; it is the cap the rules specify. |
| 7 | Report ↔ rules mismatch | None found. |
| 8 | Price / derived-field citation | Every numeric `entry_price` carries `price_date` 2026-07-29 + `price_tag` HISTORICAL. No target or CI is populated on an unverified price. |
| 9 | Sigma violations | Zero. All 24 records carry `sigma` from `REALIZED_VOL_30D`; no blanket `UNAVAILABLE`; no round-number sigma. |
| 10 | Score attribution | Every ranked name discloses family z-scores, DQ, penalties, drivers and ledger rows. `Fund_Z`/`Sent_Z` are shown as `UNAVAILABLE` and contribute `0.00` — **never** presented as neutral or supportive. |
| 11 | Source Ledger completeness | Every downstream price, vol, beta, earnings date, target, CI, drawdown, ratio and indicator state has a row in `01`. |
| 12 | Live-sounding / stale-as-current claims | Basis data is described as the 2026-07-29 close throughout. 2026-07-30 intraday quotes appear only in `10`, explicitly labelled live observation. |
| 13 | Improper GO-blocking | **Verified clean.** All five Required inputs are grounded; the missing Enhancing inputs are recorded as confidence/exposure caps only. `GO` is blocked by Evidence Thresholds 2/3/4 — a legitimate basis — not by any Enhancing gap. |
| 14 | Missing prediction records | `15_predictions.json` present: 24 `EQUITY_ALPHA` (all with `score_explainability`) + 3 `MARKET_FORECAST` + 58 settlements. Core ETF block complete. |
| 15 | Technical indicator pack | All states trace to `technical_indicators.json`. TD-9/RSI/MACD used as exhaustion/confirmation inputs only. No script failure was hidden. |

## Top three concerns (severity order)

### 1. The composite score is rank-inverted, and today's tape is demonstrating it live

Weighted-mean rank IC is **-0.1975** across n=347 settled predictions, with
19 of
23 vintages ≤ 0. This is not a magnitude problem —
CI coverage 72.05% and mean z -0.3419 are both healthy.

While this run was executing, the 2026-07-30 session delivered an unusually direct test. As of
2026-07-30T10:26:18-04:00, **21 of 24** published names were **down**, averaging
**-3.47%**, while SPY was +1.17% and SOXX
**+8.67%**. Worst: FICO -15.74%, HPQ -6.72%, VRSK -6.48%, PAYX -6.20%, BRO -5.77%.

The committee's reading: `Tech_Z` is a trend-persistence signal carrying
66.7% of live weight, so the leaderboard is mechanically the *previous* 60 days'
winners. When leadership rotates, the ranking is not merely uninformative — it is
anti-correlated. **This does not change the status** (already `NO_TRADE`) and the committee
explicitly declines to alter any score or `mu` on one session's evidence. It is recorded as the
strongest available support for the `13` diagnosis.

### 2. FICO carries a −15.7% intraday move against a grounded but now-unrepresentative entry

FICO is published at rank 9 with entry 1373.08 (2026-07-29
close, two-source verified). It is trading -15.74% as of
2026-07-30T10:26:18-04:00. The committee checked whether an unflagged earnings print explains it:
FICO is **absent from all 27 swept calendar days** and the per-name
Nasdaq endpoint returns vendor-empty, so no source supports an earnings explanation and none is
asserted. The entry price remains correct and auditable for settlement; the forward
distribution is plainly no longer centred where `mu` assumes. Disclosed here and in `10`;
**not** retro-fitted into the score, which would be curve-fitting to intraday news.

### 3. `MARKET_FORECAST` remains structurally mis-specified

Direction accuracy **16.4%** over n=63. All 9 core-ETF
forecasts settled this run were `MISS` or `FLAT_CALL` — none was a hit. The root cause
(`mu = beta x SPY_mu`) was diagnosed 2026-07-24 and is unfixed because the fix is Track A and
`eff_n`=1 < 3 (rises 2026-08-09). Publishing a
forecast known to be biased is the lesser evil versus suppressing the block the rules require;
the bias is disclosed at the point of use in `03`.

## Required fixes

**None blocking.** No fabrication, no lineage gap, no mislabelled field, no missing record.

## Final publication recommendation

**`NO_TRADE`** — inputs valid and fully grounded; no candidate set meets the quality bar.
Not `REVIEW_ONLY` (data is same-session fresh, not stale), not `HALTED` (no integrity failure).
