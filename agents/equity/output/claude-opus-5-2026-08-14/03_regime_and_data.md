# 03 — Regime and Data · 2026-08-14

## Data-mode declaration

**`DELAYED`.** Every price in this package was fetched during this run; no real-time feed is
wired. The 2026-08-14 close is final at all three vendors and all five Required inputs are
grounded, which makes the run `GO`-eligible on data grounds
(`rules.md § Data Mode Taxonomy`). It is **not** `DELAYED_PARTIAL` — no Required input failed —
and it is **not** `ILLUSTRATIVE`.

| Check | Result |
|---|---|
| Symbols fetched | 519/519 in 14.3s |
| Last bar == basis | 518/519 (`EA` is the sole exception — delisted, see `04`) |
| Price-date checks grounded | 137/137, max deviation 0.000000% |
| Ex-div `c != a` on basis bar | 0 |
| Benchmark (SPY) history | 1255 daily bars |

## Regime classification — `BULL`

| Evidence | Value | Reading | Ledger |
|---|---|---|---|
| SPY vs MA20 / MA50 | 776.34 vs 756.20 / 748.55 | **ABOVE / ABOVE** | `L013` |
| SPY 20d / 60d momentum | +4.45% / +6.08% | positive on both horizons | `L013` |
| SPY drawdown from 60d high | -0.20% | at the highs | `L001` |
| SPY 30d realized vol | 3.55% vs 4.37% prior 30d | **FALLING** | `L002` |
| VIX | 14.25 (30d mean 16.56) | below its own 30d mean; calm | `L011` |
| SPY weekly / monthly MA alignment | BULLISH / BULLISH | bullish on both | `L013` |
| QQQ vs MA20 / MA50 | **ABOVE / ABOVE** | growth participating | `L013` |
| TLT vs MA20 / MA50 | BELOW / BELOW | rates firm, no rate shock | `L018` |
| 13-week T-bill | 3.71% | stable; no `RATE_SHOCK` trigger | `L012` |

**Call: `BULL`.** Trend is up on daily, weekly and monthly bars for SPY and QQQ, realized
volatility is contracting on every core ETF, VIX sits below its 30-day mean, and the index is
0.20% from its 60-day high. `HIGH_VOL` is not defensible with vol falling across the board;
`RATE_SHOCK` is not defensible with the bill rate stable at 3.71%.

**Counter-evidence, stated rather than buried.** SPY's daily TD-9 is at
`SELL_SETUP_9` — a completed sell setup and therefore an exhaustion/reversal flag —
and SPY's monthly RSI(14) is **76.79**, above the 70 overbought
line. Per `rules.md § TD-9 Definition` and `§ Technical Indicator Pack Definition` neither is a
standalone signal; together they are why the SPY mu carries **no upward adjustment** inside its
±1.0pp band.

## Event-concentration flags

| Check | Result |
|---|---|
| Names with a confirmed print inside the 37-day sweep window | 50 of 511 |
| Names penalised (print <= 14 days) | 31 of 511 |
| Penalised names inside the published set | 0 of 24 |
| `NO_TRADE` trigger #4 (> 2 published names with earnings <= 14d) | **not triggered** |
| FOMC inside horizon | no meeting scheduled between 2026-08-14 and 2026-09-11 |

Mid-August is a quiet window: Q2 season has finished and the off-cycle August/September
reporters (retail, NVDA, ORCL, ADBE) are still ahead. Early August by contrast penalised 153 of
512 names. The sweep is **complete** (26/26
business days, zero transport failures), so absence from it is positive evidence of no print in
window, not an unknown.

## Core ETF Market Forecast Block

| ETF | Entry Price | Price Date | Price Tag | Trend (20d/50d) | 30d RVol | Beta vs SPY | mu | sigma | Sigma Source | Target Price | Target Date | 70% CI Lo | 70% CI Hi | Confidence | Ledger Rows |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SPY | 776.34 | 2026-08-14 | `HISTORICAL` | ABOVE/ABOVE | 3.55% | 1.0000 | +2.00% | 3.55% | `REALIZED_VOL_30D` | 791.87 | 2026-09-11 | 763.24 | 820.50 | MEDIUM | `L015`, `L001`, `L013`, `L023` |
| QQQ | 731.07 | 2026-08-14 | `HISTORICAL` | ABOVE/ABOVE | 6.60% | 1.7437 | +2.99% | 6.60% | `REALIZED_VOL_30D` | 752.91 | 2026-09-11 | 702.77 | 803.05 | MEDIUM | `L016`, `L001`, `L013`, `L023` |
| SOXX | 550.42 | 2026-08-14 | `HISTORICAL` | ABOVE/BELOW | 15.73% | 3.5158 | +5.53% | 15.73% | `REALIZED_VOL_30D` | 580.87 | 2026-09-11 | 490.84 | 670.89 | MEDIUM | `L017`, `L001`, `L013`, `L023` |

