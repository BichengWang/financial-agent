# 05 Factor Scores

## Calibration Inputs

Rolling calibration metrics are `INSUFFICIENT_SETTLED_N`, so no sigma or mu-table mutation is active. `mu` is assigned strictly from the calibration table by sampled percentile. `sigma` is `REALIZED_VOL_30D` from fetched daily returns. Missing enhancing feeds cap confidence at `MEDIUM`.

## Ranked Candidate Table

| Rank | Ticker | Company | Entry Price | Price Date | Price Tag | Adj Score | Pctl | Beta | 30d RVol | Days to Earnings | mu | sigma | Sigma Source | Target Price | Target Date | 70% CI Lo | 70% CI Hi | Ledger Rows | Confidence | Primary Thesis | Key Risk |
|---:|---|---|---:|---|---|---:|---|---:|---:|---:|---:|---:|---|---:|---|---:|---:|---|---|---|---|
| 1 | AMD | Advanced Micro Devices | 544.67 | 2026-06-15 | DELAYED | 100.0 | SAMPLED_PCTL (n=42) 100.0 | 3.275 | 27.01% | 50 | +6.0% | 27.0% | REALIZED_VOL_30D | 577.35 | 2026-07-13 | 424.34 | 730.36 | L033,L034,L035,L036,L037 | LOW | AI compute catch-up and strong price momentum. | excess beta and high volatility |
| 2 | GOOGL | Alphabet | 371.08 | 2026-06-15 | DELAYED | 97.6 | SAMPLED_PCTL (n=42) 97.6 | 1.519 | 8.46% | 44 | +6.0% | 8.5% | REALIZED_VOL_30D | 393.34 | 2026-07-13 | 360.69 | 426.00 | L048,L049,L050,L051,L052 | LOW | Search/cloud AI monetization with ad-cycle sensitivity. | beta/correlation or earnings risk |
| 3 | CAT | Caterpillar | 936.27 | 2026-06-15 | DELAYED | 95.1 | SAMPLED_PCTL (n=42) 95.1 | 1.850 | 12.52% | 45 | +6.0% | 12.5% | REALIZED_VOL_30D | 992.45 | 2026-07-13 | 870.50 | 1114.40 | L153,L154,L155,L156,L157 | MEDIUM | Cyclical quality with high operating leverage. | beta/correlation or earnings risk |
| 4 | GE | GE Aerospace | 344.38 | 2026-06-15 | DELAYED | 92.7 | SAMPLED_PCTL (n=42) 92.7 | 1.591 | 11.50% | 36 | +5.0% | 11.5% | REALIZED_VOL_30D | 361.60 | 2026-07-13 | 320.40 | 402.80 | L158,L159,L160,L161,L162 | MEDIUM | Aerospace quality with strong earnings surprise history. | beta/correlation or earnings risk |
| 5 | FCX | Freeport-McMoRan | 70.13 | 2026-06-15 | DELAYED | 90.2 | SAMPLED_PCTL (n=42) 90.2 | 2.612 | 16.46% | 38 | +5.0% | 16.5% | REALIZED_VOL_30D | 73.64 | 2026-07-13 | 61.63 | 85.64 | L183,L184,L185,L186,L187 | MEDIUM | Copper beta and cyclical leverage. | excess beta and high volatility |
| 6 | LLY | Eli Lilly | 1129.51 | 2026-06-15 | DELAYED | 87.8 | SAMPLED_PCTL (n=42) 87.8 | 0.678 | 8.95% | 45 | +4.0% | 9.0% | REALIZED_VOL_30D | 1174.69 | 2026-07-13 | 1069.53 | 1279.85 | L133,L134,L135,L136,L137 | MEDIUM | GLP-1/obesity leadership with positive earnings evidence. | beta/correlation or earnings risk |
| 7 | UNH | UnitedHealth | 413.07 | 2026-06-15 | DELAYED | 85.4 | SAMPLED_PCTL (n=42) 85.4 | 0.263 | 7.52% | 36 | +4.0% | 7.5% | REALIZED_VOL_30D | 429.60 | 2026-07-13 | 397.27 | 461.92 | L138,L139,L140,L141,L142 | MEDIUM | Managed-care rebound and defensive beta. | beta/correlation or earnings risk |
| 8 | BAC | Bank of America | 56.03 | 2026-06-15 | DELAYED | 82.9 | SAMPLED_PCTL (n=42) 82.9 | 0.606 | 6.45% | 30 | +3.0% | 6.5% | REALIZED_VOL_30D | 57.71 | 2026-07-13 | 53.95 | 61.47 | L113,L114,L115,L116,L117 | MEDIUM | Rate/credit-sensitive rebound with low realized sigma. | beta/correlation or earnings risk |
| 9 | GS | Goldman Sachs | 1079.29 | 2026-06-15 | DELAYED | 80.5 | SAMPLED_PCTL (n=42) 80.5 | 1.579 | 10.40% | 28 | +3.0% | 10.4% | REALIZED_VOL_30D | 1111.67 | 2026-07-13 | 994.98 | 1228.36 | L118,L119,L120,L121,L122 | MEDIUM | Capital-markets leverage and positive momentum. | beta/correlation or earnings risk |
| 10 | JPM | JPMorgan Chase | 320.65 | 2026-06-15 | DELAYED | 78.0 | SAMPLED_PCTL (n=42) 78.0 | 0.702 | 6.66% | 29 | +2.0% | 6.7% | REALIZED_VOL_30D | 327.06 | 2026-07-13 | 304.84 | 349.29 | L108,L109,L110,L111,L112 | LOW | Large-bank quality and balanced financial beta. | beta/correlation or earnings risk |
| 11 | ANET | Arista Networks | 167.12 | 2026-06-15 | DELAYED | 75.6 | SAMPLED_PCTL (n=42) 75.6 | 1.915 | 19.37% | 50 | +2.0% | 19.4% | REALIZED_VOL_30D | 170.46 | 2026-07-13 | 136.80 | 204.12 | L043,L044,L045,L046,L047 | LOW | AI networking demand and strong trend confirmation. | beta/correlation or earnings risk |
| 12 | SHW | Sherwin-Williams | 320.57 | 2026-06-15 | DELAYED | 73.2 | SAMPLED_PCTL (n=42) 73.2 | 1.037 | 8.73% | 43 | +2.0% | 8.7% | REALIZED_VOL_30D | 326.99 | 2026-07-13 | 297.88 | 356.10 | L178,L179,L180,L181,L182 | LOW | Housing/materials quality; rate sensitivity. | beta/correlation or earnings risk |
| 13 | PLD | Prologis | 148.69 | 2026-06-15 | DELAYED | 70.7 | SAMPLED_PCTL (n=42) 70.7 | 0.653 | 6.07% | 31 | +2.0% | 6.1% | REALIZED_VOL_30D | 151.66 | 2026-07-13 | 142.27 | 161.05 | L188,L189,L190,L191,L192 | LOW | Logistics real estate and rate sensitivity. | beta/correlation or earnings risk |
| 14 | ETN | Eaton | 410.98 | 2026-06-15 | DELAYED | 68.3 | SAMPLED_PCTL (n=42) 68.3 | 1.749 | 14.20% | 50 | +1.0% | 14.2% | REALIZED_VOL_30D | 415.09 | 2026-07-13 | 354.38 | 475.80 | L163,L164,L165,L166,L167 | LOW | Electrification exposure; high beta risk. | beta/correlation or earnings risk |
| 15 | LIN | Linde | 525.54 | 2026-06-15 | DELAYED | 65.9 | SAMPLED_PCTL (n=42) 65.9 | 0.054 | 6.07% | 46 | +1.0% | 6.1% | REALIZED_VOL_30D | 530.80 | 2026-07-13 | 497.59 | 564.00 | L173,L174,L175,L176,L177 | LOW | Quality materials/industrial gas defensiveness. | beta/correlation or earnings risk |
| 16 | CVX | Chevron | 181.22 | 2026-06-15 | DELAYED | 63.4 | SAMPLED_PCTL (n=42) 63.4 | -0.935 | 7.81% | 46 | +1.0% | 7.8% | REALIZED_VOL_30D | 183.04 | 2026-07-13 | 168.33 | 197.75 | L098,L099,L100,L101,L102 | LOW | Energy balance-sheet quality; oil-beta risk. | beta/correlation or earnings risk |
| 17 | ABBV | AbbVie | 222.43 | 2026-06-15 | DELAYED | 61.0 | SAMPLED_PCTL (n=42) 61.0 | -0.012 | 6.21% | 44 | +1.0% | 6.2% | REALIZED_VOL_30D | 224.65 | 2026-07-13 | 210.28 | 239.02 | L148,L149,L150,L151,L152 | LOW | Defensive pharma trend and pipeline optionality. | beta/correlation or earnings risk |
| 18 | HON | Honeywell | 230.11 | 2026-06-15 | DELAYED | 58.5 | SAMPLED_PCTL (n=42) 58.5 | 1.253 | 11.19% | 38 | N/A | 11.2% | REALIZED_VOL_30D | N/A | N/A | N/A | N/A | L168,L169,L170,L171,L172 | LOW | Industrial quality; mixed trend risk. | beta/correlation or earnings risk |
| 19 | HD | Home Depot | 329.80 | 2026-06-15 | DELAYED | 56.1 | SAMPLED_PCTL (n=42) 56.1 | 0.863 | 7.70% | 64 | N/A | 7.7% | REALIZED_VOL_30D | N/A | N/A | N/A | N/A | L073,L074,L075,L076,L077 | LOW | Housing repair/rebound signal with moderate beta. | beta/correlation or earnings risk |
| 20 | JNJ | Johnson & Johnson | 236.44 | 2026-06-15 | DELAYED | 53.7 | SAMPLED_PCTL (n=42) 53.7 | -0.010 | 5.83% | 29 | N/A | 5.8% | REALIZED_VOL_30D | N/A | N/A | N/A | N/A | L143,L144,L145,L146,L147 | LOW | Low-vol defensive health care. | beta/correlation or earnings risk |

