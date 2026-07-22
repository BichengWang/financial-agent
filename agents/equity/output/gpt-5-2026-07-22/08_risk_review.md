# 08 Risk Review — 2026-07-22

## Committee decision: APPROVE NO_TRADE

Final publication recommendation: **NO_TRADE**. The methodology and package are publishable, but no equity clears all evidence thresholds.

## Top concerns

1. **Critical — factor convergence:** Fund_Z and Sent_Z are unavailable, so every name fails 3-of-4 support and Technical exceeds 50% of conviction (L007).
2. **High — calibration:** weighted rank IC is -0.048856 over 175 canonical equity settlements, so no confidence above MEDIUM is permitted; all rows are LOW (L329).
3. **High — event concentration:** 3 top-20 names are inside the buffered 14-day earnings window. Their penalties are present, and the count independently exceeds the >2 NO_TRADE threshold.

## Control review

| Control | Result |
|---|---|
| Price / target lineage | PASS — 29/29 Yahoo/Nasdaq comparisons within 1%; target/CI formulas ledger-backed |
| Sigma lineage | PASS — REALIZED_VOL_30D for all 29 forecasts |
| Score attribution | PASS — family z-scores, DQ, penalties, drivers, and formula shown for all 26 equities |
| Kelly handling | PASS — computed diagnostically; no sizing because the investable set is empty |
| Technical lineage | PASS — 517 OK, 1 explicit UNAVAILABLE; no hand-filled indicators |
| Source Ledger | PASS — contiguous L001–L332; every displayed bundle cited |
| GO-blocking discipline | PASS — Enhancing gaps only cap confidence; NO_TRADE is based on independent evidence thresholds |
| Prediction records | PASS — 26 EQUITY_ALPHA + 3 MARKET_FORECAST, score explainability present, 0 settlement rows, due=17 with 17 verified candidates retained for next-run admission |

No revision pass is warranted: adding weights cannot repair missing production factor families without violating protected grounding rules.
