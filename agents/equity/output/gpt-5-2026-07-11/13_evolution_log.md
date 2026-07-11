# 13 Evolution Log

| Field | Value |
| --- | --- |
| Date | 2026-07-11 |
| Status | `NO_TRADE` |
| Regime | `BULL` |
| Evaluation window | Trailing 7 calendar days across all committed model packages plus the current run. |
| Ledger status | 29 unique settled equities; weighted rank IC -0.007; 0 market forecasts settled. |
| Baseline flag | `SAME_MODEL_BASELINE` |

## Observe

The settlement audit found 70 repeated stored rows but only 29 unique equity forecasts. Their hit rate and CI calibration are acceptable-to-mixed, while weighted rank IC remains slightly negative. The next independent holdout is the June 14 vintage due July 12: 17 equities plus three market forecasts that must be scored separately.

## Diagnose

Primary diagnosis: `factor calibration`. The ordering signal is not yet demonstrably predictive; technical-only daily leaderboards also remain crowded and non-investable.

## Hypothesis And Proposed Change

Track A: cap the mu Calibration Table's >=95th-percentile tier at +5.0% instead of +6.0%. Hypothesis: shrinking the top-band prior will reduce magnitude error without degrading rank ordering or drawdown. This is the carried-forward calibration proposal required by the negative-rank-IC priority override; it is not applied today.

## Validation

The July 12 17-equity vintage is the first new out-of-sample holdout. Test the counterfactual under the policy standard: IR improvement >=0.05 or hit-rate improvement >=2pp without worse drawdown; maximum drawdown deterioration <=0.50pp; turnover increase <=25%. ETF records are excluded from equity rank IC and assessed separately.

## Decision

`DEFER / NO_CHANGE_ACCEPTED`. The holdout is not due on July 11, so changing the mu table today would be premature. The active maximum-`MEDIUM` confidence cap remains; today's monitoring labels are `LOW`. No Track B mutation consumes the one-change slot while calibration priority is active.
