# 09 — Final Report — 2026-08-04

```text
══════════════════════════════════════════════════════
QUANTITATIVE EQUITY SELECTION REPORT — 2026-08-04
Run Status: NO_TRADE
Classification: INTERNAL — INVESTMENT COMMITTEE USE
══════════════════════════════════════════════════════
```

## Executive summary

All five Required inputs are grounded — 28 verified prices agreeing to the cent
across three independent sources on the 2026-08-03 completed close — yet **zero of 512 scored
names clear the Evidence Thresholds**, because `Fund_Z` and `Sent_Z` have no universe-scale fetch path
and make thresholds 2, 3 and 4 arithmetically unsatisfiable. This run fires intraday and therefore
shares its price basis with `claude-opus-5-2026-08-03`, so its ranking carries no new market
information; its contributions are 48 settlements, a fresh MoM baseline, and the
same-basis reproduction test the 2026-08-03 Track B owed. That test found `Tech_Z` reproduces to
0.0001 but `Macro_Z` only to 0.0487, isolated to the
`rate_sens` slot — the defect the now-published Metric Definition Table exists to fix. Status is
**`NO_TRADE`**.

## MoM reflection summary

Baseline **`claude-fable-5-2026-07-07`** (`CROSS_MODEL_BASELINE`, 2-way tie at delta
0d resolved by `agents.md` rule 8). Both tied books are
disclosed in `02 § 1` with their own settled statistics; the hit-rate spread is
6.36pp
and **the MoM conclusion is invariant across them** — both cohorts lost on direction and magnitude.
48 predictions settled this run under `TARGET_EQ_RUN_DATE`:
14/42 = 33.33% equity direction hits, mean z
-0.7494. Canonical rolling `EQUITY_ALPHA` n=515,
`eff_n`=1, rank IC -0.0879 → all confidence capped `MEDIUM`.

## Regime

| Regime | Data quality | Key macro risk | Ledger rows |
|---|---|---|---|
| **`BULL`** | DQ 0.80 (two of four families `UNAVAILABLE`) | leadership is defensive — QQQ -4.00% and SOXX -13.55% vs SPY over 20d, so the index trend is not confirmed by the high-beta complex | `L-MACRO-VIX`,`L-PX-SPY`,`L-HIST-001` |

Evidence: VIX 15.86; SPY above MA20 (746.01) and MA50
(744.60); 60d momentum +3.51%; 30d realized vol
3.76% versus 4.17% in the prior 30 days;
+0.00% from the 60-day high.

## Core ETF market forecast (summary of `03` — no new facts)

| ETF | Entry | Beta vs SPY | mu | sigma | Target | 70% CI | Target Date | Confidence |
|---|---|---|---|---|---|---|---|---|
| **SPY** | 757.67 | +1.000 | +2.00% | 3.76% | 772.82 | 743.18–802.46 | 2026-09-01 | MEDIUM |
| **QQQ** | 700.07 | +1.706 | +3.41% | 7.18% | 723.96 | 671.70–776.22 | 2026-09-01 | MEDIUM |
| **SOXX** | 507.68 | +3.530 | +7.06% | 18.60% | 543.52 | 445.33–641.72 | 2026-09-01 | MEDIUM |

## Ranked candidates — top 10 of 205 ranked (monitoring sleeve only)

