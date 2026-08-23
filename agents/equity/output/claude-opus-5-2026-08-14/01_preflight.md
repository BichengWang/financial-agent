# 01 — Preflight and Source Ledger · 2026-08-14

Basis `2026-08-14` close. Every fact used downstream appears below or is `UNAVAILABLE`.
Working JSON paths are cited for lineage but are **not** durable dependencies — they live under
gitignored `agents/equity/.work/`, so every decision-relevant value is written out here, in
`05` and in `15` rather than left behind a file reference.

## Data mode

`DELAYED` — every price was fetched during this run (no real-time feed is wired), the basis
close is final at all three vendors, and all five Required inputs are grounded. This is **not**
`ILLUSTRATIVE_MODE`; no value in this package is a training-reference value.

## Price Sourcing Standard — grounding gate

Three independent sources were used; the standard requires a market-data tool **or** two
independent web sources agreeing within 1%.

| Source | Endpoint | Role |
|---|---|---|
| A | `stockanalysis.com/api/symbol/{s\|e}/{SYM}/history?range=5Y` | run primary (bulk 5y history) |
| B | `api.nasdaq.com/api/quote/{SYM}/historical?assetclass={stocks\|etf}` | independent, dated rows |
| C | `quote.cnbc.com/quote-html-webservice/restQuote` — `last` gated on `last_time` == basis | independent, basis date only |

**Result: 137/137 price-date checks grounded, maximum deviation
0.000000%** across 87 symbols — every published entry price,
every settlement price, and the SPY benchmark at each settlement date. Zero confirmation
re-reads were required and zero cross-vendor disagreements were found.

Vendor-behaviour notes for this fire window (~01:36 ET Saturday, after the post-market tape
has closed) — this is a **fourth** distinct field regime, separate from the documented
pre-open, intraday and immediate-post-close cases:

- `api.nasdaq.com/api/quote/{SYM}/info` is **not usable** at this hour: `secondaryData` is
  `null` (so the "Closed at {basis} 4:00 PM ET" marker that the 2026-08-03 post-close rule
  keys on does not exist), and `primaryData.lastTradeTimestamp` reads `Aug 13, 2026` while
  `primaryData.lastSalePrice` carries the **Aug 14** close. The timestamp cannot be trusted to
  gate the price, so this endpoint was dropped in favour of the dated `historical` endpoint.
- `api.nasdaq.com/api/quote/{SYM}/historical` **works again**. It served a bot-challenge HTML
  page from 2026-07-27 onward; it now returns clean dated JSON. Bulk history is no longer
  single-sourced.
- Yahoo `query1/v8/finance/chart` remains **429-blocked**.
- Nasdaq's `historical` endpoint returns **no rows when `fromdate == todate`**; single-date
  requests must pad the window (18 settlement dates initially came back unverified for exactly
  this reason before the window was padded).

## Ex-dividend / corporate-action scan

Basis-bar `c` vs `a` was compared across all 519 symbols:
**0**
carried an ex-dividend adjustment on the basis bar, so no name in this package needed
corporate-action reconciliation between the raw entry price and the adjusted metric basis.

## Source Ledger

