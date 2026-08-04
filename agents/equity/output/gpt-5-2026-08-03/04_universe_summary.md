# 04 — Universe Summary — 2026-08-03

## Construction

| Input | Count | Cache fetched | Working source |
| --- | --- | --- | --- |
| S&P 500 | 503 | 2026-06-21T21:05:56Z | agents/equity/turtle-trader/universe/sp500.json |
| Nasdaq-100 | 101 | 2026-06-21T21:05:56Z | agents/equity/turtle-trader/universe/nasdaq100.json |
| Overlap | 89 | — | build_index_universe.py |
| Union | 515 | — | L-U-001 |
| Scoreable | 511 | 2026-08-03 | L-HIST + Nasdaq screener + technical helper |

Percentiles are labeled `INDEX_UNION_PCTL (n=511)`. Constituents caches are
stale but valid under the Index-Union Protocol; staleness is recorded instead of triggering
the prohibited fixed sample fallback.

## Inclusion / exclusion log

| Ticker | Reason |
| --- | --- |
| BF-B | market cap <= $2B or unavailable; sector classification unavailable |
| BRK-B | sector classification unavailable |
| FDXF | last history date 2026-07-31; listing/history minimum failed; technical pack unavailable |
| GEV | sector classification unavailable |

## Metric coverage

| Metric group | Sourceable | UNAVAILABLE | DQ / confidence effect | Notes |
| --- | --- | --- | --- | --- |
| Price/history/risk | 511 | 4 | Required input; complete for scoreable names | 5Y history; ≥60d analytics |
| Technical / Price | 511 | 4 | AVAILABLE; six distinct score slots | RS20/RS60 retained only as diagnostics |
| Macro / Regime | 511 | 4 | AVAILABLE; four metrics | beta fit, sector leadership, rate resilience, vol stability |
| Fundamental | 0 | 511 | DQ 0.80; family unavailable | SHADOW not promoted at ≥70% |
| Sentiment / Positioning | 0 | 511 | DQ 0.80; family unavailable | No promoted full-universe source |
| Earnings calendar | 198 confirmed / 0 estimated | 313 unresolved | Required gap; `DELAYED_PARTIAL` / `HALTED` | Union: 200 confirmed / 315 unresolved; transport-complete sweep is not next-date completeness |

## Technical indicator coverage

| Indicator | Daily | Weekly | Monthly | Ticker packs OK | Packs unavailable |
| --- | --- | --- | --- | --- | --- |
| TD9 | 517 | 517 | 517 | 517 | 1 |
| RSI14 | 517 | 517 | 516 | 517 | 1 |
| MACD | 517 | 517 | 517 | 517 | 1 |
| MA alignment | 517 | 517 | 517 | 517 | 1 |
| momentum | 517 | 517 | 515 | 517 | 1 |
| volume | 517 | 517 | 515 | 517 | 1 |
| relative strength | 517 | 517 | 515 | 517 | 1 |

Every failed field remains `UNAVAILABLE`; helper exit status was not treated as sufficient
without inspecting per-ticker coverage.
