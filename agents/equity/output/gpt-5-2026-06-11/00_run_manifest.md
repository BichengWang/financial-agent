# 00 Run Manifest

| Field | Value |
|---|---|
| Run date | 2026-06-11 |
| Model | gpt-5 |
| Run mode | MANUAL_AUTOMATION via stale request path `investments/equity/prompt/main.md`; executed current repo entrypoint `investments/equity/daily_investment_system/main.md` |
| Data mode | DELAYED |
| Status target | GO if all required inputs and portfolio constraints pass |
| Final status | NO_TRADE |
| Output folder | `investments/equity/output/gpt-5-2026-06-11/` |
| Retrieved at | 2026-06-11T18:46:41+00:00 |
| Reflection baseline | `investments/equity/output/claude-opus-4-7-2026-05-12/` |
| Baseline flag | CROSS_MODEL_BASELINE; baseline is illustrative and therefore non-binding unless corroborated by current ledger rows |
| Prediction settlement | 0 settled; 12 open future records scanned from 1 prior prediction ledger(s) |
| Source ledger counts | OBSERVED 181; DERIVED 65; INFERRED 0; ILLUSTRATIVE 0; UNAVAILABLE 1 |

## State Transition Log

`PRECHECK -> REFLECTION -> DATA_OK -> SCORED -> PORTFOLIO_DRAFT -> RISK_REVIEW -> PUBLISHED -> CLOSE_LOGGED -> EVOLUTION_REVIEW`

No stage halted. Data were sufficient for ranking and settleable prediction records. Portfolio construction rejected live positioning because the ranked long set is structurally beta-infeasible under the protected 5% single-name cap.

## GO-Gate Table (Required Inputs Only)

| Required input | Status | Evidence | Blocking? |
|---|---|---|---|
| Grounded entry price | GROUNDED | 42/42 sampled names have Nasdaq quote + Yahoo spark price agreeing within 1%; rows `L028` onward | No |
| ~60 trading days history for names and SPY | GROUNDED | 42/42 sampled names plus SPY have Nasdaq historical rows through 2026-06-10 | No |
| Sigma via fallback chain | GROUNDED | REALIZED_VOL_30D computed for every ranked/monitor name | No |
| Next earnings date | GROUNDED | Nasdaq/Zacks dates or cadence-derived Nasdaq rows for all names; no ranked name inside buffered 19-day window | No |
| Sampled universe protocol | GROUNDED | 42 large liquid cross-sector names, including prior carry-forwards and 2-3+ large names per GICS sector | No |

## Enhancing Inputs (Caps, Not GO Blockers)

| Enhancing input | Status | Treatment |
|---|---|---|
| Options IV/skew | Missing | Confidence capped at MEDIUM; sigma uses REALIZED_VOL_30D |
| Short interest / borrow | Missing | Confidence capped; no short-squeeze thesis used |
| Full analyst-revision tape | Missing | EPS surprise used as observed fundamental proxy only |
| Institutional flow | Missing | Not used |
| Full-universe percentile feed | Missing | Percentiles labeled `SAMPLED_PCTL (n=42)` |

## Artifact Checklist

- [x] `00_run_manifest.md`
- [x] `01_preflight.md`
- [x] `02_reflection.md`
- [x] `03_regime_and_data.md`
- [x] `04_universe_summary.md`
- [x] `05_factor_scores.md`
- [x] `06_top_candidates.md`
- [x] `07_portfolio_proposal.md`
- [x] `08_risk_review.md`
- [x] `09_final_report.md`
- [x] `10_midday_monitor.md`
- [x] `11_preclose_check.md`
- [x] `12_close_log.md`
- [x] `13_evolution_log.md`
- [x] `15_predictions.json`

## Final Publication Decision

`NO_TRADE`: the candidate forecasts are settleable and auditable, but a live long portfolio would require violating the 0.90-1.10 beta band. Maximum NAV beta using all positive-beta investable-grade names at the 5% cap is only 0.199.