### mu derivation (never free-handed)

| ETF | Rule | Computation | Adjustment applied | Final mu |
|---|---|---|---|---|
| SPY | regime prior, ±1.0pp | `BULL` -> +2.00% | **none** — trend supports the prior, but daily TD-9 `SELL_SETUP_9` and monthly RSI 76.79 argue against an upward adjustment; they offset | +2.00% |
| QQQ | beta x SPY mu, ±1.5pp | 1.7437 x +2.00% = +3.49% | **-0.50pp** — rs60 -1.75% vs SPY despite rs20 +0.69% | +2.99% |
| SOXX | beta x SPY mu, ±1.5pp | 3.5158 x +2.00% = +7.03% | **-1.50pp (band max)** — only core ETF below its MA50 and -15.97% from its 60d high | +5.53% |

**Known defect, disclosed rather than silently carried.** `mu = beta x SPY_mu` is a category
error: beta measures co-movement *magnitude*, not expected-return *direction*. With SOXX's beta
at 3.5158, a +2.00% SPY prior mechanically produces
+7.03% for SOXX, and the ±1.5pp adjustment band is too narrow
to bring that back to a plausible 4-week forecast — the band max still leaves
**+5.53%**. This is the diagnosed root cause of the
`MARKET_FORECAST` hit rate (32.17% rolling) and it cannot be repaired
here: the mu prior table is Track A, and Track A is gated at
`eff_n = 2 < 3` until 2026-09-07.
Two candidate replacements were tested and rejected on 2026-07-24. Recorded again in `13`.

### Analysis minimum and relative strength

| ETF | vs MA20 | vs MA50 | 30d RVol | vs prior 30d | Drawdown from 60d high | RS 20d vs SPY | RS 60d vs SPY | RSI(14) | TD-9 | MACD |
|---|---|---|---|---|---|---|---|---|---|---|
| SPY | ABOVE | ABOVE | 3.55% | FALLING (from 4.37%) | -0.20% | +0.00% | +0.00% | 65.76 | `SELL_SETUP_9` | `ABOVE_SIGNAL` |
| QQQ | ABOVE | ABOVE | 6.60% | FALLING (from 8.33%) | -1.91% | +0.69% | -1.75% | 59.60 | `SELL_SETUP_4` | `ABOVE_SIGNAL` |
| SOXX | ABOVE | BELOW | 15.73% | FALLING (from 21.60%) | -15.97% | +1.03% | +4.78% | 53.06 | `SELL_SETUP_4` | `ABOVE_SIGNAL` |

**Relative-strength note.** `QQQ/SPY` is +0.69% over 20d and
-1.75% over 60d; `SOXX/SPY` is +1.03% and
+4.78%. Semis are **outperforming** on both horizons while still
trading below their MA50 and -15.97% below the 60d high —
a recovering laggard, not a leader. That combination is why SOXX takes the full negative mu
adjustment on trend grounds even though its relative strength is positive.

**Regime-consistency check.** The `BULL` call is consistent with SPY and QQQ (both above MA20
and MA50, both with falling realized vol) and only partly with SOXX (above MA20, below MA50).
One of three core ETFs below its 50-day average is normal dispersion inside a bull tape, not a
contradiction of it.

## Universe handoff

511 scored names from the 515-name index union (`04` carries the full
inclusion/exclusion log), plus core ETFs `SPY`, `QQQ`, `SOXX` analysed separately as a
market-forecast sleeve. Core ETFs are **not** universe members: they do not count toward the
investable set, the 30-name minimum, percentile distributions or portfolio caps.

Ticker list handed to `technical_indicators.py`: the 515-name union plus
`SPY QQQ SOXX TLT` (TLT is required for the `rate_sens` Macro slot and the rate-shock check;
it is not a forecast sleeve member).

## Stop-rule assessment

| Rule | Triggered? | Note |
|---|---|---|
| `HALTED` — benchmark data missing | No | SPY history complete, 1255 bars |
| `HALTED` — unclear lineage on core fields | No | 137/137 price checks grounded; every metric ledgered |
| `HALTED` — > 20% of top candidates missing critical inputs | No | 0 of 24 |
| `HALTED` — index union unavailable | No | helper succeeded (515 names) |
| `REVIEW_ONLY` — data too stale for positioning | No | basis close is same-session and final |

Data and Regime recommends proceeding to factor scoring with data mode `DELAYED` and regime
`BULL`.
