# 03 Regime and Data — 2026-07-20 (claude-fable-5)

## Data Mode Declaration

**DELAYED.** All prices are the 2026-07-17 official session closes fetched this run: Nasdaq historical bulk (518/519 symbols, 8-worker, ~161s, price_history_fetch_manifest.json) with BF-B via IBKR conid 4931; 17 settlement-relevant names cross-verified against IBKR snapshots (max divergence 0.186%, nasdaq_verification_manifest.json). Yahoo v8 remained 429-blocked for the fifth consecutive session (probe 0/6) — Nasdaq-bulk-primary path per the 07-13 Track B. VIX from CBOE (L008), rf from treasury.gov after FRED timeout (L009). All five Required inputs grounded (L001–L012); no ILLUSTRATIVE content.

## Regime Classification: NEUTRAL — with HIGH_VOL watch (L018/regime)

| Evidence | Value | Ledger |
|---|---|---|
| SPY vs MAs | 743.29 below MA20 745.02 and MA50 744.38 (−0.23%/−0.15%) | L014, L015 |
| VIX | 18.77 (< 20 watch trigger); 20d mean 17.0 | L008 |
| Breadth | 63.4% of eligible universe above MA50 — still constructive | L010 |
| Vol regime | SPY 30d rvol (1m) 4.54% vs 2.76% prior window — rising | L015 |
| Leadership | Low-vol defensives (REITs, insurers, regionals, staples) dominate the cross-section; semis in −20% drawdown | 05 leaderboard, L020 |

The HIGH_VOL trigger (VIX > 20 while SPY holds below both MAs) has not fired; breadth and weekly/monthly SPY trend (both BULLISH, technical_indicators.json) argue against BEAR. NEUTRAL stands, consistent with both 07-17 packages.

## Core ETF Market Forecast Block

mu derivation: SPY = NEUTRAL regime prior +0.50% (L013/spymu, unadjusted). QQQ = beta 1.733 × 0.50% = +0.87%, adjusted −0.50pp (within ±1.5pp band) on deteriorating relative strength — 20d QQQ/SPY −4.06% (L017), price below both MAs, rvol doubled. SOXX = beta 3.710 × 0.50% = +1.85%, adjusted −1.50pp (band limit) on 20d SOXX/SPY −13.27%, dd60 −20.34%, rvol 22%. Betas are 60d fetched-return regressions (DERIVED, L014–L016) and remain correction-distorted — sigma, not mu, carries that information.

| ETF | Entry Price | Price Date | Price Tag | Trend (20d/50d) | 30d RVol | Beta vs SPY | mu | sigma | Sigma Source | Target Price | Target Date | 70% CI Lo | 70% CI Hi | Confidence | Ledger Rows |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SPY | 743.29 | 2026-07-17 | DELAYED | below MA20 745.02, below MA50 744.38 | 4.54% | 1.000 | +0.50% | 4.54% | REALIZED_VOL_30D | 747.01 | 2026-08-17 | 711.94 | 782.08 | MEDIUM | L014,L015 |
| QQQ | 695.33 | 2026-07-17 | DELAYED | below MA20 718.35, below MA50 719.01 | 8.87% | 1.733 | +0.37% | 8.87% | REALIZED_VOL_30D | 697.9 | 2026-08-17 | 633.75 | 762.06 | LOW | L016,L017 |
| SOXX | 521.81 | 2026-07-17 | DELAYED | below MA20 586.15, below MA50 566.37 | 22.04% | 3.710 | +0.35% | 22.04% | REALIZED_VOL_30D | 523.64 | 2026-08-17 | 404.04 | 643.23 | LOW | L018,L019 |
Relative strength: QQQ/SPY 20d −4.06% / 60d +2.22%; SOXX/SPY 20d −13.27% / 60d +17.49% (L017) — the 60d ratios still carry the spring melt-up; the 20d ratios say growth/semis leadership broke in July. Regime-consistency check: a NEUTRAL call with defensives leading and the highest-beta sleeve in a −20% drawdown is internally consistent; the forecast block's positive-but-shrunk mus reflect the prior, not conviction (SPY MEDIUM, QQQ/SOXX LOW).

## Event Concentration Flags

- **Peak earnings wave:** 12 of the 34 earnings-checked names sit inside the buffered 14-day window (L011/earnwave): CSX and MCO print in 2 days, UNP/SNA/WST in 3. NO_TRADE downgrade trigger #4 (> 2 names in-window) would bind any portfolio drawn from this leaderboard.
- **FOMC:** late-July meeting (~2026-07-28/29, structural cadence) sits inside every target horizon.
- Vendor-empty earnings rows on seven just-printed names carried as +91d cadence estimates, tag `ESTIMATED (±5d)` (earnings_calendar_manifest.json).

## Universe Handoff

`build_index_universe.py`: 515-name union (503 S&P 500 + 101 Nasdaq-100, 89 overlap; caches fetched 2026-06-21 — stale-cache rule applied, refresh is maintenance not fallback) → universe_summary.json (L003). Eligible after filters: **514** (price > $5, ADV20 > $20M, ≥ 60 bars; FDXF excluded at 36 bars — L004). Full list + SPY/QQQ/SOXX handed to `technical_indicators.py` (517/518 OK). Percentile label: `INDEX_UNION_PCTL (n=514)`.

## Ledger Coverage Gaps Affecting Scoring

Fund_Z and Sent_Z are UNAVAILABLE universe-wide (L012) — SHADOW diagnostics exist but remain unpromoted below the 70% sourceability bar. Effect: DQ 0.80, max 2 of 4 families sourceable, evidence threshold #2 unsatisfiable → structural NO_TRADE gate (15th consecutive scoring run). GICS sector labels are not carried in the constituent caches; sector references downstream are INFERRED and no sector cap is exercised (no portfolio is drafted). Handoff to Factor Scoring: proceed, full metric pack, calibration feedback from 02 §0 binds (MEDIUM cap → sleeve LOW).
