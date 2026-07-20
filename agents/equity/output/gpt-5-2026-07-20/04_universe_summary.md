# 04 Universe Summary — 2026-07-20

## Construction

The deterministic S&P 500 ∪ Nasdaq-100 caches contain 503 + 101 − 89 overlaps = **515 names** (L001). Cache vintage is 2026-06-21 and is disclosed under the stale-cache rule. Core ETFs are isolated from equity ranks.

## Inclusion / exclusion log

| Filter | Threshold | Result |
|---|---|---|
| Listing / market cap | U.S. primary; >$2B | index membership proxy, disclosed as INFERRED |
| Price | >$5 | applied to completed 07-17 close |
| 20d dollar volume | >$20M | applied to current-run history |
| Listing age | >6 months; ≥126 bars | applied |
| Halts / ambiguity | none unresolved | no propagated ambiguity |

Eligible universe: **513**. Rejections: `{'FDXF': 'fewer than 60 completed bars', 'SATS': 'fewer than 60 completed bars'}`. Percentiles are `INDEX_UNION_PCTL (n=513)`; emergency sampling was not used.

## Metric coverage

| Metric group | Sourceable | UNAVAILABLE | Effect |
|---|---:|---:|---|
| Completed price histories / risk pack | 513/513 | 0 | beta, sigma, TE, drawdown, Treynor and Calmar-style diagnostics computed where denominator is meaningful |
| Technical records D/W/M | 516/518 | 2 (SATS, FDXF) | unavailable records excluded |
| Monthly MA50 | 508/516 OK records | 8 | diagnostic gaps only |
| Earnings preflight | 77/77 | 0 | buffered penalty inputs |
| Fundamental family | 0/513 | 513 | SHADOW only; contribution 0.00, DQ reduction |
| Sentiment family | 0/513 | 513 | same |

### Technical coverage by timeframe

| Indicator | Daily sourceable | Weekly sourceable | Monthly sourceable | UNAVAILABLE D/W/M | Effect |
|---|---:|---:|---:|---|---|
| TD-9 | 516/518 | 516/518 | 516/518 | 2/2/2 | never imputed |
| RSI(14) | 516/518 | 516/518 | 515/518 | 2/2/3 | never imputed |
| MACD(12,26,9) | 516/518 | 516/518 | 511/518 | 2/2/7 | never imputed |
| MA alignment | 516/518 | 515/518 | 508/518 | 2/3/10 | never imputed |
| Momentum 20/60 | 516/518 | 515/518 | 507/518 | 2/3/11 | never imputed |
| Volume ratio | 516/518 | 516/518 | 514/518 | 2/2/4 | never imputed |
| Relative strength 20/60 | 516/518 | 515/518 | 507/518 | 2/3/11 | never imputed |

All displayed TD-9, RSI, MACD, MA, momentum, volume-ratio, and SPY-relative-strength values come from `technical_indicators.json` built after provisional-bar exclusion (L003). Only Technical and Macro are sourceable, so every equity fails the three-of-four-family gate.
