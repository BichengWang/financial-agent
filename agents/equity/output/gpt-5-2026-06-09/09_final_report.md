# Quantitative Equity Selection Report - 2026-06-09

Run Status: `REVIEW_ONLY`  
Data Status: `DELAYED_PARTIAL`  
Classification: Internal research, not a live trade recommendation

## Executive Summary

The pipeline produced a complete dated package and a source-backed review-only monitor list. No `GO` portfolio is approved because the run lacks full-universe screening plus options IV/skew, complete short-interest/borrow, execution-quality liquidity, and covariance/drawdown feeds.

Top review-only monitors: `MCK`, `PG`, `WMT`, `ABBV`, `JPM`, `XOM`, `AZO`, `UNH`.

## MoM Reflection Summary

The required MoM baseline is `/Users/mac/my-code/diary/investments/equity/output/claude-opus-4-7-2026-05-12/`, flagged `CROSS_MODEL_BASELINE`. That run was `REVIEW_ONLY` and illustrative. Its top-5 illustrative names all produced negative MoM price behavior through the current source-backed sample:

| Ticker | MoM Return | Decision |
|---|---:|---|
| MSFT | -0.86% | DOWNGRADE |
| NVDA | -6.31% | DROP |
| META | -2.22% | DOWNGRADE |
| GOOGL | -5.53% | DROP |
| AMZN | -7.77% | DROP |

The reflection downgrades mega-cap AI/growth for the 2-6 week window and promotes defensive healthcare/staples monitoring.

## Regime Assessment

Current review label: `HIGH_VOL / RATE_SHOCK`.

Evidence: VIX 19.55 and prior close 18.92 from Cboe (L001-L002), DGS10 4.55% from FRED (L003), SPY -0.55% with XLV +1.48% and XLP +1.00% in the sampled session (L004-L006).

## Candidate Table

| Rank | Ticker | Sector | Entry Price | Beta | Adj Score | Status |
|---:|---|---|---:|---:|---:|---|
| 1 | MCK | Healthcare | 783.75 | 0.32 | 0.74 | Review-only monitor |
| 2 | PG | Consumer Staples | 148.30 | 0.38 | 0.72 | Review-only monitor |
| 3 | WMT | Consumer Staples | 118.61 | 0.60 | 0.69 | Review-only monitor |
| 4 | ABBV | Healthcare | 226.43 | 0.31 | 0.68 | Review-only monitor |
| 5 | JPM | Financials | 312.82 | 1.00 | 0.65 | Review-only monitor |
| 6 | XOM | Energy | 148.73 | 0.15 | 0.62 | Review-only monitor |
| 7 | AZO | Consumer Discretionary | 3125.82 | 0.35 | 0.59 | Review-only monitor |
| 8 | UNH | Healthcare | 412.50 | 0.65 | 0.56 | Review-only monitor |

## Portfolio Analytics

No live portfolio. A paper monitoring sleeve is included in `07_portfolio_proposal.md` for process tracking only. It is not beta-compliant for `GO`, and drawdown/correlation are unavailable.

## Assumptions and Limitations

- Candidate pages are delayed/current web observations, not an institutional market-data feed.
- The full U.S. universe was not screened.
- No IV30, skew, complete short-interest, bid-ask, covariance, or 95th percentile drawdown inputs are wired.
- All target price, `mu`, sigma, and CI fields remain `N/A` where inputs are unavailable.

## Next Scheduled Review

- 15:45 ET: pre-close check if a live operator requests it.
- 16:20 ET: close log once closing prices are source-backed.
- Next automation run: next scheduled weekday pre-open cycle.
