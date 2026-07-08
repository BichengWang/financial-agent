# 04 Universe Summary

## Construction

The index-union helper succeeded: `build_index_universe.py` requires no network access (reads local constituent caches) and wrote the full S&P 500 ∪ Nasdaq-100 union. Source row: L001–L003.

| Input | Count | Cache Timestamp |
| --- | --- | --- |
| S&P 500 | 503 | 2026-06-21T21:05:56Z |
| Nasdaq-100 | 101 | 2026-06-21T21:05:56Z |
| Overlap | 89 | N/A |
| Union | 515 | 2026-07-03T12:12:15Z |

`eligible_universe.txt` (515 tickers) is the complete candidate universe per `rules.md § Index-Union Universe Protocol`, and it is **not** the same 30–40 name sample reused across runs.

## Sampled Universe Protocol Disclosure (price-history / scoring path)

Price-history fetch and technical-indicator computation for the full 515-name union was **not completed this run** — this is a documented emergency-fallback condition, not a preference: `technical_indicators.py`'s built-in Yahoo Finance fetch is blocked by this session's egress policy (403 from the proxy on `query2.finance.yahoo.com`), and IBKR-only fetch at 515-name scale (2 tool calls per name — `search_contracts` + `get_price_history`, each returning large payloads) is infeasible within a single session. Per `rules.md § Sampled Universe Protocol`:

1. **Carry-forward names (14):** all `CARRY`/`PROMOTE`-eligible names surfaced by `02_reflection.md`'s prior-baseline monitoring sleeve plus the standing technical/momentum monitoring list from the immediately prior model runs in this output tree — `MU`, `INTC`, `AMD`, `DDOG`, `PANW`, `HUM`, `DELL`, `MRVL`, `MRNA`, `CNC`, `ARM` *(ARM's IBKR history could not be captured to a local file this session — see note below — excluded)*, `FLEX`, `AMAT`, plus `CAT` (from today's own `02_reflection.md` cross-model baseline carry-forward).
2. **2–3 largest liquid names per GICS sector (S&P 500 constituents):** Information Technology (`AAPL`, `MSFT`, `NVDA`), Communication Services (`GOOGL`, `META`, `NFLX`), Consumer Discretionary (`AMZN`, `TSLA`), Financials (`JPM`, `GS`), Health Care (`UNH`), Industrials (`CAT` — already carried forward, not double-counted), Consumer Staples (`WMT`, `COST`), Energy (`XOM`), Utilities (`NEE`), Real Estate (`PLD`), Materials (`LIN`).
3. **Theme-watchlist names with a stated catalyst:** none added beyond the above (no live theme feed this session).
4. **Minimum 30, all grounded:** 30 names achieved (see substitution note below), all with grounded IBKR entry prices and 5-year history.

**Substitutions during fetch:** (a) `ARM` was in the original candidate list but its IBKR `get_price_history` result could not be captured to a local CSV file within this session's tool-output-size constraints (result returned inline rather than saved to a file, and was too large to transcribe reliably by hand) — excluded, documented, not silently dropped. (b) `SNDK` was fetched successfully but its returned daily close/volume series was **byte-identical to `MU`'s** despite distinct IBKR contract IDs — a data-lineage conflict, not a valid observation. `SNDK` was dropped and replaced with `COST` (Costco), which was verified non-duplicate against all other 32 fetched series. Both substitutions are logged here and in `01_preflight.md` / `08_risk_review.md`.

Rank within this 30-name set is labeled `SAMPLED_PCTL (n=30)` throughout `05_factor_scores.md`, `06_top_candidates.md`, `07_portfolio_proposal.md`, and `15_predictions.json`.

## Inclusion / Exclusion Filters

The 30 sampled names are all S&P 500 or Nasdaq-100 constituents with market cap far above the $2B floor, average daily dollar volume far above the $20M floor, price above $5, and listing age above 6 months — no name required an exclusion check for thin-ADR, halt, wide-spread, or low-session-count criteria (all are large, liquid, continuously-traded U.S. primary listings). No name in the 30-name sample was rejected; the two substitutions above were data-integrity exclusions, not inclusion-filter rejections.

## Coverage Summary

| Metric Group | Sourceable Count (of 30) | UNAVAILABLE Count | DQ / Confidence Effect | Notes |
| --- | --- | --- | --- | --- |
| Risk / return (beta, sigma, drawdown, Sharpe, Sortino, IR, Treynor, Kelly, VaR, CVaR) | 30 | 0 | Used in diagnostics and sizing | DERIVED from IBKR 5y daily history, 60d beta / 30d realized vol / 60d drawdown windows. |
| Technical / price (TD-9, RSI, MACD, MA, momentum, RS) | 30 | 0 | Used in `Tech_Z` | `technical_indicators.py` output, all 30 names `status: OK`. |
| Fundamental / revisions | 0 | 30 | Blocks investable status | No cross-sectional fundamental or analyst-revision feed wired this session. `Fund_Z = UNAVAILABLE` for all names. |
| Sentiment / positioning | 0 | 30 | Blocks investable status | No options IV, short-interest, or institutional-flow feed wired. `Sent_Z = UNAVAILABLE` for all names. |
| Next earnings date | 12 | 18 | Caps confidence; forces `DELAYED_PARTIAL` | Sourced via WebSearch for the top-12-ranked names only (scope-limited); remaining 18 `UNAVAILABLE`. |

Per `rules.md § Family Aggregation`, a family with fewer than two sourceable metrics is marked `UNAVAILABLE`, contributes `0.00 (UNAVAILABLE)` to the score, and does **not** count toward the "≥3 of 4 families non-negative" evidence-threshold test. With Fundamental and Sentiment both fully `UNAVAILABLE`, at most 2 of 4 families are ever available for any name — **no name in this sampled universe can clear the investable evidence threshold this run**, independent of Adj Score. This is disclosed identically in `03`, `05`, `08`, and `13`.

## Technical Indicator Coverage

Daily/weekly/monthly TD-9, RSI(14), MACD(12,26,9), MA alignment, momentum, volume ratio, and relative strength are available for all 30 sampled equities and the three core ETFs (33/33 `status: OK` in `technical_indicators.json`). No helper record is `UNAVAILABLE` this run; no field was hand-filled.
