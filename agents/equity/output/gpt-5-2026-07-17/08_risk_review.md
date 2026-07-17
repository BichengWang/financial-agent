# Risk Committee Review — 2026-07-17

## Decision

`APPROVE NO_TRADE`. The monitoring forecasts and core ETF block are publishable for calibration; no live portfolio is authorized.

## Top Concerns

1. **Evidence convergence:** every equity has one supportive scoring family, 77.78% completeness, and Technical supplies more than the permitted 50% of conviction.
2. **Factor calibration:** canonical weighted rank IC is `-0.008757` over 119 equity settlements (L336,L337); confidence stays capped at `MEDIUM` by rule (today's names are already `LOW`).
3. **Event concentration:** six names have literal earnings dates inside 14 calendar days; the required +/-5-day estimated-date buffer adds MPC, PSX, and DOC, so nine names exceed the maximum of two before portfolio sizing (L213,L222,L240,L249,L267,L276,L285,L312,L321).

## Control Review

| Control | Result | Evidence |
| --- | --- | --- |
| Price/target lineage | PASS | All entry and settlement prices have two sources, dates, timestamps, and <=1% divergence |
| Sigma lineage | PASS | All forecasts use REALIZED_VOL_30D from completed fetched histories |
| Score attribution | PASS | Every monitor shows family values, DQ, penalties, drivers, and metric rows |
| Metric ledger coverage | PASS | 370 contiguous Source Ledger rows |
| Kelly handling | PASS | Every monitor has computed 0.25 Kelly, capped at 5%; no sizing follows because evidence gates fail |
| Technical lineage | PASS | All displayed TD9/RSI/MACD/MA/momentum/RS fields come from technical_indicators.json |
| GO-blocking discipline | PASS | Enhancing inputs are caps only; NO_TRADE comes from the evidence thresholds |
| Prediction completeness | PASS | 20 EQUITY_ALPHA + 3 MARKET_FORECAST records and 63 settlements in valid JSON |
| Canonical settlement ledger | PASS | 119 equity + 18 market canonical settlements; zero due and zero conflicts |
| Event concentration | FAIL / NO_TRADE | 6 literal-date names / 9 names after the required estimated-date buffer, versus a maximum of 2 (L213,L222,L240,L249,L267,L276,L285,L312,L321) |

No revision is requested. Final publication recommendation: `NO_TRADE`.
