# 08 Risk Review

## Committee Decision

`APPROVE NO_TRADE`.

## Top Concerns

1. The newly matured holdout improves weighted rank IC to +0.200, but one positive vintage does not justify silently lifting the existing confidence cap or changing calibration parameters.
2. The leaderboard is one-family technical evidence at DQ 0.78. Fundamental, Sentiment, and per-name Macro families are unavailable, so no candidate reaches the three-family or 85% completeness threshold.
3. Sunday publication reuses Friday's last grounded close. The data are valid for delayed research and settlement, but are not brokerage-executable and contain no new session information versus Saturday.

## Lineage Checks

- Price/target: PASS. Current-run Yahoo and Nasdaq values agree within 1%; Nasdaq's one-session-behind display label is disclosed. Targets and CIs derive from ledger-backed prices, mu, and realized sigma.
- Settlement: PASS. All 17 due equities are scored on alpha versus recorded SPY; SPY/QQQ/SOXX are scored separately on raw return. The non-trading-day convention and 20 result rows are recorded in `01`, `02`, and `15`.
- Stage ordering: PASS WITH DISCLOSURE. The support helpers wrote raw PRECHECK artifacts before second-source grounding finished; the orchestrator did not accept `DATA_OK`/`TECHNICALS_OK` or score candidates until Reflection closed at 13:19Z. The manifest records this gate-versus-file timing distinction.
- Sigma: PASS. Every new forecast uses `REALIZED_VOL_30D` from current-run histories.
- Earnings: PASS. Nineteen cached Nasdaq/Zacks dates plus one official-cadence DAL estimate; the current retry failure is disclosed. HOOD is 17 days from its confirmed date and receives no 14-day penalty.
- Event concentration: PASS WITH FLAG. No published monitor is inside the 14-day earnings window; the July 28-29 FOMC meeting is inside the forecast horizon (L199) and caps conviction but does not change `NO_TRADE`.
- Score attribution: PASS. `05` shows all seven winsorized metric z-scores feeding each `Tech_Z`, then family weights, DQ, penalties, and final Adj Score; missing families are explicit `UNAVAILABLE`.
- Kelly/tail metrics: PASS as diagnostics. Treynor, Calmar, raw/quarter Kelly, VaR, CVaR, and drawdown values/formulas are present in the per-name metric ledger rows; no size is approved.
- Technical lineage: PASS. Displayed TD9/RSI/MACD/MA/momentum/volume/RS values trace to full per-name L020-style rows, `technical_indicators.json`, and history rows.
- Universe filters: INCOMPLETE / PROPERLY DOWNGRADED. Price and listing-age checks pass for 513 names; six full-universe reference/liquidity field groups are `UNAVAILABLE` in L206. No `GO` claim or silent inclusion-filter pass is made.
- Penalty lineage: PASS. Every technical penalty is reproduced by the additive threshold formula in `05`/L207 from the per-name technical rows.
- GO-blocking discipline: PASS. Enhancing feeds are not misclassified as Required failures; the independent evidence thresholds produce `NO_TRADE`.
- Prediction records: PASS. Twenty equity monitors plus SPY/QQQ/SOXX are present, with 20 newly matured settlement records.
- Evolution: PASS. The accepted Track B repo-path correction changes invocation paths only and leaves every protected scoring, grounding, and risk rule intact.

Final publication recommendation: `NO_TRADE`.
