# 08 Risk Review — Committee Decision

Adversarial review of the 2026-07-04 weekend package (23 monitoring forecasts + 3 core ETF forecasts, proposed status REVIEW_ONLY).

## Checklist Findings

1. **Fabricated/weak inputs** — none. All prices are official 2026-07-02 closes, DELAYED-tagged with observation date, verified Yahoo-vs-Nasdaq at 0.000% divergence for all 26 published names. IBKR's closed-market snapshots (2026-07-01 prior-session closes, `is_close: true`) were used only as prior-record verification and are labeled as such — the 07-03 finding reproduced, no conflation with today's entries.
2. **Overfitting/unvalidated signals** — momentum/risk-only scoring disclosed everywhere; unchanged standing concern. The family-member set for Tech_Z/Macro_Z is disclosed in the 01 header; it differs in composition from no prior run's disclosure (07-03 did not enumerate members) — flagged to evolution as a documentation-consistency item, not a violation.
3. **Event concentration** — 0 published names inside 14d earnings (18 shortlist names penalized out, incl. yesterday's #5 LII and #8 URI on the one-day window roll); weekend gap risk on 2026-07-02 entries noted; FOMC (7/28-29) precedes the 2026-08-01 target by three sessions; DOC/WST/KDP report 7/24, one day past the buffered window — acceptable but tight.
4. **Correlation/sector crowding** — Health Care 9/23 published names (39%); top-12 equal-weight HC share 42% would bind the 30% cap; DVA|DOC 0.73 and MAS|SWK 0.64 pairwise correlations flagged; average low (0.170).
5. **Beta drift** — no portfolio; pre-check exhibit max NAV beta 0.71 < 0.90 floor, diagnostic-only.
6. **Thesis quality vs confidence** — LOW everywhere; MRNA again the highest standalone risk (22.5% sigma, -0.10 penalties), acceptable as forecast-only.
7. **Rules mismatches** — none found this run. The ±2pp mu clamp holds across the sleeve (max applied adjustment -1pp).
8. **Price/derived-field citations** — complete; entries carry price_date 2026-07-02 + DELAYED tags; targets/CIs derive from tagged entries.
9. **Sigma** — REALIZED_VOL_30D on all 26 records.
10. **Score attribution** — full traces, DQ 0.80, penalties, drivers, ledger rows; UNAVAILABLE families never supportive; positive drivers limited to sourceable technical/risk metrics.
11. **Source Ledger** — 208 rows; derived rows cite formulas/inputs; ^IRX staleness (3.663% @ 2026-06-26) tagged HISTORICAL with the lag explained rather than passed off as fresh.
12. **Live-sounding claims** — none; the package consistently says "last completed session" / "Thursday's close" and labels today a closed Saturday.
13. **GO-blocking discipline** — correct; weekend rule (not Enhancing gaps) sets REVIEW_ONLY; family-gate would-be-NO_TRADE stated separately.
14. **Prediction records** — all 23 ranked names + 3 ETFs present with benchmark_price 744.78 and full score_explainability; UNH not ranked (DOWNGRADE, documented), so no record owed. The committee verified the QQQ/SOXX mu records now reproduce from the stated beta x prior derivation, unlike the 07-03 vintage (discrepancy disclosed in 02/03/13 rather than silently corrected).
15. **Technical indicator lineage** — all values cite technical_indicators.json (517 OK, 2026-07-04T18:28:29Z) computed via --history-dir on the same fetched bars; TD9/RSI as flags only.

## Top Three Concerns (severity order)

1. **Third consecutive vintage of overlapping forecasts on the same entry tape** (07-02 closes for the 07-03 and 07-04 runs; 19-name overlap with 07-03's sleeve): settlements will be strongly correlated observations and must not be read as independent calibration evidence (noted for the evolution agent).
2. **Weekend-vintage forecasts carry gap risk**: entries are Thursday closes; the first session that can move them is Monday 7/6, and this vintage's 28d window embeds the earnings season, FOMC, and a Saturday target date (2026-08-01, first settleable session 2026-08-03).
3. **Two-family scoring** (standing): unresolved pending the HUMAN_REVIEW decision on the Track B proposal — now four consecutive flags.

## Decision

**APPROVE** publication as **REVIEW_ONLY**. Data integrity clean; weekend handling correctly reasoned and disclosed; prior-vintage mu-reproduction issue surfaced transparently. Publication recommendation: REVIEW_ONLY.
