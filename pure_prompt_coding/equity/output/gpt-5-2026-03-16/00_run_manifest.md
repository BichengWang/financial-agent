# Quantitative Equity Research Run Manifest

**Date:** 2026-03-16
**Run Time:** 2026-03-16 17:52:29 PDT / 20:52:29 ET
**Run Mode:** Manual prompt execution
**Top-Level Status Target:** `REVIEW_ONLY`
**Data Mode:** `MIXED (LIVE benchmark/price data + DELAYED earnings calendar inputs + ILLUSTRATIVE portfolio risk inputs)`
**State Machine:** `PRECHECK -> DATA_OK -> SCORED -> REVIEW_ONLY -> PUBLISHED -> CLOSE_LOGGED -> EVOLUTION_REVIEW`

## Agents Executed

1. Orchestrator
2. Data and Regime Agent
3. Factor Scoring Agent
4. Portfolio Construction Agent
5. Risk Committee Agent
6. Evolution Agent

## Current Orchestrator Decision

- `PRECHECK`: complete
- `DATA_OK`: complete, but only for a sampled liquid large-cap research universe
- `SCORED`: complete
- `PORTFOLIO_DRAFT`: not approved for live execution
- `RISK_REVIEW`: complete
- `FINAL STATUS`: `REVIEW_ONLY`

## Blocking Issues

1. No full eligible U.S. universe screen was completed; this run uses a 16-name liquid large-cap research subset.
2. Portfolio-level beta, pairwise correlation, and 30-day realized volatility were not fully sourced from a validated feed.
3. Some earnings dates are confirmed by official webcast pages, but others remain estimated or unconfirmed.
4. Because of 1-3, the run is suitable for ranking and scenario analysis, not live sizing.

## Data Lineage Summary

- **LIVE:** `SPY`, `QQQ`, `DIA`, sector ETFs, and sampled security prices from finance snapshots captured around 2026-03-17 00:15 UTC.
- **DELAYED:** earnings timing inputs from official webcast pages where available and third-party calendars where not.
- **ILLUSTRATIVE:** portfolio covariance, beta, tracking-error, and drawdown estimates.

## Output Checklist

- `00_run_manifest.md`: complete
- `01_preflight.md`: complete
- `02_regime_and_data.md`: complete
- `03_universe_summary.md`: complete
- `04_factor_scores.md`: complete
- `05_top_candidates.md`: complete
- `06_portfolio_proposal.md`: complete
- `07_risk_review.md`: complete
- `08_final_report.md`: complete
- `09_midday_monitor.md`: complete
- `10_preclose_check.md`: complete
- `11_close_log.md`: complete
- `12_evolution_log.md`: complete

## Notes

This run follows the prompt system in `/Users/mac/my-code/diary/investments/equity/prompt/`, but the prompt-relative references in `main.md` point to non-existent sibling folders. Execution used the actual files under `/Users/mac/my-code/diary/investments/equity/prompt/`.
