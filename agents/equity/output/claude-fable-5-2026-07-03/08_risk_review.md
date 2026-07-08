# 08 Risk Review — Committee Decision

Adversarial review of the 2026-07-03 holiday package (23 monitoring forecasts + 3 core ETF forecasts, proposed status REVIEW_ONLY).

## Checklist Findings

1. **Fabricated/weak inputs** — none. All prices are official 2026-07-02 closes, DELAYED-tagged with observation date, verified Yahoo-vs-Nasdaq at 0.000% divergence for all 26 published names. The committee specifically reviewed the holiday data-mode decision: declaring DELAYED on fetched real closes rather than the runbook's ILLUSTRATIVE prescription is the anti-fabrication-correct choice; deviation disclosed in 00/01/03/13. IBKR's closed-market snapshots (prior-session closes) were used only as prior-record verification and are labeled as such — no conflation with today's entries.
2. **Overfitting/unvalidated signals** — momentum/risk-only scoring disclosed everywhere; unchanged standing concern.
3. **Event concentration** — 0 published names inside 14d earnings (14 shortlist names penalized out, PPG and GPC newly rolled in); weekend gap risk on 07-02 entries noted; FOMC (7/28-29) precedes the 7/31 target by two sessions.
4. **Correlation/sector crowding** — Health Care 8/23; DOC|DVA 0.73 and LII|SWK 0.71 pairwise correlations flagged; averages low (0.132).
5. **Beta drift** — no portfolio; pre-check exhibit max NAV beta 0.69 < 0.90 floor, diagnostic-only.
6. **Thesis quality vs confidence** — LOW everywhere; MRNA again the highest standalone risk (22.5% sigma, −0.10 penalties), acceptable as forecast-only.
7. **Rules mismatches** — none found this run; the ±2pp mu clamp (added 07-02) held: UNH would clamp to 0.0% and is correctly excluded via the reflection DOWNGRADE rather than published at a degenerate mu.
8. **Price/derived-field citations** — complete; entries carry price_date 2026-07-02 + DELAYED tags; targets/CIs derive from tagged entries.
9. **Sigma** — REALIZED_VOL_30D on all 26 records.
10. **Score attribution** — full traces, DQ 0.80, penalties, drivers, ledger rows; UNAVAILABLE families never supportive.
11. **Source Ledger** — 208 rows; derived rows cite formulas/inputs; ^IRX staleness (3.663% @ 06-26) tagged HISTORICAL with the lag explained rather than passed off as fresh.
12. **Live-sounding claims** — none; the package consistently says "last completed session" / "Thursday's close."
13. **GO-blocking discipline** — correct; holiday rule (not Enhancing gaps) sets REVIEW_ONLY; family-gate would-be-NO_TRADE stated separately.
14. **Prediction records** — all 23 ranked names + 3 ETFs present with benchmark_price 744.78 and explainability; UNH not ranked (DOWNGRADE, documented), so no record owed.
15. **Technical indicator lineage** — all values cite technical_indicators.json (517 OK); final-session bars, no partial-bar caveats; TD9/RSI as flags only.

## Top Three Concerns (severity order)

1. **Holiday-vintage forecasts carry weekend gap risk**: entries are Thursday closes; the first session that can move them is Monday 7/6, and this vintage's 28d window embeds both the earnings season and FOMC. Correctly REVIEW_ONLY; CI calibration will be informative.
2. **Two consecutive publications of largely overlapping sleeves** (07-02 intraday entries, 07-03 close entries — 19/23 name overlap): settlement will produce correlated observations; the calibration metrics should be read with that dependence in mind (noted for the evolution agent).
3. **Two-family scoring** (standing): unresolved pending the HUMAN_REVIEW decision on the Track B proposal — now three consecutive flags.

## Decision

**APPROVE** publication as **REVIEW_ONLY**. Data integrity clean; holiday handling correctly reasoned and disclosed. Publication recommendation: REVIEW_ONLY.
