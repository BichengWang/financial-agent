# 03 Regime and Data — 2026-07-24

## Data Mode Declaration

**`DELAYED`** per `rules.md § Data Mode Taxonomy`. Quotes fetched this run with ≤1-day lag — in fact zero lag: the run fired ~23:17 ET, roughly 7¼ hours after the 16:00 ET close, and every bar carries the 2026-07-24 official close. All five Required inputs are grounded (`00 § GO-Gate Table`), so the run is `GO`-eligible on data grounds at reduced exposure; it publishes `NO_TRADE` on the evidence threshold instead.

Not `DELAYED_PARTIAL`: no Required input is missing. Not `ILLUSTRATIVE`: nothing here comes from reference state.

## Data Coverage and Lineage

| Check | Result |
|---|---|
| Universe names with ≥60 trading days of fetched history | 514 / 515 (`FDXF` excluded — 41 bars since 2026-05-27) |
| Names with a 2026-07-24 bar | 514 / 514 scored |
| Bars per name | 1,255–1,307 (≈5 years); target lookback of 252 days comfortably exceeded |
| Benchmark (SPY) history | 1,307 bars, last 2026-07-24 — present, so no `REVIEW_ONLY` fallback on computed-analytics grounds |
| Technical indicator pack | 517 / 518 records `OK` (`FDXF` `UNAVAILABLE`) |
| Entry prices independently verified | 29 / 29 at 0.000% max difference across 3 sources |
| Lineage gaps affecting scoring | `Fund_Z`, `Sent_Z` `UNAVAILABLE` universe-wide (L144, L145); all Enhancing inputs `UNAVAILABLE` (L146) |

## Regime Classification

**Declared regime: `NEUTRAL`.**

| Evidence | Value | Ledger | Points toward |
|---|---|---|---|
| SPY drawdown from 60d high | −2.72% | L001-series | not `BEAR` |
| SPY 60d / 20d momentum | +3.83% / +0.63% | `technical_indicators.json` | not `BEAR` |
| SPY vs MA20 / MA50 | 738.93 vs 746.15 / 745.07 — **below both**, alignment `MIXED` | `technical_indicators.json` | not `BULL` |
| SPY MACD | daily `BELOW_SIGNAL`; weekly `BEARISH_CROSS` | `technical_indicators.json` | not `BULL` |
| SPY daily TD-9 | `BUY_SETUP_7` | `technical_indicators.json` | downtrend maturing, exhaustion approaching |
| SPY 30d realized vol | 3.92% monthly (≈13.5% annualised), rising from 3.75% | L001-series | not `HIGH_VOL` |
| VIX | 18.58; avg20 16.83, avg60 17.36; only **3.3%** of the last 60 sessions closed above 20 | L137 | not `HIGH_VOL` |
| Breadth | 54.5% above MA20; 64.6% above MA50; median 20d momentum **+1.64%**; 58.9% positive | L139 | not `BEAR` |
| Rates | TLT −4.69% (20d), −3.61% (60d); 13-week bill **3.81%**, stable | L136, L138 | pressure, but not `RATE_SHOCK` |

**Why not the alternatives.** `BEAR` fails on a −2.7% index drawdown with positive 60-day momentum and majority-positive breadth. `HIGH_VOL` fails on SPY realized vol near 13.5% annualised and a VIX that has closed above 20 on 2 of the last 60 sessions. `RATE_SHOCK` is the closest rejected call — TLT −4.69% over a month is a real bond drawdown and is visibly the mechanism repricing long-duration equities — but the front end is stable at 3.81% and the move is an ordinary repricing, not a shock; calling it one would overstate the evidence.

**What the label does not capture, and must be stated explicitly:** beneath a flat index there is a violent internal rotation. SOXX is −19.54% from its 60-day high and −16.34% against SPY over 20 days; QQQ is −8.30% from its high; meanwhile **40.9% of the 514 scored names now carry a negative 60-day beta to SPY, with a median beta of just +0.232** (L140). A negative-beta plurality is the arithmetic signature of an index whose path is set by a narrow cohort moving opposite to the average constituent. `NEUTRAL` is the honest index-level label; the dispersion underneath it is the actual story and is what drives today's leaderboard.

## Event Concentration Flags

- **Earnings: severe.** 29 of the 48 confirmed dates on the shortlist fall inside 14 calendar days — the peak of the Q2 cycle. 12 of the 26 published names are inside the window and carry the `-0.10` penalty with confidence capped `LOW`. This alone trips `rules.md § Downgrade to NO_TRADE` condition #4 ("more than 2 names with earnings inside 14 calendar days") for any candidate portfolio drawn from this set.
- **Reporting already absorbed:** 22 shortlist names printed within the last 12 sessions (identified by move/volume signature, `01 § Earnings Resolution`), including TRV (+9.22% on 07-17), LMT (+10.54% on 07-23), DGX (+8.61% on 07-23), TMO (+8.71% on 07-23), RTX (+7.33% on 07-23), PKG (+8.76% on 07-24) and GOOGL (−7.13% on 07-23). Several of today's top ranks are therefore **post-print** — the catalyst is behind them, which is a genuine signal-decay risk flagged in `05`.
- **FOMC:** no meeting date is sourced this run; treated as `UNAVAILABLE` rather than assumed absent from the 28-day horizon.
- **Month-end:** 2026-07-31 is the last trading day of July and falls inside the horizon; index-rebalance and window-dressing flow is unmodelled.

## Core ETF Market Forecast Block

Sleeve isolation applies: SPY, QQQ, SOXX are a market-forecast sleeve. They are never candidates, never universe members, never counted in percentiles or portfolio caps.

**Analysis minimum** (per ETF, ledger-backed, from ~1,300 fetched daily bars each):

