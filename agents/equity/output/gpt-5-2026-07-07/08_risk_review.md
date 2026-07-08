# 08 Risk Review

## Committee Decision

`APPROVE REVIEW_ONLY`. Do not publish a `GO` portfolio.

## Top Concerns

1. Required earnings-date coverage is unavailable for ranked equities, so event risk cannot be cleared.
2. Fundamental/revision and sentiment/positioning families are unavailable; the leaderboard is a technical monitor list, not a multi-factor investable set.
3. The paper top-10 basket has a parametric 95% drawdown proxy of 13.68%, above the 8% target.

## Lineage Checks

| Check | Result |
| --- | --- |
| Price/target lineage | PASS for monitoring records; entry prices and targets cite ledger rows. |
| Sigma lineage | PASS; all ranked names use `REALIZED_VOL_30D`. |
| Score attribution | PASS for technical-family scoring; Fund/Sent/Macro are explicitly unavailable. |
| Metric ledger coverage | PASS with `UNAVAILABLE` rows for missing Required/enhancing feeds. |
| Kelly threshold handling | PASS as diagnostic only; no GO allocation proposed. |
| Technical indicator lineage | PASS; values derive from `technical_indicators.json`. |
| GO-blocking discipline | PASS; missing earnings is a Required blocker, missing enhancing feeds are confidence caps. |
| Prediction records | PASS; `15_predictions.json` includes ranked monitors and SPY/QQQ/SOXX market forecasts. |

## Final Publication Recommendation

Publish as `REVIEW_ONLY` with settleable monitoring predictions. No trade instructions.
