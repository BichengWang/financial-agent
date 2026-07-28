# 01 Preflight — Source Ledger — 2026-07-28

Published before downstream interpretation. Retrieval occurred on 2026-07-28; the price basis is the last completed session, 2026-07-27. All 20 published equities and SPY/QQQ/SOXX pass the two-independent-source ≤1% grounding gate (L002, L004–L006).

| Row | artifact | field | ticker/entity | value | unit | observation_date | source | freshness_tag | claim_type | used_by |
|---|---|---|---|---|---|---|---|---|---|---|
| L001 | 01_preflight.md | index-union universe | S&P 500 ∪ Nasdaq-100 | 515 tickers; 514 scored | count | 2026-07-27 | eligible_universe.txt; universe_summary.json | HISTORICAL | OBSERVED | 03,04,05 |
| L002 | 01_preflight.md | raw daily close | 518 symbols | 2026-07-27 raw close present for current-run validation | USD | 2026-07-27 | stockanalysis_history_manifest.json | HISTORICAL | OBSERVED | 02,03,05,06,15 |
| L003 | 01_preflight.md | adjusted daily close | 518 symbols | adjusted history through 2026-07-27 | USD | 2026-07-27 | stockanalysis_history_manifest.json adjusted field | HISTORICAL | OBSERVED | return/vol/beta/correlation/technical math |
| L004 | 01_preflight.md | independent close cross-check | 518 symbols | Yahoo raw close | USD | 2026-07-27 | price_history_fetch_manifest.json | HISTORICAL | OBSERVED | price grounding |
| L005 | 01_preflight.md | independent close cross-check | 518 symbols | Nasdaq previous close | USD | 2026-07-27 | nasdaq_summary_manifest.json | DELAYED | OBSERVED | price grounding |
| L006 | 01_preflight.md | two-source price gate | 20 equities + 3 ETFs | PASS; all published names within 1% | boolean | 2026-07-27 | price_verification.json; inputs L002,L004,L005 | HISTORICAL | DERIVED | 00,08,15 |
| L007 | 01_preflight.md | VIX close | VIX | 18.67; 20d mean 16.8795 | index | 2026-07-27 | https://cdn.cboe.com/api/global/us_indices/daily_prices/VIX_History.csv | HISTORICAL | OBSERVED | 03,09 |
| L008 | 01_preflight.md | risk-free rate | DTB3 | 3.81% annual; 0.3175% monthly | pct | 2026-07-24 | FRED DTB3, 2026-07-24 | HISTORICAL | OBSERVED | Sharpe,Sortino,Treynor,Calmar |
| L009 | 01_preflight.md | market cap and sector | eligible union | 514 scored records | USD/label | 2026-07-27 | market_cap_eligibility_manifest.json; sector_manifest.json | DELAYED | OBSERVED | 04,05,07 |
| L010 | 01_preflight.md | technical indicator pack | 517 sourceable symbols | daily/weekly/monthly TD9, RSI, MACD, MA, momentum, volume, relative strength | mixed | 2026-07-27 | technical_indicators.json; StockAnalysis adjusted inputs L003 | HISTORICAL | DERIVED | 04,05,06,09,15 |
| L011 | 01_preflight.md | 30d realized volatility | 514 equities + 3 ETFs | population stdev × sqrt(21); universe median 9.36% | pct | 2026-07-27 | run_computed_manifest.json; adjusted returns L003 | HISTORICAL | DERIVED | 03,05,06,15 |
| L012 | 01_preflight.md | downside deviation | 514 equities | population stdev of negative daily returns × sqrt(21) | pct | 2026-07-27 | run_computed_manifest.json; adjusted returns L003 | HISTORICAL | DERIVED | 05 Sortino |
| L013 | 01_preflight.md | 60d beta vs SPY | 514 equities + 3 ETFs | 41.44% of universe negative beta | ratio | 2026-07-27 | run_computed_manifest.json; adjusted returns L003 | HISTORICAL | DERIVED | 03,05,07 |
| L014 | 01_preflight.md | tracking error | 514 equities | population stdev of beta-adjusted residual returns × sqrt(21) | pct | 2026-07-27 | run_computed_manifest.json; inputs L003,L013 | HISTORICAL | DERIVED | 05 IR |
| L015 | 01_preflight.md | 60d max drawdown | 514 equities + 3 ETFs | peak-to-trough adjusted close drawdown | pct | 2026-07-27 | run_computed_manifest.json; input L003 | HISTORICAL | DERIVED | 05,07 |
| L016 | 01_preflight.md | momentum and relative strength | 514 equities + 3 ETFs | 20d/60d momentum and excess vs SPY | pct | 2026-07-27 | technical_indicators.json; inputs L003,L010 | HISTORICAL | DERIVED | 05 Tech_Z |
| L017 | 01_preflight.md | TD9/RSI/MACD/MA/volume | 514 equities + 3 ETFs | daily, weekly and monthly states/values | mixed | 2026-07-27 | technical_indicators.json; formulas and input L003 | HISTORICAL | DERIVED | 05,06,15 |
| L018 | 01_preflight.md | family z-scores | 514 equities | Tech_Z 8 signals; Macro_Z 3; 5/95 winsorize then population z-score | z | 2026-07-27 | run_computed_manifest.json; inputs L011,L013,L015,L016,L017 | HISTORICAL | DERIVED | 05,15 |
| L019 | 01_preflight.md | earnings convergence | top ranks | 40 requested in 1 pass; top20 grounded | count | 2026-07-28 | earnings_calendar_manifest.json | DELAYED | OBSERVED | 05 penalties,06,08 |
| L020 | 01_preflight.md | mu calibration | published 20 | rules.md percentile bands; no per-name adjustments | pct | 2026-07-27 | rules.md mu Calibration Table; run_computed_manifest.json | HISTORICAL | DERIVED | 05,06,15 |
| L021 | 01_preflight.md | target price | published 20 + ETFs | entry × (1 + mu) | USD | 2026-07-27 | inputs L002,L020 | HISTORICAL | DERIVED | 03,05,06,15 |
| L022 | 01_preflight.md | 70% CI | published 20 + ETFs | entry × (1 + mu ± 1.04 sigma) | USD | 2026-07-27 | inputs L002,L011,L020 | HISTORICAL | DERIVED | 03,05,06,15 |
| L023 | 01_preflight.md | Sharpe | published 20 | (mu-rf_1m)/sigma | ratio | 2026-07-27 | inputs L008,L011,L020 | HISTORICAL | DERIVED | 05,06 |
| L024 | 01_preflight.md | Sortino | published 20 | (mu-rf_1m)/downside sigma | ratio | 2026-07-27 | inputs L008,L012,L020 | HISTORICAL | DERIVED | 05,06 |
| L025 | 01_preflight.md | Information ratio | published 20 | (mu-beta×SPY_mu)/tracking error | ratio | 2026-07-27 | inputs L013,L014,L020 | HISTORICAL | DERIVED | 05,06 |
| L026 | 01_preflight.md | Treynor and Calmar | published 20 | (mu-rf)/beta; (mu-rf)/abs(maxDD60) | ratio | 2026-07-27 | inputs L008,L013,L015,L020 | HISTORICAL | DERIVED | 05 |
| L027 | 01_preflight.md | Kelly | published 20 | raw=beta-adjusted residual edge / tracking-error²; quarter-Kelly capped at 5% NAV | fraction | 2026-07-27 | inputs L014,L025; rules.md Ratio Definitions and risk controls | HISTORICAL | DERIVED | 05,07 |
| L028 | 01_preflight.md | VaR95/CVaR95 | published 20 | mu-1.65sigma; mu-2.06sigma; normality assumed | pct | 2026-07-27 | inputs L011,L020 | HISTORICAL | DERIVED | 05,07 |
| L029 | 01_preflight.md | data-quality multiplier | 514 equities | 0.80 universe-wide | multiplier | 2026-07-27 | rules.md Data Quality Multiplier; L039-L041 unavailable blocks | HISTORICAL | INFERRED | 05,08 |
| L030 | 01_preflight.md | penalties | 514 equities | earnings, RVol above 2× sector median, TD9/RSI rules applied | score | 2026-07-27 | run_computed_manifest.json; sector_manifest.json; inputs L009,L011,L017,L019 | HISTORICAL | DERIVED | 05,08 |
| L031 | 01_preflight.md | Adj Score | 514 equities | Adj Score=(0.30*Tech_Z+0.15*Macro_Z)*0.80-penalties; Fund_Z/Sent_Z UNAVAILABLE | score | 2026-07-27 | run_computed_manifest.json; inputs L018,L029,L030 | HISTORICAL | DERIVED | 05,06,15 |
| L032 | 01_preflight.md | percentile rank | 514 equities | INDEX_UNION_PCTL (n=514); (n-rank)/(n-1)×100 | pctl | 2026-07-27 | run_computed_manifest.json; input L031 | HISTORICAL | DERIVED | 05,06 |
| L033 | 01_preflight.md | portfolio feasibility | published / pctl80 pool | 0 investable; pctl80 max beta 0.889447 | mixed | 2026-07-27 | run_computed_manifest.json feasibility | HISTORICAL | DERIVED | 00,07,08,09 |
| L034 | 01_preflight.md | correlation | top10 published | average 0.193146; cap 0.45 | corr | 2026-07-27 | run_computed_manifest.json; adjusted returns L003 | HISTORICAL | DERIVED | 07,08 |
| L035 | 01_preflight.md | sector concentration | published 20 | Industrials 35% exceeds 30% cap | pct | 2026-07-27 | sector_manifest.json; equal-weight diagnostic | HISTORICAL | DERIVED | 07,08 |
| L036 | 01_preflight.md | current-run settlement verification | 35 canonical keys | 29 equity + 6 market independently recomputed; all 35 agree with earlier same-day canonical rows and are retained audit-only; no conflict | count | 2026-07-27 | 15_predictions.json settlements; settlement_manifest.json audit_only_candidates | HISTORICAL | OBSERVED | 00,02,13,15 |
| L037 | 01_preflight.md | rolling calibration after same-day normalization | all canonical | current 35 rows add no canonical n; totals remain EQ n=260 eff_n=1 hit=50.77% CI=74.62% mean z=-0.1973; MF n=48 eff_n=1 hit=20.83% CI=68.75% mean z=-0.6872 | mixed | 2026-07-27 | settlement_manifest.json canonical_settlements and audit_only_candidates | HISTORICAL | OBSERVED | 00,02,13 |
| L038 | 01_preflight.md | MoM baseline | gpt-5-2026-06-30 | SAME_MODEL_BASELINE; exact 28-day target; exception NONE | path | 2026-06-30 | agents/equity/output/gpt-5-2026-06-30/15_predictions.json | HISTORICAL | OBSERVED | 00,02 |
| L039 | 01_preflight.md | Fund_Z | universe-wide | UNAVAILABLE — no universe-scale fundamental feed wired | z | 2026-07-27 | rules.md SHADOW Diagnostic Tooling | UNAVAILABLE | UNAVAILABLE | 05,DQ,evidence threshold |
| L040 | 01_preflight.md | Sent_Z | universe-wide | UNAVAILABLE — no short/options/revision/ownership feed wired | z | 2026-07-27 | rules.md SHADOW Diagnostic Tooling | UNAVAILABLE | UNAVAILABLE | 05,DQ,evidence threshold |
| L041 | 01_preflight.md | enhancing input block | universe-wide | IV/skew, spread tape, short, revisions, ownership UNAVAILABLE | mixed | 2026-07-27 | rules.md Input Classification | UNAVAILABLE | UNAVAILABLE | 00,04,08 |
| L042 | 01_preflight.md | regime classification | market | NEUTRAL | label | 2026-07-27 | regime_data_manifest.json; inputs L007,L008,L010,L011 | HISTORICAL | INFERRED | 03,09 |
| L043 | 01_preflight.md | evolution evidence gate | canonical settlements | raw n passes; eff_n=1 < 3, so Track A DEFER | count | 2026-07-27 | settlement_manifest.json; rules.md Evolution Policy | HISTORICAL | DERIVED | 13 |
| L044 | 01_preflight.md | excluded history | FDXF | 61 calendar days; listing age <=6 months | days | 2026-07-27 | run_computed_manifest.json universe exclusions | HISTORICAL | OBSERVED | 04 |
| L045 | 01_preflight.md | equity forecast pack | RTX | entry 218.42; mu 0.06; sigma 0.093596; target 231.5252; CI 210.264232-252.786168; score 0.363697 | mixed | 2026-07-27 | run_computed_manifest.json; formulas L020-L032; price gate L006 | HISTORICAL | DERIVED | 05,06,09,15 |
| L046 | 01_preflight.md | equity forecast pack | TRV | entry 390.35; mu 0.06; sigma 0.091532; target 413.771; CI 376.612303-450.929697; score 0.304548 | mixed | 2026-07-27 | run_computed_manifest.json; formulas L020-L032; price gate L006 | HISTORICAL | DERIVED | 05,06,09,15 |
| L047 | 01_preflight.md | equity forecast pack | PAYX | entry 115.48; mu 0.06; sigma 0.091481; target 122.4088; CI 111.422005-133.395595; score 0.295604 | mixed | 2026-07-27 | run_computed_manifest.json; formulas L020-L032; price gate L006 | HISTORICAL | DERIVED | 05,06,09,15 |
| L048 | 01_preflight.md | equity forecast pack | SJM | entry 121.05; mu 0.06; sigma 0.09491; target 128.313; CI 116.36459-140.26141; score 0.271538 | mixed | 2026-07-27 | run_computed_manifest.json; formulas L020-L032; price gate L006 | HISTORICAL | DERIVED | 05,06,09,15 |
| L049 | 01_preflight.md | equity forecast pack | CSX | entry 51.8; mu 0.06; sigma 0.074207; target 54.908; CI 50.91032-58.90568; score 0.268044 | mixed | 2026-07-27 | run_computed_manifest.json; formulas L020-L032; price gate L006 | HISTORICAL | DERIVED | 05,06,09,15 |
| L050 | 01_preflight.md | equity forecast pack | DGX | entry 231.84; mu 0.06; sigma 0.094515; target 245.7504; CI 222.961548-268.539252; score 0.2649 | mixed | 2026-07-27 | run_computed_manifest.json; formulas L020-L032; price gate L006 | HISTORICAL | DERIVED | 05,06,09,15 |
| L051 | 01_preflight.md | equity forecast pack | IQV | entry 213.22; mu 0.06; sigma 0.112904; target 226.0132; CI 200.976873-251.049527; score 0.255111 | mixed | 2026-07-27 | run_computed_manifest.json; formulas L020-L032; price gate L006 | HISTORICAL | DERIVED | 05,06,09,15 |
| L052 | 01_preflight.md | equity forecast pack | BBY | entry 88.45; mu 0.06; sigma 0.089385; target 93.757; CI 85.534653-101.979347; score 0.252005 | mixed | 2026-07-27 | run_computed_manifest.json; formulas L020-L032; price gate L006 | HISTORICAL | DERIVED | 05,06,09,15 |
| L053 | 01_preflight.md | equity forecast pack | MET | entry 95.19; mu 0.06; sigma 0.070412; target 100.9014; CI 93.930781-107.872019; score 0.246753 | mixed | 2026-07-27 | run_computed_manifest.json; formulas L020-L032; price gate L006 | HISTORICAL | DERIVED | 05,06,09,15 |
| L054 | 01_preflight.md | equity forecast pack | UNP | entry 299.3; mu 0.06; sigma 0.076298; target 317.258; CI 293.508569-341.007431; score 0.242917 | mixed | 2026-07-27 | run_computed_manifest.json; formulas L020-L032; price gate L006 | HISTORICAL | DERIVED | 05,06,09,15 |
| L055 | 01_preflight.md | equity forecast pack | IVZ | entry 30.11; mu 0.06; sigma 0.109961; target 31.9166; CI 28.473237-35.359963; score 0.241095 | mixed | 2026-07-27 | run_computed_manifest.json; formulas L020-L032; price gate L006 | HISTORICAL | DERIVED | 05,06,09,15 |
| L056 | 01_preflight.md | equity forecast pack | PRU | entry 121.89; mu 0.06; sigma 0.061627; target 129.2034; CI 121.391216-137.015584; score 0.233416 | mixed | 2026-07-27 | run_computed_manifest.json; formulas L020-L032; price gate L006 | HISTORICAL | DERIVED | 05,06,09,15 |
| L057 | 01_preflight.md | equity forecast pack | NSC | entry 343.35; mu 0.06; sigma 0.072372; target 363.951; CI 338.108117-389.793883; score 0.233015 | mixed | 2026-07-27 | run_computed_manifest.json; formulas L020-L032; price gate L006 | HISTORICAL | DERIVED | 05,06,09,15 |
| L058 | 01_preflight.md | equity forecast pack | ITW | entry 284.82; mu 0.06; sigma 0.066564; target 301.9092; CI 282.192091-321.626309; score 0.226854 | mixed | 2026-07-27 | run_computed_manifest.json; formulas L020-L032; price gate L006 | HISTORICAL | DERIVED | 05,06,09,15 |
| L059 | 01_preflight.md | equity forecast pack | CTAS | entry 210.98; mu 0.06; sigma 0.102878; target 223.6388; CI 201.065392-246.212208; score 0.226217 | mixed | 2026-07-27 | run_computed_manifest.json; formulas L020-L032; price gate L006 | HISTORICAL | DERIVED | 05,06,09,15 |
| L060 | 01_preflight.md | equity forecast pack | EXR | entry 148.29; mu 0.06; sigma 0.063553; target 157.1874; CI 147.386155-166.988645; score 0.224 | mixed | 2026-07-27 | run_computed_manifest.json; formulas L020-L032; price gate L006 | HISTORICAL | DERIVED | 05,06,09,15 |
| L061 | 01_preflight.md | equity forecast pack | MPC | entry 312.35; mu 0.06; sigma 0.094567; target 331.091; CI 300.371477-361.810523; score 0.222103 | mixed | 2026-07-27 | run_computed_manifest.json; formulas L020-L032; price gate L006 | HISTORICAL | DERIVED | 05,06,09,15 |
| L062 | 01_preflight.md | equity forecast pack | WELL | entry 248.34; mu 0.06; sigma 0.06886; target 263.2404; CI 245.45568-281.02512; score 0.21757 | mixed | 2026-07-27 | run_computed_manifest.json; formulas L020-L032; price gate L006 | HISTORICAL | DERIVED | 05,06,09,15 |
| L063 | 01_preflight.md | equity forecast pack | CB | entry 358.91; mu 0.06; sigma 0.080262; target 380.4446; CI 350.485492-410.403708; score 0.216063 | mixed | 2026-07-27 | run_computed_manifest.json; formulas L020-L032; price gate L006 | HISTORICAL | DERIVED | 05,06,09,15 |
| L064 | 01_preflight.md | equity forecast pack | PM | entry 195.66; mu 0.06; sigma 0.092556; target 207.3996; CI 188.565713-226.233487; score 0.203931 | mixed | 2026-07-27 | run_computed_manifest.json; formulas L020-L032; price gate L006 | HISTORICAL | DERIVED | 05,06,09,15 |
| L065 | 01_preflight.md | core ETF forecast | SPY | entry 739.09; mu 0.005; sigma 0.036365; target 742.78545; CI 714.833362-770.737538 | mixed | 2026-07-27 | run_computed_manifest.json; formulas L021-L022; price gate L006 | HISTORICAL | DERIVED | 03,09,15 |
| L066 | 01_preflight.md | core ETF forecast | QQQ | entry 682.12; mu -0.0064; sigma 0.07268; target 677.754432; CI 626.194891-729.313973 | mixed | 2026-07-27 | run_computed_manifest.json; formulas L021-L022; price gate L006 | HISTORICAL | DERIVED | 03,09,15 |
| L067 | 01_preflight.md | core ETF forecast | SOXX | entry 516.23; mu 0.003237; sigma 0.185818; target 517.901037; CI 418.139217-617.662856 | mixed | 2026-07-27 | run_computed_manifest.json; formulas L021-L022; price gate L006 | HISTORICAL | DERIVED | 03,09,15 |
| L068 | 01_preflight.md | earnings-grounding exclusion | unresolved top30 | LMT, EG, AMGN, BNY, WTW, DOC, AFL, VTRS, AMP, UDR | list | 2026-07-28 | earnings_calendar_manifest.json; run_computed_manifest.json | HISTORICAL | INFERRED | 05,06,08 |
| L069 | 01_preflight.md | event calendar | FOMC | meeting 2026-07-28–29; statement 2026-07-29 14:00 ET | date/time | 2026-07-28 | https://www.federalreserve.gov/newsevents/2026-july.htm | DELAYED | OBSERVED | 03,08,09 |

## Coverage

| claim_type | rows |
|---|---|
| OBSERVED | 14 |
| DERIVED | 49 |
| INFERRED | 3 |
| UNAVAILABLE | 3 |
| ILLUSTRATIVE | 0 |
| TOTAL | 69 |

No ILLUSTRATIVE row contributes to this package. Missing Fund_Z, Sent_Z, and Enhancing feeds remain explicitly UNAVAILABLE.
