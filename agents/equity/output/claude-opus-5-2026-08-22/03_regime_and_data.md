# 03 — Regime and Data · 2026-08-22

## Data-mode declaration

**`DELAYED`.** Every price used in this package was fetched by tool during this run; no real-time
feed is wired. The run fired Saturday 2026-08-22 at ~15:06 ET with markets closed, so the
**2026-08-21** (Friday) close is final at every vendor and serves as one consistent basis for
indicators, entry prices, and settlements alike.

All five Required inputs (`rules.md § Input Classification`) are grounded — see `01` for the
gate table. The mode is **not** `DELAYED_PARTIAL`: no Required input failed.

## Regime Classification

**Declared regime: `BULL`.**

| Evidence | Value | Ledger | Reading |
|---|---|---|---|
| SPY vs MA20 / MA50 | 765.72 vs 762.33 / 751.56 — above both, alignment `BULLISH` | L003, L013 | supports `BULL` |
| SPY 20d / 60d momentum | +3.63% / +2.29% | L013 | supports `BULL` |
| SPY drawdown from 60d high | -4.49% | L003d | not `BEAR` |
| SPY 30d realized vol (1m) | 3.56%, falling from 4.41% | L003b, L003c | not `HIGH_VOL` |
| VIX | 15.13 (prior close 16.01) | L007, L007a | not `HIGH_VOL`; supports `BULL` |
| SPY daily MACD | `BELOW_SIGNAL` | L013 | mild counter-evidence to `BULL` |
| SPY daily RSI(14) | 54.28 | L013 | neutral (30–70) |
| 3-month T-bill | 3.72% (2026-08-21) | L008 | no `RATE_SHOCK` signal |
| TLT daily MA alignment / 60d momentum | `BEARISH` / -2.68% | L006 | no `RATE_SHOCK` signal |

The one dissenting signal is SPY's daily MACD at `BELOW_SIGNAL` (histogram
-0.9447), while the weekly block reads `ABOVE_SIGNAL`. It is a
short-horizon crossover state against an otherwise unanimous trend, volatility, and VIX picture, and
it does not override the multi-signal read — `rules.md § Technical Indicator Pack Definition` explicitly treats
MACD as supportive-only, never standalone.

**Regime shift:** the prior same-model baseline (2026-07-24) declared `NEUTRAL`. The move to
`BULL` is driven by SPY reclaiming both moving averages, 20d momentum strengthening from
+0.63% to +3.63%, and VIX falling from 18.58 to 15.13. See `02 § 4`.

## Core ETF Market Forecast Block

Analysis minimum per `rules.md § Core ETF Market Forecast`, computed from 5 years of fetched daily
history per ETF (60 daily return intervals for beta and relative strength):

| ETF | 20d mom | 60d mom | Drawdown from 60d high | 30d RVol vs prior 30d | Direction | TD9 D | RSI14 D | MACD D |
|---|---|---|---|---|---|---|---|---|
| SPY | +3.63% | +2.29% | -4.49% | 3.56% vs 4.41% | FALLING | `BUY_SETUP_4` | 54.28 | `BELOW_SIGNAL` |
| QQQ | +4.27% | -2.09% | -11.22% | 6.34% vs 8.43% | FALLING | `BUY_SETUP_4` | 50.17 | `BEARISH_CROSS` |
| SOXX | -1.32% | -7.75% | -29.01% | 15.28% vs 21.44% | FALLING | `BUY_SETUP_4` | 44.94 | `ABOVE_SIGNAL` |

**mu derivation** (never free-handed). `SPY` takes the regime prior for `BULL`
(+2.00%, `rules.md` table). `QQQ` and `SOXX` take `beta_to_SPY x SPY mu`, then the
sanctioned ±1.5pp adjustment with a stated, ledger-backed relative view (L023, L024). The
adjustment rule was fixed **before** looking at the values so it is reproducible rather than
free-handed: *both RS20 and RS60 vs SPY negative -> -1.5pp; only RS60 negative -> -1.0pp; neither negative -> 0.0pp. SPY takes the regime prior unadjusted.*

