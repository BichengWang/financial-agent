# 04 Universe Summary

## Construction Method

No full U.S. equity screening feed is wired, so the run uses the Sampled Universe Protocol: current carry-forward names plus 2-3 large liquid names from each GICS sector and theme-watchlist names with sourceable histories. Percentiles are labeled `SAMPLED_PCTL (n=35)`.

## Inclusion / Exclusion Log

All 35 sampled equities passed the price, listing/liquidity proxy, 60-day history, sigma, and earnings-cadence checks. No sampled name was excluded for missing Required input. Core ETFs SPY, QQQ, and SOXX are isolated in the market-forecast sleeve and do not count toward universe percentiles.

## Eligible Universe

| Ticker | Company | Sector | Entry | 20d Ret | 60d Ret | 30d RVol | Beta | Next Earnings | 20d ADV $mm | Ledger Rows |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| AAPL | Apple | Information Technology | 295.95 | -1.01% | +17.68% | 6.36% | 0.736 | 2026-07-30 EST (+/-5d) | 15275.1 | L013,L014,L015,L016,L017,L018 |
| MSFT | Microsoft | Information Technology | 378.91 | -9.23% | -1.07% | 9.85% | 0.876 | 2026-07-29 EST (+/-5d) | 15599.0 | L019,L020,L021,L022,L023,L024 |
| NVDA | NVIDIA | Information Technology | 204.65 | -7.23% | +16.52% | 13.12% | 1.866 | 2026-08-19 EST (+/-5d) | 36705.6 | L025,L026,L027,L028,L029,L030 |
| AVGO | Broadcom | Information Technology | 392.90 | -4.42% | +21.83% | 18.21% | 2.035 | 2026-09-02 EST (+/-5d) | 13881.1 | L031,L032,L033,L034,L035,L036 |
| NOW | ServiceNow | Information Technology | 95.48 | -6.24% | -13.94% | 23.53% | 0.878 | 2026-07-22 EST (+/-5d) | 3617.0 | L037,L038,L039,L040,L041,L042 |
| GOOGL | Alphabet | Communication Services | 363.79 | -6.16% | +20.44% | 8.53% | 1.533 | 2026-07-29 EST (+/-5d) | 11873.7 | L043,L044,L045,L046,L047,L048 |
| META | Meta Platforms | Communication Services | 567.58 | -5.81% | -6.04% | 10.88% | 1.753 | 2026-07-29 EST (+/-5d) | 10970.1 | L049,L050,L051,L052,L053,L054 |
| NFLX | Netflix | Communication Services | 76.96 | -13.85% | -17.58% | 6.82% | 0.180 | 2026-07-16 EST (+/-5d) | 2989.6 | L055,L056,L057,L058,L059,L060 |
| AMZN | Amazon.com | Consumer Discretionary | 237.50 | -8.42% | +13.02% | 8.08% | 1.375 | 2026-07-29 EST (+/-5d) | 10658.0 | L061,L062,L063,L064,L065,L066 |
| TSLA | Tesla | Consumer Discretionary | 396.38 | -1.91% | +4.08% | 13.81% | 1.839 | 2026-07-22 EST (+/-5d) | 19072.8 | L067,L068,L069,L070,L071,L072 |
| HD | Home Depot | Consumer Discretionary | 327.48 | +8.28% | -1.03% | 7.66% | 0.804 | 2026-08-18 EST (+/-5d) | 1569.7 | L073,L074,L075,L076,L077,L078 |
| COST | Costco | Consumer Staples | 965.59 | -11.76% | -0.01% | 7.20% | -0.184 | 2026-08-27 EST (+/-5d) | 2394.0 | L079,L080,L081,L082,L083,L084 |
| PG | Procter & Gamble | Consumer Staples | 150.56 | +6.55% | +4.56% | 6.79% | 0.113 | 2026-07-24 EST (+/-5d) | 1225.7 | L085,L086,L087,L088,L089,L090 |
| KO | Coca-Cola | Consumer Staples | 79.93 | -2.43% | +6.42% | 6.24% | -0.415 | 2026-07-28 EST (+/-5d) | 1328.7 | L091,L092,L093,L094,L095,L096 |
| XOM | Exxon Mobil | Energy | 140.74 | -13.42% | -12.65% | 9.40% | -1.092 | 2026-07-31 EST (+/-5d) | 2449.5 | L097,L098,L099,L100,L101,L102 |
| CVX | Chevron | Energy | 177.58 | -9.97% | -13.46% | 7.94% | -0.959 | 2026-07-31 EST (+/-5d) | 1672.8 | L103,L104,L105,L106,L107,L108 |
| COP | ConocoPhillips | Energy | 111.21 | -11.11% | -12.56% | 9.21% | -1.135 | 2026-07-30 EST (+/-5d) | 803.8 | L109,L110,L111,L112,L113,L114 |
| JPM | JPMorgan Chase | Financials | 333.46 | +12.77% | +15.02% | 7.17% | 0.608 | 2026-07-14 EST (+/-5d) | 2830.9 | L115,L116,L117,L118,L119,L120 |
| BAC | Bank of America | Financials | 56.53 | +11.50% | +18.96% | 6.22% | 0.610 | 2026-07-15 EST (+/-5d) | 2047.5 | L121,L122,L123,L124,L125,L126 |
| GS | Goldman Sachs | Financials | 1099.14 | +18.35% | +32.22% | 10.08% | 1.570 | 2026-07-13 EST (+/-5d) | 2441.9 | L127,L128,L129,L130,L131,L132 |
| LLY | Eli Lilly | Health Care | 1112.00 | +8.87% | +22.12% | 8.97% | 0.691 | 2026-07-30 EST (+/-5d) | 3536.4 | L133,L134,L135,L136,L137,L138 |
| UNH | UnitedHealth | Health Care | 399.53 | +2.64% | +48.23% | 7.60% | 0.309 | 2026-07-21 EST (+/-5d) | 2685.9 | L139,L140,L141,L142,L143,L144 |
| JNJ | Johnson & Johnson | Health Care | 234.20 | +1.83% | -0.52% | 5.79% | -0.039 | 2026-07-14 EST (+/-5d) | 1727.5 | L145,L146,L147,L148,L149,L150 |
| CAT | Caterpillar | Industrials | 955.92 | +11.13% | +36.23% | 12.14% | 1.774 | 2026-07-30 EST (+/-5d) | 2483.9 | L151,L152,L153,L154,L155,L156 |
| GE | GE Aerospace | Industrials | 357.03 | +25.15% | +22.46% | 11.27% | 1.462 | 2026-07-21 EST (+/-5d) | 1543.4 | L157,L158,L159,L160,L161,L162 |
| ETN | Eaton | Industrials | 409.64 | +10.15% | +13.87% | 13.77% | 1.716 | 2026-08-04 EST (+/-5d) | 968.0 | L163,L164,L165,L166,L167,L168 |
| LIN | Linde | Materials | 515.85 | +1.93% | +7.91% | 5.50% | 0.077 | 2026-07-31 EST (+/-5d) | 1235.9 | L169,L170,L171,L172,L173,L174 |
| SHW | Sherwin-Williams | Materials | 313.80 | +4.93% | -0.05% | 8.79% | 0.997 | 2026-07-28 EST (+/-5d) | 695.3 | L175,L176,L177,L178,L179,L180 |
| FCX | Freeport-McMoRan | Materials | 69.06 | +17.65% | +25.70% | 16.24% | 2.555 | 2026-07-23 EST (+/-5d) | 850.2 | L181,L182,L183,L184,L185,L186 |
| PLD | Prologis | Real Estate | 140.94 | -1.05% | +8.16% | 6.71% | 0.681 | 2026-07-16 EST (+/-5d) | 532.3 | L187,L188,L189,L190,L191,L192 |
| AMT | American Tower | Real Estate | 181.09 | -1.04% | +2.60% | 8.76% | 0.068 | 2026-07-28 EST (+/-5d) | 565.0 | L193,L194,L195,L196,L197,L198 |
| EQIX | Equinix | Real Estate | 1088.52 | +3.82% | +12.57% | 5.61% | 0.487 | 2026-07-29 EST (+/-5d) | 607.3 | L199,L200,L201,L202,L203,L204 |
| NEE | NextEra Energy | Utilities | 85.73 | -4.81% | -4.99% | 7.41% | 0.020 | 2026-07-23 EST (+/-5d) | 1030.8 | L205,L206,L207,L208,L209,L210 |
| SO | Southern Company | Utilities | 92.53 | -1.71% | -1.30% | 5.69% | -0.171 | 2026-07-30 EST (+/-5d) | 533.9 | L211,L212,L213,L214,L215,L216 |
| DUK | Duke Energy | Utilities | 123.73 | -0.67% | -2.83% | 5.49% | -0.239 | 2026-08-04 EST (+/-5d) | 390.0 | L217,L218,L219,L220,L221,L222 |

## Metric Coverage Summary

| Metric Group | Sourceable Count | UNAVAILABLE Count | DQ / Confidence Effect | Notes |
| --- | --- | --- | --- | --- |
| Entry price cross-check | 35 | 0 | No DQ penalty | CNBC close agrees with Yahoo close within 1% |
| 60d price history | 35 | 0 | No DQ penalty | Yahoo chart histories used for returns, beta, drawdown, TD-9 |
| Sigma fallback | 35 | 0 | No DQ penalty | REALIZED_VOL_30D available for every sampled name |
| Earnings cadence | 35 | 0 | Event-risk penalty where applicable | Nasdaq prior report +91d estimate |
| Enhancing feeds | 0 | 35 | Confidence capped at MEDIUM | Options, short interest, bid-ask, analyst revisions, institutional flow unavailable |
