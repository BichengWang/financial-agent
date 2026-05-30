# Quantitative Equity Research Run Manifest

**Date:** 2026-05-29  
**Run Time:** 2026-05-29 09:30 PDT / 12:30 EDT  
**Run Mode:** Automation prompt execution  
**Top-Level Status Target:** `REVIEW_ONLY`  
**Data Mode:** `MIXED (delayed public quotes + public macro series + official company releases/search-indexed filings)`  
**State Machine:** `PRECHECK -> REFLECTION -> DATA_OK -> SCORED -> PORTFOLIO_DRAFT -> RISK_REVIEW -> PUBLISHED -> CLOSE_LOGGED -> EVOLUTION_REVIEW`

## Agents Executed

1. Orchestrator
2. Reflection stage
3. Data and Regime Agent
4. Factor Scoring Agent
5. Portfolio Construction Agent
6. Risk Committee Agent
7. Evolution Agent

## Current Orchestrator Decision

- `PRECHECK`: complete
- `REFLECTION`: complete; latest same-model baseline found at `gpt-5-2026-04-16`
- `DATA_OK`: complete for a sampled liquid large-cap research universe
- `SCORED`: complete on 28 U.S.-listed liquid names
- `PORTFOLIO_DRAFT`: completed as review-only monitoring sleeve
- `RISK_REVIEW`: complete
- `FINAL STATUS`: `REVIEW_ONLY`

## Prior-Month Reflection

**Baseline Package:** `/Users/mac/.codex/worktrees/ac9e/diary/investments/equity/output/gpt-5-2026-04-16/`

**Baseline Gap:** No exact 2026-04-29 same-model package exists in this workspace. The most recent same-model package, 2026-04-16, is used as the approximately one-month baseline.

**Prior Run Status:** `REVIEW_ONLY`

**Carry-Forward Decisions**

1. Carry `NVDA`, `GEV`, and `MSFT`; each validated with positive price follow-through and still-current company evidence.
2. Carry the AI infrastructure and power/electrification themes.
3. Keep `AVGO` on the watchlist but downgrade it for near-term June 3, 2026 earnings event risk.

**Downgrade / Removal Decisions**

1. Downgrade `META`; the stock posted negative MoM return despite still-valid advertising and AI-infrastructure fundamentals.
2. Do not promote `AVGO` into a live basket before the June 3 print without event-specific risk data.
3. Continue withholding `GO` because no validated beta, pairwise-correlation, or 95th-percentile drawdown feed is available.

## Blocking Issues

1. No full eligible U.S. universe screen was completed; the run uses a sampled 28-name liquid large-cap research set.
2. Portfolio beta, pairwise correlation, and drawdown estimates are not sourced from a validated risk engine.
3. Quote snapshots are public delayed/recent snapshots, not execution-grade synchronized market data.
4. Event risk remains meaningful: `AVGO` reports on June 3, 2026 and `ORCL` is expected to report in early June.

## Data Lineage Summary

- **DELAYED / PUBLIC QUOTES:** Stooq quote snapshots for `SPY`, `QQQ`, `IWM`, `DIA`, and sampled U.S. equities captured on 2026-05-29.
- **DELAYED / PUBLIC MACRO:** Cboe VIX history, FRED Treasury and credit series.
- **OFFICIAL / COMPANY:** NVIDIA, Broadcom, Meta, Microsoft, GE Vernova, Oracle, Palantir, Arista, Amazon, and Alphabet public releases or indexed filing pages.
- **N/A:** validated live bid/ask, IV30, short-interest deltas, beta, covariance, and drawdown model outputs.

## Output Checklist

- `00_run_manifest.md`: complete
- `01_preflight.md`: complete
- `02_reflection.md`: complete
- `03_regime_and_data.md`: complete
- `04_universe_summary.md`: complete
- `05_factor_scores.md`: complete
- `06_top_candidates.md`: complete
- `07_portfolio_proposal.md`: complete
- `08_risk_review.md`: complete
- `09_final_report.md`: complete
- `10_midday_monitor.md`: complete
- `11_preclose_check.md`: staged
- `12_close_log.md`: staged
- `13_evolution_log.md`: complete

## Source Set

- Stooq quote snapshots: `https://stooq.com/q/l/`
- Cboe VIX history: `https://cdn.cboe.com/api/global/us_indices/daily_prices/VIX_History.csv`
- FRED Treasury / credit series: `https://fred.stlouisfed.org/graph/fredgraph.csv`
- Federal Reserve FOMC calendar: `https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm`

