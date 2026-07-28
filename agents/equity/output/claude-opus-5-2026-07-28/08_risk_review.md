# 08 Risk Review — 2026-07-28

Adversarial review of the package before publication.

## Decision: **APPROVE for publication as `NO_TRADE`**

The committee approves publishing this package. It does **not** approve any position — there is nothing
to approve, and that is the correct outcome on this evidence.

## Top Three Concerns, in severity order

**1. The forecast score has a negative rank IC and we are still publishing forecasts from it.**
Weighted-mean rank IC is -0.1715 over 260 settled records. The score is not merely uninformative —
its ordering is *inverted*, meaning the names it likes most have tended to do worst in relative terms.
Confidence is capped at `MEDIUM` universe-wide as the rules require, but a cap on a label does not fix an
inverted ranking. The mitigation that matters is that **nothing is sized**: these are settleable paper
forecasts whose only job is to accumulate the evidence that will eventually justify a correction. The
committee accepts that, and flags that continuing to publish an inverted ranking beyond the point where
`eff_n` permits a fix would not be acceptable.

**2. The `MARKET_FORECAST` block is knowingly wrong and published anyway.**
20.83% hit rate over n=48; all 6
of today's ETF settlements were MISS. SOXX carries the block's *most bullish* mu (+1.82%)
while sitting -21.19% below its 60-day high with rising vol. The committee
examined whether to override it discretionarily and **declined**: the ±1.5pp band cannot reach a bearish
value from a beta of 3.6474, the table is evolution-agent property, and
Track A is gated at `eff_n = 1`. Publishing it transparently with the defect stated at the point
of use (`03`) preserves the settlement evidence; silently patching it would destroy it. **Condition: the
defect must be restated wherever the forecast is consumed** — verified present in `03`, `09` and `13`.

**3. The beta-infeasibility finding is knife-edge and must not be presented as structural.**
Max attainable beta 0.899853 misses the floor by 1.47 bp.
Earlier packages reported comfortable misses (+0.114 on 07-24, 0.8519 on 07-27); today's is inside
estimation noise. The committee **required** `00`, `07` and `09` to label it corroborating rather than
load-bearing, and to name the evidence thresholds as the binding reason. Verified.

## Review Checklist

| # | Check | Finding |
|---|---|---|
| 1 | Fabricated or weakly supported inputs | **None.** Every downstream fact traces to an L-row; 28/28 prices two-source grounded |
| 2 | Overfitting / unvalidated signal claims | **None accepted.** No Track A change proposed; `eff_n` gate respected |
| 3 | Excessive event concentration | **Breach recorded** — 3 published names report inside 14d (limit 2); an independent `NO_TRADE` ground, disclosed in `03` and `06` |
| 4 | Correlation / sector crowding | Pass — avg pairwise 0.1931 < 0.45; max sector 33.3% < 30% |
| 5 | Portfolio beta drift | Beta floor unreachable — see concern 3; no portfolio published |
| 6 | Thesis quality below stated confidence | Pass — no `HIGH` anywhere; earnings names capped `LOW` |
| 7 | Report vs shared rules mismatch | None found |
| 8 | Price / derived-field citation violations | **None.** Every `entry_price` carries `price_date` + `price_tag`; no target or CI is populated on an unverified price |
| 9 | Sigma violations | **None.** Every ranked name and ETF carries `REALIZED_VOL_30D` with a stated source; zero blanket `UNAVAILABLE` |
| 10 | Score-attribution violations | **None.** Every `Adj Score` shows family z-scores, DQ, penalties, drivers and metric rows; `Fund_Z`/`Sent_Z` labelled `UNAVAILABLE`, never neutral |
| 11 | Source Ledger violations | **None.** 55 rows cover every price, return, vol, beta, earnings date, target, CI, drawdown, ratio, indicator and sizing input |
| 12 | Live-sounding / stale-as-current claims | **None.** Basis is stated as the 2026-07-27 completed close throughout; no "current"/"latest" without a ledger row |
| 13 | Improper `GO`-blocking | **None.** All 5 Required inputs grounded; the 6 missing Enhancing inputs are listed only as confidence/exposure caps |
| 14 | Missing prediction records | **None.** 24 `EQUITY_ALPHA` (all with `score_explainability`) + 3 `MARKET_FORECAST` + 35 settlements in `15` |
| 15 | Technical indicator pack violations | **None.** Every state cites `technical_indicators.json`; TD-9/RSI treated as exhaustion flags, never standalone signals; zero hidden script failures |

## Specific Lineage Audits

**Price and target lineage.** Entry prices are the 2026-07-27 unadjusted closes (L002), corroborated by
Nasdaq to the cent on 28/28 symbols (max difference
0.000000%) and by CNBC on 27/28. The single CNBC
disagreement — PAYX, 1.030% — was **investigated rather than waived**: CNBC reports the
dividend-adjusted prior close (114.29, matching stockanalysis's `a` field exactly) while Nasdaq and
stockanalysis's `c` field report the actual close of 115.48. Three of 519 symbols carry an ex-date on
2026-07-28. Entry uses the unadjusted value per the 2026-07-26 basis rule. **The committee treats a
cross-vendor gap that resolves to a known corporate action as grounded, and one that does not as
`UNAVAILABLE`.** Two transient Nasdaq misreads (DGX, PM) were caught by a confirmation pass and the
serial re-reads matched to the cent; the discarded first reads are retained in `price_verification.json`.

**Sigma lineage.** Every sigma is `REALIZED_VOL_30D` from L013 — stdev of the last 30 adjusted daily
returns × √21. Sortino uses a genuinely distinct downside deviation (L014), not the same sigma; the
committee re-verified this, since it was a real bug on 2026-07-17 and 2026-07-20.

**Score attribution.** Recomputed independently for all 24 published names from the family z-scores
in `run_computed_manifest.json`; every `Adj Score` reproduces its stated trace exactly.

**Settlement completeness.** 35 settled, 0 conflicts, due
inventory 0 after the run. All used `TARGET_EQ_RUN_DATE` at the 2026-07-27 close,
correct for a pre-open fire on the target date.

## Final Publication Recommendation

**`NO_TRADE`.** Inputs are valid, complete against every Required gate, and fully grounded; the candidate
set does not meet the quality bar. Three independent grounds each suffice: evidence thresholds #2 and #4
(the binding ones), event concentration (3 names inside 14 days vs a limit of
2), and portfolio beta infeasibility (marginal, corroborating only).
