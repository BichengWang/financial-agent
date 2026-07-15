# 00 Run Manifest

| Field | Value |
| --- | --- |
| Date | 2026-07-15 |
| Model | gpt-5 |
| Run mode | Automation run of agents/equity/daily_investment_system/main.md |
| Data mode | DELAYED |
| Status target | NO_TRADE unless at least five names satisfy the multi-family and 85% completeness gates. |
| Final status | NO_TRADE |
| Timing | Late daily run started about 15:40 ET; the 15:45 checkpoint was completed late at the 15:55 quote cut; one official earnings source was refreshed before the 16:19 ET package cut. |
| Snapshot convention | July 15 partial technical bars at 15:41 ET; entry quotes at 15:55-15:56 ET; completed Nasdaq risk and settlement histories through July 14; official MS earnings confirmation retrieved at 16:18 ET. |
| Agents executed | Orchestrator, Data/Regime, Factor Scoring, Portfolio Construction, Risk Committee; preliminary Evolution governance review. |
| Outstanding blockers | Fundamental/revision, Sentiment/Positioning, and per-name Macro families are unavailable. |
| Enhancing limitations (not GO blockers) | Full-universe reference/liquidity, options, short-interest/borrow, and institutional-flow feeds are unavailable. |
| Reflection baseline | agents/equity/output/gpt-5-2026-06-17 |
| Baseline flag | (none) - exact 28-day same-model baseline. |
| Prediction settlement summary | 17 newly due from gpt-5-2026-06-17: 14 equities and 3 market forecasts, all TARGET_EQ_RUN_DATE at July 14 close. |
| Canonical rolling inventory | 91 equities and 12 market forecasts; timing-invalid duplicates excluded. |
| next_due_target_date | 2026-07-16 |
| due_record_count_by_model | {"gpt-5": 17} |
| Source Ledger coverage | 106 OBSERVED, 139 DERIVED, 1 INFERRED, 0 ILLUSTRATIVE, 5 UNAVAILABLE. |
| Status eligibility | All five Required inputs pass. Technical is the only supportive family, DQ=14/18=77.78%, and Technical is 100% of nonzero conviction; all three evidence gates fail. |
| Core ETF Market Forecast Block | Present for SPY, QQQ, SOXX. |
| Priority plan | plan/2026-07-15-canonical-settlement-ledger.md |

## State Transition Log

`PRECHECK -> REFLECTION -> DATA_OK -> TECHNICALS_OK -> SCORED -> NO_TRADE -> RISK_REVIEW -> PUBLISHED`

The 12:15 ET monitor was missed before invocation; the 15:45 checkpoint was completed ten minutes late. No `CLOSE_LOGGED` or completed `EVOLUTION_REVIEW` state is claimed at the publication cut.

## GO-Gate Table

| Required Input | Status | Evidence | Blocks GO? |
| --- | --- | --- | --- |
| Grounded entry price | PASS for published sleeve | Yahoo/Nasdaq agree within 1% for 39 fetched bundles; max divergence 0.2446%. | No |
| ~60 trading days history per name and SPY | PASS | 251 completed Nasdaq daily bars for all 20 monitors and SPY/QQQ/SOXX. | No |
| Sigma via fallback chain | PASS | REALIZED_VOL_30D for all 20 monitors and core ETFs. | No |
| Next earnings date | PASS | Current-run Nasdaq/Zacks observations or disclosed cadence fallback; buffered penalties applied. | No |
| S&P 500 union Nasdaq-100 universe | PASS | 515-name union; 513 scoreable after SATS/FDXF history exclusions. | No |

Missing Enhancing inputs lower DQ and confidence but are not Required-input failures. The independent three-family, 85% completeness, and max-family-50% gates produce `NO_TRADE`.

## Artifact Checklist

| Artifact | Status |
| --- | --- |
| 00_run_manifest.md through 09_final_report.md | PRESENT |
| 10_midday_monitor.md | PRESENT - missed-checkpoint disclosure |
| 11_preclose_check.md | PRESENT - late 15:55 ET checkpoint |
| 12_close_log.md | PRESENT - not due at publication cut |
| 13_evolution_log.md | PRESENT - one Track B plan, decision deferred to post-close cadence |
| 14_weekly_review.md | PRESENT - Wednesday, not applicable |
| 15_predictions.json | PRESENT - 23 OPEN predictions + 17 settlements |
| 16_monthly_review.md | PRESENT - not month-end |
| eligible_universe.txt / universe_summary.json | PRESENT |
| technical_indicators.json | PRESENT - 516/518 OK after VRTX retry |
| nasdaq_verification_manifest.json | PRESENT - 39/39 current bundles within 1% |
| earnings_calendar_manifest.json | PRESENT - 120 attempts; all 20 published dates grounded |
| history_metrics_manifest.json | PRESENT - 23/23 published/core histories OK |
| settlement_precedence_manifest.json | PRESENT - 103 timing-valid canonical keys |
| score_universe_manifest.json / run_computed_manifest.json | PRESENT |
| plan/2026-07-15-canonical-settlement-ledger.md | PRESENT - P0 improvement plan |
