# 09 Final Report

```text
══════════════════════════════════════════════════════
QUANTITATIVE EQUITY SELECTION REPORT — 2026-06-14
Run Status: NO_TRADE
Classification: INTERNAL — INVESTMENT COMMITTEE USE
══════════════════════════════════════════════════════
```

## Executive Summary

The run completed with `DELAYED` data: 42 equities plus SPY/QQQ/SOXX had cross-checked entry prices, 82 daily history rows, realized-vol sigma, and earnings cadence estimates where needed. The strongest research names are LLY, GE, BAC, GS, ANET, UNH, ABBV, and JPM. No trade is approved because the investable set cannot meet the protected 0.90-1.10 NAV beta band under the 5% single-name cap. The final status is `NO_TRADE`; 20 settleable forecasts are published for future calibration.

## MoM Reflection Summary

Baseline: `claude-opus-4-7-2026-05-12`, flagged `CROSS_MODEL_BASELINE`. It was an illustrative `REVIEW_ONLY` package with no grounded prior prices or prediction ledger, so MoM alpha scoring is `UNAVAILABLE`. No prior prediction record is due for settlement until 2026-07-08.

## Regime Table

| Regime | Data Quality | Key Macro Risk |
|---|---|---|
| NEUTRAL | DELAYED; required inputs grounded; enhancing feeds missing | SPY mixed versus 20d/50d trend; SOXX leadership is narrow and high-volatility |

## Core ETF Market Forecast

| ETF | Entry | mu | sigma | Target | CI70 | Confidence |
|---|---:|---:|---:|---:|---|---|
| SPY | 741.75 | 0.5% | 3.93% | 745.46 | 715.14-775.78 | MEDIUM |
| QQQ | 721.34 | 1.2% | 6.91% | 729.99 | 678.15-781.83 | MEDIUM |
| SOXX | 596.25 | 1.8% | 17.99% | 607.24 | 495.69-718.80 | MEDIUM |

## Ranked Candidates

| Rank | Ticker | Entry | Pctl | mu | sigma | Target | CI70 | Sleeve |
|---:|---|---:|---:|---:|---:|---:|---|---|
| 1 | AMD | 511.57 | 100.0 | 6.0% | 26.67% | 542.26 | 400.37-684.16 | MONITOR |
| 2 | LLY | 1133.00 | 97.6 | 6.0% | 9.15% | 1200.98 | 1093.16-1308.80 | INVESTABLE_GRADE |
| 3 | GE | 335.30 | 95.1 | 6.0% | 11.46% | 355.42 | 315.46-395.38 | INVESTABLE_GRADE |
| 4 | BAC | 56.02 | 92.7 | 5.0% | 6.44% | 58.82 | 55.07-62.57 | INVESTABLE_GRADE |
| 5 | GS | 1062.75 | 90.2 | 5.0% | 10.43% | 1115.89 | 1000.61-1231.17 | INVESTABLE_GRADE |
| 6 | ANET | 163.24 | 87.8 | 4.0% | 19.26% | 169.77 | 137.07-202.47 | INVESTABLE_GRADE |
| 7 | UNH | 408.52 | 85.4 | 4.0% | 7.53% | 424.86 | 392.87-456.85 | INVESTABLE_GRADE |
| 8 | ABBV | 227.73 | 82.9 | 3.0% | 6.18% | 234.56 | 219.93-249.20 | INVESTABLE_GRADE |
| 9 | JPM | 320.72 | 80.5 | 3.0% | 6.67% | 330.34 | 308.09-352.59 | INVESTABLE_GRADE |
| 10 | AMT | 187.18 | 78.0 | 2.0% | 8.63% | 190.92 | 174.12-207.72 | MONITOR |
| 11 | HD | 328.39 | 75.6 | 2.0% | 7.76% | 334.96 | 308.46-361.46 | MONITOR |
| 12 | CAT | 910.57 | 73.2 | 2.0% | 12.32% | 928.78 | 812.11-1045.45 | MONITOR |
| 13 | PLD | 148.74 | 70.7 | 2.0% | 6.09% | 151.71 | 142.29-161.14 | MONITOR |
| 14 | FCX | 68.41 | 68.3 | 1.0% | 16.57% | 69.09 | 57.31-80.88 | MONITOR |
| 15 | JNJ | 240.87 | 65.9 | 1.0% | 5.56% | 243.28 | 229.35-257.21 | MONITOR |
| 16 | PG | 149.61 | 63.4 | 1.0% | 7.03% | 151.11 | 140.17-162.04 | MONITOR |
| 17 | LIN | 523.57 | 61.0 | 1.0% | 6.16% | 528.81 | 495.26-562.35 | MONITOR |

## Portfolio Analytics / No-Trade Rationale

The max-weight investable basket has 40.0% gross exposure, estimated average pairwise correlation 0.253, and parametric 95% one-month drawdown 3.83%. The binding blocker is beta: maximum capped NAV beta is **0.384**, below the required 0.90-1.10 band. Repairing beta would require admitting sub-threshold high-beta names, which the rules prohibit.

## Assumptions and Limitations

- Data are delayed public endpoint observations, not a brokerage feed.
- Nasdaq quote timestamps showed one-session-stale labels while values matched Yahoo chart closes; this is disclosed in `01_preflight.md`.
- Full-universe screening, options IV/skew, short interest, borrow, bid-ask tape, and institutional flow are not wired.
- Percentiles are sampled percentiles, not full-market percentiles.
- `NO_TRADE` is a portfolio-construction result, not a data-integrity halt.

## Next Scheduled Review

No scheduler is active per the runbook. First known prediction settlement date in this workspace remains 2026-07-08.