## Investable Subset

Investable-grade names meeting percentile, family-support, and data-completeness thresholds: CAT, GE, FCX, LLY, UNH, BAC, GS.

## Monitoring Sleeve

Monitor names with settleable forecasts: AMD, GOOGL, JPM, ANET, SHW, PLD, ETN, LIN, CVX, ABBV.

## Near-Miss Notes

- AMD: monitor-only; pctl 100.0, support 2/4, beta 3.275.
- GOOGL: monitor-only; pctl 97.6, support 1/4, beta 1.519.
- JPM: monitor-only; pctl 78.0, support 3/4, beta 0.702.
- ANET: monitor-only; pctl 75.6, support 4/4, beta 1.915.
- SHW: monitor-only; pctl 73.2, support 2/4, beta 1.037.
- PLD: monitor-only; pctl 70.7, support 3/4, beta 0.653.
- ETN: monitor-only; pctl 68.3, support 3/4, beta 1.749.
- LIN: monitor-only; pctl 65.9, support 2/4, beta 0.054.

## Hallucination Prevention Checklist

- [x] Every numeric entry price has `price_date` and `price_tag`.
- [x] Every numeric metric cites Source Ledger rows.
- [x] `target_price = entry_price x (1 + mu)`.
- [x] Every sigma has source `REALIZED_VOL_30D`.
- [x] No investable name has `price_tag = UNAVAILABLE`.
- [x] `mu` and `sigma` derive from the prompt architecture.
- [x] No live-sounding wording is used without a ledger row.
