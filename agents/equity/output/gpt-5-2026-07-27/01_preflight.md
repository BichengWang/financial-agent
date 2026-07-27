# 01 Preflight — Source Ledger — 2026-07-27

Grounding records were assembled before reflection and scoring; row IDs were then frozen for all downstream artifacts. Every price, return, volatility, beta, earnings date, target, CI bound, drawdown, ratio, technical state, and sizing input is represented below or marked `UNAVAILABLE`.

## Run Context

- Monday pre-open run; latest completed session and sole execution-price basis: **2026-07-24**.
- Data mode: **`DELAYED`**.
- Adjusted closes drive returns/indicators; unadjusted closes drive settlements, entries, targets, and CIs. This carries forward the accepted 2026-07-26 Track B rule.
- Current-run retrieval timestamps are recorded per symbol/source in the JSON support manifests.

## Endpoint Results

| Endpoint | Use | Current-run result |
|---|---|---|
| `stockanalysis.com/api/symbol/.../history?range=5Y` | adjusted + unadjusted 5y histories | 519/519, about 25 seconds |
| `api.nasdaq.com/api/quote/.../historical` | independent official-close check | 41/41 |
| `quote.cnbc.com/.../restQuote` | third close check + `last_time` | 41/41; every date 2026-07-24 |
| `api.nasdaq.com/api/analyst/.../earnings-date` | earnings grounding | 62/62 audit requests; 56 used by bounded scoring passes |
| `api.nasdaq.com/api/quote/.../summary` | sector / industry | 24/24 published names |
| Nasdaq bulk screener | market cap | 514 current + 1 recent historical fallback (BF-B); all >$2B |
| CBOE VIX history | regime | 2026-07-24 close and 60-session averages present |
| U.S. Treasury daily bill rates | risk-free | 2026-07-24 13-week rate present |

## Price Verification

All **41 unique symbols** appearing in due settlements or new forecasts pass the Price Sourcing Standard. The largest divergence is BNY at 0.396451%, below 1%; the 17 due-settlement symbols agree exactly. `price_verification.json` records the full URLs and a separate `retrieved_at` for each source.

| Symbol | StockAnalysis | Nasdaq | CNBC | CNBC date | Max diff | Verdict |
|---|---:|---:|---:|---|---:|---|
| AAPL | 333.02 | 333.02 | 333.02 | 2026-07-24 | 0.000000% | OK |
| BAC | 62.05 | 62.05 | 62.05 | 2026-07-24 | 0.000000% | OK |
| BNY | 158.91 | 158.91 | 158.28 | 2026-07-24 | 0.396451% | OK |
| CAT | 888.73 | 888.73 | 888.73 | 2026-07-24 | 0.000000% | OK |
| CB | 359.75 | 359.75 | 359.75 | 2026-07-24 | 0.000000% | OK |
| CSX | 53.23 | 53.23 | 53.23 | 2026-07-24 | 0.000000% | OK |
| CTAS | 205.91 | 205.91 | 205.91 | 2026-07-24 | 0.000000% | OK |
| CVX | 194.79 | 194.79 | 194.79 | 2026-07-24 | 0.000000% | OK |
| DGX | 227.86 | 227.86 | 227.86 | 2026-07-24 | 0.000000% | OK |
| EQIX | 1084.24 | 1084.24 | 1084.24 | 2026-07-24 | 0.000000% | OK |
| EQR | 67.86 | 67.86 | 67.86 | 2026-07-24 | 0.000000% | OK |
| FCX | 62.60 | 62.60 | 62.60 | 2026-07-24 | 0.000000% | OK |
| GD | 386.75 | 386.75 | 386.75 | 2026-07-24 | 0.000000% | OK |
| GE | 353.73 | 353.73 | 353.73 | 2026-07-24 | 0.000000% | OK |
| GOOGL | 319.74 | 319.74 | 319.74 | 2026-07-24 | 0.000000% | OK |
| GS | 1061.23 | 1061.23 | 1061.23 | 2026-07-24 | 0.000000% | OK |
| HIG | 140.53 | 140.53 | 140.53 | 2026-07-24 | 0.000000% | OK |
| JPM | 353.21 | 353.21 | 353.21 | 2026-07-24 | 0.000000% | OK |
| LLY | 1196.03 | 1196.03 | 1196.03 | 2026-07-24 | 0.000000% | OK |
| LMT | 582.60 | 582.60 | 582.60 | 2026-07-24 | 0.000000% | OK |
| MET | 94.83 | 94.83 | 94.83 | 2026-07-24 | 0.000000% | OK |
| MPC | 309.24 | 309.24 | 309.24 | 2026-07-24 | 0.000000% | OK |
| NSC | 350.66 | 350.66 | 350.66 | 2026-07-24 | 0.000000% | OK |
| PAYX | 113.55 | 113.55 | 113.55 | 2026-07-24 | 0.000000% | OK |
| PCG | 17.85 | 17.85 | 17.85 | 2026-07-24 | 0.000000% | OK |
| PKG | 254.39 | 254.39 | 254.39 | 2026-07-24 | 0.000000% | OK |
| PM | 193.00 | 193.00 | 193.00 | 2026-07-24 | 0.000000% | OK |
| QQQ | 684.23 | 684.23 | 684.23 | 2026-07-24 | 0.000000% | OK |
| RTX | 212.79 | 212.79 | 212.79 | 2026-07-24 | 0.000000% | OK |
| SHW | 317.51 | 317.51 | 317.51 | 2026-07-24 | 0.000000% | OK |
| SJM | 118.32 | 118.32 | 118.32 | 2026-07-24 | 0.000000% | OK |
| SOXX | 527.01 | 527.01 | 527.01 | 2026-07-24 | 0.000000% | OK |
| SPY | 738.93 | 738.93 | 738.93 | 2026-07-24 | 0.000000% | OK |
| TMO | 568.26 | 568.26 | 568.26 | 2026-07-24 | 0.000000% | OK |
| TRV | 387.26 | 387.26 | 387.26 | 2026-07-24 | 0.000000% | OK |
| UNH | 420.74 | 420.74 | 420.74 | 2026-07-24 | 0.000000% | OK |
| UNP | 307.32 | 307.32 | 307.32 | 2026-07-24 | 0.000000% | OK |
| V | 355.74 | 355.74 | 355.74 | 2026-07-24 | 0.000000% | OK |
| VLO | 302.50 | 302.50 | 302.50 | 2026-07-24 | 0.000000% | OK |
| WAB | 302.50 | 302.50 | 302.50 | 2026-07-24 | 0.000000% | OK |
| WRB | 75.46 | 75.46 | 75.46 | 2026-07-24 | 0.000000% | OK |

