# Reflection — 2026-07-17

## 0. Prediction Settlement

The canonical normalizer scanned `52` prior/current packages. All `63` due keys were grounded and settled; the regenerated manifest reports `0` due and `0` conflicts.

| Ticker | Type | Vintage | Entry | Target Date | mu | Realized Return | SPY Return | Alpha | Direction | CI Result | z | Price Date | Convention | Ledger Rows |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ABBV | EQUITY_ALPHA | claude-fable-5:2026-06-10 | 225.820 | 2026-07-08 | +1.00% | +11.92% | +2.35% | +9.57% | HIT | OUT_CI_HIGH | 1.270 | 2026-07-08 | TARGET_DATE_CLOSE | L014,L015 |
| COST | EQUITY_ALPHA | claude-fable-5:2026-06-10 | 980.450 | 2026-07-08 | +6.00% | -2.79% | +2.35% | -5.13% | MISS | OUT_CI_LOW | -1.131 | 2026-07-08 | TARGET_DATE_CLOSE | L016,L017 |
| CVX | EQUITY_ALPHA | claude-fable-5:2026-06-10 | 191.010 | 2026-07-08 | +5.00% | -7.87% | +2.35% | -10.22% | MISS | OUT_CI_LOW | -1.768 | 2026-07-08 | TARGET_DATE_CLOSE | L018,L019 |
| GOOGL | EQUITY_ALPHA | claude-fable-5:2026-06-10 | 356.640 | 2026-07-08 | +1.00% | +1.48% | +2.35% | -0.87% | MISS | IN_CI | 0.046 | 2026-07-08 | TARGET_DATE_CLOSE | L020,L021 |
| LIN | EQUITY_ALPHA | claude-fable-5:2026-06-10 | 509.200 | 2026-07-08 | +2.00% | +3.63% | +2.35% | +1.28% | HIT | IN_CI | 0.259 | 2026-07-08 | TARGET_DATE_CLOSE | L022,L023 |
| LLY | EQUITY_ALPHA | claude-fable-5:2026-06-10 | 1138.160 | 2026-07-08 | +2.00% | +6.82% | +2.35% | +4.48% | HIT | IN_CI | 0.438 | 2026-07-08 | TARGET_DATE_CLOSE | L024,L025 |
| MCK | EQUITY_ALPHA | claude-fable-5:2026-06-10 | 790.220 | 2026-07-08 | +6.00% | +3.60% | +2.35% | +1.25% | HIT | IN_CI | -0.370 | 2026-07-08 | TARGET_DATE_CLOSE | L026,L027 |
| MU | EQUITY_ALPHA | claude-fable-5:2026-06-10 | 891.660 | 2026-07-08 | +1.00% | +6.41% | +2.35% | +4.06% | HIT | IN_CI | 0.185 | 2026-07-08 | TARGET_DATE_CLOSE | L028,L029 |
| NVDA | EQUITY_ALPHA | claude-fable-5:2026-06-10 | 201.650 | 2026-07-08 | +1.00% | +1.22% | +2.35% | -1.12% | MISS | IN_CI | 0.019 | 2026-07-08 | TARGET_DATE_CLOSE | L030,L031 |
| UNH | EQUITY_ALPHA | claude-fable-5:2026-06-10 | 407.130 | 2026-07-08 | +4.00% | +4.54% | +2.35% | +2.19% | HIT | IN_CI | 0.065 | 2026-07-08 | TARGET_DATE_CLOSE | L032,L033 |
| WMT | EQUITY_ALPHA | claude-fable-5:2026-06-10 | 119.830 | 2026-07-08 | +5.00% | -5.62% | +2.35% | -7.96% | MISS | OUT_CI_LOW | -1.068 | 2026-07-08 | TARGET_DATE_CLOSE | L034,L035 |
| XOM | EQUITY_ALPHA | claude-fable-5:2026-06-10 | 151.350 | 2026-07-08 | +2.00% | -6.75% | +2.35% | -9.10% | MISS | IN_CI | -1.007 | 2026-07-08 | TARGET_DATE_CLOSE | L036,L037 |
| ABBV | EQUITY_ALPHA | gpt-5:2026-06-11 | 226.955 | 2026-07-09 | +5.00% | +10.11% | +2.24% | +7.88% | HIT | IN_CI | 0.717 | 2026-07-09 | TARGET_DATE_CLOSE | L038,L039 |
| AMT | EQUITY_ALPHA | gpt-5:2026-06-11 | 190.495 | 2026-07-09 | +3.00% | -13.38% | +2.24% | -15.62% | MISS | OUT_CI_LOW | -1.881 | 2026-07-09 | TARGET_DATE_CLOSE | L040,L041 |
| ANET | EQUITY_ALPHA | gpt-5:2026-06-11 | 155.370 | 2026-07-09 | +3.00% | +18.87% | +2.24% | +16.63% | HIT | IN_CI | 0.840 | 2026-07-09 | TARGET_DATE_CLOSE | L042,L043 |
| BAC | EQUITY_ALPHA | gpt-5:2026-06-11 | 55.110 | 2026-07-09 | +4.00% | +7.51% | +2.24% | +5.27% | HIT | IN_CI | 0.552 | 2026-07-09 | TARGET_DATE_CLOSE | L044,L045 |
| COP | EQUITY_ALPHA | gpt-5:2026-06-11 | 117.315 | 2026-07-09 | +1.00% | -7.92% | +2.24% | -10.16% | MISS | IN_CI | -1.008 | 2026-07-09 | TARGET_DATE_CLOSE | L046,L047 |
| CVX | EQUITY_ALPHA | gpt-5:2026-06-11 | 188.140 | 2026-07-09 | +6.00% | -7.49% | +2.24% | -9.73% | MISS | OUT_CI_LOW | -1.818 | 2026-07-09 | TARGET_DATE_CLOSE | L048,L049 |
| GE | EQUITY_ALPHA | gpt-5:2026-06-11 | 328.940 | 2026-07-09 | +2.00% | +9.15% | +2.24% | +6.91% | HIT | IN_CI | 0.636 | 2026-07-09 | TARGET_DATE_CLOSE | L050,L051 |
| GOOGL | EQUITY_ALPHA | gpt-5:2026-06-11 | 353.820 | 2026-07-09 | +5.00% | +1.43% | +2.24% | -0.81% | MISS | IN_CI | -0.306 | 2026-07-09 | TARGET_DATE_CLOSE | L052,L053 |
| GS | EQUITY_ALPHA | gpt-5:2026-06-11 | 1024.620 | 2026-07-09 | +2.00% | +3.06% | +2.24% | +0.82% | HIT | IN_CI | 0.104 | 2026-07-09 | TARGET_DATE_CLOSE | L054,L055 |
| JNJ | EQUITY_ALPHA | gpt-5:2026-06-11 | 239.595 | 2026-07-09 | +4.00% | +8.14% | +2.24% | +5.90% | HIT | IN_CI | 0.728 | 2026-07-09 | TARGET_DATE_CLOSE | L056,L057 |
| JPM | EQUITY_ALPHA | gpt-5:2026-06-11 | 313.910 | 2026-07-09 | +1.00% | +6.87% | +2.24% | +4.63% | HIT | IN_CI | 0.917 | 2026-07-09 | TARGET_DATE_CLOSE | L058,L059 |
| KO | EQUITY_ALPHA | gpt-5:2026-06-11 | 83.385 | 2026-07-09 | +2.00% | -0.91% | +2.24% | -3.14% | MISS | IN_CI | -0.500 | 2026-07-09 | TARGET_DATE_CLOSE | L060,L061 |
| LLY | EQUITY_ALPHA | gpt-5:2026-06-11 | 1163.720 | 2026-07-09 | +6.00% | +4.57% | +2.24% | +2.34% | HIT | IN_CI | -0.120 | 2026-07-09 | TARGET_DATE_CLOSE | L062,L063 |
| MCK | EQUITY_ALPHA | gpt-5:2026-06-11 | 791.800 | 2026-07-09 | +2.00% | +0.13% | +2.24% | -2.11% | MISS | IN_CI | -0.211 | 2026-07-09 | TARGET_DATE_CLOSE | L064,L065 |
| ORCL | EQUITY_ALPHA | gpt-5:2026-06-11 | 182.330 | 2026-07-09 | +1.00% | -20.90% | +2.24% | -23.14% | MISS | OUT_CI_LOW | -1.091 | 2026-07-09 | TARGET_DATE_CLOSE | L066,L067 |
| PG | EQUITY_ALPHA | gpt-5:2026-06-11 | 149.335 | 2026-07-09 | +1.00% | -1.66% | +2.24% | -3.90% | MISS | IN_CI | -0.372 | 2026-07-09 | TARGET_DATE_CLOSE | L068,L069 |
| UNH | EQUITY_ALPHA | gpt-5:2026-06-11 | 406.330 | 2026-07-09 | +6.00% | +6.24% | +2.24% | +4.00% | HIT | IN_CI | 0.032 | 2026-07-09 | TARGET_DATE_CLOSE | L070,L071 |
| AAPL | EQUITY_ALPHA | gpt-5:2026-06-18 | 297.520 | 2026-07-16 | +1.00% | +12.01% | +0.54% | +11.47% | HIT | OUT_CI_HIGH | 1.745 | 2026-07-16 | TARGET_DATE_CLOSE | L072,L073 |
| AVGO | EQUITY_ALPHA | gpt-5:2026-06-18 | 407.500 | 2026-07-16 | +2.00% | -8.11% | +0.54% | -8.65% | MISS | IN_CI | -0.546 | 2026-07-16 | TARGET_DATE_CLOSE | L074,L075 |
| BAC | EQUITY_ALPHA | gpt-5:2026-06-18 | 56.220 | 2026-07-16 | +2.00% | +9.37% | +0.54% | +8.83% | HIT | OUT_CI_HIGH | 1.186 | 2026-07-16 | TARGET_DATE_CLOSE | L076,L077 |
| CAT | EQUITY_ALPHA | gpt-5:2026-06-18 | 988.580 | 2026-07-16 | +6.00% | -11.27% | +0.54% | -11.81% | MISS | OUT_CI_LOW | -1.405 | 2026-07-16 | TARGET_DATE_CLOSE | L078,L079 |
| CVX | EQUITY_ALPHA | gpt-5:2026-06-18 | 173.710 | 2026-07-16 | +1.00% | +5.84% | +0.54% | +5.30% | HIT | IN_CI | 0.646 | 2026-07-16 | TARGET_DATE_CLOSE | L080,L081 |
| EQIX | EQUITY_ALPHA | gpt-5:2026-06-18 | 1099.880 | 2026-07-16 | +1.00% | -8.25% | +0.54% | -8.79% | MISS | OUT_CI_LOW | -1.643 | 2026-07-16 | TARGET_DATE_CLOSE | L082,L083 |
| ETN | EQUITY_ALPHA | gpt-5:2026-06-18 | 423.030 | 2026-07-16 | +2.00% | -6.33% | +0.54% | -6.87% | MISS | IN_CI | -0.600 | 2026-07-16 | TARGET_DATE_CLOSE | L084,L085 |
| FCX | EQUITY_ALPHA | gpt-5:2026-06-18 | 68.590 | 2026-07-16 | +4.00% | -14.62% | +0.54% | -15.16% | MISS | OUT_CI_LOW | -1.185 | 2026-07-16 | TARGET_DATE_CLOSE | L086,L087 |
| GE | EQUITY_ALPHA | gpt-5:2026-06-18 | 359.120 | 2026-07-16 | +5.00% | -3.73% | +0.54% | -4.27% | MISS | IN_CI | -0.869 | 2026-07-16 | TARGET_DATE_CLOSE | L088,L089 |
| GOOGL | EQUITY_ALPHA | gpt-5:2026-06-18 | 367.900 | 2026-07-16 | +6.00% | -3.65% | +0.54% | -4.19% | MISS | OUT_CI_LOW | -1.163 | 2026-07-16 | TARGET_DATE_CLOSE | L090,L091 |
| GS | EQUITY_ALPHA | gpt-5:2026-06-18 | 1102.110 | 2026-07-16 | +5.00% | -0.60% | +0.54% | -1.14% | MISS | IN_CI | -0.560 | 2026-07-16 | TARGET_DATE_CLOSE | L092,L093 |
| JPM | EQUITY_ALPHA | gpt-5:2026-06-18 | 327.560 | 2026-07-16 | +2.00% | +4.76% | +0.54% | +4.22% | HIT | IN_CI | 0.381 | 2026-07-16 | TARGET_DATE_CLOSE | L094,L095 |
| LLY | EQUITY_ALPHA | gpt-5:2026-06-18 | 1102.120 | 2026-07-16 | +4.00% | +6.08% | +0.54% | +5.54% | HIT | IN_CI | 0.231 | 2026-07-16 | TARGET_DATE_CLOSE | L096,L097 |
| QQQ | MARKET_FORECAST | gpt-5:2026-06-18 | 739.680 | 2026-07-16 | +3.56% | -4.56% | N/A | N/A | MISS | OUT_CI_LOW | -1.067 | 2026-07-16 | TARGET_DATE_CLOSE | L098,L099 |
| SOXX | MARKET_FORECAST | gpt-5:2026-06-18 | 639.460 | 2026-07-16 | +6.56% | -17.04% | N/A | N/A | MISS | OUT_CI_LOW | -1.223 | 2026-07-16 | TARGET_DATE_CLOSE | L100,L101 |
| SPY | MARKET_FORECAST | gpt-5:2026-06-18 | 746.680 | 2026-07-16 | +2.00% | +0.54% | N/A | N/A | HIT | IN_CI | -0.347 | 2026-07-16 | TARGET_DATE_CLOSE | L102,L103 |
| UNH | EQUITY_ALPHA | gpt-5:2026-06-18 | 402.220 | 2026-07-16 | +3.00% | +5.26% | +0.54% | +4.72% | HIT | IN_CI | 0.298 | 2026-07-16 | TARGET_DATE_CLOSE | L104,L105 |
| AVGO | EQUITY_ALPHA | gpt-5:2026-06-19 | 411.350 | 2026-07-17 | +1.00% | -8.97% | +0.53% | -9.50% | MISS | IN_CI | -0.534 | 2026-07-16 | TARGET_EQ_RUN_DATE | L106,L107 |
| BAC | EQUITY_ALPHA | gpt-5:2026-06-19 | 56.200 | 2026-07-17 | +3.00% | +9.41% | +0.53% | +8.88% | HIT | IN_CI | 1.031 | 2026-07-16 | TARGET_EQ_RUN_DATE | L108,L109 |
| CAT | EQUITY_ALPHA | gpt-5:2026-06-19 | 985.820 | 2026-07-17 | +6.00% | -11.02% | +0.53% | -11.55% | MISS | OUT_CI_LOW | -1.391 | 2026-07-16 | TARGET_EQ_RUN_DATE | L110,L111 |
| CVX | EQUITY_ALPHA | gpt-5:2026-06-19 | 173.630 | 2026-07-17 | +2.00% | +5.89% | +0.53% | +5.36% | HIT | IN_CI | 0.519 | 2026-07-16 | TARGET_EQ_RUN_DATE | L112,L113 |
| EQIX | EQUITY_ALPHA | gpt-5:2026-06-19 | 1092.190 | 2026-07-17 | +2.00% | -7.60% | +0.53% | -8.14% | MISS | OUT_CI_LOW | -1.724 | 2026-07-16 | TARGET_EQ_RUN_DATE | L114,L115 |
| ETN | EQUITY_ALPHA | gpt-5:2026-06-19 | 421.770 | 2026-07-17 | +1.00% | -6.05% | +0.53% | -6.58% | MISS | IN_CI | -0.509 | 2026-07-16 | TARGET_EQ_RUN_DATE | L116,L117 |
| FCX | EQUITY_ALPHA | gpt-5:2026-06-19 | 68.680 | 2026-07-17 | +4.00% | -14.74% | +0.53% | -15.27% | MISS | OUT_CI_LOW | -1.193 | 2026-07-16 | TARGET_EQ_RUN_DATE | L118,L119 |
| GE | EQUITY_ALPHA | gpt-5:2026-06-19 | 357.640 | 2026-07-17 | +5.00% | -3.33% | +0.53% | -3.86% | MISS | IN_CI | -0.829 | 2026-07-16 | TARGET_EQ_RUN_DATE | L120,L121 |
| GOOGL | EQUITY_ALPHA | gpt-5:2026-06-19 | 368.030 | 2026-07-17 | +6.00% | -3.69% | +0.53% | -4.22% | MISS | OUT_CI_LOW | -1.167 | 2026-07-16 | TARGET_EQ_RUN_DATE | L122,L123 |
| GS | EQUITY_ALPHA | gpt-5:2026-06-19 | 1096.560 | 2026-07-17 | +5.00% | -0.10% | +0.53% | -0.63% | MISS | IN_CI | -0.509 | 2026-07-16 | TARGET_EQ_RUN_DATE | L124,L125 |
| JPM | EQUITY_ALPHA | gpt-5:2026-06-19 | 325.220 | 2026-07-17 | +2.00% | +5.51% | +0.53% | +4.98% | HIT | IN_CI | 0.475 | 2026-07-16 | TARGET_EQ_RUN_DATE | L126,L127 |
| LIN | EQUITY_ALPHA | gpt-5:2026-06-19 | 512.150 | 2026-07-17 | +1.00% | +1.68% | +0.53% | +1.14% | HIT | IN_CI | 0.122 | 2026-07-16 | TARGET_EQ_RUN_DATE | L128,L129 |
| LLY | EQUITY_ALPHA | gpt-5:2026-06-19 | 1098.570 | 2026-07-17 | +4.00% | +6.43% | +0.53% | +5.89% | HIT | IN_CI | 0.268 | 2026-07-16 | TARGET_EQ_RUN_DATE | L130,L131 |
| QQQ | MARKET_FORECAST | gpt-5:2026-06-19 | 740.620 | 2026-07-17 | +2.87% | -4.68% | N/A | N/A | MISS | IN_CI | -0.990 | 2026-07-16 | TARGET_EQ_RUN_DATE | L132,L133 |
| SOXX | MARKET_FORECAST | gpt-5:2026-06-19 | 639.450 | 2026-07-17 | +5.56% | -17.04% | N/A | N/A | MISS | OUT_CI_LOW | -1.171 | 2026-07-16 | TARGET_EQ_RUN_DATE | L134,L135 |
| SPY | MARKET_FORECAST | gpt-5:2026-06-19 | 746.740 | 2026-07-17 | +2.00% | +0.53% | N/A | N/A | HIT | IN_CI | -0.348 | 2026-07-16 | TARGET_EQ_RUN_DATE | L136,L137 |
| UNH | EQUITY_ALPHA | gpt-5:2026-06-19 | 400.960 | 2026-07-17 | +2.00% | +5.59% | +0.53% | +5.06% | HIT | IN_CI | 0.474 | 2026-07-16 | TARGET_EQ_RUN_DATE | L138,L139 |

