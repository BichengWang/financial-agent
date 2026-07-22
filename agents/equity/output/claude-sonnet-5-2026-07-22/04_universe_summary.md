# 04 Universe Summary — 2026-07-22

## Construction

Built via `build_index_universe.py` with explicit cache paths:

```
python3 agents/equity/daily_investment_system/build_index_universe.py \
  --output-tickers agents/equity/output/claude-sonnet-5-2026-07-22/eligible_universe.txt \
  --output-summary agents/equity/output/claude-sonnet-5-2026-07-22/universe_summary.json \
  --sp500-cache agents/equity/turtle-trader/universe/sp500.json \
  --nasdaq100-cache agents/equity/turtle-trader/universe/nasdaq100.json
```

| Metric | Value |
|---|---|
| S&P 500 count | 503 |
| Nasdaq-100 count | 101 |
| Overlap count | 89 |
| Union count | 515 |
| Cache `fetched_at` (both caches) | 2026-06-21T21:05:56Z |

Caches are 31 days old at run time; per `rules.md § Index-Union Universe Protocol` #5 this is a maintenance item, not a run blocker — the run still uses the cached constituent list and discloses the `fetched_at` timestamp. **No sampled-universe fallback was used** — the full index-union path succeeded end to end.

## Inclusion / Exclusion Log

Index membership (S&P 500 / Nasdaq-100) is treated as satisfying the market-cap (>$2B) and general-liquidity inclusion filters by construction (both indices screen on cap and liquidity at inclusion time). Price (>$5) and 20-day average-dollar-volume (>$20M) were independently recomputed from the fetched price history for every name as a real check, not merely assumed:

| Filter | Result |
|---|---|
| Price > $5 | 0 exclusions (no sub-$5 names in the 515-name union) |
| 20d ADV > $20M | 0 exclusions |
| Listing age > 6 months | **1 exclusion: `FDXF`** (FedEx Freight spinoff; only 38 trading days of history since 2026-05-27 — fails both the listing-age filter and the 60-trading-day minimum history requirement for `GO`-grade indicators) |
| Halted / pending delisting | 0 flagged |
| Corporate-action ambiguity | 0 flagged (BRK-B fetched as `BRK.B` on Nasdaq; SATS renamed to ECHO upstream — both resolved cleanly, no ambiguity) |
| Thin ADRs / <80% session coverage (60d) | 0 flagged beyond FDXF (short-history exclusion above already captures this case) |

**Net sourceable universe: 514 of 515** (excluding FDXF), labeled `INDEX_UNION_PCTL (n=514)` throughout `05`/`06`.

## Metric Coverage Summary

| `rules.md § Financial Metrics` input | Sourceable across universe? | Coverage | Notes |
|---|---|---|---|
| Price history (60d+ for beta/vol/drawdown/momentum) | Yes | 514/515 (99.8%) | FDXF excluded (see above) |
| Beta vs SPY (60d) | Yes | 514/515 | `DERIVED`, OLS slope |
| Realized vol 30d (sigma) | Yes | 514/515 | `DERIVED`, `REALIZED_VOL_30D` |
| 60d max drawdown | Yes | 514/515 | `DERIVED` |
| Momentum (20d/60d), relative strength (20d/60d vs SPY), volume ratio, MA alignment | Yes | 514/515 | via `technical_indicators.json` |
| TD-9, RSI(14), MACD(12,26,9) — daily/weekly/monthly | Yes | 517/518 of `technical_indicators.json` requests (515 universe + SPY/QQQ/SOXX; only FDXF `UNAVAILABLE`) | Canonical source is `technical_indicators.py`; no hand computation |
| Next earnings date | Scoped to shortlist, not universe-wide | 54/514 fetched (top-35-by-score + 14 carry-forwards + 6-name bounded second pass) | Per `agents.md`, earnings preflight is shortlist-scoped by design, not a universe-wide requirement |
| **Fundamental family** (earnings-revision momentum, revenue acceleration, margin trajectory, FCF yield, accrual quality) | **No — `SHADOW`-only, `UNAVAILABLE` for scoring** | 0/514 promoted | `fundamental_diagnostics.py` exists as a diagnostic-only tool per `rules.md § SHADOW Diagnostic Tooling`; not run this cycle (would cover far short of the 70%-of-universe promotion threshold in any case) |
| **Sentiment/Positioning family** (short interest, options skew, analyst revisions, insider buying, institutional flow) | **No — `SHADOW`-only, `UNAVAILABLE` for scoring** | 0/514 promoted | Same as above; `sentiment_diagnostics.py` not run this cycle |

**Which missing inputs affect data quality vs. `GO` eligibility:** Fund_Z and Sent_Z are the two families that structurally block evidence threshold #2 (see `05_factor_scores.md`) — this affects the investable-vs-monitor sleeve gate, not a hard `GO`-blocking data-integrity failure, since all five **Required** inputs from `rules.md § Input Classification` remain grounded (Fund/Sent are outside that Required list; they are Enhancing-tier signal families, not Required GO inputs, though their absence here is large enough in practice to zero out 55% of the nominal family weight in `Adj Score`). Options IV/skew, short interest, bid-ask tape, analyst-revision tape, and institutional-flow data (all **Enhancing** per `rules.md`) were not fetched this run — consistent with every prior dated package, they reduce the data-quality multiplier (fixed at 0.80, see `05`) and cap confidence, but do not themselves block `GO`.

## Technical Indicator Coverage (Daily/Weekly/Monthly)

| Timeframe | TD-9 | RSI(14) | MACD(12,26,9) | MA alignment / momentum / volume / RS |
|---|---|---|---|---|
| Daily | 514/514 | 514/514 | 514/514 | 514/514 |
| Weekly | 514/514 | 514/514 | 514/514 | 514/514 |
| Monthly | 514/514 | 514/514 | 514/514 | 514/514 |

All computed by `technical_indicators.py` from the same fetched 5-year daily bars used for realized vol, beta, and drawdown (2021-07-22 through 2026-07-21 basis; see `00_run_manifest.md § Price Basis Disclosure`). No hand-calculated indicator values were substituted anywhere.
