# 04 Universe Summary — 2026-07-22

## Construction

`build_index_universe.py` materialized the cached S&P 500 ∪ Nasdaq-100 union: 503 S&P names + 101 Nasdaq-100 names - 89 overlaps = **515**. Cache vintage: 2026-06-21T21:05:56Z (L001). No sampled fallback was used.

## Inclusion / exclusion

- 514 names passed the 60-completed-bar analytical minimum.
- SATS: fetched through the active Yahoo source symbol ECHO and retained under the canonical SATS universe identity.
- FDXF: 39 completed bars returned; excluded.
- All 514 retained names have >$5 last close and >$20M 20-day dollar volume in the fetched history. Listing-age/session-coverage requirements follow from the >=60-bar history gate; current bid-ask tape remains Enhancing and unavailable.

## Metric coverage

| Metric group | Sourceable | UNAVAILABLE | Effect |
|---|---:|---:|---|
| Price / 60d risk / return | 514 | 0 | full Technical/Macro compute |
| TD-9 daily / weekly / monthly | 517 / 517 / 517 | 1 / 1 / 1 | FDXF never imputed |
| RSI(14) daily / weekly / monthly | 517 / 517 / 517 | 1 / 1 / 1 | FDXF never imputed |
| MACD(12,26,9) daily / weekly / monthly | 517 / 517 / 517 | 1 / 1 / 1 | state and histogram sourceable |
| MA alignment daily / weekly / monthly | 517 / 517 / 517 | 1 / 1 / 1 | 20d/50d canonical pack |
| Momentum daily / weekly / monthly | 517 / 517 / 517 | 1 / 1 / 1 | 20/60-period values |
| Volume ratio daily / weekly / monthly | 517 / 517 / 517 | 1 / 1 / 1 | 20-period values |
| SPY relative strength daily / weekly / monthly | 517 / 517 / 517 | 1 / 1 / 1 | 20/60-period values |
| Earnings event screen | 109 selected/preselection names | 0 | 78 confirmed; 31 estimated ±5d |
| Fundamental | 0 production | 514 | family unavailable; DQ 0.80 |
| Sentiment | 0 production | 514 | family unavailable; DQ 0.80 |
| Options/borrow/bid-ask/ownership | 0 | all | Enhancing-only confidence cap |

Every percentile is `INDEX_UNION_PCTL (n=514)`. RSI, MACD, TD-9, MA alignment, momentum, volume ratio, and SPY-relative strength are sourceable on D/W/M for all 514 scoreable equities and the three ETFs (L003).