### Rolling Calibration

| Type | n | Hit Rate | CI Coverage | Mean z | Weighted Rank IC | Ledger Rows |
| --- | --- | --- | --- | --- | --- | --- |
| EQUITY_ALPHA | 119 | 55.46% | 79.83% | -0.174496 | -0.008757 | L336,L337 |
| MARKET_FORECAST | 18 | 33.33% | 77.78% | -0.619734 | N/A | L338 |

Equity CI coverage remains in the healthy 55–85% band, but weighted rank IC is non-positive over 119 records. Per policy, confidence is capped at `MEDIUM` and the Evolution priority is factor calibration. Today’s monitor records are already `LOW` because only one family is supportive.

## 1. Prior Run Summary

- Baseline: `agents/equity/output/gpt-5-2026-06-19` — exact same-model 28-day target, exception flag `NONE` (L013,L339).
- Prior status / regime: `NO_TRADE` / `BULL` (L339).
- Prior top five: CAT, GOOGL, GS, GE, LLY (L339).
- The prior run published a 14-equity paper forecast basket plus SPY/QQQ/SOXX and rejected execution because its capped investable basket could not reach the protected portfolio beta band.

## 2. MoM Price and Return Table

| Ticker | Prior Date | Prior Price | Current Date | Current Price | MoM Return | SPY Return | Alpha | Hit/Miss | CI Result | Ledger Rows |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CAT | 2026-06-18 | 985.820 | 2026-07-16 | 877.170 | -11.02% | +0.53% | -11.55% | MISS | OUT_CI_LOW | L110,L111 |
| GOOGL | 2026-06-18 | 368.030 | 2026-07-16 | 354.460 | -3.69% | +0.53% | -4.22% | MISS | OUT_CI_LOW | L122,L123 |
| GS | 2026-06-18 | 1096.560 | 2026-07-16 | 1095.460 | -0.10% | +0.53% | -0.63% | MISS | IN_CI | L124,L125 |
| GE | 2026-06-18 | 357.640 | 2026-07-16 | 345.730 | -3.33% | +0.53% | -3.86% | MISS | IN_CI | L120,L121 |
| LLY | 2026-06-18 | 1098.570 | 2026-07-16 | 1169.170 | +6.43% | +0.53% | +5.89% | HIT | IN_CI | L130,L131 |
| FCX | 2026-06-18 | 68.680 | 2026-07-16 | 58.560 | -14.74% | +0.53% | -15.27% | MISS | OUT_CI_LOW | L118,L119 |
| BAC | 2026-06-18 | 56.200 | 2026-07-16 | 61.490 | +9.41% | +0.53% | +8.88% | HIT | IN_CI | L108,L109 |
| UNH | 2026-06-18 | 400.960 | 2026-07-16 | 423.380 | +5.59% | +0.53% | +5.06% | HIT | IN_CI | L138,L139 |
| JPM | 2026-06-18 | 325.220 | 2026-07-16 | 343.150 | +5.51% | +0.53% | +4.98% | HIT | IN_CI | L126,L127 |
| CVX | 2026-06-18 | 173.630 | 2026-07-16 | 183.860 | +5.89% | +0.53% | +5.36% | HIT | IN_CI | L112,L113 |
| EQIX | 2026-06-18 | 1092.190 | 2026-07-16 | 1009.140 | -7.60% | +0.53% | -8.14% | MISS | OUT_CI_LOW | L114,L115 |
| ETN | 2026-06-18 | 421.770 | 2026-07-16 | 396.270 | -6.05% | +0.53% | -6.58% | MISS | IN_CI | L116,L117 |
| AVGO | 2026-06-18 | 411.350 | 2026-07-16 | 374.450 | -8.97% | +0.53% | -9.50% | MISS | IN_CI | L106,L107 |
| LIN | 2026-06-18 | 512.150 | 2026-07-16 | 520.740 | +1.68% | +0.53% | +1.14% | HIT | IN_CI | L128,L129 |

