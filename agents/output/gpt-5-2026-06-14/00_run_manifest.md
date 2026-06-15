# 00 Run Manifest

| Field | Value |
|---|---|
| Date | 2026-06-14 |
| Model | gpt-5 |
| Run mode | Manual weekend/evening run of `investments/equity/prompt/main.md`; compatibility stub redirects to canonical `daily_investment_system/main.md` |
| Data mode | DELAYED — last regular-session prices dated 2026-06-12; fetched during this run and cross-checked by Yahoo Finance chart plus Nasdaq quote info |
| Status target | GO if all data and portfolio constraints pass |
| Final status | NO_TRADE |
| State path | PRECHECK -> REFLECTION -> DATA_OK -> SCORED -> PORTFOLIO_DRAFT -> RISK_REVIEW -> PUBLISHED -> CLOSE_LOGGED -> EVOLUTION_REVIEW |
| Agents executed | Orchestrator, Data/Regime, Factor Scoring, Portfolio Construction, Risk Committee, Evolution |
| Retrieval timestamp | 2026-06-15T01:11:44Z |

## Rebase / Entrypoint

`kw/mac-air` was rebased against `origin/main`; it was already up to date. The requested compatibility path was missing on `origin/main`, so this run added `investments/equity/prompt/main.md` as a redirect to the canonical prompt. No research rules changed.

## Final Decision

`NO_TRADE`. Required data inputs were usable for scoring and forecasts, but the portfolio construction feasibility pre-check failed the protected NAV beta band. The 8 investable-grade names can contribute only **0.384** beta to NAV at the 5% single-name cap, below the required 0.90-1.10 range. Equal-weight beta inside the sleeve is 0.959, but the protected rule is applied to the capped portfolio, not to a hypothetical 100% sleeve that violates the 5% cap.

## Reflection Baseline

| Item | Value |
|---|---|
| Baseline path | `investments/equity/output/claude-opus-4-7-2026-05-12` |
| Baseline flag | CROSS_MODEL_BASELINE |
| Reason | No same-model folder in the 2026-04-30 to 2026-05-24 MoM window; 2026-05-12 is the closest in-window cross-model package to the 2026-05-17 target. |

## Prediction Settlement Summary

Scanned `claude-fable-5-2026-06-10/15_predictions.json` and `gpt-5-2026-06-11/15_predictions.json`. No OPEN record had `target_date <= 2026-06-14`; first known due date remains 2026-07-08. This run publishes 20 new OPEN records: 17 equity-alpha forecasts plus 3 core ETF market forecasts.

## Source Ledger Coverage Summary

| Claim type | Count |
|---|---:|
| OBSERVED | 90 |
| DERIVED | 152 |
| INFERRED | 0 |
| ILLUSTRATIVE | 0 |
| UNAVAILABLE | 0 |

## GO-Gate Table

| Required input | Status | Evidence |
|---|---|---|
| Grounded entry price | PASS | Yahoo chart close cross-checked with Nasdaq quote info for all sampled names; max cross-check difference 0.00%. |
| ~60 trading days of price history for each name and SPY | PASS | 82 daily closes fetched per symbol from Yahoo chart endpoint. |
| Sigma via fallback chain | PASS | `REALIZED_VOL_30D` computed from fetched daily returns for every ranked and monitored name. |
| Next earnings date | PASS | Nasdaq earnings-surprise prior-report dates cadence-estimated at +91d and tagged `ESTIMATED (+/-5d)`. |
| Sampled universe protocol | PASS | 42 equities covering all 11 GICS sectors plus carry-forward/theme names. |

Enhancing feeds missing: options IV/skew, short-interest/borrow, full-universe percentile feed, bid-ask tape, analyst-revision tape, institutional flow. These cap confidence and exposure but do not block `GO` by themselves.

## Artifact Checklist

| Artifact | Status |
|---|---|
| 00_run_manifest.md | Complete |
| 01_preflight.md | Complete — 242 Source Ledger rows |
| 02_reflection.md | Complete |
| 03_regime_and_data.md | Complete — core ETF block present |
| 04_universe_summary.md | Complete |
| 05_factor_scores.md | Complete |
| 06_top_candidates.md | Complete |
| 07_portfolio_proposal.md | Complete — NO_TRADE feasibility result |
| 08_risk_review.md | Complete — REJECT portfolio / approve NO_TRADE publication |
| 09_final_report.md | Complete |
| 10_midday_monitor.md | Complete — manual weekend note |
| 11_preclose_check.md | Complete — manual weekend note |
| 12_close_log.md | Complete — no positions |
| 13_evolution_log.md | Complete |
| 15_predictions.json | Complete — 20 OPEN records, settlements empty |