| artifact | field | ticker/entity | value | unit | observation_date | source | freshness_tag | claim_type | used_by |
|---|---|---|---|---|---|---|---|---|---|
| `L001` | daily OHLCV history (5y) | 519 symbols | 519/519 fetched | bars | 2026-08-14 | stockanalysis.com/api/symbol/{s\\|e}/{SYM}/history?range=5Y · retrieved 2026-08-14T22:40:26-0700 | `HISTORICAL` | `OBSERVED` | all price/return/indicator math |
| `L002` | adjusted close `a` | all symbols | used for every return/indicator computation | USD | 2026-08-14 | `L001` field `a` | `HISTORICAL` | `OBSERVED` | momentum, RS, vol, downside vol, beta, TE, drawdown, `technical_indicators.py` |
| `L003` | raw close `c` | all symbols | used for entry/target/CI prices | USD | 2026-08-14 | `L001` field `c` | `HISTORICAL` | `OBSERVED` | entry_price, target_price, CI bounds |
| `L004` | independent close verification | 87 symbols | 137/137 grounded, max dev 0.000000% | % | 2026-08-14 | `api.nasdaq.com/api/quote/{SYM}/historical` | `HISTORICAL` | `OBSERVED` | Price Sourcing Standard gate |
| `L005` | independent close verification | basis-date closes | CNBC `last` gated on `last_time` == basis | USD | 2026-08-14 | `quote.cnbc.com/quote-html-webservice/restQuote` | `HISTORICAL` | `OBSERVED` | Price Sourcing Standard gate |
| `L006` | S&P 500 constituents | index | 503 | names | 2026-06-21 | `agents/equity/turtle-trader/universe/sp500.json` | `HISTORICAL` | `OBSERVED` | universe construction |
| `L007` | Nasdaq-100 constituents | index | 101 | names | 2026-06-21 | `agents/equity/turtle-trader/universe/nasdaq100.json` | `HISTORICAL` | `OBSERVED` | universe construction |
| `L008` | index union | universe | 515 | names | 2026-08-15 | `build_index_universe.py` on `L006`+`L007` | `HISTORICAL` | `DERIVED` | eligible universe; `INDEX_UNION_PCTL` |
| `L009` | market cap + sector | 7138 rows | screener snapshot | USD / label | 2026-08-14 | `api.nasdaq.com/api/screener/stocks?tableonly=true&limit=10000&download=true` | `DELAYED` | `OBSERVED` | market-cap filter, sector table, `sector_lead` slot |
| `L010` | forward earnings calendar | full universe | 26/26 business days, complete | dates | 2026-08-14..2026-09-20 | `api.nasdaq.com/api/calendar/earnings?date=YYYY-MM-DD` swept daily | `DELAYED` | `OBSERVED` | earnings penalty, `Days to Earnings`, event-concentration check |
| `L011` | VIX daily close | ^VIX | 14.25 | index | 2026-08-14 | `cdn.cboe.com/api/global/us_indices/daily_prices/VIX_History.csv` | `HISTORICAL` | `OBSERVED` | regime classification |
| `L012` | risk-free rate (13w bank discount) | US T-bill | 3.71 | % p.a. | 2026-08-14 | US Treasury daily rates CSV (FRED `DTB3` timed out) | `OFFICIAL_FILING` | `OBSERVED` | Sharpe, Sortino, Treynor, Calmar (`rf_1m = rf/12`) |
| `L013` | technical indicator pack | 519 symbols | daily/weekly/monthly TD-9, RSI(14), MACD, MA, momentum, volume ratio, RS | mixed | 2026-08-14 | `technical_indicators.py --benchmark SPY --history-dir <adj csv tree>` on `L002` | `HISTORICAL` | `DERIVED` | `Tech_Z` slots, displayed indicator states |
| `L014` | canonical settlement ledger | all packages | due 0 · conflicts 0 · canonical 950 EQ / 150 MF | rows | 2026-08-14 | `settlement_ledger.py --output-dir agents/equity/output --as-of 2026-08-14` | `HISTORICAL` | `DERIVED` | `02 § 0`, rolling calibration metrics |
| `L015` | SPY entry price | SPY | 776.34 | USD | 2026-08-14 | `L001` + `L004` + `L005` (3 sources, 0.000000% deviation) | `HISTORICAL` | `OBSERVED` | benchmark_price, ETF forecast, beta/TE regressions |
| `L016` | QQQ entry price | QQQ | 731.07 | USD | 2026-08-14 | `L001` + `L004` + `L005` | `HISTORICAL` | `OBSERVED` | ETF forecast |
| `L017` | SOXX entry price | SOXX | 550.42 | USD | 2026-08-14 | `L001` + `L004` + `L005` | `HISTORICAL` | `OBSERVED` | ETF forecast |
| `L018` | TLT daily history | TLT | 1255 bars | bars | 2026-08-14 | `L001` | `HISTORICAL` | `OBSERVED` | `rate_sens` Macro slot |
| `L019` | winsorized cross-sectional z-scores | 511 names | clip at 5th/95th pctl, then (x - mean)/pop-stdev of the clipped series | z | 2026-08-14 | `rules.md § Family Aggregation`; bounds in `run_computed_manifest.json` | `HISTORICAL` | `DERIVED` | all family z-scores and `Adj Score` |
| `L020` | data quality multiplier | run-level | 0.80 | x | 2026-08-14 | `rules.md § Data Quality Multiplier` — 2 of 4 families `UNAVAILABLE` = notable coverage gaps | `HISTORICAL` | `INFERRED` | `Adj Score` |
| `L021` | `Fund_Z` | all 511 names | `UNAVAILABLE` | z | 2026-08-14 | no fundamental fetch path wired at universe scale (`rules.md § SHADOW Diagnostic Tooling`) | `UNAVAILABLE` | `UNAVAILABLE` | evidence threshold 2; `Adj Score` contribution 0.00 |
| `L022` | `Sent_Z` | all 511 names | `UNAVAILABLE` | z | 2026-08-14 | no sentiment/positioning fetch path wired at universe scale | `UNAVAILABLE` | `UNAVAILABLE` | evidence threshold 2; `Adj Score` contribution 0.00 |
| `L023` | regime classification | market | `BULL` | label | 2026-08-14 | `03 § Regime classification` from `L001`, `L011`, `L013` | `HISTORICAL` | `INFERRED` | Core ETF mu prior, `Macro_Z` interpretation |
| `L024` | rolling calibration metrics | `EQUITY_ALPHA` | n=950 · eff_n=2 · hit 40.53% · CI 70.84% · mean z -0.5220 · rank IC -0.0630 | mixed | 2026-08-14 | `L014` `rolling_metrics` | `HISTORICAL` | `DERIVED` | confidence cap, `13` evolution decision |
| `L025` | rolling calibration metrics | `MARKET_FORECAST` | n=150 · eff_n=2 · hit 32.17% · CI 88.67% · mean z -0.4000 | mixed | 2026-08-14 | `L014` `rolling_metrics` | `HISTORICAL` | `DERIVED` | `13` evolution decision |
| `L101` | entry price (raw close) | NTAP | 207.08 | USD | 2026-08-14 | `L003` + `L004` + `L005` | `HISTORICAL` | `OBSERVED` | `05`/`06`/`15` entry, target, CI |
| `L102` | entry price (raw close) | CRL | 280.05 | USD | 2026-08-14 | `L003` + `L004` + `L005` | `HISTORICAL` | `OBSERVED` | `05`/`06`/`15` entry, target, CI |
| `L103` | entry price (raw close) | MDT | 91.27 | USD | 2026-08-14 | `L003` + `L004` + `L005` | `HISTORICAL` | `OBSERVED` | `05`/`06`/`15` entry, target, CI |
| `L104` | entry price (raw close) | AME | 254.79 | USD | 2026-08-14 | `L003` + `L004` + `L005` | `HISTORICAL` | `OBSERVED` | `05`/`06`/`15` entry, target, CI |
| `L105` | entry price (raw close) | KKR | 114.01 | USD | 2026-08-14 | `L003` + `L004` + `L005` | `HISTORICAL` | `OBSERVED` | `05`/`06`/`15` entry, target, CI |
| `L106` | entry price (raw close) | DXCM | 89.75 | USD | 2026-08-14 | `L003` + `L004` + `L005` | `HISTORICAL` | `OBSERVED` | `05`/`06`/`15` entry, target, CI |
| `L107` | entry price (raw close) | ABNB | 184.06 | USD | 2026-08-14 | `L003` + `L004` + `L005` | `HISTORICAL` | `OBSERVED` | `05`/`06`/`15` entry, target, CI |
| `L108` | entry price (raw close) | WTW | 331.59 | USD | 2026-08-14 | `L003` + `L004` + `L005` | `HISTORICAL` | `OBSERVED` | `05`/`06`/`15` entry, target, CI |
| `L109` | entry price (raw close) | EXPE | 332.69 | USD | 2026-08-14 | `L003` + `L004` + `L005` | `HISTORICAL` | `OBSERVED` | `05`/`06`/`15` entry, target, CI |
| `L110` | entry price (raw close) | JCI | 153.64 | USD | 2026-08-14 | `L003` + `L004` + `L005` | `HISTORICAL` | `OBSERVED` | `05`/`06`/`15` entry, target, CI |
| `L111` | entry price (raw close) | BAC | 64.49 | USD | 2026-08-14 | `L003` + `L004` + `L005` | `HISTORICAL` | `OBSERVED` | `05`/`06`/`15` entry, target, CI |
| `L112` | entry price (raw close) | MRK | 135.84 | USD | 2026-08-14 | `L003` + `L004` + `L005` | `HISTORICAL` | `OBSERVED` | `05`/`06`/`15` entry, target, CI |
| `L113` | entry price (raw close) | SOLV | 88.59 | USD | 2026-08-14 | `L003` + `L004` + `L005` | `HISTORICAL` | `OBSERVED` | `05`/`06`/`15` entry, target, CI |
| `L114` | entry price (raw close) | BX | 143.93 | USD | 2026-08-14 | `L003` + `L004` + `L005` | `HISTORICAL` | `OBSERVED` | `05`/`06`/`15` entry, target, CI |
| `L115` | entry price (raw close) | URI | 1,153.83 | USD | 2026-08-14 | `L003` + `L004` + `L005` | `HISTORICAL` | `OBSERVED` | `05`/`06`/`15` entry, target, CI |
| `L116` | entry price (raw close) | SCHW | 111.09 | USD | 2026-08-14 | `L003` + `L004` + `L005` | `HISTORICAL` | `OBSERVED` | `05`/`06`/`15` entry, target, CI |
| `L117` | entry price (raw close) | STT | 191.74 | USD | 2026-08-14 | `L003` + `L004` + `L005` | `HISTORICAL` | `OBSERVED` | `05`/`06`/`15` entry, target, CI |
| `L118` | entry price (raw close) | AMGN | 415.21 | USD | 2026-08-14 | `L003` + `L004` + `L005` | `HISTORICAL` | `OBSERVED` | `05`/`06`/`15` entry, target, CI |
| `L119` | entry price (raw close) | FITB | 58.06 | USD | 2026-08-14 | `L003` + `L004` + `L005` | `HISTORICAL` | `OBSERVED` | `05`/`06`/`15` entry, target, CI |
| `L120` | entry price (raw close) | BNY | 163.24 | USD | 2026-08-14 | `L003` + `L004` + `L005` | `HISTORICAL` | `OBSERVED` | `05`/`06`/`15` entry, target, CI |
| `L121` | entry price (raw close) | IVZ | 32.55 | USD | 2026-08-14 | `L003` + `L004` + `L005` | `HISTORICAL` | `OBSERVED` | `05`/`06`/`15` entry, target, CI |
| `L122` | entry price (raw close) | DASH | 217.02 | USD | 2026-08-14 | `L003` + `L004` + `L005` | `HISTORICAL` | `OBSERVED` | `05`/`06`/`15` entry, target, CI |
| `L123` | entry price (raw close) | TECH | 72.40 | USD | 2026-08-14 | `L003` + `L004` + `L005` | `HISTORICAL` | `OBSERVED` | `05`/`06`/`15` entry, target, CI |
| `L124` | entry price (raw close) | REGN | 803.48 | USD | 2026-08-14 | `L003` + `L004` + `L005` | `HISTORICAL` | `OBSERVED` | `05`/`06`/`15` entry, target, CI |
| `L201` | technical indicator pack | NTAP | TD9 SELL9/SELL6/SELL5 · RSI 76.71/79.87/75.31 · MACD A/A/A · mom20 +26.36% · mom60 +72.24% · volratio 0.98 · rs20 +21.91% · rs60 +66.16% | mixed | 2026-08-14 | `L013` (`technical_indicators.py` on `L002`) | `HISTORICAL` | `DERIVED` | `Tech_Z` slots; displayed states in `05`/`06`/`09` |
| `L202` | technical indicator pack | CRL | TD9 SELL8/SELL9/SELL3 · RSI 76.21/74.79/65.1 · MACD A/A/A · mom20 +24.83% · mom60 +83.72% · volratio 0.80 · rs20 +20.38% · rs60 +77.64% | mixed | 2026-08-14 | `L013` (`technical_indicators.py` on `L002`) | `HISTORICAL` | `DERIVED` | `Tech_Z` slots; displayed states in `05`/`06`/`09` |
| `L203` | technical indicator pack | MDT | TD9 SELL8/SELL9/SELL1 · RSI 71.12/61.07/53.42 · MACD A/A/b · mom20 +9.70% · mom60 +17.20% · volratio 1.25 · rs20 +5.25% · rs60 +11.12% | mixed | 2026-08-14 | `L013` (`technical_indicators.py` on `L002`) | `HISTORICAL` | `DERIVED` | `Tech_Z` slots; displayed states in `05`/`06`/`09` |
| `L204` | technical indicator pack | AME | TD9 SELL4/SELL4/SELL9 · RSI 62.97/73.43/69.76 · MACD A/A/A · mom20 +7.51% · mom60 +15.32% · volratio 1.30 · rs20 +3.06% · rs60 +9.24% | mixed | 2026-08-14 | `L013` (`technical_indicators.py` on `L002`) | `HISTORICAL` | `DERIVED` | `Tech_Z` slots; displayed states in `05`/`06`/`09` |
| `L205` | technical indicator pack | KKR | TD9 SELL4/SELL7/SELL3 · RSI 68.65/61.61/52.01 · MACD A/A/b · mom20 +13.16% · mom60 +22.93% · volratio 1.19 · rs20 +8.71% · rs60 +16.85% | mixed | 2026-08-14 | `L013` (`technical_indicators.py` on `L002`) | `HISTORICAL` | `DERIVED` | `Tech_Z` slots; displayed states in `05`/`06`/`09` |
| `L206` | technical indicator pack | DXCM | TD9 SELL5/SELL5/SELL2 · RSI 67.39/69.63/54.43 · MACD A/A/A · mom20 +17.09% · mom60 +34.06% · volratio 0.73 · rs20 +12.64% · rs60 +27.98% | mixed | 2026-08-14 | `L013` (`technical_indicators.py` on `L002`) | `HISTORICAL` | `DERIVED` | `Tech_Z` slots; displayed states in `05`/`06`/`09` |
| `L207` | technical indicator pack | ABNB | TD9 BUY1/SELL3/SELL9 · RSI 74.99/76.87/66.97 · MACD A/A/A · mom20 +26.09% · mom60 +40.33% · volratio 0.78 · rs20 +21.64% · rs60 +34.25% | mixed | 2026-08-14 | `L013` (`technical_indicators.py` on `L002`) | `HISTORICAL` | `DERIVED` | `Tech_Z` slots; displayed states in `05`/`06`/`09` |
| `L208` | technical indicator pack | WTW | TD9 BUY2/SELL8/SELL2 · RSI 63.13/63.12/58.76 · MACD b/A/b · mom20 +13.00% · mom60 +30.92% · volratio 1.22 · rs20 +8.55% · rs60 +24.84% | mixed | 2026-08-14 | `L013` (`technical_indicators.py` on `L002`) | `HISTORICAL` | `DERIVED` | `Tech_Z` slots; displayed states in `05`/`06`/`09` |
| `L209` | technical indicator pack | EXPE | TD9 SELL9/SELL3/SELL3 · RSI 73.6/72.25/70.83 · MACD A/A/A · mom20 +23.78% · mom60 +55.07% · volratio 0.65 · rs20 +19.33% · rs60 +48.99% | mixed | 2026-08-14 | `L013` (`technical_indicators.py` on `L002`) | `HISTORICAL` | `DERIVED` | `Tech_Z` slots; displayed states in `05`/`06`/`09` |
| `L210` | technical indicator pack | JCI | TD9 SELL1/SELL4/SELL9 · RSI 60.93/66.21/73.06 · MACD A/B+/A · mom20 +9.38% · mom60 +13.77% · volratio 0.67 · rs20 +4.93% · rs60 +7.69% | mixed | 2026-08-14 | `L013` (`technical_indicators.py` on `L002`) | `HISTORICAL` | `DERIVED` | `Tech_Z` slots; displayed states in `05`/`06`/`09` |
| `L211` | technical indicator pack | BAC | TD9 SELL9/SELL9/SELL3 · RSI 68.45/74.71/73.63 · MACD A/A/A · mom20 +5.26% · mom60 +27.86% · volratio 0.76 · rs20 +0.81% · rs60 +21.78% | mixed | 2026-08-14 | `L013` (`technical_indicators.py` on `L002`) | `HISTORICAL` | `DERIVED` | `Tech_Z` slots; displayed states in `05`/`06`/`09` |
| `L212` | technical indicator pack | MRK | TD9 SELL6/SELL8/SELL9 · RSI 68.81/66.55/70.04 · MACD A/A/A · mom20 +6.54% · mom60 +19.76% · volratio 0.84 · rs20 +2.09% · rs60 +13.68% | mixed | 2026-08-14 | `L013` (`technical_indicators.py` on `L002`) | `HISTORICAL` | `DERIVED` | `Tech_Z` slots; displayed states in `05`/`06`/`09` |
| `L213` | technical indicator pack | SOLV | TD9 SELL3/SELL3/SELL3 · RSI 63.17/62.98/60.62 · MACD B+/A/`UNAVL` · mom20 +8.95% · mom60 +18.55% · volratio 1.17 · rs20 +4.50% · rs60 +12.47% | mixed | 2026-08-14 | `L013` (`technical_indicators.py` on `L002`) | `HISTORICAL` | `DERIVED` | `Tech_Z` slots; displayed states in `05`/`06`/`09` |
| `L214` | technical indicator pack | BX | TD9 SELL9/SELL7/SELL3 · RSI 63.93/63.84/54.8 · MACD A/A/b · mom20 +14.57% · mom60 +27.25% · volratio 0.72 · rs20 +10.12% · rs60 +21.17% | mixed | 2026-08-14 | `L013` (`technical_indicators.py` on `L002`) | `HISTORICAL` | `DERIVED` | `Tech_Z` slots; displayed states in `05`/`06`/`09` |
| `L215` | technical indicator pack | URI | TD9 SELL1/SELL2/SELL5 · RSI 59.01/64.08/67.78 · MACD A/A/A · mom20 +10.58% · mom60 +24.60% · volratio 0.95 · rs20 +6.13% · rs60 +18.52% | mixed | 2026-08-14 | `L013` (`technical_indicators.py` on `L002`) | `HISTORICAL` | `DERIVED` | `Tech_Z` slots; displayed states in `05`/`06`/`09` |
| `L216` | technical indicator pack | SCHW | TD9 SELL3/SELL9/SELL2 · RSI 76.37/72.07/68.25 · MACD A/A/B+ · mom20 +9.70% · mom60 +21.35% · volratio 0.77 · rs20 +5.25% · rs60 +15.27% | mixed | 2026-08-14 | `L013` (`technical_indicators.py` on `L002`) | `HISTORICAL` | `DERIVED` | `Tech_Z` slots; displayed states in `05`/`06`/`09` |
| `L217` | technical indicator pack | STT | TD9 SELL9/SELL9/SELL9 · RSI 67.31/87.66/88.57 · MACD B+/A/A · mom20 +5.06% · mom60 +27.71% · volratio 0.57 · rs20 +0.61% · rs60 +21.63% | mixed | 2026-08-14 | `L013` (`technical_indicators.py` on `L002`) | `HISTORICAL` | `DERIVED` | `Tech_Z` slots; displayed states in `05`/`06`/`09` |
| `L218` | technical indicator pack | AMGN | TD9 BUY1/SELL8/SELL2 · RSI 70.05/70.74/69.24 · MACD A/A/A · mom20 +13.36% · mom60 +25.54% · volratio 0.63 · rs20 +8.91% · rs60 +19.46% | mixed | 2026-08-14 | `L013` (`technical_indicators.py` on `L002`) | `HISTORICAL` | `DERIVED` | `Tech_Z` slots; displayed states in `05`/`06`/`09` |
| `L219` | technical indicator pack | FITB | TD9 SELL3/SELL2/SELL9 · RSI 59.4/66.2/71.45 · MACD b/A/A · mom20 +0.09% · mom60 +22.84% · volratio 0.97 · rs20 -4.36% · rs60 +16.76% | mixed | 2026-08-14 | `L013` (`technical_indicators.py` on `L002`) | `HISTORICAL` | `DERIVED` | `Tech_Z` slots; displayed states in `05`/`06`/`09` |
| `L220` | technical indicator pack | BNY | TD9 SELL9/SELL9/SELL9 · RSI 66.72/83.26/91.45 · MACD A/A/A · mom20 +4.30% · mom60 +20.22% · volratio 0.71 · rs20 -0.15% · rs60 +14.14% | mixed | 2026-08-14 | `L013` (`technical_indicators.py` on `L002`) | `HISTORICAL` | `DERIVED` | `Tech_Z` slots; displayed states in `05`/`06`/`09` |
| `L221` | technical indicator pack | IVZ | TD9 SELL2/SELL6/SELL9 · RSI 67.48/71.19/72.49 · MACD A/A/A · mom20 +10.59% · mom60 +23.79% · volratio 0.83 · rs20 +6.14% · rs60 +17.71% | mixed | 2026-08-14 | `L013` (`technical_indicators.py` on `L002`) | `HISTORICAL` | `DERIVED` | `Tech_Z` slots; displayed states in `05`/`06`/`09` |
| `L222` | technical indicator pack | DASH | TD9 SELL1/SELL3/SELL3 · RSI 68.38/62.45/56.57 · MACD A/A/b · mom20 +17.86% · mom60 +40.33% · volratio 0.64 · rs20 +13.41% · rs60 +34.25% | mixed | 2026-08-14 | `L013` (`technical_indicators.py` on `L002`) | `HISTORICAL` | `DERIVED` | `Tech_Z` slots; displayed states in `05`/`06`/`09` |
| `L223` | technical indicator pack | TECH | TD9 SELL1/SELL9/SELL3 · RSI 72.5/65.85/55.39 · MACD b/A/A · mom20 +0.39% · mom60 +59.23% · volratio 0.57 · rs20 -4.06% · rs60 +53.15% | mixed | 2026-08-14 | `L013` (`technical_indicators.py` on `L002`) | `HISTORICAL` | `DERIVED` | `Tech_Z` slots; displayed states in `05`/`06`/`09` |
| `L224` | technical indicator pack | REGN | TD9 BUY1/SELL8/SELL1 · RSI 77.35/65.31/55.44 · MACD A/A/A · mom20 +18.74% · mom60 +27.67% · volratio 0.53 · rs20 +14.29% · rs60 +21.59% | mixed | 2026-08-14 | `L013` (`technical_indicators.py` on `L002`) | `HISTORICAL` | `DERIVED` | `Tech_Z` slots; displayed states in `05`/`06`/`09` |
| `L301` | derived risk metrics | NTAP | sigma 12.73% (`REALIZED_VOL_30D`) · beta +1.4251 · TE 17.98% · dd60 -15.81% · Sharpe 0.447 · Sortino 0.673 · IR 0.175 · 0.25K 0.926 · VaR95 -15.00% · CVaR95 -20.22% | mixed | 2026-08-14 | formulas `rules.md § Ratio Definitions` / `§ Computed Risk Analytics` on `L002`, `L012`, `L015` | `HISTORICAL` | `DERIVED` | `05` ranked table, `15` metrics block, sizing gate |
| `L302` | derived risk metrics | CRL | sigma 13.51% (`REALIZED_VOL_30D`) · beta +0.5249 · TE 13.71% · dd60 -6.38% · Sharpe 0.421 · Sortino 1.711 · IR 0.361 · 0.25K 0.821 · VaR95 -16.30% · CVaR95 -21.84% | mixed | 2026-08-14 | formulas `rules.md § Ratio Definitions` / `§ Computed Risk Analytics` on `L002`, `L012`, `L015` | `HISTORICAL` | `DERIVED` | `05` ranked table, `15` metrics block, sizing gate |
| `L303` | derived risk metrics | MDT | sigma 7.65% (`REALIZED_VOL_30D`) · beta -0.1816 · TE 8.83% · dd60 -6.17% · Sharpe 0.744 · Sortino 0.919 · IR 0.721 · 0.25K 2.564 · VaR95 -6.62% · CVaR95 -9.76% | mixed | 2026-08-14 | formulas `rules.md § Ratio Definitions` / `§ Computed Risk Analytics` on `L002`, `L012`, `L015` | `HISTORICAL` | `DERIVED` | `05` ranked table, `15` metrics block, sizing gate |
| `L304` | derived risk metrics | AME | sigma 5.94% (`REALIZED_VOL_30D`) · beta +0.9610 · TE 5.34% · dd60 -4.38% · Sharpe 0.959 · Sortino 1.644 · IR 0.764 · 0.25K 4.257 · VaR95 -3.79% · CVaR95 -6.23% | mixed | 2026-08-14 | formulas `rules.md § Ratio Definitions` / `§ Computed Risk Analytics` on `L002`, `L012`, `L015` | `HISTORICAL` | `DERIVED` | `05` ranked table, `15` metrics block, sizing gate |
| `L305` | derived risk metrics | KKR | sigma 11.31% (`REALIZED_VOL_30D`) · beta +1.1600 · TE 9.31% · dd60 -10.13% · Sharpe 0.503 · Sortino 1.072 · IR 0.395 · 0.25K 1.174 · VaR95 -12.65% · CVaR95 -17.29% | mixed | 2026-08-14 | formulas `rules.md § Ratio Definitions` / `§ Computed Risk Analytics` on `L002`, `L012`, `L015` | `HISTORICAL` | `DERIVED` | `05` ranked table, `15` metrics block, sizing gate |
| `L306` | derived risk metrics | DXCM | sigma 14.94% (`REALIZED_VOL_30D`) · beta +0.5629 · TE 13.30% · dd60 -13.86% · Sharpe 0.381 · Sortino 0.931 · IR 0.366 · 0.25K 0.672 · VaR95 -18.65% · CVaR95 -24.77% | mixed | 2026-08-14 | formulas `rules.md § Ratio Definitions` / `§ Computed Risk Analytics` on `L002`, `L012`, `L015` | `HISTORICAL` | `DERIVED` | `05` ranked table, `15` metrics block, sizing gate |
| `L307` | derived risk metrics | ABNB | sigma 16.82% (`REALIZED_VOL_30D`) · beta +0.7466 · TE 13.27% · dd60 -7.63% · Sharpe 0.338 · Sortino 1.208 · IR 0.340 · 0.25K 0.530 · VaR95 -21.75% · CVaR95 -28.64% | mixed | 2026-08-14 | formulas `rules.md § Ratio Definitions` / `§ Computed Risk Analytics` on `L002`, `L012`, `L015` | `HISTORICAL` | `DERIVED` | `05` ranked table, `15` metrics block, sizing gate |
| `L308` | derived risk metrics | WTW | sigma 8.64% (`REALIZED_VOL_30D`) · beta -0.3695 · TE 8.47% · dd60 -4.15% · Sharpe 0.659 · Sortino 1.945 · IR 0.796 · 0.25K 2.009 · VaR95 -8.26% · CVaR95 -11.80% | mixed | 2026-08-14 | formulas `rules.md § Ratio Definitions` / `§ Computed Risk Analytics` on `L002`, `L012`, `L015` | `HISTORICAL` | `DERIVED` | `05` ranked table, `15` metrics block, sizing gate |
| `L309` | derived risk metrics | EXPE | sigma 11.56% (`REALIZED_VOL_30D`) · beta +0.4131 · TE 11.81% · dd60 -5.25% · Sharpe 0.492 · Sortino 0.934 · IR 0.438 · 0.25K 1.123 · VaR95 -13.07% · CVaR95 -17.81% | mixed | 2026-08-14 | formulas `rules.md § Ratio Definitions` / `§ Computed Risk Analytics` on `L002`, `L012`, `L015` | `HISTORICAL` | `DERIVED` | `05` ranked table, `15` metrics block, sizing gate |
| `L310` | derived risk metrics | JCI | sigma 7.14% (`REALIZED_VOL_30D`) · beta +1.2486 · TE 8.61% · dd60 -6.62% · Sharpe 0.798 · Sortino 2.238 · IR 0.407 · 0.25K 2.946 · VaR95 -5.77% · CVaR95 -8.70% | mixed | 2026-08-14 | formulas `rules.md § Ratio Definitions` / `§ Computed Risk Analytics` on `L002`, `L012`, `L015` | `HISTORICAL` | `DERIVED` | `05` ranked table, `15` metrics block, sizing gate |
| `L311` | derived risk metrics | BAC | sigma 5.12% (`REALIZED_VOL_30D`) · beta +0.3282 · TE 5.12% · dd60 -2.74% · Sharpe 1.111 · Sortino 1.393 · IR 1.045 · 0.25K 5.721 · VaR95 -2.45% · CVaR95 -4.55% | mixed | 2026-08-14 | formulas `rules.md § Ratio Definitions` / `§ Computed Risk Analytics` on `L002`, `L012`, `L015` | `HISTORICAL` | `DERIVED` | `05` ranked table, `15` metrics block, sizing gate |
| `L312` | derived risk metrics | MRK | sigma 6.91% (`REALIZED_VOL_30D`) · beta -0.4080 · TE 8.48% · dd60 -6.78% · Sharpe 0.823 · Sortino 1.400 · IR 0.804 · 0.25K 3.137 · VaR95 -5.41% · CVaR95 -8.24% | mixed | 2026-08-14 | formulas `rules.md § Ratio Definitions` / `§ Computed Risk Analytics` on `L002`, `L012`, `L015` | `HISTORICAL` | `DERIVED` | `05` ranked table, `15` metrics block, sizing gate |
| `L313` | derived risk metrics | SOLV | sigma 10.94% (`REALIZED_VOL_30D`) · beta -0.0655 · TE 10.25% · dd60 -10.79% · Sharpe 0.520 · Sortino 1.037 · IR 0.598 · 0.25K 1.253 · VaR95 -12.05% · CVaR95 -16.54% | mixed | 2026-08-14 | formulas `rules.md § Ratio Definitions` / `§ Computed Risk Analytics` on `L002`, `L012`, `L015` | `HISTORICAL` | `DERIVED` | `05` ranked table, `15` metrics block, sizing gate |
| `L314` | derived risk metrics | BX | sigma 10.86% (`REALIZED_VOL_30D`) · beta +1.0951 · TE 10.58% · dd60 -11.64% · Sharpe 0.524 · Sortino 1.233 · IR 0.360 · 0.25K 1.271 · VaR95 -11.92% · CVaR95 -16.38% | mixed | 2026-08-14 | formulas `rules.md § Ratio Definitions` / `§ Computed Risk Analytics` on `L002`, `L012`, `L015` | `HISTORICAL` | `DERIVED` | `05` ranked table, `15` metrics block, sizing gate |
| `L315` | derived risk metrics | URI | sigma 12.35% (`REALIZED_VOL_30D`) · beta +0.6718 · TE 10.77% · dd60 -11.13% · Sharpe 0.461 · Sortino 1.210 · IR 0.432 · 0.25K 0.983 · VaR95 -14.38% · CVaR95 -19.45% | mixed | 2026-08-14 | formulas `rules.md § Ratio Definitions` / `§ Computed Risk Analytics` on `L002`, `L012`, `L015` | `HISTORICAL` | `DERIVED` | `05` ranked table, `15` metrics block, sizing gate |
| `L316` | derived risk metrics | SCHW | sigma 5.52% (`REALIZED_VOL_30D`) · beta -0.1643 · TE 6.97% · dd60 -7.04% · Sharpe 1.030 · Sortino 1.671 · IR 0.908 · 0.25K 4.914 · VaR95 -3.12% · CVaR95 -5.38% | mixed | 2026-08-14 | formulas `rules.md § Ratio Definitions` / `§ Computed Risk Analytics` on `L002`, `L012`, `L015` | `HISTORICAL` | `DERIVED` | `05` ranked table, `15` metrics block, sizing gate |
| `L317` | derived risk metrics | STT | sigma 7.00% (`REALIZED_VOL_30D`) · beta +0.6830 · TE 6.32% · dd60 -5.65% · Sharpe 0.813 · Sortino 1.347 · IR 0.734 · 0.25K 3.062 · VaR95 -5.55% · CVaR95 -8.42% | mixed | 2026-08-14 | formulas `rules.md § Ratio Definitions` / `§ Computed Risk Analytics` on `L002`, `L012`, `L015` | `HISTORICAL` | `DERIVED` | `05` ranked table, `15` metrics block, sizing gate |
| `L318` | derived risk metrics | AMGN | sigma 7.78% (`REALIZED_VOL_30D`) · beta +0.0836 · TE 7.57% · dd60 -5.05% · Sharpe 0.732 · Sortino 2.094 · IR 0.770 · 0.25K 2.479 · VaR95 -6.83% · CVaR95 -10.02% | mixed | 2026-08-14 | formulas `rules.md § Ratio Definitions` / `§ Computed Risk Analytics` on `L002`, `L012`, `L015` | `HISTORICAL` | `DERIVED` | `05` ranked table, `15` metrics block, sizing gate |
| `L319` | derived risk metrics | FITB | sigma 5.73% (`REALIZED_VOL_30D`) · beta +0.3388 · TE 6.75% · dd60 -4.83% · Sharpe 0.993 · Sortino 1.151 · IR 0.788 · 0.25K 4.564 · VaR95 -3.46% · CVaR95 -5.81% | mixed | 2026-08-14 | formulas `rules.md § Ratio Definitions` / `§ Computed Risk Analytics` on `L002`, `L012`, `L015` | `HISTORICAL` | `DERIVED` | `05` ranked table, `15` metrics block, sizing gate |
| `L320` | derived risk metrics | BNY | sigma 6.98% (`REALIZED_VOL_30D`) · beta +0.5161 · TE 6.19% · dd60 -5.69% · Sharpe 0.815 · Sortino 1.585 · IR 0.802 · 0.25K 3.074 · VaR95 -5.53% · CVaR95 -8.39% | mixed | 2026-08-14 | formulas `rules.md § Ratio Definitions` / `§ Computed Risk Analytics` on `L002`, `L012`, `L015` | `HISTORICAL` | `DERIVED` | `05` ranked table, `15` metrics block, sizing gate |
| `L321` | derived risk metrics | IVZ | sigma 11.19% (`REALIZED_VOL_30D`) · beta +1.7447 · TE 8.21% · dd60 -11.40% · Sharpe 0.508 · Sortino 1.137 · IR 0.306 · 0.25K 1.197 · VaR95 -12.47% · CVaR95 -17.06% | mixed | 2026-08-14 | formulas `rules.md § Ratio Definitions` / `§ Computed Risk Analytics` on `L002`, `L012`, `L015` | `HISTORICAL` | `DERIVED` | `05` ranked table, `15` metrics block, sizing gate |
| `L322` | derived risk metrics | DASH | sigma 12.32% (`REALIZED_VOL_30D`) · beta +1.2809 · TE 12.62% · dd60 -13.26% · Sharpe 0.462 · Sortino 0.803 · IR 0.272 · 0.25K 0.988 · VaR95 -14.33% · CVaR95 -19.39% | mixed | 2026-08-14 | formulas `rules.md § Ratio Definitions` / `§ Computed Risk Analytics` on `L002`, `L012`, `L015` | `HISTORICAL` | `DERIVED` | `05` ranked table, `15` metrics block, sizing gate |
| `L323` | derived risk metrics | TECH | sigma 1.31% (`REALIZED_VOL_30D`) · beta +0.7450 · TE 13.84% · dd60 -4.02% · Sharpe 4.356 · Sortino 6.765 · IR 0.326 · 0.25K 87.887 · VaR95 +3.84% · CVaR95 +3.31% | mixed | 2026-08-14 | formulas `rules.md § Ratio Definitions` / `§ Computed Risk Analytics` on `L002`, `L012`, `L015` | `HISTORICAL` | `DERIVED` | `05` ranked table, `15` metrics block, sizing gate |
| `L324` | derived risk metrics | REGN | sigma 8.92% (`REALIZED_VOL_30D`) · beta +0.2527 · TE 8.41% · dd60 -7.56% · Sharpe 0.638 · Sortino 1.308 · IR 0.653 · 0.25K 1.884 · VaR95 -8.72% · CVaR95 -12.38% | mixed | 2026-08-14 | formulas `rules.md § Ratio Definitions` / `§ Computed Risk Analytics` on `L002`, `L012`, `L015` | `HISTORICAL` | `DERIVED` | `05` ranked table, `15` metrics block, sizing gate |
| `L401` | macro slot inputs | NTAP | beta_prox -0.4251 (z +1.047) · sector_lead +9.62% (z -0.034) · rate_sens -0.3834 vs TLT (z +0.656) · vol_stability -0.6750 (z +1.987) | mixed | 2026-08-14 | `rules.md § Family Aggregation` on `L002`, `L009`, `L018`, `L019` | `HISTORICAL` | `DERIVED` | `Macro_Z` |
| `L402` | macro slot inputs | CRL | beta_prox -0.4751 (z +0.957) · sector_lead +15.46% (z +1.260) · rate_sens -1.6557 vs TLT (z -1.202) · vol_stability -0.9748 (z -0.030) | mixed | 2026-08-14 | `rules.md § Family Aggregation` on `L002`, `L009`, `L018`, `L019` | `HISTORICAL` | `DERIVED` | `Macro_Z` |
| `L403` | macro slot inputs | MDT | beta_prox -1.1816 (z -0.326) · sector_lead +15.46% (z +1.260) · rate_sens -0.1003 vs TLT (z +1.070) · vol_stability -0.8632 (z +0.888) | mixed | 2026-08-14 | `rules.md § Family Aggregation` on `L002`, `L009`, `L018`, `L019` | `HISTORICAL` | `DERIVED` | `Macro_Z` |
| `L404` | macro slot inputs | AME | beta_prox -0.0390 (z +1.663) · sector_lead +9.15% (z -0.139) · rate_sens -0.9697 vs TLT (z -0.200) · vol_stability -0.9033 (z +0.558) | mixed | 2026-08-14 | `rules.md § Family Aggregation` on `L002`, `L009`, `L018`, `L019` | `HISTORICAL` | `DERIVED` | `Macro_Z` |
| `L405` | macro slot inputs | KKR | beta_prox -0.1600 (z +1.529) · sector_lead +15.32% (z +1.232) · rate_sens -0.9605 vs TLT (z -0.187) · vol_stability -1.0876 (z -0.959) | mixed | 2026-08-14 | `rules.md § Family Aggregation` on `L002`, `L009`, `L018`, `L019` | `HISTORICAL` | `DERIVED` | `Macro_Z` |
| `L406` | macro slot inputs | DXCM | beta_prox -0.4371 (z +1.026) · sector_lead +15.46% (z +1.260) · rate_sens -0.4391 vs TLT (z +0.575) · vol_stability -1.1075 (z -1.123) | mixed | 2026-08-14 | `rules.md § Family Aggregation` on `L002`, `L009`, `L018`, `L019` | `HISTORICAL` | `DERIVED` | `Macro_Z` |
| `L407` | macro slot inputs | ABNB | beta_prox -0.2534 (z +1.359) · sector_lead +11.24% (z +0.325) · rate_sens -1.3910 vs TLT (z -0.815) · vol_stability -1.2369 (z -1.698) | mixed | 2026-08-14 | `rules.md § Family Aggregation` on `L002`, `L009`, `L018`, `L019` | `HISTORICAL` | `DERIVED` | `Macro_Z` |
| `L408` | macro slot inputs | WTW | beta_prox -1.3695 (z -0.667) · sector_lead +15.32% (z +1.232) · rate_sens -0.0099 vs TLT (z +1.152) · vol_stability -1.0056 (z -0.284) | mixed | 2026-08-14 | `rules.md § Family Aggregation` on `L002`, `L009`, `L018`, `L019` | `HISTORICAL` | `DERIVED` | `Macro_Z` |
| `L409` | macro slot inputs | EXPE | beta_prox -0.5869 (z +0.754) · sector_lead +11.24% (z +0.325) · rate_sens -1.8854 vs TLT (z -1.537) · vol_stability -0.9696 (z +0.012) | mixed | 2026-08-14 | `rules.md § Family Aggregation` on `L002`, `L009`, `L018`, `L019` | `HISTORICAL` | `DERIVED` | `Macro_Z` |
| `L410` | macro slot inputs | JCI | beta_prox -0.2486 (z +1.368) · sector_lead +9.15% (z -0.139) · rate_sens -0.3551 vs TLT (z +0.698) · vol_stability -0.7176 (z +1.987) | mixed | 2026-08-14 | `rules.md § Family Aggregation` on `L002`, `L009`, `L018`, `L019` | `HISTORICAL` | `DERIVED` | `Macro_Z` |
| `L411` | macro slot inputs | BAC | beta_prox -0.6718 (z +0.600) · sector_lead +15.32% (z +1.232) · rate_sens -0.4721 vs TLT (z +0.527) · vol_stability -0.9698 (z +0.011) | mixed | 2026-08-14 | `rules.md § Family Aggregation` on `L002`, `L009`, `L018`, `L019` | `HISTORICAL` | `DERIVED` | `Macro_Z` |
| `L412` | macro slot inputs | MRK | beta_prox -1.4080 (z -0.737) · sector_lead +15.46% (z +1.260) · rate_sens -0.4181 vs TLT (z +0.606) · vol_stability -0.8007 (z +1.402) | mixed | 2026-08-14 | `rules.md § Family Aggregation` on `L002`, `L009`, `L018`, `L019` | `HISTORICAL` | `DERIVED` | `Macro_Z` |
| `L413` | macro slot inputs | SOLV | beta_prox -1.0655 (z -0.115) · sector_lead +15.46% (z +1.260) · rate_sens -0.9615 vs TLT (z -0.188) · vol_stability -1.0669 (z -0.789) | mixed | 2026-08-14 | `rules.md § Family Aggregation` on `L002`, `L009`, `L018`, `L019` | `HISTORICAL` | `DERIVED` | `Macro_Z` |
| `L414` | macro slot inputs | BX | beta_prox -0.0951 (z +1.647) · sector_lead +15.32% (z +1.232) · rate_sens -1.0880 vs TLT (z -0.373) · vol_stability -0.9491 (z +0.181) | mixed | 2026-08-14 | `rules.md § Family Aggregation` on `L002`, `L009`, `L018`, `L019` | `HISTORICAL` | `DERIVED` | `Macro_Z` |
| `L415` | macro slot inputs | URI | beta_prox -0.3282 (z +1.223) · sector_lead +11.24% (z +0.325) · rate_sens -0.6497 vs TLT (z +0.267) · vol_stability -1.1134 (z -1.172) | mixed | 2026-08-14 | `rules.md § Family Aggregation` on `L002`, `L009`, `L018`, `L019` | `HISTORICAL` | `DERIVED` | `Macro_Z` |
| `L416` | macro slot inputs | SCHW | beta_prox -1.1643 (z -0.294) · sector_lead +15.32% (z +1.232) · rate_sens -0.4706 vs TLT (z +0.529) · vol_stability -0.7894 (z +1.495) | mixed | 2026-08-14 | `rules.md § Family Aggregation` on `L002`, `L009`, `L018`, `L019` | `HISTORICAL` | `DERIVED` | `Macro_Z` |
| `L417` | macro slot inputs | STT | beta_prox -0.3170 (z +1.244) · sector_lead +15.32% (z +1.232) · rate_sens -0.2462 vs TLT (z +0.857) · vol_stability -1.0177 (z -0.384) | mixed | 2026-08-14 | `rules.md § Family Aggregation` on `L002`, `L009`, `L018`, `L019` | `HISTORICAL` | `DERIVED` | `Macro_Z` |
| `L418` | macro slot inputs | AMGN | beta_prox -0.9164 (z +0.156) · sector_lead +15.46% (z +1.260) · rate_sens -0.6513 vs TLT (z +0.265) · vol_stability -1.0265 (z -0.456) | mixed | 2026-08-14 | `rules.md § Family Aggregation` on `L002`, `L009`, `L018`, `L019` | `HISTORICAL` | `DERIVED` | `Macro_Z` |
| `L419` | macro slot inputs | FITB | beta_prox -0.6612 (z +0.619) · sector_lead +15.32% (z +1.232) · rate_sens -0.7305 vs TLT (z +0.149) · vol_stability -0.8327 (z +1.139) | mixed | 2026-08-14 | `rules.md § Family Aggregation` on `L002`, `L009`, `L018`, `L019` | `HISTORICAL` | `DERIVED` | `Macro_Z` |
| `L420` | macro slot inputs | BNY | beta_prox -0.4839 (z +0.941) · sector_lead +15.32% (z +1.232) · rate_sens -0.0494 vs TLT (z +1.144) · vol_stability -1.0705 (z -0.818) | mixed | 2026-08-14 | `rules.md § Family Aggregation` on `L002`, `L009`, `L018`, `L019` | `HISTORICAL` | `DERIVED` | `Macro_Z` |
| `L421` | macro slot inputs | IVZ | beta_prox -0.7447 (z +0.467) · sector_lead +15.32% (z +1.232) · rate_sens -0.8316 vs TLT (z +0.002) · vol_stability -1.0404 (z -0.571) | mixed | 2026-08-14 | `rules.md § Family Aggregation` on `L002`, `L009`, `L018`, `L019` | `HISTORICAL` | `DERIVED` | `Macro_Z` |
| `L422` | macro slot inputs | DASH | beta_prox -0.2809 (z +1.309) · sector_lead +11.24% (z +0.325) · rate_sens -1.5718 vs TLT (z -1.079) · vol_stability -0.9053 (z +0.542) | mixed | 2026-08-14 | `rules.md § Family Aggregation` on `L002`, `L009`, `L018`, `L019` | `HISTORICAL` | `DERIVED` | `Macro_Z` |
| `L423` | macro slot inputs | TECH | beta_prox -0.2550 (z +1.356) · sector_lead +15.46% (z +1.260) · rate_sens -1.3808 vs TLT (z -0.800) · vol_stability -0.0923 (z +1.987) | mixed | 2026-08-14 | `rules.md § Family Aggregation` on `L002`, `L009`, `L018`, `L019` | `HISTORICAL` | `DERIVED` | `Macro_Z` |
| `L424` | macro slot inputs | REGN | beta_prox -0.7473 (z +0.463) · sector_lead +15.46% (z +1.260) · rate_sens -0.2506 vs TLT (z +0.850) · vol_stability -1.0532 (z -0.676) | mixed | 2026-08-14 | `rules.md § Family Aggregation` on `L002`, `L009`, `L018`, `L019` | `HISTORICAL` | `DERIVED` | `Macro_Z` |

## Coverage summary

| `freshness_tag` | Rows |
|---|---|
| `LIVE` | 0 |
| `DELAYED` | 2 |
| `OFFICIAL_FILING` | 1 |
| `HISTORICAL` | 116 |
| `ILLUSTRATIVE_REF` | 0 |
| `UNAVAILABLE` | 2 |

| `claim_type` | Rows |
|---|---|
| `OBSERVED` | 39 |
| `DERIVED` | 78 |
| `INFERRED` | 2 |
| `ILLUSTRATIVE` | 0 |
| `UNAVAILABLE` | 2 |

Total rows: **121**. Every metric that feeds an `Adj Score`, penalty, confidence label
or sizing decision has a row above; the two families with no fetch path are recorded as
explicit `UNAVAILABLE` rows (`L021`, `L022`) rather than omitted or treated as neutral.

## Status eligibility

All five Required inputs from `rules.md § Input Classification` are grounded, so no Required
input blocks `GO`. The `NO_TRADE` verdict comes from `§ Evidence Thresholds`, not from this
ledger. Missing Enhancing inputs (options IV, short interest, bid-ask tape, analyst revisions,
institutional flow) lower the data-quality multiplier to 0.80 and cap
confidence — they are not cited as `GO` blockers anywhere in this package.
