# 00 Run Manifest

- Date: 2026-06-09
- Run timestamp: 2026-06-09 11:59:17 PDT / 14:59:17 EDT
- Model: gpt-5
- Run mode: MANUAL_AUTOMATION
- Data mode: DELAYED_PARTIAL
- Top-level status target: REVIEW_ONLY
- Final publication status: REVIEW_ONLY
- Output folder: `investments/equity/output/gpt-5-2026-06-09/`

## Reflection Baseline

- Baseline path: `/Users/mac/my-code/diary/investments/equity/output/claude-opus-4-7-2026-05-12/`
- Baseline flag: `CROSS_MODEL_BASELINE`
- Selection rule: no same-model `gpt-5` package exists in the MoM candidate window of 2026-04-25 through 2026-05-19; the closest in-window cross-model package is 2026-05-12.
- Short-window cross-checks explicitly not used for MoM binding decisions: `gpt-5-2026-05-29`, `gpt-5-2026-06-07`.

## State Trace

`PRECHECK -> REFLECTION -> DATA_OK(DELAYED_PARTIAL) -> SCORED(REVIEW_ONLY_MONITORS) -> PORTFOLIO_DRAFT(PAPER_REVIEW_ONLY) -> RISK_REVIEW(REJECT_GO) -> PUBLISHED(REVIEW_ONLY) -> CLOSE_LOGGED(PENDING_CLOSE) -> EVOLUTION_REVIEW(NO_CHANGE_ACCEPTED)`

## Agents Executed

1. Orchestrator and source-ledger preflight.
2. Reflection stage.
3. Data and regime agent.
4. Factor scoring agent.
5. Portfolio construction agent.
6. Risk committee agent.
7. Evolution agent.

## Source Ledger Coverage Summary

| Claim Type | Count | Notes |
|---|---:|---|
| OBSERVED | 70 | Delayed/current quotes, historical prices, beta, fundamentals, consensus targets, earnings-date fields, market/regime indicators. |
| DERIVED | 5 | MoM returns only, computed from ledger-backed prior/current prices. |
| INFERRED | 8 | Review-only factor scores, explicitly not trade forecasts. |
| ILLUSTRATIVE | 0 | No illustrative rows used in this run. |
| UNAVAILABLE | 4 | Options IV/skew, complete short-interest feed, execution spread/liquidity, and covariance/drawdown feed. |

## Critical Field Status

| Field | Status | Run Impact |
|---|---|---|
| Current prices for sampled tickers | Available with delayed/current web tags | Permits review-only monitoring. |
| Prior MoM prices for baseline top 5 | Available from historical web pages | Permits reflection. |
| Benchmark/vol/rates context | Partially available | Regime label is usable but confidence capped. |
| Full U.S. equity universe screen | Unavailable | Blocks `GO`. |
| Options IV/skew | Unavailable | Blocks `GO`; sigma and CI fields unavailable. |
| Short-interest / borrow coverage | Incomplete | Blocks `GO`. |
| Execution-quality liquidity / bid-ask spread | Unavailable | Blocks `GO`. |
| Validated covariance / drawdown model | Unavailable | Blocks `GO`. |

## Eligibility Decision

This run is eligible for `REVIEW_ONLY` only. It is not eligible for `GO` because several protected risk and evidence inputs are unavailable. It is not `HALTED` because source lineage for used facts is explicit, missing critical fields are labeled `UNAVAILABLE`, and no live recommendation is made.

## Artifact Checklist

| Artifact | Status |
|---|---|
| `00_run_manifest.md` | Complete |
| `01_preflight.md` | Complete |
| `02_reflection.md` | Complete |
| `03_regime_and_data.md` | Complete |
| `04_universe_summary.md` | Complete |
| `05_factor_scores.md` | Complete |
| `06_top_candidates.md` | Complete |
| `07_portfolio_proposal.md` | Complete |
| `08_risk_review.md` | Complete |
| `09_final_report.md` | Complete |
| `10_midday_monitor.md` | Complete |
| `11_preclose_check.md` | Pending scheduled checkpoint |
| `12_close_log.md` | Pending close |
| `13_evolution_log.md` | Complete |
