# 03 — Regime and Data · 2026-09-03

## Data-mode declaration

**`DELAYED`** per `rules.md § Data Mode Taxonomy`: every quote used was fetched during this run
from the completed 2026-09-03 session, cross-checked across independent sources, and carries a
retrieval timestamp (L002, L011, L012, L012a). Not `LIVE` (no real-time feed is wired) and not
`DELAYED_PARTIAL` (no Required input is missing — see the `01` GO-Gate Table).

## Regime classification: **`BULL`**

| Evidence test | Result | Ledger |
|---|---|---|
| SPY close vs MA20 | 773.17 vs 769.21 — above | L003, L002 |
| SPY close vs MA50 | 773.17 vs 756.14 — above | L003, L002 |
| SPY 60d momentum | +5.17% | L002 |
| SPY drawdown from 60d high | -0.61% | L003d |
| SPY 30d realized vol vs prior 30d | 3.30% vs 4.12% — falling | L003b, L003c |
| VIX close | 14.32 (T-1 15.2) | L007, L007a |
| 3m T-bill | 3.75% annual | L008 |

**7 of 7** classification tests read
bullish. SPY sits above both its 20- and 50-day averages with positive 60-day momentum, VIX at
14.32 is deep inside the low-volatility band, realized volatility is
falling, and the index is
-0.61% from its own 60-day high. No `HIGH_VOL`,
`RATE_SHOCK` or `BEAR` trigger fires. The call is **`BULL`**, which sets the SPY
4-week prior at **+2.00%** from the `rules.md § Core ETF Market Forecast` table.

## Core ETF Market Forecast Block

Sleeve isolation applies: SPY, QQQ and SOXX are a market-forecast sleeve, never candidates, never
universe members, and exempt from the single-name filters.

| ETF | Entry Price | Price Date | Price Tag | Trend (20d/50d) | 30d RVol | Beta vs SPY | mu | sigma | Sigma Source | Target Price | Target Date | 70% CI Lo | 70% CI Hi | Confidence | Ledger Rows |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SPY | 773.17 | 2026-09-03 | `DELAYED` | above / above | 3.30% (falling) | 1.0000 (self) | +2.00% | 3.30% | `REALIZED_VOL_30D` | 788.63 | 2026-10-01 | 762.10 | 815.17 | MEDIUM | L003, L003a, L003b |
| QQQ | 717.67 | 2026-09-03 | `DELAYED` | below / above | 5.71% (falling) | 1.7006 | +1.90% | 5.71% | `REALIZED_VOL_30D` | 731.31 | 2026-10-01 | 688.68 | 773.95 | MEDIUM | L004, L004a, L004b |
| SOXX | 502.20 | 2026-09-03 | `DELAYED` | below / below | 13.88% (falling) | 3.2402 | +4.98% | 13.88% | `REALIZED_VOL_30D` | 527.21 | 2026-10-01 | 454.74 | 599.68 | MEDIUM | L005, L005a, L005b |

### mu derivation (never free-handed)

| ETF | Derivation | Adjustment band |
|---|---|---|
| SPY | regime prior for BULL; no adjustment applied | ±1.0pp |
| QQQ | beta 1.7006 x SPY mu +2.0000% = +3.4012%; relative-view adjustment -1.5% (both RS20 and RS60 negative vs SPY) | ±1.5pp |
| SOXX | beta 3.2402 x SPY mu +2.0000% = +6.4804%; relative-view adjustment -1.5% (both RS20 and RS60 negative vs SPY) | ±1.5pp |

The QQQ/SOXX relative-view adjustment follows a mapping **fixed before the values were read**
(the 2026-08-22 discipline, restated here so it cannot be read as free-handed):
`both RS20 and RS60 negative -> -1.5pp; only RS60 negative -> -1.0pp; only RS20 negative -> -0.5pp; neither -> 0.0pp`.

### Relative strength and consistency check

