# 01 — Preflight and Source Ledger — 2026-08-28

Model `claude-opus-5` · fire 2026-08-28T22:08:00-04:00 (POST_CLOSE, Friday) · price basis **2026-08-28** (same-day close).

Every fact used downstream by `02`–`07` and `15_predictions.json` appears below or is
explicitly `UNAVAILABLE`. *(AMENDED 2026-09-03: was "`02`–`09`, `13`, `14`" — the 2026-08-28
run truncated after `15_predictions.json` and never wrote `08`, `09`, `13` or `14`, so the
original sentence claimed lineage for artifacts that did not exist. `08`, `09` and `13` were
backfilled on 2026-09-03 from this package's own committed data and carry `BACKFILLED` banners;
`14` was deliberately not backfilled. No analytical content in `01`–`07` or `15_predictions.json`
changed.)* Working data lives in gitignored `agents/equity/.work/claude-opus-5-2026-08-28/` per
`runbook.md § Output Location and Naming`; this ledger carries every decision-relevant value inline
together with command and formula lineage, so the package is readable without those files.

## Fetch window and vendor state

- **Fire window.** 2026-08-28T22:08:00-04:00 — 6h08m after the 16:00 ET close. All three price
  vendors carry the settled consolidated close for 2026-08-28.
- **Bulk history.** `stockanalysis.com/api/symbol/{s\|e}/{SYM}/history?range=5Y` returned 518/519
  symbols in **12.7s** at 8 workers;
  516/518 last bars are dated 2026-08-28;
  **0** symbols carry an ex-dividend `c != a` split on the basis bar.
- **Yahoo Finance** was not used as a bulk source this run; `stockanalysis.com` has been the working
  primary since 2026-07-26 and needed no fallback.
- **IBKR MCP** — `UNAVAILABLE`, connector invalidated since 2026-08-04 (L020). Grounding stands on
  stockanalysis + CNBC + Nasdaq, three independent web sources.
- **Corporate-action classifier** ran over all 515 union members before scoring (L016).

## Grounding gate — Track B effective today

`rules.md § Price Sourcing Standard` requires two independent web sources agreeing within 1%. The
CNBC leg additionally runs the **three-part identity test accepted as Track B in
`claude-opus-5-2026-08-27/13_evolution_log.md`, effective 2026-08-28** — this run is the first to apply it:

> A CNBC row may be used as a **US equity/ETF price** only when (1) `last_time` date == the basis date,
> (2) `exchange` is a U.S. venue, and (3) `volume` > 0.

Result: **27/27** published symbols
grounded on three sources, max deviation **0.0000%**,
**0** confirmation re-reads, **zero** legitimate rows rejected. The gate
rejected exactly one row — `EQR`, returning *EQ Resources Ltd* on the **ASX** at 0.41 with `last_time`
on the basis date, which the previous date-only gate would have accepted. The hypothesis logged
yesterday ("rejects the symbol-reuse row while rejecting zero legitimate rows") is **confirmed**.

**Scope note.** The gate is written for *US equity/ETF price rows*. The `.VIX` index row reports
`exchange` = "Exchange" and no volume, so conditions (2) and (3) are inapplicable by construction;
`.VIX` is grounded on the `last_time` date gate plus the independent CBOE cross-check (L007, L007a),
which agree to the cent. This is a scoping clarification of the accepted rule, not a change to it.

## Source Ledger

