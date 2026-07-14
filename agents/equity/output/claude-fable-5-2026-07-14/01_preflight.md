# 01 Preflight — Source Ledger — 2026-07-14

Run: claude-fable-5, Tuesday intraday (13:0x ET; scheduled-task fire delayed past the 07:27 pre-open slot — noted in 00). Data mode **DELAYED** — all scored prices are the 2026-07-13 Monday close, fetched this run from the Nasdaq historical API (bulk; Yahoo v8 returned HTTP 429 for the entire session, second consecutive session — probe documented in `price_history_fetch_manifest.json`), cross-verified against the IBKR MCP (**13/13 exact matches to the cent**, L016). Price-history source chain executed per the Track B change accepted 2026-07-13. VIX from CBOE official CSV; risk-free from Treasury.gov daily bill rates (FRED DTB3 timed out ×3 — documented fallback, L008). Technical indicators computed by `technical_indicators.py` from the exact fetched bars (L003). Fund/Sent family feeds remain unwired: every metric in those families is `UNAVAILABLE` (family contribution 0.00, DQ 0.80 per L020/L021) — 12th consecutive run.

| artifact | field | ticker/entity | value | unit | observation_date | source | freshness_tag | claim_type | used_by |
|---|---|---|---|---|---|---|---|---|---|
| L001 | 03/04 | universe | S&P500∪NDX100 | 515 union (503+101, 89 overlap); 514 eligible (FDXF excluded: 32 bars, listing age) | count | 2026-07-14 | build_index_universe.py; caches fetched_at 2026-06-21 | HISTORICAL | OBSERVED | 00,03,04 |
| L002 | all | price_history_bulk | 519 symbols | 5y daily bars; 517 via Nasdaq hist API (~177s, 8-worker); BF-B via IBKR conid 4931; last bar 2026-07-13 all 520 CSVs (BF-B partial 07-14 intraday bar trimmed); SATS fetched as ECHO | series | 2026-07-13 | price_history_fetch_manifest.json; retrieved_at 2026-07-14T17:07:39Z | DELAYED | OBSERVED | 02,03,05,07 |
| L003 | all | technical_indicators | 518 tickers | 517 OK / FDXF UNAVAILABLE (32 bars); D/W/M TD9, RSI14, MACD, MA, momentum, VR, RS | pack | 2026-07-13 | technical_indicators.py --history-dir (generated_at 2026-07-14T17:12:21Z) | DELAYED | DERIVED | 01,03,04,05 |
| L004 | 02/03 | close | SPY | 749.17 | USD | 2026-07-13 | Nasdaq hist API (L002); IBKR verify exact (L016) | DELAYED | OBSERVED | 02,03,05,15 |
| L005 | 03 | close | QQQ | 711.74 | USD | 2026-07-13 | Nasdaq hist API (L002); IBKR verify exact (L016) | DELAYED | OBSERVED | 03,15 |
| L006 | 03 | close | SOXX | 553.61 | USD | 2026-07-13 | Nasdaq hist API (L002); IBKR verify exact (L016) | DELAYED | OBSERVED | 03,15 |
| L007 | 03 | close | VIX | 17.16 (20d: mean 17.00, range 15.03–19.49) | index | 2026-07-13 | CBOE official VIX_History.csv, retrieved this run | DELAYED | OBSERVED | 03 |
| L008 | 05 | risk_free | 13-week T-bill | 3.76% bank discount (coupon equiv 3.85%); rf_1m 0.3133% | %/yr | 2026-07-13 | Treasury.gov daily bill rates CSV (FRED DTB3 timeout ×3 documented) | DELAYED | OBSERVED | 05 |
| L009 | 03 | close | TLT | 83.97; mom20 -2.34%, mom60 -3.29% | USD | 2026-07-13 | Nasdaq hist API (L002) | DELAYED | OBSERVED | 03 |
| L010 | 03 | etf_stats | SPY | rvol30 4.39% 1m (prior 2.88%); dd60 -1.37%; MA20 744.38 / MA50 741.99 (above both, BULLISH); mom20 +1.55%; RSI_d 54; MACD ABOVE_SIGNAL; 07-13 ret -0.77% | pack | 2026-07-13 | derived from L002/L003 per rules.md §Core ETF | DELAYED | DERIVED | 03,09,15 |
| L011 | 03 | etf_stats | QQQ | rvol30 8.54% 1m (prior 4.49%); dd60 -4.61%; below MA20 (722.30), above MA50 (716.16), MIXED; mom20 -0.75%; RSI_d 48; MACD BELOW_SIGNAL; beta60 1.686; 07-13 ret -1.90% | pack | 2026-07-13 | derived from L002/L003 | DELAYED | DERIVED | 03,09,15 |
| L012 | 03 | etf_stats | SOXX | rvol30 21.80% 1m (prior 12.55%); dd60 -15.48%; below MA20 (598.16) AND MA50 (560.30), MIXED; mom20 -5.68%, mom60 +37.76%; RSI_d 46; MACD BELOW_SIGNAL; beta60 3.59 (60d window incl. melt-up+correction — disclosed); 07-13 ret -4.77% | pack | 2026-07-13 | derived from L002/L003 | DELAYED | DERIVED | 03,09,15 |
| L013 | 03 | rs_ratios | QQQ/SPY, SOXX/SPY | QQQ/SPY 20d -2.26% / 60d +4.33%; SOXX/SPY 20d -7.11% / 60d +28.71% | % | 2026-07-13 | derived from L002 | DELAYED | DERIVED | 03,09 |
| L014 | 03 | regime | US equities | NEUTRAL (9th consecutive label): SPY above both MAs w/ VIX 17.2 mid-range, but growth complex correcting (L010-L013) | label | 2026-07-14 | analyst classification on L004-L013 | DELAYED | INFERRED | 03,05,09 |
| L015 | 04/05 | earnings_calendar | 63 shortlist symbols | 61 confirmed; FAST cadence-est 2026-07-13 ±5d (vendor-empty, penalty applied on buffered window); MU vendor-empty next ~09-25 (outside) | dates | 2026-07-14 | api.nasdaq.com/api/analyst/{sym}/earnings-date; earnings_calendar_manifest.json | DELAYED | OBSERVED | 04,05 |
| L016 | 01 | price_verification | 13 symbols | 13/13 exact to the cent: SPY/QQQ/SOXX + DVA/BAX/CRL/FFIV/FTNT/HUM/EXPD/WST/CVS/TROW | USD | 2026-07-14 | IBKR MCP get_price_snapshot RTH (priorClose or last−change); nasdaq_verification_manifest.json | LIVE | OBSERVED | 00,01,08 |
| L017 | 02 | settlement_convention | gpt-5 06-16 vintage | TARGET_EQ_RUN_DATE: target 2026-07-14 = run date, run is intraday (07-14 close does not exist yet) → settle at latest completed close 2026-07-13 | rule | 2026-07-14 | convention established 2026-07-13 run; codified into rules.md §Settlement Rules this run (Track B, 13) | DELAYED | INFERRED | 02,15 |
| L018 | 02 | baseline_selection | claude-fable-5-2026-06-10 | window 2026-05-30..2026-06-23, target 2026-06-16, folder 6d off target → SAME_MODEL_BASELINE, no gap flag | path | 2026-07-14 | agents.md §Step 2 algorithm over output/ | HISTORICAL | DERIVED | 00,02 |
| L019 | 01 | source_outage | Yahoo v8 chart API | HTTP 429 Too Many Requests (probe after 519-symbol bulk attempt; 0/519 succeeded); 2nd consecutive session | status | 2026-07-14 | direct probe, price_history_fetch_manifest.json | LIVE | OBSERVED | 00,01,13 |
| L020 | 05 | data_quality_multiplier | all ranked | 0.80 (notable coverage gaps: Fund/Sent families unwired) | x | 2026-07-14 | rules.md guideposts | DELAYED | INFERRED | 05,15 |
| L021 | 05 | family_construction | Tech_Z/Macro_Z | Tech_Z = mean z(mom20, mom60, RS20, RS60, VR20, MA-align); Macro_Z = mean z(-abs(maxDD60), -sigma_1m, -abs(beta-1)); winsorized 5/95 over n=514; Fund_Z/Sent_Z UNAVAILABLE (0 sourceable metrics) | formula | 2026-07-14 | z-inputs from L002/L003 per-name; family aggregation per rules.md; identical to 07-13 L021 | DELAYED | DERIVED | 04,05 |
| L022 | 05 | exhaustion_flag_rule | all ranked | flag if RSI14_d >= 75 or RSI14_w >= 80 or TD9 d/w SELL setup count >= 8; penalty 0.05; mu adj -1pp (suspended where it would zero mu — band floor, disclosed; ABBV today) | rule | 2026-07-14 | indicator inputs L003; rule carried from 07-13 L022 | DELAYED | INFERRED | 05 |
| L023 | 05 | earnings_penalty_rule | shortlist | -0.10 for confirmed date ≤14d; buffered ≤14+Nd for ESTIMATED(±Nd); applied: FFIV 13d, FAST est ~-1d(+91d cadence, ±5d); banks/insurers wave 07-15..17 gates STT/ELV/JBHT/MTB/PNC/BNY/RF/UNH/GE at -0.10 | rule | 2026-07-14 | rules.md §Risk Controls; dates L015 | DELAYED | DERIVED | 05 |
| L024 | 02 | settlement | GOOGL (2026-06-16 gpt-5) | settle 352.51 @ 2026-07-13; ret -5.95%; alpha -5.40%; MISS; OUT_CI_LOW; z -1.43 | USD/% | 2026-07-13 | Nasdaq hist API (L002); convention L017 | DELAYED | DERIVED | 02,15 |
| L025 | 02 | settlement | CAT (2026-06-16 gpt-5) | settle 931.47 @ 2026-07-13; ret -2.19%; alpha -1.64%; MISS; IN_CI; z -0.66 | USD/% | 2026-07-13 | Nasdaq hist API (L002); convention L017 | DELAYED | DERIVED | 02,15 |
| L026 | 02 | settlement | LLY (2026-06-16 gpt-5) | settle 1181.87 @ 2026-07-13; ret +5.12%; alpha +5.67%; HIT; IN_CI; z 0.01 | USD/% | 2026-07-13 | Nasdaq hist API (L002); convention L017 | DELAYED | DERIVED | 02,15 |
| L027 | 02 | settlement | UNH (2026-06-16 gpt-5) | settle 429.09 @ 2026-07-13; ret +5.00%; alpha +5.56%; HIT; IN_CI; z 0.0 | USD/% | 2026-07-13 | Nasdaq hist API (L002); convention L017 | DELAYED | DERIVED | 02,15 |
| L028 | 02 | settlement | GE (2026-06-16 gpt-5) | settle 353.42 @ 2026-07-13; ret +1.32%; alpha +1.88%; HIT; IN_CI; z -0.23 | USD/% | 2026-07-13 | Nasdaq hist API (L002); convention L017 | DELAYED | DERIVED | 02,15 |
| L029 | 02 | settlement | CVX (2026-06-16 gpt-5) | settle 182.2 @ 2026-07-13; ret +1.56%; alpha +2.11%; HIT; IN_CI; z -0.31 | USD/% | 2026-07-13 | Nasdaq hist API (L002); convention L017 | DELAYED | DERIVED | 02,15 |
| L030 | 02 | settlement | GS (2026-06-16 gpt-5) | settle 1045.91 @ 2026-07-13; ret -4.36%; alpha -3.80%; MISS; IN_CI; z -0.71 | USD/% | 2026-07-13 | Nasdaq hist API (L002); convention L017 | DELAYED | DERIVED | 02,15 |
| L031 | 02 | settlement | FCX (2026-06-16 gpt-5) | settle 59.97 @ 2026-07-13; ret -14.74%; alpha -14.19%; MISS; IN_CI; z -1.02 | USD/% | 2026-07-13 | Nasdaq hist API (L002); convention L017 | DELAYED | DERIVED | 02,15 |
| L032 | 02 | settlement | BAC (2026-06-16 gpt-5) | settle 59.5 @ 2026-07-13; ret +4.94%; alpha +5.49%; HIT; IN_CI; z 0.45 | USD/% | 2026-07-13 | Nasdaq hist API (L002); convention L017 | DELAYED | DERIVED | 02,15 |
| L033 | 02 | settlement | JPM (2026-06-16 gpt-5) | settle 334.53 @ 2026-07-13; ret +1.62%; alpha +2.17%; HIT; IN_CI; z -0.06 | USD/% | 2026-07-13 | Nasdaq hist API (L002); convention L017 | DELAYED | DERIVED | 02,15 |
| L034 | 02 | settlement | NVDA (2026-06-16 gpt-5) | settle 203.53 @ 2026-07-13; ret -2.89%; alpha -2.34%; MISS; IN_CI; z -0.38 | USD/% | 2026-07-13 | Nasdaq hist API (L002); convention L017 | DELAYED | DERIVED | 02,15 |
| L035 | 02 | settlement | AAPL (2026-06-16 gpt-5) | settle 317.31 @ 2026-07-13; ret +6.50%; alpha +7.06%; HIT; IN_CI; z 0.82 | USD/% | 2026-07-13 | Nasdaq hist API (L002); convention L017 | DELAYED | DERIVED | 02,15 |
| L036 | 02 | settlement | PLD (2026-06-16 gpt-5) | settle 142.16 @ 2026-07-13; ret -2.58%; alpha -2.03%; MISS; IN_CI; z -0.59 | USD/% | 2026-07-13 | Nasdaq hist API (L002); convention L017 | DELAYED | DERIVED | 02,15 |
| L037 | 02 | settlement | AVGO (2026-06-16 gpt-5) | settle 384.05 @ 2026-07-13; ret +0.09%; alpha +0.64%; HIT; IN_CI; z -0.05 | USD/% | 2026-07-13 | Nasdaq hist API (L002); convention L017 | DELAYED | DERIVED | 02,15 |
| L038 | 02 | settlement | SPY (2026-06-16 gpt-5) | settle 749.17 @ 2026-07-13; ret -0.55%; alpha N/A; MISS; IN_CI; z -0.66 | USD/% | 2026-07-13 | Nasdaq hist API (L002); convention L017 | DELAYED | DERIVED | 02,15 |
| L039 | 02 | settlement | QQQ (2026-06-16 gpt-5) | settle 711.74 @ 2026-07-13; ret -3.50%; alpha N/A; MISS; OUT_CI_LOW; z -1.11 | USD/% | 2026-07-13 | Nasdaq hist API (L002); convention L017 | DELAYED | DERIVED | 02,15 |
| L040 | 02 | settlement | SOXX (2026-06-16 gpt-5) | settle 553.61 @ 2026-07-13; ret -9.66%; alpha N/A; MISS; IN_CI; z -0.92 | USD/% | 2026-07-13 | Nasdaq hist API (L002); convention L017 | DELAYED | DERIVED | 02,15 |
| L041 | 02 | mom_price | MCK | 790.22 (2026-06-10) -> 812.28 (2026-07-13); MoM +2.79%; alpha -0.48% | USD/% | 2026-07-13 | prior: baseline pkg 06-10; current: L002 | DELAYED | DERIVED | 02 |
| L042 | 02 | mom_price | COST | 980.45 (2026-06-10) -> 926.43 (2026-07-13); MoM -5.51%; alpha -8.78% | USD/% | 2026-07-13 | prior: baseline pkg 06-10; current: L002 | DELAYED | DERIVED | 02 |
| L043 | 02 | mom_price | WMT | 119.83 (2026-06-10) -> 114.78 (2026-07-13); MoM -4.21%; alpha -7.49% | USD/% | 2026-07-13 | prior: baseline pkg 06-10; current: L002 | DELAYED | DERIVED | 02 |
| L044 | 02 | mom_price | CVX | 191.01 (2026-06-10) -> 182.2 (2026-07-13); MoM -4.61%; alpha -7.88% | USD/% | 2026-07-13 | prior: baseline pkg 06-10; current: L002 | DELAYED | DERIVED | 02 |
| L045 | 02 | mom_price | UNH | 407.13 (2026-06-10) -> 429.09 (2026-07-13); MoM +5.39%; alpha +2.12% | USD/% | 2026-07-13 | prior: baseline pkg 06-10; current: L002 | DELAYED | DERIVED | 02 |
| L046 | 02 | mom_price | MU | 891.66 (2026-06-10) -> 937.0 (2026-07-13); MoM +5.08%; alpha +1.81% | USD/% | 2026-07-13 | prior: baseline pkg 06-10; current: L002 | DELAYED | DERIVED | 02 |
| L047 | 02 | mom_price | XOM | 151.35 (2026-06-10) -> 144.51 (2026-07-13); MoM -4.52%; alpha -7.79% | USD/% | 2026-07-13 | prior: baseline pkg 06-10; current: L002 | DELAYED | DERIVED | 02 |
| L048 | 02 | mom_price | LIN | 509.2 (2026-06-10) -> 524.06 (2026-07-13); MoM +2.92%; alpha -0.35% | USD/% | 2026-07-13 | prior: baseline pkg 06-10; current: L002 | DELAYED | DERIVED | 02 |
| L049 | 02 | mom_price | LLY | 1138.16 (2026-06-10) -> 1181.87 (2026-07-13); MoM +3.84%; alpha +0.57% | USD/% | 2026-07-13 | prior: baseline pkg 06-10; current: L002 | DELAYED | DERIVED | 02 |
| L050 | 02 | mom_price | NVDA | 201.65 (2026-06-10) -> 203.53 (2026-07-13); MoM +0.93%; alpha -2.34% | USD/% | 2026-07-13 | prior: baseline pkg 06-10; current: L002 | DELAYED | DERIVED | 02 |
| L051 | 02 | mom_price | GOOGL | 356.64 (2026-06-10) -> 352.51 (2026-07-13); MoM -1.16%; alpha -4.43% | USD/% | 2026-07-13 | prior: baseline pkg 06-10; current: L002 | DELAYED | DERIVED | 02 |
| L052 | 02 | mom_price | ABBV | 225.82 (2026-06-10) -> 248.0 (2026-07-13); MoM +9.82%; alpha +6.55% | USD/% | 2026-07-13 | prior: baseline pkg 06-10; current: L002 | DELAYED | DERIVED | 02 |
| L053 | 05 | entry_price | DVA | 235.58 | USD | 2026-07-13 | Nasdaq historical API (bulk, retrieved this run; L002) | DELAYED | OBSERVED | 02,05,06,15 |
| L054 | 05 | price_history/indicators | DVA | 5y daily bars (last 2026-07-13); D/W/M pack | series | 2026-07-13 | L002 CSV + technical_indicators.py (L003) | DELAYED | OBSERVED | 05 |
| L055 | 05 | sigma_1m | DVA | 6.98% | 1m return sd | 2026-07-13 | REALIZED_VOL_30D: stdev(daily ret, 30d) x sqrt(21) from L054 | DELAYED | DERIVED | 05,15 |
| L056 | 05 | beta_60d | DVA | 0.585 | x | 2026-07-13 | 60d daily-return regression vs SPY (L004, L054) | DELAYED | DERIVED | 05 |
| L057 | 05 | next_earnings | DVA | 21d (confirmed) | date | 2026-07-14 | api.nasdaq.com/api/analyst earnings-date fetch (L015) | DELAYED | OBSERVED | 05 |
| L058 | 05 | metrics_pack | DVA | Sharpe 0.67, Sortino 0.73, IR 0.31, kraw 10.26, k025 0.05, VaR95 -6.5%, CVaR95 -9.4%, maxDD60 -6.31% | pack | 2026-07-13 | formulas rules.md §Ratio Definitions; inputs L053-L056, L008 | DELAYED | DERIVED | 05,07 |
| L059 | 05 | score_trace | DVA | (0.30*0.00+0.30*+1.67+0.25*0.00+0.15*+1.00)*0.80-0.05=+0.470; pctl 100.0; mu +5.0% (band -1pp exhaustion) | trace | 2026-07-14 | family z L021; DQ L020; penalties L022/L023; mu table rules.md | DELAYED | DERIVED | 05,06,15 |
| L060 | 05 | entry_price | BAX | 22.57 | USD | 2026-07-13 | Nasdaq historical API (bulk, retrieved this run; L002) | DELAYED | OBSERVED | 02,05,06,15 |
| L061 | 05 | price_history/indicators | BAX | 5y daily bars (last 2026-07-13); D/W/M pack | series | 2026-07-13 | L002 CSV + technical_indicators.py (L003) | DELAYED | OBSERVED | 05 |
| L062 | 05 | sigma_1m | BAX | 11.12% | 1m return sd | 2026-07-13 | REALIZED_VOL_30D: stdev(daily ret, 30d) x sqrt(21) from L061 | DELAYED | DERIVED | 05,15 |
| L063 | 05 | beta_60d | BAX | 0.467 | x | 2026-07-13 | 60d daily-return regression vs SPY (L004, L061) | DELAYED | DERIVED | 05 |
| L064 | 05 | next_earnings | BAX | 16d (confirmed) | date | 2026-07-14 | api.nasdaq.com/api/analyst earnings-date fetch (L015) | DELAYED | OBSERVED | 05 |
| L065 | 05 | metrics_pack | BAX | Sharpe 0.42, Sortino 0.41, IR 0.43, kraw 4.04, k025 0.05, VaR95 -13.3%, CVaR95 -17.9%, maxDD60 -11.78% | pack | 2026-07-13 | formulas rules.md §Ratio Definitions; inputs L060-L063, L008 | DELAYED | DERIVED | 05,07 |
| L066 | 05 | score_trace | BAX | (0.30*0.00+0.30*+1.45+0.25*0.00+0.15*+0.39)*0.80-0.05=+0.345; pctl 99.8; mu +5.0% (band -1pp exhaustion) | trace | 2026-07-14 | family z L021; DQ L020; penalties L022/L023; mu table rules.md | DELAYED | DERIVED | 05,06,15 |
| L067 | 05 | entry_price | CRL | 229.75 | USD | 2026-07-13 | Nasdaq historical API (bulk, retrieved this run; L002) | DELAYED | OBSERVED | 02,05,06,15 |
| L068 | 05 | price_history/indicators | CRL | 5y daily bars (last 2026-07-13); D/W/M pack | series | 2026-07-13 | L002 CSV + technical_indicators.py (L003) | DELAYED | OBSERVED | 05 |
| L069 | 05 | sigma_1m | CRL | 11.95% | 1m return sd | 2026-07-13 | REALIZED_VOL_30D: stdev(daily ret, 30d) x sqrt(21) from L068 | DELAYED | DERIVED | 05,15 |
| L070 | 05 | beta_60d | CRL | 1.05 | x | 2026-07-13 | 60d daily-return regression vs SPY (L004, L068) | DELAYED | DERIVED | 05 |
| L071 | 05 | next_earnings | CRL | 22d (confirmed) | date | 2026-07-14 | api.nasdaq.com/api/analyst earnings-date fetch (L015) | DELAYED | OBSERVED | 05 |
| L072 | 05 | metrics_pack | CRL | Sharpe 0.39, Sortino 0.35, IR 0.31, kraw 3.5, k025 0.05, VaR95 -14.7%, CVaR95 -19.6%, maxDD60 -19.19% | pack | 2026-07-13 | formulas rules.md §Ratio Definitions; inputs L067-L070, L008 | DELAYED | DERIVED | 05,07 |
| L073 | 05 | score_trace | CRL | (0.30*0.00+0.30*+1.51+0.25*0.00+0.15*+0.26)*0.80-0.05=+0.344; pctl 99.6; mu +5.0% (band -1pp exhaustion) | trace | 2026-07-14 | family z L021; DQ L020; penalties L022/L023; mu table rules.md | DELAYED | DERIVED | 05,06,15 |
| L074 | 05 | entry_price | FTNT | 160.62 | USD | 2026-07-13 | Nasdaq historical API (bulk, retrieved this run; L002) | DELAYED | OBSERVED | 02,05,06,15 |
| L075 | 05 | price_history/indicators | FTNT | 5y daily bars (last 2026-07-13); D/W/M pack | series | 2026-07-13 | L002 CSV + technical_indicators.py (L003) | DELAYED | OBSERVED | 05 |
| L076 | 05 | sigma_1m | FTNT | 12.79% | 1m return sd | 2026-07-13 | REALIZED_VOL_30D: stdev(daily ret, 30d) x sqrt(21) from L075 | DELAYED | DERIVED | 05,15 |
| L077 | 05 | beta_60d | FTNT | 0.844 | x | 2026-07-13 | 60d daily-return regression vs SPY (L004, L075) | DELAYED | DERIVED | 05 |
| L078 | 05 | next_earnings | FTNT | 15d (confirmed) | date | 2026-07-14 | api.nasdaq.com/api/analyst earnings-date fetch (L015) | DELAYED | OBSERVED | 05 |
| L079 | 05 | metrics_pack | FTNT | Sharpe 0.37, Sortino 0.41, IR 0.29, kraw 3.06, k025 0.05, VaR95 -16.1%, CVaR95 -21.3%, maxDD60 -7.54% | pack | 2026-07-13 | formulas rules.md §Ratio Definitions; inputs L074-L077, L008 | DELAYED | DERIVED | 05,07 |
| L080 | 05 | score_trace | FTNT | (0.30*0.00+0.30*+1.25+0.25*0.00+0.15*+0.66)*0.80-0.05=+0.329; pctl 99.4; mu +5.0% (band -1pp exhaustion) | trace | 2026-07-14 | family z L021; DQ L020; penalties L022/L023; mu table rules.md | DELAYED | DERIVED | 05,06,15 |
| L081 | 05 | entry_price | ABNB | 146.33 | USD | 2026-07-13 | Nasdaq historical API (bulk, retrieved this run; L002) | DELAYED | OBSERVED | 02,05,06,15 |
| L082 | 05 | price_history/indicators | ABNB | 5y daily bars (last 2026-07-13); D/W/M pack | series | 2026-07-13 | L002 CSV + technical_indicators.py (L003) | DELAYED | OBSERVED | 05 |
| L083 | 05 | sigma_1m | ABNB | 9.76% | 1m return sd | 2026-07-13 | REALIZED_VOL_30D: stdev(daily ret, 30d) x sqrt(21) from L082 | DELAYED | DERIVED | 05,15 |
| L084 | 05 | beta_60d | ABNB | 0.79 | x | 2026-07-13 | 60d daily-return regression vs SPY (L004, L082) | DELAYED | DERIVED | 05 |
| L085 | 05 | next_earnings | ABNB | 23d (confirmed) | date | 2026-07-14 | api.nasdaq.com/api/analyst earnings-date fetch (L015) | DELAYED | OBSERVED | 05 |
| L086 | 05 | metrics_pack | ABNB | Sharpe 0.58, Sortino 0.7, IR 0.71, kraw 6.3, k025 0.05, VaR95 -10.1%, CVaR95 -14.1%, maxDD60 -10.46% | pack | 2026-07-13 | formulas rules.md §Ratio Definitions; inputs L081-L084, L008 | DELAYED | DERIVED | 05,07 |
| L087 | 05 | score_trace | ABNB | (0.30*0.00+0.30*+0.99+0.25*0.00+0.15*+0.73)*0.80-0.00=+0.326; pctl 99.2; mu +6.0% (band) | trace | 2026-07-14 | family z L021; DQ L020; penalties L022/L023; mu table rules.md | DELAYED | DERIVED | 05,06,15 |
| L088 | 05 | entry_price | DOC | 21.73 | USD | 2026-07-13 | Nasdaq historical API (bulk, retrieved this run; L002) | DELAYED | OBSERVED | 02,05,06,15 |
| L089 | 05 | price_history/indicators | DOC | 5y daily bars (last 2026-07-13); D/W/M pack | series | 2026-07-13 | L002 CSV + technical_indicators.py (L003) | DELAYED | OBSERVED | 05 |
| L090 | 05 | sigma_1m | DOC | 7.59% | 1m return sd | 2026-07-13 | REALIZED_VOL_30D: stdev(daily ret, 30d) x sqrt(21) from L089 | DELAYED | DERIVED | 05,15 |
| L091 | 05 | beta_60d | DOC | 0.696 | x | 2026-07-13 | 60d daily-return regression vs SPY (L004, L089) | DELAYED | DERIVED | 05 |
| L092 | 05 | next_earnings | DOC | 21d (confirmed) | date | 2026-07-14 | api.nasdaq.com/api/analyst earnings-date fetch (L015) | DELAYED | OBSERVED | 05 |
| L093 | 05 | metrics_pack | DOC | Sharpe 0.75, Sortino 0.85, IR 0.46, kraw 10.42, k025 0.05, VaR95 -6.5%, CVaR95 -9.6%, maxDD60 -7.94% | pack | 2026-07-13 | formulas rules.md §Ratio Definitions; inputs L088-L091, L008 | DELAYED | DERIVED | 05,07 |
| L094 | 05 | score_trace | DOC | (0.30*0.00+0.30*+0.86+0.25*0.00+0.15*+0.94)*0.80-0.00=+0.321; pctl 99.0; mu +6.0% (band) | trace | 2026-07-14 | family z L021; DQ L020; penalties L022/L023; mu table rules.md | DELAYED | DERIVED | 05,06,15 |
| L095 | 05 | entry_price | HUM | 406.0 | USD | 2026-07-13 | Nasdaq historical API (bulk, retrieved this run; L002) | DELAYED | OBSERVED | 02,05,06,15 |
| L096 | 05 | price_history/indicators | HUM | 5y daily bars (last 2026-07-13); D/W/M pack | series | 2026-07-13 | L002 CSV + technical_indicators.py (L003) | DELAYED | OBSERVED | 05 |
| L097 | 05 | sigma_1m | HUM | 11.13% | 1m return sd | 2026-07-13 | REALIZED_VOL_30D: stdev(daily ret, 30d) x sqrt(21) from L096 | DELAYED | DERIVED | 05,15 |
| L098 | 05 | beta_60d | HUM | 0.115 | x | 2026-07-13 | 60d daily-return regression vs SPY (L004, L096) | DELAYED | DERIVED | 05 |
| L099 | 05 | next_earnings | HUM | 15d (confirmed) | date | 2026-07-14 | api.nasdaq.com/api/analyst earnings-date fetch (L015) | DELAYED | OBSERVED | 05 |
| L100 | 05 | metrics_pack | HUM | Sharpe 0.42, Sortino 0.59, IR 0.4, kraw 4.04, k025 0.05, VaR95 -13.4%, CVaR95 -17.9%, maxDD60 -5.56% | pack | 2026-07-13 | formulas rules.md §Ratio Definitions; inputs L095-L098, L008 | DELAYED | DERIVED | 05,07 |
| L101 | 05 | score_trace | HUM | (0.30*0.00+0.30*+1.30+0.25*0.00+0.15*+0.45)*0.80-0.05=+0.316; pctl 98.8; mu +5.0% (band -1pp exhaustion) | trace | 2026-07-14 | family z L021; DQ L020; penalties L022/L023; mu table rules.md | DELAYED | DERIVED | 05,06,15 |
| L102 | 05 | entry_price | EXPD | 175.5 | USD | 2026-07-13 | Nasdaq historical API (bulk, retrieved this run; L002) | DELAYED | OBSERVED | 02,05,06,15 |
| L103 | 05 | price_history/indicators | EXPD | 5y daily bars (last 2026-07-13); D/W/M pack | series | 2026-07-13 | L002 CSV + technical_indicators.py (L003) | DELAYED | OBSERVED | 05 |
| L104 | 05 | sigma_1m | EXPD | 6.0% | 1m return sd | 2026-07-13 | REALIZED_VOL_30D: stdev(daily ret, 30d) x sqrt(21) from L103 | DELAYED | DERIVED | 05,15 |
| L105 | 05 | beta_60d | EXPD | 0.215 | x | 2026-07-13 | 60d daily-return regression vs SPY (L004, L103) | DELAYED | DERIVED | 05 |
| L106 | 05 | next_earnings | EXPD | 21d (confirmed) | date | 2026-07-14 | api.nasdaq.com/api/analyst earnings-date fetch (L015) | DELAYED | OBSERVED | 05 |
| L107 | 05 | metrics_pack | EXPD | Sharpe 0.78, Sortino 0.65, IR 0.58, kraw 13.89, k025 0.05, VaR95 -4.9%, CVaR95 -7.4%, maxDD60 -7.46% | pack | 2026-07-13 | formulas rules.md §Ratio Definitions; inputs L102-L105, L008 | DELAYED | DERIVED | 05,07 |
| L108 | 05 | score_trace | EXPD | (0.30*0.00+0.30*+1.09+0.25*0.00+0.15*+0.81)*0.80-0.05=+0.309; pctl 98.6; mu +5.0% (band -1pp exhaustion) | trace | 2026-07-14 | family z L021; DQ L020; penalties L022/L023; mu table rules.md | DELAYED | DERIVED | 05,06,15 |
| L109 | 05 | entry_price | KMB | 110.18 | USD | 2026-07-13 | Nasdaq historical API (bulk, retrieved this run; L002) | DELAYED | OBSERVED | 02,05,06,15 |
| L110 | 05 | price_history/indicators | KMB | 5y daily bars (last 2026-07-13); D/W/M pack | series | 2026-07-13 | L002 CSV + technical_indicators.py (L003) | DELAYED | OBSERVED | 05 |
| L111 | 05 | sigma_1m | KMB | 9.12% | 1m return sd | 2026-07-13 | REALIZED_VOL_30D: stdev(daily ret, 30d) x sqrt(21) from L110 | DELAYED | DERIVED | 05,15 |
| L112 | 05 | beta_60d | KMB | -0.126 | x | 2026-07-13 | 60d daily-return regression vs SPY (L004, L110) | DELAYED | DERIVED | 05 |
| L113 | 05 | next_earnings | KMB | 21d (confirmed) | date | 2026-07-14 | api.nasdaq.com/api/analyst earnings-date fetch (L015) | DELAYED | OBSERVED | 05 |
| L114 | 05 | metrics_pack | KMB | Sharpe 0.62, Sortino 0.77, IR 0.79, kraw 7.21, k025 0.05, VaR95 -9.0%, CVaR95 -12.8%, maxDD60 -5.7% | pack | 2026-07-13 | formulas rules.md §Ratio Definitions; inputs L109-L112, L008 | DELAYED | DERIVED | 05,07 |
| L115 | 05 | score_trace | KMB | (0.30*0.00+0.30*+1.04+0.25*0.00+0.15*+0.46)*0.80-0.00=+0.305; pctl 98.4; mu +6.0% (band) | trace | 2026-07-14 | family z L021; DQ L020; penalties L022/L023; mu table rules.md | DELAYED | DERIVED | 05,06,15 |
| L116 | 05 | entry_price | CVS | 105.9 | USD | 2026-07-13 | Nasdaq historical API (bulk, retrieved this run; L002) | DELAYED | OBSERVED | 02,05,06,15 |
| L117 | 05 | price_history/indicators | CVS | 5y daily bars (last 2026-07-13); D/W/M pack | series | 2026-07-13 | L002 CSV + technical_indicators.py (L003) | DELAYED | OBSERVED | 05 |
| L118 | 05 | sigma_1m | CVS | 7.16% | 1m return sd | 2026-07-13 | REALIZED_VOL_30D: stdev(daily ret, 30d) x sqrt(21) from L117 | DELAYED | DERIVED | 05,15 |
| L119 | 05 | beta_60d | CVS | -0.116 | x | 2026-07-13 | 60d daily-return regression vs SPY (L004, L117) | DELAYED | DERIVED | 05 |
| L120 | 05 | next_earnings | CVS | 22d (confirmed) | date | 2026-07-14 | api.nasdaq.com/api/analyst earnings-date fetch (L015) | DELAYED | OBSERVED | 05 |
| L121 | 05 | metrics_pack | CVS | Sharpe 0.65, Sortino 0.79, IR 0.57, kraw 9.75, k025 0.05, VaR95 -6.8%, CVaR95 -9.7%, maxDD60 -8.78% | pack | 2026-07-13 | formulas rules.md §Ratio Definitions; inputs L116-L119, L008 | DELAYED | DERIVED | 05,07 |
| L122 | 05 | score_trace | CVS | (0.30*0.00+0.30*+1.24+0.25*0.00+0.15*+0.48)*0.80-0.05=+0.304; pctl 98.2; mu +5.0% (band -1pp exhaustion) | trace | 2026-07-14 | family z L021; DQ L020; penalties L022/L023; mu table rules.md | DELAYED | DERIVED | 05,06,15 |
| L123 | 05 | entry_price | TROW | 113.65 | USD | 2026-07-13 | Nasdaq historical API (bulk, retrieved this run; L002) | DELAYED | OBSERVED | 02,05,06,15 |
| L124 | 05 | price_history/indicators | TROW | 5y daily bars (last 2026-07-13); D/W/M pack | series | 2026-07-13 | L002 CSV + technical_indicators.py (L003) | DELAYED | OBSERVED | 05 |
| L125 | 05 | sigma_1m | TROW | 7.48% | 1m return sd | 2026-07-13 | REALIZED_VOL_30D: stdev(daily ret, 30d) x sqrt(21) from L124 | DELAYED | DERIVED | 05,15 |
| L126 | 05 | beta_60d | TROW | 0.583 | x | 2026-07-13 | 60d daily-return regression vs SPY (L004, L124) | DELAYED | DERIVED | 05 |
| L127 | 05 | next_earnings | TROW | 17d (confirmed) | date | 2026-07-14 | api.nasdaq.com/api/analyst earnings-date fetch (L015) | DELAYED | OBSERVED | 05 |
| L128 | 05 | metrics_pack | TROW | Sharpe 0.63, Sortino 0.81, IR 0.78, kraw 8.94, k025 0.05, VaR95 -7.3%, CVaR95 -10.4%, maxDD60 -5.42% | pack | 2026-07-13 | formulas rules.md §Ratio Definitions; inputs L123-L126, L008 | DELAYED | DERIVED | 05,07 |
| L129 | 05 | score_trace | TROW | (0.30*0.00+0.30*+0.95+0.25*0.00+0.15*+0.99)*0.80-0.05=+0.298; pctl 98.1; mu +5.0% (band -1pp exhaustion) | trace | 2026-07-14 | family z L021; DQ L020; penalties L022/L023; mu table rules.md | DELAYED | DERIVED | 05,06,15 |
| L130 | 05 | entry_price | BBY | 81.65 | USD | 2026-07-13 | Nasdaq historical API (bulk, retrieved this run; L002) | DELAYED | OBSERVED | 02,05,06,15 |
| L131 | 05 | price_history/indicators | BBY | 5y daily bars (last 2026-07-13); D/W/M pack | series | 2026-07-13 | L002 CSV + technical_indicators.py (L003) | DELAYED | OBSERVED | 05 |
| L132 | 05 | sigma_1m | BBY | 9.78% | 1m return sd | 2026-07-13 | REALIZED_VOL_30D: stdev(daily ret, 30d) x sqrt(21) from L131 | DELAYED | DERIVED | 05,15 |
| L133 | 05 | beta_60d | BBY | 0.599 | x | 2026-07-13 | 60d daily-return regression vs SPY (L004, L131) | DELAYED | DERIVED | 05 |
| L134 | 05 | next_earnings | BBY | 44d (confirmed) | date | 2026-07-14 | api.nasdaq.com/api/analyst earnings-date fetch (L015) | DELAYED | OBSERVED | 05 |
| L135 | 05 | metrics_pack | BBY | Sharpe 0.48, Sortino 0.48, IR 0.35, kraw 5.23, k025 0.05, VaR95 -11.1%, CVaR95 -15.1%, maxDD60 -17.06% | pack | 2026-07-13 | formulas rules.md §Ratio Definitions; inputs L130-L133, L008 | DELAYED | DERIVED | 05,07 |
| L136 | 05 | score_trace | BBY | (0.30*0.00+0.30*+1.27+0.25*0.00+0.15*+0.34)*0.80-0.05=+0.296; pctl 97.9; mu +5.0% (band -1pp exhaustion) | trace | 2026-07-14 | family z L021; DQ L020; penalties L022/L023; mu table rules.md | DELAYED | DERIVED | 05,06,15 |
| L137 | 05 | entry_price | BEN | 32.83 | USD | 2026-07-13 | Nasdaq historical API (bulk, retrieved this run; L002) | DELAYED | OBSERVED | 02,05,06,15 |
| L138 | 05 | price_history/indicators | BEN | 5y daily bars (last 2026-07-13); D/W/M pack | series | 2026-07-13 | L002 CSV + technical_indicators.py (L003) | DELAYED | OBSERVED | 05 |
| L139 | 05 | sigma_1m | BEN | 8.31% | 1m return sd | 2026-07-13 | REALIZED_VOL_30D: stdev(daily ret, 30d) x sqrt(21) from L138 | DELAYED | DERIVED | 05,15 |
| L140 | 05 | beta_60d | BEN | 0.905 | x | 2026-07-13 | 60d daily-return regression vs SPY (L004, L138) | DELAYED | DERIVED | 05 |
| L141 | 05 | next_earnings | BEN | 17d (confirmed) | date | 2026-07-14 | api.nasdaq.com/api/analyst earnings-date fetch (L015) | DELAYED | OBSERVED | 05 |
| L142 | 05 | metrics_pack | BEN | Sharpe 0.68, Sortino 0.7, IR 0.69, kraw 8.69, k025 0.05, VaR95 -7.7%, CVaR95 -11.1%, maxDD60 -6.12% | pack | 2026-07-13 | formulas rules.md §Ratio Definitions; inputs L137-L140, L008 | DELAYED | DERIVED | 05,07 |
| L143 | 05 | score_trace | BEN | (0.30*0.00+0.30*+0.69+0.25*0.00+0.15*+1.08)*0.80-0.00=+0.296; pctl 97.7; mu +6.0% (band) | trace | 2026-07-14 | family z L021; DQ L020; penalties L022/L023; mu table rules.md | DELAYED | DERIVED | 05,06,15 |
| L144 | 05 | entry_price | PANW | 330.3 | USD | 2026-07-13 | Nasdaq historical API (bulk, retrieved this run; L002) | DELAYED | OBSERVED | 02,05,06,15 |
| L145 | 05 | price_history/indicators | PANW | 5y daily bars (last 2026-07-13); D/W/M pack | series | 2026-07-13 | L002 CSV + technical_indicators.py (L003) | DELAYED | OBSERVED | 05 |
| L146 | 05 | sigma_1m | PANW | 17.67% | 1m return sd | 2026-07-13 | REALIZED_VOL_30D: stdev(daily ret, 30d) x sqrt(21) from L145 | DELAYED | DERIVED | 05,15 |
| L147 | 05 | beta_60d | PANW | 1.497 | x | 2026-07-13 | 60d daily-return regression vs SPY (L004, L145) | DELAYED | DERIVED | 05 |
| L148 | 05 | next_earnings | PANW | 34d (confirmed) | date | 2026-07-14 | api.nasdaq.com/api/analyst earnings-date fetch (L015) | DELAYED | OBSERVED | 05 |
| L149 | 05 | metrics_pack | PANW | Sharpe 0.27, Sortino 0.36, IR 0.3, kraw 1.6, k025 0.05, VaR95 -24.2%, CVaR95 -31.4%, maxDD60 -13.3% | pack | 2026-07-13 | formulas rules.md §Ratio Definitions; inputs L144-L147, L008 | DELAYED | DERIVED | 05,07 |
| L150 | 05 | score_trace | PANW | (0.30*0.00+0.30*+1.51+0.25*0.00+0.15*-0.15)*0.80-0.05=+0.294; pctl 97.5; mu +5.0% (band -1pp exhaustion) | trace | 2026-07-14 | family z L021; DQ L020; penalties L022/L023; mu table rules.md | DELAYED | DERIVED | 05,06,15 |
| L151 | 05 | entry_price | ADP | 251.05 | USD | 2026-07-13 | Nasdaq historical API (bulk, retrieved this run; L002) | DELAYED | OBSERVED | 02,05,06,15 |
| L152 | 05 | price_history/indicators | ADP | 5y daily bars (last 2026-07-13); D/W/M pack | series | 2026-07-13 | L002 CSV + technical_indicators.py (L003) | DELAYED | OBSERVED | 05 |
| L153 | 05 | sigma_1m | ADP | 9.41% | 1m return sd | 2026-07-13 | REALIZED_VOL_30D: stdev(daily ret, 30d) x sqrt(21) from L152 | DELAYED | DERIVED | 05,15 |
| L154 | 05 | beta_60d | ADP | -0.668 | x | 2026-07-13 | 60d daily-return regression vs SPY (L004, L152) | DELAYED | DERIVED | 05 |
| L155 | 05 | next_earnings | ADP | 15d (confirmed) | date | 2026-07-14 | api.nasdaq.com/api/analyst earnings-date fetch (L015) | DELAYED | OBSERVED | 05 |
| L156 | 05 | metrics_pack | ADP | Sharpe 0.6, Sortino 0.95, IR 0.68, kraw 6.78, k025 0.05, VaR95 -9.5%, CVaR95 -13.4%, maxDD60 -8.19% | pack | 2026-07-13 | formulas rules.md §Ratio Definitions; inputs L151-L154, L008 | DELAYED | DERIVED | 05,07 |
| L157 | 05 | score_trace | ADP | (0.30*0.00+0.30*+1.21+0.25*0.00+0.15*+0.02)*0.80-0.00=+0.293; pctl 97.3; mu +6.0% (band) | trace | 2026-07-14 | family z L021; DQ L020; penalties L022/L023; mu table rules.md | DELAYED | DERIVED | 05,06,15 |
| L158 | 05 | entry_price | MPC | 296.88 | USD | 2026-07-13 | Nasdaq historical API (bulk, retrieved this run; L002) | DELAYED | OBSERVED | 02,05,06,15 |
| L159 | 05 | price_history/indicators | MPC | 5y daily bars (last 2026-07-13); D/W/M pack | series | 2026-07-13 | L002 CSV + technical_indicators.py (L003) | DELAYED | OBSERVED | 05 |
| L160 | 05 | sigma_1m | MPC | 10.16% | 1m return sd | 2026-07-13 | REALIZED_VOL_30D: stdev(daily ret, 30d) x sqrt(21) from L159 | DELAYED | DERIVED | 05,15 |
| L161 | 05 | beta_60d | MPC | -0.658 | x | 2026-07-13 | 60d daily-return regression vs SPY (L004, L159) | DELAYED | DERIVED | 05 |
| L162 | 05 | next_earnings | MPC | 21d (confirmed) | date | 2026-07-14 | api.nasdaq.com/api/analyst earnings-date fetch (L015) | DELAYED | OBSERVED | 05 |
| L163 | 05 | metrics_pack | MPC | Sharpe 0.46, Sortino 0.42, IR 0.51, kraw 4.84, k025 0.05, VaR95 -11.8%, CVaR95 -15.9%, maxDD60 -9.09% | pack | 2026-07-13 | formulas rules.md §Ratio Definitions; inputs L158-L161, L008 | DELAYED | DERIVED | 05,07 |
| L164 | 05 | score_trace | MPC | (0.30*0.00+0.30*+1.47+0.25*0.00+0.15*-0.07)*0.80-0.05=+0.293; pctl 97.1; mu +5.0% (band -1pp exhaustion) | trace | 2026-07-14 | family z L021; DQ L020; penalties L022/L023; mu table rules.md | DELAYED | DERIVED | 05,06,15 |
| L165 | 05 | entry_price | ESS | 297.48 | USD | 2026-07-13 | Nasdaq historical API (bulk, retrieved this run; L002) | DELAYED | OBSERVED | 02,05,06,15 |
| L166 | 05 | price_history/indicators | ESS | 5y daily bars (last 2026-07-13); D/W/M pack | series | 2026-07-13 | L002 CSV + technical_indicators.py (L003) | DELAYED | OBSERVED | 05 |
| L167 | 05 | sigma_1m | ESS | 5.85% | 1m return sd | 2026-07-13 | REALIZED_VOL_30D: stdev(daily ret, 30d) x sqrt(21) from L166 | DELAYED | DERIVED | 05,15 |
| L168 | 05 | beta_60d | ESS | -0.136 | x | 2026-07-13 | 60d daily-return regression vs SPY (L004, L166) | DELAYED | DERIVED | 05 |
| L169 | 05 | next_earnings | ESS | 15d (confirmed) | date | 2026-07-14 | api.nasdaq.com/api/analyst earnings-date fetch (L015) | DELAYED | OBSERVED | 05 |
| L170 | 05 | metrics_pack | ESS | Sharpe 0.97, Sortino 1.1, IR 1.03, kraw 17.53, k025 0.05, VaR95 -3.7%, CVaR95 -6.1%, maxDD60 -4.11% | pack | 2026-07-13 | formulas rules.md §Ratio Definitions; inputs L165-L168, L008 | DELAYED | DERIVED | 05,07 |
| L171 | 05 | score_trace | ESS | (0.30*0.00+0.30*+0.86+0.25*0.00+0.15*+0.71)*0.80-0.00=+0.290; pctl 96.9; mu +6.0% (band) | trace | 2026-07-14 | family z L021; DQ L020; penalties L022/L023; mu table rules.md | DELAYED | DERIVED | 05,06,15 |
| L172 | 05 | entry_price | FFIV | 420.95 | USD | 2026-07-13 | Nasdaq historical API (bulk, retrieved this run; L002) | DELAYED | OBSERVED | 02,05,06,15 |
| L173 | 05 | price_history/indicators | FFIV | 5y daily bars (last 2026-07-13); D/W/M pack | series | 2026-07-13 | L002 CSV + technical_indicators.py (L003) | DELAYED | OBSERVED | 05 |
| L174 | 05 | sigma_1m | FFIV | 8.64% | 1m return sd | 2026-07-13 | REALIZED_VOL_30D: stdev(daily ret, 30d) x sqrt(21) from L173 | DELAYED | DERIVED | 05,15 |
| L175 | 05 | beta_60d | FFIV | 0.826 | x | 2026-07-13 | 60d daily-return regression vs SPY (L004, L173) | DELAYED | DERIVED | 05 |
| L176 | 05 | next_earnings | FFIV | 13d (confirmed) | date | 2026-07-14 | api.nasdaq.com/api/analyst earnings-date fetch (L015) | DELAYED | OBSERVED | 05 |
| L177 | 05 | metrics_pack | FFIV | Sharpe 0.66, Sortino 0.68, IR 0.62, kraw 8.04, k025 0.05, VaR95 -8.3%, CVaR95 -11.8%, maxDD60 -5.95% | pack | 2026-07-13 | formulas rules.md §Ratio Definitions; inputs L172-L175, L008 | DELAYED | DERIVED | 05,07 |
| L178 | 05 | score_trace | FFIV | (0.30*0.00+0.30*+1.09+0.25*0.00+0.15*+1.02)*0.80-0.10=+0.285; pctl 96.7; mu +6.0% (band) | trace | 2026-07-14 | family z L021; DQ L020; penalties L022/L023; mu table rules.md | DELAYED | DERIVED | 05,06,15 |
| L179 | 05 | entry_price | DDOG | 260.24 | USD | 2026-07-13 | Nasdaq historical API (bulk, retrieved this run; L002) | DELAYED | OBSERVED | 02,05,06,15 |
| L180 | 05 | price_history/indicators | DDOG | 5y daily bars (last 2026-07-13); D/W/M pack | series | 2026-07-13 | L002 CSV + technical_indicators.py (L003) | DELAYED | OBSERVED | 05 |
| L181 | 05 | sigma_1m | DDOG | 18.56% | 1m return sd | 2026-07-13 | REALIZED_VOL_30D: stdev(daily ret, 30d) x sqrt(21) from L180 | DELAYED | DERIVED | 05,15 |
| L182 | 05 | beta_60d | DDOG | 0.426 | x | 2026-07-13 | 60d daily-return regression vs SPY (L004, L180) | DELAYED | DERIVED | 05 |
| L183 | 05 | next_earnings | DDOG | 23d (confirmed) | date | 2026-07-14 | api.nasdaq.com/api/analyst earnings-date fetch (L015) | DELAYED | OBSERVED | 05 |
| L184 | 05 | metrics_pack | DDOG | Sharpe 0.31, Sortino 0.53, IR 0.25, kraw 1.74, k025 0.05, VaR95 -24.6%, CVaR95 -32.2%, maxDD60 -20.51% | pack | 2026-07-13 | formulas rules.md §Ratio Definitions; inputs L179-L182, L008 | DELAYED | DERIVED | 05,07 |
| L185 | 05 | score_trace | DDOG | (0.30*0.00+0.30*+1.45+0.25*0.00+0.15*-0.57)*0.80-0.00=+0.281; pctl 96.5; mu +6.0% (band) | trace | 2026-07-14 | family z L021; DQ L020; penalties L022/L023; mu table rules.md | DELAYED | DERIVED | 05,06,15 |
| L186 | 05 | entry_price | LYV | 183.25 | USD | 2026-07-13 | Nasdaq historical API (bulk, retrieved this run; L002) | DELAYED | OBSERVED | 02,05,06,15 |
| L187 | 05 | price_history/indicators | LYV | 5y daily bars (last 2026-07-13); D/W/M pack | series | 2026-07-13 | L002 CSV + technical_indicators.py (L003) | DELAYED | OBSERVED | 05 |
| L188 | 05 | sigma_1m | LYV | 6.95% | 1m return sd | 2026-07-13 | REALIZED_VOL_30D: stdev(daily ret, 30d) x sqrt(21) from L187 | DELAYED | DERIVED | 05,15 |
| L189 | 05 | beta_60d | LYV | 0.628 | x | 2026-07-13 | 60d daily-return regression vs SPY (L004, L187) | DELAYED | DERIVED | 05 |
| L190 | 05 | next_earnings | LYV | 23d (confirmed) | date | 2026-07-14 | api.nasdaq.com/api/analyst earnings-date fetch (L015) | DELAYED | OBSERVED | 05 |
| L191 | 05 | metrics_pack | LYV | Sharpe 0.82, Sortino 0.97, IR 0.77, kraw 12.42, k025 0.05, VaR95 -5.5%, CVaR95 -8.3%, maxDD60 -6.42% | pack | 2026-07-13 | formulas rules.md §Ratio Definitions; inputs L186-L189, L008 | DELAYED | DERIVED | 05,07 |
| L192 | 05 | score_trace | LYV | (0.30*0.00+0.30*+0.66+0.25*0.00+0.15*+1.02)*0.80-0.00=+0.280; pctl 96.3; mu +6.0% (band) | trace | 2026-07-14 | family z L021; DQ L020; penalties L022/L023; mu table rules.md | DELAYED | DERIVED | 05,06,15 |
| L193 | 05 | entry_price | LLY | 1181.87 | USD | 2026-07-13 | Nasdaq historical API (bulk, retrieved this run; L002) | DELAYED | OBSERVED | 02,05,06,15 |
| L194 | 05 | price_history/indicators | LLY | 5y daily bars (last 2026-07-13); D/W/M pack | series | 2026-07-13 | L002 CSV + technical_indicators.py (L003) | DELAYED | OBSERVED | 05 |
| L195 | 05 | sigma_1m | LLY | 9.59% | 1m return sd | 2026-07-13 | REALIZED_VOL_30D: stdev(daily ret, 30d) x sqrt(21) from L194 | DELAYED | DERIVED | 05,15 |
| L196 | 05 | beta_60d | LLY | 0.172 | x | 2026-07-13 | 60d daily-return regression vs SPY (L004, L194) | DELAYED | DERIVED | 05 |
| L197 | 05 | next_earnings | LLY | 22d (confirmed) | date | 2026-07-14 | api.nasdaq.com/api/analyst earnings-date fetch (L015) | DELAYED | OBSERVED | 05 |
| L198 | 05 | metrics_pack | LLY | Sharpe 0.18, Sortino 0.23, IR 0.18, kraw 2.17, k025 0.05, VaR95 -13.8%, CVaR95 -17.8%, maxDD60 -8.18% | pack | 2026-07-13 | formulas rules.md §Ratio Definitions; inputs L193-L196, L008 | DELAYED | DERIVED | 05,07 |
| L199 | 05 | score_trace | LLY | (0.30*0.00+0.30*+0.67+0.25*0.00+0.15*+0.48)*0.80-0.05=+0.170; pctl 80.7; mu +2.0% (band -1pp exhaustion) | trace | 2026-07-14 | family z L021; DQ L020; penalties L022/L023; mu table rules.md | DELAYED | DERIVED | 05,06,15 |
| L200 | 05 | entry_price | ABBV | 248.0 | USD | 2026-07-13 | Nasdaq historical API (bulk, retrieved this run; L002) | DELAYED | OBSERVED | 02,05,06,15 |
| L201 | 05 | price_history/indicators | ABBV | 5y daily bars (last 2026-07-13); D/W/M pack | series | 2026-07-13 | L002 CSV + technical_indicators.py (L003) | DELAYED | OBSERVED | 05 |
| L202 | 05 | sigma_1m | ABBV | 9.62% | 1m return sd | 2026-07-13 | REALIZED_VOL_30D: stdev(daily ret, 30d) x sqrt(21) from L201 | DELAYED | DERIVED | 05,15 |
| L203 | 05 | beta_60d | ABBV | -0.628 | x | 2026-07-13 | 60d daily-return regression vs SPY (L004, L201) | DELAYED | DERIVED | 05 |
| L204 | 05 | next_earnings | ABBV | 17d (confirmed) | date | 2026-07-14 | api.nasdaq.com/api/analyst earnings-date fetch (L015) | DELAYED | OBSERVED | 05 |
| L205 | 05 | metrics_pack | ABBV | Sharpe 0.07, Sortino 0.11, IR 0.17, kraw 1.08, k025 0.05, VaR95 -14.9%, CVaR95 -18.8%, maxDD60 -5.56% | pack | 2026-07-13 | formulas rules.md §Ratio Definitions; inputs L200-L203, L008 | DELAYED | DERIVED | 05,07 |
| L206 | 05 | score_trace | ABBV | (0.30*0.00+0.30*+0.61+0.25*0.00+0.15*+0.14)*0.80-0.05=+0.113; pctl 69.2; mu +1.0% (band exhaustion -1pp suspended (band floor); floor at band min, exhaustion -1pp suspended (would zero mu)) | trace | 2026-07-14 | family z L021; DQ L020; penalties L022/L023; mu table rules.md | DELAYED | DERIVED | 05,06,15 |
| L207 | 05 | entry_price | LIN | 524.06 | USD | 2026-07-13 | Nasdaq historical API (bulk, retrieved this run; L002) | DELAYED | OBSERVED | 02,05,06,15 |
| L208 | 05 | price_history/indicators | LIN | 5y daily bars (last 2026-07-13); D/W/M pack | series | 2026-07-13 | L002 CSV + technical_indicators.py (L003) | DELAYED | OBSERVED | 05 |
| L209 | 05 | sigma_1m | LIN | 6.0% | 1m return sd | 2026-07-13 | REALIZED_VOL_30D: stdev(daily ret, 30d) x sqrt(21) from L208 | DELAYED | DERIVED | 05,15 |
| L210 | 05 | beta_60d | LIN | 0.109 | x | 2026-07-13 | 60d daily-return regression vs SPY (L004, L208) | DELAYED | DERIVED | 05 |
| L211 | 05 | next_earnings | LIN | 17d (confirmed) | date | 2026-07-14 | api.nasdaq.com/api/analyst earnings-date fetch (L015) | DELAYED | OBSERVED | 05 |
| L212 | 05 | metrics_pack | LIN | Sharpe 0.28, Sortino 0.36, IR 0.33, kraw 5.56, k025 0.05, VaR95 -7.9%, CVaR95 -10.4%, maxDD60 -4.19% | pack | 2026-07-13 | formulas rules.md §Ratio Definitions; inputs L207-L210, L008 | DELAYED | DERIVED | 05,07 |
| L213 | 05 | score_trace | LIN | (0.30*0.00+0.30*+0.08+0.25*0.00+0.15*+0.83)*0.80-0.00=+0.119; pctl 70.8; mu +2.0% (band) | trace | 2026-07-14 | family z L021; DQ L020; penalties L022/L023; mu table rules.md | DELAYED | DERIVED | 05,06,15 |
| L214 | 05 | entry_price | ANET | 181.15 | USD | 2026-07-13 | Nasdaq historical API (bulk, retrieved this run; L002) | DELAYED | OBSERVED | 02,05,06,15 |
| L215 | 05 | price_history/indicators | ANET | 5y daily bars (last 2026-07-13); D/W/M pack | series | 2026-07-13 | L002 CSV + technical_indicators.py (L003) | DELAYED | OBSERVED | 05 |
| L216 | 05 | sigma_1m | ANET | 18.73% | 1m return sd | 2026-07-13 | REALIZED_VOL_30D: stdev(daily ret, 30d) x sqrt(21) from L215 | DELAYED | DERIVED | 05,15 |
| L217 | 05 | beta_60d | ANET | 1.828 | x | 2026-07-13 | 60d daily-return regression vs SPY (L004, L215) | DELAYED | DERIVED | 05 |
| L218 | 05 | next_earnings | ANET | 21d (confirmed) | date | 2026-07-14 | api.nasdaq.com/api/analyst earnings-date fetch (L015) | DELAYED | OBSERVED | 05 |
| L219 | 05 | metrics_pack | ANET | Sharpe 0.25, Sortino 0.25, IR 0.24, kraw 1.43, k025 0.05, VaR95 -25.9%, CVaR95 -33.6%, maxDD60 -23.24% | pack | 2026-07-13 | formulas rules.md §Ratio Definitions; inputs L214-L217, L008 | DELAYED | DERIVED | 05,07 |
| L220 | 05 | score_trace | ANET | (0.30*0.00+0.30*+1.32+0.25*0.00+0.15*-0.84)*0.80-0.00=+0.216; pctl 90.3; mu +5.0% (band) | trace | 2026-07-14 | family z L021; DQ L020; penalties L022/L023; mu table rules.md | DELAYED | DERIVED | 05,06,15 |


## Coverage Summary (247 rows)

| claim_type | rows |
|---|---|
| OBSERVED | 58 (L001-L009, L015, L016, L019 + 24×2 per-name price/history rows) |
| DERIVED | 181 (ETF stats, RS, settlements, MoM, per-name sigma/beta/metrics/trace rows) |
| INFERRED | 4 (L014 regime, L017 convention, L020 DQ, L022 flag rule) |
| ILLUSTRATIVE | 0 |
| UNAVAILABLE (fields recorded as such) | Fund_Z/Sent_Z universe-wide; FDXF pack; Treynor (beta-quality caveat); isolated monthly-MA gaps |

Every price used downstream is DELAYED (2026-07-13 close) with retrieval timestamp 2026-07-14T17:07:39Z; settlement and entry prices satisfy the Price Sourcing Standard via market-data-tool verification (IBKR 13/13 exact) on top of the Nasdaq bulk source. Zero UNAVAILABLE Required fields.
