# 04 — Universe Summary · 2026-08-27

## Construction

| Step | Count | Source |
|---|---|---|
| S&P 500 constituent cache | 503 | `agents/equity/turtle-trader/universe/sp500.json`, fetched_at 2026-06-21T21:05:56Z |
| Nasdaq-100 constituent cache | 101 | `agents/equity/turtle-trader/universe/nasdaq100.json`, fetched_at 2026-06-21T21:05:56Z |
| Overlap | 89 | DERIVED by `build_index_universe.py` |
| **Index union** | 515 | `.work/claude-opus-5-2026-08-27/eligible_universe.txt` (L001) |
| Fetched 5Y history | 514 | stockanalysis bulk, 10.7s at 8 workers (L002) |
| **Scored universe** | 509 | after the filters below; percentiles labelled `INDEX_UNION_PCTL (n=509)` |

**Cache staleness.** Both constituent caches were fetched 2026-06-21, making them
**67 days** stale at this run date. `rules.md § Index-Union Universe Protocol` rule 5 is explicit that
stale caches are still used and their `fetched_at` logged — refresh is a maintenance task, not a reason
to fall back to a 30-name sample. The consequence is visible below: stale caches are exactly why
delisted and renamed names survive in the union long enough to need corporate-action classification.

The Sampled Universe Protocol was **not** used. The index-union helper succeeded, so every percentile
in this package is `INDEX_UNION_PCTL (n=509)`.

## Inclusion filters applied

| Filter (rules.md § Universe Construction) | Threshold | Source | Applied |
|---|---|---|---|
| U.S. primary exchange listing | required | Nasdaq screener presence (L009) | yes |
| Market cap | > $2B | screener `marketCap` (L009) | yes |
| Average daily dollar volume | > $20M over 20 sessions | DERIVED: mean(close x volume) over the last 20 raw bars (L002) | yes |
| Price | > $5 | raw basis close (L002) | yes |
| Listing age | > 6 months | DERIVED: >= 126 daily bars in the fetched series (L002) | yes |
| Bid-ask spread | <= 50 bps | **no source wired** — Enhancing input, `UNAVAILABLE` (L023) | **no** |
| Traded >= 80% of the trailing 60 sessions | required | implied by the last-bar and bar-count gates | partial |
| No unresolved corporate-action ambiguity | required | corporate-action ledger (L025) | yes |

The bid-ask filter cannot be applied because no spread tape is wired. It is an **Enhancing** input, so
it lowers data quality and caps confidence but never blocks `GO` — and it is disclosed here rather
than being described as passed.

## Rejection log (6 of 515)

| Ticker | Reason | Detail |
|---|---|---|
| AVB | `STALE_LAST_BAR` | last bar 2026-08-14 != basis 2026-08-27; corporate-action class CORPORATE_ACTION_DELISTED |
| BF-B | `MARKET_CAP_UNAVAILABLE` | screener marketCap field empty (vendor gap) |
| EA | `STALE_LAST_BAR` | last bar 2026-08-04 != basis 2026-08-27; corporate-action class CORPORATE_ACTION_DELISTED |
| EQR | `NO_PRICE_HISTORY` | HTTPError: HTTP Error 400: Bad Request |
| FDXF | `STALE_LAST_BAR` | last bar 2026-08-26 != basis 2026-08-27; corporate-action class TRANSIENT_FETCH_FAILURE |
| Q | `INDICATOR_INCOMPLETE` | daily/weekly MA alignment UNAVAILABLE (209 bars) |

`FDXF` is rejected on the stale-last-bar gate, which fires first, but it would have been rejected
anyway on listing age: its first bar is 2026-05-27, so it becomes eligible around 2026-11-27.
Its stale bar is **not** a corporate action — see below.

### Corporate-action classification (L025)

Track B accepted 2026-08-22, effective 2026-08-23: every symbol whose last bar predates the basis, or
whose bulk fetch transport-fails, is classified against two independent references, ledgered, and
intersected with open prediction keys.

| Ticker | Classification | Successor | Detected by | Settlement effect |
|---|---|---|---|---|
| EQR | `CORPORATE_ACTION_RENAMED` | VMRK | stockanalysis bulk fetch HTTP 400 (transport failure branch) | 2 open prediction keys reference EQR; both reported UNSETTLEABLE_CORPORATE_ACTION and left due. |
| AVB | `CORPORATE_ACTION_DELISTED` | none identified | last bar 2026-08-14 predates basis 2026-08-27 (9 sessions stale) | No open prediction keys reference AVB. Excluded from the scored universe on the last-bar gate. |
| EA | `CORPORATE_ACTION_DELISTED` | none identified | last bar 2026-08-04 predates basis 2026-08-27 (16 sessions stale) | No open prediction keys reference EA. Excluded from the scored universe on the last-bar gate. |
| FDXF | `TRANSIENT_FETCH_FAILURE` | none identified | last bar 2026-08-26 predates basis 2026-08-27 (1 session stale) | No open prediction keys reference FDXF. Independently excluded from the scored universe on the >6-month listing-age filter (first bar 2026-05-27; eligible ~2026-11-27). |

