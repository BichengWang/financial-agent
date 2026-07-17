# 03 Regime and Data — 2026-07-17

## Data Mode

**DELAYED** (rules.md §Data Mode Taxonomy): all quotes fetched this run with the 2026-07-17 **official close** (the run fired 15:59 ET; data collection ran 16:05–16:45 ET after the close completed). Zero Required inputs missing → GO-eligible on data; the run's NO_TRADE is an evidence-threshold outcome, not a data outcome. Fetch chain and verification: 01 preamble, L002, L016.

- Regime: **NEUTRAL** (L014). Evidence: SPY closed 743.15, −1.01% Friday, **below MA20 (745.01) and MA50 (744.38)** with a fresh daily MACD **BEARISH_CROSS** and RSI 48 — but mom60 +5.55%, weekly and monthly alignment BULLISH, and drawdown from the 60d high only −2.16% (L009). VIX 18.75, +2.02 on the day but below the 20 HIGH_VOL line (L007). 30d realized vol 4.54% (1m-scaled) vs 2.76% in the prior 30d window — **rising sharply**. QQQ (−1.50%) and SOXX (−1.64%) led Friday's decline. Not BULL (price below both MAs, bearish momentum cross), not HIGH_VOL yet (VIX < 20) — NEUTRAL, with an explicit **HIGH_VOL watch trigger**: VIX close > 20 with SPY still below both MAs.
- Consistency: gpt-5 called NEUTRAL this morning pre-open on 07-16 data ("daily alignment mixed and MACD crossed bearish"); Friday's close confirmed both signals on my evening data. Same call, independent windows.
- TLT 84.52, +0.37% Friday (flight-to-quality bid; still below its own MA20/50, L006) — rates are not the stress vector today; the move is equity-led de-risking into an earnings-heavy week.

## Core ETF Market Forecast Block (rules.md §Core ETF Market Forecast)

| ETF | Entry Price | Price Date | Price Tag | Trend (20d/50d) | 30d RVol | Beta vs SPY | mu | sigma | Sigma Source | Target Price | Target Date | 70% CI Lo | 70% CI Hi | Confidence | Ledger Rows |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SPY | 743.15 | 2026-07-17 | DELAYED | below MA20 745.01, below MA50 744.38 | 4.54% | 1 | +0.50% | 4.54% | REALIZED_VOL_30D | 746.87 | 2026-08-14 | 711.78 | 781.95 | MEDIUM | L197 |
| QQQ | 695.33 | 2026-07-17 | DELAYED | below MA20 718.35, below MA50 719.01 | 8.87% | 1.732 | +0.37% | 8.87% | REALIZED_VOL_30D | 697.9 | 2026-08-14 | 633.75 | 762.06 | LOW | L198 |
| SOXX | 521.81 | 2026-07-17 | DELAYED | below MA20 586.15, below MA50 566.37 | 22.04% | 3.707 | +0.35% | 22.04% | REALIZED_VOL_30D | 523.64 | 2026-08-14 | 404.04 | 643.23 | LOW | L199 |

mu derivation (rules.md §Core ETF): NEUTRAL SPY prior +0.5%, no adjustment (one down Friday is not a ledger-backed reason to leave the band's center; the CI covers it). QQQ = beta 1.732 × 0.5% − 0.5pp = **+0.37%** — the −0.5pp adjustment is ledger-backed deterioration: RS20 −4.06%, price below MA20/MA50, daily MACD below signal (L010), partially offset by RS60 +2.37%. SOXX = beta 3.707 × 0.5% − 1.5pp (full band) = **+0.35%** — RS20 −13.29%, −20.34% off the 60d high, rvol30 22.04% ≈ 1.65× the prior window, well below both MAs (L011); the beta-mechanical +1.85% would be indefensible against that tape, and the full-band cut is the maximum the rule allows without an evolution change. Confidence: SPY MEDIUM (trend/vol/RS coherent with a NEUTRAL call); QQQ and SOXX LOW (beta-derived positive mu against negative short-window trend — the derivation rule and the tape disagree; the CI bands are wide and honest about it). Beta note: 60d betas (QQQ 1.73, SOXX 3.71) are elevated by the July semis correction concentrating index variance; disclosed as computed, not smoothed.

Relative strength: QQQ/SPY −4.06% (20d) / +2.37% (60d); SOXX/SPY −13.29% (20d) / +18.48% (60d) — a violent short-window unwind inside a still-positive quarter (L010-L011). Regime-consistency: a NEUTRAL call with defensive cross-sectional leadership and semis distribution is internally coherent; the market-forecast sleeve's positive-but-shrunk mus reflect the prior table, not conviction.

## Event Concentration (flag)

Q2 earnings wave is at its peak inside the 2–6 week horizon: **27 of 65 preflight symbols sit inside the buffered 14-day penalty window** (L015), including RF/FITB (printed this morning, est. ±5d), CSX/NTRS/GL/MCO at 5d, WST/UNP/HBAN/SNA/NSC at 6d, FFIV 10d, IQV/BXP/INCY/UPS 11d, IEX/FTNT/HUM/ADP/CHRW 12d, BAX/AAPL 13d, ABBV/LIN/FRT/TROW 14d. Next FOMC is inside the horizon (late July). Downgrade-trigger #4 (>2 top names with earnings inside 14d) would bind on any GO attempt; academic under the structural NO_TRADE but recorded.

## Universe Handoff

`build_index_universe.py` ran before any price fetch: 515-name union (503 S&P 500 + 101 Nasdaq-100, 89 overlap; caches 2026-06-21, stale-cache rule applied), 514 eligible after filters — FDXF rejected (36 daily bars < 126 listing-age minimum). Full inclusion/exclusion log: 04. Handoff to `technical_indicators.py`: 514 eligible + SPY QQQ SOXX TLT (519 computed, 518 OK + FDXF error). Every regime, price, vol, beta, and event fact above carries a ledger row in 01.
