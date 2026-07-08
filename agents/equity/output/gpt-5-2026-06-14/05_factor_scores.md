# 05 Factor Scores

## Calibration Inputs

Rolling calibration metrics are `INSUFFICIENT_SETTLED_N`, so no sigma or mu-table mutation is active. `mu` is assigned strictly from the calibration table by sampled percentile. `sigma` is `REALIZED_VOL_30D` from fetched daily returns.

## Ranked Candidate Table

| Rank | Ticker | Company | Entry Price | Price Date | Price Tag | Adj Score | Pctl | Beta | 30d RVol | Days to Earnings | mu | sigma | Sigma Source | Target Price | Target Date | 70% CI Lo | 70% CI Hi | Ledger Rows | Confidence | Primary Thesis | Key Risk |
|---:|---|---|---:|---|---|---:|---|---:|---:|---:|---:|---:|---|---:|---|---:|---:|---|---|---|---|
| 1 | AMD | Advanced Micro Devices | 511.57 | 2026-06-12 | DELAYED | 100.0 | SAMPLED_PCTL (n=42) 100.0 | 3.301 | 26.67% | 51 | 6.0% | 26.7% | REALIZED_VOL_30D | 542.26 | 2026-07-12 | 400.37 | 684.16 | L033,L034,L035,L036,L037,L223 | LOW | INFERRED technical and regime signal. | beta/correlation or earnings risk |
| 2 | LLY | Eli Lilly | 1133.00 | 2026-06-12 | DELAYED | 97.6 | SAMPLED_PCTL (n=42) 97.6 | 0.729 | 9.15% | 46 | 6.0% | 9.2% | REALIZED_VOL_30D | 1200.98 | 2026-07-12 | 1093.16 | 1308.80 | L133,L134,L135,L136,L137,L224 | MEDIUM | GLP-1/obesity leadership plus positive 20d momentum; key risk is valuation compression. | beta/correlation or earnings risk |
| 3 | GE | GE Aerospace | 335.30 | 2026-06-12 | DELAYED | 95.1 | SAMPLED_PCTL (n=42) 95.1 | 1.633 | 11.46% | 37 | 6.0% | 11.5% | REALIZED_VOL_30D | 355.42 | 2026-07-12 | 315.46 | 395.38 | L158,L159,L160,L161,L162,L225 | MEDIUM | Aerospace/industrial quality with strong 20d trend; key risk is cyclical reversal. | beta/correlation or earnings risk |
| 4 | BAC | Bank of America | 56.02 | 2026-06-12 | DELAYED | 92.7 | SAMPLED_PCTL (n=42) 92.7 | 0.622 | 6.44% | 31 | 5.0% | 6.4% | REALIZED_VOL_30D | 58.82 | 2026-07-12 | 55.07 | 62.57 | L113,L114,L115,L116,L117,L226 | MEDIUM | Financial rebound with low realized sigma; key risk is rate/credit sensitivity. | beta/correlation or earnings risk |
| 5 | GS | Goldman Sachs | 1062.75 | 2026-06-12 | DELAYED | 90.2 | SAMPLED_PCTL (n=42) 90.2 | 1.642 | 10.43% | 29 | 5.0% | 10.4% | REALIZED_VOL_30D | 1115.89 | 2026-07-12 | 1000.61 | 1231.17 | L118,L119,L120,L121,L122,L227 | MEDIUM | Capital-markets leverage and strong 60d momentum; key risk is high beta. | beta/correlation or earnings risk |
| 6 | ANET | Arista Networks | 163.24 | 2026-06-12 | DELAYED | 87.8 | SAMPLED_PCTL (n=42) 87.8 | 1.951 | 19.26% | 51 | 4.0% | 19.3% | REALIZED_VOL_30D | 169.77 | 2026-07-12 | 137.07 | 202.47 | L043,L044,L045,L046,L047,L228 | MEDIUM | AI-networking momentum with high beta; key risk is volatility and capex unwind. | beta/correlation or earnings risk |
| 7 | UNH | UnitedHealth | 408.52 | 2026-06-12 | DELAYED | 85.4 | SAMPLED_PCTL (n=42) 85.4 | 0.271 | 7.53% | 37 | 4.0% | 7.5% | REALIZED_VOL_30D | 424.86 | 2026-07-12 | 392.87 | 456.85 | L138,L139,L140,L141,L142,L229 | MEDIUM | Health-care rebound and defensive beta; key risk is policy/headline pressure. | beta/correlation or earnings risk |
| 8 | ABBV | AbbVie | 227.73 | 2026-06-12 | DELAYED | 82.9 | SAMPLED_PCTL (n=42) 82.9 | 0.075 | 6.18% | 45 | 3.0% | 6.2% | REALIZED_VOL_30D | 234.56 | 2026-07-12 | 219.93 | 249.20 | L148,L149,L150,L151,L152,L230 | MEDIUM | Defensive health-care trend with low beta; key risk is pipeline or estimate reset. | beta/correlation or earnings risk |
| 9 | JPM | JPMorgan Chase | 320.72 | 2026-06-12 | DELAYED | 80.5 | SAMPLED_PCTL (n=42) 80.5 | 0.750 | 6.67% | 30 | 3.0% | 6.7% | REALIZED_VOL_30D | 330.34 | 2026-07-12 | 308.09 | 352.59 | L108,L109,L110,L111,L112,L231 | MEDIUM | Large-bank quality with balanced beta; key risk is credit-spread widening. | beta/correlation or earnings risk |
| 10 | AMT | American Tower | 187.18 | 2026-06-12 | DELAYED | 78.0 | SAMPLED_PCTL (n=42) 78.0 | 0.145 | 8.63% | 44 | 2.0% | 8.6% | REALIZED_VOL_30D | 190.92 | 2026-07-12 | 174.12 | 207.72 | L193,L194,L195,L196,L197,L232 | LOW | Real-estate recovery signal; key risk is rate sensitivity. | beta/correlation or earnings risk |
| 11 | HD | Home Depot | 328.39 | 2026-06-12 | DELAYED | 75.6 | SAMPLED_PCTL (n=42) 75.6 | 0.900 | 7.76% | 65 | 2.0% | 7.8% | REALIZED_VOL_30D | 334.96 | 2026-07-12 | 308.46 | 361.46 | L073,L074,L075,L076,L077,L233 | LOW | Consumer discretionary repair with acceptable beta; key risk is housing demand. | beta/correlation or earnings risk |
| 12 | CAT | Caterpillar | 910.57 | 2026-06-12 | DELAYED | 73.2 | SAMPLED_PCTL (n=42) 73.2 | 1.893 | 12.32% | 46 | 2.0% | 12.3% | REALIZED_VOL_30D | 928.78 | 2026-07-12 | 812.11 | 1045.45 | L153,L154,L155,L156,L157,L234 | LOW | Industrial/cyclical quality but percentile below investable bar; key risk is beta and late-cycle demand. | beta/correlation or earnings risk |
| 13 | PLD | Prologis | 148.74 | 2026-06-12 | DELAYED | 70.7 | SAMPLED_PCTL (n=42) 70.7 | 0.689 | 6.09% | 32 | 2.0% | 6.1% | REALIZED_VOL_30D | 151.71 | 2026-07-12 | 142.29 | 161.14 | L188,L189,L190,L191,L192,L235 | LOW | Real-estate momentum off low-vol base; key risk is rates. | beta/correlation or earnings risk |
| 14 | FCX | Freeport-McMoRan | 68.41 | 2026-06-12 | DELAYED | 68.3 | SAMPLED_PCTL (n=42) 68.3 | 2.725 | 16.57% | 39 | 1.0% | 16.6% | REALIZED_VOL_30D | 69.09 | 2026-07-12 | 57.31 | 80.88 | L183,L184,L185,L186,L187,L236 | LOW | Copper beta and strong 60d trend; key risk is excessive beta. | beta/correlation or earnings risk |
| 15 | JNJ | Johnson & Johnson | 240.87 | 2026-06-12 | DELAYED | 65.9 | SAMPLED_PCTL (n=42) 65.9 | 0.042 | 5.56% | 30 | 1.0% | 5.6% | REALIZED_VOL_30D | 243.28 | 2026-07-12 | 229.35 | 257.21 | L143,L144,L145,L146,L147,L237 | LOW | Low-vol defensive support; key risk is low alpha intensity. | beta/correlation or earnings risk |
| 16 | PG | Procter & Gamble | 149.61 | 2026-06-12 | DELAYED | 63.4 | SAMPLED_PCTL (n=42) 63.4 | 0.114 | 7.03% | 40 | 1.0% | 7.0% | REALIZED_VOL_30D | 151.11 | 2026-07-12 | 140.17 | 162.04 | L088,L089,L090,L091,L092,L238 | LOW | Staples defensiveness; key risk is weak upside. | beta/correlation or earnings risk |
| 17 | LIN | Linde | 523.57 | 2026-06-12 | DELAYED | 61.0 | SAMPLED_PCTL (n=42) 61.0 | 0.048 | 6.16% | 47 | 1.0% | 6.2% | REALIZED_VOL_30D | 528.81 | 2026-07-12 | 495.26 | 562.35 | L173,L174,L175,L176,L177,L239 | LOW | Quality materials name; key risk is low momentum. | beta/correlation or earnings risk |
| 18 | SHW | Sherwin-Williams | 317.30 | 2026-06-12 | DELAYED | 58.5 | SAMPLED_PCTL (n=42) 58.5 | 1.065 | 8.74% | 44 | N/A | 8.7% | REALIZED_VOL_30D | N/A | N/A | N/A | N/A | L178,L179,L180,L181,L182,None | LOW | INFERRED technical and regime signal. | beta/correlation or earnings risk |
| 19 | AAPL | Apple | 291.13 | 2026-06-12 | DELAYED | 56.1 | SAMPLED_PCTL (n=42) 56.1 | 0.730 | 7.02% | 46 | N/A | 7.0% | REALIZED_VOL_30D | N/A | N/A | N/A | N/A | L013,L014,L015,L016,L017,None | LOW | INFERRED technical and regime signal. | beta/correlation or earnings risk |
| 20 | V | Visa | 322.39 | 2026-06-12 | DELAYED | 53.7 | SAMPLED_PCTL (n=42) 53.7 | 0.142 | 5.48% | 44 | N/A | 5.5% | REALIZED_VOL_30D | N/A | N/A | N/A | N/A | L123,L124,L125,L126,L127,None | LOW | INFERRED technical and regime signal. | beta/correlation or earnings risk |

## Investable Subset

Investable-grade names meeting percentile, family-support, and data-completeness thresholds: LLY, GE, BAC, GS, ANET, UNH, ABBV, JPM.

## Monitoring Sleeve

Monitor names with settleable forecasts: AMD (high-percentile near-miss; 2/4 family support), AMT, HD, CAT, PLD, FCX, JNJ, PG, LIN.

## Near-Miss Notes

- AMD ranks first by raw momentum but has only 2/4 supportive factor families and beta 3.301, so it is monitor-only despite receiving a settleable forecast record.
- CAT and FCX have useful cyclical signals but fall below the 80th sampled percentile and remain monitor/near-miss only.
- Low-beta defensives help drawdown but reduce capped NAV beta, which becomes binding in portfolio construction.

## Hallucination Prevention Checklist

- [x] Every numeric entry price has `price_date` and `price_tag`.
- [x] Every numeric metric cites Source Ledger rows.
- [x] `target_price = entry_price x (1 + mu)`.
- [x] Every sigma has source `REALIZED_VOL_30D`.
- [x] No investable name has `price_tag = UNAVAILABLE`.
- [x] `mu` and `sigma` derive from the prompt architecture.
- [x] No live-sounding wording is used without a ledger row.
