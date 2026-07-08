# 08 Risk Review — Committee Decision

Adversarial review of the 2026-07-02 package (23 monitoring forecasts + 3 core ETF forecasts, proposed status NO_TRADE).

## Checklist Findings

1. **Fabricated/weak inputs** — none. Every price is tagged LIVE with observation date 2026-07-02 and two-source verification (Yahoo intraday + Nasdaq, max divergence 0.635%); IBKR MCP live corroboration on 7 names (≤0.18%). Intraday partial-bar and partial-volume caveats disclosed rather than hidden.
2. **Overfitting/unvalidated signals** — momentum/risk-only scoring disclosed in every trace. The committee re-emphasizes: this leaderboard is a rotation screen until fundamental/sentiment feeds exist.
3. **Event concentration** — 0 published names inside the 14d earnings window (11 shortlist names penalized out, incl. DAL rank 30 and UNH); trigger #4 not activated. FOMC sits 1 day before the 2026-07-30 target date — CI calibration absorbs it, documented in 03.
4. **Correlation/sector crowding** — Health Care 8/23 published names; DOC|DVA pairwise correlation 0.73 flagged (both health-care-adjacent defensives); any GO book from this board binds the 30% sector cap. Averages remain low (0.127).
5. **Beta drift** — no portfolio; pre-check exhibit: max achievable NAV beta 0.63 at the 5% cap (< 0.90 floor). Correctly diagnostic-only.
6. **Thesis quality vs confidence** — all LOW, consistent with 2/4 families. MRNA carries the highest standalone risk (22% monthly sigma, RSI 80, −18% DD60): correctly penalized (−0.10: HIGH_VOL + exhaustion) and mu shaded to +5%; the committee accepts it as a monitor-only forecast, would reject it from any sized book.
7. **Rules mismatches** — one found and corrected mid-run: the mu Calibration Table's ±2pp total-adjustment cap is now enforced by a clamp; the 2026-07-01 UNH record (−3pp stacked) is disclosed in 02 §6 and 13 and stands as recorded for settlement. No other mismatches on cross-read.
8. **Price/derived-field citations** — complete (price_date + price_tag everywhere; no targets off unverified prices).
9. **Sigma** — REALIZED_VOL_30D on all 26 records; no blanket UNAVAILABLE; every ranked name settleable.
10. **Score attribution** — full traces with family z-scores, DQ 0.80, penalties, drivers, ledger rows; UNAVAILABLE families never counted as support.
11. **Source Ledger** — 208 rows cover all downstream facts; derived rows cite formulas and inputs.
12. **Live-sounding claims** — LIVE tags are backed by actual live fetches this run (19:21–19:29Z); no stale-as-current claims found.
13. **GO-blocking discipline** — correct: all 5 Required inputs PASS; Enhancing gaps are caps only. NO_TRADE flows from threshold arithmetic. Now blocked identically in 3 consecutive completed runs across 2 models — escalated to Evolution as mandatory work (13).
14. **Prediction records** — all 23 ranked names + 3 ETF records present with benchmark_price (741.60) and explainability; UNH deliberately not ranked today (DOWNGRADE in 02 §5) so no record is owed for it.
15. **Technical indicator lineage** — all values cite technical_indicators.json; TD9-9/RSI≥75 used as flags/shades only; FDXF failure surfaced as exclusion.

## Top Three Concerns (severity order)

1. **Publishing 23 momentum-extended names into a live de-grossing tape.** Second consecutive violent unwind session (SOXX −7.2% intraday after −6.41%; HUM −3.8% giving back). 10 of 23 names carry exhaustion flags; the equal-weight top-12 diagnostic dd95 is 9.1% — above the 8% cap that would bind a real book (third independent NO_TRADE ground). Forecast-only publication is the correct exposure.
2. **Intraday entry prices ~40 minutes before a pre-holiday close.** Prices may drift into the close and over the 3-day weekend gap; settlements use recorded entries (documented). Acceptable for monitor forecasts; would be unacceptable for GO sizing.
3. **Two-family scoring** (standing concern): the board can chase whatever momentum regime is in force. First settlements land 2026-07-08 — the committee expects the calibration metrics to start disciplining mu/sigma within two weeks.

## Decision

**APPROVE** publication as **NO_TRADE**. No revision required; data integrity clean; the mu-clamp correction is a compliance fix, properly disclosed. Publication recommendation: NO_TRADE.
