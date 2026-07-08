# 04 Universe Summary

Universe construction: S&P 500 ∪ Nasdaq-100 index union from local constituent caches (both fetched 2026-06-21T21:05:56Z — 16 days old; per protocol, stale caches are used and logged, refresh is maintenance). Counts from `universe_summary.json` (generated 2026-07-07T15:52:47Z): **503 + 101 − 89 = 515 union**. Percentile label: **INDEX_UNION_PCTL (n=513)**. Sampled fallback NOT used.

## Inclusion / Exclusion Log

| Screen | Threshold | Result |
|---|---|---|
| Bars | >= 61 daily bars | FDXF rejected (28 bars) |
| Freshness | last bar = live 2026-07-07 session | SATS rejected (last bar 2026-07-02; second consecutive no-print session) |
| Price | > $5 | 0 rejected |
| Liquidity | ADV$20d > $20M | 0 rejected |
| Coverage | >= 80% of trailing 60 sessions | 0 rejected |
| **Eligible** | | **513** |

## Metric Coverage Summary

| Metric group | Sourceable | UNAVAILABLE | Effect |
|---|---|---|---|
| Price/volume history (5y daily) | 513/513 + 3 ETFs + 3 macro | — | Required input PASS |
| Realized vol, beta, TE, drawdown, momentum, RS, volume ratio | 513/513 | — | Tech_Z + Macro_Z fully computable |
| Technical indicator pack (TD-9, RSI14, MACD, MA, mom, VR, RS — d/w/m) | 513/513 daily & weekly; 513/513 monthly | — | >=70% coverage bar cleared; contributes to Tech_Z |
| Fundamental family (revisions, margins, FCF, ROIC, leverage) | 0/513 | 513 | Family UNAVAILABLE — contribution 0.00, DQ 0.80; **data-quality issue, not a GO blocker** (Enhancing) |
| Sentiment family (short interest, options skew, analyst revisions) | 0/513 | 513 | Family UNAVAILABLE — same treatment |
| Earnings dates | 80-name estimate shortlist (07-04/07-06 estimates re-based + new-entrant cadence estimates incl. DDOG, STT, AXON, RVTY, EW, ESS, BNY, JNJ, C and the mid-July insurance/exchange cluster) | universe rest not evaluated | -0.10 penalty inside buffered <=19d window (**35 names hit**, incl. DAL est 07-09 and the banks cluster); every published name and every top-40 rank carries an estimate |
| Risk-free rate | ^IRX 3.725% @ 2026-07-07 (fresh) | — | ratios use rf_1m 0.310% |

RSI and MACD are sourceable for >=70% of the eligible universe, so they contribute to Tech_Z per rules.md §Technical Indicator Pack; TD-9 setup 9 / RSI>=75 act only as exhaustion penalty flags, never standalone signals.

Adj-score distribution over 513 names: p95 +0.246, p80 +0.132, p60 +0.058, median +0.021 — modestly firmer than 07-06 (p95 +0.236, p80 +0.141, median +0.019) with a defensives-led top decile: the security-software complex holds its ranks while airlines/banks slip on freshly-applied earnings-window penalties and semis fall out of the leaderboard entirely on today's -7% SOXX session.

Earnings-estimate scope note: the cadence-estimate shortlist covers the 07-04/07-06 estimated names re-based to 2026-07-07 plus new-entrant estimates for today's leaderboard entrants; every published name and every top-40 rank carries an estimate or a documented window verdict.
