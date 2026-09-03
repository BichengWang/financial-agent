# 09 — Final Report · 2026-08-28 *(backfilled)*

> **BACKFILLED 2026-09-03** — the 2026-08-28 scheduled run wrote `01`-`07` and `15_predictions.json`
> and then truncated before publishing this artifact. It is reconstructed here from that package's
> **own committed data** (`01`-`07`, `15_predictions.json`) by the 2026-09-03 run. No analytical content
> is invented: anything the truncated run never persisted is marked `UNAVAILABLE` rather than
> recomputed from a different basis. No prediction record was added, altered, or removed.

```text
══════════════════════════════════════════════════════
QUANTITATIVE EQUITY SELECTION REPORT — 2026-08-28
Run Status: NO_TRADE
Classification: INTERNAL — INVESTMENT COMMITTEE USE
══════════════════════════════════════════════════════
```

## 1. Executive summary

All five Required inputs were grounded on a 2026-08-28 post-close basis (fire 22:08 ET) and
510 index-union names were scored, but no name was investable: `Fund_Z` and `Sent_Z` are
`UNAVAILABLE` universe-wide, so evidence thresholds 2, 3 and 4 fail by construction. Zero
predictions were due, so `settlements` is empty by design rather than by omission. The sleeve-beta
band was **feasible** this run (max attainable +1.1177 against a 0.90 floor), which is the opposite
of the two immediately preceding packages — feasibility is not why this run did not trade.

## 2. MoM Reflection Summary

Summarises `02`; introduces no new facts.

| Item | Value |
|---|---|
| Settled this run | 0 — no prediction anywhere in the corpus carried `target_date == 2026-08-28` |
| Due inventory | 2 — both `EQR` keys, `UNSETTLEABLE_CORPORATE_ACTION` |
| Canonical rolling `EQUITY_ALPHA` | raw n 1355, 28-day eff_n 2, hit 37.49%, CI 71.88%, mean z -0.5553 |
| Canonical rolling `MARKET_FORECAST` | raw n 201, 28-day eff_n 2, hit 40.11%, CI 90.55%, mean z -0.1848 |
| Track A gate | not satisfied — `INSUFFICIENT_EFFECTIVE_N` for both record types |

## 3. Regime

| Regime | Data quality | Key macro risk |
|---|---|---|
| **`BULL`** (see `03`) | 0.80 — two of four factor families unsourceable | a volatility expansion would hit a trend-persistence leaderboard hardest; see `03` |

## 4. Core ETF market forecast

Summarises `03`; no new facts.

| ETF | Entry | mu | sigma | Target | 70% CI | Confidence |
|---|---|---|---|---|---|---|
| SPY | 769.35 | +2.00% | 3.38% | 784.74 | 757.72 - 811.75 | MEDIUM |
| QQQ | 716.43 | +2.48% | 5.98% | 734.18 | 689.66 - 778.70 | MEDIUM |
| SOXX | 508.62 | +5.36% | 14.57% | 535.90 | 458.85 - 612.95 | MEDIUM |

## 5. Ranked candidates (24 names, monitoring sleeve only)

Carried from `05`/`06`; the full tables with score traces and technical states are in those
artifacts and are not duplicated here.

