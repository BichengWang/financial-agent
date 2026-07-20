# 08 Risk Review — 2026-07-20

## Decision: APPROVE NO_TRADE

1. **Binding family gate:** Fund_Z/Sent_Z remain SHADOW/unpromoted; zero names meet three-of-four support.
2. **Calibration:** weighted rank IC is -0.048856 over 175 canonical equity settlements; confidence cannot expand.
3. **Event/tape risk:** the July 28–29 FOMC meeting lies inside the horizon and SOXX has 22.0% one-month realized sigma (L005,L008).

## Explicit control review

| Control | Result | Evidence / treatment |
|---|---|---|
| Price and target lineage | PASS | 36/36 Yahoo/Nasdaq comparisons pass; targets and CIs derive from entry, mu and sigma (L006) |
| Sigma lineage | PASS | REALIZED_VOL_30D from completed histories for every forecast; provisional July 20 rows excluded (L002) |
| Score attribution | PASS | all 23 rows carry Fund/Tech/Sent/Macro, DQ, penalties, positive/negative drivers and full formula traces |
| Metric Ledger coverage | PASS | price/event rows are separated from technical/risk/score/forecast metric rows in 05; no displayed numeric metric lacks a row |
| Kelly thresholds | PASS / CAP-BINDING | zero monitors have Kelly <=0 or <2%; all 23 sourceable 0.25-Kelly values reach the 5% single-name cap; NO_TRADE authorizes no sizing |
| Technical lineage / interpretation | PASS | TD9, RSI, MACD, MA, momentum, volume and relative strength come only from `technical_indicators.json` (L003); exhaustion is a penalty, never a standalone signal |
| Source Ledger completeness | PASS | allowed tags only; inferred regime is explicit (L008); Fund/Sent are UNAVAILABLE rather than neutral (L007) |
| GO-blocking discipline | PASS | Required price/history/sigma/event/universe inputs pass; Enhancing gaps cap DQ/confidence and do not create a false blocker |
| Prediction completeness | PASS | 23 equity records with explainability plus SPY/QQQ/SOXX and all 68 timing-valid settlements |

Final recommendation: **NO_TRADE**. No revision is warranted because the failure is structural evidence sufficiency, not a repairable portfolio mix.
