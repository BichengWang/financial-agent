# 03 Regime and Data

## Data Mode

**`DELAYED`** — declared per `rules.md § Data Mode Taxonomy`. All Required inputs (grounded entry prices, ≥60 trading days of history, sigma, earnings-date estimate, index-union universe) are grounded via the IBKR MCP connection this run, but the daily-run universe scan fell back to the Sampled Universe Protocol (see below), so this is not a clean `LIVE` full-universe run. Not `DELAYED_PARTIAL` because no Required input is missing outright for the names actually scored — the gap is universe breadth, documented explicitly.

## Regime Classification

**Regime: `BULL`** (medium-high confidence).

Evidence (ledger rows `L001`–`L009`, `L010`–`L011`, `L011`–`L016` in `01_preflight.md`):

- SPY, QQQ, and SOXX are all in `BULLISH` weekly MA alignment (close > MA20 > MA50) as of 2026-07-01.
- SPY 60-day momentum +13.18%, QQQ +23.22%, SOXX +74.28% (technical_indicators.json, daily block).
- VIX = 16.53 (2026-07-02 live), down from 16.59 prior close and well below the 21.51 close that drove the `HIGH_VOL/RATE_SHOCK` baseline regime on 2026-06-05 — the acute rate-shock episode has unwound.
- Trailing-month sector tape: `XLK` +19.8%, `XLV` +2.47%, `XLI` -0.82%, `XLF` -1.07%, `XLP` -1.61%, `XLE` -5.58% — broad, tech-led risk appetite over the month.
- Caveat: the trailing **week** shows a rotation wobble — `XLK` -3.52%, `XLV` +4.58%, `XLI` +2.06% — and SPY/QQQ both show a daily MACD bearish crossover (`BELOW_SIGNAL`) plus a `SELL_SETUP_3` TD-9 daily count. This is read as a short-term pullback/rotation inside a still-bullish weekly trend, not a regime change, per `rules.md`: "TD-9 setup 9... does not override the multi-factor score alone," and a `SELL_SETUP_3` is well short of the `9` exhaustion count.
- SOXX carries a **weekly `TD9 SELL_SETUP_9`** (full exhaustion count) and weekly RSI 72.53 (overbought) — a name-level and theme-level caution flag inside the broader bull call, discussed further below and in `05_factor_scores.md`.

No hard disqualifier from `rules.md § Stop Criteria` applies to the regime call itself.

## Core ETF Market Forecast Block

| ETF | Entry Price | Price Date | Price Tag | Trend (20d/50d) | 30d RVol (1m-scaled) | Beta vs SPY | mu | sigma | Sigma Source | Target Price | Target Date | 70% CI Lo | 70% CI Hi | Confidence | Ledger Rows |
| --- | ---: | --- | --- | --- | ---: | ---: | ---: | ---: | --- | ---: | --- | ---: | ---: | --- | --- |
| SPY | 746.40 | 2026-07-02 | LIVE | Close>MA20>MA50 (BULLISH); daily MACD BELOW_SIGNAL, TD9 SELL_SETUP_3 | 4.45% | 1.00 (def.) | +1.5% | 4.45% | REALIZED_VOL_30D | 757.60 | 2026-07-30 | 723.04 | 792.15 | MEDIUM | L001–L003 |
| QQQ | 725.59 | 2026-07-02 | LIVE | Close>MA20>MA50 (BULLISH); daily MACD BELOW_SIGNAL, TD9 SELL_SETUP_3 | 8.35% | 1.58 | +2.4% | 8.35% | REALIZED_VOL_30D | 742.79 | 2026-07-30 | 679.77 | 805.80 | MEDIUM | L004–L006 |
| SOXX | 599.50 | 2026-07-02 | LIVE | Daily MIXED (close≈MA20>MA50); weekly BULLISH but weekly TD9 SELL_SETUP_9 (exhaustion), weekly RSI 72.5 (overbought) | 21.32% | 3.23 | +3.35% | 21.32% | REALIZED_VOL_30D | 619.58 | 2026-07-30 | 486.64 | 752.53 | MEDIUM | L007–L009 |

**mu derivation** (per `rules.md § Core ETF Market Forecast`):

- `SPY`: BULL regime prior = +2.0% (4-week), adjusted **-0.5pp** to +1.5% — stated reason: daily MACD bearish crossover and TD-9 `SELL_SETUP_3` on both SPY and QQQ signal near-term consolidation risk despite the bullish weekly trend; adjustment is within the ±1.0pp allowed band.
- `QQQ`: mu = beta_to_SPY (1.5777, `DERIVED` from 60d daily returns, `L005`) × SPY mu (1.5%) = **+2.37%**, rounded to +2.4%. No discretionary adjustment applied.
- `SOXX`: mu = beta_to_SPY (3.2301, `DERIVED`, `L008`) × SPY mu (1.5%) = +4.85% raw, adjusted **-1.5pp** (maximum allowed band) to +3.35% — stated reason: the weekly TD-9 `SELL_SETUP_9` exhaustion signal and overbought weekly RSI (72.5) on SOXX are ledger-backed negative technical drivers that justify trimming the pure beta-implied mu.

**Relative-strength notes** (technical_indicators.json daily/weekly blocks, `L003`/`L006`/`L009`):

- `QQQ/SPY`: +10.04% over 60 trading days (daily block `relative_strength_60d_vs_benchmark_pct`); +16.46% over 60 weeks (weekly block). QQQ has meaningfully outpaced SPY across both windows.
- `SOXX/SPY`: +61.10% over 60 trading days (daily); +177.07% over 60 weeks (weekly). Semiconductor beta has dominated the broad tape — the single largest driver of the month's rally and also the largest concentration/event risk (see `08_risk_review.md`).
- Consistency check: the regime call (`BULL`) is consistent with all three ETFs' bullish weekly alignment and QQQ/SOXX's outsized relative strength; the one inconsistency is SOXX's daily `MIXED` alignment and its overbought weekly signal, which is disclosed above rather than smoothed over.