| artifact | field | ticker/entity | value | unit | observation_date | source | freshness_tag | claim_type | used_by |
|---|---|---|---|---|---|---|---|---|---|
| L001 | index_union_count | S&P 500 union Nasdaq-100 | 515 | tickers | 2026-06-21 | build_index_universe.py from local constituent caches (helper run 2026-08-29T02:09:19Z UTC) | HISTORICAL | OBSERVED | 03, 04, 05 |
| L002 | sp500_cache_fetched_at | sp500.json | 2026-06-21T21:05:56Z | timestamp | 2026-06-21 | agents/equity/turtle-trader/universe/sp500.json | HISTORICAL | OBSERVED | 04 |
| L003 | nasdaq100_cache_fetched_at | nasdaq100.json | 2026-06-21T21:05:56Z | timestamp | 2026-06-21 | agents/equity/turtle-trader/universe/nasdaq100.json | HISTORICAL | OBSERVED | 04 |
| L004 | bulk_history_coverage | universe + core ETFs | 518/519 symbols, 5y daily bars | symbols | 2026-08-28 | stockanalysis.com/api/symbol/{s\|e}/{SYM}/history?range=5Y | DELAYED | OBSERVED | 03, 04, 05, 07 |
| L005 | bulk_history_basis_bars | universe + core ETFs | 516/518 last bars on 2026-08-28 | symbols | 2026-08-28 | stockanalysis.com/api/symbol/{s\|e}/{SYM}/history?range=5Y | DELAYED | OBSERVED | 01, 03 |
| L006 | ex_dividend_basis_bar_count | universe + core ETFs | 0 | symbols | 2026-08-28 | stockanalysis.com/api/symbol/{s\|e}/{SYM}/history?range=5Y last-bar raw close c vs adjusted close a | DELAYED | DERIVED | 01, 05 |
| L007 | vix_close | VIX | 14.43 | index level | 2026-08-28 | cdn.cboe.com/api/global/us_indices/daily_prices/VIX_History.csv | DELAYED | OBSERVED | 03 |
| L007a | vix_close_crosscheck | VIX | 14.43 | index level | 2026-08-28 | quote.cnbc.com/quote-html-webservice/restQuote/symbolType/symbol symbol .VIX, `last` gated on `last_time` date == basis | DELAYED | OBSERVED | 03 |
| L007b | vix_prior_close | VIX | 14.51 | index level | 2026-08-27 | CBOE VIX_History.csv row 2026-08-27; equals CNBC `previous_day_closing` 14.51 to the cent | DELAYED | OBSERVED | 03 |
| L008 | risk_free_13w | US 3-month T-bill | 3.74 | percent annual | 2026-08-28 | home.treasury.gov daily_treasury_bill_rates 2026, 13 WEEKS BANK DISCOUNT (FRED fredgraph.csv timed out - 10th consecutive) | DELAYED | OBSERVED | 05, 07 |
| L009 | earnings_calendar_sweep | universe | 26/26 business days 2026-08-28..2026-10-04, zero transport failures | business days | 2026-08-28 | api.nasdaq.com/api/calendar/earnings?date=YYYY-MM-DD | DELAYED | OBSERVED | 05, 08 |
| L010 | market_cap_and_sector | universe | 7132 rows | records | 2026-08-28 | api.nasdaq.com/api/screener/stocks | DELAYED | OBSERVED | 04, 05, 07 |
| L011 | price_crosscheck_cnbc | published set + core ETFs | 27/27 exact to the cent vs stockanalysis | symbols | 2026-08-28 | quote.cnbc.com/quote-html-webservice/restQuote/symbolType/symbol `last` gated on the three-part identity test | DELAYED | DERIVED | 01, 03, 08 |
| L011a | price_crosscheck_nasdaq | published set + core ETFs | 27/27 exact to the cent vs stockanalysis | symbols | 2026-08-28 | api.nasdaq.com/api/quote/{sym}/info primaryData.lastSalePrice, bare-date marker == basis | DELAYED | DERIVED | 01, 03, 08 |
| L012 | grounding_gate_result | published set + core ETFs | 27/27 grounded on 3 independent sources; max deviation 0.0000%; 0 confirmation re-reads | symbols | 2026-08-28 | rules.md section Price Sourcing Standard requirement 1 (two independent web sources within 1%) | DELAYED | DERIVED | 03, 08, 09 |
| L013 | technical_indicator_pack | universe + core ETFs | 519 tickers, status OK, as_of 2026-08-28 | tickers | 2026-08-28 | technical_indicators.py --tickers SPY QQQ SOXX TLT --tickers-file helper_tickers.txt --benchmark SPY --range 5y --history-dir history_adj/ | DELAYED | DERIVED | 05, 06, 07 |
| L014 | canonical_settlement_ledger | all packages | 1355 EQUITY_ALPHA + 201 MARKET_FORECAST canonical; 0 conflicts; 87 rejected rows; 80 packages | settlements | 2026-08-28 | settlement_ledger.py --output-dir agents/equity/output --as-of 2026-08-28 | DELAYED | DERIVED | 02, 13 |
| L014a | rolling_metrics_equity_alpha | EQUITY_ALPHA | n=1355, eff_n=2, hit=37.49%, CI cov=71.88%, mean z=-0.5553 | metrics | 2026-08-28 | settlement_manifest.json rolling_metrics.equity_alpha | DELAYED | DERIVED | 02, 05, 13 |
| L014b | rolling_metrics_market_forecast | MARKET_FORECAST | n=201, eff_n=2, hit=40.11%, CI cov=90.55%, mean z=-0.1848 | metrics | 2026-08-28 | settlement_manifest.json rolling_metrics.market_forecast | DELAYED | DERIVED | 02, 03, 13 |
| L014c | rank_ic_aggregate | EQUITY_ALPHA | weighted mean -0.0495 over 69 vintages; median -0.0496; 38 negative | Spearman | 2026-08-28 | settlement_manifest.json rolling_metrics.rank_ic_by_vintage | DELAYED | DERIVED | 02, 05, 13 |
| L014d | due_inventory | all packages | 2 keys due at as_of 2026-08-28; both are EQR corporate-action keys | keys | 2026-08-28 | settlement_ledger.py due_inventory | DELAYED | DERIVED | 02, 15 |
| L015 | mom_baseline_folder | claude-opus-5-2026-07-30 | delta 1d from target 2026-07-31, age 29d, flag OK | folder | 2026-07-30 | agents.md section Orchestrator Step 2 baseline algorithm | HISTORICAL | DERIVED | 02, 09 |
| L016 | corporate_action_ledger | EQR, AVB, EA | EQR CORPORATE_ACTION_RENAMED (to VMRK) + SYMBOL_REUSE_FOREIGN_LISTING on the CNBC tape; AVB CORPORATE_ACTION_DELISTED (last bar 2026-08-14); EA CORPORATE_ACTION_DELISTED (last bar 2026-08-04) | symbols | 2026-08-28 | stockanalysis.com/api/symbol/{s\|e}/{SYM}/history?range=5Y fetch result + api.nasdaq.com/api/screener/stocks absence + quote.cnbc.com/quote-html-webservice/restQuote/symbolType/symbol identity fields | DELAYED | DERIVED | 04, 08, 13 |
| L017 | spy_benchmark_price | SPY | 769.35 | USD | 2026-08-28 | stockanalysis.com/api/symbol/{s\|e}/{SYM}/history?range=5Y last raw close; CNBC and Nasdaq agree to the cent | DELAYED | OBSERVED | 02, 05, 15 |
| L018 | fund_z_availability | universe | UNAVAILABLE - no fetch path wired at universe scale | family | 2026-08-28 | rules.md section SHADOW Diagnostic Tooling; Phase 2 bulk companyfacts not attempted | UNAVAILABLE | UNAVAILABLE | 05, 08, 09 |
| L019 | sent_z_availability | universe | UNAVAILABLE - no fetch path wired at universe scale | family | 2026-08-28 | rules.md section SHADOW Diagnostic Tooling; Phase 2 threaded Nasdaq fetch not attempted | UNAVAILABLE | UNAVAILABLE | 05, 08, 09 |
| L020 | ibkr_market_data | brokerage MCP | UNAVAILABLE - connector invalidated since 2026-08-04; not attempted this run | tool | 2026-08-28 | IBKR MCP get_price_snapshot / get_price_history | UNAVAILABLE | UNAVAILABLE | 01, 08 |
| L021 | data_quality_multiplier | all scored names | 0.8 | multiplier | 2026-08-28 | rules.md section Data Quality Multiplier: 0.80 = notable coverage gaps (2 of 4 factor families UNAVAILABLE) | DELAYED | INFERRED | 05, 08 |
| L022 | earnings_penalty_census | universe | 15 of 510 scored names print within 14 calendar days; 27 print anywhere in the 26-business-day window | names | 2026-08-28 | api.nasdaq.com/api/calendar/earnings?date=YYYY-MM-DD | DELAYED | DERIVED | 05, 08 |
| L200 | entry_price | RJF | 179.36 | USD | 2026-08-28 | stockanalysis.com/api/symbol/{s\|e}/{SYM}/history?range=5Y last raw close c; CNBC 179.36; Nasdaq 179.36 | DELAYED | OBSERVED | 05, 06, 07, 15 |
| L201 | entry_price | SCHW | 110.16 | USD | 2026-08-28 | stockanalysis.com/api/symbol/{s\|e}/{SYM}/history?range=5Y last raw close c; CNBC 110.16; Nasdaq 110.16 | DELAYED | OBSERVED | 05, 06, 07, 15 |
| L202 | entry_price | BLK | 1164.48 | USD | 2026-08-28 | stockanalysis.com/api/symbol/{s\|e}/{SYM}/history?range=5Y last raw close c; CNBC 1164.48; Nasdaq 1164.48 | DELAYED | OBSERVED | 05, 06, 07, 15 |
| L203 | entry_price | RVTY | 128.80 | USD | 2026-08-28 | stockanalysis.com/api/symbol/{s\|e}/{SYM}/history?range=5Y last raw close c; CNBC 128.80; Nasdaq 128.80 | DELAYED | OBSERVED | 05, 06, 07, 15 |
| L204 | entry_price | SJM | 132.34 | USD | 2026-08-28 | stockanalysis.com/api/symbol/{s\|e}/{SYM}/history?range=5Y last raw close c; CNBC 132.34; Nasdaq 132.34 | DELAYED | OBSERVED | 05, 06, 07, 15 |
| L205 | entry_price | APD | 308.09 | USD | 2026-08-28 | stockanalysis.com/api/symbol/{s\|e}/{SYM}/history?range=5Y last raw close c; CNBC 308.09; Nasdaq 308.09 | DELAYED | OBSERVED | 05, 06, 07, 15 |
| L206 | entry_price | BDX | 189.52 | USD | 2026-08-28 | stockanalysis.com/api/symbol/{s\|e}/{SYM}/history?range=5Y last raw close c; CNBC 189.52; Nasdaq 189.52 | DELAYED | OBSERVED | 05, 06, 07, 15 |
| L207 | entry_price | BNY | 162.50 | USD | 2026-08-28 | stockanalysis.com/api/symbol/{s\|e}/{SYM}/history?range=5Y last raw close c; CNBC 162.50; Nasdaq 162.50 | DELAYED | OBSERVED | 05, 06, 07, 15 |
| L208 | entry_price | IQV | 261.75 | USD | 2026-08-28 | stockanalysis.com/api/symbol/{s\|e}/{SYM}/history?range=5Y last raw close c; CNBC 261.75; Nasdaq 261.75 | DELAYED | OBSERVED | 05, 06, 07, 15 |
| L209 | entry_price | GIS | 41.55 | USD | 2026-08-28 | stockanalysis.com/api/symbol/{s\|e}/{SYM}/history?range=5Y last raw close c; CNBC 41.55; Nasdaq 41.55 | DELAYED | OBSERVED | 05, 06, 07, 15 |
| L210 | entry_price | NWSA | 30.97 | USD | 2026-08-28 | stockanalysis.com/api/symbol/{s\|e}/{SYM}/history?range=5Y last raw close c; CNBC 30.97; Nasdaq 30.97 | DELAYED | OBSERVED | 05, 06, 07, 15 |
| L211 | entry_price | NDAQ | 99.31 | USD | 2026-08-28 | stockanalysis.com/api/symbol/{s\|e}/{SYM}/history?range=5Y last raw close c; CNBC 99.31; Nasdaq 99.31 | DELAYED | OBSERVED | 05, 06, 07, 15 |
| L212 | entry_price | NWS | 34.85 | USD | 2026-08-28 | stockanalysis.com/api/symbol/{s\|e}/{SYM}/history?range=5Y last raw close c; CNBC 34.85; Nasdaq 34.85 | DELAYED | OBSERVED | 05, 06, 07, 15 |
| L213 | entry_price | VEEV | 276.69 | USD | 2026-08-28 | stockanalysis.com/api/symbol/{s\|e}/{SYM}/history?range=5Y last raw close c; CNBC 276.69; Nasdaq 276.69 | DELAYED | OBSERVED | 05, 06, 07, 15 |
| L214 | entry_price | A | 153.84 | USD | 2026-08-28 | stockanalysis.com/api/symbol/{s\|e}/{SYM}/history?range=5Y last raw close c; CNBC 153.84; Nasdaq 153.84 | DELAYED | OBSERVED | 05, 06, 07, 15 |
| L215 | entry_price | RMD | 240.33 | USD | 2026-08-28 | stockanalysis.com/api/symbol/{s\|e}/{SYM}/history?range=5Y last raw close c; CNBC 240.33; Nasdaq 240.33 | DELAYED | OBSERVED | 05, 06, 07, 15 |
| L216 | entry_price | ABT | 112.47 | USD | 2026-08-28 | stockanalysis.com/api/symbol/{s\|e}/{SYM}/history?range=5Y last raw close c; CNBC 112.47; Nasdaq 112.47 | DELAYED | OBSERVED | 05, 06, 07, 15 |
| L217 | entry_price | STT | 193.33 | USD | 2026-08-28 | stockanalysis.com/api/symbol/{s\|e}/{SYM}/history?range=5Y last raw close c; CNBC 193.33; Nasdaq 193.33 | DELAYED | OBSERVED | 05, 06, 07, 15 |
| L218 | entry_price | JNJ | 268.04 | USD | 2026-08-28 | stockanalysis.com/api/symbol/{s\|e}/{SYM}/history?range=5Y last raw close c; CNBC 268.04; Nasdaq 268.04 | DELAYED | OBSERVED | 05, 06, 07, 15 |
| L219 | entry_price | VRTX | 541.69 | USD | 2026-08-28 | stockanalysis.com/api/symbol/{s\|e}/{SYM}/history?range=5Y last raw close c; CNBC 541.69; Nasdaq 541.69 | DELAYED | OBSERVED | 05, 06, 07, 15 |
| L220 | entry_price | NEM | 127.98 | USD | 2026-08-28 | stockanalysis.com/api/symbol/{s\|e}/{SYM}/history?range=5Y last raw close c; CNBC 127.98; Nasdaq 127.98 | DELAYED | OBSERVED | 05, 06, 07, 15 |
| L221 | entry_price | AMP | 559.32 | USD | 2026-08-28 | stockanalysis.com/api/symbol/{s\|e}/{SYM}/history?range=5Y last raw close c; CNBC 559.32; Nasdaq 559.32 | DELAYED | OBSERVED | 05, 06, 07, 15 |
| L222 | entry_price | NOW | 144.71 | USD | 2026-08-28 | stockanalysis.com/api/symbol/{s\|e}/{SYM}/history?range=5Y last raw close c; CNBC 144.71; Nasdaq 144.71 | DELAYED | OBSERVED | 05, 06, 07, 15 |
| L223 | entry_price | ICE | 162.33 | USD | 2026-08-28 | stockanalysis.com/api/symbol/{s\|e}/{SYM}/history?range=5Y last raw close c; CNBC 162.33; Nasdaq 162.33 | DELAYED | OBSERVED | 05, 06, 07, 15 |
| L300 | technical_indicator_pack | RJF | TD9 d/w/m SELL_SETUP_3/SELL_SETUP_9/SELL_SETUP_2; RSI14 58.60/65.28/62.54; MACD BELOW_SIGNAL/ABOVE_SIGNAL/BULLISH_CROSS; MA align d/w BULLISH/BULLISH | states | 2026-08-28 | technical_indicators.py on history_adj/ CSVs (see L013, L004) | DELAYED | DERIVED | 05, 06, 07, 15 |
| L301 | technical_indicator_pack | SCHW | TD9 d/w/m BUY_SETUP_3/SELL_SETUP_9/SELL_SETUP_2; RSI14 57.26/68.35/67.81; MACD BELOW_SIGNAL/ABOVE_SIGNAL/BULLISH_CROSS; MA align d/w BULLISH/BULLISH | states | 2026-08-28 | technical_indicators.py on history_adj/ CSVs (see L013, L004) | DELAYED | DERIVED | 05, 06, 07, 15 |
| L302 | technical_indicator_pack | BLK | TD9 d/w/m BUY_SETUP_1/SELL_SETUP_9/SELL_SETUP_2; RSI14 59.90/62.10/61.08; MACD BELOW_SIGNAL/ABOVE_SIGNAL/BELOW_SIGNAL; MA align d/w BULLISH/BULLISH | states | 2026-08-28 | technical_indicators.py on history_adj/ CSVs (see L013, L004) | DELAYED | DERIVED | 05, 06, 07, 15 |
| L303 | technical_indicator_pack | RVTY | TD9 d/w/m SELL_SETUP_8/SELL_SETUP_4/SELL_SETUP_3; RSI14 69.84/71.13/59.83; MACD ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL; MA align d/w BULLISH/BULLISH | states | 2026-08-28 | technical_indicators.py on history_adj/ CSVs (see L013, L004) | DELAYED | DERIVED | 05, 06, 07, 15 |
| L304 | technical_indicator_pack | SJM | TD9 d/w/m SELL_SETUP_9/SELL_SETUP_7/SELL_SETUP_2; RSI14 72.68/74.74/63.18; MACD ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL; MA align d/w BULLISH/BULLISH | states | 2026-08-28 | technical_indicators.py on history_adj/ CSVs (see L013, L004) | DELAYED | DERIVED | 05, 06, 07, 15 |
| L305 | technical_indicator_pack | APD | TD9 d/w/m SELL_SETUP_6/SELL_SETUP_4/SELL_SETUP_8; RSI14 58.03/59.93/58.12; MACD BULLISH_CROSS/ABOVE_SIGNAL/ABOVE_SIGNAL; MA align d/w BULLISH/BULLISH | states | 2026-08-28 | technical_indicators.py on history_adj/ CSVs (see L013, L004) | DELAYED | DERIVED | 05, 06, 07, 15 |
| L306 | technical_indicator_pack | BDX | TD9 d/w/m BUY_SETUP_2/SELL_SETUP_9/SELL_SETUP_2; RSI14 70.05/70.20/60.81; MACD BELOW_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL; MA align d/w BULLISH/BULLISH | states | 2026-08-28 | technical_indicators.py on history_adj/ CSVs (see L013, L004) | DELAYED | DERIVED | 05, 06, 07, 15 |
| L307 | technical_indicator_pack | BNY | TD9 d/w/m SELL_SETUP_4/SELL_SETUP_9/SELL_SETUP_9; RSI14 57.98/76.13/91.36; MACD BELOW_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL; MA align d/w BULLISH/BULLISH | states | 2026-08-28 | technical_indicators.py on history_adj/ CSVs (see L013, L004) | DELAYED | DERIVED | 05, 06, 07, 15 |
| L308 | technical_indicator_pack | IQV | TD9 d/w/m SELL_SETUP_8/SELL_SETUP_9/SELL_SETUP_3; RSI14 72.36/73.07/61.86; MACD ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL; MA align d/w BULLISH/MIXED | states | 2026-08-28 | technical_indicators.py on history_adj/ CSVs (see L013, L004) | DELAYED | DERIVED | 05, 06, 07, 15 |
| L309 | technical_indicator_pack | GIS | TD9 d/w/m SELL_SETUP_3/SELL_SETUP_4/SELL_SETUP_1; RSI14 67.38/61.82/42.07; MACD ABOVE_SIGNAL/ABOVE_SIGNAL/BELOW_SIGNAL; MA align d/w BULLISH/MIXED | states | 2026-08-28 | technical_indicators.py on history_adj/ CSVs (see L013, L004) | DELAYED | DERIVED | 05, 06, 07, 15 |
| L310 | technical_indicator_pack | NWSA | TD9 d/w/m SELL_SETUP_9/SELL_SETUP_8/SELL_SETUP_3; RSI14 68.15/68.78/62.08; MACD ABOVE_SIGNAL/ABOVE_SIGNAL/BELOW_SIGNAL; MA align d/w BULLISH/BULLISH | states | 2026-08-28 | technical_indicators.py on history_adj/ CSVs (see L013, L004) | DELAYED | DERIVED | 05, 06, 07, 15 |
| L311 | technical_indicator_pack | NDAQ | TD9 d/w/m SELL_SETUP_7/SELL_SETUP_7/SELL_SETUP_2; RSI14 69.08/62.82/61.38; MACD ABOVE_SIGNAL/ABOVE_SIGNAL/BELOW_SIGNAL; MA align d/w BULLISH/BULLISH | states | 2026-08-28 | technical_indicators.py on history_adj/ CSVs (see L013, L004) | DELAYED | DERIVED | 05, 06, 07, 15 |
| L312 | technical_indicator_pack | NWS | TD9 d/w/m BUY_SETUP_1/SELL_SETUP_8/SELL_SETUP_3; RSI14 64.48/66.46/61.28; MACD ABOVE_SIGNAL/ABOVE_SIGNAL/BELOW_SIGNAL; MA align d/w BULLISH/BULLISH | states | 2026-08-28 | technical_indicators.py on history_adj/ CSVs (see L013, L004) | DELAYED | DERIVED | 05, 06, 07, 15 |
| L313 | technical_indicator_pack | VEEV | TD9 d/w/m SELL_SETUP_2/SELL_SETUP_9/SELL_SETUP_2; RSI14 74.85/72.75/59.83; MACD ABOVE_SIGNAL/ABOVE_SIGNAL/BELOW_SIGNAL; MA align d/w BULLISH/MIXED | states | 2026-08-28 | technical_indicators.py on history_adj/ CSVs (see L013, L004) | DELAYED | DERIVED | 05, 06, 07, 15 |
| L314 | technical_indicator_pack | A | TD9 d/w/m SELL_SETUP_1/SELL_SETUP_8/SELL_SETUP_4; RSI14 61.01/65.27/59.19; MACD ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL; MA align d/w BULLISH/MIXED | states | 2026-08-28 | technical_indicators.py on history_adj/ CSVs (see L013, L004) | DELAYED | DERIVED | 05, 06, 07, 15 |
| L315 | technical_indicator_pack | RMD | TD9 d/w/m SELL_SETUP_8/SELL_SETUP_5/SELL_SETUP_1; RSI14 69.57/61.48/53.00; MACD ABOVE_SIGNAL/ABOVE_SIGNAL/BELOW_SIGNAL; MA align d/w BULLISH/MIXED | states | 2026-08-28 | technical_indicators.py on history_adj/ CSVs (see L013, L004) | DELAYED | DERIVED | 05, 06, 07, 15 |
| L316 | technical_indicator_pack | ABT | TD9 d/w/m BUY_SETUP_3/SELL_SETUP_9/SELL_SETUP_2; RSI14 59.70/61.49/51.08; MACD BELOW_SIGNAL/ABOVE_SIGNAL/BELOW_SIGNAL; MA align d/w BULLISH/MIXED | states | 2026-08-28 | technical_indicators.py on history_adj/ CSVs (see L013, L004) | DELAYED | DERIVED | 05, 06, 07, 15 |
| L317 | technical_indicator_pack | STT | TD9 d/w/m SELL_SETUP_4/SELL_SETUP_9/SELL_SETUP_9; RSI14 62.01/81.82/88.76; MACD ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL; MA align d/w BULLISH/BULLISH | states | 2026-08-28 | technical_indicators.py on history_adj/ CSVs (see L013, L004) | DELAYED | DERIVED | 05, 06, 07, 15 |
| L318 | technical_indicator_pack | JNJ | TD9 d/w/m BUY_SETUP_2/SELL_SETUP_4/SELL_SETUP_9; RSI14 57.07/65.56/77.93; MACD ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL; MA align d/w BULLISH/BULLISH | states | 2026-08-28 | technical_indicators.py on history_adj/ CSVs (see L013, L004) | DELAYED | DERIVED | 05, 06, 07, 15 |
| L319 | technical_indicator_pack | VRTX | TD9 d/w/m BUY_SETUP_2/SELL_SETUP_4/SELL_SETUP_2; RSI14 61.43/66.90/62.80; MACD ABOVE_SIGNAL/ABOVE_SIGNAL/BULLISH_CROSS; MA align d/w BULLISH/BULLISH | states | 2026-08-28 | technical_indicators.py on history_adj/ CSVs (see L013, L004) | DELAYED | DERIVED | 05, 06, 07, 15 |
| L320 | technical_indicator_pack | NEM | TD9 d/w/m BUY_SETUP_1/SELL_SETUP_4/SELL_SETUP_1; RSI14 64.49/62.92/69.82; MACD ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL; MA align d/w BULLISH/BULLISH | states | 2026-08-28 | technical_indicators.py on history_adj/ CSVs (see L013, L004) | DELAYED | DERIVED | 05, 06, 07, 15 |
| L321 | technical_indicator_pack | AMP | TD9 d/w/m BUY_SETUP_1/SELL_SETUP_9/SELL_SETUP_2; RSI14 58.51/68.87/62.22; MACD BELOW_SIGNAL/ABOVE_SIGNAL/BULLISH_CROSS; MA align d/w MIXED/BULLISH | states | 2026-08-28 | technical_indicators.py on history_adj/ CSVs (see L013, L004) | DELAYED | DERIVED | 05, 06, 07, 15 |
| L322 | technical_indicator_pack | NOW | TD9 d/w/m SELL_SETUP_2/SELL_SETUP_8/SELL_SETUP_2; RSI14 72.72/63.55/50.24; MACD ABOVE_SIGNAL/ABOVE_SIGNAL/BELOW_SIGNAL; MA align d/w BULLISH/MIXED | states | 2026-08-28 | technical_indicators.py on history_adj/ CSVs (see L013, L004) | DELAYED | DERIVED | 05, 06, 07, 15 |
| L323 | technical_indicator_pack | ICE | TD9 d/w/m BUY_SETUP_2/SELL_SETUP_7/SELL_SETUP_1; RSI14 72.12/59.63/53.81; MACD ABOVE_SIGNAL/ABOVE_SIGNAL/BELOW_SIGNAL; MA align d/w BULLISH/MIXED | states | 2026-08-28 | technical_indicators.py on history_adj/ CSVs (see L013, L004) | DELAYED | DERIVED | 05, 06, 07, 15 |
| L400 | momentum_and_relative_strength | RJF | mom20 +1.92%; mom60 +22.82%; RS20 vs SPY -1.07%; RS60 vs SPY +20.56%; volume ratio 20d 1.85 | percent / ratio | 2026-08-28 | technical_indicators.py daily block on adjusted closes (L013) | DELAYED | DERIVED | 05, 06, 07 |
| L401 | momentum_and_relative_strength | SCHW | mom20 +4.98%; mom60 +27.59%; RS20 vs SPY +1.99%; RS60 vs SPY +25.33%; volume ratio 20d 1.68 | percent / ratio | 2026-08-28 | technical_indicators.py daily block on adjusted closes (L013) | DELAYED | DERIVED | 05, 06, 07 |
| L402 | momentum_and_relative_strength | BLK | mom20 +6.79%; mom60 +18.18%; RS20 vs SPY +3.80%; RS60 vs SPY +15.92%; volume ratio 20d 1.37 | percent / ratio | 2026-08-28 | technical_indicators.py daily block on adjusted closes (L013) | DELAYED | DERIVED | 05, 06, 07 |
| L403 | momentum_and_relative_strength | RVTY | mom20 +14.47%; mom60 +27.52%; RS20 vs SPY +11.48%; RS60 vs SPY +25.26%; volume ratio 20d 1.04 | percent / ratio | 2026-08-28 | technical_indicators.py daily block on adjusted closes (L013) | DELAYED | DERIVED | 05, 06, 07 |
| L404 | momentum_and_relative_strength | SJM | mom20 +12.01%; mom60 +31.91%; RS20 vs SPY +9.02%; RS60 vs SPY +29.65%; volume ratio 20d 1.17 | percent / ratio | 2026-08-28 | technical_indicators.py daily block on adjusted closes (L013) | DELAYED | DERIVED | 05, 06, 07 |
| L405 | momentum_and_relative_strength | APD | mom20 +4.48%; mom60 +9.83%; RS20 vs SPY +1.49%; RS60 vs SPY +7.57%; volume ratio 20d 1.16 | percent / ratio | 2026-08-28 | technical_indicators.py daily block on adjusted closes (L013) | DELAYED | DERIVED | 05, 06, 07 |
| L406 | momentum_and_relative_strength | BDX | mom20 +14.43%; mom60 +31.07%; RS20 vs SPY +11.44%; RS60 vs SPY +28.81%; volume ratio 20d 0.95 | percent / ratio | 2026-08-28 | technical_indicators.py daily block on adjusted closes (L013) | DELAYED | DERIVED | 05, 06, 07 |
| L407 | momentum_and_relative_strength | BNY | mom20 +3.95%; mom60 +16.06%; RS20 vs SPY +0.96%; RS60 vs SPY +13.80%; volume ratio 20d 1.01 | percent / ratio | 2026-08-28 | technical_indicators.py daily block on adjusted closes (L013) | DELAYED | DERIVED | 05, 06, 07 |
| L408 | momentum_and_relative_strength | IQV | mom20 +11.37%; mom60 +43.78%; RS20 vs SPY +8.38%; RS60 vs SPY +41.52%; volume ratio 20d 1.50 | percent / ratio | 2026-08-28 | technical_indicators.py daily block on adjusted closes (L013) | DELAYED | DERIVED | 05, 06, 07 |
| L409 | momentum_and_relative_strength | GIS | mom20 +16.22%; mom60 +31.39%; RS20 vs SPY +13.23%; RS60 vs SPY +29.13%; volume ratio 20d 1.14 | percent / ratio | 2026-08-28 | technical_indicators.py daily block on adjusted closes (L013) | DELAYED | DERIVED | 05, 06, 07 |
| L410 | momentum_and_relative_strength | NWSA | mom20 +12.37%; mom60 +18.89%; RS20 vs SPY +9.38%; RS60 vs SPY +16.63%; volume ratio 20d 1.34 | percent / ratio | 2026-08-28 | technical_indicators.py daily block on adjusted closes (L013) | DELAYED | DERIVED | 05, 06, 07 |
| L411 | momentum_and_relative_strength | NDAQ | mom20 +5.44%; mom60 +14.81%; RS20 vs SPY +2.45%; RS60 vs SPY +12.55%; volume ratio 20d 0.97 | percent / ratio | 2026-08-28 | technical_indicators.py daily block on adjusted closes (L013) | DELAYED | DERIVED | 05, 06, 07 |
| L412 | momentum_and_relative_strength | NWS | mom20 +11.45%; mom60 +16.87%; RS20 vs SPY +8.46%; RS60 vs SPY +14.61%; volume ratio 20d 1.37 | percent / ratio | 2026-08-28 | technical_indicators.py daily block on adjusted closes (L013) | DELAYED | DERIVED | 05, 06, 07 |
| L413 | momentum_and_relative_strength | VEEV | mom20 +35.78%; mom60 +54.82%; RS20 vs SPY +32.79%; RS60 vs SPY +52.56%; volume ratio 20d 1.78 | percent / ratio | 2026-08-28 | technical_indicators.py daily block on adjusted closes (L013) | DELAYED | DERIVED | 05, 06, 07 |
| L414 | momentum_and_relative_strength | A | mom20 +11.18%; mom60 +12.18%; RS20 vs SPY +8.19%; RS60 vs SPY +9.92%; volume ratio 20d 1.47 | percent / ratio | 2026-08-28 | technical_indicators.py daily block on adjusted closes (L013) | DELAYED | DERIVED | 05, 06, 07 |
| L415 | momentum_and_relative_strength | RMD | mom20 +14.24%; mom60 +29.26%; RS20 vs SPY +11.25%; RS60 vs SPY +27.00%; volume ratio 20d 0.88 | percent / ratio | 2026-08-28 | technical_indicators.py daily block on adjusted closes (L013) | DELAYED | DERIVED | 05, 06, 07 |
| L416 | momentum_and_relative_strength | ABT | mom20 +6.40%; mom60 +30.21%; RS20 vs SPY +3.41%; RS60 vs SPY +27.95%; volume ratio 20d 1.04 | percent / ratio | 2026-08-28 | technical_indicators.py daily block on adjusted closes (L013) | DELAYED | DERIVED | 05, 06, 07 |
| L417 | momentum_and_relative_strength | STT | mom20 +4.98%; mom60 +23.06%; RS20 vs SPY +1.99%; RS60 vs SPY +20.80%; volume ratio 20d 0.49 | percent / ratio | 2026-08-28 | technical_indicators.py daily block on adjusted closes (L013) | DELAYED | DERIVED | 05, 06, 07 |
| L418 | momentum_and_relative_strength | JNJ | mom20 +5.08%; mom60 +20.66%; RS20 vs SPY +2.09%; RS60 vs SPY +18.40%; volume ratio 20d 0.90 | percent / ratio | 2026-08-28 | technical_indicators.py daily block on adjusted closes (L013) | DELAYED | DERIVED | 05, 06, 07 |
| L419 | momentum_and_relative_strength | VRTX | mom20 +13.54%; mom60 +26.46%; RS20 vs SPY +10.55%; RS60 vs SPY +24.20%; volume ratio 20d 0.74 | percent / ratio | 2026-08-28 | technical_indicators.py daily block on adjusted closes (L013) | DELAYED | DERIVED | 05, 06, 07 |
| L420 | momentum_and_relative_strength | NEM | mom20 +36.57%; mom60 +19.08%; RS20 vs SPY +33.58%; RS60 vs SPY +16.82%; volume ratio 20d 1.07 | percent / ratio | 2026-08-28 | technical_indicators.py daily block on adjusted closes (L013) | DELAYED | DERIVED | 05, 06, 07 |
| L421 | momentum_and_relative_strength | AMP | mom20 +2.79%; mom60 +27.25%; RS20 vs SPY -0.20%; RS60 vs SPY +24.99%; volume ratio 20d 0.76 | percent / ratio | 2026-08-28 | technical_indicators.py daily block on adjusted closes (L013) | DELAYED | DERIVED | 05, 06, 07 |
| L422 | momentum_and_relative_strength | NOW | mom20 +30.10%; mom60 +22.74%; RS20 vs SPY +27.11%; RS60 vs SPY +20.48%; volume ratio 20d 1.62 | percent / ratio | 2026-08-28 | technical_indicators.py daily block on adjusted closes (L013) | DELAYED | DERIVED | 05, 06, 07 |
| L423 | momentum_and_relative_strength | ICE | mom20 +6.46%; mom60 +17.68%; RS20 vs SPY +3.47%; RS60 vs SPY +15.42%; volume ratio 20d 0.92 | percent / ratio | 2026-08-28 | technical_indicators.py daily block on adjusted closes (L013) | DELAYED | DERIVED | 05, 06, 07 |
| L500 | beta_and_tracking_error | RJF | beta vs SPY +0.2350; beta vs TLT -0.0343; tracking error 1m 6.53% | slope / percent | 2026-08-28 | cov(r, r_SPY, ddof=0)/var(r_SPY) over the trailing 60 daily adjusted return intervals; TE = pstdev(r - beta*r_SPY) x sqrt(21) | DELAYED | DERIVED | 05, 07, 08 |
| L501 | beta_and_tracking_error | SCHW | beta vs SPY -0.1404; beta vs TLT -0.2498; tracking error 1m 6.61% | slope / percent | 2026-08-28 | cov(r, r_SPY, ddof=0)/var(r_SPY) over the trailing 60 daily adjusted return intervals; TE = pstdev(r - beta*r_SPY) x sqrt(21) | DELAYED | DERIVED | 05, 07, 08 |
| L502 | beta_and_tracking_error | BLK | beta vs SPY +0.8093; beta vs TLT +0.6376; tracking error 1m 7.28% | slope / percent | 2026-08-28 | cov(r, r_SPY, ddof=0)/var(r_SPY) over the trailing 60 daily adjusted return intervals; TE = pstdev(r - beta*r_SPY) x sqrt(21) | DELAYED | DERIVED | 05, 07, 08 |
| L503 | beta_and_tracking_error | RVTY | beta vs SPY +0.4591; beta vs TLT +0.7976; tracking error 1m 10.38% | slope / percent | 2026-08-28 | cov(r, r_SPY, ddof=0)/var(r_SPY) over the trailing 60 daily adjusted return intervals; TE = pstdev(r - beta*r_SPY) x sqrt(21) | DELAYED | DERIVED | 05, 07, 08 |
| L504 | beta_and_tracking_error | SJM | beta vs SPY -0.7004; beta vs TLT +0.7699; tracking error 1m 10.48% | slope / percent | 2026-08-28 | cov(r, r_SPY, ddof=0)/var(r_SPY) over the trailing 60 daily adjusted return intervals; TE = pstdev(r - beta*r_SPY) x sqrt(21) | DELAYED | DERIVED | 05, 07, 08 |
| L505 | beta_and_tracking_error | APD | beta vs SPY +0.1969; beta vs TLT -0.5557; tracking error 1m 7.93% | slope / percent | 2026-08-28 | cov(r, r_SPY, ddof=0)/var(r_SPY) over the trailing 60 daily adjusted return intervals; TE = pstdev(r - beta*r_SPY) x sqrt(21) | DELAYED | DERIVED | 05, 07, 08 |
| L506 | beta_and_tracking_error | BDX | beta vs SPY -0.0960; beta vs TLT +0.6931; tracking error 1m 8.42% | slope / percent | 2026-08-28 | cov(r, r_SPY, ddof=0)/var(r_SPY) over the trailing 60 daily adjusted return intervals; TE = pstdev(r - beta*r_SPY) x sqrt(21) | DELAYED | DERIVED | 05, 07, 08 |
| L507 | beta_and_tracking_error | BNY | beta vs SPY +0.4852; beta vs TLT -0.0809; tracking error 1m 6.41% | slope / percent | 2026-08-28 | cov(r, r_SPY, ddof=0)/var(r_SPY) over the trailing 60 daily adjusted return intervals; TE = pstdev(r - beta*r_SPY) x sqrt(21) | DELAYED | DERIVED | 05, 07, 08 |
| L508 | beta_and_tracking_error | IQV | beta vs SPY -0.2791; beta vs TLT +0.8472; tracking error 1m 12.68% | slope / percent | 2026-08-28 | cov(r, r_SPY, ddof=0)/var(r_SPY) over the trailing 60 daily adjusted return intervals; TE = pstdev(r - beta*r_SPY) x sqrt(21) | DELAYED | DERIVED | 05, 07, 08 |
| L509 | beta_and_tracking_error | GIS | beta vs SPY -0.3791; beta vs TLT +0.5651; tracking error 1m 10.25% | slope / percent | 2026-08-28 | cov(r, r_SPY, ddof=0)/var(r_SPY) over the trailing 60 daily adjusted return intervals; TE = pstdev(r - beta*r_SPY) x sqrt(21) | DELAYED | DERIVED | 05, 07, 08 |
| L510 | beta_and_tracking_error | NWSA | beta vs SPY -0.4096; beta vs TLT +0.2531; tracking error 1m 8.07% | slope / percent | 2026-08-28 | cov(r, r_SPY, ddof=0)/var(r_SPY) over the trailing 60 daily adjusted return intervals; TE = pstdev(r - beta*r_SPY) x sqrt(21) | DELAYED | DERIVED | 05, 07, 08 |
| L511 | beta_and_tracking_error | NDAQ | beta vs SPY +0.3738; beta vs TLT -0.3852; tracking error 1m 8.75% | slope / percent | 2026-08-28 | cov(r, r_SPY, ddof=0)/var(r_SPY) over the trailing 60 daily adjusted return intervals; TE = pstdev(r - beta*r_SPY) x sqrt(21) | DELAYED | DERIVED | 05, 07, 08 |
| L512 | beta_and_tracking_error | NWS | beta vs SPY -0.4311; beta vs TLT +0.2026; tracking error 1m 8.59% | slope / percent | 2026-08-28 | cov(r, r_SPY, ddof=0)/var(r_SPY) over the trailing 60 daily adjusted return intervals; TE = pstdev(r - beta*r_SPY) x sqrt(21) | DELAYED | DERIVED | 05, 07, 08 |
| L513 | beta_and_tracking_error | VEEV | beta vs SPY +0.4360; beta vs TLT +0.5795; tracking error 1m 14.79% | slope / percent | 2026-08-28 | cov(r, r_SPY, ddof=0)/var(r_SPY) over the trailing 60 daily adjusted return intervals; TE = pstdev(r - beta*r_SPY) x sqrt(21) | DELAYED | DERIVED | 05, 07, 08 |
| L514 | beta_and_tracking_error | A | beta vs SPY +0.4071; beta vs TLT +0.5517; tracking error 1m 8.25% | slope / percent | 2026-08-28 | cov(r, r_SPY, ddof=0)/var(r_SPY) over the trailing 60 daily adjusted return intervals; TE = pstdev(r - beta*r_SPY) x sqrt(21) | DELAYED | DERIVED | 05, 07, 08 |
| L515 | beta_and_tracking_error | RMD | beta vs SPY +0.1674; beta vs TLT +0.9035; tracking error 1m 10.60% | slope / percent | 2026-08-28 | cov(r, r_SPY, ddof=0)/var(r_SPY) over the trailing 60 daily adjusted return intervals; TE = pstdev(r - beta*r_SPY) x sqrt(21) | DELAYED | DERIVED | 05, 07, 08 |
| L516 | beta_and_tracking_error | ABT | beta vs SPY -0.4386; beta vs TLT +0.4501; tracking error 1m 9.41% | slope / percent | 2026-08-28 | cov(r, r_SPY, ddof=0)/var(r_SPY) over the trailing 60 daily adjusted return intervals; TE = pstdev(r - beta*r_SPY) x sqrt(21) | DELAYED | DERIVED | 05, 07, 08 |
| L517 | beta_and_tracking_error | STT | beta vs SPY +0.6287; beta vs TLT -0.0841; tracking error 1m 6.47% | slope / percent | 2026-08-28 | cov(r, r_SPY, ddof=0)/var(r_SPY) over the trailing 60 daily adjusted return intervals; TE = pstdev(r - beta*r_SPY) x sqrt(21) | DELAYED | DERIVED | 05, 07, 08 |
| L518 | beta_and_tracking_error | JNJ | beta vs SPY -0.7547; beta vs TLT +0.2593; tracking error 1m 6.72% | slope / percent | 2026-08-28 | cov(r, r_SPY, ddof=0)/var(r_SPY) over the trailing 60 daily adjusted return intervals; TE = pstdev(r - beta*r_SPY) x sqrt(21) | DELAYED | DERIVED | 05, 07, 08 |
| L519 | beta_and_tracking_error | VRTX | beta vs SPY +0.1319; beta vs TLT +0.9238; tracking error 1m 8.73% | slope / percent | 2026-08-28 | cov(r, r_SPY, ddof=0)/var(r_SPY) over the trailing 60 daily adjusted return intervals; TE = pstdev(r - beta*r_SPY) x sqrt(21) | DELAYED | DERIVED | 05, 07, 08 |
| L520 | beta_and_tracking_error | NEM | beta vs SPY +1.8424; beta vs TLT +1.0251; tracking error 1m 12.49% | slope / percent | 2026-08-28 | cov(r, r_SPY, ddof=0)/var(r_SPY) over the trailing 60 daily adjusted return intervals; TE = pstdev(r - beta*r_SPY) x sqrt(21) | DELAYED | DERIVED | 05, 07, 08 |
| L521 | beta_and_tracking_error | AMP | beta vs SPY +0.3129; beta vs TLT +0.0189; tracking error 1m 6.54% | slope / percent | 2026-08-28 | cov(r, r_SPY, ddof=0)/var(r_SPY) over the trailing 60 daily adjusted return intervals; TE = pstdev(r - beta*r_SPY) x sqrt(21) | DELAYED | DERIVED | 05, 07, 08 |
| L522 | beta_and_tracking_error | NOW | beta vs SPY +0.5182; beta vs TLT +0.1243; tracking error 1m 17.44% | slope / percent | 2026-08-28 | cov(r, r_SPY, ddof=0)/var(r_SPY) over the trailing 60 daily adjusted return intervals; TE = pstdev(r - beta*r_SPY) x sqrt(21) | DELAYED | DERIVED | 05, 07, 08 |
| L523 | beta_and_tracking_error | ICE | beta vs SPY -0.1127; beta vs TLT -0.1332; tracking error 1m 7.66% | slope / percent | 2026-08-28 | cov(r, r_SPY, ddof=0)/var(r_SPY) over the trailing 60 daily adjusted return intervals; TE = pstdev(r - beta*r_SPY) x sqrt(21) | DELAYED | DERIVED | 05, 07, 08 |
| L600 | volatility_and_drawdown | RJF | realized vol 30d (1m) 5.68%; vol60 6.59%; downside sigma 3.80%; max drawdown 60d -6.10% | percent | 2026-08-28 | pstdev of trailing 30 (resp. 60) daily adjusted returns x sqrt(21); downside sigma over negative returns only; drawdown = worst peak-to-trough over the 61 most recent adjusted closes | DELAYED | DERIVED | 05, 06, 07, 15 |
| L601 | volatility_and_drawdown | SCHW | realized vol 30d (1m) 5.74%; vol60 6.63%; downside sigma 3.74%; max drawdown 60d -5.36% | percent | 2026-08-28 | pstdev of trailing 30 (resp. 60) daily adjusted returns x sqrt(21); downside sigma over negative returns only; drawdown = worst peak-to-trough over the 61 most recent adjusted closes | DELAYED | DERIVED | 05, 06, 07, 15 |
| L602 | volatility_and_drawdown | BLK | realized vol 30d (1m) 6.64%; vol60 7.97%; downside sigma 3.11%; max drawdown 60d -10.14% | percent | 2026-08-28 | pstdev of trailing 30 (resp. 60) daily adjusted returns x sqrt(21); downside sigma over negative returns only; drawdown = worst peak-to-trough over the 61 most recent adjusted closes | DELAYED | DERIVED | 05, 06, 07, 15 |
| L603 | volatility_and_drawdown | RVTY | realized vol 30d (1m) 9.86%; vol60 10.54%; downside sigma 4.88%; max drawdown 60d -6.38% | percent | 2026-08-28 | pstdev of trailing 30 (resp. 60) daily adjusted returns x sqrt(21); downside sigma over negative returns only; drawdown = worst peak-to-trough over the 61 most recent adjusted closes | DELAYED | DERIVED | 05, 06, 07, 15 |
| L604 | volatility_and_drawdown | SJM | realized vol 30d (1m) 8.47%; vol60 10.85%; downside sigma 4.71%; max drawdown 60d -8.42% | percent | 2026-08-28 | pstdev of trailing 30 (resp. 60) daily adjusted returns x sqrt(21); downside sigma over negative returns only; drawdown = worst peak-to-trough over the 61 most recent adjusted closes | DELAYED | DERIVED | 05, 06, 07, 15 |
| L605 | volatility_and_drawdown | APD | realized vol 30d (1m) 5.14%; vol60 7.97%; downside sigma 3.57%; max drawdown 60d -6.88% | percent | 2026-08-28 | pstdev of trailing 30 (resp. 60) daily adjusted returns x sqrt(21); downside sigma over negative returns only; drawdown = worst peak-to-trough over the 61 most recent adjusted closes | DELAYED | DERIVED | 05, 06, 07, 15 |
| L606 | volatility_and_drawdown | BDX | realized vol 30d (1m) 7.47%; vol60 8.43%; downside sigma 2.90%; max drawdown 60d -7.45% | percent | 2026-08-28 | pstdev of trailing 30 (resp. 60) daily adjusted returns x sqrt(21); downside sigma over negative returns only; drawdown = worst peak-to-trough over the 61 most recent adjusted closes | DELAYED | DERIVED | 05, 06, 07, 15 |
| L607 | volatility_and_drawdown | BNY | realized vol 30d (1m) 5.23%; vol60 6.70%; downside sigma 3.69%; max drawdown 60d -5.69% | percent | 2026-08-28 | pstdev of trailing 30 (resp. 60) daily adjusted returns x sqrt(21); downside sigma over negative returns only; drawdown = worst peak-to-trough over the 61 most recent adjusted closes | DELAYED | DERIVED | 05, 06, 07, 15 |
| L608 | volatility_and_drawdown | IQV | realized vol 30d (1m) 14.20%; vol60 12.73%; downside sigma 4.46%; max drawdown 60d -10.23% | percent | 2026-08-28 | pstdev of trailing 30 (resp. 60) daily adjusted returns x sqrt(21); downside sigma over negative returns only; drawdown = worst peak-to-trough over the 61 most recent adjusted closes | DELAYED | DERIVED | 05, 06, 07, 15 |
| L609 | volatility_and_drawdown | GIS | realized vol 30d (1m) 9.16%; vol60 10.36%; downside sigma 5.57%; max drawdown 60d -8.14% | percent | 2026-08-28 | pstdev of trailing 30 (resp. 60) daily adjusted returns x sqrt(21); downside sigma over negative returns only; drawdown = worst peak-to-trough over the 61 most recent adjusted closes | DELAYED | DERIVED | 05, 06, 07, 15 |
| L610 | volatility_and_drawdown | NWSA | realized vol 30d (1m) 8.37%; vol60 8.23%; downside sigma 5.86%; max drawdown 60d -9.72% | percent | 2026-08-28 | pstdev of trailing 30 (resp. 60) daily adjusted returns x sqrt(21); downside sigma over negative returns only; drawdown = worst peak-to-trough over the 61 most recent adjusted closes | DELAYED | DERIVED | 05, 06, 07, 15 |
| L611 | volatility_and_drawdown | NDAQ | realized vol 30d (1m) 4.29%; vol60 8.87%; downside sigma 2.00%; max drawdown 60d -15.59% | percent | 2026-08-28 | pstdev of trailing 30 (resp. 60) daily adjusted returns x sqrt(21); downside sigma over negative returns only; drawdown = worst peak-to-trough over the 61 most recent adjusted closes | DELAYED | DERIVED | 05, 06, 07, 15 |
| L612 | volatility_and_drawdown | NWS | realized vol 30d (1m) 8.83%; vol60 8.76%; downside sigma 5.63%; max drawdown 60d -10.48% | percent | 2026-08-28 | pstdev of trailing 30 (resp. 60) daily adjusted returns x sqrt(21); downside sigma over negative returns only; drawdown = worst peak-to-trough over the 61 most recent adjusted closes | DELAYED | DERIVED | 05, 06, 07, 15 |
| L613 | volatility_and_drawdown | VEEV | realized vol 30d (1m) 16.72%; vol60 14.90%; downside sigma 5.56%; max drawdown 60d -14.30% | percent | 2026-08-28 | pstdev of trailing 30 (resp. 60) daily adjusted returns x sqrt(21); downside sigma over negative returns only; drawdown = worst peak-to-trough over the 61 most recent adjusted closes | DELAYED | DERIVED | 05, 06, 07, 15 |
| L614 | volatility_and_drawdown | A | realized vol 30d (1m) 7.97%; vol60 8.41%; downside sigma 4.44%; max drawdown 60d -10.15% | percent | 2026-08-28 | pstdev of trailing 30 (resp. 60) daily adjusted returns x sqrt(21); downside sigma over negative returns only; drawdown = worst peak-to-trough over the 61 most recent adjusted closes | DELAYED | DERIVED | 05, 06, 07, 15 |
| L615 | volatility_and_drawdown | RMD | realized vol 30d (1m) 9.70%; vol60 10.62%; downside sigma 6.16%; max drawdown 60d -12.68% | percent | 2026-08-28 | pstdev of trailing 30 (resp. 60) daily adjusted returns x sqrt(21); downside sigma over negative returns only; drawdown = worst peak-to-trough over the 61 most recent adjusted closes | DELAYED | DERIVED | 05, 06, 07, 15 |
| L616 | volatility_and_drawdown | ABT | realized vol 30d (1m) 6.13%; vol60 9.57%; downside sigma 3.86%; max drawdown 60d -7.18% | percent | 2026-08-28 | pstdev of trailing 30 (resp. 60) daily adjusted returns x sqrt(21); downside sigma over negative returns only; drawdown = worst peak-to-trough over the 61 most recent adjusted closes | DELAYED | DERIVED | 05, 06, 07, 15 |
| L617 | volatility_and_drawdown | STT | realized vol 30d (1m) 6.55%; vol60 6.94%; downside sigma 5.09%; max drawdown 60d -5.65% | percent | 2026-08-28 | pstdev of trailing 30 (resp. 60) daily adjusted returns x sqrt(21); downside sigma over negative returns only; drawdown = worst peak-to-trough over the 61 most recent adjusted closes | DELAYED | DERIVED | 05, 06, 07, 15 |
| L618 | volatility_and_drawdown | JNJ | realized vol 30d (1m) 6.17%; vol60 7.36%; downside sigma 4.45%; max drawdown 60d -7.57% | percent | 2026-08-28 | pstdev of trailing 30 (resp. 60) daily adjusted returns x sqrt(21); downside sigma over negative returns only; drawdown = worst peak-to-trough over the 61 most recent adjusted closes | DELAYED | DERIVED | 05, 06, 07, 15 |
| L619 | volatility_and_drawdown | VRTX | realized vol 30d (1m) 8.51%; vol60 8.75%; downside sigma 2.99%; max drawdown 60d -11.12% | percent | 2026-08-28 | pstdev of trailing 30 (resp. 60) daily adjusted returns x sqrt(21); downside sigma over negative returns only; drawdown = worst peak-to-trough over the 61 most recent adjusted closes | DELAYED | DERIVED | 05, 06, 07, 15 |
| L620 | volatility_and_drawdown | NEM | realized vol 30d (1m) 13.87%; vol60 14.50%; downside sigma 5.48%; max drawdown 60d -17.74% | percent | 2026-08-28 | pstdev of trailing 30 (resp. 60) daily adjusted returns x sqrt(21); downside sigma over negative returns only; drawdown = worst peak-to-trough over the 61 most recent adjusted closes | DELAYED | DERIVED | 05, 06, 07, 15 |
| L621 | volatility_and_drawdown | AMP | realized vol 30d (1m) 4.73%; vol60 6.66%; downside sigma 2.95%; max drawdown 60d -5.34% | percent | 2026-08-28 | pstdev of trailing 30 (resp. 60) daily adjusted returns x sqrt(21); downside sigma over negative returns only; drawdown = worst peak-to-trough over the 61 most recent adjusted closes | DELAYED | DERIVED | 05, 06, 07, 15 |
| L622 | volatility_and_drawdown | NOW | realized vol 30d (1m) 18.12%; vol60 17.56%; downside sigma 8.87%; max drawdown 60d -25.00% | percent | 2026-08-28 | pstdev of trailing 30 (resp. 60) daily adjusted returns x sqrt(21); downside sigma over negative returns only; drawdown = worst peak-to-trough over the 61 most recent adjusted closes | DELAYED | DERIVED | 05, 06, 07, 15 |
| L623 | volatility_and_drawdown | ICE | realized vol 30d (1m) 5.78%; vol60 7.67%; downside sigma 3.80%; max drawdown 60d -13.16% | percent | 2026-08-28 | pstdev of trailing 30 (resp. 60) daily adjusted returns x sqrt(21); downside sigma over negative returns only; drawdown = worst peak-to-trough over the 61 most recent adjusted closes | DELAYED | DERIVED | 05, 06, 07, 15 |
| L700 | next_earnings_date | RJF | NO_PRINT_IN_WINDOW through 2026-10-04 | date | 2026-08-28 | api.nasdaq.com/api/calendar/earnings?date=YYYY-MM-DD complete 26-business-day sweep (NO_PRINT_IN_WINDOW) | DELAYED | OBSERVED | 05, 07, 08 |
| L701 | next_earnings_date | SCHW | NO_PRINT_IN_WINDOW through 2026-10-04 | date | 2026-08-28 | api.nasdaq.com/api/calendar/earnings?date=YYYY-MM-DD complete 26-business-day sweep (NO_PRINT_IN_WINDOW) | DELAYED | OBSERVED | 05, 07, 08 |
| L702 | next_earnings_date | BLK | NO_PRINT_IN_WINDOW through 2026-10-04 | date | 2026-08-28 | api.nasdaq.com/api/calendar/earnings?date=YYYY-MM-DD complete 26-business-day sweep (NO_PRINT_IN_WINDOW) | DELAYED | OBSERVED | 05, 07, 08 |
| L703 | next_earnings_date | RVTY | NO_PRINT_IN_WINDOW through 2026-10-04 | date | 2026-08-28 | api.nasdaq.com/api/calendar/earnings?date=YYYY-MM-DD complete 26-business-day sweep (NO_PRINT_IN_WINDOW) | DELAYED | OBSERVED | 05, 07, 08 |
| L704 | next_earnings_date | SJM | NO_PRINT_IN_WINDOW through 2026-10-04 | date | 2026-08-28 | api.nasdaq.com/api/calendar/earnings?date=YYYY-MM-DD complete 26-business-day sweep (NO_PRINT_IN_WINDOW) | DELAYED | OBSERVED | 05, 07, 08 |
| L705 | next_earnings_date | APD | NO_PRINT_IN_WINDOW through 2026-10-04 | date | 2026-08-28 | api.nasdaq.com/api/calendar/earnings?date=YYYY-MM-DD complete 26-business-day sweep (NO_PRINT_IN_WINDOW) | DELAYED | OBSERVED | 05, 07, 08 |
| L706 | next_earnings_date | BDX | NO_PRINT_IN_WINDOW through 2026-10-04 | date | 2026-08-28 | api.nasdaq.com/api/calendar/earnings?date=YYYY-MM-DD complete 26-business-day sweep (NO_PRINT_IN_WINDOW) | DELAYED | OBSERVED | 05, 07, 08 |
| L707 | next_earnings_date | BNY | NO_PRINT_IN_WINDOW through 2026-10-04 | date | 2026-08-28 | api.nasdaq.com/api/calendar/earnings?date=YYYY-MM-DD complete 26-business-day sweep (NO_PRINT_IN_WINDOW) | DELAYED | OBSERVED | 05, 07, 08 |
| L708 | next_earnings_date | IQV | NO_PRINT_IN_WINDOW through 2026-10-04 | date | 2026-08-28 | api.nasdaq.com/api/calendar/earnings?date=YYYY-MM-DD complete 26-business-day sweep (NO_PRINT_IN_WINDOW) | DELAYED | OBSERVED | 05, 07, 08 |
| L709 | next_earnings_date | GIS | 2026-09-23 (26d) | date | 2026-08-28 | api.nasdaq.com/api/calendar/earnings?date=YYYY-MM-DD complete 26-business-day sweep (CONFIRMED_CALENDAR) | DELAYED | OBSERVED | 05, 07, 08 |
| L710 | next_earnings_date | NWSA | NO_PRINT_IN_WINDOW through 2026-10-04 | date | 2026-08-28 | api.nasdaq.com/api/calendar/earnings?date=YYYY-MM-DD complete 26-business-day sweep (NO_PRINT_IN_WINDOW) | DELAYED | OBSERVED | 05, 07, 08 |
| L711 | next_earnings_date | NDAQ | NO_PRINT_IN_WINDOW through 2026-10-04 | date | 2026-08-28 | api.nasdaq.com/api/calendar/earnings?date=YYYY-MM-DD complete 26-business-day sweep (NO_PRINT_IN_WINDOW) | DELAYED | OBSERVED | 05, 07, 08 |
| L712 | next_earnings_date | NWS | NO_PRINT_IN_WINDOW through 2026-10-04 | date | 2026-08-28 | api.nasdaq.com/api/calendar/earnings?date=YYYY-MM-DD complete 26-business-day sweep (NO_PRINT_IN_WINDOW) | DELAYED | OBSERVED | 05, 07, 08 |
| L713 | next_earnings_date | VEEV | NO_PRINT_IN_WINDOW through 2026-10-04 | date | 2026-08-28 | api.nasdaq.com/api/calendar/earnings?date=YYYY-MM-DD complete 26-business-day sweep (NO_PRINT_IN_WINDOW) | DELAYED | OBSERVED | 05, 07, 08 |
| L714 | next_earnings_date | A | NO_PRINT_IN_WINDOW through 2026-10-04 | date | 2026-08-28 | api.nasdaq.com/api/calendar/earnings?date=YYYY-MM-DD complete 26-business-day sweep (NO_PRINT_IN_WINDOW) | DELAYED | OBSERVED | 05, 07, 08 |
| L715 | next_earnings_date | RMD | NO_PRINT_IN_WINDOW through 2026-10-04 | date | 2026-08-28 | api.nasdaq.com/api/calendar/earnings?date=YYYY-MM-DD complete 26-business-day sweep (NO_PRINT_IN_WINDOW) | DELAYED | OBSERVED | 05, 07, 08 |
| L716 | next_earnings_date | ABT | NO_PRINT_IN_WINDOW through 2026-10-04 | date | 2026-08-28 | api.nasdaq.com/api/calendar/earnings?date=YYYY-MM-DD complete 26-business-day sweep (NO_PRINT_IN_WINDOW) | DELAYED | OBSERVED | 05, 07, 08 |
| L717 | next_earnings_date | STT | NO_PRINT_IN_WINDOW through 2026-10-04 | date | 2026-08-28 | api.nasdaq.com/api/calendar/earnings?date=YYYY-MM-DD complete 26-business-day sweep (NO_PRINT_IN_WINDOW) | DELAYED | OBSERVED | 05, 07, 08 |
| L718 | next_earnings_date | JNJ | NO_PRINT_IN_WINDOW through 2026-10-04 | date | 2026-08-28 | api.nasdaq.com/api/calendar/earnings?date=YYYY-MM-DD complete 26-business-day sweep (NO_PRINT_IN_WINDOW) | DELAYED | OBSERVED | 05, 07, 08 |
| L719 | next_earnings_date | VRTX | NO_PRINT_IN_WINDOW through 2026-10-04 | date | 2026-08-28 | api.nasdaq.com/api/calendar/earnings?date=YYYY-MM-DD complete 26-business-day sweep (NO_PRINT_IN_WINDOW) | DELAYED | OBSERVED | 05, 07, 08 |
| L720 | next_earnings_date | NEM | NO_PRINT_IN_WINDOW through 2026-10-04 | date | 2026-08-28 | api.nasdaq.com/api/calendar/earnings?date=YYYY-MM-DD complete 26-business-day sweep (NO_PRINT_IN_WINDOW) | DELAYED | OBSERVED | 05, 07, 08 |
| L721 | next_earnings_date | AMP | NO_PRINT_IN_WINDOW through 2026-10-04 | date | 2026-08-28 | api.nasdaq.com/api/calendar/earnings?date=YYYY-MM-DD complete 26-business-day sweep (NO_PRINT_IN_WINDOW) | DELAYED | OBSERVED | 05, 07, 08 |
| L722 | next_earnings_date | NOW | NO_PRINT_IN_WINDOW through 2026-10-04 | date | 2026-08-28 | api.nasdaq.com/api/calendar/earnings?date=YYYY-MM-DD complete 26-business-day sweep (NO_PRINT_IN_WINDOW) | DELAYED | OBSERVED | 05, 07, 08 |
| L723 | next_earnings_date | ICE | NO_PRINT_IN_WINDOW through 2026-10-04 | date | 2026-08-28 | api.nasdaq.com/api/calendar/earnings?date=YYYY-MM-DD complete 26-business-day sweep (NO_PRINT_IN_WINDOW) | DELAYED | OBSERVED | 05, 07, 08 |
| L800 | core_etf_forecast_inputs | SPY | entry 769.35; beta vs SPY +1.0000; 30d RVol(1m) 3.38% (FALLING); drawdown from 60d high -1.10%; RS20 +0.00%; RS60 +0.00% | mixed | 2026-08-28 | stockanalysis.com/api/symbol/{s\|e}/{SYM}/history?range=5Y + technical_indicators.py (L004, L013) | DELAYED | DERIVED | 03, 09, 15 |
| L801 | core_etf_forecast_inputs | QQQ | entry 716.43; beta vs SPY +1.7389; 30d RVol(1m) 5.98% (FALLING); drawdown from 60d high -3.60%; RS20 +1.14%; RS60 -5.89% | mixed | 2026-08-28 | stockanalysis.com/api/symbol/{s\|e}/{SYM}/history?range=5Y + technical_indicators.py (L004, L013) | DELAYED | DERIVED | 03, 09, 15 |
| L802 | core_etf_forecast_inputs | SOXX | entry 508.62; beta vs SPY +3.4320; 30d RVol(1m) 14.57% (FALLING); drawdown from 60d high -22.35%; RS20 -2.25%; RS60 -19.61% | mixed | 2026-08-28 | stockanalysis.com/api/symbol/{s\|e}/{SYM}/history?range=5Y + technical_indicators.py (L004, L013) | DELAYED | DERIVED | 03, 09, 15 |

