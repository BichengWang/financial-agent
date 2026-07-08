# 08 Risk Review

## Committee Decision

`APPROVE` the publication as `NO_TRADE`.

## Top Concerns

1. Portfolio beta feasibility fails: max NAV beta is 0.280, below the protected 0.90-1.10 band.
2. Enhancing feeds are unavailable, so confidence remains capped at `MEDIUM` and no `HIGH` labels are allowed.
3. Several top names have mixed short-window technical states, so the score attribution must remain probabilistic and monitorable rather than executable.

## Required Checks

| Check | Result |
| --- | --- |
| Price/target lineage | PASS - every entry, target, and CI uses Yahoo price rows cross-checked with Nasdaq quote values. |
| Sigma lineage | PASS - every sigma uses REALIZED_VOL_30D from fetched daily returns. |
| Score attribution | PASS - ranked names include family z-scores, DQ, penalties, and score traces. |
| Metric ledger coverage | PASS - price, history, beta, sigma, earnings, liquidity, and technical rows are present. |
| Kelly threshold handling | PASS - investable names have positive capped Kelly; lower-ranked names are monitor-only or diagnostic. |
| Technical indicator lineage | PASS - all displayed TD-9, RSI, MACD, MA, momentum, volume, and RS fields cite technical_indicators.json. |
| GO-blocking discipline | PASS - missing enhancing feeds cap confidence only; NO_TRADE is caused by protected portfolio beta feasibility. |
| Prediction records | PASS - every investable/monitor equity plus SPY, QQQ, SOXX is represented in 15_predictions.json. |

## Final Publication Recommendation

Publish `NO_TRADE`. Do not execute a portfolio.
