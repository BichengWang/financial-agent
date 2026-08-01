# 04 — Universe Summary — 2026-08-01

## Index-union construction (normal path — no sampled fallback)

| Field | Value |
|---|---|
| Source | `build_index_universe.py` |
| S&P 500 constituents | 503 |
| Nasdaq-100 constituents | 101 |
| Overlap | 89 |
| **Union** | **515** |
| Cache paths | `agents/equity/turtle-trader/universe/sp500.json`, `agents/equity/turtle-trader/universe/nasdaq100.json` |
| Cache `fetched_at` | 2026-06-21T21:05:56Z / 2026-06-21T21:05:56Z |
| Cache age at run date | **41 days** |
| Scored universe | **513** |
| Percentile label | **`INDEX_UNION_PCTL (n=513)`** |

The helper succeeded, so the **Sampled Universe Protocol was not used**. Per
`rules.md § Index-Union Universe Protocol` rule 5, stale caches are used as-is for the run
and their timestamps logged; refreshing them is a maintenance task and is **not** grounds to
fall back to a 30-name sample. The caches are
41
days old — worth refreshing soon, but constituent turnover over six weeks is small and does
not distort percentile denominators materially.

## Inclusion / exclusion log

Filters per `rules.md § Universe Construction`: U.S. primary listing, market cap > $2B,
ADDV20 > $20M, price > $5, listing age > 6 months, ≥ 80% of the trailing 60 sessions traded.

| Ticker | Reason | Detail |
|---|---|---|
| BF-B | `MARKET_CAP_UNAVAILABLE` | market cap field empty at the Nasdaq screener for `BF/B` — a real vendor gap, recorded `UNAVAILABLE` rather than estimated; ADDV20 $68.2M and price $28.73 both pass |
| FDXF | `NO_HISTORY_OR_INDICATORS` | FedEx spin-off, first bar 2026-05-27 — fails the >6-month listing-age filter; becomes eligible ~2026-11-27 |

**2 of 515 rejected**, leaving **513** scored.
Both rejections are principled and neither is a fetch failure: BF-B has a genuine vendor
data gap and FDXF is genuinely too young. Note BF-B ranks nowhere near the leaderboard on
any available metric, so the gap is immaterial to the outcome.

## Metric coverage across the eligible universe

`rules.md § Financial Metrics and Score Attribution` requires a metric to be sourceable for
≥ 70% of the universe before it may contribute to `Adj Score`.

| Metric group | Sourceable | UNAVAILABLE | Coverage | Contributes to `Adj Score`? |
|---|---|---|---|---|
| Price / return history | 513 | 0 | 100.0% | Yes |
| 20d & 60d momentum | 513 | 0 | 100.0% | Yes (`Tech_Z`) |
| Relative strength vs SPY (20d, 60d) | 513 | 0 | 100.0% | Yes (`Tech_Z`) — **but see the duplication finding in `13`** |
| MA alignment (D/W/M) | 513 | 0 | 100.0% | Yes (`Tech_Z`) |
| MACD(12,26,9) D/W/M | 513 | 0 | 100.0% | Yes (`Tech_Z`) |
| TD-9 setup D/W/M | 513 | 0 | 100.0% | Diagnostic / exhaustion flag only |
| RSI(14) D/W/M | 513 | 0 | 100.0% | Diagnostic / exhaustion flag only |
| 20d volume ratio | 513 | 0 | 100.0% | Yes (`Tech_Z`) |
| 60d max drawdown | 513 | 0 | 100.0% | Yes (`Tech_Z`) |
| 60d beta, tracking error | 513 | 0 | 100.0% | Yes (`Macro_Z`) |
| 30d realized & downside vol | 513 | 0 | 100.0% | sigma, Sortino |
| Sector / market cap | 511 / 513 | 2 / 0 | 99.6% / 100.0% | Yes (`Macro_Z` sector leadership) |
| Next earnings date | 195 confirmed + 320 no-print | 0 | **100.0%** | Penalty input |
| **Fundamental family** | **0** | **513** | **0.0%** | **No — `Fund_Z` = `UNAVAILABLE`** |
| **Sentiment family** | **0** | **513** | **0.0%** | **No — `Sent_Z` = `UNAVAILABLE`** |
| Options IV30 / skew | 0 | 513 | 0.0% | No |
| Short interest / borrow | 0 | 513 | 0.0% | No |
| Bid-ask spread tape | 0 | 513 | 0.0% | No |

### Which gaps affect data quality vs `GO` eligibility

- **Affect `GO` eligibility:** none. All five Required inputs from
  `rules.md § Input Classification` are grounded (see the `00` GO-Gate Table).
- **Affect data quality and the evidence thresholds:** the Fundamental and Sentiment
  families. Their absence sets the DQ multiplier to 0.80 and makes
  evidence thresholds 2, 3 and 4 unsatisfiable for every name. This is the entire reason the
  run is `NO_TRADE`, and it is a **tooling gap, not a market judgement**.

### Technical indicator coverage by timeframe

| Indicator | Daily | Weekly | Monthly |
|---|---|---|---|
| TD-9 setup | 513/513 | 513/513 | 513/513 |
| RSI(14) | 513/513 | 513/513 | 513/513 |
| MACD(12,26,9) | 513/513 | 513/513 | 513/513 |
| MA alignment | 513/513 | 513/513 | 513/513 |
| 20/60 momentum | 513/513 | 513/513 | 513/513 |
| Volume ratio 20d | 513/513 | — | — |
| Relative strength vs SPY | 513/513 | 513/513 | 513/513 |

## Sector distribution of the scored universe

| Sector | Names | Share |
|---|---|---|
| Consumer Discretionary | 104 | 20.3% |
| Industrials | 85 | 16.6% |
| Technology | 82 | 16.0% |
| Finance | 68 | 13.3% |
| Health Care | 56 | 10.9% |
| Utilities | 37 | 7.2% |
| Real Estate | 28 | 5.5% |
| Consumer Staples | 21 | 4.1% |
| Energy | 16 | 3.1% |
| Telecommunications | 9 | 1.8% |
| Basic Materials | 5 | 1.0% |
| UNKNOWN | 2 | 0.4% |

