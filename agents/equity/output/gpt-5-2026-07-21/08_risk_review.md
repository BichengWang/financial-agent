# 08 Risk Review — 2026-07-21

## Committee decision: APPROVE NO_TRADE

Final publication recommendation: **NO_TRADE**. The methodology and package are publishable, but no equity clears all evidence thresholds.

## Top concerns

1. **Critical — factor convergence:** Fund_Z and Sent_Z are unavailable, so every name fails 3-of-4 support and Technical exceeds 50% of conviction (L007).
2. **High — calibration:** weighted rank IC remains -0.048856 over 175 canonical equity settlements, so no confidence above MEDIUM is permitted; all rows are LOW (L297).
3. **Medium — event concentration:** 2 top-20 names are inside the buffered 14-day earnings window. Their penalties are present; the count does not independently exceed the >2 NO_TRADE threshold.

## Control review

| Control | Result |
|---|---|
| Price / target lineage | PASS — 26/26 Yahoo/Nasdaq comparisons within 1%; target/CI formulas ledger-backed |
| Sigma lineage | PASS — REALIZED_VOL_30D for all 26 forecasts |
| Score attribution | PASS — family z-scores, DQ, penalties, drivers, and formula shown for all 23 equities |
| Kelly handling | PASS — computed diagnostically; no sizing because the investable set is empty |
| Technical lineage | PASS — 516 OK, 2 explicit UNAVAILABLE; no hand-filled indicators |
| Source Ledger | PASS — contiguous L001–L300; every displayed bundle cited |
| GO-blocking discipline | PASS — Enhancing gaps only cap confidence; NO_TRADE is based on independent evidence thresholds |
| Prediction records | PASS — 23 EQUITY_ALPHA + 3 MARKET_FORECAST, score explainability present, settlements empty because due=0 |

No revision pass is warranted: adding weights cannot repair missing production factor families without violating protected grounding rules.
