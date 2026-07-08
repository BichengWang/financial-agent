# 03 Regime and Data

## Data Mode

**`DELAYED_PARTIAL`** — grounded IBKR quotes/history fetched this run for all core ETFs and the 30-name sampled universe, but one Required input (next earnings date, `rules.md § Input Classification` item 4) is missing for 18 of 30 sampled names (documented fetch-scope limitation in `01_preflight.md`, `00_run_manifest.md`). Per `rules.md § Data Mode Taxonomy`, a missing Required input under delayed quotes forces `DELAYED_PARTIAL` → `REVIEW_ONLY`-eligible on that dimension alone; separately, the factor-family gate (below) forces `NO_TRADE` regardless. See `09_final_report.md` for the final single-status resolution.

## Regime Classification: `BULL` (confidence: MEDIUM)

Evidence (all ledger-backed, `01_preflight.md` rows L004–L019):

| Signal | Value | Reading |
| --- | --- | --- |
| VIX close (2026-07-02) | 16.15 (L004) | Low-volatility regime (well under the ~20 HIGH_VOL heuristic threshold) |
| VIX 30d trailing average trend | 18.52 → 17.57 → 16.15 (three successive 30d windows, L005) | Falling — volatility compressing, not expanding |
| SPY trend vs 20d/50d MA | Close 744.78 > MA20 741.08 > MA50 737.43 (daily); weekly/monthly MA alignment `BULLISH` | Bullish |
| QQQ trend vs 20d/50d MA | Close 712.60 < MA20 721.10 > MA50 709.15 (daily, `MIXED`); weekly/monthly MA alignment `BULLISH` | Mixed daily, bullish weekly/monthly |
| SOXX trend vs 20d/50d MA | Close 566.32 < MA20 597.79 > MA50 545.63 (daily, `MIXED`); weekly/monthly `BULLISH` | Mixed daily, bullish weekly/monthly |
| SPY/QQQ/SOXX 60d momentum | +12.98% / +21.07% / +62.85% | Strongly positive across all three — durable uptrend |
| SPY/QQQ/SOXX 20d momentum | -1.25% / -4.25% / -8.02% | Negative — a near-term pullback/consolidation inside the larger uptrend |

**Regime-consistency note:** The 20d/daily picture (mixed MA alignment, negative 20d momentum on QQQ/SOXX) is a near-term pullback, not a regime change — 60d momentum, weekly/monthly MA alignment, and a falling VIX all confirm the broader `BULL` trend. Confidence is capped at `MEDIUM` (not `HIGH`) specifically because of this daily-vs-monthly divergence.

## Event Concentration

No FOMC or index-rebalance date was checked against the 2–6 week horizon this run (no economic-calendar feed wired). Earnings concentration: of the 12 ranked sampled names with a sourced next-earnings date, none fall within 14 calendar days of 2026-07-03 (nearest is `INTC` at 20 days) — no earnings-penalty trigger this run (`05_factor_scores.md`).

## Core ETF Market Forecast Block (SPY · QQQ · SOXX)

Per `rules.md § Core ETF Market Forecast`. ~5y daily history fetched per ETF via IBKR (`01` rows L006–L019); mu derivation follows the regime-prior table (never free-handed).

| ETF | Entry Price | Price Date | Price Tag | Trend (20d/50d) | 30d RVol | Beta vs SPY | mu | sigma | Sigma Source | Target Price | Target Date | 70% CI Lo | 70% CI Hi | Confidence | Ledger Rows |
| --- | ---: | --- | --- | --- | ---: | ---: | ---: | ---: | --- | ---: | --- | ---: | ---: | --- | --- |
| SPY | 745.76 | 2026-07-03 | DELAYED | Bullish (close>MA20>MA50, daily+weekly+monthly) | 4.41% | 1.00 (benchmark) | +2.0% | 4.41% | REALIZED_VOL_30D | 760.68 | 2026-07-31 | 726.44 | 794.91 | MEDIUM | L006,L007,L008 |
| QQQ | 725.17 | 2026-07-03 | DELAYED | Mixed daily (close<MA20>MA50); bullish weekly/monthly | 8.47% | 1.589 (DERIVED, 60d) | +3.2% | 8.47% | REALIZED_VOL_30D | 748.38 | 2026-07-31 | 684.48 | 812.28 | MEDIUM | L009,L010,L011 |
| SOXX | 599.70 | 2026-07-03 | DELAYED | Mixed daily (close<MA20>MA50); bullish weekly/monthly | 21.96% | 3.273 (DERIVED, 60d) | +5.0% | 21.96% | REALIZED_VOL_30D | 629.69 | 2026-07-31 | 492.69 | 766.68 | MEDIUM | L012,L013,L014 |

