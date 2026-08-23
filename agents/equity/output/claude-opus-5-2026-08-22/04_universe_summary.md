# 04 — Universe Summary · 2026-08-22

## Construction

Built by `build_index_universe.py` from the local constituent caches — the normal daily path. The
emergency Sampled Universe Protocol was **not** used.

```bash
python3 agents/equity/daily_investment_system/build_index_universe.py \
  --output-tickers agents/equity/.work/claude-opus-5-2026-08-22/eligible_universe.txt \
  --output-summary agents/equity/.work/claude-opus-5-2026-08-22/universe_summary.json
```

| Quantity | Count | Cache | Cache fetched_at |
|---|---|---|---|
| S&P 500 constituents | 503 | `agents/equity/turtle-trader/universe/sp500.json` | 2026-06-21T21:05:56Z |
| Nasdaq-100 constituents | 101 | `agents/equity/turtle-trader/universe/nasdaq100.json` | 2026-06-21T21:05:56Z |
| Overlap | 89 | — | — |
| **Union (input universe)** | **515** | — | 2026-08-22T19:07:26Z |

The caches are **62 days stale**. Per `rules.md § Index-Union Universe Protocol` rule 5
they are used as-is for the run and their timestamps logged; refreshing them is a maintenance task,
never a reason to fall back to a 30-name sample. Staleness has a concrete cost this run — see the
corporate-action rejections below.

Percentile label for every rank in this package: **`INDEX_UNION_PCTL (n=509)`**.

## Inclusion / exclusion filters applied

| Filter | Threshold | Source |
|---|---|---|
| Listing | U.S. primary exchange | Nasdaq screener (L009) |
| Market cap | > $2B | L009, L600-series |
| Average daily dollar volume | > $20M over 20 trading days | DERIVED from L002 (L600-series) |
| Price | > $5 | L002, L200-series |
| Listing age | > 6 months (~126 daily bars) | L002 bar count |
| Corporate action | excluded when unresolved | L025 |
| Indicator completeness | daily+weekly MA alignment required | L013 |

## Inclusion / exclusion log

Input 515 → **scored 509**, with 6 rejections:

| Ticker | Reason | Detail |
|---|---|---|
| AVB | STALE_LAST_BAR | last bar 2026-08-14 != basis 2026-08-21; ceased trading / corporate action |
| BF-B | MARKET_CAP_UNAVAILABLE | screener marketCap field empty (vendor gap) |
| EA | STALE_LAST_BAR | last bar 2026-08-04 != basis 2026-08-21; ceased trading / corporate action |
| EQR | NO_PRICE_HISTORY | HTTPError: HTTP Error 400: Bad Request |
| FDXF | LISTING_AGE_UNDER_6M | 60 daily bars (< ~126 sessions); first bar 2026-05-28 |
| Q | INDICATOR_INCOMPLETE | daily/weekly MA alignment UNAVAILABLE (205 bars) |

### Corporate-action rejections (L025)

Three of the six rejections are the same root cause: the constituent caches predate corporate
actions that removed these names from the tape.

- **`EQR`** — renamed into / absorbed by **`VMRK` (Vivmark Residential)**. The bulk history endpoint
  now returns HTTP 400 for `EQR`; the Nasdaq screener has no `EQR` row but does carry `VMRK`
  (Real Estate, market cap 52,597,125,000); CNBC returns the name "Vivmark Residential" under the
  legacy `EQR` symbol at the 2026-08-21 close. `VMRK` itself has 251 continuous daily bars back to
  2025-08-21.
- **`AVB`** — last daily bar **2026-08-14**, absent from the screener, no vendor quote. `VMRK`'s
  market cap is close to the combined pre-event capitalisation of `EQR` and `AVB`, which is
  consistent with a combination, but **the exchange ratio was not fetched and is not asserted here**.
- **`EA`** — last daily bar **2026-08-04**, absent from the screener, no successor found by name
  search across all 7,183 screener rows.

None of the three can produce a grounded 2026-08-21 entry price from two independent sources, so all
three are `UNAVAILABLE` and excluded rather than estimated. **Two OPEN predictions reference `EQR`**
with target dates 2026-08-23 and 2026-08-24 and will come due on the next run with no settleable
price — that gap is this run's Track B proposal (`13`).

