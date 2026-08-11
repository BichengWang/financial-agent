# 12 — Close Log

## Completed-close state

The run used the completed Monday 2026-08-10 regular-session close. StockAnalysis and CNBC
agreed exactly on all 23 published entries [L016]. SPY closed 773.03; VIX closed 15.46 and the
13-week bank-discount rate was 3.74% [L004,L006,L015].

## Settlement close

All 200 due keys were published before closeout: 50 `ORDINARY`, 73 `WEEKEND_TARGET`, and 77
same-day `TARGET_DATE_CLOSE` rows with timezone-aware settled-at timestamps after 16:00 ET.
Post-publication normalization: EQ 819, MF 132, due 0, conflicts 0, rejected 87 [L018,L028].

## Final state

- Regime: `BULL`.
- Status: `NO_TRADE`.
- Forecasts: 20 equity monitors + SPY/QQQ/SOXX.
- Portfolio: none; diagnostic drawdown and sector caps fail.
- Evolution: one Track A scoring-weight proposal logged and deferred at `eff_n=2`.

No intraday or after-hours print is used as an entry or settlement price.
