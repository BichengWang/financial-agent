```text
══════════════════════════════════════════════════════
QUANTITATIVE EQUITY SELECTION REPORT — 2026-06-11
Run Status: NO_TRADE
Classification: INTERNAL — INVESTMENT COMMITTEE USE
══════════════════════════════════════════════════════
```

## Executive Summary

The run completed with `DELAYED` data and a 42-name sampled universe. Required inputs are grounded for all ranked names: quote cross-checks, 60-day histories, realized-vol sigma, earnings dates, and SPY benchmark price. The best research candidates are led by LLY, CVX, UNH, ABBV, BAC, JNJ, ANET, and AMT, but no live portfolio is approved because the investable-grade long set cannot meet the protected 0.90-1.10 NAV beta band under 5% single-name caps. The final status is `NO_TRADE`; 17 settleable paper forecasts are published for future calibration.

## MoM Reflection Summary

Baseline: `claude-opus-4-7-2026-05-12`, flagged `CROSS_MODEL_BASELINE` and illustrative. Its top names had no grounded prior prices, so MoM alpha scoring is `UNAVAILABLE`; current ledger rows drive today’s ranking instead. No prior prediction record is due for settlement until 2026-07-08.

## Regime Table

| Regime | Data Quality | Key Macro Risk |
|---|---|---|
| HIGH_VOL with RATE_SHOCK overlay | DELAYED; required inputs grounded; enhancing feeds missing | VIX near 19.78 and `^TNX` 4.467; confidence capped without options/short-interest feeds |

## Ranked Candidates

| Rank | Ticker | Entry | Pctl | mu | sigma | Target | CI70 | Sleeve |
|---:|---|---:|---:|---:|---:|---:|---|---|
| 1 | LLY | 1163.72 | 100.0 | 6.0% | 11.9% | 1233.54 | 1089.16-1377.92 | INVESTABLE_GRADE |
| 2 | CVX | 188.14 | 97.6 | 6.0% | 7.4% | 199.43 | 184.91-213.95 | INVESTABLE_GRADE |
| 3 | UNH | 406.33 | 95.2 | 6.0% | 7.5% | 430.71 | 398.91-462.51 | INVESTABLE_GRADE |
| 4 | ABBV | 226.96 | 92.9 | 5.0% | 7.1% | 238.30 | 221.46-255.14 | INVESTABLE_GRADE |
| 5 | GOOGL | 353.82 | 90.5 | 5.0% | 11.7% | 371.51 | 328.60-414.42 | MONITOR |
| 6 | BAC | 55.11 | 88.1 | 4.0% | 6.4% | 57.31 | 53.67-60.96 | INVESTABLE_GRADE |
| 7 | JNJ | 239.59 | 85.7 | 4.0% | 5.7% | 249.18 | 234.99-263.37 | INVESTABLE_GRADE |
| 8 | ANET | 155.37 | 83.3 | 3.0% | 18.9% | 160.03 | 129.51-190.55 | INVESTABLE_GRADE |
| 9 | AMT | 190.50 | 81.0 | 3.0% | 8.7% | 196.21 | 178.95-213.47 | INVESTABLE_GRADE |
| 10 | MCK | 791.80 | 78.6 | 2.0% | 8.9% | 807.64 | 734.41-880.86 | MONITOR |
| 11 | GS | 1024.62 | 76.2 | 2.0% | 10.2% | 1045.11 | 936.36-1153.87 | MONITOR |
| 12 | KO | 83.39 | 73.8 | 2.0% | 5.8% | 85.05 | 80.02-90.09 | MONITOR |
| 13 | GE | 328.94 | 71.4 | 2.0% | 11.2% | 335.52 | 297.08-373.96 | MONITOR |
| 14 | JPM | 313.91 | 69.0 | 1.0% | 6.4% | 317.05 | 296.17-337.93 | MONITOR |
| 15 | ORCL | 182.33 | 66.7 | 1.0% | 20.1% | 184.15 | 146.09-222.22 | MONITOR |
| 16 | PG | 149.34 | 64.3 | 1.0% | 7.2% | 150.83 | 139.71-161.95 | MONITOR |
| 17 | COP | 117.31 | 61.9 | 1.0% | 8.8% | 118.49 | 107.69-129.28 | MONITOR |

## Portfolio Analytics / No-Trade Rationale

The rejected equal 5% sleeve has normalized beta 0.391, average pairwise correlation 0.120, and parametric 95% one-month drawdown 2.91%. The binding issue is beta: maximum NAV beta from positive-beta investable-grade names at the single-name cap is only 0.199, versus the required 0.90-1.10 band. Sector concentration also fails for Health Care in the equal sleeve.

## Assumptions and Limitations

- Quote data are delayed/current web endpoint observations, not a brokerage feed.
- Full-universe screening, options IV/skew, short interest, borrow, and institutional flow are not wired.
- Percentiles are sampled percentiles, not full-market percentiles.
- `NO_TRADE` is a portfolio-construction result, not a data-integrity halt.

## Next Scheduled Review

Next full run: 2026-06-12 pre-open if manually triggered or if the scheduler is recreated. First known prediction settlement date in this workspace: 2026-07-08.
