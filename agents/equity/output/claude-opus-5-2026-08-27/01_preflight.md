# 01 — Preflight and Source Ledger · 2026-08-27

Model `claude-opus-5` · post-close fire · price basis **2026-08-27** (Thursday regular session) ·
target date **2026-09-24** (`run_date + 28d`).

This artifact is generated from `run_computed_manifest.json`, `settlement_manifest.json`,
`price_verification.json`, `earnings_sweep.json`, `corporate_actions.json` and
`macro_inputs.json`. No figure below was typed by hand. The working JSONs live under
`.work/claude-opus-5-2026-08-27/` and the scratchpad and are **not** committed
(`runbook.md § Retention Contract`); every decision-relevant value they carry is persisted here,
in `05`, and in `15`.

> **AMENDED 2026-08-27** (second scheduled fire ~22:03 ET). One over-claimed count in row `L011`
> is corrected in place, original preserved. No package was republished and no prediction record
> was added or altered; `NO_TRADE` and every downstream number stand. See **§ Amendment** at the
> end of this file for the three re-verified gates and the evidence.

## Fire window and price basis

The task fired at 19:09 ET, **after** the 16:00 close. At that hour the same-day close is final at
every vendor — 515 of 518 fetched symbols carry a
2026-08-27 last bar — and same-day `TARGET_DATE_CLOSE` settlement is available, so 50 of the
231 due keys settled a day earlier than a pre-open fire would have allowed.
`POST_MKT` vendor field semantics were re-verified and held exactly as documented on 2026-08-03:
CNBC `last` gated on `last_time` date == basis is the official close (`previous_day_closing` is T-1),
and Nasdaq `secondaryData.lastSalePrice` gated on the "Closed at 2026-08-27 4:00 PM ET" marker is the
close (`primaryData` is the after-hours tape).

## GO-Gate Table (Required inputs only)

| # | Required input (rules.md § Input Classification) | Status | Evidence |
|---|---|---|---|
| 1 | Grounded entry price | GROUNDED | 27/27 symbols on 3 independent sources, max deviation 0.095123% (L002, L011, L012, L012a) |
| 2 | ~60 trading days of history per name + SPY | GROUNDED | 518/519 symbols fetched at 5Y depth in 10.7s (L002) |
| 3 | sigma via the Sigma Fallback Chain | GROUNDED | REALIZED_VOL_30D for all 24 published names and all 3 core ETFs (L300-L323, L003b/L004b/L005b) |
| 4 | Next earnings date | GROUNDED | complete 27-business-day forward sweep, 0 transport failures; entire scored universe classified (L010, L600-L623) |
| 5 | S&P 500 union Nasdaq-100 index-union universe | GROUNDED | build_index_universe.py union 515; 509 scored after filters (L001, L009) |

All five Required inputs are grounded, so the run is **not** `DELAYED_PARTIAL` and the blocker is not
data availability. Enhancing inputs are listed as caps, never blockers (L023):

| Enhancing input | Status | Effect |
|---|---|---|
| Options IV / skew | `UNAVAILABLE` | sigma falls to `REALIZED_VOL_30D` (chain step 2); confidence capped `MEDIUM` |
| Short interest / borrow | `UNAVAILABLE` | `Sent_Z` cannot be built; data-quality multiplier 0.80 |
| Bid-ask spread tape | `UNAVAILABLE` | 50bp spread exclusion filter cannot be applied; disclosed in `04` |
| Analyst revision tape | `UNAVAILABLE` | `Fund_Z`/`Sent_Z` cannot be built; data-quality multiplier 0.80 |
| Institutional ownership flow | `UNAVAILABLE` | no effect beyond the above |
| Full-universe percentile feed | GROUNDED (not needed) | percentiles come from the index union itself, `INDEX_UNION_PCTL (n={m['universe']['scored']})` |

Per `rules.md § Input Classification`, a run with all Required inputs grounded and several Enhancing
inputs missing is a valid `GO` candidate at reduced confidence and a 50% gross cap — it is **not**
automatically `REVIEW_ONLY`. This run's `NO_TRADE` is therefore driven by the evidence thresholds in
`05` and the portfolio infeasibility in `07`, not by input availability.

## Source Ledger

