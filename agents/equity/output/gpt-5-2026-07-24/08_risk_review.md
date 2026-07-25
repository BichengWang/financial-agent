# 08 Risk Review — 2026-07-24

## Committee decision: APPROVE NO_TRADE

Final publication recommendation: **NO_TRADE**. The methodology and package are publishable, but no equity clears all evidence thresholds.

## Top concerns

1. **Critical — factor convergence:** Fund_Z and Sent_Z are unavailable, so every name fails 3-of-4 support and available conviction is confined to two families (L010).
2. **High — calibration:** weighted rank IC remains -0.093914 over 189 canonical equity settlements, so no confidence above MEDIUM is permitted; all rows are LOW (L333).
3. **High — event density:** 3 top-20 names and 6 full-sleeve monitors are inside buffered earnings windows. Their penalties are present; they would be omitted as needed from any feasible basket, so this does not independently force NO_TRADE.

## Control review

| Control | Result |
|---|---|
| Price / target lineage | PASS — 29/29 Yahoo/Nasdaq comparisons within 1%; target/CI formulas ledger-backed |
| Universe eligibility | PASS — 515/515 passed >$2B; 511 retained names also pass history, price, ADV, and earnings-date screens |
| Earnings coverage | PASS — 511/511 scored names have dates; 3 unresolved names were excluded before ranking |
| Sigma lineage | PASS — REALIZED_VOL_30D for all 29 forecasts |
| Score attribution | PASS — family z-scores, DQ, penalties, drivers, and formula shown for all 26 equities |
| Kelly handling | PASS — preferred beta-adjusted edge / tracking-error variance used; no sizing because the investable set is empty |
| Technical lineage | PASS — record status 517 OK / 1 UNAVAILABLE; exact field-level D/W/M gaps disclosed in `04`; no hand-filled indicators |
| Source Ledger | PASS — contiguous L001–L336; every displayed bundle cited |
| GO-blocking discipline | PASS — Enhancing gaps only cap confidence; NO_TRADE is based on the binding three-family evidence threshold |
| Prediction records | PASS — 26 EQUITY_ALPHA + 3 MARKET_FORECAST, score explainability present, settlements empty because due=0 |

No revision pass is warranted: adding weights cannot repair missing production factor families without violating protected grounding rules.