## Return-Basis Validation

The current 519-symbol fetch was independently materialized to adjusted-close CSVs. Against the 2026-07-26 structured package, all **514/514** scoreable unadjusted closes and all **517/517** comparable technical packs match exactly. FDXF is present in today's required 518-record technical envelope but is explicitly `UNAVAILABLE` because only 40 usable bars exist.

## Source Ledger

| Row | artifact | field | ticker/entity | value | unit | observation_date | source | freshness_tag | claim_type | used_by |
|---|---|---|---|---|---|---|---|---|---|---|
| L001 | 01 | close (unadjusted) | 41 settlement/forecast symbols | `price_verification.json` | USD | 2026-07-24 | 3 sources; per-source retrieval timestamps 2026-07-27 | HISTORICAL | OBSERVED | 02,03,05,15 |
| L002 | 01 | close (unadjusted) | 24 published equities | see `05` | USD | 2026-07-24 | L001 | HISTORICAL | OBSERVED | 05,06,15 |
| L003 | 01 | daily bars (adjusted + raw) | 515 union + SPY/QQQ/SOXX/TLT | 40–1,255 bars | USD | through 2026-07-24 | `price_history_fetch_manifest.json` | HISTORICAL | OBSERVED | 03,05,technical indicators |
| L004 | 01 | retrieval timestamp | history bundle | completed 2026-07-27T12:52:39Z | ISO ts | 2026-07-27 | current run log | DELAYED | OBSERVED | 01 |
| L005 | 01 | VIX close | VIX | 18.58 | index | 2026-07-24 | CBOE, retrieved 2026-07-27T12:55:43Z | HISTORICAL | OBSERVED | 03 |
| L006 | 01 | VIX 30d / prior 30d avg | VIX | 17.12 / 17.60 | index | 2026-07-24 | means of L005 series | HISTORICAL | DERIVED | 03 |
| L007 | 01 | 13-week T-bill bank discount | U.S. Treasury | 3.81 | % p.a. | 2026-07-24 | Treasury, retrieved 2026-07-27T12:55:43Z | HISTORICAL | OBSERVED | 05 ratios |
| L008 | 01 | monthly risk-free | U.S. Treasury | 0.003175 | decimal | 2026-07-24 | L007 / 12 | HISTORICAL | DERIVED | 05 ratios |
| L009 | 01 | index-union counts | universe | 503 / 101 / 89 / 515 | count | cache 2026-06-21T21:05:56Z | helper + `universe_summary.json` | HISTORICAL | OBSERVED | 00,03,04 |
| L010 | 01 | scored universe | universe | 514 | count | 2026-07-27 | L009 minus FDXF | HISTORICAL | DERIVED | 04,05 |
| L011 | 01 | exclusion | FDXF | 40 usable bars from 2026-05-28 | count | 2026-07-24 | L003 | HISTORICAL | OBSERVED | 04 |
| L012 | 01 | listing-age admission | Q | 185 bars from 2025-10-28 | count | 2026-07-24 | L003 | HISTORICAL | OBSERVED | 04 |
| L013 | 01 | 30d realized vol | 514 equities + 3 ETFs | see `05`/`03` | decimal 1m | 2026-07-24 | stdev(last 30 adjusted returns)×√21, L003 | HISTORICAL | DERIVED | 03,05,15 |
| L014 | 01 | prior-30d realized vol | core ETFs | SPY .0375 / QQQ .0640 / SOXX .1692 | decimal 1m | 2026-07-24 | prior 30 adjusted returns, L003 | HISTORICAL | DERIVED | 03 |
| L015 | 01 | downside sigma | 514 equities | see `05` | decimal 1m | 2026-07-24 | stdev(negative returns)×√21, L003 | HISTORICAL | DERIVED | 05 |
| L016 | 01 | 60d beta vs SPY | 514 equities + ETFs/TLT | see `03`/`05` | ratio | 2026-07-24 | OLS on adjusted returns, L003 | HISTORICAL | DERIVED | 03,05,07 |
| L017 | 01 | tracking error | 514 equities | see `05` | decimal 1m | 2026-07-24 | stdev(r−βr_SPY)×√21, L003/L016 | HISTORICAL | DERIVED | 05 |
| L018 | 01 | 60d max drawdown | 514 equities + ETFs | see `03`/`05` | decimal | 2026-07-24 | worst adjusted-close peak/trough, L003 | HISTORICAL | DERIVED | 03,05 |
| L019 | 01 | ADV20 | 514 equities | all >$20M | USD | 2026-07-24 | mean(raw close×volume), L003 | HISTORICAL | DERIVED | 04 |
| L020 | 01 | median sigma30 | universe | 0.096089 | decimal 1m | 2026-07-24 | median L013 | HISTORICAL | DERIVED | 05 |
| L021 | 01 | company / GICS sector / sub-industry | 24 published equities | `sector_manifest.json` | label | 2026-07-27 | current S&P 500 constituent table; raw Nasdaq labels retained for audit | DELAYED | OBSERVED | 05,07,09 |
| L022 | 01 | confirmed earnings | 37 scoring-pass names | `earnings_calendar_manifest.json` | date | 2026-07-27 | Nasdaq analyst endpoint, current retrieval | DELAYED | OBSERVED | 05,08 |
| L023 | 01 | cadence-estimated earnings | 18 scoring-pass names | prior print +91d (±5d) | date | 2026-07-27 | vendor-empty + current standing signature rule | DELAYED | INFERRED | 05 |
| L024 | 01 | conservative print-week estimate | HIG | `ESTIMATED_PRINT_WEEK (±5d)` | date | 2026-07-27 | vendor-empty, no signature | DELAYED | INFERRED | 05 |
| L025 | 01 | momentum 20/60 | scored set + core ETFs | see artifacts | % | 2026-07-24 | `technical_indicators.json`, L003 | HISTORICAL | DERIVED | 03,05 |
| L026 | 01 | relative strength vs SPY | scored set + core ETFs | see artifacts | pp | 2026-07-24 | `technical_indicators.json`, L003 | HISTORICAL | DERIVED | 03,05 |
| L027 | 01 | volume ratio | scored set | see `05` | ratio | 2026-07-24 | `technical_indicators.json`, L003 | HISTORICAL | DERIVED | 05 |
| L028 | 01 | core ETF close | SPY/QQQ/SOXX | 738.93 / 684.23 / 527.01 | USD | 2026-07-24 | L001 | HISTORICAL | OBSERVED | 03,09,15 |
| L029 | 01 | TLT state | TLT | 83.25; DD −4.45%; RSI 33.19; mom60 −2.52%; RVol30 2.57% vs 2.63% prior | mixed | 2026-07-24 | L003 + helper; realized-vol and momentum formulas | HISTORICAL | DERIVED | 03 |
| L030 | 01 | forecast sigma | 24 equities + 3 ETFs | `REALIZED_VOL_30D` | decimal 1m | 2026-07-24 | L013; fallback step 2 | HISTORICAL | DERIVED | 03,05,15 |
| L031 | 01 | market cap | index union | 515 >$2B | USD | 2026-07-27 / BF-B 2026-07-25 | current Nasdaq bulk + one recent BF-B fallback | DELAYED | OBSERVED | 04 |
| L032 | 01 | deterministic reproduction | scoreable set | 514 closes + 517 technical packs exact | count | 2026-07-27 | current fetch vs prior structured artifact | HISTORICAL | DERIVED | 00,04,13 |
| L135 | 01 | technical indicator pack | 518 required records | 517 OK; FDXF UNAVAILABLE | mixed | 2026-07-24 | helper on current adjusted CSVs, L003 | HISTORICAL | DERIVED | 03,04,05,06,09,15 |
| L136 | 01 | settlement prices | 34 keys / 17 symbols | see `02` | USD | 2026-07-24 | L001 | HISTORICAL | OBSERVED | 02,15 |
| L137 | 01 | settlement arithmetic | 34 keys | return, alpha, CI, z | decimal | 2026-07-27 | settlement rules, L136 + vintage records | HISTORICAL | DERIVED | 02 |
| L138 | 01 | canonical ledger state | all models | due 0; conflicts 0; EQ 231; MF 42; eff_n 1/1 | count | 2026-07-27 | `settlement_manifest.json` | HISTORICAL | DERIVED | 00,02,13 |
| L139 | 01 | regime | market | `NEUTRAL` | label | 2026-07-24 | judgment on L005/L025/L028/L029/L135 | HISTORICAL | INFERRED | 03,05,09 |
| L140 | 01 | defensive Macro polarity | universe | low beta/vol/DD score better | polarity | 2026-07-27 | regime-conditional judgment, L139 | HISTORICAL | INFERRED | 05 |
| L141 | 01 | portfolio feasibility | top 10 | max attainable beta −0.159 | ratio | 2026-07-27 | sum(5%×highest betas), L016 | HISTORICAL | DERIVED | 07,08 |
| L142 | 01 | beta distribution | universe | 212/514 negative; median +0.228 | count/ratio | 2026-07-24 | L016 | HISTORICAL | DERIVED | 03,07 |
| L143 | 01 | adjusted-basis carry-forward | current histories | 514/514 closes and 517/517 comparable packs exact | count | 2026-07-27 | L003/L032 | HISTORICAL | DERIVED | 05,13 |
| L144 | 01 | Fundamental family | 514 names | `UNAVAILABLE` | — | 2026-07-27 | SHADOW not promoted | UNAVAILABLE | UNAVAILABLE | 05,08 |
| L145 | 01 | Sentiment family | 514 names | `UNAVAILABLE` | — | 2026-07-27 | SHADOW not promoted | UNAVAILABLE | UNAVAILABLE | 05,08 |
| L146 | 01 | Enhancing inputs | universe | `UNAVAILABLE` | — | 2026-07-27 | no feed wired | UNAVAILABLE | UNAVAILABLE | 05,08 |
| L147 | 01 | price-source divergence | 41 symbols | max 0.396451%; all pass | % | 2026-07-24 | `price_verification.json` | HISTORICAL | OBSERVED | 00,08 |
| L148 | 01 | earnings-signature audit | EQR/PKG/WRB/CB | 0.01%/0.01%/2.45%/2.46% moves with ≥1.8× volume | %/ratio | 2026-07-24 | adjusted histories + standing rule | HISTORICAL | DERIVED | 08,13 |
| L149 | 01 | composite score / adjusted score / percentile | 514 scored equities | `Composite_Z`; DQ-adjusted score; `INDEX_UNION_PCTL (n=514)` | mixed | 2026-07-27 | family z-scores and polarity from L013-L027/L139-L145; scoring formula in `rules.md` | HISTORICAL | DERIVED | 04,05,06,09,15 |
| L150 | 01 | forecast, ratio, and sizing arithmetic | 206 forecast-eligible equities + 3 ETFs; 24 equities published | target/CI; Sharpe/Sortino/IR; Kelly; VaR/CVaR | mixed | 2026-07-27 | formulas in `rules.md` using L007-L008/L013-L018/L028/L030; IR and Kelly use beta-adjusted edge and tracking-error risk | HISTORICAL | DERIVED | 03,05,06,07,08,09,15 |

## Coverage and Limitations

Grounding alone is `GO`-eligible; the `NO_TRADE` result comes from evidence and feasibility gates. `Fund_Z` and `Sent_Z` are unavailable, DQ is 0.80, and the Enhancing block is absent. The technical envelope is complete and honest: 517 records are OK and FDXF is unavailable rather than hand-filled. EQR and PKG are disclosed as weak vendor-empty resolutions under today's standing rule; `13` tightens that rule for the next run.