| Rank | Ticker | Sector | Entry | Adj Score | Score Trace | Pctl | Beta | 30d RVol | Sharpe | Max DD60 | TD9 D/W/M | RSI14 D/W/M | MACD D/W/M | mu | Target | Conf |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **DXCM** | Health Care | 87.31 | +0.4319 | `(0.3*0.00(UA) + 0.3*+1.4253 + 0.25*0.00(UA) + 0.15*+0.7489) * 0.80 - 0.00 = +0.4319` | 100.00 | +0.205 | 15.33% | 0.371 | -13.86% | S5/S4/S2 | 72.6/67.8/53.5 | ABOVE/ABOVE/ABOVE | +6.0% | 92.55 | MEDIUM |
| 2 | **BMY** | Health Care | 65.47 | +0.3993 | `(0.3*0.00(UA) + 0.3*+1.3624 + 0.25*0.00(UA) + 0.15*+0.6030) * 0.80 - 0.00 = +0.3993` | 99.80 | -0.203 | 8.67% | 0.656 | -9.32% | S9/S7/S2 | 71.8/68.5/65.5 | ABOVE/ABOVE/ABOVE | +6.0% | 69.40 | MEDIUM |
| 3 | **BEN** | Finance | 35.24 | +0.3616 | `(0.3*0.00(UA) + 0.3*+1.0970 + 0.25*0.00(UA) + 0.15*+0.8196) * 0.80 - 0.00 = +0.3616` | 99.61 | +1.095 | 8.12% | 0.700 | -6.42% | S7/S1/S8 | 66.1/74.3/71.8 | BULL_X/ABOVE/ABOVE | +6.0% | 37.35 | MEDIUM |
| 4 | **BAX** | Health Care | 28.10 | +0.3335 | `(0.3*0.00(UA) + 0.3*+1.2327 + 0.25*0.00(UA) + 0.15*+0.3136) * 0.80 - 0.00 = +0.3335` | 99.41 | +0.644 | 14.23% | 0.400 | -7.19% | S7/S9/S3 | 76.4/73.6/51.7 | ABOVE/ABOVE/ABOVE | +6.0% | 29.79 | MEDIUM |
| 5 | **WTW** | Finance | 341.63 | +0.3279 | `(0.3*0.00(UA) + 0.3*+1.1885 + 0.25*0.00(UA) + 0.15*+0.3555) * 0.80 - 0.00 = +0.3279` | 99.22 | -0.367 | 9.85% | 0.578 | -6.18% | S7/S7/S2 | 81.6/68.4/60.8 | ABOVE/ABOVE/BELOW | +6.0% | 362.13 | MEDIUM |
| 6 | **COO** | Health Care | 74.23 | +0.2807 | `(0.3*0.00(UA) + 0.3*+0.8387 + 0.25*0.00(UA) + 0.15*+0.6620) * 0.80 - 0.00 = +0.2807` | 99.02 | -0.380 | 8.75% | 0.650 | -7.67% | S5/S1/S2 | 63.3/55.8/46.2 | BULL_X/ABOVE/BULL_X | +6.0% | 78.68 | MEDIUM |
| 7 | **BBY** | Consumer Discretionary | 85.25 | +0.2682 | `(0.3*0.00(UA) + 0.3*+0.8677 + 0.25*0.00(UA) + 0.15*+0.4994) * 0.80 - 0.00 = +0.2682` | 98.83 | +0.421 | 8.14% | 0.699 | -8.93% | B2/S9/S4 | 56.3/65.1/58.9 | BELOW/ABOVE/ABOVE | +6.0% | 90.37 | MEDIUM |
| 8 | **FTNT** | Technology | 163.21 | +0.2642 | `(0.3*0.00(UA) + 0.3*+0.5853 + 0.25*0.00(UA) + 0.15*+1.0311) * 0.80 - 0.00 = +0.2642` | 98.63 | +0.968 | 10.70% | 0.531 | -10.10% | S4/S9/S6 | 61.3/77.7/78.4 | BELOW/ABOVE/ABOVE | +6.0% | 173.00 | MEDIUM |
| 9 | **ROST** | Consumer Discretionary | 252.91 | +0.2598 | `(0.3*0.00(UA) + 0.3*+0.9090 + 0.25*0.00(UA) + 0.15*+0.3469) * 0.80 - 0.00 = +0.2598` | 98.43 | +0.219 | 8.84% | 0.643 | -13.03% | S7/S4/S9 | 71.0/69.1/76.4 | ABOVE/BULL_X/ABOVE | +6.0% | 268.08 | MEDIUM |
| 10 | **NTAP** | Technology | 182.92 | +0.2572 | `(0.3*0.00(UA) + 0.3*+0.7563 + 0.25*0.00(UA) + 0.15*+0.6306) * 0.80 - 0.00 = +0.2572` | 98.24 | +1.439 | 12.08% | 0.471 | -15.81% | S9/S5/S5 | 68.0/74.3/71.5 | ABOVE/ABOVE/ABOVE | +6.0% | 193.90 | MEDIUM |

Full 24-name sleeve with complete metric blocks: `05_factor_scores.md`, `06_top_candidates.md`.

## No-trade rationale

| Trigger (`rules.md § Downgrade to NO_TRADE`) | State | Evidence |
|---|---|---|
| #1 Fewer than 5 names pass the investable threshold | **FIRED** | 0 of 512 clear all five Evidence Thresholds |
| #2 Best candidates miss the 80th-pctl bar | not fired | 103 names clear the percentile bar |
| #3 Average pairwise correlation > 0.45 | not fired | 0.1482 |
| #4 More than 2 names with earnings inside 14d | n/a | the investable set is empty |
| #5 95th-pctl 1-month drawdown > 8% | **FIRED (independently)** | 8.50% on the naive top-20 sleeve |
| #6 Structurally infeasible (beta / sector / factor) | **FIRED (independently)** | rank-ordered sleeve beta +0.5323 vs the 0.90 floor, though the attainable range [-0.5413, +1.3472] does contain the band |

Three independent triggers fire. The binding one is #1.

## Assumptions and limitations

1. **Shared basis.** This intraday run's newest completed close is 2026-08-03 — the same basis as the
   prior package. The cross-sectional ranking therefore adds no new price information.
2. **Two of four factor families are unavailable.** `Fund_Z` and `Sent_Z` are `UNAVAILABLE`
   universe-wide; DQ is fixed at 0.80. This is the sole reason no package since 2026-07-01
   has reached `GO`.
3. **The composite score is rank-inverted** (-0.0879 weighted-mean rank IC). All confidence is
   capped `MEDIUM` and no name is presented as a recommendation.
4. **`Macro_Z` is not exactly reproducible across runs** — the `rate_sens` convention was
   under-specified before this package. Fixed forward by the Metric Definition Table in `05`.
5. **Normality is assumed** for VaR95, CVaR95 and the 95th-percentile drawdown estimate.
6. **`eff_n` = 1** — raw n=515 is statistically vacuous for Track A purposes;
   no calibration parameter may move yet.
7. **IBKR MCP was unavailable** (connector connection invalidated). Grounding rests on three
   independent web sources that agreed to the cent.
8. **FOMC calendar is `UNAVAILABLE`** — no feed wired; not estimated.

## Next scheduled review

| Checkpoint | When | Owner |
|---|---|---|
| Midday monitor | 2026-08-04 12:15 ET — **ran this fire**, see `10_midday_monitor.md` | Orchestrator |
| Pre-close check | 2026-08-04 15:45 ET — not run | Orchestrator |
| Close log | 2026-08-04 16:20 ET — not run | Orchestrator |
| Next full pipeline | 2026-08-05 pre-open | Orchestrator |
| Weekly parameter review | 2026-08-07 (Friday) 17:15 ET | Evolution Agent |
| `eff_n` increment check | **2026-08-05** — the falsifiable 2026-07-28 projection (43 pending) | Evolution Agent |