## 3. Theme-Level Performance

- Baseline equity forecasts: `6/14` HIT and `10/14` IN_CI. Its vintage rank IC is `-0.0637` (L337,L369).
- Baseline core ETFs: `1/3` direction HIT and `2/3` IN_CI. This supports interval calibration more than directional conviction (L338,L369).
- Technical leadership remains useful as a monitor, but cannot be treated as multi-family confirmation; Fund_Z/Sent_Z are still SHADOW and Macro_Z is unavailable.

## 4. Regime Shift Assessment

The baseline called `BULL`. Today is `NEUTRAL` (L368): SPY has a mixed 20d/50d alignment and a fresh daily bearish MACD cross, while QQQ and SOXX have negative 20d momentum but positive 60d momentum. Completed 30d volatility rose for all three core ETFs. This is a loss of short-horizon breadth, not a fabricated `BEAR` call; factor weights remain unchanged.

## 5. Carry-Forward Decisions

| Ticker/Theme | Prior Score | Prior Thesis | MoM Return | Decision | Rationale | Ledger Rows |
| --- | --- | --- | --- | --- | --- | --- |
| CAT | 100.00 | Cyclical machinery quality with strong trend and operating leverage. | -11.02% | DROP | Negative realized alpha and absent from today's top 20. | L340,L354 |
| GOOGL | 97.10 | Search/cloud AI monetization with positive earnings evidence. | -3.69% | DROP | Negative realized alpha and absent from today's top 20. | L341,L355 |
| GS | 94.10 | Capital-markets leverage and positive momentum. | -0.10% | DROP | Negative realized alpha and absent from today's top 20. | L342,L356 |
| GE | 91.20 | Aerospace quality and strong earnings surprise history. | -3.33% | DROP | Negative realized alpha and absent from today's top 20. | L343,L357 |
| LLY | 88.20 | GLP-1/obesity leadership with resilient relative strength. | +6.43% | DOWNGRADE | Positive alpha, but no longer in today's top 20. | L344,L358 |
| FCX | 85.30 | Copper beta and cyclical leverage in a pro-risk tape. | -14.74% | DROP | Negative realized alpha and absent from today's top 20. | L345,L359 |
| BAC | 82.40 | Rate/credit-sensitive financial rebound with low realized sigma. | +9.41% | CARRY | Still in today's top grounded monitor sleeve. | L346,L360 |
| UNH | 79.40 | Managed-care rebound with defensive beta. | +5.59% | DOWNGRADE | Positive alpha, but no longer in today's top 20. | L347,L361 |
| JPM | 76.50 | Large-bank quality with balanced credit and capital-markets exposure. | +5.51% | DOWNGRADE | Positive alpha, but no longer in today's top 20. | L348,L362 |
| CVX | 73.50 | Energy major quality but negative market beta in the sampled window. | +5.89% | DOWNGRADE | Positive alpha, but no longer in today's top 20. | L349,L363 |
| EQIX | 70.60 | Data-center REIT demand with rate sensitivity. | -7.60% | DROP | Negative realized alpha and absent from today's top 20. | L350,L364 |
| ETN | 67.60 | Electrification exposure with high beta and cyclical sensitivity. | -6.05% | DROP | Negative realized alpha and absent from today's top 20. | L351,L365 |
| AVGO | 64.70 | AI networking/custom silicon strength balanced by high beta. | -8.97% | DROP | Negative realized alpha and absent from today's top 20. | L352,L366 |
| LIN | 61.80 | Industrial-gas quality with lower beta. | +1.68% | DOWNGRADE | Positive alpha, but no longer in today's top 20. | L353,L367 |

## 6. Sign-Off

All prices are `HISTORICAL` exact-date closes from two current-run sources, with 2026-07-17 targets settled at the completed 2026-07-16 close under `TARGET_EQ_RUN_DATE`. Reflection confidence is `HIGH` for settlement arithmetic and `MEDIUM` for regime interpretation. The structural issue is non-positive rank IC, not missing settlement data.
