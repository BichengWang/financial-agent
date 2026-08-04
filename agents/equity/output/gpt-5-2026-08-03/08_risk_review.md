# 08 — Risk Review — 2026-08-03

## Committee decision

**`APPROVE NO_TRADE`**. The monitoring publication is auditable; an executable portfolio is
not defensible under the protected evidence thresholds.

## Top concerns

1. `Fund_Z` and `Sent_Z` are unavailable for all scoreable names, making three supportive
   families impossible and leaving Technical at 66.7% of live conviction.
2. Weighted rolling rank IC is -0.0879 over
   515 equity settlements; confidence remains capped `MEDIUM`.
3. `eff_n=1` means the large raw ledger is still one
   overlapping target-window sample; Track A changes cannot be accepted.

## Review checklist

| Control | Finding | Decision |
| --- | --- | --- |
| Price/target lineage | 23/23 completed closes cross-checked; targets = entry×(1+mu) | PASS |
| Sigma lineage | REALIZED_VOL_30D from the same fetched adjusted histories for every published record | PASS |
| Score attribution | Six-signal Tech_Z + four-signal Macro_Z; DQ and penalties disclosed per name | PASS |
| Metric ledger coverage | 207 ledger rows; missing families explicitly UNAVAILABLE | PASS |
| Kelly handling | Computed from beta-adjusted residual edge / tracking-error variance; no name promoted investable | PASS |
| Technical lineage | technical_indicators.py pack; RS diagnostics are not double-counted | PASS |
| GO-blocking discipline | Required inputs pass; NO_TRADE comes from evidence thresholds, not Enhancing gaps | PASS |
| Prediction completeness | 20 EQUITY_ALPHA + 3 MARKET_FORECAST; 88 settlements | PASS |
| Settlement timing | due=0; conflicts=0; weekend and post-close flags explicit | PASS |
| Hard risk caps | No portfolio proposed; diagnostic beta/correlation/drawdown/sector states disclosed | PASS |

No fabricated or contradictory evidence propagated. Required fixes before any future `GO`:
promote sourceable full-universe Fundamental and Sentiment families under governance, then
re-run all portfolio constraints. Final recommendation: **`NO_TRADE`**.
