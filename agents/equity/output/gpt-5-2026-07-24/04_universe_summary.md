# 04 Universe Summary — 2026-07-24

## Construction

`build_index_universe.py` materialized the cached S&P 500 ∪ Nasdaq-100 union: 503 S&P names + 101 Nasdaq-100 names - 89 overlaps = **515**. Cache vintage: 2026-06-21T21:05:56Z (L001). No sampled fallback was used.

## Inclusion / exclusion

- 515/515 index-union names passed the >$2B market-cap filter; the smallest was CAG at $7.07B (L004).
- FDXF returned 41 completed bars and was excluded. The other 514 equities passed the 60-bar analytical minimum (L002,L003).
- 3 names (BRK-B, FDX, FER) remained without a sourceable next earnings date after both attempts and were excluded before scoring. The other 511 names have confirmed or cadence-estimated dates (L008).
- WAB is retained: its completed 2026-07-24 Yahoo/Nasdaq close comparison now passes the 1% gate in the published-price manifest (L190).
- All 511 retained names have >$5 last close, >$20M 20-day dollar volume, and >$2B market cap. Listing-age/session coverage follows from the >=60-bar history gate and index-union membership; current bid-ask tape remains Enhancing and unavailable (L009).

## Metric coverage

| Metric group | Sourceable | UNAVAILABLE | Effect |
|---|---:|---:|---|
| Price / 60d risk / return | 511 | 0 | full Technical/Macro compute |
| Market-cap eligibility | 515 | 0 | all raw index-union names pass >$2B; current-run Nasdaq screener plus BF-B fallback |
| TD-9 daily / weekly / monthly | 517 / 517 / 517 | 1 / 1 / 1 | exact field-level coverage; FDXF never imputed |
| RSI(14) daily / weekly / monthly | 517 / 517 / 516 | 1 / 1 / 2 | sparse monthly history remains explicit |
| MACD(12,26,9) daily / weekly / monthly | 517 / 517 / 512 | 1 / 1 / 6 | state/histogram availability follows minimum bars |
| MA alignment daily / weekly / monthly | 517 / 516 / 509 | 1 / 2 / 9 | requires both 20- and 50-period averages |
| Momentum 20-period daily / weekly / monthly | 517 / 517 / 515 | 1 / 1 / 3 | exact field-level coverage |
| Momentum 60-period daily / weekly / monthly | 517 / 516 / 508 | 1 / 2 / 10 | younger listings remain UNAVAILABLE |
| Volume ratio daily / weekly / monthly | 517 / 517 / 515 | 1 / 1 / 3 | 20-period values |
| SPY relative strength 20-period D/W/M | 517 / 517 / 515 | 1 / 1 / 3 | exact field-level coverage |
| SPY relative strength 60-period D/W/M | 517 / 516 / 508 | 1 / 2 / 10 | younger listings remain UNAVAILABLE |
| Earnings event screen | 511 scoreable names | 3 excluded names | 380 confirmed; 131 estimated ±5d across 514 attempted names |
| Fundamental | 0 production | 511 | family unavailable; DQ 0.80 |
| Sentiment | 0 production | 511 | family unavailable; DQ 0.80 |
| Options/borrow/bid-ask/ownership | 0 | all | Enhancing-only confidence cap |

Every percentile is `INDEX_UNION_PCTL (n=511)`. Daily scoring inputs are sourceable for all 511 scoreable equities. Sparse weekly/monthly subfields for younger listings are not imputed and are counted explicitly above; every displayed field for the 26-name published sleeve is sourceable (L003).
