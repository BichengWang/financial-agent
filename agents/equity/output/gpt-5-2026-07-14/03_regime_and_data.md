# 03 Regime And Data

Data mode: `DELAYED`. This late daily run uses two-source-grounded July 14 intraday prices. The Yahoo technical helper, rankings, and regime moving averages include the July 14 partial daily bar; completed Nasdaq risk histories end July 13. Regime: `BULL` with `MEDIUM` confidence and a short-horizon cooling flag. SPY remains above its daily 20d/50d averages; QQQ and SOXX have mixed daily alignment but retain positive 60d momentum. Thirty-day realized volatility rose versus the preceding 30-day window for every core ETF.
Regime ledger rows: L001, L245, L206, L207, L008, L009, L010, L011, L012, L013, L014, L015, L016, L017, L018, L019, L020, L021, L022, L023, L024, L025

## Core ETF Market Forecast Block

| ETF | Entry Price | Price Date | Price Tag | 20d/50d MA | 30d RVol | Beta vs SPY | mu | sigma | Sigma Source | Target Price | Target Date | 70% CI Lo | 70% CI Hi | Confidence | Ledger Rows |
| --- | ---: | --- | --- | --- | ---: | ---: | ---: | ---: | --- | ---: | --- | ---: | ---: | --- | --- |
| SPY | 751.785 | 2026-07-14 | DELAYED | 744.88/742.65 | 4.47% | 1.00 | 2.00% | 4.47% | REALIZED_VOL_30D | 766.82 | 2026-08-11 | 731.89 | 801.75 | MEDIUM | L008,L009,L010,L011,L012,L013 |
| QQQ | 720.572 | 2026-07-14 | DELAYED | 722.26/717.22 | 8.69% | 1.69 | 3.62% | 8.69% | REALIZED_VOL_30D | 746.67 | 2026-08-11 | 681.57 | 811.77 | MEDIUM | L014,L015,L016,L017,L018,L019 |
| SOXX | 570.925 | 2026-07-14 | DELAYED | 596.89/562.49 | 22.17% | 3.59 | 7.68% | 22.17% | REALIZED_VOL_30D | 614.77 | 2026-08-11 | 483.10 | 746.43 | MEDIUM | L020,L021,L022,L023,L024,L025 |

SPY drawdown from its 60d high is -1.37%; QQQ -4.61%; SOXX -15.48%. Daily relative strength from the canonical helper: QQQ/SPY -1.46% over 20d and 5.37% over 60d; SOXX/SPY -5.60% and 33.50%.

Mu derivation: SPY uses the `BULL` +2.00% prior. QQQ uses `1.686 x 2.00% + 0.25pp = 3.62%`. SOXX uses `3.590 x 2.00% + 0.50pp = 7.68%`. Adjustments are within the allowed bands; QQQ/SOXX retain strong 60d relative strength but negative 20d relative strength, so confidence remains MEDIUM.

Universe handoff: 515 index-union names; 513 scoreable equities after excluding SATS and FDXF for insufficient bars. Price and listing-age screens pass for scored names. Full-universe market-cap, ADV, spread, exact session coverage, halt/delisting, and corporate-action fields are Enhancing and `UNAVAILABLE`; they lower DQ and prevent claiming those screens passed, but do not independently block GO under the Required-vs-Enhancing policy. The factor-evidence gates independently produce the monitoring-only result.

## Event Concentration

- Earnings penalty window: 0 of 20 published monitors fall inside the buffered 14-day event window. The nearest is AXON at 20 days with an estimated date; the ±5-day buffer requires a penalty only at 19 days or fewer. Ledger: L206.
- Earnings concentration: 12 of 20 monitors (60%) have estimated reports clustered August 3-6, inside the August 11 forecast horizon: DDOG, XYZ, MPC, CRL, EXPD, DVA, ANET, AMD, ALL, AXON, PSX, and GEN. This is not yet a hard event-window penalty, but it reinforces LOW equity confidence and creates horizon-level gap risk. Ledger: L207.
- Macro event: the Federal Reserve's July 28-29 FOMC meeting falls inside the 28-day forecast horizon. This is a book-wide confidence risk, not a per-name positive score contribution. Ledger: L245.
- Regime consistency: long-trend support is BULL-consistent; short-horizon QQQ/SOXX cooling and higher realized volatility prevent HIGH confidence.
