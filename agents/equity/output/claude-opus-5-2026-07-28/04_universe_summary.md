# 04 Universe Summary — 2026-07-28

## Construction — Index-Union Protocol (normal path)

```bash
python3 agents/equity/daily_investment_system/build_index_universe.py \
  --output-tickers agents/equity/output/claude-opus-5-2026-07-28/eligible_universe.txt \
  --output-summary agents/equity/output/claude-opus-5-2026-07-28/universe_summary.json
```

| Count | Value |
|---|---|
| S&P 500 constituents | 503 |
| Nasdaq-100 constituents | 101 |
| Overlap | 89 |
| **Union** | **515** |
| Cache `fetched_at` | 2026-06-21T21:05:56Z (both caches) |
| Scored after filters | **514** |

Percentiles throughout this package are labelled **`INDEX_UNION_PCTL (n=514)`**. The emergency Sampled
Universe Protocol was **not** used — the helper succeeded, so using a fixed 30–40 name sample would be
a process failure per `rules.md § Index-Union Universe Protocol` #6.

The constituent caches are 36 days
old. Per rule #5 they are used as-is for the run and the timestamp is logged; refreshing them is
maintenance, not a reason to fall back.

## Inclusion / Exclusion Log

| Filter | Threshold | Names failing |
|---|---|---|
| U.S. primary exchange | required | 0 |
| Market cap | > $2B | 0 |
| 20-day average daily dollar volume | > $20M | 0 |
| Price | > $5 | 0 |
| Listing age | > 6 months | **1** |
| Traded ≥ 80% of trailing 60 sessions | required | **1** (same name) |
| Minimum 60 bars of history | required | **1** (same name) |

### Rejection log

| Ticker | Reasons |
|---|---|
| FDXF | listing age 60d <= 183d (first bar 2026-05-28); traded 41/60 trailing sessions (<80%); only 41 bars (<60 minimum history) |

**FDXF** is the FedEx freight spin-off, first bar 2026-05-28 (41 sessions). It fails the
listing-age filter legitimately and becomes eligible around 2026-11-27. Same treatment as 2026-07-24.

`BF-B`'s market cap is empty in the Nasdaq screener — a real vendor gap, recorded as `UNAVAILABLE`
rather than estimated. It ranks 257/514 so the gap never affects a published decision.

### Exclusion filters that could NOT be applied

| Filter | Status |
|---|---|
| Bid-ask spread above 50 bps | **`UNAVAILABLE`** — no bid-ask tape wired (L048) |
| Halted / pending delisting | **`UNAVAILABLE`** — no halt feed; no proxy substituted |
| Unresolved corporate-action ambiguity | **partially applied** — 3 ex-dividend cases detected and resolved (L054) |

These are disclosed as coverage gaps, not silently treated as passing. They are Enhancing inputs and
do not block `GO`; they contribute to the 0.8 data-quality multiplier.

## Metric Coverage

| Metric group | Sourceable across the universe | Status |
|---|---|---|
| Price / volume / liquidity | 514/514 (100%) | full |
| Realized vol, downside vol, beta, tracking error, drawdown | 514/514 (100%) | full |
| Technical pack (TD-9, RSI, MACD, MA, momentum, volume, RS) | 514/514 (100%) daily/weekly/monthly | full |
| Sector / industry | 510/514 | near-full |
| Market cap | 512/514 | near-full (1 vendor gap) |
| Next earnings date | 58/514 — **top-20 fully grounded** | bounded by design |
| Fundamental family inputs | 0/514 | **`UNAVAILABLE`** (L046) |
| Sentiment / positioning inputs | 0/514 | **`UNAVAILABLE`** (L047) |
| Options IV / short interest / bid-ask / revisions | 0/514 | **`UNAVAILABLE`** (L048) |

**Which gaps affect `GO` eligibility, and which only affect data quality.** Per
`rules.md § Input Classification`, all five Required inputs are grounded (see the `00` GO-gate table) —
none of the gaps above blocks `GO`. What they do is cap the data-quality multiplier at
0.8, which independently trips Evidence Threshold #4 (data completeness ≥ 85%), and leave
only 2 of 4 families available, which makes Evidence Threshold #2 unsatisfiable. **That is the
distinction that decides this run: the data is good enough to publish honestly, and not good enough to
mark anything investable.**

Earnings coverage is bounded deliberately, not accidentally: the endpoint is per-symbol and the run
resolves the shortlist to convergence (top-20 fully grounded) under a 4-pass / 60-name cap. This run
used **2 passes over 58 names with zero transport failures**.

## Technical Indicator Coverage (daily / weekly / monthly)

| Indicator | Daily | Weekly | Monthly |
|---|---|---|---|
| TD-9 setup | 514/514 | 514/514 | 514/514 |
| RSI(14) | 514/514 | 514/514 | 513/514 |
| MACD(12,26,9) | 514/514 | 514/514 | 514/514 |
| MA alignment | 514/514 | 514/514 | 514/514 |
| 20/60 momentum | 514/514 | 0/514 | 0/514 |
| Volume ratio 20d | 514/514 | — | — |
| Relative strength vs SPY | 514/514 | 0/514 | 0/514 |

All values come from `technical_indicators.json` (L010, L019), computed on **adjusted** closes. Coverage
clears the 70%-of-universe bar in `rules.md § Financial Metrics and Score Attribution`, so RSI and MACD
are eligible to contribute to `Tech_Z` rather than being diagnostics only.
