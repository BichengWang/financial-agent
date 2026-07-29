# 08 Risk Review — 2026-07-29

Adversarial review of the proposed output before publication.

## Decision: **APPROVE** for publication as **`NO_TRADE`**

There is no portfolio to approve or reject. What is reviewed here is whether the `NO_TRADE` call is
honest, whether the 24 published monitoring forecasts are properly grounded and settleable, and
whether any fabricated or mislabeled value propagated.

## Top Three Concerns (severity order)

### 1. The earnings-grounding defect found mid-run — **resolved, but it nearly shipped**

Six names (ADP, AON, AWK, FICO, HUM, VRSK) were scored **penalty-free while reporting the same day**,
and two of them ranked in the pre-regrounding top 8. Had the run published on the retired heuristic,
it would have carried names through an earnings print with no `−0.10` penalty and `MEDIUM` rather than
`LOW` confidence — a direct violation of `rules.md § Risk Controls`.

It was caught because the vendor-empty rate (27 of 59) looked implausible for late July and was probed
against an independent source rather than accepted. The committee's finding: **the fix is correct and
strictly strengthens grounding** — it replaces an *inference* about a past price move with a *positive
observation* from a forward calendar, cross-validated
25/25
against the endpoint it replaces. No protected rule or grounding gate is weakened. Approved.

The residual concern is process, not output: a heuristic that infers a *future* date from a *past*
price move was load-bearing for three consecutive published packages (2026-07-26, -27, -28). Those
packages should be regarded as carrying an unquantified earnings-penalty error. This is logged in `13`.

### 2. Concentration and correlation of the monitoring sleeve are not risk-managed

19 of 24 published names carry negative beta and 8 of 24
sit in Industrials. If these were positions, the 0.90–1.10
beta band and the 30% sector cap would both bind hard. They are **not** positions, and no correlation
matrix was computed (`07`). The committee accepts this for a `NO_TRADE` run but flags explicitly:
**the monitoring sleeve is not a shadow portfolio and must not be read as one.** It is a set of
24 independently-settleable forecasts that happen to share a regime thesis.

### 3. `MARKET_FORECAST` records are published knowing the mu rule is wrong

`03` assigns SOXX the largest positive mu (+1.8241%) precisely because it is the
most beaten-down, highest-beta member of the sleeve. The rule has produced a
18.52% direction rate over n=54, and all 6 settled this run missed.
Publishing a forecast believed to be miscalibrated is defensible **only** because the correction is
Track A, gated at `eff_n = 1` until 2026-08-09, and
hand-overriding a protected calibration table outside the evolution policy is itself a violation. The
committee requires — and confirms — that the defect is disclosed at the point of use in `03`, not
buried. Approved on that basis.

## Review Checklist

| # | Check | Finding |
|---|---|---|
| 1 | Fabricated or weakly supported inputs | **None.** 28/28 entry prices exact to the cent across 3–4 independent sources (L011, L012) |
| 2 | Overfitting / unvalidated signal claims | None. No parameter was tuned this run; Track A is gated at `eff_n=1` |
| 3 | Excessive event concentration | 272 of 514 universe names print inside 14 days, but only 1 of 24 published (ADP, penalised, `LOW`) |
| 4 | Correlation / sector crowding | Present and **disclosed** (concern 2). Not risk-managed because there is no portfolio |
| 5 | Portfolio beta drift | N/A — no portfolio. Attainable range computed pre-sizing (L045) |
| 6 | Thesis quality below stated confidence | No. Every published name is `MEDIUM` or `LOW`; rank IC -0.2064 caps `HIGH` universe-wide |
| 7 | Report/rules mismatch | None found |
| 8 | Price/derived-field citation violations | None. Every `entry_price` carries `price_date` + `price_tag`; no target or CI is populated on an unverified price |
| 9 | Sigma violations | None. All 24 carry `REALIZED_VOL_30D` (L013); no blanket `UNAVAILABLE`, no round unsourced sigma |
| 10 | Score-attribution violations | None. Every name has family z-scores, DQ, penalties, drivers, ledger rows. `Fund_Z`/`Sent_Z` shown as `UNAVAILABLE`, never neutral |
| 11 | Source Ledger violations | None. 51 rows; every downstream numeric traces to one |
| 12 | Live-sounding / stale-as-current claims | None. The 2026-07-28 basis is stated explicitly wherever prices appear |
| 13 | Improper GO-blocking | **None — verified.** All 5 Required inputs grounded. The Enhancing gaps (L036, L046-L048) are cited only as DQ/confidence caps. `NO_TRADE` is composition-driven |
| 14 | Missing prediction records | None. 24 `EQUITY_ALPHA` (all with `score_explainability`) + 3 `MARKET_FORECAST` + 44 settlements |
| 15 | Technical indicator pack violations | None. All states cite `technical_indicators.json` (L021); TD-9 and RSI used as exhaustion flags with a confirming condition, never standalone |

## Specific Verifications Performed

- **Price lineage.** Re-read 28 symbols against CNBC and Nasdaq independently of the primary
  fetch: 28/28 exact. Core ETFs additionally reconciled against IBKR via `last − change`
  (prior-close empty pre-market) — exact on all three.
- **Sigma lineage.** Every `sigma` equals the name's 30-day realized vol from adjusted closes, scaled
  `sqrt(21)`. Sortino uses **downside** deviation, not total sigma — the bug fixed 2026-07-21 has not
  regressed (spot-checked: Sortino != Sharpe for all 24 names).
- **Score attribution.** `Adj Score` re-derived independently from `composite_z × DQ − penalties` for
  all 514 names; zero mismatches.
- **Target/CI arithmetic.** `target = entry × (1+mu)` and `CI = entry × (1+mu±1.04σ)` re-derived for
  all 24 published rows; zero mismatches.
- **Settlement timing.** All 44 settlements carry `TARGET_EQ_RUN_DATE` with a
  2026-07-28 settle date. The canonical normalizer re-validated every historical candidate and reports
  due inventory 0, conflicts 0.
- **Prediction-record completeness.** Every published name appears in `15_predictions.json` with
  `benchmark_price` present and non-null, `score_explainability` present, no `HIGH` confidence, and no
  zero sigma.

## Required Fixes

None outstanding. The earnings-grounding defect was fixed before publication and the affected names
re-ranked.

## Final Publication Recommendation

**`NO_TRADE`.** Inputs are valid and fully grounded; the candidate set does not meet the quality bar.
Publishing 24 settleable monitoring forecasts alongside it is the correct behaviour — it is how
the system accumulates the evidence needed to ever publish `GO`.
