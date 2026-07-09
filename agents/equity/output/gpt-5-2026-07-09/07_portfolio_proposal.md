# 07 Portfolio Proposal

No portfolio is proposed. The GO gate fails on refreshed earnings dates, and the score stack has only one sourceable factor family. Sizing a live portfolio would violate the evidence threshold even though delayed prices and realized-volatility sigma are available.

## Portfolio Analytics

`N/A - no live portfolio`: risk analytics are not computed for execution because the portfolio is rejected before sizing. Ranked-name risk metrics are present in `05_factor_scores.md` and `15_predictions.json` for settlement.

## Excluded-Name Rationale

All ranked names are excluded from a live book for the same reason: missing earnings-date, fundamental/revision, and sentiment/positioning evidence.
