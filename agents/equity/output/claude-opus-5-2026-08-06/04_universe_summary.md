# 04 — Universe Summary

## Construction

| Field | Value |
|---|---|
| Source | S&P 500 ∪ Nasdaq-100 constituent caches via `build_index_universe.py` |
| S&P 500 constituents | 503 |
| Nasdaq-100 constituents | 101 |
| Overlap | 89 |
| **Union** | **515** |
| S&P 500 cache `fetched_at` | `2026-06-21T21:05:56Z` |
| Nasdaq-100 cache `fetched_at` | `2026-06-21T21:05:56Z` |
| Cache age at run date | 46 days |
| Scored after filters | **511** |
| Rejected | 4 |
| Percentile label | `INDEX_UNION_PCTL (n=511)` |

The index-union helper **succeeded**, so the Sampled Universe Protocol was not used and no
fixed 30–40 name sample appears anywhere in this run. Caches are
46
days old; `rules.md § Index-Union Universe Protocol` rule 5 requires using them anyway and
logging the timestamp, which is done above.

## Inclusion filters applied

| Filter | Threshold | Applied from | Names removed |
|---|---|---|---|
| U.S. primary exchange | required | delisting/identity check (L019) | 1 (`EA`) |
| Market cap | > $2B | Nasdaq screener `marketCap` (L007) | 1 (1 vendor-empty) |
| Average daily dollar volume | > $20M over 20 sessions | raw closes x volume (L001) | 0 |
| Price | > $5 | raw close (L001) | 0 |
| Listing age | > 6 months | first fetched bar (L001) | 1 (`FDXF`) |
| Indicator completeness | daily+weekly MA/MACD available | `technical_indicators.json` (L004) | 1 (`Q`) |

## Rejection log

| Ticker | Reason | Detail | Eligible again? |
|---|---|---|---|
| BF-B | `MARKET_CAP_UNAVAILABLE` | vendor marketCap field empty | When the vendor populates `marketCap`. BF-B ranks far outside the published set, so this is immaterial to the leaderboard. |
| EA | `DELISTED_OR_HALTED` | last bar 2026-08-04 != basis 2026-08-05 | No — the US listing has ceased. |
| FDXF | `NO_HISTORY` | fetch or indicator pack unavailable | ~2026-11-27, six months after its 2026-05-28 first bar. |
| Q | `INDICATOR_INCOMPLETE` | 193 daily bars; weekly/daily MA or MACD UNAVAILABLE | When it accumulates 250 daily bars (~2026-10). |

## Metric coverage summary

| Metric group (`rules.md § Financial Metrics and Score Attribution`) | Sourceable | UNAVAILABLE | Effect |
|---|---|---|---|
| Risk / return (Sharpe, Sortino, IR, Treynor, Calmar, beta, tracking error) | 511/511 | 0 | Full — feeds `Macro_Z` and the metric block |
| Tail risk (60d max DD, VaR95, CVaR95) | 511/511 | 0 | Full — `dd60` is a `Tech_Z` slot |
| Sizing (raw Kelly, 0.25x Kelly) | 24/24 published | 0 | Full for every ranked name |
| Technical (momentum, RS, MA, volume, TD-9, RSI, MACD) | 511/511 | 0 | Full — six distinct `Tech_Z` slots |
| Fundamental / quality (revisions, margins, FCF, ROIC, leverage) | 0 | 511/511 | **`Fund_Z` UNAVAILABLE universe-wide** — contributes 0.00, does not count toward the 3-of-4 threshold |
| Sentiment / positioning (revision breadth, short interest, IV/skew) | 0 | 511/511 | **`Sent_Z` UNAVAILABLE universe-wide** — same treatment |

Two of four families are unavailable. Per `rules.md § Financial Metrics and Score
Attribution` a metric may contribute to `Adj Score` only when sourceable for >= 70% of the
universe; `Fund_Z` and `Sent_Z` are at 0%, so they are excluded rather than imputed. **No
missing metric is described anywhere in this package as neutral or supportive.**

## Technical indicator coverage (daily / weekly / monthly)

| Indicator | Daily | Weekly | Monthly | Notes |
|---|---|---|---|---|
| TD-9 setup | 511/511 | 511/511 | 511/511 | Setup count only; Countdown not computed |
| RSI(14) | 511/511 | 511/511 | 511/511 | Wilder |
| MACD(12,26,9) | 511/511 | 511/511 | 511/511 | Line/signal/histogram/state |
| MA alignment | 511/511 | 511/511 | 511/511 | MA20/MA50; `Q` rejected for incompleteness |
| 20/60-bar momentum | 511/511 | 511/511 | 511/511 | Two `Tech_Z` slots (daily) |
| Volume ratio (20-bar) | 511/511 | 511/511 | 511/511 | One `Tech_Z` slot (daily) |
| Relative strength vs SPY (20/60) | 511/511 | 511/511 | 511/511 | **Diagnostic only** — not a `Tech_Z` slot (Track B effective 2026-08-03) |

## Sector distribution of the scored universe

| Sector | Scored names | Share |
|---|---|---|
| Consumer Discretionary | 103 | 20.2% |
| Industrials | 86 | 16.8% |
| Technology | 80 | 15.7% |
| Finance | 68 | 13.3% |
| Health Care | 56 | 11.0% |
| Utilities | 37 | 7.2% |
| Real Estate | 28 | 5.5% |
| Consumer Staples | 21 | 4.1% |
| Energy | 16 | 3.1% |
| Telecommunications | 10 | 2.0% |
| Basic Materials | 5 | 1.0% |
| UNAVAILABLE | 1 | 0.2% |
