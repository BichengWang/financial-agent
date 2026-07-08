# 01 Preflight

Data mode: `DELAYED_PARTIAL`. Source Ledger rows below are the only facts used downstream; unavailable non-price feeds are explicit blockers/caps.

| row_id | artifact | field | ticker/entity | value | unit | observation_date | source | freshness_tag | claim_type | used_by |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| L001 | 01_preflight.md | index_union_universe | S&P500_UNION_NDX100 | 515 | count | 2026-07-08 | build_index_universe.py; universe_summary.json | HISTORICAL | OBSERVED | 03,04,05 |
| L002 | 01_preflight.md | price_history_coverage | ALL_REQUESTED | 517/518 | tickers | 2026-07-08 | Yahoo chart CSV prefetch; retrieved_at 2026-07-08T17:44:12Z; history_prefetch_summary.json | DELAYED | OBSERVED | 01,03,05,07 |
| L003 | 01_preflight.md | technical_indicator_pack | ALL_SOURCEABLE | 517 | tickers | 2026-07-08 | technical_indicators.py output; generated_at 2026-07-08T17:44:20Z | DELAYED | DERIVED | 03,05 |
| L004 | 01_preflight.md | next_earnings_date | ALL_RANKED | UNAVAILABLE | date | 2026-07-08 | No connected earnings calendar feed in this run | UNAVAILABLE | UNAVAILABLE | 00,04,05,08 |
| L005 | 01_preflight.md | fundamental_revision_metrics | ALL_RANKED | UNAVAILABLE | mixed | 2026-07-08 | No connected fundamental/revision feed in this run | UNAVAILABLE | UNAVAILABLE | 04,05,08 |
| L006 | 01_preflight.md | sentiment_positioning_metrics | ALL_RANKED | UNAVAILABLE | mixed | 2026-07-08 | No options/short-interest/borrow/positioning feed in this run | UNAVAILABLE | UNAVAILABLE | 04,05,08 |
| L007 | 01_preflight.md | bid_ask_execution_tape | ALL_RANKED | UNAVAILABLE | mixed | 2026-07-08 | No live bid-ask/execution-quality feed in this run | UNAVAILABLE | UNAVAILABLE | 00,08 |
| L008 | 01_preflight.md | entry_price | SPY | 744.92 | USD | 2026-07-08 | Yahoo chart CSV investments/equity/output/gpt-5-2026-07-08/history/SPY.csv; retrieved_at 2026-07-08T17:44:20Z | DELAYED | OBSERVED | 03,09,15 |
| L009 | 01_preflight.md | etf_forecast_metrics | SPY | mu=0.0050; sigma=0.0441; beta=1.00 | decimal | 2026-07-08 | Derived from 60d/30d fetched returns plus technical_indicators.json | DELAYED | DERIVED | 03,09,15 |
| L010 | 01_preflight.md | entry_price | QQQ | 709.53 | USD | 2026-07-08 | Yahoo chart CSV investments/equity/output/gpt-5-2026-07-08/history/QQQ.csv; retrieved_at 2026-07-08T17:44:20Z | DELAYED | OBSERVED | 03,09,15 |
| L011 | 01_preflight.md | etf_forecast_metrics | QQQ | mu=0.0083; sigma=0.0859; beta=1.66 | decimal | 2026-07-08 | Derived from 60d/30d fetched returns plus technical_indicators.json | DELAYED | DERIVED | 03,09,15 |
| L012 | 01_preflight.md | entry_price | SOXX | 561.37 | USD | 2026-07-08 | Yahoo chart CSV investments/equity/output/gpt-5-2026-07-08/history/SOXX.csv; retrieved_at 2026-07-08T17:44:20Z | DELAYED | OBSERVED | 03,09,15 |
| L013 | 01_preflight.md | etf_forecast_metrics | SOXX | mu=0.0221; sigma=0.2220; beta=3.42 | decimal | 2026-07-08 | Derived from 60d/30d fetched returns plus technical_indicators.json | DELAYED | DERIVED | 03,09,15 |
| L014 | 01_preflight.md | settlement_current_price | MCK | 815.34 | USD | 2026-07-08 | Yahoo chart CSV; retrieved_at 2026-07-08T17:44:20Z | DELAYED | OBSERVED | 02,15 |
| L015 | 01_preflight.md | settlement_current_price | COST | 953.77 | USD | 2026-07-08 | Yahoo chart CSV; retrieved_at 2026-07-08T17:44:20Z | DELAYED | OBSERVED | 02,15 |
| L016 | 01_preflight.md | settlement_current_price | WMT | 112.85 | USD | 2026-07-08 | Yahoo chart CSV; retrieved_at 2026-07-08T17:44:20Z | DELAYED | OBSERVED | 02,15 |
| L017 | 01_preflight.md | settlement_current_price | CVX | 175.74 | USD | 2026-07-08 | Yahoo chart CSV; retrieved_at 2026-07-08T17:44:20Z | DELAYED | OBSERVED | 02,15 |
| L018 | 01_preflight.md | settlement_current_price | UNH | 426.86 | USD | 2026-07-08 | Yahoo chart CSV; retrieved_at 2026-07-08T17:44:20Z | DELAYED | OBSERVED | 02,15 |
| L019 | 01_preflight.md | settlement_current_price | MU | 937.60 | USD | 2026-07-08 | Yahoo chart CSV; retrieved_at 2026-07-08T17:44:20Z | DELAYED | OBSERVED | 02,15 |
| L020 | 01_preflight.md | settlement_current_price | XOM | 140.22 | USD | 2026-07-08 | Yahoo chart CSV; retrieved_at 2026-07-08T17:44:20Z | DELAYED | OBSERVED | 02,15 |
| L021 | 01_preflight.md | settlement_current_price | LIN | 529.08 | USD | 2026-07-08 | Yahoo chart CSV; retrieved_at 2026-07-08T17:44:20Z | DELAYED | OBSERVED | 02,15 |
| L022 | 01_preflight.md | settlement_current_price | LLY | 1222.50 | USD | 2026-07-08 | Yahoo chart CSV; retrieved_at 2026-07-08T17:44:20Z | DELAYED | OBSERVED | 02,15 |
| L023 | 01_preflight.md | settlement_current_price | NVDA | 202.59 | USD | 2026-07-08 | Yahoo chart CSV; retrieved_at 2026-07-08T17:44:20Z | DELAYED | OBSERVED | 02,15 |
| L024 | 01_preflight.md | settlement_current_price | GOOGL | 360.04 | USD | 2026-07-08 | Yahoo chart CSV; retrieved_at 2026-07-08T17:44:20Z | DELAYED | OBSERVED | 02,15 |
| L025 | 01_preflight.md | settlement_current_price | ABBV | 253.81 | USD | 2026-07-08 | Yahoo chart CSV; retrieved_at 2026-07-08T17:44:20Z | DELAYED | OBSERVED | 02,15 |
| L026 | 01_preflight.md | entry_price | DDOG | 256.84 | USD | 2026-07-08 | Yahoo chart CSV investments/equity/output/gpt-5-2026-07-08/history/DDOG.csv; retrieved_at 2026-07-08T17:44:20Z | DELAYED | OBSERVED | 05,06,09,15 |
| L027 | 01_preflight.md | ranking_and_risk_metrics | DDOG | Adj=1.19; Tech_Z=5.33; sigma=0.1834; beta=0.59 | decimal | 2026-07-08 | Derived from fetched 60d/30d returns and technical_indicators.json | DELAYED | DERIVED | 05,06,07,08,15 |
| L028 | 01_preflight.md | entry_price | DELL | 431.44 | USD | 2026-07-08 | Yahoo chart CSV investments/equity/output/gpt-5-2026-07-08/history/DELL.csv; retrieved_at 2026-07-08T17:44:20Z | DELAYED | OBSERVED | 05,06,09,15 |
| L029 | 01_preflight.md | ranking_and_risk_metrics | DELL | Adj=1.09; Tech_Z=4.96; sigma=0.3312; beta=2.36 | decimal | 2026-07-08 | Derived from fetched 60d/30d returns and technical_indicators.json | DELAYED | DERIVED | 05,06,07,08,15 |
| L030 | 01_preflight.md | entry_price | PANW | 321.02 | USD | 2026-07-08 | Yahoo chart CSV investments/equity/output/gpt-5-2026-07-08/history/PANW.csv; retrieved_at 2026-07-08T17:44:20Z | DELAYED | OBSERVED | 05,06,09,15 |
| L031 | 01_preflight.md | ranking_and_risk_metrics | PANW | Adj=0.95; Tech_Z=4.32; sigma=0.1769; beta=1.47 | decimal | 2026-07-08 | Derived from fetched 60d/30d returns and technical_indicators.json | DELAYED | DERIVED | 05,06,07,08,15 |
| L032 | 01_preflight.md | entry_price | CRWD | 189.52 | USD | 2026-07-08 | Yahoo chart CSV investments/equity/output/gpt-5-2026-07-08/history/CRWD.csv; retrieved_at 2026-07-08T17:44:20Z | DELAYED | OBSERVED | 05,06,09,15 |
| L033 | 01_preflight.md | ranking_and_risk_metrics | CRWD | Adj=0.86; Tech_Z=3.92; sigma=0.1627; beta=1.44 | decimal | 2026-07-08 | Derived from fetched 60d/30d returns and technical_indicators.json | DELAYED | DERIVED | 05,06,07,08,15 |
| L034 | 01_preflight.md | entry_price | MU | 937.60 | USD | 2026-07-08 | Yahoo chart CSV investments/equity/output/gpt-5-2026-07-08/history/MU.csv; retrieved_at 2026-07-08T17:44:20Z | DELAYED | OBSERVED | 05,06,09,15 |
| L035 | 01_preflight.md | ranking_and_risk_metrics | MU | Adj=0.81; Tech_Z=3.78; sigma=0.3654; beta=4.49 | decimal | 2026-07-08 | Derived from fetched 60d/30d returns and technical_indicators.json | DELAYED | DERIVED | 05,06,07,08,15 |
| L036 | 01_preflight.md | entry_price | HUM | 402.05 | USD | 2026-07-08 | Yahoo chart CSV investments/equity/output/gpt-5-2026-07-08/history/HUM.csv; retrieved_at 2026-07-08T17:44:20Z | DELAYED | OBSERVED | 05,06,09,15 |
| L037 | 01_preflight.md | ranking_and_risk_metrics | HUM | Adj=0.81; Tech_Z=3.81; sigma=0.1123; beta=0.16 | decimal | 2026-07-08 | Derived from fetched 60d/30d returns and technical_indicators.json | DELAYED | DERIVED | 05,06,07,08,15 |
| L038 | 01_preflight.md | entry_price | FTNT | 155.92 | USD | 2026-07-08 | Yahoo chart CSV investments/equity/output/gpt-5-2026-07-08/history/FTNT.csv; retrieved_at 2026-07-08T17:44:20Z | DELAYED | OBSERVED | 05,06,09,15 |
| L039 | 01_preflight.md | ranking_and_risk_metrics | FTNT | Adj=0.77; Tech_Z=3.58; sigma=0.1282; beta=0.84 | decimal | 2026-07-08 | Derived from fetched 60d/30d returns and technical_indicators.json | DELAYED | DERIVED | 05,06,07,08,15 |
| L040 | 01_preflight.md | entry_price | AMD | 512.41 | USD | 2026-07-08 | Yahoo chart CSV investments/equity/output/gpt-5-2026-07-08/history/AMD.csv; retrieved_at 2026-07-08T17:44:20Z | DELAYED | OBSERVED | 05,06,09,15 |
| L041 | 01_preflight.md | ranking_and_risk_metrics | AMD | Adj=0.74; Tech_Z=3.46; sigma=0.2372; beta=4.49 | decimal | 2026-07-08 | Derived from fetched 60d/30d returns and technical_indicators.json | DELAYED | DERIVED | 05,06,07,08,15 |
| L042 | 01_preflight.md | entry_price | MRNA | 74.52 | USD | 2026-07-08 | Yahoo chart CSV investments/equity/output/gpt-5-2026-07-08/history/MRNA.csv; retrieved_at 2026-07-08T17:44:20Z | DELAYED | OBSERVED | 05,06,09,15 |
| L043 | 01_preflight.md | ranking_and_risk_metrics | MRNA | Adj=0.71; Tech_Z=3.28; sigma=0.2339; beta=1.17 | decimal | 2026-07-08 | Derived from fetched 60d/30d returns and technical_indicators.json | DELAYED | DERIVED | 05,06,07,08,15 |
| L044 | 01_preflight.md | entry_price | AXON | 602.40 | USD | 2026-07-08 | Yahoo chart CSV investments/equity/output/gpt-5-2026-07-08/history/AXON.csv; retrieved_at 2026-07-08T17:44:20Z | DELAYED | OBSERVED | 05,06,09,15 |
| L045 | 01_preflight.md | ranking_and_risk_metrics | AXON | Adj=0.70; Tech_Z=3.30; sigma=0.2136; beta=1.25 | decimal | 2026-07-08 | Derived from fetched 60d/30d returns and technical_indicators.json | DELAYED | DERIVED | 05,06,07,08,15 |
| L046 | 01_preflight.md | entry_price | HOOD | 111.79 | USD | 2026-07-08 | Yahoo chart CSV investments/equity/output/gpt-5-2026-07-08/history/HOOD.csv; retrieved_at 2026-07-08T17:44:20Z | DELAYED | OBSERVED | 05,06,09,15 |
| L047 | 01_preflight.md | ranking_and_risk_metrics | HOOD | Adj=0.66; Tech_Z=3.06; sigma=0.2320; beta=2.47 | decimal | 2026-07-08 | Derived from fetched 60d/30d returns and technical_indicators.json | DELAYED | DERIVED | 05,06,07,08,15 |
| L048 | 01_preflight.md | entry_price | SNDK | 1660.05 | USD | 2026-07-08 | Yahoo chart CSV investments/equity/output/gpt-5-2026-07-08/history/SNDK.csv; retrieved_at 2026-07-08T17:44:20Z | DELAYED | OBSERVED | 05,06,09,15 |
| L049 | 01_preflight.md | ranking_and_risk_metrics | SNDK | Adj=0.60; Tech_Z=2.87; sigma=0.3846; beta=3.96 | decimal | 2026-07-08 | Derived from fetched 60d/30d returns and technical_indicators.json | DELAYED | DERIVED | 05,06,07,08,15 |
| L050 | 01_preflight.md | entry_price | CNC | 67.46 | USD | 2026-07-08 | Yahoo chart CSV investments/equity/output/gpt-5-2026-07-08/history/CNC.csv; retrieved_at 2026-07-08T17:44:20Z | DELAYED | OBSERVED | 05,06,09,15 |
| L051 | 01_preflight.md | ranking_and_risk_metrics | CNC | Adj=0.55; Tech_Z=2.64; sigma=0.1245; beta=-0.56 | decimal | 2026-07-08 | Derived from fetched 60d/30d returns and technical_indicators.json | DELAYED | DERIVED | 05,06,07,08,15 |
| L052 | 01_preflight.md | entry_price | ARM | 297.38 | USD | 2026-07-08 | Yahoo chart CSV investments/equity/output/gpt-5-2026-07-08/history/ARM.csv; retrieved_at 2026-07-08T17:44:20Z | DELAYED | OBSERVED | 05,06,09,15 |
| L053 | 01_preflight.md | ranking_and_risk_metrics | ARM | Adj=0.49; Tech_Z=2.46; sigma=0.3212; beta=5.17 | decimal | 2026-07-08 | Derived from fetched 60d/30d returns and technical_indicators.json | DELAYED | DERIVED | 05,06,07,08,15 |
| L054 | 01_preflight.md | entry_price | DVA | 231.43 | USD | 2026-07-08 | Yahoo chart CSV investments/equity/output/gpt-5-2026-07-08/history/DVA.csv; retrieved_at 2026-07-08T17:44:20Z | DELAYED | OBSERVED | 05,06,09,15 |
| L055 | 01_preflight.md | ranking_and_risk_metrics | DVA | Adj=0.43; Tech_Z=2.16; sigma=0.0719; beta=0.48 | decimal | 2026-07-08 | Derived from fetched 60d/30d returns and technical_indicators.json | DELAYED | DERIVED | 05,06,07,08,15 |
| L056 | 01_preflight.md | entry_price | NTAP | 164.08 | USD | 2026-07-08 | Yahoo chart CSV investments/equity/output/gpt-5-2026-07-08/history/NTAP.csv; retrieved_at 2026-07-08T17:44:20Z | DELAYED | OBSERVED | 05,06,09,15 |
| L057 | 01_preflight.md | ranking_and_risk_metrics | NTAP | Adj=0.41; Tech_Z=2.06; sigma=0.2194; beta=1.19 | decimal | 2026-07-08 | Derived from fetched 60d/30d returns and technical_indicators.json | DELAYED | DERIVED | 05,06,07,08,15 |
| L058 | 01_preflight.md | entry_price | INTC | 107.62 | USD | 2026-07-08 | Yahoo chart CSV investments/equity/output/gpt-5-2026-07-08/history/INTC.csv; retrieved_at 2026-07-08T17:44:20Z | DELAYED | OBSERVED | 05,06,09,15 |
| L059 | 01_preflight.md | ranking_and_risk_metrics | INTC | Adj=0.39; Tech_Z=1.96; sigma=0.2694; beta=3.52 | decimal | 2026-07-08 | Derived from fetched 60d/30d returns and technical_indicators.json | DELAYED | DERIVED | 05,06,07,08,15 |
| L060 | 01_preflight.md | entry_price | HPE | 44.70 | USD | 2026-07-08 | Yahoo chart CSV investments/equity/output/gpt-5-2026-07-08/history/HPE.csv; retrieved_at 2026-07-08T17:44:20Z | DELAYED | OBSERVED | 05,06,09,15 |
| L061 | 01_preflight.md | ranking_and_risk_metrics | HPE | Adj=0.39; Tech_Z=1.96; sigma=0.2576; beta=2.08 | decimal | 2026-07-08 | Derived from fetched 60d/30d returns and technical_indicators.json | DELAYED | DERIVED | 05,06,07,08,15 |
| L062 | 01_preflight.md | entry_price | MRVL | 233.42 | USD | 2026-07-08 | Yahoo chart CSV investments/equity/output/gpt-5-2026-07-08/history/MRVL.csv; retrieved_at 2026-07-08T17:44:20Z | DELAYED | OBSERVED | 05,06,09,15 |
| L063 | 01_preflight.md | ranking_and_risk_metrics | MRVL | Adj=0.34; Tech_Z=1.77; sigma=0.4221; beta=4.41 | decimal | 2026-07-08 | Derived from fetched 60d/30d returns and technical_indicators.json | DELAYED | DERIVED | 05,06,07,08,15 |
| L064 | 01_preflight.md | entry_price | TECH | 70.54 | USD | 2026-07-08 | Yahoo chart CSV investments/equity/output/gpt-5-2026-07-08/history/TECH.csv; retrieved_at 2026-07-08T17:44:20Z | DELAYED | OBSERVED | 05,06,09,15 |
| L065 | 01_preflight.md | ranking_and_risk_metrics | TECH | Adj=0.33; Tech_Z=1.72; sigma=0.1982; beta=0.68 | decimal | 2026-07-08 | Derived from fetched 60d/30d returns and technical_indicators.json | DELAYED | DERIVED | 05,06,07,08,15 |

