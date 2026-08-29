# 04 — Universe Summary · 2026-08-28

## Construction

The normal index-union path succeeded (L001): S&P 500 503,
Nasdaq-100 101, overlap 89, union
515. Caches were fetched 2026-06-21T21:05:56Z. Core ETFs are
outside the candidate universe.

- Input union: 515
- Scoreable before MoM binding: 507
- Binding MoM DROP exclusions: AAPL, AON, AWK, CTAS, PCG, RTX, SYK
- Final scored cross-section: 500
- Published monitoring names: 20; investable: 0

## Inclusion / exclusion log

| Ticker | Reason | Detail |
|---|---|---|
| AWK | MOM_BASELINE_DROP | 2026-07-30 baseline forecast produced non-positive alpha or lower-CI breach; no stronger new ledger evidence |
| AON | MOM_BASELINE_DROP | 2026-07-30 baseline forecast produced non-positive alpha or lower-CI breach; no stronger new ledger evidence |
| AAPL | MOM_BASELINE_DROP | 2026-07-30 baseline forecast produced non-positive alpha or lower-CI breach; no stronger new ledger evidence |
| AVB | STALE_LAST_BAR | last bar 2026-08-14 != basis 2026-08-28; possible corporate action |
| BRK-B | MARKET_CAP_UNAVAILABLE | Nasdaq screener marketCap absent |
| BF-B | MARKET_CAP_UNAVAILABLE | Nasdaq screener marketCap absent |
| CTAS | MOM_BASELINE_DROP | 2026-07-30 baseline forecast produced non-positive alpha or lower-CI breach; no stronger new ledger evidence |
| EA | STALE_LAST_BAR | last bar 2026-08-04 != basis 2026-08-28; possible corporate action |
| EQR | NO_PRICE_HISTORY | HTTPError: HTTP Error 400: Bad Request |
| FDXF | LISTING_AGE_UNDER_6M | 65 daily bars (<126); first bar 2026-05-28 |
| PCG | MOM_BASELINE_DROP | 2026-07-30 baseline forecast produced non-positive alpha or lower-CI breach; no stronger new ledger evidence |
| Q | INDICATOR_INCOMPLETE | daily/weekly MA alignment UNAVAILABLE |
| RTX | MOM_BASELINE_DROP | 2026-07-30 baseline forecast produced non-positive alpha or lower-CI breach; no stronger new ledger evidence |
| SYK | MOM_BASELINE_DROP | 2026-07-30 baseline forecast produced non-positive alpha or lower-CI breach; no stronger new ledger evidence |
| TRI | STALE_LAST_BAR | last bar 2026-08-27 != basis 2026-08-28; possible corporate action |

## Metric coverage

| Metric group | Sourceable | UNAVAILABLE | Effect |
|---|---:|---:|---|
| Price/history/liquidity | 500 | 0 final scored | Required gates pass |
| Earnings date or completed no-print sweep | 500 | 0 | Required gate passes |
| Technical/price family | 500 | 0 | Available; 66.7% of live family conviction |
| Macro/regime family | 500 | 0 | Available |
| Fundamental family | 0 | 500 | DQ reduced; confidence capped |
| Sentiment/positioning family | 0 | 500 | DQ reduced; confidence capped |

Daily/weekly/monthly TD-9, RSI(14), MACD(12,26,9), MA alignment and momentum are complete for every
published row. Relative strength is computed D/W/M against SPY where defined; daily RS20/RS60 is
persisted below. Volume confirmation is represented by the sourceable 20-day price/volume history.
Missing factor families are never treated as neutral or supportive.

Published sector counts: Basic Materials=1, Consumer Discretionary=2, Consumer Staples=1, Finance=5, Health Care=5, Industrials=2, Technology=4.
