# 03 — Regime and Data — 2026-08-03

## Data mode and integrity

Data mode is `DELAYED`: completed 2026-08-03 closes and five-year histories were fetched
during this run. The universe helper succeeded at 515 names; 511
passed the eligibility/technical minimum and 4 were rejected.

## Regime assessment

| Field | Value | Ledger |
| --- | --- | --- |
| Regime | BULL | L-TI-SPY, L-MAC-VIX, L-MAC-VIX60 |
| SPY trend | ABOVE/MA20; ABOVE/MA50; RS60 +0.00% | L-TI-SPY |
| VIX | 15.86 vs recent mean 17.2415 | L-MAC-VIX, L-MAC-VIX60 |
| Event concentration | 153/511 scoreable names and 0/20 published names have earnings inside 14d | L-EA-* |
| Data quality | 0.80; Fundamental and Sentiment unavailable | L-UNA-FUND, L-UNA-SENT |

## Core ETF Market Forecast Block

| ETF | Entry | Price date | Tag | Trend 20d/50d | 30d RVol | Beta vs SPY | mu | sigma | Sigma source | Target | Target date | 70% CI Lo | 70% CI Hi | Confidence | Ledger |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SPY | $757.67 | 2026-08-03 | HISTORICAL | ABOVE/ABOVE | 3.83% | +1.000 | +2.00% | 3.83% | REALIZED_VOL_30D | $772.82 | 2026-08-31 | $742.68 | $802.97 | MEDIUM | L-PX-SPY, L-TI-SPY, L-RM-SPY |
| QQQ | $700.07 | 2026-08-03 | HISTORICAL | ABOVE/BELOW | 7.30% | +1.706 | +1.91% | 7.30% | REALIZED_VOL_30D | $713.46 | 2026-08-31 | $660.30 | $766.61 | MEDIUM | L-PX-QQQ, L-TI-QQQ, L-RM-QQQ |
| SOXX | $507.68 | 2026-08-03 | HISTORICAL | BELOW/BELOW | 18.92% | +3.530 | +5.56% | 18.92% | REALIZED_VOL_30D | $535.91 | 2026-08-31 | $436.03 | $635.78 | MEDIUM | L-PX-SOXX, L-TI-SOXX, L-RM-SOXX |

Relative strength: QQQ vs SPY is -4.00%
over 20d and -2.78% over 60d;
SOXX vs SPY is -13.55% and
-3.30%. The ETF forecasts obey
the existing regime-prior/beta rule; its known category-error concern remains deferred under
Track A because `eff_n=1`. Confidence stays `MEDIUM`.

## Handoff

The exact 515-name union plus SPY/QQQ/SOXX was handed to `technical_indicators.py`; TLT was
fetched separately for rate-sensitivity diagnostics. No sampled-universe fallback was used.
