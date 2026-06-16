# 04 Universe Summary

## Construction Rule

No full U.S. equity screening feed is wired, so the Sampled Universe Protocol is used. The sample starts with MoM carry-forward names from `investments/equity/output/claude-opus-4-7-2026-05-24`, adds large liquid names from each of the 11 GICS sectors, and preserves current theme-watchlist names with ledger-backed prices and histories. Percentiles are labeled `SAMPLED_PCTL (n=35)`.

## Inclusion / Exclusion Log

| Ticker | Company | Sector | Entry | 30d RVol | Beta | 20d ADV $mm | Next Earnings | Decision | Ledger Rows |
|---|---|---|---|---|---|---|---|---|---|
| AAPL | Apple | Information Technology | 297.94 | 6.7% | 0.738 | 15197.8 | 2026-07-30 EST (+/-5d) | INCLUDED | L013,L014,L015,L016,L017,L018 |
| MSFT | Microsoft | Information Technology | 393.55 | 9.3% | 0.785 | 15578.0 | 2026-07-29 EST (+/-5d) | INCLUDED | L019,L020,L021,L022,L023,L024 |
| NVDA | NVIDIA | Information Technology | 209.59 | 12.9% | 1.872 | 37373.0 | 2026-08-19 EST (+/-5d) | INCLUDED | L025,L026,L027,L028,L029,L030 |
| AVGO | Broadcom | Information Technology | 383.71 | 17.6% | 2.157 | 13470.2 | 2026-09-02 EST (+/-5d) | INCLUDED | L031,L032,L033,L034,L035,L036 |
| NOW | ServiceNow | Information Technology | 101.85 | 22.8% | 0.766 | 3945.0 | 2026-07-22 EST (+/-5d) | INCLUDED | L037,L038,L039,L040,L041,L042 |
| GOOGL | Alphabet | Communication Services | 374.82 | 8.3% | 1.500 | 12269.5 | 2026-07-29 EST (+/-5d) | INCLUDED | L043,L044,L045,L046,L047,L048 |
| META | Meta Platforms | Communication Services | 597.70 | 9.9% | 1.663 | 10841.7 | 2026-07-29 EST (+/-5d) | INCLUDED | L049,L050,L051,L052,L053,L054 |
| NFLX | Netflix | Communication Services | 78.67 | 6.6% | 0.091 | 2855.9 | 2026-07-16 EST (+/-5d) | INCLUDED | L055,L056,L057,L058,L059,L060 |
| AMZN | Amazon | Consumer Discretionary | 249.41 | 7.8% | 1.319 | 10692.2 | 2026-07-29 EST (+/-5d) | INCLUDED | L061,L062,L063,L064,L065,L066 |
| TSLA | Tesla | Consumer Discretionary | 408.37 | 13.6% | 1.861 | 19462.2 | 2026-07-22 EST (+/-5d) | INCLUDED | L067,L068,L069,L070,L071,L072 |
| HD | Home Depot | Consumer Discretionary | 335.64 | 7.7% | 0.868 | 1631.8 | 2026-08-18 EST (+/-5d) | INCLUDED | L073,L074,L075,L076,L077,L078 |
| COST | Costco | Consumer Staples | 986.41 | 7.0% | -0.228 | 2513.3 | 2026-08-27 EST (+/-5d) | INCLUDED | L079,L080,L081,L082,L083,L084 |
| WMT | Walmart | Consumer Staples | 121.63 | 8.6% | 0.118 | 3186.3 | 2026-08-20 EST (+/-5d) | INCLUDED | L085,L086,L087,L088,L089,L090 |
| PG | Procter & Gamble | Consumer Staples | 151.77 | 7.0% | 0.104 | 1234.7 | 2026-07-24 EST (+/-5d) | INCLUDED | L091,L092,L093,L094,L095,L096 |
| XOM | Exxon Mobil | Energy | 140.98 | 9.4% | -1.082 | 2531.4 | 2026-07-31 EST (+/-5d) | INCLUDED | L097,L098,L099,L100,L101,L102 |
| CVX | Chevron | Energy | 179.41 | 7.9% | -0.949 | 1751.7 | 2026-07-31 EST (+/-5d) | INCLUDED | L103,L104,L105,L106,L107,L108 |
| COP | ConocoPhillips | Energy | 110.51 | 9.3% | -1.141 | 794.0 | 2026-07-30 EST (+/-5d) | INCLUDED | L109,L110,L111,L112,L113,L114 |
| JPM | JPMorgan Chase | Financials | 329.20 | 6.7% | 0.700 | 2676.6 | 2026-07-14 EST (+/-5d) | INCLUDED | L115,L116,L117,L118,L119,L120 |
| BAC | Bank of America | Financials | 56.70 | 6.5% | 0.599 | 2035.6 | 2026-07-15 EST (+/-5d) | INCLUDED | L121,L122,L123,L124,L125,L126 |
| GS | Goldman Sachs | Financials | 1093.58 | 10.4% | 1.575 | 2388.7 | 2026-07-13 EST (+/-5d) | INCLUDED | L127,L128,L129,L130,L131,L132 |
| LLY | Eli Lilly | Health Care | 1124.32 | 9.0% | 0.678 | 3571.5 | 2026-07-30 EST (+/-5d) | INCLUDED | L133,L134,L135,L136,L137,L138 |
| UNH | UnitedHealth | Health Care | 408.65 | 7.5% | 0.223 | 2733.9 | 2026-07-21 EST (+/-5d) | INCLUDED | L139,L140,L141,L142,L143,L144 |
| JNJ | Johnson & Johnson | Health Care | 232.57 | 5.9% | -0.018 | 1765.4 | 2026-07-14 EST (+/-5d) | INCLUDED | L145,L146,L147,L148,L149,L150 |
| CAT | Caterpillar | Industrials | 952.35 | 12.5% | 1.835 | 2499.8 | 2026-07-30 EST (+/-5d) | INCLUDED | L151,L152,L153,L154,L155,L156 |
| GE | GE Aerospace | Industrials | 348.80 | 11.4% | 1.586 | 1527.9 | 2026-07-21 EST (+/-5d) | INCLUDED | L157,L158,L159,L160,L161,L162 |
| ETN | Eaton | Industrials | 411.75 | 14.0% | 1.714 | 995.4 | 2026-08-04 EST (+/-5d) | INCLUDED | L163,L164,L165,L166,L167,L168 |
| LIN | Linde | Materials | 514.33 | 6.1% | 0.039 | 1220.1 | 2026-07-31 EST (+/-5d) | INCLUDED | L169,L170,L171,L172,L173,L174 |
| SHW | Sherwin-Williams | Materials | 321.95 | 8.7% | 1.037 | 685.4 | 2026-07-28 EST (+/-5d) | INCLUDED | L175,L176,L177,L178,L179,L180 |
| FCX | Freeport-McMoRan | Materials | 70.34 | 16.5% | 2.613 | 843.7 | 2026-07-23 EST (+/-5d) | INCLUDED | L181,L182,L183,L184,L185,L186 |
| PLD | Prologis | Real Estate | 145.93 | 6.1% | 0.654 | 524.0 | 2026-07-16 EST (+/-5d) | INCLUDED | L187,L188,L189,L190,L191,L192 |
| AMT | American Tower | Real Estate | 185.18 | 8.7% | 0.127 | 593.6 | 2026-07-28 EST (+/-5d) | INCLUDED | L193,L194,L195,L196,L197,L198 |
| EQIX | Equinix | Real Estate | 1098.68 | 5.0% | 0.568 | 590.9 | 2026-07-29 EST (+/-5d) | INCLUDED | L199,L200,L201,L202,L203,L204 |
| NEE | NextEra Energy | Utilities | 86.83 | 7.5% | 0.132 | 1238.9 | 2026-07-23 EST (+/-5d) | INCLUDED | L205,L206,L207,L208,L209,L210 |
| SO | Southern Company | Utilities | 94.69 | 5.5% | -0.098 | 546.4 | 2026-07-30 EST (+/-5d) | INCLUDED | L211,L212,L213,L214,L215,L216 |
| CEG | Constellation Energy | Utilities | 270.13 | 15.0% | 1.296 | 1114.4 | 2026-08-10 EST (+/-5d) | INCLUDED | L217,L218,L219,L220,L221,L222 |

## Metric Coverage Summary

| Metric Group | Sourceable Count | UNAVAILABLE Count | DQ / Confidence Effect | Notes |
|---|---|---|---|---|
| Entry price | 35 | 0 | Required input PASS | Nasdaq/Yahoo cross-check <= 1% |
| 60d history | 35 | 0 | Required input PASS | Nasdaq daily historical rows sufficient for beta/correlation/drawdown |
| Sigma | 35 | 0 | Required input PASS | REALIZED_VOL_30D for every sampled equity |
| Next earnings date | 35 | 0 | Required input PASS | Nasdaq prior report date + 91d cadence estimate |
| Liquidity | 35 | 0 | Universe filter PASS | 20d average dollar volume derived from fetched close x volume |
| Options/short/bid-ask/analyst revisions | 0 | 35 | Confidence capped at MEDIUM | Enhancing only; not used as GO blockers |
