# 10 — Midday Monitor — 2026-08-04

> **AMENDED 2026-08-05** — the original narrative described the sleeve as having
> *underperformed* SPY and called the session a second live demonstration of the rank inversion.
> The computed same-session alpha is **+0.06pp** — flat, not negative — so
> that claim was wrong and is corrected below. Every table figure is unchanged; only the prose
> around them was over-claimed.

**Observation-only.** This checkpoint changes nothing unless a stop criterion fires
(`runbook.md § Cadence`). No stop criterion fired. The run remains `NO_TRADE`, and no position
exists to adjust.

| Field | Value |
|---|---|
| Checkpoint time | 2026-08-04T12:05:00-04:00 |
| Market status | `REG_MKT` (CNBC `curmktstatus`, confirmed on all 28 verified symbols) |
| Published-record basis | 2026-08-03 completed close — **unchanged**; the tape below is not an entry basis |
| Live quote source | CNBC `last`, gated on `last_time` = 2026-08-04 (`L-PX-*` sources re-read at fire time) |
| Freshness tag on live values | `LIVE` |

## Core ETF tape

| ETF | Basis close (2026-08-03) | Live last | Intraday move |
|---|---|---|---|
| **SPY** | 757.67 | 768.57 | +1.44% |
| **QQQ** | 700.07 | 719.14 | +2.72% |
| **SOXX** | 507.68 | 539.52 | +6.27% |

## Published sleeve versus the tape

| Ticker | Entry (2026-08-03) | Live last | Intraday move | vs SPY | Still inside 70% CI |
|---|---|---|---|---|---|
| **DXCM** | 87.31 | 87.10 | -0.24% | -1.68% | inside |
| **BMY** | 65.47 | 64.38 | -1.66% | -3.10% | inside |
| **BEN** | 35.24 | 35.46 | +0.62% | -0.81% | inside |
| **BAX** | 28.10 | 27.64 | -1.64% | -3.08% | inside |
| **WTW** | 341.63 | 339.20 | -0.71% | -2.15% | inside |
| **COO** | 74.23 | 74.45 | +0.30% | -1.14% | inside |
| **BBY** | 85.25 | 85.13 | -0.14% | -1.58% | inside |
| **FTNT** | 163.21 | 165.61 | +1.47% | +0.03% | inside |
| **ROST** | 252.91 | 253.12 | +0.08% | -1.36% | inside |
| **NTAP** | 182.92 | 192.47 | +5.22% | +3.78% | inside |
| **IQV** | 233.36 | 228.01 | -2.29% | -3.73% | inside |
| **KKR** | 106.56 | 107.07 | +0.48% | -0.96% | inside |
| **REGN** | 759.24 | 757.98 | -0.17% | -1.60% | inside |
| **TGT** | 149.35 | 149.22 | -0.09% | -1.53% | inside |
| **ZBRA** | 291.64 | 355.88 | +22.03% | +20.59% | **outside** |
| **ARES** | 138.57 | 140.40 | +1.32% | -0.12% | inside |
| **MSFT** | 487.65 | 497.03 | +1.92% | +0.48% | inside |
| **GRMN** | 304.76 | 303.52 | -0.41% | -1.85% | inside |
| **VEEV** | 206.25 | 210.09 | +1.86% | +0.42% | inside |
| **PCAR** | 132.06 | 134.64 | +1.95% | +0.52% | inside |
| **LH** | 307.42 | 309.76 | +0.76% | -0.68% | inside |
| **COF** | 217.68 | 221.74 | +1.87% | +0.43% | inside |
| **HIG** | 142.90 | 141.86 | -0.73% | -2.17% | inside |
| **WSM** | 239.80 | 249.87 | +4.20% | +2.76% | inside |

## Observation — the sleeve versus a risk-on session

| Statistic | Value |
|---|---|
| Published names quoted | 24 |
| Names down on the session | **10 of 24** |
| Mean intraday move of the published sleeve | **+1.50%** |
| SPY over the same window | +1.44% |
| Same-session mean alpha | **+0.06pp** |
| SOXX over the same window | +6.27% |

Within hours of a ranking computed from the 2026-08-03 close, the market ran a sharp risk-on session —
SOXX +6.27%, QQQ +2.72%. Against that, the published sleeve returned
+1.50% versus SPY's +1.44%, i.e. **same-session alpha of
+0.06pp** with 10 of 24 names down outright.

**Read this carefully, because it is easy to over-claim.** The sleeve **essentially matched** its
benchmark — +0.06pp is not a meaningful deviation over a few hours. This is
therefore **not** a repeat of the 2026-07-30 intraday observation, where the sleeve trailed SPY by
4.6pp; the superficially similar setup (defensive book, semis ripping) did **not** produce the same
outcome today.

What the session *does* show is narrower: a sleeve with diagnostic beta +0.5323
kept pace with SPY while the high-beta complex ran far ahead of both. That is consistent with a
defensive tilt — it is evidence about the sleeve's **beta**, which `07` already establishes from the
fetched covariance matrix, and it is **not** independent evidence about rank ordering. Rank IC is a
cross-sectional property and cannot be evaluated from one session's mean.

**No action is taken on this.** One session is not a dataset, `eff_n` = 1 forbids any
Track A change, and re-scoring mid-series would break the comparability the settlement ledger depends
on. The 24 records settle on 2026-09-01 on their own terms.

## Stop-criteria check

| Stop criterion | State |
|---|---|
| Hard halt (`rules.md § Hard Halt Criteria`) | none triggered — data lineage intact, benchmark data present |
| `NO_TRADE` downgrade | already `NO_TRADE`; no further downgrade available |
| Position-level stops | n/a — no position exists |
