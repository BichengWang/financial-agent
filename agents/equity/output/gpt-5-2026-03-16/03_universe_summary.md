# Universe Summary

**Date:** 2026-03-16
**Universe Type:** Sampled liquid large-cap U.S. research subset
**Universe Status:** Valid for ranking, not for full cross-sectional deployment

## Inclusion Rules Applied

- U.S.-listed equities
- Price above $5
- Market cap clearly above $2B
- Intraday dollar volume comfortably above the strategy minimum based on sampled live volume

## Sample Universe

`NVDA`, `AVGO`, `META`, `GE`, `GEV`, `ETN`, `CRM`, `AMZN`, `MSFT`, `GOOGL`, `LRCX`, `ANET`, `GS`, `JPM`, `PANW`, `WMT`

## Universe Counts

| Item | Count |
| --- | ---: |
| Sample names reviewed | 16 |
| Hard-filter passes | 16 |
| Hard-filter rejects | 0 |
| Investable-on-sample basis | 5 |
| Near misses | 11 |

## Rejection Log

| Ticker | Reason |
| --- | --- |
| `GE` | Strong industrial trend, but lower immediate catalyst quality than `GEV` and `ETN` |
| `CRM` | Fresh earnings strength, but exact next earnings date not confirmed in-source |
| `LRCX` | Excellent technicals, but catalyst/evidence set thinner than top semi names |
| `AMZN` | Strong price action, but weaker discrete 30-day catalyst in sourced materials |
| `MSFT` | Quality compounder, but lower tactical edge on sampled evidence |
| `GOOGL` | Positive tape, but no stronger short-horizon catalyst than peers |
| `ANET` | Good AI-networking exposure, but less sourced event evidence |
| `GS` | Healthy financials tape, but weaker alpha case than industrial/AI leaders |
| `JPM` | Similar issue as `GS`; more beta-like than catalyst-rich |
| `PANW` | Price action lagged the leadership cohort |
| `WMT` | Defensive laggard on a risk-on day |

## Methodological Limitation

The prompt system asks for an eligible U.S. universe ranking. This run does not satisfy that standard. It ranks a high-liquidity research subset instead, which is enough for scenario analysis and monitoring, but not enough for a live `GO` decision.