## Ledger coverage

| freshness_tag | rows |
|---|---|
| DELAYED | 169 |
| HISTORICAL | 4 |
| UNAVAILABLE | 3 |

| claim_type | rows |
|---|---|
| DERIVED | 112 |
| INFERRED | 1 |
| OBSERVED | 60 |
| UNAVAILABLE | 3 |

Total ledger rows: **176**. `ILLUSTRATIVE_REF` rows: **0** — the run is
not in `ILLUSTRATIVE_MODE`; the declared `data_mode` is `DELAYED`.

## Preflight status

| Required input (rules.md § Input Classification) | State | Evidence |
|---|---|---|
| 1. Grounded entry price | **GROUNDED** | L012 — 27/27 on three sources at 0.0000% max deviation |
| 2. ~60 trading days of history per name and SPY | **GROUNDED** | L004, L005 — 518 symbols x 5y daily bars |
| 3. sigma via the Sigma Fallback Chain | **GROUNDED** | L600+ — `REALIZED_VOL_30D` for all 24 published names and all 3 core ETFs |
| 4. Next earnings date | **GROUNDED** | L009, L022, L700+ — complete 26-business-day forward sweep, 510/510 scored names resolved |
| 5. Index-union universe | **GROUNDED** | L001-L003 — 515 tickers from `build_index_universe.py`; no sampled fallback |

All five Required inputs are grounded, so `DELAYED` is the correct data mode and no Required
input blocks `GO`. The run's `NO_TRADE` status is driven by the evidence thresholds in
`05`/`08`, not by data availability.

## Enhancing inputs (caps, never GO blockers)

| Enhancing input | State | Effect |
|---|---|---|
| Options IV / skew | `UNAVAILABLE` | no options feed wired; sigma falls to `REALIZED_VOL_30D` (chain step 2) |
| Short interest / borrow | `UNAVAILABLE` | contributes to `Sent_Z` being `UNAVAILABLE` (L019) |
| Bid-ask spread tape | `UNAVAILABLE` | 50 bps exclusion filter cannot be applied; liquidity screened on ADDV instead |
| Analyst revision tape | `UNAVAILABLE` | contributes to `Sent_Z` being `UNAVAILABLE` (L019) |
| Institutional ownership flow | `UNAVAILABLE` | no effect beyond `Sent_Z` |
| Full-universe fundamental feed | `UNAVAILABLE` | `Fund_Z` `UNAVAILABLE` (L018); SHADOW tooling exists but covers far under the 70% threshold |

Data-quality multiplier **0.80** (L021) and confidence capped at `MEDIUM` for every
name — see `05 § Calibration feedback binding`.

