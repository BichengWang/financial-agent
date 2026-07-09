# 08 Risk Review

Decision: `APPROVE REVIEW_ONLY`; reject any `GO` interpretation.

## Top Concerns

1. Missing refreshed earnings dates are a Required-input failure for `GO`.
2. Fundamental/revision and sentiment/positioning feeds are unavailable, so the factor stack is technical-only and confidence is capped at `LOW`.
3. The monitoring sleeve remains technology/cyber/semiconductor concentrated, so live sizing would require a fuller risk input set.

## Required Checks

| Check | Result |
| --- | --- |
| Price/target lineage | PASS for review-only; delayed Yahoo chart rows and ledger IDs are present. |
| Sigma lineage | PASS; REALIZED_VOL_30D from fetched histories. |
| Score attribution | PASS; every Adj Score traces Tech_Z, DQ, and penalties. |
| Metric ledger coverage | PASS for displayed technical/risk metrics; non-price feeds marked UNAVAILABLE. |
| Kelly threshold handling | PASS for monitoring; no live positions sized. |
| Technical indicator lineage | PASS; all displayed states cite `technical_indicators.json`. |
| GO-blocking discipline | PASS; only Required earnings-date failure blocks GO. |
| Prediction records | PASS; core ETFs plus 20 monitoring names are in `15_predictions.json`. |

Final publication recommendation: `REVIEW_ONLY`.
