# 03 Regime and Data — 2026-07-22

## Data Mode Declaration

`DELAYED` — no brokerage feed wired for equity price history; all prices are public-endpoint fetches made this run (Nasdaq bulk historical + Nasdaq quote-info official-close), cross-checked once against IBKR MCP for SPY. All five Required inputs (`rules.md § Input Classification`) are grounded; see `00_run_manifest.md § GO-Gate Table`.

## Regime Classification: `NEUTRAL` (semiconductor high-volatility pocket)

Evidence (ledger rows L0005–L0029, `01_preflight.md`):

- **SPY** sits essentially on top of both its 20d MA (744.98) and 50d MA (744.88) at the last historical close (748.28, 2026-07-21), a shallow -1.49% drawdown from its 60-day high, 30d realized vol 4.02% (rising modestly from 3.53% the prior 30d window). No broad-market stress signal.
- **VIX** closed 17.05 (2026-07-21), essentially in line with its own 60-day average (17.34) — confirms no broad-market vol regime shift.
- **QQQ** has slipped below both its 20d MA (714.67) and 50d MA (719.29) at 708.97, a -4.98% drawdown from its 60-day high, 30d realized vol 8.08% (up from 6.15%). Relative strength vs SPY is negative over 20d (-4.45%) but still positive over 60d (+3.21%) — a decelerating-leadership signal, not yet a reversal.
- **SOXX** shows the clearest stress: -15.62% drawdown from its 60-day high at 552.69 (well below its 20d MA 575.27 and 50d MA 567.92), 30d realized vol 20.70% (up sharply from 16.66% the prior 30d window — vol nearly doubling), and a sharp -16.14% 20-day relative-strength reversal against SPY even though it remains +19.70% ahead of SPY on a 60-day view. 60-day beta to SPY of 3.82 is well above SOXX's typical historical range (~1.3–1.8), reflecting this idiosyncratic vol spike rather than a durable shift in market sensitivity — disclosed, not smoothed over.

**Classification rationale:** no defensible case for `BULL` (QQQ/SOXX trend deterioration), `BEAR` (SPY itself is flat, not falling), `RATE_SHOCK` (no rate-shock evidence sourced this run), or broad-market `HIGH_VOL` (VIX at its own average). `NEUTRAL` best describes the broad tape, with an explicit semiconductor-sector high-vol flag carried into Macro_Z scoring and the mu prior table below.

## Core ETF Market Forecast Block

| ETF | Entry Price | Price Date | Price Tag | Trend (20d/50d) | 30d RVol | Beta vs SPY | mu | sigma | Sigma Source | Target Price | Target Date | 70% CI Lo | 70% CI Hi | Confidence | Ledger Rows |
|---|---:|---|---|---|---:|---:|---:|---:|---|---:|---|---:|---:|---|---|
| SPY | 747.48 | 2026-07-22 | DELAYED | At 20d/50d (flat) | 4.02% (rising) | 1.000 | +0.50% | 4.02% | REALIZED_VOL_30D | 751.22 | 2026-08-19 | 719.97 | 782.47 | MEDIUM | L0005,L0006,L0007,L0008 |
| QQQ | 705.35 | 2026-07-22 | DELAYED | Below 20d/50d | 8.08% (rising) | 1.742 | +0.87% | 8.08% | REALIZED_VOL_30D | 711.49 | 2026-08-19 | 652.23 | 770.76 | MEDIUM | L0009,L0010,L0011,L0012,L0013,L0014,L0015 |
| SOXX | 555.52 | 2026-07-22 | DELAYED | Below 20d/50d | 20.70% (rising) | 3.817 | +1.91% | 20.70% | REALIZED_VOL_30D | 566.12 | 2026-08-19 | 446.52 | 685.73 | MEDIUM | L0016,L0017,L0018,L0019,L0020,L0021,L0022 |

**mu derivation:** SPY mu = NEUTRAL regime prior (+0.5%, `rules.md § Core ETF Market Forecast` table), no discretionary adjustment applied. QQQ/SOXX mu = `beta_60d × SPY mu` per the required formula, no discretionary adjustment applied (SOXX's elevated beta was considered for a downward adjustment given the idiosyncratic-vol argument above, but +1.91% mu is not itself an unreasonable output and the ±1.5pp discretionary band was left unused rather than stacking a second judgment call on top of an already-disclosed anomaly).

**Relative-strength notes:** QQQ/SPY: -4.45% (20d), +3.21% (60d). SOXX/SPY: -16.14% (20d), +19.70% (60d). **Regime-consistency check:** the broad-market `NEUTRAL` call is consistent with SPY's own flat trend and average VIX; QQQ and SOXX's below-MA trend and negative 20d relative strength are a *within-regime* sector-specific divergence (semiconductors cooling off after a strong 60-day run), not evidence against the NEUTRAL classification for the benchmark itself.

## Universe Handoff

`build_index_universe.py` succeeded: 503 S&P 500 + 101 Nasdaq-100 constituents, 89 overlap, 515-name union (cache `fetched_at` 2026-06-21, reused per `rules.md § Index-Union Universe Protocol` #5 — refresh is a maintenance task, not a run blocker). Full detail in `04_universe_summary.md`. Price-history + technical-indicator handoff to factor scoring: 514 of 515 names sourceable (`FDXF` excluded — 38 fetched bars, recent spinoff, fails both the 60-bar minimum and the >6-month listing-age inclusion filter).

## Event Concentration Flag

Earnings season is materially concentrated this week and next: of the 54 names with a completed earnings-date preflight (`01_preflight.md`), every `CONFIRMED`-tagged date lands within 1–15 calendar days of today (TMO/HBAN/WST/FCX report tomorrow, 2026-07-23). This is disclosed as a standing event-concentration condition affecting the candidate set's earnings-penalty exposure in `05_factor_scores.md`, not a data-quality gap.