`FDXF` remains excluded on listing age (60 daily bars (< ~126 sessions); first bar 2026-05-28) and
becomes eligible around 2026-11-27. `Q` has 205 bars
— insufficient for weekly MA alignment. `BF-B`'s screener `marketCap` field is empty; that is a real
vendor gap, marked `UNAVAILABLE` rather than estimated.

## Sector composition of the scored universe

| Sector | Names | Share |
|---|---|---|
| Consumer Discretionary | 103 | 20.2% |
| Industrials | 86 | 16.9% |
| Technology | 80 | 15.7% |
| Finance | 68 | 13.4% |
| Health Care | 56 | 11.0% |
| Utilities | 37 | 7.3% |
| Real Estate | 26 | 5.1% |
| Consumer Staples | 21 | 4.1% |
| Energy | 16 | 3.1% |
| Telecommunications | 10 | 2.0% |
| Basic Materials | 5 | 1.0% |
| UNCLASSIFIED | 1 | 0.2% |

## Metric coverage summary

Which `rules.md § Financial Metrics and Score Attribution` inputs are sourceable across the eligible
universe:

| Metric group | Sourceable | Status | Effect |
|---|---|---|---|
| Risk / return (Sharpe, Sortino, IR, Treynor, Calmar, beta, tracking error) | 509/509 (100%) | **Sourceable** | feeds Technical and Macro families |
| Tail risk (60d max drawdown, VaR95, CVaR95) | 509/509 (100%) | **Sourceable** | `dd60` is a Technical slot; VaR/CVaR are displayed diagnostics |
| Sizing (raw Kelly, 0.25x Kelly) | 509/509 (100%) | **Sourceable** | investability gate and sizing input |
| Technical (momentum, RS, MA alignment, volume, TD-9, RSI, MACD) | 509/509 (100%) daily | **Sourceable** | `Tech_Z` |
| Fundamental / quality (revisions, margins, FCF yield, ROIC, leverage, valuation) | 0/509 (0%) | **UNAVAILABLE** | `Fund_Z` UNAVAILABLE universe-wide — no fetch path wired |
| Sentiment / positioning (revision breadth, short interest, borrow, IV/skew, put/call) | 0/509 (0%) | **UNAVAILABLE** | `Sent_Z` UNAVAILABLE universe-wide — no fetch path wired |

`Fund_Z` and `Sent_Z` are the binding constraint on this system and have been since the series
began. `rules.md § SHADOW Diagnostic Tooling` records why: the Phase-1 diagnostics exist and passed a
shadow run, but they covered ~4.7% of the universe against a 70%-of-universe bar that
`§ Financial Metrics and Score Attribution` already imposes before any metric may enter `Adj Score`.
Promotion needs Phase 2 (bulk `companyfacts.zip` plus a threaded Nasdaq fetch across all ~509 names),
which has not been attempted. **This is a data-quality gap, not a `GO` blocker in itself** — but it
makes evidence thresholds 2, 3, and 4 arithmetically unsatisfiable, which is what produces
`NO_TRADE`.

## Technical indicator coverage (daily / weekly / monthly)

| Indicator | Daily | Weekly | Monthly |
|---|---|---|---|
| TD-9 daily / weekly / monthly | 509/509 (100.0%) | 509/509 (100.0%) | 509/509 (100.0%) |
| RSI(14) daily / weekly / monthly | 509/509 (100.0%) | 509/509 (100.0%) | 509/509 (100.0%) |
| MACD(12,26,9) state | 509/509 (100.0%) | 509/509 (100.0%) | 506/509 (99.4%) |
| MA alignment | 509/509 (100.0%) | 509/509 (100.0%) | 502/509 (98.6%) |
| 20-bar momentum | 509/509 (100.0%) | 509/509 (100.0%) | 508/509 (99.8%) |
| 60-bar momentum | 509/509 (100.0%) | 509/509 (100.0%) | 500/509 (98.2%) |
| 20-bar volume ratio | 509/509 (100.0%) | n/a | n/a |
| Relative strength vs SPY (20/60) | 509/509 (100.0%) | n/a | n/a |

Monthly gaps are confined to names with fewer than ~5 years of history and are display-only — they
do not enter `Tech_Z`, whose six slots use daily and weekly blocks exclusively.
