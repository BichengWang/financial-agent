# 08 — Risk Review — 2026-08-01

Adversarial review by the risk committee before publication.

## Decision: **APPROVE the `NO_TRADE` publication**

No portfolio is proposed, so there is nothing to size-check. The committee's job here is to
verify that the package is honest, fully grounded, and that `NO_TRADE` is reached for the
*stated* reason. It is. **Zero revision passes were requested** (budget 1 of 1 unused).

## Top three concerns, in severity order

**1 — `Tech_Z` double-counts momentum (new, material, now measured).**
`relative_strength` is `momentum − benchmark_momentum`, a constant shift, so `z(rs20)` and
`z(mom20)` are numerically identical to
4e-16. Four of `Tech_Z`'s eight slots are therefore two
signals counted twice, giving momentum 33.3% of live composite weight instead
of 16.7%. The committee judged this **not** grounds to block publication,
because (a) the run is `NO_TRADE` regardless, so no capital is at risk, and (b) changing the
engine mid-series would break comparability with the ranked history without benefit. It is
logged as an accepted Track B fix in `13`, effective next run, with measured impact. The
committee explicitly required that `05` disclose the defect next to the scores it affects —
it does.

**2 — The `MARKET_FORECAST` block is publishing forecasts it knows are miscalibrated.**
Canonical hit rate 20.27% over n=78, mean z -0.6633. SOXX's
formula mu of +7.34% exceeds the maximum equity mu the
calibration table can issue, for an ETF below both moving averages. The ±1.5pp adjustment
band is applied at full bearish extent and remains far too narrow. The committee accepts
publication **only** because the alternative — withholding the records — would make the
error unmeasurable, and because `03` states the defect plainly rather than presenting the
number as a view. The fix is Track A and blocked by `eff_n` = 1.

**3 — All 439 settled records still represent one overlapping 28-day window.**
`eff_n` = 1. Raw `n` is large enough to look authoritative and is not. Every
calibration statement in this package is explicitly qualified by that, and no Track A change
was proposed.

## Review checklist

| # | Check | Finding |
|---|---|---|
| 1 | Fabricated or weakly supported inputs | **None.** 77/77 prices on 3 independent sources; 0 `ILLUSTRATIVE` rows |
| 2 | Overfitting / unvalidated signal claims | **None.** No Track A change proposed; the one accepted change is a defect fix with measured impact |
| 3 | Excessive event concentration | 1 of 24 published names inside 14d of earnings — below the >2 `NO_TRADE` trigger; universe-level concentration (153/515) disclosed in `03` |
| 4 | Correlation / sector crowding | Naive sleeve correlation 0.1282 PASS; Health Care 35.0% **breaches** the 30% cap — disclosed in `07`, contributes to `NO_TRADE` |
| 5 | Portfolio beta drift | Naive sleeve beta +0.4608, **below** the 0.90 floor — disclosed, not hidden |
| 6 | Thesis quality below stated confidence | Confidence capped `MEDIUM` universally by the rank-IC binding; theses labelled `INFERRED` |
| 7 | Report vs shared-rules mismatch | None found |
| 8 | Price/derived-field citation violations | **None.** Every numeric `entry_price` carries `price_date` + `price_tag`; no target/CI is populated on an unverified price |
| 9 | Sigma violations | **None.** Every ranked name and all 3 ETFs carry `REALIZED_VOL_30D` with a stated source; no blanket `sigma = UNAVAILABLE` |
| 10 | Score-attribution violations | **None.** All 24 published names carry family z-scores, DQ, penalties, drivers and metric ledger rows; `Fund_Z`/`Sent_Z` reported `UNAVAILABLE`, never neutral |
| 11 | Source Ledger violations | **None.** Every price, indicator, risk metric, earnings date and sizing input has a row or an explicit `UNAVAILABLE` row |
| 12 | Live-sounding / stale-as-current claims | **None.** 2026-08-01 is a Saturday and every artifact says the basis is the 2026-07-31 close |
| 13 | Improper GO-blocking | **None.** All 5 Required inputs grounded; Enhancing gaps listed separately as caps. `NO_TRADE` is driven by evidence thresholds, not by Enhancing inputs |
| 14 | Missing prediction records | **None.** 24 `EQUITY_ALPHA` (all with `score_explainability`) + 3 `MARKET_FORECAST` + 107 settlements |
| 15 | Technical indicator pack violations | **None.** All states trace to `technical_indicators.json`; TD-9 `9` and RSI extremes used as exhaustion flags only, never standalone signals |

## Lineage checks performed

- **Price/target lineage** — 77 names re-read from 3 vendors; max deviation
  0.0661% against a 1% tolerance;
  0 confirmation re-reads needed.
- **Sigma lineage** — every sigma is the 30d realized vol of adjusted-close daily returns
  scaled √21, recomputed from `L-HIST`.
- **Score attribution** — `Adj Score` re-derived from stored family z-scores for all
  24 published names in the verification pass (see below).
- **Kelly handling** — `0.25 × Kelly` is reported for every ranked name. Because no name is
  investable, the `< 2% NAV` penalty and `≥ 5% NAV` cap-binding rules are moot this run and
  were not applied cosmetically.
- **Technical indicator interpretation** — TD-9 setup `9` and RSI ≥ 70 appear on several
  published names and are treated as exhaustion/reversal flags affecting confidence only.
- **Prediction-record completeness** — verified programmatically; see `09`.

## Publication recommendation

**`NO_TRADE`.** Inputs are valid and fully grounded; no candidate set meets the quality bar.
The committee specifically rejects characterising this as a data-availability failure at the
*run* level — every Required input was obtained. It is a **capability gap**: two of four
factor families have no fetch path, and until Phase 2 of the fundamentals/sentiment plan
lands, every run will reach this same conclusion regardless of market conditions.
