# 04 Universe Summary — 2026-07-14

## Construction

S&P 500 ∪ Nasdaq-100 index-union path (normal daily path): **515 union / 514 eligible** — INDEX_UNION_PCTL (n=514). Source `universe_summary.json`: sp500_count 503, nasdaq100_count 101, overlap 89, caches fetched_at 2026-06-21T21:05:56Z (stale-cache rule: use and log, refresh is maintenance). No sampled fallback used.

## Inclusion / Exclusion Log

| Filter | Result |
|---|---|
| U.S. primary listing | 515/515 pass (constituent caches are US-listed) |
| Market cap > $2B | Pass by construction (index membership); not independently re-verified — no mcap feed |
| 20d ADDV > $20M | 514/514 pass (index-cap scale; min observed well above threshold) |
| Price > $5 | 514/514 pass |
| Listing age > 6 months / history ≥ 65 bars | **FDXF excluded** (32 bars since 2026-05-27 listing) |
| Halts / delisting / corporate-action ambiguity | SATS trades as ECHO (EchoStar rename) — fetched as ECHO, saved as SATS, no ambiguity; BF-B sourced via IBKR (Nasdaq API returns empty for that share class) |

## Earnings Penalty Roll (63-symbol confirmed-dates preflight, L015)

61 confirmed / 2 vendor-empty (FAST cadence-est 2026-07-13 ±5d → penalty on buffered window; MU next ~09-25, outside). Names inside the ≤14d window carrying -0.10 today: **FFIV (13d), STT (2d), UNH (2d), GE (2d), ELV (1d), JBHT (1d), MTB (1d), PNC (1d), BNY (1d), RF (3d), WRB (6d), NTRS (8d), CSX (8d), WST (9d), UNP (9d), EW (9d), AMP (9d), AXP (10d), V (14d), IQV (14d), FAST (est)**. The 07-15..07-17 financials wave is the dominant cross-sectional event gate for the second consecutive run.

## Metric Coverage Summary

| Metric Group | Sourceable | UNAVAILABLE | Effect |
|---|---|---|---|
| Price history / risk-return pack (rvol, beta, maxDD, momentum, VaR/CVaR, Kelly, Sharpe/Sortino/IR) | 514 | 0 | — (rf sourced L008 → ratios are rf-adjusted, not RAW_DIAGNOSTIC; Sortino computed from persisted downside series this run) |
| Technical pack D/W/M (TD9, RSI, MACD, MA, mom, VR, RS) | 514 | FDXF (rejected) + isolated monthly-MA gaps on short-history names | — |
| Earnings dates | 61 confirmed + 1 cadence-est (shortlist) | MU vendor-empty (outside horizon) | penalties per roll above |
| Fundamental family | 0 | 514 | family 0.00; DQ 0.80; conf cap LOW (Enhancing-class, not a GO blocker) |
| Sentiment family | 0 | 514 | family 0.00; DQ 0.80; conf cap LOW (Enhancing-class) |

Data quality vs GO eligibility: all five Required inputs grounded (00 GO-Gate); the missing families are Enhancing-class and affect data quality (DQ 0.80) and the 3-of-4-families evidence threshold — which is what forces NO_TRADE at the construction stage, not the data gate.
