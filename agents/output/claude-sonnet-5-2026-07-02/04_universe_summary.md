# 04 Universe Summary

## Index-Union Universe (theoretical candidate list)

Per `universe_summary.json`:

| Metric | Value |
| --- | --- |
| S&P 500 count | 503 |
| Nasdaq-100 count | 101 |
| Overlap count | 89 |
| Union count | 515 |
| SP500 cache fetched_at | 2026-06-21T21:05:56Z |
| Nasdaq100 cache fetched_at | 2026-06-21T21:05:56Z |
| Generated at (this run) | 2026-07-02T12:03:29Z |

`build_index_universe.py` succeeded without error. `eligible_universe.txt` (515 tickers) is published and retained as the theoretical scan universe.

## Sampled Universe Protocol Disclosure (Emergency Fallback, Actually Used for Scoring)

Price-history fetch for the full 515-name union was not achievable this session (Yahoo Finance egress blocked by organizational policy; IBKR MCP per-name fetch for 515 names is outside the practical tool-call budget). See `03_regime_and_data.md § Universe Handoff` and `01_preflight.md § Data-Source Disclosure` for the full evidentiary trail.

**Sampling rule applied** (`rules.md § Sampled Universe Protocol`):

1. Carry-forward names from `02_reflection.md` (cross-model baseline monitoring list, non-binding since the baseline had no ledger, but used as a valid starting sample per protocol step 1): `AZO`, `UNH`, `MCK`, `JPM`, `XOM`, `CAT`, `WMT`, `ABBV`, `GS`, `PG` (10 names).
2. 2–3 largest liquid S&P 500 constituents per each of the 11 GICS sectors: `AAPL`/`MSFT`/`NVDA` (Technology), `LLY` (Health Care, in addition to `UNH`/`ABBV` above), `GOOGL`/`META`/`NFLX` (Communication Services), `AMZN`/`HD`/`TSLA` (Consumer Discretionary), `COST` (Consumer Staples, in addition to `WMT`/`PG`), `CVX` (Energy, in addition to `XOM`), `HON` (Industrials, in addition to `CAT`), `NEE` (Utilities), `PLD` (Real Estate), `LIN` (Materials), plus `BAC`/`V`-tier Financials already covered by `JPM`/`GS` above (20 names).
3. Current theme-watchlist names with a stated catalyst: `AVGO`, `MU`, `AMD` (AI/semiconductor capex cycle — the single largest driver of this month's tape per `03_regime_and_data.md`), `PLTR` (AI-software theme) — counted within the sector allocation above, not additive.
4. **Total: 30 names**, meeting the Sampled Universe Protocol's minimum-30 requirement. All 30 have grounded IBKR 5-year daily price history (1,253 bars each) and pass the inclusion filters below on inspection (all are large, liquid, long-listed U.S. primary-exchange names).

Every percentile in `05_factor_scores.md` is labeled `SAMPLED_PCTL (n=30)`.

## Inclusion / Exclusion Filters

Applied qualitatively to the 30 sampled names (no automated screen was run against market cap / ADV / spread data, since that data was not separately fetched for this sample — all 30 are S&P 500 or Nasdaq-100 mega/large-caps that self-evidently clear the `> $2B market cap`, `> $20M ADV`, `> $5 price`, `> 6 months listed` thresholds in `rules.md § Universe Construction`). No name was excluded from the sample. This is disclosed as a qualitative pass, not a quantitative filter run, and is a coverage gap relative to the full index-union protocol.

## Rejection Log

No names were rejected from the 30-name sample — all 30 remained in the scored set. The **515-name index-union universe minus the 30 sampled names (485 names)** were not scored this run at all, for the data-access reasons above, not for failing an inclusion/exclusion filter. This is a universe-breadth gap, not a rejection.

## Metric Coverage Summary

| `rules.md § Financial Metrics and Score Attribution` input | Sourceable this run? | Coverage | Effect |
| --- | --- | --- | --- |
| Fundamental (earnings-revision momentum, revenue accel, margin trend, FCF yield, ROIC/ROE, leverage, valuation) | **No** | 0 / 30 | Family `UNAVAILABLE`; `Fund_Z` = `0.00 (UNAVAILABLE)`; does not count toward 3-of-4 threshold |
| Technical / Price (momentum, RS vs SPY, MA alignment, TD-9, RSI, MACD, volume ratio) | **Yes** | 30 / 30 | Family sourceable; `Tech_Z` computed |
| Sentiment / Positioning (short interest, options skew, analyst revisions, insider buying, institutional flow) | **No** | 0 / 30 | Family `UNAVAILABLE`; `Sent_Z` = `0.00 (UNAVAILABLE)`; does not count toward 3-of-4 threshold |
| Macro / Regime (60d beta, sector-rotation leadership, rate sensitivity, VIX regime, DXY/oil/credit) | **Partial — 2 of 5 menu items** | 30 / 30 for the 2 sourced sub-metrics (beta, correlation-to-SPY) | Family sourceable via 2 metrics (meets the ≥2-sourceable-metrics rule); `Macro_Z` computed from beta-deviation and correlation-to-SPY only — rate sensitivity, VIX-regime cross-sectional discriminant, and DXY/oil/credit residuals are not sourced per name |
| Risk/return ratios (Sharpe, Sortino, IR, Treynor, Calmar) | **No — blocked upstream** | 0 / 30 | Cannot be computed without a risk-free rate source and a settled `mu`/beta pairing beyond what's disclosed; marked `UNAVAILABLE` in `05_factor_scores.md`, not guessed |
| Tail risk (VaR95, CVaR95, 60d max drawdown) | **Max drawdown: Yes. VaR/CVaR: parametric only** | 30 / 30 (drawdown); 30/30 (parametric VaR/CVaR from mu/sigma, disclosed as parametric) | Max drawdown `DERIVED` from fetched history; VaR95/CVaR95 computed parametrically per `rules.md` formulas once mu/sigma exist (monitoring sleeve only) |
| Sizing (Raw Kelly, 0.25×Kelly) | **Monitoring sleeve only** | 12 / 30 (only names carrying mu/sigma) | See `05_factor_scores.md`/`07_portfolio_proposal.md` |
| Technical indicator pack (TD-9, RSI, MACD daily/weekly/monthly, MA, momentum, volume, RS) | **Yes** | 30 / 30 | Full coverage via `technical_indicators.json` |

**Technical indicator coverage detail** (daily / weekly / monthly, all from `technical_indicators.json`):

- TD-9 setup counts: 30/30/30 sourceable (100% each timeframe).
- RSI(14): 30/30/30 sourceable.
- MACD(12,26,9) state: 30/30/30 sourceable.
- MA alignment (20/50): 30/30/30 sourceable.
- 20/60-bar momentum: 30/30 (daily); weekly/monthly momentum keys present but not separately tabulated in `05` (daily is the primary scoring input; weekly/monthly TD-9/RSI/MACD states are shown as diagnostics).
- 20-bar volume ratio: 30/30 sourceable (daily).
- Relative strength vs SPY (20d/60d): 30/30 sourceable.

Since Fundamental and Sentiment are `UNAVAILABLE` for 100% of the sampled universe (0% ≥ the 70% sourceability bar), neither family may contribute to `Adj Score` per `rules.md § Financial Metrics and Score Attribution`; this is a `GO`-eligibility-affecting gap, not merely a data-quality cap, because it structurally blocks every name from meeting the "3 of 4 factor families non-negative" Evidence Threshold. See `05_factor_scores.md` and `08_risk_review.md`.
