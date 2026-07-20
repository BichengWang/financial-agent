# 01 Preflight — Source Ledger (2026-07-20, claude-fable-5)

Generated programmatically at 2026-07-20T16:43:48Z from run-computed JSONs; retrieval timestamps per fetch manifests (price_history_fetch_manifest.json, nasdaq_verification_manifest.json, earnings_calendar_manifest.json). Basis: Monday intraday run (12:21 ET) — entry/settlement basis is the last completed close (Fri 2026-07-17). No same-day intraday prints are used for scoring or settlement.

| row | artifact | field | ticker/entity | value | unit | observation_date | source | freshness_tag | claim_type | used_by |
|---|---|---|---|---|---|---|---|---|---|---|
| L001 | 00 | run_date/basis | run | 2026-07-20 intraday 12:21 ET; entry basis 2026-07-17 close | - | 2026-07-20 | scheduler fire time | LIVE | OBSERVED | 00,02,03 |
| L002 | 00 | data_mode | run | DELAYED (prior-session official closes fetched this run) | - | 2026-07-17 | Nasdaq historical bulk + IBKR verification | DELAYED | OBSERVED | 00,03 |
| L003 | 04 | universe | S&P500∪NDX100 | 515 union (503+101, 89 overlap); caches fetched_at 2026-06-21 | tickers | 2026-07-20 | build_index_universe.py; universe_summary.json | HISTORICAL | OBSERVED | 03,04,05 |
| L004 | 04 | eligible_n | universe | 514 after filters (FDXF excluded: 36 bars) | tickers | 2026-07-17 | compute_analytics (price>$5, ADV20>$20M, ≥60 bars) | DELAYED | DERIVED | 04,05 |
| L005 | 01 | price_history | 518 symbols | 5y daily bars, 518/519 ok, all last_date 2026-07-17 | bars | 2026-07-17 | api.nasdaq.com historical bulk (8-worker); BF-B via IBKR conid 4931 | DELAYED | OBSERVED | all |
| L006 | 03 | VIX close | ^VIX | 18.77 | index | 2026-07-17 | cdn.cboe.com VIX_History.csv | DELAYED | OBSERVED | 03,09 |
| L007 | 03 | rf 13w | T-bill | 3.71% annual | % | 2026-07-17 | home.treasury.gov daily bill rates (FRED timeout fallback) | DELAYED | OBSERVED | 05 ratios |
| L008 | 03 | breadth | universe | 63.4% above MA50 | % | 2026-07-17 | technical_indicators.json | DELAYED | DERIVED | 03 |
| L009 | 03 | event_concentration | shortlist | 12 of 34 checked names inside buffered 14d window | names | 2026-07-20 | api.nasdaq.com/api/analyst/{sym}/earnings-date (2 passes) | DELAYED | OBSERVED | 03,07,08 |
| L010 | 03 | regime | market | NEUTRAL with HIGH_VOL watch (SPY below MA20/MA50, VIX 18.77<20, breadth 63.4%, defensive leadership) | - | 2026-07-17 | rows L006,L008 + ETF rows below | DELAYED | INFERRED | 03,05,09 |
| L011 | 05 | DQ multiplier | all | 0.80 (notable coverage gaps: Fund/Sent families unwired) | - | 2026-07-20 | rules.md guideposts | DELAYED | DERIVED | 05 |
| L012 | 05 | family availability | all | Fund_Z UNAVAILABLE, Sent_Z UNAVAILABLE (no fetch path; SHADOW not promoted); Tech_Z, Macro_Z sourceable | - | 2026-07-20 | rules.md §SHADOW | UNAVAILABLE | OBSERVED | 05,07,08 |
| L013 | 03 | SPY mu prior | SPY | +0.50% (NEUTRAL regime prior, unadjusted) | % | 2026-07-20 | rules.md Core ETF mu table | DELAYED | DERIVED | 03,15 |
| L014 | 03 | close | SPY | 743.29 | USD | 2026-07-17 | Nasdaq historical (etf) + IBKR snapshot last-change verification | DELAYED | OBSERVED | 02,03,05,09,15 |
| L015 | 03 | trend/vol/beta/dd | SPY | ma20 745.02, ma50 744.38, rvol30(1m) 4.54% (prior 2.76%), beta 1.000, dd60 -2.14% | - | 2026-07-17 | technical_indicators.json + 60d regression vs SPY (row L005) | DELAYED | DERIVED | 03,09,15 |
| L016 | 03 | close | QQQ | 695.33 | USD | 2026-07-17 | Nasdaq historical (etf) + IBKR snapshot last-change verification | DELAYED | OBSERVED | 02,03,05,09,15 |
| L017 | 03 | trend/vol/beta/dd | QQQ | ma20 718.35, ma50 719.01, rvol30(1m) 8.87% (prior 4.45%), beta 1.733, dd60 -6.81% | - | 2026-07-17 | technical_indicators.json + 60d regression vs SPY (row L005) | DELAYED | DERIVED | 03,09,15 |
| L018 | 03 | close | SOXX | 521.81 | USD | 2026-07-17 | Nasdaq historical (etf) + IBKR snapshot last-change verification | DELAYED | OBSERVED | 02,03,05,09,15 |
| L019 | 03 | trend/vol/beta/dd | SOXX | ma20 586.15, ma50 566.37, rvol30(1m) 22.04% (prior 13.34%), beta 3.710, dd60 -20.34% | - | 2026-07-17 | technical_indicators.json + 60d regression vs SPY (row L005) | DELAYED | DERIVED | 03,09,15 |
| L020 | 03 | RS ratios | QQQ,SOXX vs SPY | {'QQQ/SPY_20d': -4.06, 'QQQ/SPY_60d': 2.22, 'SOXX/SPY_20d': -13.27, 'SOXX/SPY_60d': 17.49} | % | 2026-07-17 | price ratios from row L005 | DELAYED | DERIVED | 03,09 |
| L021 | 02 | settle close | AVGO | 370.825 | USD | 2026-07-17 | Nasdaq historical; IBKR cross 370.83 (div 0.001%) | DELAYED | OBSERVED | 02,15 settlements |
| L022 | 02 | settle close | BAC | 61.27 | USD | 2026-07-17 | Nasdaq historical; IBKR cross 61.27 (div 0.000%) | DELAYED | OBSERVED | 02,15 settlements |
| L023 | 02 | settle close | CAT | 880.28 | USD | 2026-07-17 | Nasdaq historical; IBKR cross 878.65 (div 0.185%) | DELAYED | OBSERVED | 02,15 settlements |
| L024 | 02 | settle close | CVX | 187.38 | USD | 2026-07-17 | Nasdaq historical; IBKR cross 187.38 (div 0.000%) | DELAYED | OBSERVED | 02,15 settlements |
| L025 | 02 | settle close | EQIX | 1020.0 | USD | 2026-07-17 | Nasdaq historical; IBKR cross 1020.0 (div 0.000%) | DELAYED | OBSERVED | 02,15 settlements |
| L026 | 02 | settle close | ETN | 399.99 | USD | 2026-07-17 | Nasdaq historical; IBKR cross 399.99 (div 0.000%) | DELAYED | OBSERVED | 02,15 settlements |
| L027 | 02 | settle close | FCX | 58.38 | USD | 2026-07-17 | Nasdaq historical; IBKR cross 58.38 (div 0.000%) | DELAYED | OBSERVED | 02,15 settlements |
| L028 | 02 | settle close | GE | 348.83 | USD | 2026-07-17 | Nasdaq historical; IBKR cross 348.83 (div 0.000%) | DELAYED | OBSERVED | 02,15 settlements |
| L029 | 02 | settle close | GOOGL | 346.77 | USD | 2026-07-17 | Nasdaq historical; IBKR cross 346.77 (div 0.000%) | DELAYED | OBSERVED | 02,15 settlements |
| L030 | 02 | settle close | GS | 1065.22 | USD | 2026-07-17 | Nasdaq historical; IBKR cross 1065.22 (div 0.000%) | DELAYED | OBSERVED | 02,15 settlements |
| L031 | 02 | settle close | JPM | 341.1 | USD | 2026-07-17 | Nasdaq historical; IBKR cross 341.1 (div 0.000%) | DELAYED | OBSERVED | 02,15 settlements |
| L032 | 02 | settle close | LIN | 513.22 | USD | 2026-07-17 | Nasdaq historical; IBKR cross 513.22 (div 0.000%) | DELAYED | OBSERVED | 02,15 settlements |
| L033 | 02 | settle close | LLY | 1179.11 | USD | 2026-07-17 | Nasdaq historical; IBKR cross 1179.11 (div 0.000%) | DELAYED | OBSERVED | 02,15 settlements |
| L034 | 02 | settle close | QQQ | 695.33 | USD | 2026-07-17 | Nasdaq historical; IBKR cross 695.33 (div 0.000%) | DELAYED | OBSERVED | 02,15 settlements |
| L035 | 02 | settle close | SOXX | 521.81 | USD | 2026-07-17 | Nasdaq historical; IBKR cross 521.81 (div 0.000%) | DELAYED | OBSERVED | 02,15 settlements |
| L036 | 02 | settle close | SPY | 743.29 | USD | 2026-07-17 | Nasdaq historical; IBKR cross 743.29 (div 0.000%) | DELAYED | OBSERVED | 02,15 settlements |
| L037 | 02 | settle close | UNH | 426.09 | USD | 2026-07-17 | Nasdaq historical; IBKR cross 426.09 (div 0.000%) | DELAYED | OBSERVED | 02,15 settlements |
| L038 | 02 | settle close | AVGO | 370.825 | USD | 2026-07-17 | Nasdaq historical; IBKR cross 370.83 (div 0.001%) | DELAYED | OBSERVED | 02,15 settlements |
| L039 | 02 | settle close | BAC | 61.27 | USD | 2026-07-17 | Nasdaq historical; IBKR cross 61.27 (div 0.000%) | DELAYED | OBSERVED | 02,15 settlements |
| L040 | 02 | settle close | CAT | 880.28 | USD | 2026-07-17 | Nasdaq historical; IBKR cross 878.65 (div 0.185%) | DELAYED | OBSERVED | 02,15 settlements |
| L041 | 02 | settle close | CVX | 187.38 | USD | 2026-07-17 | Nasdaq historical; IBKR cross 187.38 (div 0.000%) | DELAYED | OBSERVED | 02,15 settlements |
| L042 | 02 | settle close | EQIX | 1020.0 | USD | 2026-07-17 | Nasdaq historical; IBKR cross 1020.0 (div 0.000%) | DELAYED | OBSERVED | 02,15 settlements |
| L043 | 02 | settle close | ETN | 399.99 | USD | 2026-07-17 | Nasdaq historical; IBKR cross 399.99 (div 0.000%) | DELAYED | OBSERVED | 02,15 settlements |
| L044 | 02 | settle close | FCX | 58.38 | USD | 2026-07-17 | Nasdaq historical; IBKR cross 58.38 (div 0.000%) | DELAYED | OBSERVED | 02,15 settlements |
| L045 | 02 | settle close | GE | 348.83 | USD | 2026-07-17 | Nasdaq historical; IBKR cross 348.83 (div 0.000%) | DELAYED | OBSERVED | 02,15 settlements |
| L046 | 02 | settle close | GOOGL | 346.77 | USD | 2026-07-17 | Nasdaq historical; IBKR cross 346.77 (div 0.000%) | DELAYED | OBSERVED | 02,15 settlements |
| L047 | 02 | settle close | GS | 1065.22 | USD | 2026-07-17 | Nasdaq historical; IBKR cross 1065.22 (div 0.000%) | DELAYED | OBSERVED | 02,15 settlements |
| L048 | 02 | settle close | JPM | 341.1 | USD | 2026-07-17 | Nasdaq historical; IBKR cross 341.1 (div 0.000%) | DELAYED | OBSERVED | 02,15 settlements |
| L049 | 02 | settle close | LIN | 513.22 | USD | 2026-07-17 | Nasdaq historical; IBKR cross 513.22 (div 0.000%) | DELAYED | OBSERVED | 02,15 settlements |
| L050 | 02 | settle close | LLY | 1179.11 | USD | 2026-07-17 | Nasdaq historical; IBKR cross 1179.11 (div 0.000%) | DELAYED | OBSERVED | 02,15 settlements |
| L051 | 02 | settle close | QQQ | 695.33 | USD | 2026-07-17 | Nasdaq historical; IBKR cross 695.33 (div 0.000%) | DELAYED | OBSERVED | 02,15 settlements |
| L052 | 02 | settle close | SOXX | 521.81 | USD | 2026-07-17 | Nasdaq historical; IBKR cross 521.81 (div 0.000%) | DELAYED | OBSERVED | 02,15 settlements |
| L053 | 02 | settle close | SPY | 743.29 | USD | 2026-07-17 | Nasdaq historical; IBKR cross 743.29 (div 0.000%) | DELAYED | OBSERVED | 02,15 settlements |
| L054 | 02 | settle close | UNH | 426.09 | USD | 2026-07-17 | Nasdaq historical; IBKR cross 426.09 (div 0.000%) | DELAYED | OBSERVED | 02,15 settlements |
| L055 | 02 | settle close | AVGO | 370.825 | USD | 2026-07-17 | Nasdaq historical; IBKR cross 370.83 (div 0.001%) | DELAYED | OBSERVED | 02,15 settlements |
| L056 | 02 | settle close | BAC | 61.27 | USD | 2026-07-17 | Nasdaq historical; IBKR cross 61.27 (div 0.000%) | DELAYED | OBSERVED | 02,15 settlements |
| L057 | 02 | settle close | CAT | 880.28 | USD | 2026-07-17 | Nasdaq historical; IBKR cross 878.65 (div 0.185%) | DELAYED | OBSERVED | 02,15 settlements |
| L058 | 02 | settle close | CVX | 187.38 | USD | 2026-07-17 | Nasdaq historical; IBKR cross 187.38 (div 0.000%) | DELAYED | OBSERVED | 02,15 settlements |
| L059 | 02 | settle close | EQIX | 1020.0 | USD | 2026-07-17 | Nasdaq historical; IBKR cross 1020.0 (div 0.000%) | DELAYED | OBSERVED | 02,15 settlements |
| L060 | 02 | settle close | ETN | 399.99 | USD | 2026-07-17 | Nasdaq historical; IBKR cross 399.99 (div 0.000%) | DELAYED | OBSERVED | 02,15 settlements |
| L061 | 02 | settle close | FCX | 58.38 | USD | 2026-07-17 | Nasdaq historical; IBKR cross 58.38 (div 0.000%) | DELAYED | OBSERVED | 02,15 settlements |
| L062 | 02 | settle close | GE | 348.83 | USD | 2026-07-17 | Nasdaq historical; IBKR cross 348.83 (div 0.000%) | DELAYED | OBSERVED | 02,15 settlements |
| L063 | 02 | settle close | GOOGL | 346.77 | USD | 2026-07-17 | Nasdaq historical; IBKR cross 346.77 (div 0.000%) | DELAYED | OBSERVED | 02,15 settlements |
| L064 | 02 | settle close | GS | 1065.22 | USD | 2026-07-17 | Nasdaq historical; IBKR cross 1065.22 (div 0.000%) | DELAYED | OBSERVED | 02,15 settlements |
| L065 | 02 | settle close | JPM | 341.1 | USD | 2026-07-17 | Nasdaq historical; IBKR cross 341.1 (div 0.000%) | DELAYED | OBSERVED | 02,15 settlements |
| L066 | 02 | settle close | LIN | 513.22 | USD | 2026-07-17 | Nasdaq historical; IBKR cross 513.22 (div 0.000%) | DELAYED | OBSERVED | 02,15 settlements |
| L067 | 02 | settle close | LLY | 1179.11 | USD | 2026-07-17 | Nasdaq historical; IBKR cross 1179.11 (div 0.000%) | DELAYED | OBSERVED | 02,15 settlements |
| L068 | 02 | settle close | QQQ | 695.33 | USD | 2026-07-17 | Nasdaq historical; IBKR cross 695.33 (div 0.000%) | DELAYED | OBSERVED | 02,15 settlements |
| L069 | 02 | settle close | SOXX | 521.81 | USD | 2026-07-17 | Nasdaq historical; IBKR cross 521.81 (div 0.000%) | DELAYED | OBSERVED | 02,15 settlements |
| L070 | 02 | settle close | SPY | 743.29 | USD | 2026-07-17 | Nasdaq historical; IBKR cross 743.29 (div 0.000%) | DELAYED | OBSERVED | 02,15 settlements |
| L071 | 02 | settle close | UNH | 426.09 | USD | 2026-07-17 | Nasdaq historical; IBKR cross 426.09 (div 0.000%) | DELAYED | OBSERVED | 02,15 settlements |
| L072 | 02 | settle close | AVGO | 370.825 | USD | 2026-07-17 | Nasdaq historical; IBKR cross 370.83 (div 0.001%) | DELAYED | OBSERVED | 02,15 settlements |
| L073 | 02 | settle close | BAC | 61.27 | USD | 2026-07-17 | Nasdaq historical; IBKR cross 61.27 (div 0.000%) | DELAYED | OBSERVED | 02,15 settlements |
| L074 | 02 | settle close | CAT | 880.28 | USD | 2026-07-17 | Nasdaq historical; IBKR cross 878.65 (div 0.185%) | DELAYED | OBSERVED | 02,15 settlements |
| L075 | 02 | settle close | CVX | 187.38 | USD | 2026-07-17 | Nasdaq historical; IBKR cross 187.38 (div 0.000%) | DELAYED | OBSERVED | 02,15 settlements |
| L076 | 02 | settle close | EQIX | 1020.0 | USD | 2026-07-17 | Nasdaq historical; IBKR cross 1020.0 (div 0.000%) | DELAYED | OBSERVED | 02,15 settlements |
| L077 | 02 | settle close | ETN | 399.99 | USD | 2026-07-17 | Nasdaq historical; IBKR cross 399.99 (div 0.000%) | DELAYED | OBSERVED | 02,15 settlements |
| L078 | 02 | settle close | FCX | 58.38 | USD | 2026-07-17 | Nasdaq historical; IBKR cross 58.38 (div 0.000%) | DELAYED | OBSERVED | 02,15 settlements |
| L079 | 02 | settle close | GE | 348.83 | USD | 2026-07-17 | Nasdaq historical; IBKR cross 348.83 (div 0.000%) | DELAYED | OBSERVED | 02,15 settlements |
| L080 | 02 | settle close | GOOGL | 346.77 | USD | 2026-07-17 | Nasdaq historical; IBKR cross 346.77 (div 0.000%) | DELAYED | OBSERVED | 02,15 settlements |
| L081 | 02 | settle close | GS | 1065.22 | USD | 2026-07-17 | Nasdaq historical; IBKR cross 1065.22 (div 0.000%) | DELAYED | OBSERVED | 02,15 settlements |
| L082 | 02 | settle close | JPM | 341.1 | USD | 2026-07-17 | Nasdaq historical; IBKR cross 341.1 (div 0.000%) | DELAYED | OBSERVED | 02,15 settlements |
| L083 | 02 | settle close | LIN | 513.22 | USD | 2026-07-17 | Nasdaq historical; IBKR cross 513.22 (div 0.000%) | DELAYED | OBSERVED | 02,15 settlements |
| L084 | 02 | settle close | LLY | 1179.11 | USD | 2026-07-17 | Nasdaq historical; IBKR cross 1179.11 (div 0.000%) | DELAYED | OBSERVED | 02,15 settlements |
| L085 | 02 | settle close | QQQ | 695.33 | USD | 2026-07-17 | Nasdaq historical; IBKR cross 695.33 (div 0.000%) | DELAYED | OBSERVED | 02,15 settlements |
| L086 | 02 | settle close | SOXX | 521.81 | USD | 2026-07-17 | Nasdaq historical; IBKR cross 521.81 (div 0.000%) | DELAYED | OBSERVED | 02,15 settlements |
| L087 | 02 | settle close | SPY | 743.29 | USD | 2026-07-17 | Nasdaq historical; IBKR cross 743.29 (div 0.000%) | DELAYED | OBSERVED | 02,15 settlements |
| L088 | 02 | settle close | UNH | 426.09 | USD | 2026-07-17 | Nasdaq historical; IBKR cross 426.09 (div 0.000%) | DELAYED | OBSERVED | 02,15 settlements |
| L089 | 02 | SPY MoM pair | SPY | 725.43 (2026-06-10) -> 743.29 (2026-07-17) | USD | 2026-07-17 | history CSVs row L005 | HISTORICAL | OBSERVED | 02 |
| L090 | 02 | MoM baseline | claude-fable-5-2026-06-10 | BASELINE_WINDOW_GAP (12d off 06-22 target; only same-model folder in 06-05..06-29 window) | - | 2026-07-20 | agents.md baseline algorithm | HISTORICAL | DERIVED | 00,02 |
| L091 | 05 | close | DOC | 22.51 | USD | 2026-07-17 | Nasdaq historical bulk (row L005) | DELAYED | OBSERVED | 05,06,09,15 |
| L092 | 05 | beta60/te | DOC | beta 0.532 | - | 2026-07-17 | 60d daily regression vs SPY | DELAYED | DERIVED | 05,07 |
| L093 | 05 | rvol30 1m sigma | DOC | 7.2% | % | 2026-07-17 | stdev(30d daily returns)*sqrt(21) | DELAYED | DERIVED | 05,15 |
| L094 | 05 | maxDD60/VaR/CVaR | DOC | dd -6.23%, VaR95 -6.9%, CVaR95 -9.8% | % | 2026-07-17 | 60d window; parametric mu-1.65/2.06 sigma (normality assumed) | DELAYED | DERIVED | 05,07 |
| L095 | 05 | technical pack | DOC | TD9 SELL_SETUP_3/SELL_SETUP_4/SELL_SETUP_4; RSI 70.59/68.72/59.02; MACD BULLISH_CROSS/ABOVE_SIGNAL/ABOVE_SIGNAL | - | 2026-07-17 | technical_indicators.json (technical_indicators.py) | DELAYED | DERIVED | 05,06,09 |
| L096 | 05 | next earnings | DOC | 2026-08-04 (15d, confirmed) | date | 2026-07-20 | api.nasdaq.com analyst earnings-date; +91d cadence for vendor-empty post-prints | DELAYED | OBSERVED | 05,08 |
| L097 | 05 | forecast block | DOC | mu +5.0% (band prior +6% - 1pp exhaustion (RSI/TD9 flag)), sigma 7.20% REALIZED_VOL_30D, target 23.64, CI [21.95,25.32] | - | 2026-07-20 | mu Calibration Table band @ pctl 100.0; CI=entry*(1+mu±1.04σ) | DELAYED | DERIVED | 05,09,15 |
| L098 | 05 | close | EXPD | 182.8 | USD | 2026-07-17 | Nasdaq historical bulk (row L005) | DELAYED | OBSERVED | 05,06,09,15 |
| L099 | 05 | beta60/te | EXPD | beta 0.203 | - | 2026-07-17 | 60d daily regression vs SPY | DELAYED | DERIVED | 05,07 |
| L100 | 05 | rvol30 1m sigma | EXPD | 6.15% | % | 2026-07-17 | stdev(30d daily returns)*sqrt(21) | DELAYED | DERIVED | 05,15 |
| L101 | 05 | maxDD60/VaR/CVaR | EXPD | dd -6.7%, VaR95 -5.1%, CVaR95 -7.7% | % | 2026-07-17 | 60d window; parametric mu-1.65/2.06 sigma (normality assumed) | DELAYED | DERIVED | 05,07 |
| L102 | 05 | technical pack | EXPD | TD9 SELL_SETUP_7/SELL_SETUP_9/SELL_SETUP_2; RSI 77.54/72.74/73.18; MACD ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | - | 2026-07-17 | technical_indicators.json (technical_indicators.py) | DELAYED | DERIVED | 05,06,09 |
| L103 | 05 | next earnings | EXPD | 2026-08-04 (15d, confirmed) | date | 2026-07-20 | api.nasdaq.com analyst earnings-date; +91d cadence for vendor-empty post-prints | DELAYED | OBSERVED | 05,08 |
| L104 | 05 | forecast block | EXPD | mu +5.0% (band prior +6% - 1pp exhaustion (RSI/TD9 flag)), sigma 6.15% REALIZED_VOL_30D, target 191.94, CI [180.25,203.63] | - | 2026-07-20 | mu Calibration Table band @ pctl 99.8; CI=entry*(1+mu±1.04σ) | DELAYED | DERIVED | 05,09,15 |
| L105 | 05 | close | RF | 31.65 | USD | 2026-07-17 | Nasdaq historical bulk (row L005) | DELAYED | OBSERVED | 05,06,09,15 |
| L106 | 05 | beta60/te | RF | beta 0.181 | - | 2026-07-17 | 60d daily regression vs SPY | DELAYED | DERIVED | 05,07 |
| L107 | 05 | rvol30 1m sigma | RF | 6.91% | % | 2026-07-17 | stdev(30d daily returns)*sqrt(21) | DELAYED | DERIVED | 05,15 |
| L108 | 05 | maxDD60/VaR/CVaR | RF | dd -6.73%, VaR95 -5.4%, CVaR95 -8.2% | % | 2026-07-17 | 60d window; parametric mu-1.65/2.06 sigma (normality assumed) | DELAYED | DERIVED | 05,07 |
| L109 | 05 | technical pack | RF | TD9 SELL_SETUP_7/SELL_SETUP_7/SELL_SETUP_2; RSI 63.78/67.07/65.3; MACD ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | - | 2026-07-17 | technical_indicators.json (technical_indicators.py) | DELAYED | DERIVED | 05,06,09 |
| L110 | 05 | next earnings | RF | 2026-10-15 (87d, ESTIMATED print-cadence +91d (±5d)) | date | 2026-07-20 | api.nasdaq.com analyst earnings-date; +91d cadence for vendor-empty post-prints | DELAYED | INFERRED | 05,08 |
| L111 | 05 | forecast block | RF | mu +6.0% (band prior +6%), sigma 6.91% REALIZED_VOL_30D, target 33.55, CI [31.28,35.82] | - | 2026-07-20 | mu Calibration Table band @ pctl 99.6; CI=entry*(1+mu±1.04σ) | DELAYED | DERIVED | 05,09,15 |
| L112 | 05 | close | JBHT | 291.41 | USD | 2026-07-17 | Nasdaq historical bulk (row L005) | DELAYED | OBSERVED | 05,06,09,15 |
| L113 | 05 | beta60/te | JBHT | beta 0.571 | - | 2026-07-17 | 60d daily regression vs SPY | DELAYED | DERIVED | 05,07 |
| L114 | 05 | rvol30 1m sigma | JBHT | 10.61% | % | 2026-07-17 | stdev(30d daily returns)*sqrt(21) | DELAYED | DERIVED | 05,15 |
| L115 | 05 | maxDD60/VaR/CVaR | JBHT | dd -7.64%, VaR95 -11.5%, CVaR95 -15.8% | % | 2026-07-17 | 60d window; parametric mu-1.65/2.06 sigma (normality assumed) | DELAYED | DERIVED | 05,07 |
| L116 | 05 | technical pack | JBHT | TD9 SELL_SETUP_2/SELL_SETUP_1/SELL_SETUP_9; RSI 58.3/70.23/73.98; MACD ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | - | 2026-07-17 | technical_indicators.json (technical_indicators.py) | DELAYED | DERIVED | 05,06,09 |
| L117 | 05 | next earnings | JBHT | 2026-10-14 (86d, ESTIMATED print-cadence +91d (±5d)) | date | 2026-07-20 | api.nasdaq.com analyst earnings-date; +91d cadence for vendor-empty post-prints | DELAYED | INFERRED | 05,08 |
| L118 | 05 | forecast block | JBHT | mu +6.0% (band prior +6%), sigma 10.61% REALIZED_VOL_30D, target 308.89, CI [276.75,341.04] | - | 2026-07-20 | mu Calibration Table band @ pctl 99.4; CI=entry*(1+mu±1.04σ) | DELAYED | DERIVED | 05,09,15 |
| L119 | 05 | close | BBY | 85.41 | USD | 2026-07-17 | Nasdaq historical bulk (row L005) | DELAYED | OBSERVED | 05,06,09,15 |
| L120 | 05 | beta60/te | BBY | beta 0.588 | - | 2026-07-17 | 60d daily regression vs SPY | DELAYED | DERIVED | 05,07 |
| L121 | 05 | rvol30 1m sigma | BBY | 8.35% | % | 2026-07-17 | stdev(30d daily returns)*sqrt(21) | DELAYED | DERIVED | 05,15 |
| L122 | 05 | maxDD60/VaR/CVaR | BBY | dd -12.61%, VaR95 -8.8%, CVaR95 -12.2% | % | 2026-07-17 | 60d window; parametric mu-1.65/2.06 sigma (normality assumed) | DELAYED | DERIVED | 05,07 |
| L123 | 05 | technical pack | BBY | TD9 SELL_SETUP_9/SELL_SETUP_3/SELL_SETUP_3; RSI 72.11/64.55/56.08; MACD ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | - | 2026-07-17 | technical_indicators.json (technical_indicators.py) | DELAYED | DERIVED | 05,06,09 |
| L124 | 05 | next earnings | BBY | 2026-08-27 (38d, ESTIMATED (±5d)) | date | 2026-07-20 | api.nasdaq.com analyst earnings-date; +91d cadence for vendor-empty post-prints | DELAYED | INFERRED | 05,08 |
| L125 | 05 | forecast block | BBY | mu +5.0% (band prior +6% - 1pp exhaustion (RSI/TD9 flag)), sigma 8.35% REALIZED_VOL_30D, target 89.68, CI [82.27,97.1] | - | 2026-07-20 | mu Calibration Table band @ pctl 99.2; CI=entry*(1+mu±1.04σ) | DELAYED | DERIVED | 05,09,15 |
| L126 | 05 | close | TRV | 368.98 | USD | 2026-07-17 | Nasdaq historical bulk (row L005) | DELAYED | OBSERVED | 05,06,09,15 |
| L127 | 05 | beta60/te | TRV | beta -0.758 | - | 2026-07-17 | 60d daily regression vs SPY | DELAYED | DERIVED | 05,07 |
| L128 | 05 | rvol30 1m sigma | TRV | 9.7% | % | 2026-07-17 | stdev(30d daily returns)*sqrt(21) | DELAYED | DERIVED | 05,15 |
| L129 | 05 | maxDD60/VaR/CVaR | TRV | dd -6.8%, VaR95 -11.0%, CVaR95 -15.0% | % | 2026-07-17 | 60d window; parametric mu-1.65/2.06 sigma (normality assumed) | DELAYED | DERIVED | 05,07 |
| L130 | 05 | technical pack | TRV | TD9 SELL_SETUP_1/SELL_SETUP_7/SELL_SETUP_4; RSI 75.49/76.07/73.94; MACD BULLISH_CROSS/ABOVE_SIGNAL/ABOVE_SIGNAL | - | 2026-07-17 | technical_indicators.json (technical_indicators.py) | DELAYED | DERIVED | 05,06,09 |
| L131 | 05 | next earnings | TRV | 2026-10-16 (88d, ESTIMATED print-cadence +91d (±5d)) | date | 2026-07-20 | api.nasdaq.com analyst earnings-date; +91d cadence for vendor-empty post-prints | DELAYED | INFERRED | 05,08 |
| L132 | 05 | forecast block | TRV | mu +5.0% (band prior +6% - 1pp exhaustion (RSI/TD9 flag)), sigma 9.70% REALIZED_VOL_30D, target 387.43, CI [350.19,424.67] | - | 2026-07-20 | mu Calibration Table band @ pctl 99.0; CI=entry*(1+mu±1.04σ) | DELAYED | DERIVED | 05,09,15 |
| L133 | 05 | close | PRU | 119.07 | USD | 2026-07-17 | Nasdaq historical bulk (row L005) | DELAYED | OBSERVED | 05,06,09,15 |
| L134 | 05 | beta60/te | PRU | beta 0.154 | - | 2026-07-17 | 60d daily regression vs SPY | DELAYED | DERIVED | 05,07 |
| L135 | 05 | rvol30 1m sigma | PRU | 6.34% | % | 2026-07-17 | stdev(30d daily returns)*sqrt(21) | DELAYED | DERIVED | 05,15 |
| L136 | 05 | maxDD60/VaR/CVaR | PRU | dd -3.6%, VaR95 -5.5%, CVaR95 -8.1% | % | 2026-07-17 | 60d window; parametric mu-1.65/2.06 sigma (normality assumed) | DELAYED | DERIVED | 05,07 |
| L137 | 05 | technical pack | PRU | TD9 SELL_SETUP_9/SELL_SETUP_9/SELL_SETUP_2; RSI 71.32/66.51/58.83; MACD ABOVE_SIGNAL/ABOVE_SIGNAL/BULLISH_CROSS | - | 2026-07-17 | technical_indicators.json (technical_indicators.py) | DELAYED | DERIVED | 05,06,09 |
| L138 | 05 | next earnings | PRU | 2026-08-04 (15d, confirmed) | date | 2026-07-20 | api.nasdaq.com analyst earnings-date; +91d cadence for vendor-empty post-prints | DELAYED | OBSERVED | 05,08 |
| L139 | 05 | forecast block | PRU | mu +5.0% (band prior +6% - 1pp exhaustion (RSI/TD9 flag)), sigma 6.34% REALIZED_VOL_30D, target 125.02, CI [117.17,132.87] | - | 2026-07-20 | mu Calibration Table band @ pctl 98.8; CI=entry*(1+mu±1.04σ) | DELAYED | DERIVED | 05,09,15 |
| L140 | 05 | close | GEN | 26.74 | USD | 2026-07-17 | Nasdaq historical bulk (row L005) | DELAYED | OBSERVED | 05,06,09,15 |
| L141 | 05 | beta60/te | GEN | beta 0.583 | - | 2026-07-17 | 60d daily regression vs SPY | DELAYED | DERIVED | 05,07 |
| L142 | 05 | rvol30 1m sigma | GEN | 10.26% | % | 2026-07-17 | stdev(30d daily returns)*sqrt(21) | DELAYED | DERIVED | 05,15 |
| L143 | 05 | maxDD60/VaR/CVaR | GEN | dd -17.11%, VaR95 -10.9%, CVaR95 -15.1% | % | 2026-07-17 | 60d window; parametric mu-1.65/2.06 sigma (normality assumed) | DELAYED | DERIVED | 05,07 |
| L144 | 05 | technical pack | GEN | TD9 SELL_SETUP_4/SELL_SETUP_3/SELL_SETUP_3; RSI 61.36/59.43/53.56; MACD ABOVE_SIGNAL/ABOVE_SIGNAL/BELOW_SIGNAL | - | 2026-07-17 | technical_indicators.json (technical_indicators.py) | DELAYED | DERIVED | 05,06,09 |
| L145 | 05 | next earnings | GEN | 2026-08-06 (17d, confirmed) | date | 2026-07-20 | api.nasdaq.com analyst earnings-date; +91d cadence for vendor-empty post-prints | DELAYED | OBSERVED | 05,08 |
| L146 | 05 | forecast block | GEN | mu +6.0% (band prior +6%), sigma 10.26% REALIZED_VOL_30D, target 28.34, CI [25.49,31.2] | - | 2026-07-20 | mu Calibration Table band @ pctl 98.6; CI=entry*(1+mu±1.04σ) | DELAYED | DERIVED | 05,09,15 |
| L147 | 05 | close | FITB | 58.01 | USD | 2026-07-17 | Nasdaq historical bulk (row L005) | DELAYED | OBSERVED | 05,06,09,15 |
| L148 | 05 | beta60/te | FITB | beta 0.232 | - | 2026-07-17 | 60d daily regression vs SPY | DELAYED | DERIVED | 05,07 |
| L149 | 05 | rvol30 1m sigma | FITB | 8.0% | % | 2026-07-17 | stdev(30d daily returns)*sqrt(21) | DELAYED | DERIVED | 05,15 |
| L150 | 05 | maxDD60/VaR/CVaR | FITB | dd -7.31%, VaR95 -7.2%, CVaR95 -10.5% | % | 2026-07-17 | 60d window; parametric mu-1.65/2.06 sigma (normality assumed) | DELAYED | DERIVED | 05,07 |
| L151 | 05 | technical pack | FITB | TD9 SELL_SETUP_4/SELL_SETUP_7/SELL_SETUP_2; RSI 61.54/67.16/68.68; MACD BEARISH_CROSS/ABOVE_SIGNAL/ABOVE_SIGNAL | - | 2026-07-17 | technical_indicators.json (technical_indicators.py) | DELAYED | DERIVED | 05,06,09 |
| L152 | 05 | next earnings | FITB | 2026-10-15 (87d, ESTIMATED print-cadence +91d (±5d)) | date | 2026-07-20 | api.nasdaq.com analyst earnings-date; +91d cadence for vendor-empty post-prints | DELAYED | INFERRED | 05,08 |
| L153 | 05 | forecast block | FITB | mu +6.0% (band prior +6%), sigma 8.00% REALIZED_VOL_30D, target 61.49, CI [56.67,66.31] | - | 2026-07-20 | mu Calibration Table band @ pctl 98.4; CI=entry*(1+mu±1.04σ) | DELAYED | DERIVED | 05,09,15 |
| L154 | 05 | close | STT | 182.5 | USD | 2026-07-17 | Nasdaq historical bulk (row L005) | DELAYED | OBSERVED | 05,06,09,15 |
| L155 | 05 | beta60/te | STT | beta 0.691 | - | 2026-07-17 | 60d daily regression vs SPY | DELAYED | DERIVED | 05,07 |
| L156 | 05 | rvol30 1m sigma | STT | 7.37% | % | 2026-07-17 | stdev(30d daily returns)*sqrt(21) | DELAYED | DERIVED | 05,15 |
| L157 | 05 | maxDD60/VaR/CVaR | STT | dd -3.86%, VaR95 -7.2%, CVaR95 -10.2% | % | 2026-07-17 | 60d window; parametric mu-1.65/2.06 sigma (normality assumed) | DELAYED | DERIVED | 05,07 |
| L158 | 05 | technical pack | STT | TD9 SELL_SETUP_4/SELL_SETUP_9/SELL_SETUP_9; RSI 64.62/86.3/86.0; MACD ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | - | 2026-07-17 | technical_indicators.json (technical_indicators.py) | DELAYED | DERIVED | 05,06,09 |
| L159 | 05 | next earnings | STT | 2026-10-15 (87d, ESTIMATED print-cadence +91d (±5d)) | date | 2026-07-20 | api.nasdaq.com analyst earnings-date; +91d cadence for vendor-empty post-prints | DELAYED | INFERRED | 05,08 |
| L160 | 05 | forecast block | STT | mu +5.0% (band prior +6% - 1pp exhaustion (RSI/TD9 flag)), sigma 7.37% REALIZED_VOL_30D, target 191.62, CI [177.63,205.62] | - | 2026-07-20 | mu Calibration Table band @ pctl 98.2; CI=entry*(1+mu±1.04σ) | DELAYED | DERIVED | 05,09,15 |
| L161 | 05 | close | CFG | 72.39 | USD | 2026-07-17 | Nasdaq historical bulk (row L005) | DELAYED | OBSERVED | 05,06,09,15 |
| L162 | 05 | beta60/te | CFG | beta 0.333 | - | 2026-07-17 | 60d daily regression vs SPY | DELAYED | DERIVED | 05,07 |
| L163 | 05 | rvol30 1m sigma | CFG | 8.33% | % | 2026-07-17 | stdev(30d daily returns)*sqrt(21) | DELAYED | DERIVED | 05,15 |
| L164 | 05 | maxDD60/VaR/CVaR | CFG | dd -7.91%, VaR95 -7.7%, CVaR95 -11.2% | % | 2026-07-17 | 60d window; parametric mu-1.65/2.06 sigma (normality assumed) | DELAYED | DERIVED | 05,07 |
| L165 | 05 | technical pack | CFG | TD9 SELL_SETUP_4/SELL_SETUP_7/SELL_SETUP_2; RSI 60.84/69.93/71.92; MACD ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | - | 2026-07-17 | technical_indicators.json (technical_indicators.py) | DELAYED | DERIVED | 05,06,09 |
| L166 | 05 | next earnings | CFG | 2026-10-14 (86d, ESTIMATED print-cadence +91d (±5d)) | date | 2026-07-20 | api.nasdaq.com analyst earnings-date; +91d cadence for vendor-empty post-prints | DELAYED | INFERRED | 05,08 |
| L167 | 05 | forecast block | CFG | mu +6.0% (band prior +6%), sigma 8.33% REALIZED_VOL_30D, target 76.73, CI [70.46,83.01] | - | 2026-07-20 | mu Calibration Table band @ pctl 98.1; CI=entry*(1+mu±1.04σ) | DELAYED | DERIVED | 05,09,15 |
| L168 | 05 | close | PAYX | 114.39 | USD | 2026-07-17 | Nasdaq historical bulk (row L005) | DELAYED | OBSERVED | 05,06,09,15 |
| L169 | 05 | beta60/te | PAYX | beta -0.626 | - | 2026-07-17 | 60d daily regression vs SPY | DELAYED | DERIVED | 05,07 |
| L170 | 05 | rvol30 1m sigma | PAYX | 8.97% | % | 2026-07-17 | stdev(30d daily returns)*sqrt(21) | DELAYED | DERIVED | 05,15 |
| L171 | 05 | maxDD60/VaR/CVaR | PAYX | dd -6.35%, VaR95 -9.8%, CVaR95 -13.5% | % | 2026-07-17 | 60d window; parametric mu-1.65/2.06 sigma (normality assumed) | DELAYED | DERIVED | 05,07 |
| L172 | 05 | technical pack | PAYX | TD9 SELL_SETUP_6/SELL_SETUP_9/SELL_SETUP_2; RSI 71.47/64.31/47.9; MACD ABOVE_SIGNAL/ABOVE_SIGNAL/BELOW_SIGNAL | - | 2026-07-17 | technical_indicators.json (technical_indicators.py) | DELAYED | DERIVED | 05,06,09 |
| L173 | 05 | next earnings | PAYX | 2026-09-23 (65d, ESTIMATED print-cadence +91d (±5d)) | date | 2026-07-20 | api.nasdaq.com analyst earnings-date; +91d cadence for vendor-empty post-prints | DELAYED | INFERRED | 05,08 |
| L174 | 05 | forecast block | PAYX | mu +5.0% (band prior +6% - 1pp exhaustion (RSI/TD9 flag)), sigma 8.97% REALIZED_VOL_30D, target 120.11, CI [109.44,130.78] | - | 2026-07-20 | mu Calibration Table band @ pctl 97.9; CI=entry*(1+mu±1.04σ) | DELAYED | DERIVED | 05,09,15 |
| L175 | 05 | close | MTB | 249.24 | USD | 2026-07-17 | Nasdaq historical bulk (row L005) | DELAYED | OBSERVED | 05,06,09,15 |
| L176 | 05 | beta60/te | MTB | beta 0.177 | - | 2026-07-17 | 60d daily regression vs SPY | DELAYED | DERIVED | 05,07 |
| L177 | 05 | rvol30 1m sigma | MTB | 6.63% | % | 2026-07-17 | stdev(30d daily returns)*sqrt(21) | DELAYED | DERIVED | 05,15 |
| L178 | 05 | maxDD60/VaR/CVaR | MTB | dd -7.11%, VaR95 -4.9%, CVaR95 -7.6% | % | 2026-07-17 | 60d window; parametric mu-1.65/2.06 sigma (normality assumed) | DELAYED | DERIVED | 05,07 |
| L179 | 05 | technical pack | MTB | TD9 SELL_SETUP_6/SELL_SETUP_7/SELL_SETUP_2; RSI 66.17/68.64/68.33; MACD ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | - | 2026-07-17 | technical_indicators.json (technical_indicators.py) | DELAYED | DERIVED | 05,06,09 |
| L180 | 05 | next earnings | MTB | 2026-10-14 (86d, ESTIMATED print-cadence +91d (±5d)) | date | 2026-07-20 | api.nasdaq.com analyst earnings-date; +91d cadence for vendor-empty post-prints | DELAYED | INFERRED | 05,08 |
| L181 | 05 | forecast block | MTB | mu +6.0% (band prior +6%), sigma 6.63% REALIZED_VOL_30D, target 264.19, CI [247.02,281.37] | - | 2026-07-20 | mu Calibration Table band @ pctl 97.7; CI=entry*(1+mu±1.04σ) | DELAYED | DERIVED | 05,09,15 |
| L182 | 05 | close | MPC | 312.6 | USD | 2026-07-17 | Nasdaq historical bulk (row L005) | DELAYED | OBSERVED | 05,06,09,15 |
| L183 | 05 | beta60/te | MPC | beta -0.52 | - | 2026-07-17 | 60d daily regression vs SPY | DELAYED | DERIVED | 05,07 |
| L184 | 05 | rvol30 1m sigma | MPC | 10.17% | % | 2026-07-17 | stdev(30d daily returns)*sqrt(21) | DELAYED | DERIVED | 05,15 |
| L185 | 05 | maxDD60/VaR/CVaR | MPC | dd -9.09%, VaR95 -11.8%, CVaR95 -16.0% | % | 2026-07-17 | 60d window; parametric mu-1.65/2.06 sigma (normality assumed) | DELAYED | DERIVED | 05,07 |
| L186 | 05 | technical pack | MPC | TD9 SELL_SETUP_9/SELL_SETUP_4/SELL_SETUP_6; RSI 77.67/74.53/80.41; MACD ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | - | 2026-07-17 | technical_indicators.json (technical_indicators.py) | DELAYED | DERIVED | 05,06,09 |
| L187 | 05 | next earnings | MPC | 2026-08-04 (15d, confirmed) | date | 2026-07-20 | api.nasdaq.com analyst earnings-date; +91d cadence for vendor-empty post-prints | DELAYED | OBSERVED | 05,08 |
| L188 | 05 | forecast block | MPC | mu +5.0% (band prior +6% - 1pp exhaustion (RSI/TD9 flag)), sigma 10.17% REALIZED_VOL_30D, target 328.23, CI [295.15,361.31] | - | 2026-07-20 | mu Calibration Table band @ pctl 97.5; CI=entry*(1+mu±1.04σ) | DELAYED | DERIVED | 05,09,15 |
| L189 | 05 | close | KHC | 25.88 | USD | 2026-07-17 | Nasdaq historical bulk (row L005) | DELAYED | OBSERVED | 05,06,09,15 |
| L190 | 05 | beta60/te | KHC | beta -0.114 | - | 2026-07-17 | 60d daily regression vs SPY | DELAYED | DERIVED | 05,07 |
| L191 | 05 | rvol30 1m sigma | KHC | 9.67% | % | 2026-07-17 | stdev(30d daily returns)*sqrt(21) | DELAYED | DERIVED | 05,15 |
| L192 | 05 | maxDD60/VaR/CVaR | KHC | dd -9.97%, VaR95 -10.0%, CVaR95 -13.9% | % | 2026-07-17 | 60d window; parametric mu-1.65/2.06 sigma (normality assumed) | DELAYED | DERIVED | 05,07 |
| L193 | 05 | technical pack | KHC | TD9 SELL_SETUP_4/SELL_SETUP_3/SELL_SETUP_1; RSI 62.48/58.1/44.33; MACD ABOVE_SIGNAL/ABOVE_SIGNAL/BULLISH_CROSS | - | 2026-07-17 | technical_indicators.json (technical_indicators.py) | DELAYED | DERIVED | 05,06,09 |
| L194 | 05 | next earnings | KHC | 2026-08-05 (16d, confirmed) | date | 2026-07-20 | api.nasdaq.com analyst earnings-date; +91d cadence for vendor-empty post-prints | DELAYED | OBSERVED | 05,08 |
| L195 | 05 | forecast block | KHC | mu +6.0% (band prior +6%), sigma 9.67% REALIZED_VOL_30D, target 27.43, CI [24.83,30.04] | - | 2026-07-20 | mu Calibration Table band @ pctl 97.3; CI=entry*(1+mu±1.04σ) | DELAYED | DERIVED | 05,09,15 |
| L196 | 05 | close | MET | 94.0 | USD | 2026-07-17 | Nasdaq historical bulk (row L005) | DELAYED | OBSERVED | 05,06,09,15 |
| L197 | 05 | beta60/te | MET | beta -0.028 | - | 2026-07-17 | 60d daily regression vs SPY | DELAYED | DERIVED | 05,07 |
| L198 | 05 | rvol30 1m sigma | MET | 7.3% | % | 2026-07-17 | stdev(30d daily returns)*sqrt(21) | DELAYED | DERIVED | 05,15 |
| L199 | 05 | maxDD60/VaR/CVaR | MET | dd -4.77%, VaR95 -7.0%, CVaR95 -10.0% | % | 2026-07-17 | 60d window; parametric mu-1.65/2.06 sigma (normality assumed) | DELAYED | DERIVED | 05,07 |
| L200 | 05 | technical pack | MET | TD9 SELL_SETUP_9/SELL_SETUP_9/SELL_SETUP_4; RSI 68.75/69.51/64.95; MACD ABOVE_SIGNAL/ABOVE_SIGNAL/BULLISH_CROSS | - | 2026-07-17 | technical_indicators.json (technical_indicators.py) | DELAYED | DERIVED | 05,06,09 |
| L201 | 05 | next earnings | MET | 2026-08-05 (16d, confirmed) | date | 2026-07-20 | api.nasdaq.com analyst earnings-date; +91d cadence for vendor-empty post-prints | DELAYED | OBSERVED | 05,08 |
| L202 | 05 | forecast block | MET | mu +5.0% (band prior +6% - 1pp exhaustion (RSI/TD9 flag)), sigma 7.30% REALIZED_VOL_30D, target 98.7, CI [91.56,105.84] | - | 2026-07-20 | mu Calibration Table band @ pctl 97.1; CI=entry*(1+mu±1.04σ) | DELAYED | DERIVED | 05,09,15 |
| L203 | 05 | close | BAC | 61.27 | USD | 2026-07-17 | Nasdaq historical bulk (row L005) | DELAYED | OBSERVED | 05,06,09,15 |
| L204 | 05 | beta60/te | BAC | beta 0.204 | - | 2026-07-17 | 60d daily regression vs SPY | DELAYED | DERIVED | 05,07 |
| L205 | 05 | rvol30 1m sigma | BAC | 5.92% | % | 2026-07-17 | stdev(30d daily returns)*sqrt(21) | DELAYED | DERIVED | 05,15 |
| L206 | 05 | maxDD60/VaR/CVaR | BAC | dd -7.15%, VaR95 -4.8%, CVaR95 -7.2% | % | 2026-07-17 | 60d window; parametric mu-1.65/2.06 sigma (normality assumed) | DELAYED | DERIVED | 05,07 |
| L207 | 05 | technical pack | BAC | TD9 SELL_SETUP_4/SELL_SETUP_7/SELL_SETUP_2; RSI 70.02/69.31/69.45; MACD ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | - | 2026-07-17 | technical_indicators.json (technical_indicators.py) | DELAYED | DERIVED | 05,06,09 |
| L208 | 05 | next earnings | BAC | 2026-10-14 (86d, ESTIMATED print-cadence +91d (±5d)) | date | 2026-07-20 | api.nasdaq.com analyst earnings-date; +91d cadence for vendor-empty post-prints | DELAYED | INFERRED | 05,08 |
| L209 | 05 | forecast block | BAC | mu +5.0% (band prior +6% - 1pp exhaustion (RSI/TD9 flag)), sigma 5.92% REALIZED_VOL_30D, target 64.33, CI [60.56,68.1] | - | 2026-07-20 | mu Calibration Table band @ pctl 96.9; CI=entry*(1+mu±1.04σ) | DELAYED | DERIVED | 05,09,15 |
| L210 | 05 | close | CTAS | 204.45 | USD | 2026-07-17 | Nasdaq historical bulk (row L005) | DELAYED | OBSERVED | 05,06,09,15 |
| L211 | 05 | beta60/te | CTAS | beta -0.327 | - | 2026-07-17 | 60d daily regression vs SPY | DELAYED | DERIVED | 05,07 |
| L212 | 05 | rvol30 1m sigma | CTAS | 11.21% | % | 2026-07-17 | stdev(30d daily returns)*sqrt(21) | DELAYED | DERIVED | 05,15 |
| L213 | 05 | maxDD60/VaR/CVaR | CTAS | dd -7.92%, VaR95 -13.5%, CVaR95 -18.1% | % | 2026-07-17 | 60d window; parametric mu-1.65/2.06 sigma (normality assumed) | DELAYED | DERIVED | 05,07 |
| L214 | 05 | technical pack | CTAS | TD9 SELL_SETUP_6/SELL_SETUP_4/SELL_SETUP_1; RSI 74.23/64.14/57.36; MACD ABOVE_SIGNAL/ABOVE_SIGNAL/BELOW_SIGNAL | - | 2026-07-17 | technical_indicators.json (technical_indicators.py) | DELAYED | DERIVED | 05,06,09 |
| L215 | 05 | next earnings | CTAS | 2026-10-14 (86d, ESTIMATED print-cadence +91d (±5d)) | date | 2026-07-20 | api.nasdaq.com analyst earnings-date; +91d cadence for vendor-empty post-prints | DELAYED | INFERRED | 05,08 |
| L216 | 05 | forecast block | CTAS | mu +5.0% (band prior +6% - 1pp exhaustion (RSI/TD9 flag)), sigma 11.21% REALIZED_VOL_30D, target 214.67, CI [190.83,238.51] | - | 2026-07-20 | mu Calibration Table band @ pctl 96.7; CI=entry*(1+mu±1.04σ) | DELAYED | DERIVED | 05,09,15 |
| L217 | 05 | close | CSX | 50.75 | USD | 2026-07-17 | Nasdaq historical bulk (row L005) | DELAYED | OBSERVED | 05,06,09,15 |
| L218 | 05 | beta60/te | CSX | beta 0.181 | - | 2026-07-17 | 60d daily regression vs SPY | DELAYED | DERIVED | 05,07 |
| L219 | 05 | rvol30 1m sigma | CSX | 5.81% | % | 2026-07-17 | stdev(30d daily returns)*sqrt(21) | DELAYED | DERIVED | 05,15 |
| L220 | 05 | maxDD60/VaR/CVaR | CSX | dd -4.2%, VaR95 -5.6%, CVaR95 -8.0% | % | 2026-07-17 | 60d window; parametric mu-1.65/2.06 sigma (normality assumed) | DELAYED | DERIVED | 05,07 |
| L221 | 05 | technical pack | CSX | TD9 SELL_SETUP_9/SELL_SETUP_9/SELL_SETUP_8; RSI 70.27/74.6/73.21; MACD ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | - | 2026-07-17 | technical_indicators.json (technical_indicators.py) | DELAYED | DERIVED | 05,06,09 |
| L222 | 05 | next earnings | CSX | 2026-07-22 (2d, confirmed) | date | 2026-07-20 | api.nasdaq.com analyst earnings-date; +91d cadence for vendor-empty post-prints | DELAYED | OBSERVED | 05,08 |
| L223 | 05 | forecast block | CSX | mu +4.0% (band prior +5% - 1pp exhaustion (RSI/TD9 flag)), sigma 5.81% REALIZED_VOL_30D, target 52.78, CI [49.71,55.85] | - | 2026-07-20 | mu Calibration Table band @ pctl 93.6; CI=entry*(1+mu±1.04σ) | DELAYED | DERIVED | 05,09,15 |
| L224 | 05 | close | UNH | 426.09 | USD | 2026-07-17 | Nasdaq historical bulk (row L005) | DELAYED | OBSERVED | 05,06,09,15 |
| L225 | 05 | beta60/te | UNH | beta -0.191 | - | 2026-07-17 | 60d daily regression vs SPY | DELAYED | DERIVED | 05,07 |
| L226 | 05 | rvol30 1m sigma | UNH | 7.83% | % | 2026-07-17 | stdev(30d daily returns)*sqrt(21) | DELAYED | DERIVED | 05,15 |
| L227 | 05 | maxDD60/VaR/CVaR | UNH | dd -6.06%, VaR95 -8.9%, CVaR95 -12.1% | % | 2026-07-17 | 60d window; parametric mu-1.65/2.06 sigma (normality assumed) | DELAYED | DERIVED | 05,07 |
| L228 | 05 | technical pack | UNH | TD9 BUY_SETUP_4/SELL_SETUP_9/SELL_SETUP_4; RSI 57.88/68.45/53.34; MACD BELOW_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | - | 2026-07-17 | technical_indicators.json (technical_indicators.py) | DELAYED | DERIVED | 05,06,09 |
| L229 | 05 | next earnings | UNH | 2026-10-15 (87d, ESTIMATED print-cadence +91d (±5d)) | date | 2026-07-20 | api.nasdaq.com analyst earnings-date; +91d cadence for vendor-empty post-prints | DELAYED | INFERRED | 05,08 |
| L230 | 05 | forecast block | UNH | mu +4.0% (band prior +5% - 1pp exhaustion (RSI/TD9 flag)), sigma 7.83% REALIZED_VOL_30D, target 443.13, CI [408.43,477.84] | - | 2026-07-20 | mu Calibration Table band @ pctl 92.2; CI=entry*(1+mu±1.04σ) | DELAYED | DERIVED | 05,09,15 |
| L231 | 05 | close | UNP | 301.75 | USD | 2026-07-17 | Nasdaq historical bulk (row L005) | DELAYED | OBSERVED | 05,06,09,15 |
| L232 | 05 | beta60/te | UNP | beta -0.167 | - | 2026-07-17 | 60d daily regression vs SPY | DELAYED | DERIVED | 05,07 |
| L233 | 05 | rvol30 1m sigma | UNP | 7.02% | % | 2026-07-17 | stdev(30d daily returns)*sqrt(21) | DELAYED | DERIVED | 05,15 |
| L234 | 05 | maxDD60/VaR/CVaR | UNP | dd -8.06%, VaR95 -7.6%, CVaR95 -10.5% | % | 2026-07-17 | 60d window; parametric mu-1.65/2.06 sigma (normality assumed) | DELAYED | DERIVED | 05,07 |
| L235 | 05 | technical pack | UNP | TD9 SELL_SETUP_9/SELL_SETUP_4/SELL_SETUP_6; RSI 77.34/70.84/65.99; MACD ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | - | 2026-07-17 | technical_indicators.json (technical_indicators.py) | DELAYED | DERIVED | 05,06,09 |
| L236 | 05 | next earnings | UNP | 2026-07-23 (3d, confirmed) | date | 2026-07-20 | api.nasdaq.com analyst earnings-date; +91d cadence for vendor-empty post-prints | DELAYED | OBSERVED | 05,08 |
| L237 | 05 | forecast block | UNP | mu +4.0% (band prior +5% - 1pp exhaustion (RSI/TD9 flag)), sigma 7.02% REALIZED_VOL_30D, target 313.82, CI [291.78,335.86] | - | 2026-07-20 | mu Calibration Table band @ pctl 91.8; CI=entry*(1+mu±1.04σ) | DELAYED | DERIVED | 05,09,15 |
| L238 | 05 | close | MNST | 97.5 | USD | 2026-07-17 | Nasdaq historical bulk (row L005) | DELAYED | OBSERVED | 05,06,09,15 |
| L239 | 05 | beta60/te | MNST | beta 0.365 | - | 2026-07-17 | 60d daily regression vs SPY | DELAYED | DERIVED | 05,07 |
| L240 | 05 | rvol30 1m sigma | MNST | 5.47% | % | 2026-07-17 | stdev(30d daily returns)*sqrt(21) | DELAYED | DERIVED | 05,15 |
| L241 | 05 | maxDD60/VaR/CVaR | MNST | dd -3.87%, VaR95 -5.0%, CVaR95 -7.3% | % | 2026-07-17 | 60d window; parametric mu-1.65/2.06 sigma (normality assumed) | DELAYED | DERIVED | 05,07 |
| L242 | 05 | technical pack | MNST | TD9 SELL_SETUP_6/SELL_SETUP_9/SELL_SETUP_4; RSI 59.02/74.4/72.83; MACD BELOW_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | - | 2026-07-17 | technical_indicators.json (technical_indicators.py) | DELAYED | DERIVED | 05,06,09 |
| L243 | 05 | next earnings | MNST | 2026-08-06 (17d, ESTIMATED (±5d)) | date | 2026-07-20 | api.nasdaq.com analyst earnings-date; +91d cadence for vendor-empty post-prints | DELAYED | INFERRED | 05,08 |
| L244 | 05 | forecast block | MNST | mu +4.0% (band prior +5% - 1pp exhaustion (RSI/TD9 flag)), sigma 5.47% REALIZED_VOL_30D, target 101.4, CI [95.85,106.95] | - | 2026-07-20 | mu Calibration Table band @ pctl 91.0; CI=entry*(1+mu±1.04σ) | DELAYED | DERIVED | 05,09,15 |
| L245 | 05 | close | FRT | 126.02 | USD | 2026-07-17 | Nasdaq historical bulk (row L005) | DELAYED | OBSERVED | 05,06,09,15 |
| L246 | 05 | beta60/te | FRT | beta -0.088 | - | 2026-07-17 | 60d daily regression vs SPY | DELAYED | DERIVED | 05,07 |
| L247 | 05 | rvol30 1m sigma | FRT | 5.51% | % | 2026-07-17 | stdev(30d daily returns)*sqrt(21) | DELAYED | DERIVED | 05,15 |
| L248 | 05 | maxDD60/VaR/CVaR | FRT | dd -4.33%, VaR95 -5.1%, CVaR95 -7.4% | % | 2026-07-17 | 60d window; parametric mu-1.65/2.06 sigma (normality assumed) | DELAYED | DERIVED | 05,07 |
| L249 | 05 | technical pack | FRT | TD9 SELL_SETUP_4/SELL_SETUP_1/SELL_SETUP_6; RSI 63.69/65.99/67.56; MACD BULLISH_CROSS/ABOVE_SIGNAL/ABOVE_SIGNAL | - | 2026-07-17 | technical_indicators.json (technical_indicators.py) | DELAYED | DERIVED | 05,06,09 |
| L250 | 05 | next earnings | FRT | 2026-07-31 (11d, confirmed) | date | 2026-07-20 | api.nasdaq.com analyst earnings-date; +91d cadence for vendor-empty post-prints | DELAYED | OBSERVED | 05,08 |
| L251 | 05 | forecast block | FRT | mu +4.0% (band prior +4%), sigma 5.51% REALIZED_VOL_30D, target 131.06, CI [123.84,138.28] | - | 2026-07-20 | mu Calibration Table band @ pctl 89.5; CI=entry*(1+mu±1.04σ) | DELAYED | DERIVED | 05,09,15 |
| L252 | 05 | close | ADP | 255.265 | USD | 2026-07-17 | Nasdaq historical bulk (row L005) | DELAYED | OBSERVED | 05,06,09,15 |
| L253 | 05 | beta60/te | ADP | beta -0.713 | - | 2026-07-17 | 60d daily regression vs SPY | DELAYED | DERIVED | 05,07 |
| L254 | 05 | rvol30 1m sigma | ADP | 9.03% | % | 2026-07-17 | stdev(30d daily returns)*sqrt(21) | DELAYED | DERIVED | 05,15 |
| L255 | 05 | maxDD60/VaR/CVaR | ADP | dd -8.19%, VaR95 -10.9%, CVaR95 -14.6% | % | 2026-07-17 | 60d window; parametric mu-1.65/2.06 sigma (normality assumed) | DELAYED | DERIVED | 05,07 |
| L256 | 05 | technical pack | ADP | TD9 SELL_SETUP_6/SELL_SETUP_4/SELL_SETUP_2; RSI 68.81/61.68/50.16; MACD ABOVE_SIGNAL/ABOVE_SIGNAL/BELOW_SIGNAL | - | 2026-07-17 | technical_indicators.json (technical_indicators.py) | DELAYED | DERIVED | 05,06,09 |
| L257 | 05 | next earnings | ADP | 2026-07-29 (9d, confirmed) | date | 2026-07-20 | api.nasdaq.com analyst earnings-date; +91d cadence for vendor-empty post-prints | DELAYED | OBSERVED | 05,08 |
| L258 | 05 | forecast block | ADP | mu +4.0% (band prior +4%), sigma 9.03% REALIZED_VOL_30D, target 265.48, CI [241.51,289.44] | - | 2026-07-20 | mu Calibration Table band @ pctl 87.3; CI=entry*(1+mu±1.04σ) | DELAYED | DERIVED | 05,09,15 |
| L259 | 05 | close | IQV | 206.26 | USD | 2026-07-17 | Nasdaq historical bulk (row L005) | DELAYED | OBSERVED | 05,06,09,15 |
| L260 | 05 | beta60/te | IQV | beta 0.459 | - | 2026-07-17 | 60d daily regression vs SPY | DELAYED | DERIVED | 05,07 |
| L261 | 05 | rvol30 1m sigma | IQV | 11.19% | % | 2026-07-17 | stdev(30d daily returns)*sqrt(21) | DELAYED | DERIVED | 05,15 |
| L262 | 05 | maxDD60/VaR/CVaR | IQV | dd -10.59%, VaR95 -14.5%, CVaR95 -19.0% | % | 2026-07-17 | 60d window; parametric mu-1.65/2.06 sigma (normality assumed) | DELAYED | DERIVED | 05,07 |
| L263 | 05 | technical pack | IQV | TD9 BUY_SETUP_1/SELL_SETUP_4/SELL_SETUP_2; RSI 62.67/58.36/52.0; MACD ABOVE_SIGNAL/ABOVE_SIGNAL/BULLISH_CROSS | - | 2026-07-17 | technical_indicators.json (technical_indicators.py) | DELAYED | DERIVED | 05,06,09 |
| L264 | 05 | next earnings | IQV | 2026-07-28 (8d, confirmed) | date | 2026-07-20 | api.nasdaq.com analyst earnings-date; +91d cadence for vendor-empty post-prints | DELAYED | OBSERVED | 05,08 |
| L265 | 05 | forecast block | IQV | mu +4.0% (band prior +4%), sigma 11.19% REALIZED_VOL_30D, target 214.51, CI [190.52,238.5] | - | 2026-07-20 | mu Calibration Table band @ pctl 87.1; CI=entry*(1+mu±1.04σ) | DELAYED | DERIVED | 05,09,15 |
| L266 | 05 | close | MCO | 510.86 | USD | 2026-07-17 | Nasdaq historical bulk (row L005) | DELAYED | OBSERVED | 05,06,09,15 |
| L267 | 05 | beta60/te | MCO | beta 0.078 | - | 2026-07-17 | 60d daily regression vs SPY | DELAYED | DERIVED | 05,07 |
| L268 | 05 | rvol30 1m sigma | MCO | 8.71% | % | 2026-07-17 | stdev(30d daily returns)*sqrt(21) | DELAYED | DERIVED | 05,15 |
| L269 | 05 | maxDD60/VaR/CVaR | MCO | dd -8.1%, VaR95 -10.4%, CVaR95 -13.9% | % | 2026-07-17 | 60d window; parametric mu-1.65/2.06 sigma (normality assumed) | DELAYED | DERIVED | 05,07 |
| L270 | 05 | technical pack | MCO | TD9 SELL_SETUP_4/SELL_SETUP_3/SELL_SETUP_1; RSI 66.93/62.61/58.41; MACD ABOVE_SIGNAL/ABOVE_SIGNAL/BELOW_SIGNAL | - | 2026-07-17 | technical_indicators.json (technical_indicators.py) | DELAYED | DERIVED | 05,06,09 |
| L271 | 05 | next earnings | MCO | 2026-07-22 (2d, confirmed) | date | 2026-07-20 | api.nasdaq.com analyst earnings-date; +91d cadence for vendor-empty post-prints | DELAYED | OBSERVED | 05,08 |
| L272 | 05 | forecast block | MCO | mu +4.0% (band prior +4%), sigma 8.71% REALIZED_VOL_30D, target 531.29, CI [485.04,577.54] | - | 2026-07-20 | mu Calibration Table band @ pctl 86.2; CI=entry*(1+mu±1.04σ) | DELAYED | DERIVED | 05,09,15 |
| L273 | 05 | close | CHRW | 208.5 | USD | 2026-07-17 | Nasdaq historical bulk (row L005) | DELAYED | OBSERVED | 05,06,09,15 |
| L274 | 05 | beta60/te | CHRW | beta 0.512 | - | 2026-07-17 | 60d daily regression vs SPY | DELAYED | DERIVED | 05,07 |
| L275 | 05 | rvol30 1m sigma | CHRW | 8.89% | % | 2026-07-17 | stdev(30d daily returns)*sqrt(21) | DELAYED | DERIVED | 05,15 |
| L276 | 05 | maxDD60/VaR/CVaR | CHRW | dd -15.2%, VaR95 -11.7%, CVaR95 -15.3% | % | 2026-07-17 | 60d window; parametric mu-1.65/2.06 sigma (normality assumed) | DELAYED | DERIVED | 05,07 |
| L277 | 05 | technical pack | CHRW | TD9 SELL_SETUP_7/SELL_SETUP_1/SELL_SETUP_2; RSI 72.19/65.81/74.55; MACD ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | - | 2026-07-17 | technical_indicators.json (technical_indicators.py) | DELAYED | DERIVED | 05,06,09 |
| L278 | 05 | next earnings | CHRW | 2026-07-29 (9d, confirmed) | date | 2026-07-20 | api.nasdaq.com analyst earnings-date; +91d cadence for vendor-empty post-prints | DELAYED | OBSERVED | 05,08 |
| L279 | 05 | forecast block | CHRW | mu +3.0% (band prior +4% - 1pp exhaustion (RSI/TD9 flag)), sigma 8.89% REALIZED_VOL_30D, target 214.75, CI [195.47,234.04] | - | 2026-07-20 | mu Calibration Table band @ pctl 86.0; CI=entry*(1+mu±1.04σ) | DELAYED | DERIVED | 05,09,15 |
| L280 | 05 | close | SNA | 410.99 | USD | 2026-07-17 | Nasdaq historical bulk (row L005) | DELAYED | OBSERVED | 05,06,09,15 |
| L281 | 05 | beta60/te | SNA | beta 0.552 | - | 2026-07-17 | 60d daily regression vs SPY | DELAYED | DERIVED | 05,07 |
| L282 | 05 | rvol30 1m sigma | SNA | 5.91% | % | 2026-07-17 | stdev(30d daily returns)*sqrt(21) | DELAYED | DERIVED | 05,15 |
| L283 | 05 | maxDD60/VaR/CVaR | SNA | dd -7.96%, VaR95 -5.8%, CVaR95 -8.2% | % | 2026-07-17 | 60d window; parametric mu-1.65/2.06 sigma (normality assumed) | DELAYED | DERIVED | 05,07 |
| L284 | 05 | technical pack | SNA | TD9 SELL_SETUP_4/SELL_SETUP_7/SELL_SETUP_9; RSI 61.99/67.08/67.37; MACD BULLISH_CROSS/ABOVE_SIGNAL/ABOVE_SIGNAL | - | 2026-07-17 | technical_indicators.json (technical_indicators.py) | DELAYED | DERIVED | 05,06,09 |
| L285 | 05 | next earnings | SNA | 2026-07-23 (3d, confirmed) | date | 2026-07-20 | api.nasdaq.com analyst earnings-date; +91d cadence for vendor-empty post-prints | DELAYED | OBSERVED | 05,08 |
| L286 | 05 | forecast block | SNA | mu +4.0% (band prior +4%), sigma 5.91% REALIZED_VOL_30D, target 427.43, CI [402.15,452.71] | - | 2026-07-20 | mu Calibration Table band @ pctl 85.4; CI=entry*(1+mu±1.04σ) | DELAYED | DERIVED | 05,09,15 |
| L287 | 05 | close | UPS | 117.72 | USD | 2026-07-17 | Nasdaq historical bulk (row L005) | DELAYED | OBSERVED | 05,06,09,15 |
| L288 | 05 | beta60/te | UPS | beta 0.942 | - | 2026-07-17 | 60d daily regression vs SPY | DELAYED | DERIVED | 05,07 |
| L289 | 05 | rvol30 1m sigma | UPS | 9.19% | % | 2026-07-17 | stdev(30d daily returns)*sqrt(21) | DELAYED | DERIVED | 05,15 |
| L290 | 05 | maxDD60/VaR/CVaR | UPS | dd -12.2%, VaR95 -12.2%, CVaR95 -15.9% | % | 2026-07-17 | 60d window; parametric mu-1.65/2.06 sigma (normality assumed) | DELAYED | DERIVED | 05,07 |
| L291 | 05 | technical pack | UPS | TD9 SELL_SETUP_9/SELL_SETUP_7/SELL_SETUP_1; RSI 69.36/64.83/51.13; MACD ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | - | 2026-07-17 | technical_indicators.json (technical_indicators.py) | DELAYED | DERIVED | 05,06,09 |
| L292 | 05 | next earnings | UPS | 2026-07-28 (8d, confirmed) | date | 2026-07-20 | api.nasdaq.com analyst earnings-date; +91d cadence for vendor-empty post-prints | DELAYED | OBSERVED | 05,08 |
| L293 | 05 | forecast block | UPS | mu +3.0% (band prior +4% - 1pp exhaustion (RSI/TD9 flag)), sigma 9.19% REALIZED_VOL_30D, target 121.25, CI [110.0,132.51] | - | 2026-07-20 | mu Calibration Table band @ pctl 85.0; CI=entry*(1+mu±1.04σ) | DELAYED | DERIVED | 05,09,15 |
| L294 | 05 | close | AAPL | 333.74 | USD | 2026-07-17 | Nasdaq historical bulk (row L005) | DELAYED | OBSERVED | 05,06,09,15 |
| L295 | 05 | beta60/te | AAPL | beta 0.448 | - | 2026-07-17 | 60d daily regression vs SPY | DELAYED | DERIVED | 05,07 |
| L296 | 05 | rvol30 1m sigma | AAPL | 9.83% | % | 2026-07-17 | stdev(30d daily returns)*sqrt(21) | DELAYED | DERIVED | 05,15 |
| L297 | 05 | maxDD60/VaR/CVaR | AAPL | dd -12.71%, VaR95 -14.2%, CVaR95 -18.2% | % | 2026-07-17 | 60d window; parametric mu-1.65/2.06 sigma (normality assumed) | DELAYED | DERIVED | 05,07 |
| L298 | 05 | technical pack | AAPL | TD9 SELL_SETUP_9/SELL_SETUP_3/SELL_SETUP_3; RSI 71.65/69.4/70.21; MACD ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | - | 2026-07-17 | technical_indicators.json (technical_indicators.py) | DELAYED | DERIVED | 05,06,09 |
| L299 | 05 | next earnings | AAPL | 2026-07-30 (10d, confirmed) | date | 2026-07-20 | api.nasdaq.com analyst earnings-date; +91d cadence for vendor-empty post-prints | DELAYED | OBSERVED | 05,08 |
| L300 | 05 | forecast block | AAPL | mu +2.0% (band prior +3% - 1pp exhaustion (RSI/TD9 flag)), sigma 9.83% REALIZED_VOL_30D, target 340.41, CI [306.31,374.52] | - | 2026-07-20 | mu Calibration Table band @ pctl 81.3; CI=entry*(1+mu±1.04σ) | DELAYED | DERIVED | 05,09,15 |
| L301 | 05 | close | WST | 358.24 | USD | 2026-07-17 | Nasdaq historical bulk (row L005) | DELAYED | OBSERVED | 05,06,09,15 |
| L302 | 05 | beta60/te | WST | beta 0.012 | - | 2026-07-17 | 60d daily regression vs SPY | DELAYED | DERIVED | 05,07 |
| L303 | 05 | rvol30 1m sigma | WST | 6.44% | % | 2026-07-17 | stdev(30d daily returns)*sqrt(21) | DELAYED | DERIVED | 05,15 |
| L304 | 05 | maxDD60/VaR/CVaR | WST | dd -7.89%, VaR95 -7.6%, CVaR95 -10.3% | % | 2026-07-17 | 60d window; parametric mu-1.65/2.06 sigma (normality assumed) | DELAYED | DERIVED | 05,07 |
| L305 | 05 | technical pack | WST | TD9 BUY_SETUP_1/SELL_SETUP_6/SELL_SETUP_4; RSI 61.47/68.11/61.6; MACD BELOW_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | - | 2026-07-17 | technical_indicators.json (technical_indicators.py) | DELAYED | DERIVED | 05,06,09 |
| L306 | 05 | next earnings | WST | 2026-07-23 (3d, confirmed) | date | 2026-07-20 | api.nasdaq.com analyst earnings-date; +91d cadence for vendor-empty post-prints | DELAYED | OBSERVED | 05,08 |
| L307 | 05 | forecast block | WST | mu +3.0% (band prior +3%), sigma 6.44% REALIZED_VOL_30D, target 368.99, CI [344.99,392.99] | - | 2026-07-20 | mu Calibration Table band @ pctl 80.3; CI=entry*(1+mu±1.04σ) | DELAYED | DERIVED | 05,09,15 |
| L308 | 05 | close | LLY | 1179.11 | USD | 2026-07-17 | Nasdaq historical bulk (row L005) | DELAYED | OBSERVED | 05,06,09,15 |
| L309 | 05 | beta60/te | LLY | beta 0.021 | - | 2026-07-17 | 60d daily regression vs SPY | DELAYED | DERIVED | 05,07 |
| L310 | 05 | rvol30 1m sigma | LLY | 9.51% | % | 2026-07-17 | stdev(30d daily returns)*sqrt(21) | DELAYED | DERIVED | 05,15 |
| L311 | 05 | maxDD60/VaR/CVaR | LLY | dd -7.63%, VaR95 -14.7%, CVaR95 -18.6% | % | 2026-07-17 | 60d window; parametric mu-1.65/2.06 sigma (normality assumed) | DELAYED | DERIVED | 05,07 |
| L312 | 05 | technical pack | LLY | TD9 BUY_SETUP_6/SELL_SETUP_9/SELL_SETUP_3; RSI 54.85/63.97/66.35; MACD BELOW_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | - | 2026-07-17 | technical_indicators.json (technical_indicators.py) | DELAYED | DERIVED | 05,06,09 |
| L313 | 05 | next earnings | LLY | 2026-08-05 (16d, confirmed) | date | 2026-07-20 | api.nasdaq.com analyst earnings-date; +91d cadence for vendor-empty post-prints | DELAYED | OBSERVED | 05,08 |
| L314 | 05 | forecast block | LLY | mu +1.0% (band prior +2% - 1pp exhaustion (RSI/TD9 flag)), sigma 9.51% REALIZED_VOL_30D, target 1190.9, CI [1074.24,1307.56] | - | 2026-07-20 | mu Calibration Table band @ pctl 77.6; CI=entry*(1+mu±1.04σ) | DELAYED | DERIVED | 05,09,15 |
| L315 | 05 | close | GE | 348.83 | USD | 2026-07-17 | Nasdaq historical bulk (row L005) | DELAYED | OBSERVED | 05,06,09,15 |
| L316 | 05 | beta60/te | GE | beta 1.033 | - | 2026-07-17 | 60d daily regression vs SPY | DELAYED | DERIVED | 05,07 |
| L317 | 05 | rvol30 1m sigma | GE | 9.52% | % | 2026-07-17 | stdev(30d daily returns)*sqrt(21) | DELAYED | DERIVED | 05,15 |
| L318 | 05 | maxDD60/VaR/CVaR | GE | dd -8.7%, VaR95 -14.7%, CVaR95 -18.6% | % | 2026-07-17 | 60d window; parametric mu-1.65/2.06 sigma (normality assumed) | DELAYED | DERIVED | 05,07 |
| L319 | 05 | technical pack | GE | TD9 BUY_SETUP_2/BUY_SETUP_1/SELL_SETUP_3; RSI 47.84/58.39/68.1; MACD BELOW_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | - | 2026-07-17 | technical_indicators.json (technical_indicators.py) | DELAYED | DERIVED | 05,06,09 |
| L320 | 05 | next earnings | GE | 2026-10-15 (87d, ESTIMATED print-cadence +91d (±5d)) | date | 2026-07-20 | api.nasdaq.com analyst earnings-date; +91d cadence for vendor-empty post-prints | DELAYED | INFERRED | 05,08 |
| L321 | 05 | forecast block | GE | mu +1.0% (band prior +1%), sigma 9.52% REALIZED_VOL_30D, target 352.32, CI [317.77,386.87] | - | 2026-07-20 | mu Calibration Table band @ pctl 68.8; CI=entry*(1+mu±1.04σ) | DELAYED | DERIVED | 05,09,15 |
| L322 | 10 | intraday spot | SPY | 746.52 (+0.43%) | USD | 2026-07-20 | IBKR get_price_snapshot ts 2026-07-20T16:29Z (RTH) | LIVE | OBSERVED | 10 only - no scoring use |
| L323 | 10 | intraday spot | QQQ | 703.15 (+1.12%) | USD | 2026-07-20 | IBKR get_price_snapshot ts 2026-07-20T16:29Z (RTH) | LIVE | OBSERVED | 10 only - no scoring use |
| L324 | 10 | intraday spot | SOXX | 533.81 (+2.30%) | USD | 2026-07-20 | IBKR get_price_snapshot ts 2026-07-20T16:29Z (RTH) | LIVE | OBSERVED | 10 only - no scoring use |
| L325 | 10 | intraday spot | AVGO | 382.16 (+3.06%) | USD | 2026-07-20 | IBKR get_price_snapshot ts 2026-07-20T16:29Z (RTH) | LIVE | OBSERVED | 10 only - no scoring use |

**Coverage:** 325 rows — OBSERVED 136 (incl. 4 LIVE intraday spots used only by 10), DERIVED 174, INFERRED 15, ILLUSTRATIVE 0, UNAVAILABLE 0. The family-availability disclosure row (L012) carries freshness_tag UNAVAILABLE by design; no Required input row is UNAVAILABLE.

Status eligibility: all five Required inputs grounded (grounded entry prices; ≥60d history universe-wide; sigma chain step 2; earnings confirmed/cadence-estimated for every published name; index-union universe). Fund/Sent are Enhancing-class gaps handled via DQ 0.80 + confidence caps — never GO blockers. Final status NO_TRADE is driven by evidence thresholds, not input failure.