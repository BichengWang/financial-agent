# 08 Risk Review

## Committee Decision

`APPROVE NO_TRADE`.

## Top Concerns

1. Calibration state is knife-edge: normalized weighted rank IC is -0.007 at n=29, so the active maximum-`MEDIUM` cap must remain; today's `LOW` labels are stricter.
2. The leaderboard is one-family technical evidence at DQ 0.78. Fundamental, Sentiment, and per-name Macro families are unavailable, so no candidate reaches the three-family or 85% completeness threshold.
3. The June 14 holdout matures July 12: 17 equity predictions and three separately scored ETF forecasts. Settling them early or pooling ETF outcomes into equity rank IC would breach the prediction contract.

## Lineage Checks

- Price/target: PASS. Yahoo and Nasdaq values agree within 1%; Nasdaq's one-session-behind display label is disclosed. Targets and CIs derive from ledger-backed prices, mu, and realized sigma.
- Sigma: PASS. Every record uses `REALIZED_VOL_30D` from current-run histories.
- Earnings: PASS. Nineteen Nasdaq/Zacks dates plus one official-cadence DAL estimate; HOOD receives the buffered-window penalty.
- Score attribution: PASS. Each score shows family z-scores, DQ, penalties, drivers, and metric rows; missing families are explicit `UNAVAILABLE`.
- Kelly/tail metrics: PASS as diagnostics; no size is approved.
- Technical lineage: PASS. Displayed TD9/RSI/MACD/MA/momentum/volume/RS values trace to `technical_indicators.json` and history rows.
- GO-blocking discipline: PASS. Enhancing feeds are not misclassified as Required failures; the independent evidence thresholds produce `NO_TRADE`.
- Prediction records: PASS. Twenty equity monitors plus SPY/QQQ/SOXX are present; settlements are empty because nothing newly matured.

Final publication recommendation: `NO_TRADE`.
