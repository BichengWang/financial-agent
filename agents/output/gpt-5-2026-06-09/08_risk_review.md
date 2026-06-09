# 08 Risk Review

## Committee Decision

`REJECT` for `GO`; publish `REVIEW_ONLY`.

## Top Three Concerns

1. Critical risk feeds are still missing. Options IV/skew, complete short-interest/borrow, execution spread/liquidity, and covariance/drawdown inputs are unavailable (L090-L093).
2. The candidate set is sampled, not a full U.S. equity universe. This blocks percentile claims from becoming investable rankings.
3. The paper sleeve cannot satisfy the portfolio beta band on a validated basis. The gross-normalized sampled beta is below the 0.90-1.10 band, and a valid covariance model is unavailable.

## Price Citation Review

PASS for review-only use. Every numeric entry price in the candidate and paper-sleeve tables has a price date, price tag, and source-ledger row.

## Derived-Field Review

PASS. Target prices, confidence intervals, drawdown, and Sharpe are not populated where source inputs are missing.

## Required Fixes Before Any Future GO

- Wire an options source for candidate IV30 and skew.
- Wire synchronized short-interest / borrow coverage.
- Wire execution-quality liquidity, including bid-ask spread.
- Wire a validated return-series covariance and 95th percentile drawdown model.
- Run a full U.S. eligible-universe screen rather than a sampled watchlist.

## Final Publication Recommendation

`REVIEW_ONLY`.

The report may publish the monitoring list, reflection, and paper sleeve for process tracking only. It must not present live position sizing, expected return, target price, or confidence interval fields.