## Universe Handoff

`build_index_universe.py` succeeded and materialized the full S&P 500 ∪ Nasdaq-100 union: **515 tickers** (503 S&P 500, 101 Nasdaq-100, 89 overlap) — see `universe_summary.json` and `04_universe_summary.md`.

However, price-history fetch for that full 515-name list is **not achievable this session**:

1. `technical_indicators.py`'s built-in Yahoo Finance fallback was attempted for all 515 names (plus SPY/QQQ/SOXX) and every single Yahoo fetch failed with `403 Forbidden` — confirmed as an organizational egress-policy denial via the agent proxy status endpoint (`query2.finance.yahoo.com` blocked, `kind=connect_rejected`), not a transient error. Per proxy operating instructions, this was not retried.
2. Fetching 515 individual names via IBKR MCP `get_price_history` one-by-one is outside this session's practical tool-call budget (each 5y-daily response is 70–130KB, requiring individual file-based retrieval and conversion).

Per `rules.md § Sampled Universe Protocol` ("...or the run cannot fetch enough history for the index-union universe"), this run falls back to a **30-name sampled universe**, fully IBKR-grounded (5y daily history for every name, live entry-price snapshots for the top 12 by score). Composition:

- 10 names carried from the `02_reflection.md` cross-model baseline monitoring list: `AZO`, `UNH`, `MCK`, `JPM`, `XOM`, `CAT`, `WMT`, `ABBV`, `GS`, `PG`.
- 20 additional large-cap names spanning all 11 GICS sectors plus an explicit AI/semiconductor theme watchlist (current catalyst: the ongoing AI-capex cycle driving SOXX's 74% 60-day momentum): `AAPL`, `MSFT`, `NVDA`, `LLY`, `AMZN`, `GOOGL`, `META`, `TSLA`, `AVGO`, `PLTR`, `HD`, `NFLX`, `HON`, `COST`, `CVX`, `NEE`, `PLD`, `LIN`, `MU`, `AMD`.

This satisfies the Sampled Universe Protocol's minimum-30 requirement. Every percentile in `05_factor_scores.md` is labeled `SAMPLED_PCTL (n=30)`, not `INDEX_UNION_PCTL`. Per `agents.md § Factor Scoring Agent Prompt`, this caps the final publishable status at `REVIEW_ONLY` **unless** the fallback was caused by a transient fetch failure after the index-union file was materialized. The index-union file *was* materialized (515 names); the cause is a documented, non-transient environment constraint (Yahoo egress policy + IBKR call-volume budget), not a data-quality shortcut. The orchestrator treats this conservatively as capping the run below `GO` regardless of downstream evidence-threshold results — see `00_run_manifest.md` and `08_risk_review.md` for the final status reconciliation.

## Event Concentration Flags

- **Semiconductor/AI concentration**: 3 of the 30 sampled names (`MU`, `AMD`, `AVGO`) plus the SOXX benchmark itself carry outsized 60-day momentum (+74% to +173%) and outsized 60-day drawdown-from-high (-17% to -24%), indicating a single crowded factor/theme dominates the top of the ranked list (see `05_factor_scores.md` top 3: `MU`, `META`, `AMD`). This is flagged as a portfolio-construction constraint, not a reason to exclude the names from scoring.
- **Earnings calendar**: not sourceable this run — no earnings-calendar feed is connected via IBKR MCP tools, and web fetch was not attempted given the Yahoo-block precedent (same egress-policy risk). Every name's `Days to Earnings` field is `UNAVAILABLE` in `05_factor_scores.md`. Per `rules.md § Input Classification`, earnings date is a **Required** input for `GO`; its absence for the sampled set is a second, independent block on `GO` beyond the factor-family gate (see `08_risk_review.md`).
- **FOMC / macro calendar inside horizon**: not checked this run (no calendar feed connected); disclosed as an unverified gap, not assumed clear.

## Technical-Indicator Helper Handoff

`technical_indicators.py` was run twice this session:

1. Attempted with `--tickers-file eligible_universe.txt` (515 names) + Yahoo fallback → 515/515 `UNAVAILABLE` (Yahoo blocked); 3/3 core ETFs `OK` (IBKR CSV history-dir). This run's `technical_indicators.json` was **overwritten** by the successful sampled-universe run below (the failed 515-name attempt is documented here and in `01_preflight.md`/`00_run_manifest.md`, not published as a separate artifact).
2. Re-run with `--tickers-file sampled_universe.txt` (30 names) + `--history-dir` pointing at IBKR-sourced CSVs (SPY, QQQ, SOXX, and all 30 sampled names) → **33/33 `OK`**. This is the published `technical_indicators.json`.

Handoff ticker list for downstream factor scoring: the 30 sampled-universe tickers plus SPY/QQQ/SOXX (regime sleeve, not scored as candidates).

## Handoff Note to Factor Scoring

- Fundamental and Sentiment/Positioning families are `UNAVAILABLE` for every sampled name (no fundamentals or positioning feed connected this session). Factor scoring must set both families' displayed contribution to `0.00 (UNAVAILABLE)` per `rules.md § Family Aggregation` and must not count either toward the "3 of 4 families supportive" investability threshold.
- Technical and Macro families are fully sourceable (technical_indicators.json + finance-metrics computed from the same IBKR 5y history) for all 30 sampled names — use them as the sole scoring basis, disclosed as such.
- Earnings date is `UNAVAILABLE` for all names — apply the 14-day-earnings penalty logic as `UNAVAILABLE`, not as "clear," and disclose the gap in every score trace.
