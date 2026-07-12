# 03 Regime And Data

Data mode: `DELAYED`. Regime: `BULL` with `MEDIUM` confidence and concentrated growth/semiconductor leadership. SPY and QQQ retain bullish daily MA alignment and positive 20d/60d momentum; SOXX has mixed daily alignment but strong 60d relative strength. Thirty-day realized volatility rose versus the preceding 30-day window: SPY 4.44% vs 2.92%, QQQ 8.58% vs 4.62%, SOXX 21.79% vs 12.79%. Ledger: L004-L015.

## Core ETF Market Forecast Block

| ETF | Entry Price | Price Date | Price Tag | 20d/50d MA | 30d RVol | Beta vs SPY | mu | sigma | Sigma Source | Target Price | Target Date | 70% CI Lo | 70% CI Hi | Confidence | Ledger Rows |
| --- | ---: | --- | --- | --- | ---: | ---: | ---: | ---: | --- | ---: | --- | ---: | ---: | --- | --- |
| SPY | 754.95 | 2026-07-10 | DELAYED | 743.81/741.24 | 4.44% | 1.00 | 2.00% | 4.44% | REALIZED_VOL_30D | 770.05 | 2026-08-09 | 735.16 | 804.94 | MEDIUM | L004,L005,L006,L007 |
| QQQ | 725.51 | 2026-07-10 | DELAYED | 722.57/715.16 | 8.58% | 1.68 | 3.87% | 8.58% | REALIZED_VOL_30D | 753.57 | 2026-08-09 | 688.85 | 818.29 | MEDIUM | L008,L009,L010,L011 |
| SOXX | 581.34 | 2026-07-10 | DELAYED | 599.82/558.23 | 21.79% | 3.52 | 8.04% | 21.79% | REALIZED_VOL_30D | 628.05 | 2026-08-09 | 496.29 | 759.81 | MEDIUM | L012,L013,L014,L015 |

SPY drawdown from its 60d high is -0.61%; QQQ -2.77%; SOXX -11.25%. Daily relative strength from the canonical helper: QQQ/SPY 0.52% over 20d and 6.71% over 60d; SOXX/SPY 3.29% and 36.18%. Rising volatility and SOXX's mixed short trend temper the BULL call.

Mu derivation: SPY uses the `BULL` +2.00% prior. QQQ uses `1.684 x 2.00% + 0.50pp = 3.87%`. SOXX uses `3.518 x 2.00% + 1.00pp = 8.04%`. Adjustments are within the allowed bands and supported by relative strength.

Universe handoff: 515 index-union names; 513 scoreable equities after excluding SATS and FDXF for insufficient bars. Price and listing-age filters pass for all scored names; full-universe market-cap, ADV, spread, session-calendar, halt/delisting, and corporate-action fields are `UNAVAILABLE` (L205-L206), so these are monitoring ranks and cannot support `GO`. Core ETFs remain isolated from candidate ranks. The nearest published earnings date is HOOD on 2026-07-29, 17 days away, outside the confirmed-date 14-day penalty window.

## Event Concentration

- Earnings concentration: 0 of 20 published monitors are inside the confirmed-date 14-day window; the cached schedule retry limitation is disclosed in `01`. No clustered-earnings stop fires.
- Macro event: the Federal Reserve's July 28-29 FOMC meeting falls inside the 28-day forecast horizon. This is a portfolio-wide event flag and confidence risk, not a per-name score contribution. Ledger: L199.
