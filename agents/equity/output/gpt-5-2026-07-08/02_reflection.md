# 02 Reflection

## 0. Prediction Settlement

Scanned prior `15_predictions.json` files. 12 OPEN predictions matured by 2026-07-08; all were from the 2026-06-10 `claude-fable-5` ledger.

| Ticker | Vintage | Entry | Target Date | mu | Current Price | Realized Return | SPY Return | Alpha | Direction | CI Result | z |
| --- | --- | ---: | --- | ---: | ---: | ---: | ---: | ---: | --- | --- | ---: |
| MCK | 2026-06-10 | 790.22 | 2026-07-08 | 6.00% | 815.34 | 3.18% | 2.28% | 0.90% | HIT | IN_CI | -0.43 |
| COST | 2026-06-10 | 980.45 | 2026-07-08 | 6.00% | 953.77 | -2.72% | 2.28% | -5.00% | MISS | OUT_CI_LOW | -1.12 |
| WMT | 2026-06-10 | 119.83 | 2026-07-08 | 5.00% | 112.85 | -5.82% | 2.28% | -8.11% | MISS | OUT_CI_LOW | -1.09 |
| CVX | 2026-06-10 | 191.01 | 2026-07-08 | 5.00% | 175.74 | -7.99% | 2.28% | -10.27% | MISS | OUT_CI_LOW | -1.78 |
| UNH | 2026-06-10 | 407.13 | 2026-07-08 | 4.00% | 426.86 | 4.85% | 2.28% | 2.57% | HIT | IN_CI | 0.10 |
| MU | 2026-06-10 | 891.66 | 2026-07-08 | 1.00% | 937.60 | 5.15% | 2.28% | 2.87% | HIT | IN_CI | 0.14 |
| XOM | 2026-06-10 | 151.35 | 2026-07-08 | 2.00% | 140.22 | -7.35% | 2.28% | -9.63% | MISS | OUT_CI_LOW | -1.08 |
| LIN | 2026-06-10 | 509.20 | 2026-07-08 | 2.00% | 529.08 | 3.90% | 2.28% | 1.62% | HIT | IN_CI | 0.30 |
| LLY | 2026-06-10 | 1138.16 | 2026-07-08 | 2.00% | 1222.50 | 7.41% | 2.28% | 5.13% | HIT | IN_CI | 0.49 |
| NVDA | 2026-06-10 | 201.65 | 2026-07-08 | 1.00% | 202.59 | 0.47% | 2.28% | -1.81% | MISS | IN_CI | -0.04 |
| GOOGL | 2026-06-10 | 356.64 | 2026-07-08 | 1.00% | 360.04 | 0.95% | 2.28% | -1.33% | MISS | IN_CI | -0.00 |
| ABBV | 2026-06-10 | 225.82 | 2026-07-08 | 1.00% | 253.81 | 12.39% | 2.28% | 10.11% | HIT | OUT_CI_HIGH | 1.32 |

## Rolling Calibration Metrics

| Metric | Value | Note |
| --- | ---: | --- |
| Hit rate | 50.0% | Equity-alpha settlements only; minimum-N satisfied with 12 records. |
| CI coverage | 58.3% | Target 55%-85% healthy band. |
| Mean z | -0.27 | Realized return minus forecast mu over forecast sigma. |
| Rank IC | -0.51 | Spearman rank correlation of vintage adj_score vs realized alpha. |
| Market forecast line | INSUFFICIENT_SETTLED_N | No matured MARKET_FORECAST records in this settlement batch. |

## 1. Prior Run Summary

Same-model MoM baseline selected by the runbook algorithm: `investments/equity/output/gpt-5-2026-06-09` (`SAME_MODEL_BASELINE`). That run was `REVIEW_ONLY` and listed MCK, PG, WMT, ABBV, JPM, XOM, AZO, and UNH as review-only monitors.

## 2. MoM Price & Return Table

