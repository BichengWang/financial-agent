# 08 Risk Review — 2026-07-30

**Committee decision: APPROVE publication as NO_TRADE.**

## Top concerns

1. **Critical — factor convergence:** Fund_Z and Sent_Z are unavailable; every ranked equity fails the three-family gate.
2. **High — market-forecast calibration:** MARKET_FORECAST direction accuracy is 16.39% at n=63, but eff_n=1 blocks a Track A repair.
3. **High — portfolio feasibility:** the diagnostic sleeve fails beta_0_90_to_1_10, drawdown95_at_or_below_0_08, factor_family_gate.

## Checklist

| Check | Result |
| --- | --- |
| Price/target lineage | PASS — Nasdaq plus Yahoo within 1%, targets/CI formula-bound |
| Sigma lineage | PASS — REALIZED_VOL_30D from adjusted closes |
| Score attribution | PASS — top signed component drivers, family z, DQ, penalties and rows present |
| Metric ledger | PASS — grouped formulas, portfolio diagnostics and full per-name technical fields are ledgered |
| Kelly thresholds | PASS — 5% cap binding disclosed per name; factor gate leaves every weight at zero |
| Technical lineage and interpretation | PASS — `technical_indicators.json`, 517/518 OK; TD9/RSI/MACD are multi-signal context, never standalone; bullish-cross credit is gated by positive daily 20/60 momentum and relative strength |
| Source Ledger completeness | PASS — observed and forecast prices, indicators, sizing inputs and downstream analytics close to L001-L068 |
| GO-blocking discipline | PASS — Enhancing gaps are caps, not named GO blockers |
| Prediction records | PASS — 20 equities + 3 ETFs |
| Settlement timing | PASS — 0 new rows; normalizer preserves 58 earlier valid TARGET_EQ_RUN_DATE rows |
| Earnings grounding | PASS — exact or prior-report+91d `ESTIMATED (±5d)` dates for every scored name; complete forward sweep cross-check; retired price-signature heuristic absent |
| Risk-free alignment | PASS — 3.83% is identical in source and calculations |

Publication recommendation: **NO_TRADE**. The audit pass repaired MoM price lineage, signed component-driver selection, exact transform disclosure, ETF diagnostics, earnings typing, portfolio formulas, and downstream price tagging; the remaining failure is the structural factor-family gate.
