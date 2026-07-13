# 08 Risk Review

## Committee Decision

`APPROVE NO_TRADE`.

## Top Concerns

1. The June 15 vintage rank IC is -0.083 despite 11/17 direction hits; the normalized weighted rank IC remains +0.124, so no calibration override fires, but the existing confidence restraint remains appropriate.
2. The leaderboard is one-family technical evidence at DQ 0.78. Fundamental, Sentiment, and per-name Macro families are unavailable, so no candidate reaches the three-family or 85% completeness threshold.
3. This pre-open publication settles target-day forecasts at the latest completed July 10 close. The convention is explicit and repeatable, but it is not a July 13 regular-session close.

## Lineage Checks

- Price/target: PASS. Current-run Yahoo and Nasdaq `Previous Close` values agree within 1% for all 38 unique published/settled symbols. Targets and CIs derive from ledger-backed price, mu, and realized sigma.
- Settlement: PASS. All 17 due equities are scored on alpha versus their recorded SPY benchmark; SPY/QQQ/SOXX are scored separately on raw return. Twenty result rows are present in `01`, `02`, and `15`.
- Stage ordering: PASS. Raw PRECHECK support files preceded grounding; REFLECTION closed before any candidate score or portfolio decision was accepted.
- Sigma: PASS. Every new forecast uses `REALIZED_VOL_30D` from current-run histories.
- Earnings: PASS. Nineteen shortlist dates were fetched this run; DAL uses the allowed official July 10 report +91-day cadence estimate. HOOD is 16 days from its confirmed date, outside the 14-day penalty window.
- Event concentration: PASS WITH FLAG. No published monitor is inside the 14-day earnings window; the July 28-29 FOMC meeting is inside the forecast horizon.
- Score attribution: PASS. `05` shows the seven winsorized technical metric z-scores, family weights, DQ, penalties, and final Adj Score; missing families are `UNAVAILABLE`.
- Kelly/tail metrics: PASS as diagnostics. No position size is approved.
- Technical lineage: PASS. Displayed TD9/RSI/MACD/MA/momentum/volume/RS values trace to `technical_indicators.json` and history rows.
- Universe filters: INCOMPLETE / PROPERLY DOWNGRADED. Price and listing-age checks pass for 513 names; six full-universe reference/liquidity field groups remain `UNAVAILABLE` in L206.
- GO-blocking discipline: PASS. Enhancing feeds are not mislabeled Required failures; the independent evidence thresholds produce `NO_TRADE`.
- Prediction records: PASS. Twenty equity monitors plus SPY/QQQ/SOXX are present, with 20 newly matured settlement records.
- Evolution: PASS. The prior accepted confirmed-earnings fetch was executed; today's single Track B proposal addresses all-model due-inventory visibility without changing a protected rule.

Final publication recommendation: `NO_TRADE`.
