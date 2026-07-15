# 08 Risk Review

## Committee Decision

`APPROVE NO_TRADE`.

## Top Concerns

1. The 2026-06-17 vintage produced 9/14 hits but rank IC -0.248; ordering remains weak even though rolling rank IC is narrowly positive at +0.040.
2. The leaderboard is one-family technical evidence at DQ 14/18 = 0.78. Fundamental, Sentiment, and per-name Macro are unavailable, so no candidate reaches the three-family or 85% completeness threshold.
3. Prior packages contained 184 settlement rows for only 86 keys, including conflicting July 14 cuts. This run rejects the timing-invalid intraday rows, but a durable canonical settlement implementation remains the P0 process improvement in `plan/2026-07-15-canonical-settlement-ledger.md`.

## Lineage Checks

- Price/target: PASS. Current-run Yahoo and Nasdaq values agree within 1% for every published entry; maximum divergence is 0.2446%. Targets and CIs derive from ledger-backed price, mu, and realized sigma.
- Settlement: PASS. All 14 due equities are scored on alpha versus recorded SPY; ETFs use raw return. Every record uses the completed July 14 close under `TARGET_EQ_RUN_DATE`.
- Canonicalization: PASS FOR CURRENT PACKAGE. The timing-valid rollup is 91 equities and 12 market forecasts; duplicate candidates are audit-only. The implementation plan is logged as Track B/HUMAN_REVIEW.
- Stage ordering: PASS. Reflection completed before current candidate ranks were published.
- Sigma: PASS. Every new forecast uses `REALIZED_VOL_30D` from completed Nasdaq history.
- Earnings: PASS WITH FLAGS. All 20 dates are grounded; 2 names enter the buffered event window and receive 0.10 penalties.
- Event concentration: PASS WITH FLAGS. 12/20 monitors have estimated reports within the forecast horizon; the July 28-29 FOMC meeting is also inside it.
- Score attribution: PASS. `05` shows raw, winsorized, and z values, family weights, DQ, penalties, final Adj Score, and ledger rows; missing families are `UNAVAILABLE`.
- Kelly/tail metrics: PASS as diagnostics. No size is approved.
- Technical lineage: PASS. Displayed states cite a distinct price-history row plus helper formulas; none is treated as a standalone signal.
- GO-blocking discipline: PASS. All five Required inputs pass; Enhancing gaps lower DQ but do not block GO. The independent evidence thresholds produce `NO_TRADE`.
- Prediction records: PASS. Twenty equity monitors plus SPY/QQQ/SOXX and 17 settlements are present.
- Evolution: DEFERRED to the post-close cadence. The single Track B priority is documented in `plan/` and `13`; no scoring or protected rule changes in this run.

Final publication recommendation: `NO_TRADE`.
