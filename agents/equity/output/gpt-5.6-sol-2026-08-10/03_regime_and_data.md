# 03 — Regime and Data

## Data mode and regime

Data mode is `DELAYED`; every cited market value is the completed 2026-08-10 close. Regime is
`BULL`: SPY 773.03 is above MA20 751.37 and MA50 747.03, with +3.18% 20d and +4.40% 60d
momentum [L601]. VIX is 15.46 versus 14.90 prior [L004-L005], and only 48.14% of scored names
have bullish daily MA alignment [L019], so confidence stays restrained.

The next FOMC meeting is September 15-16, inside the slow 42-day research horizon but outside
the default September 7 target [L027]. The default target falls on Labor Day; settlement will
use the September 4 close under `WEEKEND_TARGET` [L029].

## Core ETF Market Forecast Block

| ETF | Entry Price | Price Date | Price Tag | Trend (20d/50d) | 30d RVol | Beta vs SPY | mu | sigma | Sigma Source | Target Price | Target Date | 70% CI Lo | 70% CI Hi | Confidence | Ledger Rows |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SPY | $773.03 | 2026-08-10 | HISTORICAL | BULLISH (751.37/747.03) | 3.75% | 1.0000 | 2.00% | 3.75% | REALIZED_VOL_30D | $788.49 | 2026-09-07 | $758.38 | $818.60 | MEDIUM | L601 |
| QQQ | $720.87 | 2026-08-10 | HISTORICAL | MIXED (700.80/714.03) | 7.23% | 1.7099 | 3.42% | 7.23% | REALIZED_VOL_30D | $745.52 | 2026-09-07 | $691.34 | $799.71 | MEDIUM | L602 |
| SOXX | $529.39 | 2026-08-10 | HISTORICAL | MIXED (527.70/565.61) | 17.78% | 3.4761 | 6.95% | 17.78% | REALIZED_VOL_30D | $566.19 | 2026-09-07 | $468.29 | $664.10 | MEDIUM | L603 |

### Relative strength and consistency

- SPY: 30d realized vol fell from 4.31% to 3.75%; 60d drawdown is -4.49%. Trend is consistent with `BULL` [L601].
- QQQ: RS is -1.90% over 20d and -3.43% over 60d vs SPY; 30d vol fell to 7.23%. Mixed MA alignment tempers the broad bull call [L602].
- SOXX: RS is -7.55% over 20d and -4.14% over 60d; 60d drawdown is -29.01%. The semiconductor sleeve is the clearest inconsistency with `BULL` [L603].

Each ETF mu is mechanical: SPY uses the +2.00% BULL prior; QQQ and SOXX use 60d beta times
that prior, with no discretionary adjustment.

## Universe handoff

The 515-name union produced 511 scored names. Data/Regime handed those names and the three ETF
records to Technical and Factor Scoring; four exclusions are documented in `04` [L010-L019].
