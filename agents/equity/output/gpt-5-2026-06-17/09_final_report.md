# 09 Final Report

```text
══════════════════════════════════════════════════════
QUANTITATIVE EQUITY SELECTION REPORT - 2026-06-17
Run Status: NO_TRADE
Classification: INTERNAL - INVESTMENT COMMITTEE USE
══════════════════════════════════════════════════════
```

## Executive Summary

The run completed with `DELAYED` data: 35 equities plus SPY/QQQ/SOXX had cross-checked entry prices, daily history, realized-vol sigma, liquidity, and earnings cadence estimates. The strongest investable-grade research names are GS, JPM, CAT, BAC, GE, GOOGL. No trade is approved because the investable set cannot meet the protected 0.90-1.10 NAV beta band under the 5% single-name cap and average pairwise correlation is above the 0.45 cap. The final status is `NO_TRADE`; 17 settleable forecasts are published for future calibration.

## MoM Reflection Summary

Baseline: `investments/equity/output/claude-opus-4-7-2026-05-24`, flagged `CROSS_MODEL_BASELINE`. It was an older cross-model package with no compatible prediction ledger, so MoM alpha scoring is `UNAVAILABLE`. No prior prediction record is due for settlement as of 2026-06-17.

## Regime Table

| Regime | Data Quality | Key Macro Risk |
| --- | --- | --- |
| BULL | DELAYED; required inputs grounded; enhancing feeds missing | Trend support remains conditional on beta and volatility discipline |

## Core ETF Market Forecast

| ETF | Entry | mu | sigma | Target | CI70 | Confidence |
| --- | --- | --- | --- | --- | --- | --- |
| SPY | 740.96 | +2.0% | 4.31% | 755.78 | 722.55-789.01 | MEDIUM |
| QQQ | 722.51 | +3.6% | 7.55% | 748.84 | 692.12-805.56 | MEDIUM |
| SOXX | 599.73 | +6.6% | 18.99% | 639.56 | 521.09-758.03 | MEDIUM |

## Ranked Candidates

| Rank | Ticker | Entry | Pctl | mu | sigma | Target | CI70 | Sleeve |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | GS | 1099.14 | 100.0 | +6.0% | 10.08% | 1165.09 | 1049.89-1280.28 | INVESTABLE_GRADE |
| 2 | FCX | 69.06 | 97.1 | +6.0% | 16.24% | 73.20 | 61.54-84.87 | MONITOR |
| 3 | JPM | 333.46 | 94.1 | +5.0% | 7.17% | 350.13 | 325.26-375.00 | INVESTABLE_GRADE |
| 4 | CAT | 955.92 | 91.2 | +5.0% | 12.14% | 1003.72 | 883.06-1124.37 | INVESTABLE_GRADE |
| 5 | BAC | 56.53 | 88.2 | +4.0% | 6.22% | 58.79 | 55.14-62.45 | INVESTABLE_GRADE |
| 6 | GE | 357.03 | 85.3 | +4.0% | 11.27% | 371.31 | 329.45-413.17 | INVESTABLE_GRADE |
| 7 | GOOGL | 363.79 | 82.4 | +3.0% | 8.53% | 374.70 | 342.42-406.98 | INVESTABLE_GRADE |
| 8 | LLY | 1112.00 | 79.4 | +2.0% | 8.97% | 1134.24 | 1030.53-1237.95 | MONITOR |
| 9 | UNH | 399.53 | 76.5 | +2.0% | 7.60% | 407.52 | 375.96-439.08 | MONITOR |
| 10 | ETN | 409.64 | 73.5 | +2.0% | 13.77% | 417.83 | 359.16-476.50 | MONITOR |
| 11 | HD | 327.48 | 70.6 | +2.0% | 7.66% | 334.03 | 307.95-360.11 | MONITOR |
| 12 | SO | 92.53 | 67.6 | +1.0% | 5.69% | 93.46 | 87.98-98.93 | MONITOR |
| 13 | AAPL | 295.95 | 64.7 | +1.0% | 6.36% | 298.91 | 279.33-318.49 | MONITOR |
| 14 | CVX | 177.58 | 61.8 | +1.0% | 7.94% | 179.36 | 164.69-194.02 | MONITOR |

## Portfolio Analytics / No-Trade Rationale

The max-weight investable basket has 30.0% gross exposure, estimated average pairwise correlation 0.499, and parametric 95% one-month drawdown 3.67%. The binding blockers are beta and correlation: maximum capped NAV beta is **0.378**, below the required 0.90-1.10 band, and average pairwise correlation is above the 0.45 cap. Repairing beta would require admitting sub-threshold high-beta names, which the rules prohibit.

## Assumptions and Limitations

- Data are public endpoint observations, not a brokerage feed.
- CNBC regular-close prices were cross-checked against Yahoo chart closes; all observed differences were within the 1% standard.
- Full-universe screening, options IV/skew, short interest, borrow, bid-ask tape, and institutional flow are not wired.
- Percentiles are sampled percentiles, not full-market percentiles.
- `NO_TRADE` is a portfolio-construction result, not a data-integrity halt.

## Next Scheduled Review

No scheduler is active per the runbook. First known prediction settlement date in this workspace is 2026-07-08.
