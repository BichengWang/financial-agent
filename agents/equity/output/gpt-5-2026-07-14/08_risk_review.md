# 08 Risk Review

## Committee Decision

`APPROVE NO_TRADE`.

## Top Concerns

1. The June 16 vintage rank IC is -0.292 despite 10/14 direction hits. Normalized weighted rank IC remains narrowly positive at +0.050, so the calibration priority override does not fire, but confidence restraint is required.
2. The leaderboard is one-family technical evidence at DQ 14/18 = 0.78. Fundamental, Sentiment, and per-name Macro families are unavailable, so no candidate reaches the three-family or 85% completeness threshold; Technical supplies 100% of nonzero conviction and also violates the 50% family-concentration cap.
3. The late daily run mixes a July 14 delayed intraday price and partial-session technical/ranking cut with completed July 13 risk histories. Each lineage is explicit and prices agree across providers, but the time-cut mismatch requires post-close process review.

## Lineage Checks

- Price/target: PASS. Current-run Yahoo and Nasdaq values agree within 1% for all 35 unique published/settled symbols; maximum divergence is 0.426474%. Targets and CIs derive from ledger-backed price, mu, and realized sigma.
- Settlement: PASS. All 14 due equities are scored on alpha versus their recorded SPY benchmark; SPY/QQQ/SOXX are scored separately on raw return. Seventeen result rows are present in `01`, `02`, and `15`. Rolling duplicates use the deterministic policy in `settlement_precedence_manifest.json`: exact target-date settlement run first, otherwise earliest complete settlement run after target; price observation dates are tracked separately for non-trading days.
- Stage ordering: PASS. PRECHECK support files preceded REFLECTION; current settlements closed before any candidate rank was published.
- Sigma: PASS. Every new forecast uses `REALIZED_VOL_30D` from 251 completed Nasdaq history bars.
- Earnings: PASS WITH FLAG. Eighteen final dates use current Nasdaq/Zacks observations; BAC and GS use official July 14 reports +91-day cadence. No final monitor enters the buffered event window, but 12/20 estimated reports cluster August 3-6 inside the forecast horizon. Ledger: L206,L207.
- Event concentration: PASS WITH FLAGS. The July 28-29 FOMC meeting and the 12-name estimated August 3-6 earnings cluster are inside the forecast horizon. Ledger: L245,L207.
- Score attribution: PASS. `05` shows raw, winsorized, and z values for all seven technical metrics, family weights, the 14/18 DQ calculation, penalties, final Adj Score, and Source Ledger rows; missing families are `UNAVAILABLE`.
- Metric-ledger completeness: PASS. All 20 equity predictions carry nonempty `ledger_rows` and `score_explainability.ledger_rows`; `01` contains 250 total rows before publication.
- Kelly/tail metrics: PASS as diagnostics. All 20 displayed 0.25-Kelly values bind at the protected 5% cap; no position size is approved.
- Technical lineage and interpretation: PASS. Displayed TD9/RSI/MACD/MA/momentum/volume/RS values cite a distinct Yahoo history row plus helper formulas, and `05` records bullish/bearish state mappings, breadth construction, penalties, and signal direction.
- Universe screens: INCOMPLETE / PROPERLY DOWNGRADED. Six Enhancing full-universe reference/liquidity field groups remain `UNAVAILABLE`; no pass is inferred.
- GO-blocking discipline: PASS. All five Required inputs pass. Missing Enhancing screens lower DQ/confidence but are not treated as Required failures; the three independent factor-evidence thresholds produce `NO_TRADE`.
- Prediction records: PASS. Twenty equity monitors plus SPY/QQQ/SOXX are present, with 17 newly matured settlement records.
- Evolution: DEFERRED. One preliminary Track B snapshot-cut proposal is logged, but the required after-close review was not due; no change is accepted or effective in this package.

Final publication recommendation: `NO_TRADE`.