| Pair | 20d | 60d | Reading |
|---|---|---|---|
| QQQ / SPY | -0.18% | -3.67% | growth is tracking the index over 20d and lagging over 60d |
| SOXX / SPY | -6.29% | -15.79% | semis are lagging badly on both horizons |
| TLT / SPY | -0.76% | -7.63% | long duration is lagging equities — consistent with a risk-on tape, not a rate shock |

**Consistency note.** A `BULL` call with VIX at 14.32 and SPY above both
moving averages is internally consistent. There is one *known* inconsistency inside the ETF block
itself, and it is a mechanical property of the mu rule rather than a judgment: SOXX is the weakest
of the three on relative strength (RS60 -15.79%) yet carries the
**highest** mu (+4.98%), because `mu = beta x SPY_mu` scales with beta
(3.2402) and the permitted ±1.5pp adjustment cannot overcome it.
This is the category error diagnosed on 2026-07-24 — beta measures co-movement magnitude, not
expected-return direction. It is carried, disclosed, and revisited in `13`, where the
`MARKET_FORECAST` Track A gate is checked.

## Event-concentration flags

| Flag | Value | Threshold | Status |
|---|---|---|---|
| Names in the scored universe printing inside 14 days | 10 of 508 | n/a — universe-level context | informational |
| Published names printing inside 14 days | 0 | > 2 triggers NO_TRADE #4 | **PASS** |
| Forward calendar sweep completeness | 27/27 business days, 0 failures | must be complete for absence to count as evidence | **PASS** |

Earnings density across the swept window (issuers per business day, whole tape):

| Date | Issuers | Date | Issuers | Date | Issuers |
|---|---|---|---|---|---|
| 2026-09-03 | 50 | 2026-09-16 | 10 | 2026-09-29 | 5 |
| 2026-09-04 | 15 | 2026-09-17 | 7 | 2026-09-30 | 3 |
| 2026-09-07 | 7 | 2026-09-18 | 1 | 2026-10-01 | 8 |
| 2026-09-08 | 29 | 2026-09-21 | 12 | 2026-10-02 | 0 |
| 2026-09-09 | 45 | 2026-09-22 | 6 | 2026-10-05 | 21 |
| 2026-09-10 | 24 | 2026-09-23 | 8 | 2026-10-06 | 5 |
| 2026-09-11 | 7 | 2026-09-24 | 14 | 2026-10-07 | 8 |
| 2026-09-14 | 8 | 2026-09-25 | 4 | 2026-10-08 | 14 |
| 2026-09-15 | 5 | 2026-09-28 | 7 | 2026-10-09 | 4 |

Early September is a genuine earnings trough: only **10** of 508 scored
names print inside the 14-day penalty window, and **0** of the 24 published
names do.

## Universe handoff

`build_index_universe.py` succeeded, so the normal index-union path applies and the Sampled
Universe Protocol is **not** used. The exact ticker list handed to `technical_indicators.py` is
the 518-symbol set with fetched history (universe names plus SPY/QQQ/SOXX/TLT); full
construction and the rejection log are in `04`.

## Stop-rule check

| Rule | Condition | Result |
|---|---|---|
| Hard halt 1 | benchmark data missing outside illustrative mode | not triggered — SPY has 1255 daily bars (L002, L003) |
| Hard halt 2 | unclear lineage on price/volume/beta/earnings date | not triggered — every downstream field has a `01` ledger row |
| Hard halt 3 | > 20% of top-ranked candidates with unresolved missing critical inputs | not triggered — 0 of 24 published names has an ungrounded Required input |
| Hard halt 4 | index union cannot be materialized | not triggered — union 515 built from local caches (L001) |
| Hard halt 5 | caps unreachable for process/data-integrity reasons | not triggered — see `07`; the beta band is *feasible* this run |
| Hard halt 6 | fabricated or contradictory evidence | not triggered — see `08` |

Recommendation to the orchestrator: **proceed to scoring**; data is sufficient for analysis and
for settleable forecasts, and the run's status is decided downstream on candidate quality.