| ETF | Entry | Px Date | Tag | Trend (20d/50d) | 30d RVol | RVol Trend | Beta vs SPY | DD from 60d High | mu | sigma | Sigma Src | Target | Target Date | CI70 Lo | CI70 Hi | Conf |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SPY | 738.93 | 2026-07-24 | DELAYED | MA20 746.15 / MA50 745.07 (MIXED) | 3.92% | RISING | 1.0000 | -2.72% | +0.00% | 3.92% | REALIZED_VOL_30D | 738.93 | 2026-08-21 | 708.82 | 769.04 | MEDIUM |
| QQQ | 684.23 | 2026-07-24 | DELAYED | MA20 711.71 / MA50 718.29 (BEARISH) | 7.96% | RISING | 1.7222 | -8.30% | -1.00% | 7.96% | REALIZED_VOL_30D | 677.39 | 2026-08-21 | 620.75 | 734.03 | MEDIUM |
| SOXX | 527.01 | 2026-07-24 | DELAYED | MA20 565.45 / MA50 569.22 (BEARISH) | 20.18% | RISING | 3.6366 | -19.54% | -1.50% | 20.18% | REALIZED_VOL_30D | 519.10 | 2026-08-21 | 408.50 | 629.71 | MEDIUM |

**Relative strength** (`technical_indicators.json`, daily block):

| Pair | 20d | 60d |
|---|---|---|
| QQQ / SPY | **−5.12%** | +0.23% |
| SOXX / SPY | **−16.34%** | +16.30% |

The 20-day and 60-day columns have opposite signs for both pairs: growth and semis led over the quarter and have given it back violently in the last month. SOXX's +16.30% 60-day relative strength against −16.34% over 20 days is the sharpest reversal in the block.

**Regime-consistency check:** the block is consistent with the declared `NEUTRAL` index regime plus an internal growth-to-value rotation — SPY's own realized vol (3.92%) and drawdown (−2.72%) are unremarkable, while QQQ (7.96% vol, −8.30% drawdown) and SOXX (20.18% vol, −19.54% drawdown) carry essentially all of the stress. All three ETFs show `RISING` 30-day realized vol versus the prior 30 days.

### mu derivation (never free-handed)

| ETF | Rule | Base | Adjustment (band) | Final mu | Ledger-backed reason |
|---|---|---|---|---|---|
| SPY | regime prior, `NEUTRAL` | +0.5% | **−0.5pp** (±1.0pp allowed) | **0.00%** | Close below both MA20 and MA50; daily MACD `BELOW_SIGNAL`; weekly MACD `BEARISH_CROSS`; 30d realized vol rising 3.75% → 3.92% |
| QQQ | `beta_60d × SPY_mu` = 1.7222 × 0.00% | 0.00% | **−1.0pp** (±1.5pp allowed) | **−1.00%** | `BEARISH` MA alignment; RSI(14) 39.29; RS20 −5.12% vs SPY; −8.30% from 60d high |
| SOXX | `beta_60d × SPY_mu` = 3.6366 × 0.00% | 0.00% | **−1.5pp** (±1.5pp allowed) | **−1.50%** | `BEARISH` MA alignment; RS20 −16.34% vs SPY; −19.54% from 60d high; 30d realized vol 20.18%, rising from 16.92% |

Two disclosures are required here, both material:

1. **The beta multiplier degenerated to zero.** With SPY's mu adjusted to exactly 0.00%, `beta × SPY_mu` is 0.00% for both QQQ and SOXX regardless of their betas (1.72 and 3.64). Today's QQQ and SOXX forecasts are therefore driven **entirely by the ±1.5pp adjustment band**, not by the beta rule the spec nominates as primary. This is disclosed rather than presented as a principled derivation, and it is direct evidence for the structural problem analysed in `13_evolution_log.md`: because the base term scales a *positive* SPY prior by a beta ≥ 1, the adjustment band is normally far too small to ever express a bearish view on a high-beta ETF. Today that only worked out because the base happened to land on zero.
2. **SPY's direction call will not be scored.** `|mu| = 0.00% < 0.5%`, so at settlement SPY takes `N/A - FLAT_CALL` per `rules.md § Settlement Rules`; only CI calibration and magnitude error `z` will be scored. This is the honest consequence of a genuinely flat view, not an evasion — QQQ and SOXX both carry scoreable directional calls.

Sigma for all three is `REALIZED_VOL_30D` from the fetched bars (Sigma Fallback Chain step 2; step 1 `IV30` unavailable — no options feed wired; step 3 never needed). Confidence is `MEDIUM` for all three: `HIGH` requires trend, vol, and relative strength all aligned with the regime call at data quality ≥0.90, and neither the trend/vol alignment nor the 0.80 data-quality multiplier permits it.

## Universe Handoff

- Index-union path **succeeded** — no Sampled Universe fallback, and none was permitted.
- Handed to `technical_indicators.py`: the 515 union tickers plus SPY, QQQ, SOXX (518 records; 517 `OK`).
- Handed to Factor Scoring: **514 scored names**, all percentiles labelled `INDEX_UNION_PCTL (n=514)`.
- Rejection log and inclusion/exclusion detail: `04_universe_summary.md`.

## Stop-Rule Assessment

No `HALTED` condition is met: benchmark data is present, lineage is clear for every core field, no fabricated or contradictory evidence was found, and the index-union universe materialised. The Data/Regime stage recommends proceeding to factor scoring with data quality **0.80** and confidence capped, and flags in advance that evidence threshold #2 cannot be satisfied by any name (`Fund_Z`/`Sent_Z` `UNAVAILABLE`) — which is what ultimately produces `NO_TRADE`.
