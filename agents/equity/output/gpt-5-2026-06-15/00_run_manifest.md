# 00 Run Manifest

| Field | Value |
|---|---|
| Run date | 2026-06-15 |
| Model | gpt-5 |
| Run mode | Full daily pipeline via `investments/equity/prompt/main.md` compatibility entrypoint |
| Data mode | DELAYED |
| State transitions | PRECHECK -> REFLECTION -> DATA_OK -> SCORED -> PORTFOLIO_DRAFT -> RISK_REVIEW -> PUBLISHED -> CLOSE_LOGGED -> EVOLUTION_REVIEW |
| Status target | GO if risk constraints pass; otherwise NO_TRADE |
| Final status | NO_TRADE |
| Agents executed | Orchestrator, Data/Regime, Factor Scoring, Portfolio Construction, Risk Committee, Evolution |
| Reflection baseline | `investments/equity/output/claude-opus-4-7-2026-05-12` |
| Baseline flag | CROSS_MODEL_BASELINE |
| Prediction settlement summary | 0 settled; no `OPEN` prediction target_date <= 2026-06-15 |
| Core ETF Market Forecast Block | Present for SPY, QQQ, SOXX |
| Outstanding blockers | protected NAV beta band; max capped investable NAV beta is below 0.90 |

## Source Ledger Coverage Counts

| Claim Type | Count |
|---|---:|
| OBSERVED | 90 |
| DERIVED | 132 |
| INFERRED | 0 |
| ILLUSTRATIVE | 0 |
| UNAVAILABLE | 0 |

## GO-Gate Table

| Required Input | Status | Evidence | Blocks GO? |
|---|---|---|---|
| Grounded entry price | PASS | Yahoo chart prices cross-checked with Nasdaq quotes for 42 equities plus 3 ETFs; max diff 0.05%. | No |
| ~60 trading days history for names and SPY | PASS | Yahoo daily chart rows >= 61 for all sampled names and ETFs. | No |
| Sigma via fallback chain | PASS | `REALIZED_VOL_30D` computed for every ranked/monitor name and ETF. | No |
| Next earnings date | PASS | Nasdaq prior report date + 91d cadence estimate, tagged `ESTIMATED (+/-5d)`. | No |
| Sampled universe protocol | PASS | 42-name deterministic sampled universe across all 11 GICS sectors. | No |

## Enhancing Inputs Missing

Options IV/skew, short-interest/borrow, bid-ask tape, analyst-revision tape, institutional ownership flow, and a full-universe percentile feed are not wired. Treatment: confidence capped at `MEDIUM`, gross exposure capped, but these inputs do not block `GO` by themselves.

## Artifact Checklist

| Artifact | Status |
|---|---|
| 00_run_manifest.md | present |
| 01_preflight.md | present |
| 02_reflection.md | present |
| 03_regime_and_data.md | present |
| 04_universe_summary.md | present |
| 05_factor_scores.md | present |
| 06_top_candidates.md | present |
| 07_portfolio_proposal.md | present |
| 08_risk_review.md | present |
| 09_final_report.md | present |
| 10_midday_monitor.md | present |
| 11_preclose_check.md | present |
| 12_close_log.md | present |
| 13_evolution_log.md | present |
| 15_predictions.json | present |