| Rank | Ticker | Entry | Adj Score | mu | sigma | Target | 70% CI | Confidence |
|---|---|---|---|---|---|---|---|---|
| 1 | RJF | 179.36 | +0.3519 | +6.00% | 5.68% | 190.12 | 179.52 - 200.72 | MEDIUM |
| 2 | SCHW | 110.16 | +0.3505 | +6.00% | 5.74% | 116.77 | 110.20 - 123.34 | MEDIUM |
| 3 | BLK | 1164.48 | +0.3322 | +6.00% | 6.64% | 1234.35 | 1153.94 - 1314.76 | MEDIUM |
| 4 | RVTY | 128.80 | +0.3112 | +6.00% | 9.86% | 136.53 | 123.32 - 149.74 | MEDIUM |
| 5 | SJM | 132.34 | +0.3079 | +6.00% | 8.47% | 140.28 | 128.63 - 151.93 | MEDIUM |
| 6 | APD | 308.09 | +0.3067 | +6.00% | 5.14% | 326.58 | 310.12 - 343.03 | MEDIUM |
| 7 | BDX | 189.52 | +0.3028 | +6.00% | 7.47% | 200.89 | 186.16 - 215.62 | MEDIUM |
| 8 | BNY | 162.50 | +0.3026 | +6.00% | 5.23% | 172.25 | 163.42 - 181.08 | MEDIUM |
| 9 | IQV | 261.75 | +0.3020 | +6.00% | 14.20% | 277.46 | 238.81 - 316.10 | MEDIUM |
| 10 | GIS | 41.55 | +0.2968 | +6.00% | 9.16% | 44.04 | 40.09 - 48.00 | MEDIUM |
| 11 | NWSA | 30.97 | +0.2928 | +6.00% | 8.37% | 32.83 | 30.13 - 35.53 | MEDIUM |
| 12 | NDAQ | 99.31 | +0.2909 | +6.00% | 4.29% | 105.27 | 100.84 - 109.70 | MEDIUM |
| 13 | NWS | 34.85 | +0.2872 | +6.00% | 8.83% | 36.94 | 33.74 - 40.14 | MEDIUM |
| 14 | VEEV | 276.69 | +0.2864 | +6.00% | 16.72% | 293.29 | 245.19 - 341.40 | MEDIUM |
| 15 | A | 153.84 | +0.2740 | +6.00% | 7.97% | 163.07 | 150.31 - 175.83 | MEDIUM |
| 16 | RMD | 240.33 | +0.2737 | +6.00% | 9.70% | 254.75 | 230.50 - 279.00 | MEDIUM |
| 17 | ABT | 112.47 | +0.2723 | +6.00% | 6.13% | 119.22 | 112.05 - 126.39 | MEDIUM |
| 18 | STT | 193.33 | +0.2712 | +6.00% | 6.55% | 204.93 | 191.75 - 218.11 | MEDIUM |
| 19 | JNJ | 268.04 | +0.2671 | +6.00% | 6.17% | 284.12 | 266.93 - 301.31 | MEDIUM |
| 20 | VRTX | 541.69 | +0.2640 | +6.00% | 8.51% | 574.19 | 526.25 - 622.14 | MEDIUM |
| 21 | NEM | 127.98 | +0.2621 | +6.00% | 13.87% | 135.66 | 117.20 - 154.11 | MEDIUM |
| 22 | AMP | 559.32 | +0.2600 | +6.00% | 4.73% | 592.88 | 565.38 - 620.38 | MEDIUM |
| 23 | NOW | 144.71 | +0.2599 | +6.00% | 18.12% | 153.39 | 126.12 - 180.67 | MEDIUM |
| 24 | ICE | 162.33 | +0.2572 | +6.00% | 5.78% | 172.07 | 162.31 - 181.83 | MEDIUM |

## 6. No-trade rationale

`rules.md § Downgrade to NO_TRADE` #1 fires: zero names pass the investable threshold against a
minimum of five. `06` records the cause — evidence thresholds 2, 3 and 4 fail for every name in
the 510-name universe because `Fund_Z` and `Sent_Z` are `UNAVAILABLE`. The beta band was
feasible; composition and evidence, not feasibility, are the blockers.

## 7. Assumptions and limitations

| # | Assumption / limitation |
|---|---|
| 1 | Return and indicator math uses adjusted closes; entry/target/CI use raw closes. |
| 2 | Parametric normality is assumed for VaR95, CVaR95 and the 95th-percentile drawdown. |
| 3 | No options feed is wired, so sigma never reaches the IV30 step. |
| 4 | IBKR MCP invalidated since 2026-08-04; grounding rests on three web sources. |
| 5 | `Fund_Z` and `Sent_Z` are `UNAVAILABLE` universe-wide. |
| 6 | **This report was backfilled on 2026-09-03.** It introduces no fact absent from the 2026-08-28 package's own `01`-`07` and `15_predictions.json`. |

## 8. Next scheduled review

Superseded: the next package in the corpus is `gpt-5.6-sol-2026-08-28`, and the next
`claude-opus-5` run is 2026-09-03.