| Ticker | Prior Date | Prior Price | Current Date | Current Price | MoM Return | SPY Return | Alpha | Hit/Miss | Notes |
| --- | --- | ---: | --- | ---: | ---: | ---: | ---: | --- | --- |
| MCK | 2026-06-09 | 784.23 | 2026-07-08 | 815.34 | 3.97% | 1.07% | 2.90% | HIT | Source rows L066,L067 and L002 |
| PG | 2026-06-09 | 148.67 | 2026-07-08 | 148.91 | 0.16% | 1.07% | -0.90% | MISS | Source rows L068,L069 and L002 |
| WMT | 2026-06-09 | 118.88 | 2026-07-08 | 112.85 | -5.07% | 1.07% | -6.14% | MISS | Source rows L070,L071 and L002 |
| ABBV | 2026-06-09 | 225.42 | 2026-07-08 | 253.81 | 12.59% | 1.07% | 11.53% | HIT | Source rows L072,L073 and L002 |
| JPM | 2026-06-09 | 312.70 | 2026-07-08 | 333.09 | 6.52% | 1.07% | 5.45% | HIT | Source rows L074,L075 and L002 |
| XOM | 2026-06-09 | 148.91 | 2026-07-08 | 140.22 | -5.84% | 1.07% | -6.90% | MISS | Source rows L076,L077 and L002 |
| AZO | 2026-06-09 | 3137.75 | 2026-07-08 | 3072.17 | -2.09% | 1.07% | -3.16% | MISS | Source rows L078,L079 and L002 |
| UNH | 2026-06-09 | 413.00 | 2026-07-08 | 426.86 | 3.36% | 1.07% | 2.29% | HIT | Source rows L080,L081 and L002 |

## 3. Theme-Level Performance

Defensive health care and staples were mixed: MCK and UNH carried acceptable absolute behavior, but several defensive names lagged SPY's strong MoM gain. High-beta AI and semiconductor monitors from the June 10 cross-model ledger had wide dispersion, with MU and NVDA generating positive alpha while several defensive candidates missed their alpha targets.

## 4. Regime Shift Assessment

Prior baseline emphasized HIGH_VOL/RATE_SHOCK defense. July 8 delayed history supports a `NEUTRAL` label: SPY remains above 20d/50d moving averages, while QQQ and SOXX show negative 20d momentum and daily MACD below signal despite strong 60d relative strength.

## 5. Carry-Forward Decisions

| Ticker/Theme | Prior Score | Prior Thesis | MoM Return | Decision | Rationale |
| --- | ---: | --- | ---: | --- | --- |
| MCK | UNAVAILABLE | 2026-06-09 review-only monitor | 3.97% | CARRY | Alpha vs SPY was 2.90%; decision is binding only where current ledger evidence reconfirms the name. |
| PG | UNAVAILABLE | 2026-06-09 review-only monitor | 0.16% | DOWNGRADE | Alpha vs SPY was -0.90%; decision is binding only where current ledger evidence reconfirms the name. |
| WMT | UNAVAILABLE | 2026-06-09 review-only monitor | -5.07% | DROP | Alpha vs SPY was -6.14%; decision is binding only where current ledger evidence reconfirms the name. |
| ABBV | UNAVAILABLE | 2026-06-09 review-only monitor | 12.59% | CARRY | Alpha vs SPY was 11.53%; decision is binding only where current ledger evidence reconfirms the name. |
| JPM | UNAVAILABLE | 2026-06-09 review-only monitor | 6.52% | CARRY | Alpha vs SPY was 5.45%; decision is binding only where current ledger evidence reconfirms the name. |
| XOM | UNAVAILABLE | 2026-06-09 review-only monitor | -5.84% | DROP | Alpha vs SPY was -6.90%; decision is binding only where current ledger evidence reconfirms the name. |
| AZO | UNAVAILABLE | 2026-06-09 review-only monitor | -2.09% | DROP | Alpha vs SPY was -3.16%; decision is binding only where current ledger evidence reconfirms the name. |
| UNH | UNAVAILABLE | 2026-06-09 review-only monitor | 3.36% | CARRY | Alpha vs SPY was 2.29%; decision is binding only where current ledger evidence reconfirms the name. |

## 6. Sign-Off

Freshness tag: `DELAYED` for all settlement and MoM prices, retrieved during this run at 2026-07-08T17:44:20Z. Reflection confidence: `MEDIUM` for price settlement math and `LOW` for thesis validation because non-price feeds remain unavailable.