**mu derivation detail:**
- `SPY`: regime prior for `BULL` = +2.0% (`rules.md § Core ETF Market Forecast` table), unadjusted.
- `QQQ`: `beta_to_SPY (1.589, DERIVED from 60d daily returns, L009) × SPY mu (2.0%) = +3.18%`, rounded to +3.2%, unadjusted.
- `SOXX`: raw `beta_to_SPY (3.273, DERIVED, L012) × SPY mu (2.0%) = +6.55%`. Adjusted **-1.5pp** (maximum allowed band) to +5.0% on a stated, ledger-backed reason: SOXX monthly RSI(14) = 75.4 (overbought) and monthly TD-9 = `SELL_SETUP_9` (exhaustion flag) after a +62.85% 60-day rally (L012–L014) — the raw beta-scaled projection is tempered for late-cycle exhaustion risk within the sector-momentum leg of the `BULL` call.

**Relative-strength notes (from `technical_indicators.json`):** QQQ/SPY relative strength: +8.09% (60d), -3.0% (20d) — QQQ outperformed SPY over 60d but underperformed over the most recent 20d pullback. SOXX/SPY relative strength: +49.87% (60d), -6.77% (20d) — SOXX vastly outperformed on the 60d window (semis led the rally) but gave back more than the broad market in the recent 20d consolidation, consistent with the overbought/exhaustion read above.

**Sleeve isolation:** SPY, QQQ, and SOXX are a market-forecast sleeve only — they do not count toward the 5–10 investable set, the 30-name sampled-universe minimum, percentile distributions, or portfolio caps.

## Universe Handoff

`build_index_universe.py` succeeded: 515-ticker S&P 500 ∪ Nasdaq-100 union (`eligible_universe.txt`, `universe_summary.json`; `01` rows L001–L003). Per the documented Sampled Universe Protocol fallback (`01_preflight.md`), price-history fetch and technical-indicator computation used a 30-name subset (`sampled_universe.txt`) — see `04_universe_summary.md` for construction detail and full rejection/inclusion accounting.

## Ledger Coverage Gaps Affecting Scoring

- Fundamental family (earnings-revision momentum, revenue acceleration, margin trajectory, FCF yield, ROIC/ROE, leverage, valuation): 0/30 sourceable — no cross-sectional fundamental feed wired this session. `Fund_Z = UNAVAILABLE` for all 30 names.
- Sentiment/positioning family (short-interest change, options-skew, analyst revisions, insider buying, institutional ownership trend): 0/30 sourceable — no such feed wired. `Sent_Z = UNAVAILABLE` for all 30 names.
- Next earnings date: 12/30 sourced (top-12 by Adj Score, via WebSearch cross-checked against company IR / SEC 8-K / earnings-calendar aggregators); 18/30 `UNAVAILABLE` (fetch-scope limitation, not attempted).

## Handoff Note for Factor Scoring

Technical/Price and Macro/Regime families are fully sourceable (`technical_indicators.json` + DERIVED 60d beta/sigma/drawdown bundle) for all 30 sampled names; Fundamental and Sentiment/Positioning families are UNAVAILABLE universe-wide. Per `rules.md § Evidence Thresholds` item 2 ("at least 3 of 4 factor families are non-negative," with UNAVAILABLE families excluded from that count), **no name in this sampled universe can reach the investable evidence threshold this run**, independent of its Adj Score. Factor Scoring should rank the sampled universe on the two available families for monitoring-sleeve purposes only and recommend `NO_TRADE` for the investable sleeve.
