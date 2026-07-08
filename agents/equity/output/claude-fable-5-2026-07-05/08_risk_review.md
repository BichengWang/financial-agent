# 08 Risk Review — Committee Decision

Adversarial review of the 2026-07-05 weekend package (23 monitoring forecasts + 3 core ETF forecasts, proposed status REVIEW_ONLY).

## Checklist Findings

1. **Fabricated/weak inputs** — none. All prices are official 2026-07-02 closes, DELAYED-tagged with observation date, verified Yahoo-vs-Nasdaq at 0.000% divergence for all 26 published names. IBKR's closed-market snapshots (2026-07-01 prior-session closes, `is_close: true`) were used only as prior-record verification and are labeled as such — the 07-03/07-04 finding reproduced a third time, no conflation with today's entries.
2. **Overfitting/unvalidated signals** — momentum/risk-only scoring disclosed everywhere; unchanged standing concern. Family-member sets for Tech_Z/Macro_Z disclosed in the 01 header, identical to 07-04.
3. **Event concentration** — 0 published names inside 14d earnings (21 shortlist names penalized out, incl. yesterday's #3 DOC, #16 WST, #18 KDP on the one-day window roll); three-day weekend gap risk on 2026-07-02 entries noted; FOMC (7/28-29) precedes the 2026-08-02 target by two-three sessions; FFIV (est 7/27), MAS/SWK/HUM/WELL/INCY/BXP (est 7/28-29) and BEN/ABBV (est 7/31) report inside the horizon but outside the buffered window — flagged per name in 05.
4. **Correlation/sector crowding** — Health Care 9/23 published names (39%); top-12 equal-weight HC share 42% would bind the 30% cap; MAS|SWK 0.64 and HSIC|BAX 0.56 pairwise correlations flagged; average low (0.177).
5. **Beta drift** — no portfolio; pre-check exhibit max NAV beta 0.70 < 0.90 floor, diagnostic-only.
6. **Thesis quality vs confidence** — LOW everywhere; MRNA again the highest standalone risk (22.5% sigma, -0.10 penalties), acceptable as forecast-only.
7. **Rules mismatches** — none found this run. The ±2pp mu clamp holds across the sleeve (max applied adjustment -1pp, EXHAUSTION-documented).
8. **Price/derived-field citations** — complete; entries carry price_date 2026-07-02 + DELAYED tags; targets/CIs derive from tagged entries.
9. **Sigma** — REALIZED_VOL_30D on all 26 records.
10. **Score attribution** — full traces, DQ 0.80, penalties, drivers, ledger rows; UNAVAILABLE families never supportive; positive drivers limited to sourceable technical/risk metrics.
11. **Source Ledger** — 208 rows; derived rows cite formulas/inputs; the ^IRX series is fresh this run (3.668% @ 2026-07-02, DELAYED) — the 07-03/07-04 staleness note is retired rather than silently dropped.
12. **Live-sounding claims** — none; the package consistently says "last completed session" / "Thursday's close" and labels today a closed Sunday.
13. **GO-blocking discipline** — correct; weekend rule (not Enhancing gaps) sets REVIEW_ONLY; family-gate would-be-NO_TRADE stated separately.
14. **Prediction records** — all 23 ranked names + 3 ETFs present with benchmark_price 744.78 and full score_explainability; UNH not ranked (DOWNGRADE, documented), so no record owed; DOC/WST/KDP not ranked today (earnings-window churn, documented), so no records owed. QQQ/SOXX mu records reproduce from the stated beta x prior derivation and carry machine-checkable `mu_derivation` blocks.
15. **Technical indicator lineage** — all values cite technical_indicators.json (517 OK, 2026-07-05T19:47:38Z) computed via --history-dir on the same fetched bars; TD9/RSI as flags only.

## Top Three Concerns (severity order)

1. **Fourth consecutive vintage of overlapping forecasts on the same entry tape** (2026-07-02 closes for the 07-02 intraday, 07-03, 07-04 and 07-05 runs; 20-name overlap with 07-04's sleeve): settlements will be strongly correlated observations and must not be read as independent calibration evidence (noted for the evolution agent — the correlated-cluster caveat now covers ~4x23 records maturing 2026-07-30..08-02).
2. **Weekend-vintage forecasts carry gap risk**: entries are Thursday closes; the first session that can move them is Monday 7/6, and this vintage's 28d window embeds the earnings season, FOMC, and a Sunday target date (2026-08-02, first settleable session 2026-08-03).
3. **Two-family scoring** (standing): unresolved pending the HUMAN_REVIEW decision on the Track B proposal — now five consecutive flags.

## Decision

**APPROVE** publication as **REVIEW_ONLY**. Data integrity clean; weekend handling correctly reasoned and disclosed; earnings-window churn (DOC/WST/KDP out, WELL/INCY/BXP in) is the penalty machinery responding to calendar drift as designed, not score instability. Publication recommendation: REVIEW_ONLY.
