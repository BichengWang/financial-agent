# 08 Risk Review

Decision: `REJECT` live portfolio. Final publication recommendation: `NO_TRADE`.

## Top Concerns

1. Protected beta infeasibility: max NAV beta from positive-beta investable-grade names at 5% each is 0.199, far below 0.90.
2. Equal-weight investable-grade sleeve has Health Care concentration above the 30% gross-share cap.
3. Enhancing feeds are missing, so confidence is capped even though required inputs are grounded.

## Checklist

| Check | Result |
|---|---|
| Fabricated inputs | PASS - prices cross-checked and histories fetched this run |
| Source ledger coverage | PASS - price/history/earnings/beta/sigma/target rows in `01` |
| Sigma source | PASS - all sleeve forecasts use `REALIZED_VOL_30D` |
| Prediction records | PASS - `15_predictions.json` contains 17 records |
| GO-blocking classification | PASS - missing enhancing inputs are not GO blockers |
| Portfolio beta | FAIL - structural `NO_TRADE` |
| Sector concentration | FAIL in rejected equal sleeve |
| Drawdown | PASS - rejected sleeve estimate 2.91% below 8% |

Required fix: none inside this run. The proper action is to publish `NO_TRADE`, not to force a beta-compliant basket using weaker names.