| artifact | field | ticker/entity | value | unit | observation_date | source | freshness_tag | claim_type | used_by |
|---|---|---|---|---|---|---|---|---|---|
| L001 | index constituent caches | S&P 500 union Nasdaq-100 | 503 + 101, overlap 89, union 515 | count | 2026-06-21 | agents/equity/turtle-trader/universe/sp500.json + nasdaq100.json via build_index_universe.py (caches fetched_at 2026-06-21T21:05:56Z) | HISTORICAL | OBSERVED | 03, 04 |
| L002 | daily OHLCV history 5Y | 515 universe + SPY/QQQ/SOXX/TLT | 518/519 symbols OK, 1 failed | bars | 2026-08-27 | https://stockanalysis.com/api/symbol/{s\|e}/{SYM}/history?range=5Y retrieved_at 2026-08-27T16:11:27-0700 (10.7s, 8 workers) | DELAYED | OBSERVED | 03, 04, 05, 07, 15 |
| L002a | history manifest (regenerability) | 519 symbols | per-symbol bar counts, first/last bar, last raw+adj close, ex-div flag; 515 last bars == 2026-08-27 | manifest | 2026-08-27 | .work/claude-opus-5-2026-08-27 stockanalysis_history_manifest.json (CSV trees stay in the scratchpad per the 2026-08-01 size rule) | DELAYED | DERIVED | 01, 04 |
| L002b | adjusted vs raw close basis | 519 symbols | ex-dividend c!=a on the basis bar: 7 names (BAX, EBAY, HII, LH, NEE, TAP, TMUS) | count | 2026-08-27 | DERIVED: scan of last-bar c vs a across the fetched tree; Track B 2026-07-26 — adjusted closes for all return/indicator math, raw closes for entry/target/CI | DELAYED | DERIVED | 01, 04, 05 |
| L003 | close (raw) / close (adjusted) | SPY | 771.10 / 771.1000 | USD | 2026-08-27 | https://stockanalysis.com/api/symbol/{s\|e}/{SYM}/history?range=5Y (L002) | DELAYED | OBSERVED | 03, 05, 15 |
| L003a | beta vs SPY (60d) | SPY | 1.000000 | ratio | 2026-08-27 | DERIVED: cov(r,r_SPY,ddof=0)/var(r_SPY) on 60 daily adjusted return intervals; inputs L002, L003 | DELAYED | DERIVED | 03, 15 |
| L003b | realized vol 30d (1m) | SPY | 0.034875 | decimal | 2026-08-27 | DERIVED: pstdev(30 daily adj returns) x sqrt(21); input L002 | DELAYED | DERIVED | 03, 15 |
| L003c | prior-30d realized vol (1m) | SPY | 0.044617 | decimal | 2026-08-27 | DERIVED: pstdev(daily adj returns [-60:-30]) x sqrt(21); input L002 | DELAYED | DERIVED | 03 |
| L003d | drawdown from 60d high | SPY | -0.044946 | decimal | 2026-08-27 | DERIVED: worst peak-to-trough over the 61 most recent adjusted closes; input L002 | DELAYED | DERIVED | 03 |
| L003e | relative strength 20d / 60d vs SPY | SPY | +0.00% / +0.00% | percent | 2026-08-27 | technical_indicators.py daily block (L013); formula: rules.md § Technical Indicator Pack Definition | DELAYED | DERIVED | 03 |
| L004 | close (raw) / close (adjusted) | QQQ | 721.11 / 721.1100 | USD | 2026-08-27 | https://stockanalysis.com/api/symbol/{s\|e}/{SYM}/history?range=5Y (L002) | DELAYED | OBSERVED | 03, 05, 15 |
| L004a | beta vs SPY (60d) | QQQ | 1.720903 | ratio | 2026-08-27 | DERIVED: cov(r,r_SPY,ddof=0)/var(r_SPY) on 60 daily adjusted return intervals; inputs L002, L003 | DELAYED | DERIVED | 03, 15 |
| L004b | realized vol 30d (1m) | QQQ | 0.060912 | decimal | 2026-08-27 | DERIVED: pstdev(30 daily adj returns) x sqrt(21); input L002 | DELAYED | DERIVED | 03, 15 |
| L004c | prior-30d realized vol (1m) | QQQ | 0.086517 | decimal | 2026-08-27 | DERIVED: pstdev(daily adj returns [-60:-30]) x sqrt(21); input L002 | DELAYED | DERIVED | 03 |
| L004d | drawdown from 60d high | QQQ | -0.112177 | decimal | 2026-08-27 | DERIVED: worst peak-to-trough over the 61 most recent adjusted closes; input L002 | DELAYED | DERIVED | 03 |
| L004e | relative strength 20d / 60d vs SPY | QQQ | +1.52% / -5.03% | percent | 2026-08-27 | technical_indicators.py daily block (L013); formula: rules.md § Technical Indicator Pack Definition | DELAYED | DERIVED | 03 |
| L005 | close (raw) / close (adjusted) | SOXX | 525.43 / 525.4300 | USD | 2026-08-27 | https://stockanalysis.com/api/symbol/{s\|e}/{SYM}/history?range=5Y (L002) | DELAYED | OBSERVED | 03, 05, 15 |
| L005a | beta vs SPY (60d) | SOXX | 3.347798 | ratio | 2026-08-27 | DERIVED: cov(r,r_SPY,ddof=0)/var(r_SPY) on 60 daily adjusted return intervals; inputs L002, L003 | DELAYED | DERIVED | 03, 15 |
| L005b | realized vol 30d (1m) | SOXX | 0.143845 | decimal | 2026-08-27 | DERIVED: pstdev(30 daily adj returns) x sqrt(21); input L002 | DELAYED | DERIVED | 03, 15 |
| L005c | prior-30d realized vol (1m) | SOXX | 0.217258 | decimal | 2026-08-27 | DERIVED: pstdev(daily adj returns [-60:-30]) x sqrt(21); input L002 | DELAYED | DERIVED | 03 |
| L005d | drawdown from 60d high | SOXX | -0.290087 | decimal | 2026-08-27 | DERIVED: worst peak-to-trough over the 61 most recent adjusted closes; input L002 | DELAYED | DERIVED | 03 |
| L005e | relative strength 20d / 60d vs SPY | SOXX | +0.17% / -14.89% | percent | 2026-08-27 | technical_indicators.py daily block (L013); formula: rules.md § Technical Indicator Pack Definition | DELAYED | DERIVED | 03 |
| L006 | close (raw) / close (adjusted) | TLT | 83.13 / 83.1300 | USD | 2026-08-27 | https://stockanalysis.com/api/symbol/{s\|e}/{SYM}/history?range=5Y (L002) | DELAYED | OBSERVED | 03, 05, 15 |
| L006a | beta vs SPY (60d) | TLT | 0.219824 | ratio | 2026-08-27 | DERIVED: cov(r,r_SPY,ddof=0)/var(r_SPY) on 60 daily adjusted return intervals; inputs L002, L003 | DELAYED | DERIVED | 03, 15 |
| L006b | realized vol 30d (1m) | TLT | 0.030856 | decimal | 2026-08-27 | DERIVED: pstdev(30 daily adj returns) x sqrt(21); input L002 | DELAYED | DERIVED | 03, 15 |
| L006c | prior-30d realized vol (1m) | TLT | 0.025568 | decimal | 2026-08-27 | DERIVED: pstdev(daily adj returns [-60:-30]) x sqrt(21); input L002 | DELAYED | DERIVED | 03 |
| L006d | drawdown from 60d high | TLT | -0.062552 | decimal | 2026-08-27 | DERIVED: worst peak-to-trough over the 61 most recent adjusted closes; input L002 | DELAYED | DERIVED | 03 |
| L006e | relative strength 20d / 60d vs SPY | TLT | -3.17% / -3.97% | percent | 2026-08-27 | technical_indicators.py daily block (L013); formula: rules.md § Technical Indicator Pack Definition | DELAYED | DERIVED | 03 |
| L007 | VIX close | ^VIX | 14.51 | index | 2026-08-27 | quote.cnbc.com restQuote symbol .VIX — field `last`, gated on last_time 2026-08-27T16:15:01-0400 | DELAYED | OBSERVED | 03 (regime) |
| L007a | VIX close T-1 (cross-check) | ^VIX | 15.21 | index | 2026-08-26 | cdn.cboe.com/api/global/us_indices/daily_prices/VIX_History.csv last row 08/26/2026; equals CNBC previous_day_closing 15.21 to the cent — CBOE's file lags one session post-close | DELAYED | OBSERVED | 03 |
| L008 | risk-free rate (3m T-bill) | RF | 3.69 | percent annual | 08/27/2026 | https://home.treasury.gov/resource-center/data-chart-center/interest-rates/daily-treasury-rates.csv/2026/all?type=daily_treasury_bill_rates&field_tdr_date_value=2026&page&_format=csv — 13-week bank discount (DTB3 equivalent) | DELAYED | OBSERVED | 05 (Sharpe/Sortino/Treynor/Calmar) |
| L008a | FRED DTB3 fetch attempt | RF | FAILED — read operation timed out | n/a | 2026-08-27 | https://fred.stlouisfed.org/graph/fredgraph.csv?id=DTB3 — 9th consecutive session timing out; Treasury CSV (L008) is the standing fallback | UNAVAILABLE | OBSERVED | 01 |
| L009 | market cap + sector | 7103 listed issues | one screener call; B-shares keyed BRK/B, BF/B | USD / GICS-style label | 2026-08-27 | https://api.nasdaq.com/api/screener/stocks?tableonly=true&limit=10000&offset=0&download=true (Origin/Referer headers) retrieved_at 2026-08-27T16:11:46-0700 | DELAYED | OBSERVED | 04, 05, 07 |
| L010 | forward earnings calendar sweep | entire scored universe | 27/27 business days fetched, 0 transport failures, sweep_complete=True, 366 distinct symbols on calendar | count | 2026-08-27 .. 2026-10-03 | https://api.nasdaq.com/api/calendar/earnings?date=YYYY-MM-DD swept over every business day in [run_date, run_date+37d]; Track B accepted 2026-07-29 — absence is positive evidence only when the sweep is complete | DELAYED | OBSERVED | 03, 04, 05, 15 |
| L011 | entry-price cross-check (CNBC) | 27 published symbols | agreement with L002 to the cent on **26/27** *(was 27/27 — AMENDED 2026-08-27, see § Amendment)*; the exception is `TECH`, which L221 already tabulates at 0.0138% | USD | 2026-08-27 | https://quote.cnbc.com/quote-html-webservice/restQuote/symbolType/symbol — field `last` gated on last_time date == 2026-08-27 (market POST_MKT) | DELAYED | OBSERVED | 05, 06, 07, 15 |
| L012 | entry-price cross-check (Nasdaq) | 27 published symbols | max deviation vs L002 0.095123% | USD | 2026-08-27 | https://api.nasdaq.com/api/quote/{sym}/info — field `secondaryData.lastSalePrice` gated on the 'Closed at Aug 27, 2026 4:00 PM ET' marker (primaryData is the after-hours tape) | DELAYED | OBSERVED | 05, 06, 07, 15 |
| L012a | price grounding summary | 27 published symbols | 27/27 grounded on 3 independent sources, 0 confirmation re-reads | count | 2026-08-27 | DERIVED from L002 + L011 + L012 under rules.md § Price Sourcing Standard (two independent web sources agreeing within 1%) | DELAYED | DERIVED | 05, 06, 07, 08, 15 |
| L013 | technical indicator pack | 518 symbols (514 universe with history + 4 ETFs) | TD-9 / RSI(14) / MACD(12,26,9) / MA / momentum / volume / RS, daily+weekly+monthly | mixed | 2026-08-27 | python3 agents/equity/daily_investment_system/technical_indicators.py --tickers SPY QQQ SOXX TLT --tickers-file .work/claude-opus-5-2026-08-27/universe_with_history.txt --benchmark SPY --range 5y --history-dir <adjusted-close CSV tree> (formula: rules.md § Technical Indicator Pack Definition); input L002 | DELAYED | DERIVED | 05, 06, 07, 15 |
| L014 | canonical settlement ledger (pre-write) | ALL models | 1153 EQ + 174 MF canonical, 231 due, 0 conflicts | count | 2026-08-27 | python3 agents/equity/daily_investment_system/settlement_ledger.py --output-dir agents/equity/output --manifest-out .work/claude-opus-5-2026-08-27/settlement_manifest.json --as-of 2026-08-27 | DELAYED | DERIVED | 02 § 0, 13 |
| L014a | rolling calibration EQUITY_ALPHA (pre-write) | ALL models | n=1153, eff_n=2, hit 39.38%, CI 71.47%, mean z -0.5506 | mixed | 2026-08-27 | DERIVED from L014 | DELAYED | DERIVED | 02 § 0, 05 (calibration binding), 13 |
| L014b | rolling calibration MARKET_FORECAST (pre-write) | ALL models | n=174, eff_n=2, hit 35.71%, CI 90.23%, mean z -0.2952 | mixed | 2026-08-27 | DERIVED from L014 — reported separately from EQUITY_ALPHA per rules.md § Rolling Calibration Metrics | DELAYED | DERIVED | 02 § 0, 13 |
| L014c | rank IC by vintage (pre-write) | ALL models | 60 vintages, mean -0.0840, median -0.0567, 55.00% at or below zero | Spearman rho | 2026-08-27 | DERIVED from L014 — Spearman correlation of adj_score vs realized_alpha within each vintage | DELAYED | DERIVED | 02 § 0, 05 (confidence cap), 13 |
| L014d | settlements written this run | ALL models | 229 rows (WEEKEND_TARGET 26, ORDINARY 153, TARGET_DATE_CLOSE 50) | count | 2026-08-27 | DERIVED: due keys from L014 priced at the target-date close from L002; timing per rules.md § Settlement Rules | DELAYED | DERIVED | 02 § 0, 15 |
| L014e | canonical settlement ledger (post-write verification) | ALL models | EQ n=1355 eff_n=2, MF n=201 eff_n=2, due 2, conflicts 0, rejected 87 (unchanged) | count | 2026-08-27 | settlement_ledger.py re-run after 15_predictions.json was written; the 2 remaining due keys are the EQR corporate-action keys (L025) | DELAYED | DERIVED | 02 § 0, 08, 13 |
| L015 | MoM baseline selection | claude-opus-5-2026-07-30 | tie at delta 0d with gpt-5-2026-07-30; resolved by rule 8(a) same model family | folder | 2026-07-30 | agents.md § Orchestrator Step 2 (window 2026-07-13 .. 2026-08-06, target 2026-07-30) | HISTORICAL | DERIVED | 00, 02 |
| L016 | sleeve beta feasibility | published 24 | attainable [0.0090, 0.2919] vs band [0.90, 1.10] => feasible=False | beta | 2026-08-27 | DERIVED: 5% single-name cap => >=20 names; max attainable = mean of the 20 highest betas in the published pool; inputs L002, L003 | DELAYED | DERIVED | 07, 08 |
| L016a | avg pairwise correlation | published 24 | 0.1416 | ratio | 2026-08-27 | DERIVED: mean of all 276 pairwise correlations of 60d daily adjusted returns; input L002 | DELAYED | DERIVED | 07, 08 |
| L016b | naive top-20 EW 95th-pctl 1m drawdown | published top 20 | 0.063763 | decimal | 2026-08-27 | DERIVED: 1.65 x portfolio_sigma_1m (normality assumed), portfolio_sigma_1m = sqrt(w'Sigma w) x sqrt(21) on 60d daily adjusted returns; input L002 | DELAYED | DERIVED | 07, 08 |
| L016c | naive top-20 EW sleeve beta | published top 20 | 0.1633 | beta | 2026-08-27 | DERIVED: equal-weighted mean of the 20 highest-ranked published names' 60d betas; inputs L002, L003 | DELAYED | DERIVED | 07, 08 |
| L017 | brokerage market-data tool (IBKR MCP) | SPY/QQQ/SOXX | NOT ATTEMPTED | n/a | 2026-08-27 | The IBKR MCP connector has been in an invalidated state since 2026-08-04 ('connection was invalidated, user needs to reconnect') and was not reconnected; grounding stands on the three independent web sources L002/L011/L012 | UNAVAILABLE | OBSERVED | 01, 08 |
| L020 | data quality multiplier | ALL scored | 0.80 | multiplier | 2026-08-27 | rules.md § Data Quality Multiplier — 0.80 'notable coverage gaps': Fund_Z and Sent_Z UNAVAILABLE universe-wide (no fetch path wired; rules.md § SHADOW Diagnostic Tooling) | DELAYED | INFERRED | 05, 15 |
| L021 | Fundamental family | ALL scored | UNAVAILABLE | z-score | 2026-08-27 | No fetch path wired for the full universe. rules.md § SHADOW Diagnostic Tooling: fundamental_diagnostics.py exists but Phase 2 (bulk companyfacts across ~514 names) is not implemented, so the 70%-of-universe sourceability bar in rules.md § Financial Metrics is unmet | UNAVAILABLE | UNAVAILABLE | 05, 15 |
| L022 | Sentiment / positioning family | ALL scored | UNAVAILABLE | z-score | 2026-08-27 | No fetch path wired for the full universe (same plan Phase 2 as L021) | UNAVAILABLE | UNAVAILABLE | 05, 15 |
| L023 | Enhancing inputs | ALL scored | options IV/skew, short interest/borrow, bid-ask tape, analyst revision tape, institutional flow — all UNAVAILABLE | n/a | 2026-08-27 | rules.md § Input Classification — Enhancing inputs; never GO blockers, they cap confidence at MEDIUM and lower data quality | UNAVAILABLE | UNAVAILABLE | 00 (GO-gate caps), 05, 08 |
| L025 | corporate-action ledger | EQR, AVB, EA, FDXF | EQR=CORPORATE_ACTION_RENAMED (successor VMRK); AVB=CORPORATE_ACTION_DELISTED; EA=CORPORATE_ACTION_DELISTED; FDXF=TRANSIENT_FETCH_FAILURE | classification | 2026-08-27 | Track B accepted 2026-08-22, effective 2026-08-23: any symbol whose last bar predates the basis or whose fetch transport-fails is classified against two independent references (L009 screener presence + CNBC quote/name/exchange); inputs L002, L009 | DELAYED | DERIVED | 02 § 0, 04, 08, 13 |
| L025a | corporate-action / open-prediction intersection | EQR | 2 open prediction keys (claude-opus-5-2026-07-26 target 2026-08-23; gpt-5-2026-07-27 target 2026-08-24) reported UNSETTLEABLE_CORPORATE_ACTION and left due | count | 2026-08-27 | DERIVED: intersection of L025 with L014 due inventory; no exchange ratio inferred and no settlement against a successor symbol (explicit non-goal of the 2026-08-22 Track B) | DELAYED | DERIVED | 02 § 0, 08, 15 |
| L026 | symbol-reuse hazard (new this run) | EQR | CNBC returns a DIFFERENT security under the legacy US ticker: name 'EQ Resources Ltd', exchange ASX, last 0.41, last_time 2026-08-27, volume 0 | USD | 2026-08-27 | https://quote.cnbc.com/quote-html-webservice/restQuote/symbolType/symbol?symbols=EQR — the date gate alone (last_time == basis) accepts this row; only the `exchange` field distinguishes it. See 13_evolution_log.md. | DELAYED | OBSERVED | 08, 13 |
| L200 | entry price (raw close) | SJM | 131.84 | USD | 2026-08-27 | stockanalysis 5Y history (L002), cross-verified CNBC (L011) at 0.0000% and Nasdaq (L012) at 0.0190% deviation | DELAYED | OBSERVED | 05, 06, 07, 15 |
| L201 | entry price (raw close) | RVTY | 129.71 | USD | 2026-08-27 | stockanalysis 5Y history (L002), cross-verified CNBC (L011) at 0.0000% and Nasdaq (L012) at 0.0308% deviation | DELAYED | OBSERVED | 05, 06, 07, 15 |
| L202 | entry price (raw close) | GILD | 148.86 | USD | 2026-08-27 | stockanalysis 5Y history (L002), cross-verified CNBC (L011) at 0.0000% and Nasdaq (L012) at 0.0000% deviation | DELAYED | OBSERVED | 05, 06, 07, 15 |
| L203 | entry price (raw close) | BLK | 1167.57 | USD | 2026-08-27 | stockanalysis 5Y history (L002), cross-verified CNBC (L011) at 0.0000% and Nasdaq (L012) at 0.0291% deviation | DELAYED | OBSERVED | 05, 06, 07, 15 |
| L204 | entry price (raw close) | AMGN | 436.99 | USD | 2026-08-27 | stockanalysis 5Y history (L002), cross-verified CNBC (L011) at 0.0000% and Nasdaq (L012) at 0.0000% deviation | DELAYED | OBSERVED | 05, 06, 07, 15 |
| L205 | entry price (raw close) | JNJ | 265.77 | USD | 2026-08-27 | stockanalysis 5Y history (L002), cross-verified CNBC (L011) at 0.0000% and Nasdaq (L012) at 0.0000% deviation | DELAYED | OBSERVED | 05, 06, 07, 15 |
| L206 | entry price (raw close) | RMD | 235.76 | USD | 2026-08-27 | stockanalysis 5Y history (L002), cross-verified CNBC (L011) at 0.0000% and Nasdaq (L012) at 0.0297% deviation | DELAYED | OBSERVED | 05, 06, 07, 15 |
| L207 | entry price (raw close) | A | 157.69 | USD | 2026-08-27 | stockanalysis 5Y history (L002), cross-verified CNBC (L011) at 0.0000% and Nasdaq (L012) at 0.0951% deviation | DELAYED | OBSERVED | 05, 06, 07, 15 |
| L208 | entry price (raw close) | VEEV | 282.13 | USD | 2026-08-27 | stockanalysis 5Y history (L002), cross-verified CNBC (L011) at 0.0000% and Nasdaq (L012) at 0.0408% deviation | DELAYED | OBSERVED | 05, 06, 07, 15 |
| L209 | entry price (raw close) | NWSA | 31.19 | USD | 2026-08-27 | stockanalysis 5Y history (L002), cross-verified CNBC (L011) at 0.0000% and Nasdaq (L012) at 0.0000% deviation | DELAYED | OBSERVED | 05, 06, 07, 15 |
| L210 | entry price (raw close) | FTNT | 172.78 | USD | 2026-08-27 | stockanalysis 5Y history (L002), cross-verified CNBC (L011) at 0.0000% and Nasdaq (L012) at 0.0000% deviation | DELAYED | OBSERVED | 05, 06, 07, 15 |
| L211 | entry price (raw close) | STT | 193.37 | USD | 2026-08-27 | stockanalysis 5Y history (L002), cross-verified CNBC (L011) at 0.0000% and Nasdaq (L012) at 0.0440% deviation | DELAYED | OBSERVED | 05, 06, 07, 15 |
| L212 | entry price (raw close) | BNY | 162.24 | USD | 2026-08-27 | stockanalysis 5Y history (L002), cross-verified CNBC (L011) at 0.0000% and Nasdaq (L012) at 0.0000% deviation | DELAYED | OBSERVED | 05, 06, 07, 15 |
| L213 | entry price (raw close) | SCHW | 108.05 | USD | 2026-08-27 | stockanalysis 5Y history (L002), cross-verified CNBC (L011) at 0.0000% and Nasdaq (L012) at 0.0324% deviation | DELAYED | OBSERVED | 05, 06, 07, 15 |
| L214 | entry price (raw close) | NWS | 35.32 | USD | 2026-08-27 | stockanalysis 5Y history (L002), cross-verified CNBC (L011) at 0.0000% and Nasdaq (L012) at 0.0000% deviation | DELAYED | OBSERVED | 05, 06, 07, 15 |
| L215 | entry price (raw close) | VRTX | 547.55 | USD | 2026-08-27 | stockanalysis 5Y history (L002), cross-verified CNBC (L011) at 0.0000% and Nasdaq (L012) at 0.0000% deviation | DELAYED | OBSERVED | 05, 06, 07, 15 |
| L216 | entry price (raw close) | BAC | 61.17 | USD | 2026-08-27 | stockanalysis 5Y history (L002), cross-verified CNBC (L011) at 0.0000% and Nasdaq (L012) at 0.0163% deviation | DELAYED | OBSERVED | 05, 06, 07, 15 |
| L217 | entry price (raw close) | MPC | 363.54 | USD | 2026-08-27 | stockanalysis 5Y history (L002), cross-verified CNBC (L011) at 0.0000% and Nasdaq (L012) at 0.0000% deviation | DELAYED | OBSERVED | 05, 06, 07, 15 |
| L218 | entry price (raw close) | CRL | 296.41 | USD | 2026-08-27 | stockanalysis 5Y history (L002), cross-verified CNBC (L011) at 0.0000% and Nasdaq (L012) at 0.0169% deviation | DELAYED | OBSERVED | 05, 06, 07, 15 |
| L219 | entry price (raw close) | BMY | 66.95 | USD | 2026-08-27 | stockanalysis 5Y history (L002), cross-verified CNBC (L011) at 0.0000% and Nasdaq (L012) at 0.0075% deviation | DELAYED | OBSERVED | 05, 06, 07, 15 |
| L220 | entry price (raw close) | TGT | 165.93 | USD | 2026-08-27 | stockanalysis 5Y history (L002), cross-verified CNBC (L011) at 0.0000% and Nasdaq (L012) at 0.0181% deviation | DELAYED | OBSERVED | 05, 06, 07, 15 |
| L221 | entry price (raw close) | TECH | 72.48 | USD | 2026-08-27 | stockanalysis 5Y history (L002), cross-verified CNBC (L011) at 0.0138% and Nasdaq (L012) at 0.0138% deviation | DELAYED | OBSERVED | 05, 06, 07, 15 |
| L222 | entry price (raw close) | PFE | 28.02 | USD | 2026-08-27 | stockanalysis 5Y history (L002), cross-verified CNBC (L011) at 0.0000% and Nasdaq (L012) at 0.0357% deviation | DELAYED | OBSERVED | 05, 06, 07, 15 |
| L223 | entry price (raw close) | ABT | 111.59 | USD | 2026-08-27 | stockanalysis 5Y history (L002), cross-verified CNBC (L011) at 0.0000% and Nasdaq (L012) at 0.0269% deviation | DELAYED | OBSERVED | 05, 06, 07, 15 |
| L300 | realized vol 30d (sigma, 1m) | SJM | 0.086785 | decimal | 2026-08-27 | DERIVED: pstdev(30 daily adjusted returns) x sqrt(21); sigma_source REALIZED_VOL_30D per rules.md § Sigma Fallback Chain; input L002 | DELAYED | DERIVED | 05, 06, 07, 15 |
| L301 | realized vol 30d (sigma, 1m) | RVTY | 0.099287 | decimal | 2026-08-27 | DERIVED: pstdev(30 daily adjusted returns) x sqrt(21); sigma_source REALIZED_VOL_30D per rules.md § Sigma Fallback Chain; input L002 | DELAYED | DERIVED | 05, 06, 07, 15 |
| L302 | realized vol 30d (sigma, 1m) | GILD | 0.074741 | decimal | 2026-08-27 | DERIVED: pstdev(30 daily adjusted returns) x sqrt(21); sigma_source REALIZED_VOL_30D per rules.md § Sigma Fallback Chain; input L002 | DELAYED | DERIVED | 05, 06, 07, 15 |
| L303 | realized vol 30d (sigma, 1m) | BLK | 0.067642 | decimal | 2026-08-27 | DERIVED: pstdev(30 daily adjusted returns) x sqrt(21); sigma_source REALIZED_VOL_30D per rules.md § Sigma Fallback Chain; input L002 | DELAYED | DERIVED | 05, 06, 07, 15 |
| L304 | realized vol 30d (sigma, 1m) | AMGN | 0.077494 | decimal | 2026-08-27 | DERIVED: pstdev(30 daily adjusted returns) x sqrt(21); sigma_source REALIZED_VOL_30D per rules.md § Sigma Fallback Chain; input L002 | DELAYED | DERIVED | 05, 06, 07, 15 |
| L305 | realized vol 30d (sigma, 1m) | JNJ | 0.062017 | decimal | 2026-08-27 | DERIVED: pstdev(30 daily adjusted returns) x sqrt(21); sigma_source REALIZED_VOL_30D per rules.md § Sigma Fallback Chain; input L002 | DELAYED | DERIVED | 05, 06, 07, 15 |
| L306 | realized vol 30d (sigma, 1m) | RMD | 0.098546 | decimal | 2026-08-27 | DERIVED: pstdev(30 daily adjusted returns) x sqrt(21); sigma_source REALIZED_VOL_30D per rules.md § Sigma Fallback Chain; input L002 | DELAYED | DERIVED | 05, 06, 07, 15 |
| L307 | realized vol 30d (sigma, 1m) | A | 0.082609 | decimal | 2026-08-27 | DERIVED: pstdev(30 daily adjusted returns) x sqrt(21); sigma_source REALIZED_VOL_30D per rules.md § Sigma Fallback Chain; input L002 | DELAYED | DERIVED | 05, 06, 07, 15 |
| L308 | realized vol 30d (sigma, 1m) | VEEV | 0.166124 | decimal | 2026-08-27 | DERIVED: pstdev(30 daily adjusted returns) x sqrt(21); sigma_source REALIZED_VOL_30D per rules.md § Sigma Fallback Chain; input L002 | DELAYED | DERIVED | 05, 06, 07, 15 |
| L309 | realized vol 30d (sigma, 1m) | NWSA | 0.083912 | decimal | 2026-08-27 | DERIVED: pstdev(30 daily adjusted returns) x sqrt(21); sigma_source REALIZED_VOL_30D per rules.md § Sigma Fallback Chain; input L002 | DELAYED | DERIVED | 05, 06, 07, 15 |
| L310 | realized vol 30d (sigma, 1m) | FTNT | 0.124334 | decimal | 2026-08-27 | DERIVED: pstdev(30 daily adjusted returns) x sqrt(21); sigma_source REALIZED_VOL_30D per rules.md § Sigma Fallback Chain; input L002 | DELAYED | DERIVED | 05, 06, 07, 15 |
| L311 | realized vol 30d (sigma, 1m) | STT | 0.067374 | decimal | 2026-08-27 | DERIVED: pstdev(30 daily adjusted returns) x sqrt(21); sigma_source REALIZED_VOL_30D per rules.md § Sigma Fallback Chain; input L002 | DELAYED | DERIVED | 05, 06, 07, 15 |
| L312 | realized vol 30d (sigma, 1m) | BNY | 0.056026 | decimal | 2026-08-27 | DERIVED: pstdev(30 daily adjusted returns) x sqrt(21); sigma_source REALIZED_VOL_30D per rules.md § Sigma Fallback Chain; input L002 | DELAYED | DERIVED | 05, 06, 07, 15 |
| L313 | realized vol 30d (sigma, 1m) | SCHW | 0.056828 | decimal | 2026-08-27 | DERIVED: pstdev(30 daily adjusted returns) x sqrt(21); sigma_source REALIZED_VOL_30D per rules.md § Sigma Fallback Chain; input L002 | DELAYED | DERIVED | 05, 06, 07, 15 |
| L314 | realized vol 30d (sigma, 1m) | NWS | 0.087411 | decimal | 2026-08-27 | DERIVED: pstdev(30 daily adjusted returns) x sqrt(21); sigma_source REALIZED_VOL_30D per rules.md § Sigma Fallback Chain; input L002 | DELAYED | DERIVED | 05, 06, 07, 15 |
| L315 | realized vol 30d (sigma, 1m) | VRTX | 0.084308 | decimal | 2026-08-27 | DERIVED: pstdev(30 daily adjusted returns) x sqrt(21); sigma_source REALIZED_VOL_30D per rules.md § Sigma Fallback Chain; input L002 | DELAYED | DERIVED | 05, 06, 07, 15 |
| L316 | realized vol 30d (sigma, 1m) | BAC | 0.047855 | decimal | 2026-08-27 | DERIVED: pstdev(30 daily adjusted returns) x sqrt(21); sigma_source REALIZED_VOL_30D per rules.md § Sigma Fallback Chain; input L002 | DELAYED | DERIVED | 05, 06, 07, 15 |
| L317 | realized vol 30d (sigma, 1m) | MPC | 0.105852 | decimal | 2026-08-27 | DERIVED: pstdev(30 daily adjusted returns) x sqrt(21); sigma_source REALIZED_VOL_30D per rules.md § Sigma Fallback Chain; input L002 | DELAYED | DERIVED | 05, 06, 07, 15 |
| L318 | realized vol 30d (sigma, 1m) | CRL | 0.133155 | decimal | 2026-08-27 | DERIVED: pstdev(30 daily adjusted returns) x sqrt(21); sigma_source REALIZED_VOL_30D per rules.md § Sigma Fallback Chain; input L002 | DELAYED | DERIVED | 05, 06, 07, 15 |
| L319 | realized vol 30d (sigma, 1m) | BMY | 0.067266 | decimal | 2026-08-27 | DERIVED: pstdev(30 daily adjusted returns) x sqrt(21); sigma_source REALIZED_VOL_30D per rules.md § Sigma Fallback Chain; input L002 | DELAYED | DERIVED | 05, 06, 07, 15 |
| L320 | realized vol 30d (sigma, 1m) | TGT | 0.086430 | decimal | 2026-08-27 | DERIVED: pstdev(30 daily adjusted returns) x sqrt(21); sigma_source REALIZED_VOL_30D per rules.md § Sigma Fallback Chain; input L002 | DELAYED | DERIVED | 05, 06, 07, 15 |
| L321 | realized vol 30d (sigma, 1m) | TECH | 0.011834 | decimal | 2026-08-27 | DERIVED: pstdev(30 daily adjusted returns) x sqrt(21); sigma_source REALIZED_VOL_30D per rules.md § Sigma Fallback Chain; input L002 | DELAYED | DERIVED | 05, 06, 07, 15 |
| L322 | realized vol 30d (sigma, 1m) | PFE | 0.059241 | decimal | 2026-08-27 | DERIVED: pstdev(30 daily adjusted returns) x sqrt(21); sigma_source REALIZED_VOL_30D per rules.md § Sigma Fallback Chain; input L002 | DELAYED | DERIVED | 05, 06, 07, 15 |
| L323 | realized vol 30d (sigma, 1m) | ABT | 0.062425 | decimal | 2026-08-27 | DERIVED: pstdev(30 daily adjusted returns) x sqrt(21); sigma_source REALIZED_VOL_30D per rules.md § Sigma Fallback Chain; input L002 | DELAYED | DERIVED | 05, 06, 07, 15 |
| L400 | technical indicator pack | SJM | TD9 SELL_SETUP_9/SELL_SETUP_7/SELL_SETUP_2; RSI 72.13/74.47/62.99; MACD ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL; MA BULLISH/BULLISH/MIXED; mom20/60 +8.89%/+32.45%; RS20/60 +4.92%/+30.67%; vol ratio 1.69 | mixed | 2026-08-27 | technical_indicators.py (L013) on the adjusted-close tree (L002) | DELAYED | DERIVED | 05, 06, 07, 15 |
| L401 | technical indicator pack | RVTY | TD9 SELL_SETUP_7/SELL_SETUP_4/SELL_SETUP_3; RSI 72.24/71.60/60.14; MACD ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL; MA BULLISH/BULLISH/MIXED; mom20/60 +14.24%/+29.29%; RS20/60 +10.27%/+27.51%; vol ratio 1.28 | mixed | 2026-08-27 | technical_indicators.py (L013) on the adjusted-close tree (L002) | DELAYED | DERIVED | 05, 06, 07, 15 |
| L402 | technical indicator pack | GILD | TD9 SELL_SETUP_9/SELL_SETUP_4/SELL_SETUP_1; RSI 69.18/66.84/71.11; MACD ABOVE_SIGNAL/ABOVE_SIGNAL/BULLISH_CROSS; MA BULLISH/BULLISH/BULLISH; mom20/60 +13.39%/+17.46%; RS20/60 +9.42%/+15.68%; vol ratio 0.76 | mixed | 2026-08-27 | technical_indicators.py (L013) on the adjusted-close tree (L002) | DELAYED | DERIVED | 05, 06, 07, 15 |
| L403 | technical indicator pack | BLK | TD9 SELL_SETUP_5/SELL_SETUP_9/SELL_SETUP_2; RSI 61.03/62.38/61.23; MACD BELOW_SIGNAL/ABOVE_SIGNAL/BELOW_SIGNAL; MA BULLISH/BULLISH/BULLISH; mom20/60 +6.30%/+15.23%; RS20/60 +2.33%/+13.45%; vol ratio 1.32 | mixed | 2026-08-27 | technical_indicators.py (L013) on the adjusted-close tree (L002) | DELAYED | DERIVED | 05, 06, 07, 15 |
| L404 | technical indicator pack | AMGN | TD9 BUY_SETUP_1/SELL_SETUP_9/SELL_SETUP_2; RSI 68.94/74.38/71.79; MACD ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL; MA BULLISH/BULLISH/BULLISH; mom20/60 +13.39%/+33.90%; RS20/60 +9.42%/+32.12%; vol ratio 0.68 | mixed | 2026-08-27 | technical_indicators.py (L013) on the adjusted-close tree (L002) | DELAYED | DERIVED | 05, 06, 07, 15 |
| L405 | technical indicator pack | JNJ | TD9 BUY_SETUP_1/SELL_SETUP_4/SELL_SETUP_9; RSI 54.62/63.93/77.55; MACD ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL; MA BULLISH/BULLISH/BULLISH; mom20/60 +4.40%/+19.83%; RS20/60 +0.43%/+18.05%; vol ratio 1.10 | mixed | 2026-08-27 | technical_indicators.py (L013) on the adjusted-close tree (L002) | DELAYED | DERIVED | 05, 06, 07, 15 |
| L406 | technical indicator pack | RMD | TD9 SELL_SETUP_7/SELL_SETUP_5/SELL_SETUP_1; RSI 66.40/59.71/51.93; MACD ABOVE_SIGNAL/ABOVE_SIGNAL/BELOW_SIGNAL; MA BULLISH/MIXED/MIXED; mom20/60 +13.37%/+29.33%; RS20/60 +9.40%/+27.55%; vol ratio 1.02 | mixed | 2026-08-27 | technical_indicators.py (L013) on the adjusted-close tree (L002) | DELAYED | DERIVED | 05, 06, 07, 15 |
| L407 | technical indicator pack | A | TD9 BUY_SETUP_3/SELL_SETUP_8/SELL_SETUP_4; RSI 70.27/69.14/60.38; MACD ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL; MA BULLISH/MIXED/MIXED; mom20/60 +13.68%/+16.99%; RS20/60 +9.71%/+15.21%; vol ratio 1.67 | mixed | 2026-08-27 | technical_indicators.py (L013) on the adjusted-close tree (L002) | DELAYED | DERIVED | 05, 06, 07, 15 |
| L408 | technical indicator pack | VEEV | TD9 SELL_SETUP_1/SELL_SETUP_9/SELL_SETUP_2; RSI 79.57/73.59/60.55; MACD BULLISH_CROSS/ABOVE_SIGNAL/BELOW_SIGNAL; MA BULLISH/MIXED/BULLISH; mom20/60 +39.97%/+54.22%; RS20/60 +36.00%/+52.44%; vol ratio 3.27 | mixed | 2026-08-27 | technical_indicators.py (L013) on the adjusted-close tree (L002) | DELAYED | DERIVED | 05, 06, 07, 15 |
| L409 | technical indicator pack | NWSA | TD9 SELL_SETUP_9/SELL_SETUP_8/SELL_SETUP_3; RSI 71.28/69.40/62.49; MACD ABOVE_SIGNAL/ABOVE_SIGNAL/BELOW_SIGNAL; MA BULLISH/BULLISH/BULLISH; mom20/60 +11.04%/+18.10%; RS20/60 +7.07%/+16.32%; vol ratio 1.49 | mixed | 2026-08-27 | technical_indicators.py (L013) on the adjusted-close tree (L002) | DELAYED | DERIVED | 05, 06, 07, 15 |
| L410 | technical indicator pack | FTNT | TD9 SELL_SETUP_3/SELL_SETUP_2/SELL_SETUP_6; RSI 64.73/75.31/80.05; MACD BULLISH_CROSS/ABOVE_SIGNAL/ABOVE_SIGNAL; MA BULLISH/BULLISH/BULLISH; mom20/60 +12.01%/+16.07%; RS20/60 +8.04%/+14.29%; vol ratio 1.26 | mixed | 2026-08-27 | technical_indicators.py (L013) on the adjusted-close tree (L002) | DELAYED | DERIVED | 05, 06, 07, 15 |
| L411 | technical indicator pack | STT | TD9 SELL_SETUP_3/SELL_SETUP_9/SELL_SETUP_9; RSI 62.10/81.83/88.76; MACD BULLISH_CROSS/ABOVE_SIGNAL/ABOVE_SIGNAL; MA BULLISH/BULLISH/BULLISH; mom20/60 +5.77%/+21.63%; RS20/60 +1.80%/+19.85%; vol ratio 0.67 | mixed | 2026-08-27 | technical_indicators.py (L013) on the adjusted-close tree (L002) | DELAYED | DERIVED | 05, 06, 07, 15 |
| L412 | technical indicator pack | BNY | TD9 SELL_SETUP_3/SELL_SETUP_9/SELL_SETUP_9; RSI 57.46/75.98/91.33; MACD BELOW_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL; MA BULLISH/BULLISH/BULLISH; mom20/60 +3.95%/+15.29%; RS20/60 -0.02%/+13.51%; vol ratio 1.04 | mixed | 2026-08-27 | technical_indicators.py (L013) on the adjusted-close tree (L002) | DELAYED | DERIVED | 05, 06, 07, 15 |
| L413 | technical indicator pack | SCHW | TD9 BUY_SETUP_2/SELL_SETUP_9/SELL_SETUP_2; RSI 51.69/64.25/66.76; MACD BELOW_SIGNAL/ABOVE_SIGNAL/BULLISH_CROSS; MA MIXED/BULLISH/BULLISH; mom20/60 +3.87%/+23.69%; RS20/60 -0.10%/+21.91%; vol ratio 1.38 | mixed | 2026-08-27 | technical_indicators.py (L013) on the adjusted-close tree (L002) | DELAYED | DERIVED | 05, 06, 07, 15 |
| L414 | technical indicator pack | NWS | TD9 SELL_SETUP_9/SELL_SETUP_8/SELL_SETUP_3; RSI 70.10/67.64/61.99; MACD ABOVE_SIGNAL/ABOVE_SIGNAL/BELOW_SIGNAL; MA BULLISH/BULLISH/BULLISH; mom20/60 +11.07%/+17.03%; RS20/60 +7.10%/+15.25%; vol ratio 1.42 | mixed | 2026-08-27 | technical_indicators.py (L013) on the adjusted-close tree (L002) | DELAYED | DERIVED | 05, 06, 07, 15 |
| L415 | technical indicator pack | VRTX | TD9 BUY_SETUP_1/SELL_SETUP_4/SELL_SETUP_2; RSI 65.06/68.87/63.34; MACD ABOVE_SIGNAL/ABOVE_SIGNAL/BULLISH_CROSS; MA BULLISH/BULLISH/BULLISH; mom20/60 +13.67%/+28.81%; RS20/60 +9.70%/+27.03%; vol ratio 0.71 | mixed | 2026-08-27 | technical_indicators.py (L013) on the adjusted-close tree (L002) | DELAYED | DERIVED | 05, 06, 07, 15 |
| L416 | technical indicator pack | BAC | TD9 BUY_SETUP_1/BUY_SETUP_2/SELL_SETUP_3; RSI 43.15/62.35/70.00; MACD BELOW_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL; MA MIXED/BULLISH/BULLISH; mom20/60 -0.91%/+17.16%; RS20/60 -4.88%/+15.38%; vol ratio 1.64 | mixed | 2026-08-27 | technical_indicators.py (L013) on the adjusted-close tree (L002) | DELAYED | DERIVED | 05, 06, 07, 15 |
| L417 | technical indicator pack | MPC | TD9 SELL_SETUP_2/SELL_SETUP_9/SELL_SETUP_7; RSI 69.54/76.64/85.17; MACD ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL; MA BULLISH/BULLISH/BULLISH; mom20/60 +16.06%/+38.58%; RS20/60 +12.09%/+36.80%; vol ratio 1.16 | mixed | 2026-08-27 | technical_indicators.py (L013) on the adjusted-close tree (L002) | DELAYED | DERIVED | 05, 06, 07, 15 |
| L418 | technical indicator pack | CRL | TD9 SELL_SETUP_7/SELL_SETUP_9/SELL_SETUP_3; RSI 73.88/77.28/67.05; MACD BEARISH_CROSS/ABOVE_SIGNAL/ABOVE_SIGNAL; MA BULLISH/BULLISH/MIXED; mom20/60 +26.34%/+69.58%; RS20/60 +22.37%/+67.80%; vol ratio 0.93 | mixed | 2026-08-27 | technical_indicators.py (L013) on the adjusted-close tree (L002) | DELAYED | DERIVED | 05, 06, 07, 15 |
| L419 | technical indicator pack | BMY | TD9 BUY_SETUP_1/SELL_SETUP_9/SELL_SETUP_2; RSI 60.33/68.54/66.75; MACD ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL; MA BULLISH/BULLISH/BULLISH; mom20/60 +3.22%/+24.32%; RS20/60 -0.75%/+22.54%; vol ratio 0.43 | mixed | 2026-08-27 | technical_indicators.py (L013) on the adjusted-close tree (L002) | DELAYED | DERIVED | 05, 06, 07, 15 |
| L420 | technical indicator pack | TGT | TD9 SELL_SETUP_7/SELL_SETUP_5/SELL_SETUP_9; RSI 68.99/75.58/70.45; MACD ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL; MA BULLISH/BULLISH/MIXED; mom20/60 +15.70%/+35.74%; RS20/60 +11.73%/+33.96%; vol ratio 0.91 | mixed | 2026-08-27 | technical_indicators.py (L013) on the adjusted-close tree (L002) | DELAYED | DERIVED | 05, 06, 07, 15 |
| L421 | technical indicator pack | TECH | TD9 SELL_SETUP_2/SELL_SETUP_9/SELL_SETUP_3; RSI 69.49/65.96/55.49; MACD BELOW_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL; MA BULLISH/BULLISH/MIXED; mom20/60 +0.74%/+45.79%; RS20/60 -3.23%/+44.01%; vol ratio 0.61 | mixed | 2026-08-27 | technical_indicators.py (L013) on the adjusted-close tree (L002) | DELAYED | DERIVED | 05, 06, 07, 15 |
| L422 | technical indicator pack | PFE | TD9 BUY_SETUP_1/SELL_SETUP_6/SELL_SETUP_1; RSI 65.39/66.78/58.24; MACD ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL; MA BULLISH/BULLISH/MIXED; mom20/60 +12.48%/+11.59%; RS20/60 +8.51%/+9.81%; vol ratio 0.79 | mixed | 2026-08-27 | technical_indicators.py (L013) on the adjusted-close tree (L002) | DELAYED | DERIVED | 05, 06, 07, 15 |
| L423 | technical indicator pack | ABT | TD9 BUY_SETUP_2/SELL_SETUP_9/SELL_SETUP_2; RSI 57.65/60.30/50.65; MACD BELOW_SIGNAL/ABOVE_SIGNAL/BELOW_SIGNAL; MA BULLISH/MIXED/MIXED; mom20/60 +5.66%/+29.22%; RS20/60 +1.69%/+27.44%; vol ratio 0.95 | mixed | 2026-08-27 | technical_indicators.py (L013) on the adjusted-close tree (L002) | DELAYED | DERIVED | 05, 06, 07, 15 |
| L500 | beta / drawdown / tracking error (60d) | SJM | beta -0.6986; beta_TLT +0.7618; dd60 -0.084238; TE 0.104807 | mixed | 2026-08-27 | DERIVED: cov/var slope on 60 daily adjusted return intervals; dd60 = worst peak-to-trough over the 61 most recent adjusted closes; TE = pstdev(r - beta*r_SPY) x sqrt(21); inputs L002, L003 | DELAYED | DERIVED | 05, 06, 07, 15 |
| L501 | beta / drawdown / tracking error (60d) | RVTY | beta +0.4440; beta_TLT +0.7785; dd60 -0.063759; TE 0.103718 | mixed | 2026-08-27 | DERIVED: cov/var slope on 60 daily adjusted return intervals; dd60 = worst peak-to-trough over the 61 most recent adjusted closes; TE = pstdev(r - beta*r_SPY) x sqrt(21); inputs L002, L003 | DELAYED | DERIVED | 05, 06, 07, 15 |
| L502 | beta / drawdown / tracking error (60d) | GILD | beta +0.1043; beta_TLT +0.7683; dd60 -0.059607; TE 0.085230 | mixed | 2026-08-27 | DERIVED: cov/var slope on 60 daily adjusted return intervals; dd60 = worst peak-to-trough over the 61 most recent adjusted closes; TE = pstdev(r - beta*r_SPY) x sqrt(21); inputs L002, L003 | DELAYED | DERIVED | 05, 06, 07, 15 |
| L503 | beta / drawdown / tracking error (60d) | BLK | beta +0.8465; beta_TLT +0.6776; dd60 -0.101392; TE 0.074182 | mixed | 2026-08-27 | DERIVED: cov/var slope on 60 daily adjusted return intervals; dd60 = worst peak-to-trough over the 61 most recent adjusted closes; TE = pstdev(r - beta*r_SPY) x sqrt(21); inputs L002, L003 | DELAYED | DERIVED | 05, 06, 07, 15 |
| L504 | beta / drawdown / tracking error (60d) | AMGN | beta +0.1414; beta_TLT +0.9022; dd60 -0.050515; TE 0.078476 | mixed | 2026-08-27 | DERIVED: cov/var slope on 60 daily adjusted return intervals; dd60 = worst peak-to-trough over the 61 most recent adjusted closes; TE = pstdev(r - beta*r_SPY) x sqrt(21); inputs L002, L003 | DELAYED | DERIVED | 05, 06, 07, 15 |
| L505 | beta / drawdown / tracking error (60d) | JNJ | beta -0.7412; beta_TLT +0.2674; dd60 -0.075662; TE 0.067264 | mixed | 2026-08-27 | DERIVED: cov/var slope on 60 daily adjusted return intervals; dd60 = worst peak-to-trough over the 61 most recent adjusted closes; TE = pstdev(r - beta*r_SPY) x sqrt(21); inputs L002, L003 | DELAYED | DERIVED | 05, 06, 07, 15 |
| L506 | beta / drawdown / tracking error (60d) | RMD | beta +0.1495; beta_TLT +0.8940; dd60 -0.126780; TE 0.106070 | mixed | 2026-08-27 | DERIVED: cov/var slope on 60 daily adjusted return intervals; dd60 = worst peak-to-trough over the 61 most recent adjusted closes; TE = pstdev(r - beta*r_SPY) x sqrt(21); inputs L002, L003 | DELAYED | DERIVED | 05, 06, 07, 15 |
| L507 | beta / drawdown / tracking error (60d) | A | beta +0.3635; beta_TLT +0.4954; dd60 -0.101467; TE 0.081748 | mixed | 2026-08-27 | DERIVED: cov/var slope on 60 daily adjusted return intervals; dd60 = worst peak-to-trough over the 61 most recent adjusted closes; TE = pstdev(r - beta*r_SPY) x sqrt(21); inputs L002, L003 | DELAYED | DERIVED | 05, 06, 07, 15 |
| L508 | beta / drawdown / tracking error (60d) | VEEV | beta +0.4655; beta_TLT +0.5953; dd60 -0.162786; TE 0.148039 | mixed | 2026-08-27 | DERIVED: cov/var slope on 60 daily adjusted return intervals; dd60 = worst peak-to-trough over the 61 most recent adjusted closes; TE = pstdev(r - beta*r_SPY) x sqrt(21); inputs L002, L003 | DELAYED | DERIVED | 05, 06, 07, 15 |
| L509 | beta / drawdown / tracking error (60d) | NWSA | beta -0.3845; beta_TLT +0.2670; dd60 -0.097212; TE 0.081263 | mixed | 2026-08-27 | DERIVED: cov/var slope on 60 daily adjusted return intervals; dd60 = worst peak-to-trough over the 61 most recent adjusted closes; TE = pstdev(r - beta*r_SPY) x sqrt(21); inputs L002, L003 | DELAYED | DERIVED | 05, 06, 07, 15 |
| L510 | beta / drawdown / tracking error (60d) | FTNT | beta +1.1979; beta_TLT +0.0203; dd60 -0.103987; TE 0.108879 | mixed | 2026-08-27 | DERIVED: cov/var slope on 60 daily adjusted return intervals; dd60 = worst peak-to-trough over the 61 most recent adjusted closes; TE = pstdev(r - beta*r_SPY) x sqrt(21); inputs L002, L003 | DELAYED | DERIVED | 05, 06, 07, 15 |
| L511 | beta / drawdown / tracking error (60d) | STT | beta +0.6448; beta_TLT -0.0638; dd60 -0.056541; TE 0.065007 | mixed | 2026-08-27 | DERIVED: cov/var slope on 60 daily adjusted return intervals; dd60 = worst peak-to-trough over the 61 most recent adjusted closes; TE = pstdev(r - beta*r_SPY) x sqrt(21); inputs L002, L003 | DELAYED | DERIVED | 05, 06, 07, 15 |
| L512 | beta / drawdown / tracking error (60d) | BNY | beta +0.4917; beta_TLT -0.0698; dd60 -0.056933; TE 0.064157 | mixed | 2026-08-27 | DERIVED: cov/var slope on 60 daily adjusted return intervals; dd60 = worst peak-to-trough over the 61 most recent adjusted closes; TE = pstdev(r - beta*r_SPY) x sqrt(21); inputs L002, L003 | DELAYED | DERIVED | 05, 06, 07, 15 |
| L513 | beta / drawdown / tracking error (60d) | SCHW | beta -0.1050; beta_TLT -0.2064; dd60 -0.053645; TE 0.066151 | mixed | 2026-08-27 | DERIVED: cov/var slope on 60 daily adjusted return intervals; dd60 = worst peak-to-trough over the 61 most recent adjusted closes; TE = pstdev(r - beta*r_SPY) x sqrt(21); inputs L002, L003 | DELAYED | DERIVED | 05, 06, 07, 15 |
| L514 | beta / drawdown / tracking error (60d) | NWS | beta -0.4122; beta_TLT +0.2066; dd60 -0.104841; TE 0.085963 | mixed | 2026-08-27 | DERIVED: cov/var slope on 60 daily adjusted return intervals; dd60 = worst peak-to-trough over the 61 most recent adjusted closes; TE = pstdev(r - beta*r_SPY) x sqrt(21); inputs L002, L003 | DELAYED | DERIVED | 05, 06, 07, 15 |
| L515 | beta / drawdown / tracking error (60d) | VRTX | beta +0.1165; beta_TLT +0.8987; dd60 -0.111161; TE 0.086950 | mixed | 2026-08-27 | DERIVED: cov/var slope on 60 daily adjusted return intervals; dd60 = worst peak-to-trough over the 61 most recent adjusted closes; TE = pstdev(r - beta*r_SPY) x sqrt(21); inputs L002, L003 | DELAYED | DERIVED | 05, 06, 07, 15 |
| L516 | beta / drawdown / tracking error (60d) | BAC | beta +0.3191; beta_TLT +0.4041; dd60 -0.056164; TE 0.052888 | mixed | 2026-08-27 | DERIVED: cov/var slope on 60 daily adjusted return intervals; dd60 = worst peak-to-trough over the 61 most recent adjusted closes; TE = pstdev(r - beta*r_SPY) x sqrt(21); inputs L002, L003 | DELAYED | DERIVED | 05, 06, 07, 15 |
| L517 | beta / drawdown / tracking error (60d) | MPC | beta -0.2006; beta_TLT -0.9248; dd60 -0.090940; TE 0.102395 | mixed | 2026-08-27 | DERIVED: cov/var slope on 60 daily adjusted return intervals; dd60 = worst peak-to-trough over the 61 most recent adjusted closes; TE = pstdev(r - beta*r_SPY) x sqrt(21); inputs L002, L003 | DELAYED | DERIVED | 05, 06, 07, 15 |
| L518 | beta / drawdown / tracking error (60d) | CRL | beta +0.5021; beta_TLT +1.2415; dd60 -0.063784; TE 0.122024 | mixed | 2026-08-27 | DERIVED: cov/var slope on 60 daily adjusted return intervals; dd60 = worst peak-to-trough over the 61 most recent adjusted closes; TE = pstdev(r - beta*r_SPY) x sqrt(21); inputs L002, L003 | DELAYED | DERIVED | 05, 06, 07, 15 |
| L519 | beta / drawdown / tracking error (60d) | BMY | beta +0.0222; beta_TLT +0.5657; dd60 -0.057098; TE 0.085010 | mixed | 2026-08-27 | DERIVED: cov/var slope on 60 daily adjusted return intervals; dd60 = worst peak-to-trough over the 61 most recent adjusted closes; TE = pstdev(r - beta*r_SPY) x sqrt(21); inputs L002, L003 | DELAYED | DERIVED | 05, 06, 07, 15 |
| L520 | beta / drawdown / tracking error (60d) | TGT | beta +0.0147; beta_TLT +1.0609; dd60 -0.106941; TE 0.096404 | mixed | 2026-08-27 | DERIVED: cov/var slope on 60 daily adjusted return intervals; dd60 = worst peak-to-trough over the 61 most recent adjusted closes; TE = pstdev(r - beta*r_SPY) x sqrt(21); inputs L002, L003 | DELAYED | DERIVED | 05, 06, 07, 15 |
| L521 | beta / drawdown / tracking error (60d) | TECH | beta +0.6904; beta_TLT +0.9543; dd60 -0.040214; TE 0.133545 | mixed | 2026-08-27 | DERIVED: cov/var slope on 60 daily adjusted return intervals; dd60 = worst peak-to-trough over the 61 most recent adjusted closes; TE = pstdev(r - beta*r_SPY) x sqrt(21); inputs L002, L003 | DELAYED | DERIVED | 05, 06, 07, 15 |
| L522 | beta / drawdown / tracking error (60d) | PFE | beta +0.0138; beta_TLT +0.5905; dd60 -0.096910; TE 0.064150 | mixed | 2026-08-27 | DERIVED: cov/var slope on 60 daily adjusted return intervals; dd60 = worst peak-to-trough over the 61 most recent adjusted closes; TE = pstdev(r - beta*r_SPY) x sqrt(21); inputs L002, L003 | DELAYED | DERIVED | 05, 06, 07, 15 |
| L523 | beta / drawdown / tracking error (60d) | ABT | beta -0.4252; beta_TLT +0.4597; dd60 -0.071786; TE 0.094216 | mixed | 2026-08-27 | DERIVED: cov/var slope on 60 daily adjusted return intervals; dd60 = worst peak-to-trough over the 61 most recent adjusted closes; TE = pstdev(r - beta*r_SPY) x sqrt(21); inputs L002, L003 | DELAYED | DERIVED | 05, 06, 07, 15 |
| L600 | next earnings date | SJM | NO_PRINT_IN_WINDOW | date | 2026-08-27 | Complete forward calendar sweep (L010): absent from all 27 fetched business-day pages through 2026-10-03 | DELAYED | OBSERVED | 05, 06, 07, 15 |
| L601 | next earnings date | RVTY | NO_PRINT_IN_WINDOW | date | 2026-08-27 | Complete forward calendar sweep (L010): absent from all 27 fetched business-day pages through 2026-10-03 | DELAYED | OBSERVED | 05, 06, 07, 15 |
| L602 | next earnings date | GILD | NO_PRINT_IN_WINDOW | date | 2026-08-27 | Complete forward calendar sweep (L010): absent from all 27 fetched business-day pages through 2026-10-03 | DELAYED | OBSERVED | 05, 06, 07, 15 |
| L603 | next earnings date | BLK | NO_PRINT_IN_WINDOW | date | 2026-08-27 | Complete forward calendar sweep (L010): absent from all 27 fetched business-day pages through 2026-10-03 | DELAYED | OBSERVED | 05, 06, 07, 15 |
| L604 | next earnings date | AMGN | NO_PRINT_IN_WINDOW | date | 2026-08-27 | Complete forward calendar sweep (L010): absent from all 27 fetched business-day pages through 2026-10-03 | DELAYED | OBSERVED | 05, 06, 07, 15 |
| L605 | next earnings date | JNJ | NO_PRINT_IN_WINDOW | date | 2026-08-27 | Complete forward calendar sweep (L010): absent from all 27 fetched business-day pages through 2026-10-03 | DELAYED | OBSERVED | 05, 06, 07, 15 |
| L606 | next earnings date | RMD | NO_PRINT_IN_WINDOW | date | 2026-08-27 | Complete forward calendar sweep (L010): absent from all 27 fetched business-day pages through 2026-10-03 | DELAYED | OBSERVED | 05, 06, 07, 15 |
| L607 | next earnings date | A | NO_PRINT_IN_WINDOW | date | 2026-08-27 | Complete forward calendar sweep (L010): absent from all 27 fetched business-day pages through 2026-10-03 | DELAYED | OBSERVED | 05, 06, 07, 15 |
| L608 | next earnings date | VEEV | NO_PRINT_IN_WINDOW | date | 2026-08-27 | Complete forward calendar sweep (L010): absent from all 27 fetched business-day pages through 2026-10-03 | DELAYED | OBSERVED | 05, 06, 07, 15 |
| L609 | next earnings date | NWSA | NO_PRINT_IN_WINDOW | date | 2026-08-27 | Complete forward calendar sweep (L010): absent from all 27 fetched business-day pages through 2026-10-03 | DELAYED | OBSERVED | 05, 06, 07, 15 |
| L610 | next earnings date | FTNT | NO_PRINT_IN_WINDOW | date | 2026-08-27 | Complete forward calendar sweep (L010): absent from all 27 fetched business-day pages through 2026-10-03 | DELAYED | OBSERVED | 05, 06, 07, 15 |
| L611 | next earnings date | STT | NO_PRINT_IN_WINDOW | date | 2026-08-27 | Complete forward calendar sweep (L010): absent from all 27 fetched business-day pages through 2026-10-03 | DELAYED | OBSERVED | 05, 06, 07, 15 |
| L612 | next earnings date | BNY | NO_PRINT_IN_WINDOW | date | 2026-08-27 | Complete forward calendar sweep (L010): absent from all 27 fetched business-day pages through 2026-10-03 | DELAYED | OBSERVED | 05, 06, 07, 15 |
| L613 | next earnings date | SCHW | NO_PRINT_IN_WINDOW | date | 2026-08-27 | Complete forward calendar sweep (L010): absent from all 27 fetched business-day pages through 2026-10-03 | DELAYED | OBSERVED | 05, 06, 07, 15 |
| L614 | next earnings date | NWS | NO_PRINT_IN_WINDOW | date | 2026-08-27 | Complete forward calendar sweep (L010): absent from all 27 fetched business-day pages through 2026-10-03 | DELAYED | OBSERVED | 05, 06, 07, 15 |
| L615 | next earnings date | VRTX | NO_PRINT_IN_WINDOW | date | 2026-08-27 | Complete forward calendar sweep (L010): absent from all 27 fetched business-day pages through 2026-10-03 | DELAYED | OBSERVED | 05, 06, 07, 15 |
| L616 | next earnings date | BAC | NO_PRINT_IN_WINDOW | date | 2026-08-27 | Complete forward calendar sweep (L010): absent from all 27 fetched business-day pages through 2026-10-03 | DELAYED | OBSERVED | 05, 06, 07, 15 |
| L617 | next earnings date | MPC | NO_PRINT_IN_WINDOW | date | 2026-08-27 | Complete forward calendar sweep (L010): absent from all 27 fetched business-day pages through 2026-10-03 | DELAYED | OBSERVED | 05, 06, 07, 15 |
| L618 | next earnings date | CRL | NO_PRINT_IN_WINDOW | date | 2026-08-27 | Complete forward calendar sweep (L010): absent from all 27 fetched business-day pages through 2026-10-03 | DELAYED | OBSERVED | 05, 06, 07, 15 |
| L619 | next earnings date | BMY | NO_PRINT_IN_WINDOW | date | 2026-08-27 | Complete forward calendar sweep (L010): absent from all 27 fetched business-day pages through 2026-10-03 | DELAYED | OBSERVED | 05, 06, 07, 15 |
| L620 | next earnings date | TGT | NO_PRINT_IN_WINDOW | date | 2026-08-27 | Complete forward calendar sweep (L010): absent from all 27 fetched business-day pages through 2026-10-03 | DELAYED | OBSERVED | 05, 06, 07, 15 |
| L621 | next earnings date | TECH | NO_PRINT_IN_WINDOW | date | 2026-08-27 | Complete forward calendar sweep (L010): absent from all 27 fetched business-day pages through 2026-10-03 | DELAYED | OBSERVED | 05, 06, 07, 15 |
| L622 | next earnings date | PFE | NO_PRINT_IN_WINDOW | date | 2026-08-27 | Complete forward calendar sweep (L010): absent from all 27 fetched business-day pages through 2026-10-03 | DELAYED | OBSERVED | 05, 06, 07, 15 |
| L623 | next earnings date | ABT | NO_PRINT_IN_WINDOW | date | 2026-08-27 | Complete forward calendar sweep (L010): absent from all 27 fetched business-day pages through 2026-10-03 | DELAYED | OBSERVED | 05, 06, 07, 15 |

## Coverage summary

| freshness_tag | rows |
|---|---|
| `DELAYED` | 170 |
| `HISTORICAL` | 2 |
| `UNAVAILABLE` | 5 |
| `LIVE` | 0 |
| `OFFICIAL_FILING` | 0 |
| `ILLUSTRATIVE_REF` | 0 |

| claim_type | rows |
|---|---|
| `OBSERVED` | 64 |
| `DERIVED` | 109 |
| `INFERRED` | 1 |
| `UNAVAILABLE` | 3 |

Total ledger rows: **177**. The run is not in `ILLUSTRATIVE_MODE`; no row carries an
`ILLUSTRATIVE_REF` tag and no table in this package carries the illustrative banner.

## Documented failed or skipped fetches

| Source | Attempt | Outcome | Consequence |
|---|---|---|---|
| FRED `fredgraph.csv?id=DTB3` | 1 request, 45s timeout | read timeout (9th consecutive session) | Treasury daily-bill CSV fallback supplied 3m T-bill 3.69% (L008) |
| stockanalysis `EQR` 5Y history | 3 attempts with backoff | HTTP 400 Bad Request | classified `CORPORATE_ACTION_RENAMED` against two independent references (L025); the ticker is excluded from scoring and its 2 open prediction keys are left due (L025a) |
| IBKR MCP (`get_price_snapshot` / `get_price_history`) | not attempted | connector invalidated since 2026-08-04 | grounding stands on three independent web sources; recorded as an absence of evidence, not as agreement (L017) |
| FOMC meeting calendar | not attempted | no wired source | event-concentration section in `03` records the FOMC field as `UNAVAILABLE` rather than asserting an absence |

## Amendment — 2026-08-27 (second scheduled fire, 22:03 ET)

> **AMENDED 2026-08-27 (second scheduled fire ~22:03 ET, ~3h after the 19:09 package merged as
> PR #68).** The scheduled task fired a second time for the same `(model, date)`. Per the
> no-republish gate established 2026-08-01, a duplicate package would inject 24 `EQUITY_ALPHA` +
> 3 `MARKET_FORECAST` records with identical vintage, target date and entry prices into the
> ledger — perfectly correlated rows that inflate raw `n` while adding zero independent
> evidence. **No package was republished and no prediction record was added or altered.** All
> three gates were re-verified and held; this amendment corrects one over-claimed count found
> in the process. The `NO_TRADE` status and every downstream number are unchanged.

### Gate 1 — settlement inventory (nothing left to settle)

`settlement_ledger.py --as-of 2026-08-27` re-run to a scratchpad path reproduces the committed
manifest exactly: canonical `EQUITY_ALPHA` **1355**, `MARKET_FORECAST` **201**,
conflicts **0**, rejected rows **87**, audit-only
**268**, from **80** packages. Rolling metrics
re-derive to the committed § Reflection table to every published digit — EQ hit rate
**37.49%**, CI coverage **71.88%**, mean z
**-0.5553**, `eff_n` **2**; MF hit rate **40.11%**,
CI coverage **90.55%**, mean z **-0.1848**, `eff_n`
**2**.

`due_inventory` is **2**, and both keys are exactly the corporate-action
pair the 19:09 run documented as unsettleable (`EQR` claude-opus-5 vintage 2026-07-26 target 2026-08-23; `EQR` gpt-5 vintage 2026-07-27 target 2026-08-24). Nothing was left for this fire to
settle. The `eff_n` projection is unchanged and still falsifiable: EQ increments on
**2026-09-03** (24 pending), MF on
**2026-09-07** (3 pending).

### Gate 2 — same basis, and one genuine vendor drift

Markets were closed and the basis is unchanged, so a re-fetch must return the identical closes.
A fresh `stockanalysis .../history?range=5D` fetch and an independent CNBC sweep of all 27
published symbols each returned **26 of 27 exact to the cent**. The single exception is
`TECH` (Bio-Techne): published **72.48**, now **72.47** at all three vendors — stockanalysis
`c` and `a`, CNBC `last` (`last_time` 2026-08-27T16:00:00-0400, NASDAQ, volume 1,661,988) and
Nasdaq `primaryData.lastSalePrice`.

This is not a fetch error. At 19:09 ET stockanalysis's same-day bar carried a **preliminary**
close of 72.48 while CNBC and Nasdaq already carried the consolidated 72.47 — which is precisely
what row `L221` recorded at publication (both cross-checks at 0.0138%). By 22:03 ET
stockanalysis had converged to 72.47.

**The published `entry_price` of 72.48 is left unchanged, deliberately.** It was grounded when
observed (two independent sources within the 1% gate; the deviation is 0.0138%, and the run's
worst cross-vendor spread was 0.095123%), it is what the run actually saw, and rewriting a
merged package's entry price would break the property that a package records its own fire-time
observation — the property settlement integrity depends on. The residual effect is 1.38 bps on
one monitoring-sleeve name in a `NO_TRADE` run, or **0.012 sigma** against `TECH`'s sigma of
0.011834.

### Gate 3 — no early application of a future-effective change

The 19:09 run accepted one Track B change — the `SYMBOL_REUSE_FOREIGN_LISTING` price gate —
stamped **effective 2026-08-28** and flagged `HUMAN_REVIEW`. It was **not** applied here;
applying an accepted-but-not-yet-effective change inside a same-day duplicate is exactly what
the evolution log's comparability rationale forbids. It was exercised in verification only,
where it accepted all 27 published symbols (every one a US venue with non-zero volume,
`TECH` included) — consistent with the 27/27-accept, zero-false-reject result the log reports.

### What this amendment corrects

Row `L011` claimed CNBC agreement "to the cent on 27/27". The package's own row `L221`
simultaneously recorded `TECH`'s CNBC deviation as 0.0138% — so the summary count contradicted
the per-name evidence it summarizes. Counting the ledger's own entry-price rows gives 23 of 24
equity names at 0.0000% plus the three core ETFs, i.e. **26/27**. `L011` is corrected in place
with the original preserved. This is the "check counts you narrate, not just counts you
tabulate" error class: the count was asserted rather than computed from the rows beneath it.

**Nothing else changes.** The grounding gate is met either way — the standard is two independent
sources agreeing within 1%, and the worst spread in the run was 0.095123% — so GO-Gate row 1,
`L012a`, `03 § Hard halt 2` and `09 § 7` all remain accurate as written. Package integrity was
re-verified at **1,634 checks / 0 failures**, including the `15_predictions.json` contract, the
`MARKET_FORECAST` null contract, `composite_z` and `Adj Score` re-derived from
`score_explainability`, the 70% CI bounds re-derived at the `rules.md § Price and Target
Citation Standard` factor of 1.04, all 50 `TARGET_DATE_CLOSE` rows carrying timezone-aware
`settled_at` at or after 16:00 ET, and 66 markdown tables with zero column mismatches.

### Corpus check

`origin/main` is at `7c4a718` (PR #68) and nothing merged after it, so — unlike the 2026-08-01
third fire — no committed census or roster claim went stale on arrival.

### Carried forward to the next run

Post-close vendor precedence deserves a look. Nasdaq deviates from stockanalysis on many names
as an ordinary consolidated-tape artifact (0.0075%-0.0951% on 15 of the 24 equity ledger rows here), so its
disagreement is noise. **CNBC's disagreement is not**: CNBC matched stockanalysis on 23 of 24
equity names exactly, and the one name it flagged is the one where stockanalysis was carrying a
preliminary close. A candidate rule — *when CNBC and Nasdaq agree with each other against
stockanalysis on the basis bar, take their value* — is recorded here as an observation only. It
is **not** proposed as a change this run: `13_evolution_log.md` already accepted its one Track B
change for 2026-08-27 under the policy limit, and this fire publishes no package.