| L066 | 01_preflight.md | mom_prior_price | MCK | 784.23 | USD | 2026-06-09 | Yahoo chart CSV investments/equity/output/gpt-5-2026-07-08/history/MCK.csv; retrieved_at 2026-07-08T17:44:20Z | DELAYED | OBSERVED | 02 |
| L067 | 01_preflight.md | mom_current_price | MCK | 815.34 | USD | 2026-07-08 | Yahoo chart CSV investments/equity/output/gpt-5-2026-07-08/history/MCK.csv; retrieved_at 2026-07-08T17:44:20Z | DELAYED | OBSERVED | 02 |
| L068 | 01_preflight.md | mom_prior_price | PG | 148.67 | USD | 2026-06-09 | Yahoo chart CSV investments/equity/output/gpt-5-2026-07-08/history/PG.csv; retrieved_at 2026-07-08T17:44:20Z | DELAYED | OBSERVED | 02 |
| L069 | 01_preflight.md | mom_current_price | PG | 148.91 | USD | 2026-07-08 | Yahoo chart CSV investments/equity/output/gpt-5-2026-07-08/history/PG.csv; retrieved_at 2026-07-08T17:44:20Z | DELAYED | OBSERVED | 02 |
| L070 | 01_preflight.md | mom_prior_price | WMT | 118.88 | USD | 2026-06-09 | Yahoo chart CSV investments/equity/output/gpt-5-2026-07-08/history/WMT.csv; retrieved_at 2026-07-08T17:44:20Z | DELAYED | OBSERVED | 02 |
| L071 | 01_preflight.md | mom_current_price | WMT | 112.85 | USD | 2026-07-08 | Yahoo chart CSV investments/equity/output/gpt-5-2026-07-08/history/WMT.csv; retrieved_at 2026-07-08T17:44:20Z | DELAYED | OBSERVED | 02 |
| L072 | 01_preflight.md | mom_prior_price | ABBV | 225.42 | USD | 2026-06-09 | Yahoo chart CSV investments/equity/output/gpt-5-2026-07-08/history/ABBV.csv; retrieved_at 2026-07-08T17:44:20Z | DELAYED | OBSERVED | 02 |
| L073 | 01_preflight.md | mom_current_price | ABBV | 253.81 | USD | 2026-07-08 | Yahoo chart CSV investments/equity/output/gpt-5-2026-07-08/history/ABBV.csv; retrieved_at 2026-07-08T17:44:20Z | DELAYED | OBSERVED | 02 |
| L074 | 01_preflight.md | mom_prior_price | JPM | 312.70 | USD | 2026-06-09 | Yahoo chart CSV investments/equity/output/gpt-5-2026-07-08/history/JPM.csv; retrieved_at 2026-07-08T17:44:20Z | DELAYED | OBSERVED | 02 |
| L075 | 01_preflight.md | mom_current_price | JPM | 333.09 | USD | 2026-07-08 | Yahoo chart CSV investments/equity/output/gpt-5-2026-07-08/history/JPM.csv; retrieved_at 2026-07-08T17:44:20Z | DELAYED | OBSERVED | 02 |
| L076 | 01_preflight.md | mom_prior_price | XOM | 148.91 | USD | 2026-06-09 | Yahoo chart CSV investments/equity/output/gpt-5-2026-07-08/history/XOM.csv; retrieved_at 2026-07-08T17:44:20Z | DELAYED | OBSERVED | 02 |
| L077 | 01_preflight.md | mom_current_price | XOM | 140.22 | USD | 2026-07-08 | Yahoo chart CSV investments/equity/output/gpt-5-2026-07-08/history/XOM.csv; retrieved_at 2026-07-08T17:44:20Z | DELAYED | OBSERVED | 02 |
| L078 | 01_preflight.md | mom_prior_price | AZO | 3137.75 | USD | 2026-06-09 | Yahoo chart CSV investments/equity/output/gpt-5-2026-07-08/history/AZO.csv; retrieved_at 2026-07-08T17:44:20Z | DELAYED | OBSERVED | 02 |
| L079 | 01_preflight.md | mom_current_price | AZO | 3072.17 | USD | 2026-07-08 | Yahoo chart CSV investments/equity/output/gpt-5-2026-07-08/history/AZO.csv; retrieved_at 2026-07-08T17:44:20Z | DELAYED | OBSERVED | 02 |
| L080 | 01_preflight.md | mom_prior_price | UNH | 413.00 | USD | 2026-06-09 | Yahoo chart CSV investments/equity/output/gpt-5-2026-07-08/history/UNH.csv; retrieved_at 2026-07-08T17:44:20Z | DELAYED | OBSERVED | 02 |
| L081 | 01_preflight.md | mom_current_price | UNH | 426.86 | USD | 2026-07-08 | Yahoo chart CSV investments/equity/output/gpt-5-2026-07-08/history/UNH.csv; retrieved_at 2026-07-08T17:44:20Z | DELAYED | OBSERVED | 02 |

## Coverage Summary

OBSERVED 53; DERIVED 24; INFERRED 0; ILLUSTRATIVE 0; UNAVAILABLE 4.

Technical indicator rows cite both fetched CSV history and `technical_indicators.json`. Missing earnings/fundamental/sentiment rows are recorded as `UNAVAILABLE`, not treated as neutral evidence.