| ETF | beta vs SPY (60d) | SPY mu | mu = beta x SPY mu | Adjustment | Final mu | Ledger-backed reason |
|---|---|---|---|---|---|---|
| SPY | 1.0000 | +2.00% | +2.00% | +0.0pp | +2.00% | regime prior applied unadjusted (SPY is the benchmark itself) |
| QQQ | 1.7144 | +2.00% | +3.43% | -1.0pp | +2.43% | RS60 negative (-4.28%) with RS20 +0.62% -> -1.0pp; 60d is the dominant horizon for a 4-week call |
| SOXX | 3.3339 | +2.00% | +6.67% | -1.5pp | +5.17% | both relative-strength horizons negative vs SPY (RS20 -4.77%, RS60 -9.81%) -> full -1.5pp band |

### Forecast block

| ETF | Entry Price | Price Date | Price Tag | Trend (20d/50d) | 30d RVol | Beta vs SPY | mu | sigma | Sigma Source | Target Price | Target Date | 70% CI Lo | 70% CI Hi | Confidence | Ledger Rows |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SPY | 765.72 | 2026-08-21 | `DELAYED` | 762.33 / 751.56 (`BULLISH`) | 3.56% (FALLING) | 1.0000 | +2.00% | 3.56% | `REALIZED_VOL_30D` | 781.03 | 2026-09-19 | 752.69 | 809.38 | MEDIUM | L003, L003a-d |
| QQQ | 713.44 | 2026-08-21 | `DELAYED` | 709.19 / 713.35 (`MIXED`) | 6.34% (FALLING) | 1.7144 | +2.43% | 6.34% | `REALIZED_VOL_30D` | 730.77 | 2026-09-19 | 683.70 | 777.84 | MEDIUM | L004, L004a-d |
| SOXX | 520.05 | 2026-08-21 | `DELAYED` | 525.12 / 558.76 (`BEARISH`) | 15.28% (FALLING) | 3.3339 | +5.17% | 15.28% | `REALIZED_VOL_30D` | 546.93 | 2026-09-19 | 464.29 | 629.56 | MEDIUM | L005, L005a-d |

**Relative strength** (L024): `QQQ/SPY` +0.62% over 20d and
-4.28% over 60d; `SOXX/SPY` -4.77% over 20d and
-9.81% over 60d.

**Regime-consistency check:** the block is consistent with the declared `BULL` call at the
index level — SPY is above both moving averages with falling realized vol and a VIX at
15.13 — while both growth proxies still trail the index on a 60-day view. This is a
broad-market advance that the growth complex has not yet led. Confidence is `MEDIUM` for all three:
`HIGH` requires trend, vol, and relative strength to align *and* data quality ≥ 0.90, and data
quality is 0.80 (L020).

**Sleeve isolation:** the three ETFs are a market-forecast sleeve. They are not candidates, are not
universe members, do not enter percentile distributions or portfolio caps, and are exempt from the
single-name universe filters.

## Event concentration

The forward earnings sweep (L010) covers **26 business days**,
2026-08-24 … 2026-09-28, with **26** fetched and zero transport
failures — a complete sweep, so absence is positive evidence.

- Names with a confirmed print inside the 14-day penalty window: **29** of 509 scored.
- Names with a confirmed print anywhere in the 37-day window: **43**.
- Names with `NO_PRINT_IN_WINDOW`: **466**.

Late August sits between quarterly reporting seasons, so the earnings-risk backdrop is unusually
light — a marked contrast with the 153-of-512 penalty count recorded on 2026-08-03 at the peak of
Q2 season. **No name in the published 24 carries an earnings penalty**, and the
`rules.md § Downgrade to NO_TRADE` #4 trigger (more than 2 published names printing inside 14 days)
is not met.

No FOMC meeting falls inside the 28-day forecast horizon per the run's macro inputs; this is
recorded as an absence of positive evidence, not as a fetched calendar.

## Universe handoff

The exact ticker list handed to `technical_indicators.py` was the 515-name index union
plus the four ETFs `SPY QQQ SOXX TLT` — 519 symbols, of which
**518** returned history and **1** failed (L002). Details in `04`.

## Stop-rule assessment

No `HALTED` condition is met: benchmark data is present and grounded, lineage is clear for every
core field, the index-union universe materialised, and no fabricated or contradictory evidence was
found. The Data/Regime stage recommends proceeding to factor scoring at data quality
**0.80** with confidence capped, and flags in advance that evidence threshold #2
cannot be satisfied by any name because `Fund_Z` and `Sent_Z` are `UNAVAILABLE` universe-wide.
