# 10 — Midday Monitor — 2026-07-30

**Observation only. Nothing here changes any published number, score, or status.**

This run fired intraday at 2026-07-30T10:06:00-04:00, so a real monitor is owed (a pre-open run would stub it).
Quotes captured **2026-07-30T10:26:18-04:00**, market status `REG_MKT`.
Basis for everything published remains the **2026-07-29** close.

## Market

| Instrument | 2026-07-29 close | Live | Move |
|---|---|---|---|
| SPY | 729.46 | 738.00 | **+1.17%** |
| QQQ | 661.73 | 681.86 | **+3.04%** |
| SOXX | 465.00 | 505.33 | **+8.67%** |
| TLT | 82.85 | 82.87 | +0.02% |

A violent factor rotation is under way: semiconductors are up
+8.67% in the first hour, roughly
7.4x the SPY move, while long
duration (TLT +0.02%) is flat. This is the **mirror image** of the
window that just settled, in which SOXX fell -17.89%.

## Published monitoring sleeve vs the live tape

| Rank | Ticker | Entry (2026-07-29) | Live | Move | 70% CI | Position |
|---|---|---|---|---|---|---|
| 1 | GRMN | 294.83 | 289.61 | **-1.77%** | 265.10–359.94 | inside |
| 2 | BBY | 90.17 | 88.37 | **-2.00%** | 87.25–103.91 | inside |
| 3 | IQV | 247.56 | 237.37 | **-4.12%** | 221.59–303.23 | inside |
| 4 | NTAP | 173.23 | 173.54 | **+0.18%** | 160.53–206.72 | inside |
| 5 | BXP | 72.97 | 70.77 | **-3.01%** | 70.89–83.80 | **outside** |
| 6 | TRV | 389.01 | 374.23 | **-3.80%** | 373.32–451.38 | inside |
| 7 | INCY | 127.10 | 122.08 | **-3.95%** | 119.05–150.40 | inside |
| 8 | GEHC | 71.90 | 68.69 | **-4.46%** | 65.12–87.31 | inside |
| 9 | FICO | 1373.08 | 1157.00 | **-15.74%** | 1284.96–1625.97 | **outside** |
| 10 | ADP | 273.37 | 258.82 | **-5.32%** | 260.90–318.64 | **outside** |
| 11 | F | 15.28 | 14.79 | **-3.21%** | 14.93–17.46 | **outside** |
| 12 | HUM | 365.41 | 365.31 | **-0.03%** | 345.60–429.06 | inside |
| 13 | CPAY | 392.85 | 385.26 | **-1.93%** | 377.63–455.21 | inside |
| 14 | PAYX | 122.13 | 114.56 | **-6.20%** | 116.90–142.01 | **outside** |
| 15 | FTNT | 153.22 | 157.40 | **+2.73%** | 145.83–178.99 | inside |
| 16 | SJM | 126.35 | 122.43 | **-3.10%** | 120.89–146.97 | inside |
| 17 | MRSH | 197.59 | 189.79 | **-3.95%** | 189.67–229.22 | inside |
| 18 | BRO | 74.87 | 70.55 | **-5.77%** | 70.45–88.28 | inside |
| 19 | HPQ | 28.41 | 26.50 | **-6.72%** | 26.68–33.55 | **outside** |
| 20 | RTX | 215.25 | 211.58 | **-1.70%** | 206.56–249.77 | inside |
| 21 | CTAS | 216.53 | 205.39 | **-5.14%** | 207.12–251.93 | **outside** |
| 22 | IEX | 229.52 | 236.11 | **+2.87%** | 230.96–255.62 | inside |
| 23 | DVA | 240.96 | 239.67 | **-0.54%** | 241.60–269.24 | **outside** |
| 24 | VRSK | 213.15 | 199.33 | **-6.48%** | 202.45–249.43 | **outside** |

| Summary | Value |
|---|---|
| Names down | **21 of 24** |
| Mean move | **-3.47%** |
| SPY over the same span | +1.17% |
| Implied same-session alpha | **-4.64pp** |
| Already outside their 70% CI | 9 |

## Assessment

The book this run ranked highest is, within one hour, the losing side of the day's rotation:
21 of 24 names down, averaging -3.47% against SPY +1.17%.
That is a 4.64pp adverse move in a single session.

This is exactly the failure mode the rolling metrics describe — rank-order inversion, not
magnitude error — and it arrives as a clean out-of-sample observation, since these ranks were
computed from 2026-07-29 data with no knowledge of the 2026-07-30 tape. It is recorded in
`13_evolution_log.md` as supporting evidence for a proposal that remains **`DEFERRED`**: one
session is not a calibration dataset, and `eff_n`=1 < 3 forbids a Track A change
regardless.

**FICO** is the single largest dislocation at -15.74%. Per `08 § 2` no
source supports an earnings explanation — it is absent from all
27 swept calendar days and vendor-empty per-name — so none is
asserted.

## Stop criteria

No stop criterion fires. The run already published `NO_TRADE` with no positions, so there is no
exposure to reduce, no stop to trigger, and nothing to act on. Per
`runbook.md § Cadence`, midday review changes nothing unless a stop criterion fires.