The intersection with open prediction keys produced **2**
matches, both `EQR`, both reported `UNSETTLEABLE_CORPORATE_ACTION` and left due (`02 § 0`, L025a).
No exchange ratio was inferred and no key was settled against `VMRK` — that is the explicit non-goal
of the accepted change.

## Sector composition of the scored universe

| Sector (Nasdaq screener taxonomy) | Names | Share | Median 60d momentum |
|---|---|---|---|
| Consumer Discretionary | 103 | 20.24% | +6.16% |
| Industrials | 86 | 16.90% | +1.82% |
| Technology | 80 | 15.72% | -1.03% |
| Finance | 68 | 13.36% | +12.71% |
| Health Care | 56 | 11.00% | +18.85% |
| Utilities | 37 | 7.27% | -0.17% |
| Real Estate | 26 | 5.11% | +1.21% |
| Consumer Staples | 21 | 4.13% | +5.75% |
| Energy | 16 | 3.14% | +5.17% |
| Telecommunications | 10 | 1.96% | +4.80% |
| Basic Materials | 5 | 0.98% | +10.05% |
| Miscellaneous | 1 | 0.20% | +6.83% |

The `sector_lead` macro slot is the **median** 60d momentum of the name's own sector, broadcast to
each member (see the normative Metric Definition Table in `05`).

## Metric coverage

| rules.md § Financial Metrics input | Sourceable across the eligible universe | Effect |
|---|---|---|
| Price history (>= 60 trading days) | 509/509 (100%) | Required input — GROUNDED |
| Realized vol 30d / 60d, downside vol, beta, tracking error, drawdown | 509/509 (100%) | all Technical/Macro slots computable |
| Momentum, MA alignment, MACD, volume ratio, relative strength | 509/509 (100%) | `Tech_Z` fully sourceable |
| Market cap and sector | 509/509 (100%) | universe filter + `sector_lead` slot |
| Next earnings date | 509/509 (100%) | Required input — complete forward sweep (L010) |
| Fundamental family inputs (revisions, margins, FCF, ROIC, leverage) | 0 (0%) | **`Fund_Z` UNAVAILABLE** — blocks evidence threshold #2 (L021) |
| Sentiment / positioning inputs (short interest, IV/skew, revision breadth) | 0 (0%) | **`Sent_Z` UNAVAILABLE** — blocks evidence threshold #2 (L022) |
| Bid-ask spread tape | 0 (0%) | Enhancing — exclusion filter not applied; never a GO blocker |

Two of the four factor families are `UNAVAILABLE` universe-wide. That is a **data-quality** failure
(multiplier 1.00 -> 0.80, L020), not a neutral pass: `rules.md § Family Aggregation` sets an
`UNAVAILABLE` family's displayed contribution to `0.00 (UNAVAILABLE)` and forbids counting it toward
the "3 of 4 families supportive" threshold.

## Technical indicator coverage (daily / weekly / monthly)

| Indicator | Daily | Weekly | Monthly | Notes |
|---|---|---|---|---|
| TD-9 setup | 509/509 | 509/509 | 509/509 | setup count only, no Countdown (rules.md § TD-9 Definition) |
| RSI(14) Wilder | 509/509 | 509/509 | 509/509 | exhaustion flag, not a standalone signal |
| MACD(12,26,9) state + histogram | 509/509 | 509/509 | 509/509 | daily+weekly enter `Tech_Z`; monthly is displayed only |
| MA20 / MA50 alignment | 509/509 | 509/509 | 509/509 | a name missing daily **or** weekly alignment is rejected `INDICATOR_INCOMPLETE` (`Q` this run) |
| 20/60-bar momentum | 509/509 | 509/509 | 509/509 | daily 20d and 60d are two of the six `Tech_Z` slots |
| 20-bar volume ratio | 509/509 | 509/509 | 509/509 | daily is the `vol_conf` slot |
| 20/60-bar relative strength vs SPY | 509/509 | 509/509 | 509/509 | **diagnostic only** — not a `Tech_Z` slot (Track B effective 2026-08-03) |

Monthly blocks are display-only. Names with a short history can carry an `UNAVAILABLE` monthly
reading without being rejected; only a missing **daily or weekly** MA alignment is disqualifying,
which is why `Q` (205 bars) is the single `INDICATOR_INCOMPLETE` rejection.
