# 01 — Preflight and Source Ledger

Run date `2026-08-07` · model `claude-opus-5` · basis `2026-08-07` · data mode `DELAYED`.

This ledger is written **before** reflection, scoring, portfolio construction or risk review
uses any fact downstream. Every price, return, volatility, beta, earnings date, target, CI
bound, drawdown, ratio, technical-indicator state and sizing input below is either sourced
here or marked `UNAVAILABLE`. Derived rows name their formula and input rows.

## Grounding summary

| Gate | Result |
|---|---|
| Symbols fetched | 519/519 (0 failures, 12.2s) |
| Last bar == basis | 518/519 |
| Ex-dividend `c != a` on the basis bar | 0 symbols |
| Published entry prices grounded (>=2 independent sources within 1%) | 27/27 |
| Max cross-vendor deviation | 0.0000% |
| Confirmation re-reads required | 0 |
| Scored universe | 511 of 515 (4 rejected) |

Three independent sources were used for every published name and core ETF — the
stockanalysis bulk history tree, `quote.cnbc.com` and `api.nasdaq.com/api/quote/{SYM}/info`.
At a post-close fire the vendor field semantics differ from both the pre-open and intraday
cases: CNBC's `last` is the official close only when `last_time` falls on the basis date
(`previous_day_closing` returns T-1), and Nasdaq's `secondaryData.lastSalePrice` is the close
only behind the "Closed at {basis} 4:00 PM ET" marker (`primaryData` is the after-hours
tape). Both gates were enforced in code, and all 27 symbols agreed to
0.0000%.

## Source Ledger

| row | artifact | field | ticker/entity | value | unit | observation_date | source | freshness_tag | claim_type | used_by |
|---|---|---|---|---|---|---|---|---|---|---|
| `L001` | 03/05 | daily OHLCV history (5y) | 519 symbols | 519/519 symbols, 1255 median bars | bars | 2026-08-07 | stockanalysis.com/api/symbol/{s\\|e}/{SYM}/history?range=5Y | `HISTORICAL` | `OBSERVED` | all price/return/indicator math |
| `L002` | 01 | adjusted-close tree | same 519 symbols | vendor field `a` written to the `Close` column of the adj/ tree | USD | 2026-08-07 | stockanalysis.com/api/symbol/{s\\|e}/{SYM}/history?range=5Y | `HISTORICAL` | `DERIVED` | technical_indicators.py input; momentum, RS, vol, beta, TE, drawdown (Track B 2026-07-26) |
| `L003` | 01 | raw-close tree | same 519 symbols | vendor field `c` | USD | 2026-08-07 | stockanalysis.com/api/symbol/{s\\|e}/{SYM}/history?range=5Y | `HISTORICAL` | `OBSERVED` | entry_price, target_price, CI bounds |
| `L004` | 03 | VIX close | ^VIX | 14.9 | index | 2026-08-07 | cdn.cboe.com/api/global/us_indices/daily_prices/VIX_History.csv | `HISTORICAL` | `OBSERVED` | regime classification, Macro_Z context |
| `L005` | 03 | VIX prior close | ^VIX | 15.15 | index | 2026-08-06 | cdn.cboe.com/.../VIX_History.csv | `HISTORICAL` | `OBSERVED` | vol-direction note in 03 |
| `L006` | 05 | risk-free rate (13-week bank discount) | US T-bill | 3.72 | % annual | 2026-08-07 | home.treasury.gov daily_treasury_bill_rates CSV 2026 | `OFFICIAL_FILING` | `OBSERVED` | Sharpe / Sortino / Treynor / Calmar excess-return numerators |
| `L007` | 05 | rf_1m | US T-bill | 0.3100 | % monthly | 2026-08-07 | formula rf_annual/12 on `L006` | `OFFICIAL_FILING` | `DERIVED` | same ratios as `L006` |
| `L008` | 04 | S&P 500 constituent cache | index | 503 | names | 2026-06-21 | agents/equity/turtle-trader/universe/sp500.json | `HISTORICAL` | `OBSERVED` | build_index_universe.py |
| `L009` | 04 | Nasdaq-100 constituent cache | index | 101 | names | 2026-06-21 | agents/equity/turtle-trader/universe/nasdaq100.json | `HISTORICAL` | `OBSERVED` | build_index_universe.py |
| `L010` | 04 | index union | S&P 500 union Nasdaq-100 | 515 | names | 2026-08-08 | build_index_universe.py (overlap 89) | `HISTORICAL` | `DERIVED` | eligible universe; `INDEX_UNION_PCTL` denominator |
| `L011` | 04 | market cap + sector | 7127 rows | one bulk call | USD / GICS-style | 2026-08-07 | api.nasdaq.com/api/screener/stocks?tableonly=true&limit=10000&download=true | `DELAYED` | `OBSERVED` | universe inclusion filters; sector_lead slot; sector tables |
| `L012` | 04 | forward earnings calendar sweep | full universe | 26/26 business days, sweep_complete=True | days | 2026-08-07 | api.nasdaq.com/api/calendar/earnings?date=YYYY-MM-DD | `DELAYED` | `OBSERVED` | earnings penalty; event-concentration flag |
| `L013` | 05 | names with a confirmed print in the 37d window | universe | 59 | names | 2026-08-07 | derived from `L012` | `DELAYED` | `DERIVED` | `CONFIRMED_CALENDAR` tagging |
| `L014` | 05 | names penalized (earnings <= 14d) | universe | 26 | names | 2026-08-07 | derived from `L012`; rules.md § Risk Controls -0.10 | `DELAYED` | `DERIVED` | Adj Score penalty term |
| `L015` | 03 | benchmark close | SPY | 773.26 | USD | 2026-08-07 | stockanalysis.com/api/symbol/{s\\|e}/{SYM}/history?range=5Y + CNBC + Nasdaq (3 sources, 0.0000% dev) | `HISTORICAL` | `OBSERVED` | benchmark_price on every EQUITY_ALPHA record; beta; RS; alpha |
| `L016` | 01 | price grounding pass | 27 symbols | 27/27 grounded, max deviation 0.0000% | % | 2026-08-07 | stockanalysis + quote.cnbc.com + api.nasdaq.com/api/quote/{SYM}/info | `HISTORICAL` | `DERIVED` | Price Sourcing Standard gate for every published entry_price |
| `L017` | 02 | canonical settlement ledger | all models | EQ n=643 eff_n=2; MF n=108 eff_n=1; due=50; conflicts=0 | records | 2026-08-07 | settlement_ledger.py --as-of 2026-08-07 | `HISTORICAL` | `DERIVED` | rolling calibration; Track A gating; reflection § 0 |
| `L018` | 02 | deferred settlement diagnostic | 50 due keys | 50 priced at the 2026-08-07 close; not published as canonical | records | 2026-08-07 | raw closes from `L003`; benchmark from `L015` | `HISTORICAL` | `DERIVED` | reflection § 0 diagnostic; MoM table; tie-break disclosure |
| `L019` | 05 | technical indicator pack | 519 symbols | daily/weekly/monthly TD-9, RSI(14), MACD(12,26,9), MA alignment, momentum, volume ratio, RS vs SPY | mixed | 2026-08-07 | technical_indicators.py --benchmark SPY --range 5y --history-dir <adj tree> (input rows `L002`) | `HISTORICAL` | `DERIVED` | Tech_Z slots; displayed indicator states in 05/06/07/09; `15_predictions.json` |
| `L020` | 03 | TLT history | TLT | 1255 bars, last close 82.76 | USD | 2026-08-07 | stockanalysis.com/api/symbol/{s\\|e}/{SYM}/history?range=5Y | `HISTORICAL` | `OBSERVED` | `rate_sens` Macro_Z slot |
| `L021` | 05 | data quality multiplier | run-level | 0.80 | multiplier | 2026-08-07 | rules.md § Data Quality Multiplier — 0.80 notable coverage gaps (2 of 4 families) | `HISTORICAL` | `INFERRED` | every Adj Score |
| `L022` | 05 | Fund_Z family | universe-wide | UNAVAILABLE | z | 2026-08-07 | no XBRL fetch path wired at universe scale | `UNAVAILABLE` | `UNAVAILABLE` | evidence threshold #2/#3; DQ multiplier |
| `L023` | 05 | Sent_Z family | universe-wide | UNAVAILABLE | z | 2026-08-07 | no short-interest / revision / IV feed wired | `UNAVAILABLE` | `UNAVAILABLE` | evidence threshold #2/#3; DQ multiplier |
| `L024` | 07 | top-20 correlation matrix | top 20 by Adj Score | avg pairwise 0.1699, max 0.7287 (WSM/SWK) | correlation | 2026-08-07 | corrcoef of 60 daily adjusted returns from `L002` | `HISTORICAL` | `DERIVED` | portfolio correlation cap check |
| `L025` | 07 | naive top-20 EW 95th-pctl 1m drawdown | sleeve | 9.15% | % | 2026-08-07 | 1.65 x sqrt(w' Sigma w) x sqrt(21) on `L002`; normality assumed | `HISTORICAL` | `DERIVED` | `rules.md § Stop Criteria` downgrade #5 |
| `L026` | 07 | attainable sleeve beta range | >=80th pctl pool | -0.3876 … 1.3387 | beta | 2026-08-07 | mean of the 20 lowest / 20 highest betas under the 5% cap | `HISTORICAL` | `DERIVED` | Task 0 feasibility pre-check |
| `L101` | 05/06/07/09 | entry price (raw close) | DASH | 216.26 | USD | 2026-08-07 | 2 independent sources agree to 0.0000% | `HISTORICAL` | `OBSERVED` | target_price, CI bounds, Kelly sizing input |
| `L102` | 05/06/07/09 | entry price (raw close) | ABNB | 178.07 | USD | 2026-08-07 | 2 independent sources agree to 0.0000% | `HISTORICAL` | `OBSERVED` | target_price, CI bounds, Kelly sizing input |
| `L103` | 05/06/07/09 | entry price (raw close) | GEN | 29.17 | USD | 2026-08-07 | 2 independent sources agree to 0.0000% | `HISTORICAL` | `OBSERVED` | target_price, CI bounds, Kelly sizing input |
| `L104` | 05/06/07/09 | entry price (raw close) | VEEV | 230.47 | USD | 2026-08-07 | 2 independent sources agree to 0.0000% | `HISTORICAL` | `OBSERVED` | target_price, CI bounds, Kelly sizing input |
| `L105` | 05/06/07/09 | entry price (raw close) | HPQ | 30.05 | USD | 2026-08-07 | 2 independent sources agree to 0.0000% | `HISTORICAL` | `OBSERVED` | target_price, CI bounds, Kelly sizing input |
| `L106` | 05/06/07/09 | entry price (raw close) | WSM | 251.78 | USD | 2026-08-07 | 2 independent sources agree to 0.0000% | `HISTORICAL` | `OBSERVED` | target_price, CI bounds, Kelly sizing input |
| `L107` | 05/06/07/09 | entry price (raw close) | TECH | 72.29 | USD | 2026-08-07 | 2 independent sources agree to 0.0000% | `HISTORICAL` | `OBSERVED` | target_price, CI bounds, Kelly sizing input |
| `L108` | 05/06/07/09 | entry price (raw close) | DXCM | 84.75 | USD | 2026-08-07 | 2 independent sources agree to 0.0000% | `HISTORICAL` | `OBSERVED` | target_price, CI bounds, Kelly sizing input |
| `L109` | 05/06/07/09 | entry price (raw close) | CPAY | 392.94 | USD | 2026-08-07 | 2 independent sources agree to 0.0000% | `HISTORICAL` | `OBSERVED` | target_price, CI bounds, Kelly sizing input |
| `L110` | 05/06/07/09 | entry price (raw close) | NTAP | 189.52 | USD | 2026-08-07 | 2 independent sources agree to 0.0000% | `HISTORICAL` | `OBSERVED` | target_price, CI bounds, Kelly sizing input |
| `L111` | 05/06/07/09 | entry price (raw close) | BAX | 27.55 | USD | 2026-08-07 | 2 independent sources agree to 0.0000% | `HISTORICAL` | `OBSERVED` | target_price, CI bounds, Kelly sizing input |
| `L112` | 05/06/07/09 | entry price (raw close) | GPN | 86.12 | USD | 2026-08-07 | 2 independent sources agree to 0.0000% | `HISTORICAL` | `OBSERVED` | target_price, CI bounds, Kelly sizing input |
| `L113` | 05/06/07/09 | entry price (raw close) | MET | 97.77 | USD | 2026-08-07 | 2 independent sources agree to 0.0000% | `HISTORICAL` | `OBSERVED` | target_price, CI bounds, Kelly sizing input |
| `L114` | 05/06/07/09 | entry price (raw close) | SWK | 103.89 | USD | 2026-08-07 | 2 independent sources agree to 0.0000% | `HISTORICAL` | `OBSERVED` | target_price, CI bounds, Kelly sizing input |
| `L115` | 05/06/07/09 | entry price (raw close) | PH | 1,073.87 | USD | 2026-08-07 | 2 independent sources agree to 0.0000% | `HISTORICAL` | `OBSERVED` | target_price, CI bounds, Kelly sizing input |
| `L116` | 05/06/07/09 | entry price (raw close) | PFE | 26.76 | USD | 2026-08-07 | 2 independent sources agree to 0.0000% | `HISTORICAL` | `OBSERVED` | target_price, CI bounds, Kelly sizing input |
| `L117` | 05/06/07/09 | entry price (raw close) | TPR | 162.36 | USD | 2026-08-07 | 2 independent sources agree to 0.0000% | `HISTORICAL` | `OBSERVED` | target_price, CI bounds, Kelly sizing input |
| `L118` | 05/06/07/09 | entry price (raw close) | FAST | 51.84 | USD | 2026-08-07 | 2 independent sources agree to 0.0000% | `HISTORICAL` | `OBSERVED` | target_price, CI bounds, Kelly sizing input |
| `L119` | 05/06/07/09 | entry price (raw close) | INSM | 131.10 | USD | 2026-08-07 | 2 independent sources agree to 0.0000% | `HISTORICAL` | `OBSERVED` | target_price, CI bounds, Kelly sizing input |
| `L120` | 05/06/07/09 | entry price (raw close) | GRMN | 310.89 | USD | 2026-08-07 | 2 independent sources agree to 0.0000% | `HISTORICAL` | `OBSERVED` | target_price, CI bounds, Kelly sizing input |
| `L121` | 05/06/07/09 | entry price (raw close) | EXPE | 310.68 | USD | 2026-08-07 | 2 independent sources agree to 0.0000% | `HISTORICAL` | `OBSERVED` | target_price, CI bounds, Kelly sizing input |
| `L122` | 05/06/07/09 | entry price (raw close) | BKNG | 214.42 | USD | 2026-08-07 | 2 independent sources agree to 0.0000% | `HISTORICAL` | `OBSERVED` | target_price, CI bounds, Kelly sizing input |
| `L123` | 05/06/07/09 | entry price (raw close) | WTW | 344.82 | USD | 2026-08-07 | 2 independent sources agree to 0.0000% | `HISTORICAL` | `OBSERVED` | target_price, CI bounds, Kelly sizing input |
| `L124` | 05/06/07/09 | entry price (raw close) | CRL | 267.49 | USD | 2026-08-07 | 2 independent sources agree to 0.0000% | `HISTORICAL` | `OBSERVED` | target_price, CI bounds, Kelly sizing input |
| `L201` | 05/15 | REALIZED_VOL_30D | DASH | 12.30% | % 1-month | 2026-08-07 | population stdev of 30 daily adjusted returns x sqrt(21) on `L002` | `HISTORICAL` | `DERIVED` | sigma; CI bounds; Sharpe; VaR/CVaR; Kelly |
| `L202` | 05/15 | REALIZED_VOL_30D | ABNB | 16.69% | % 1-month | 2026-08-07 | population stdev of 30 daily adjusted returns x sqrt(21) on `L002` | `HISTORICAL` | `DERIVED` | sigma; CI bounds; Sharpe; VaR/CVaR; Kelly |
| `L203` | 05/15 | REALIZED_VOL_30D | GEN | 9.66% | % 1-month | 2026-08-07 | population stdev of 30 daily adjusted returns x sqrt(21) on `L002` | `HISTORICAL` | `DERIVED` | sigma; CI bounds; Sharpe; VaR/CVaR; Kelly |
| `L204` | 05/15 | REALIZED_VOL_30D | VEEV | 12.86% | % 1-month | 2026-08-07 | population stdev of 30 daily adjusted returns x sqrt(21) on `L002` | `HISTORICAL` | `DERIVED` | sigma; CI bounds; Sharpe; VaR/CVaR; Kelly |
| `L205` | 05/15 | REALIZED_VOL_30D | HPQ | 13.38% | % 1-month | 2026-08-07 | population stdev of 30 daily adjusted returns x sqrt(21) on `L002` | `HISTORICAL` | `DERIVED` | sigma; CI bounds; Sharpe; VaR/CVaR; Kelly |
| `L206` | 05/15 | REALIZED_VOL_30D | WSM | 9.11% | % 1-month | 2026-08-07 | population stdev of 30 daily adjusted returns x sqrt(21) on `L002` | `HISTORICAL` | `DERIVED` | sigma; CI bounds; Sharpe; VaR/CVaR; Kelly |
| `L207` | 05/15 | REALIZED_VOL_30D | TECH | 1.42% | % 1-month | 2026-08-07 | population stdev of 30 daily adjusted returns x sqrt(21) on `L002` | `HISTORICAL` | `DERIVED` | sigma; CI bounds; Sharpe; VaR/CVaR; Kelly |
| `L208` | 05/15 | REALIZED_VOL_30D | DXCM | 15.32% | % 1-month | 2026-08-07 | population stdev of 30 daily adjusted returns x sqrt(21) on `L002` | `HISTORICAL` | `DERIVED` | sigma; CI bounds; Sharpe; VaR/CVaR; Kelly |
| `L209` | 05/15 | REALIZED_VOL_30D | CPAY | 7.66% | % 1-month | 2026-08-07 | population stdev of 30 daily adjusted returns x sqrt(21) on `L002` | `HISTORICAL` | `DERIVED` | sigma; CI bounds; Sharpe; VaR/CVaR; Kelly |
| `L210` | 05/15 | REALIZED_VOL_30D | NTAP | 12.57% | % 1-month | 2026-08-07 | population stdev of 30 daily adjusted returns x sqrt(21) on `L002` | `HISTORICAL` | `DERIVED` | sigma; CI bounds; Sharpe; VaR/CVaR; Kelly |
| `L211` | 05/15 | REALIZED_VOL_30D | BAX | 14.38% | % 1-month | 2026-08-07 | population stdev of 30 daily adjusted returns x sqrt(21) on `L002` | `HISTORICAL` | `DERIVED` | sigma; CI bounds; Sharpe; VaR/CVaR; Kelly |
| `L212` | 05/15 | REALIZED_VOL_30D | GPN | 12.62% | % 1-month | 2026-08-07 | population stdev of 30 daily adjusted returns x sqrt(21) on `L002` | `HISTORICAL` | `DERIVED` | sigma; CI bounds; Sharpe; VaR/CVaR; Kelly |
| `L213` | 05/15 | REALIZED_VOL_30D | MET | 6.70% | % 1-month | 2026-08-07 | population stdev of 30 daily adjusted returns x sqrt(21) on `L002` | `HISTORICAL` | `DERIVED` | sigma; CI bounds; Sharpe; VaR/CVaR; Kelly |
| `L214` | 05/15 | REALIZED_VOL_30D | SWK | 10.51% | % 1-month | 2026-08-07 | population stdev of 30 daily adjusted returns x sqrt(21) on `L002` | `HISTORICAL` | `DERIVED` | sigma; CI bounds; Sharpe; VaR/CVaR; Kelly |
| `L215` | 05/15 | REALIZED_VOL_30D | PH | 8.54% | % 1-month | 2026-08-07 | population stdev of 30 daily adjusted returns x sqrt(21) on `L002` | `HISTORICAL` | `DERIVED` | sigma; CI bounds; Sharpe; VaR/CVaR; Kelly |
| `L216` | 05/15 | REALIZED_VOL_30D | PFE | 5.68% | % 1-month | 2026-08-07 | population stdev of 30 daily adjusted returns x sqrt(21) on `L002` | `HISTORICAL` | `DERIVED` | sigma; CI bounds; Sharpe; VaR/CVaR; Kelly |
| `L217` | 05/15 | REALIZED_VOL_30D | TPR | 8.52% | % 1-month | 2026-08-07 | population stdev of 30 daily adjusted returns x sqrt(21) on `L002` | `HISTORICAL` | `DERIVED` | sigma; CI bounds; Sharpe; VaR/CVaR; Kelly |
| `L218` | 05/15 | REALIZED_VOL_30D | FAST | 7.44% | % 1-month | 2026-08-07 | population stdev of 30 daily adjusted returns x sqrt(21) on `L002` | `HISTORICAL` | `DERIVED` | sigma; CI bounds; Sharpe; VaR/CVaR; Kelly |
| `L219` | 05/15 | REALIZED_VOL_30D | INSM | 29.31% | % 1-month | 2026-08-07 | population stdev of 30 daily adjusted returns x sqrt(21) on `L002` | `HISTORICAL` | `DERIVED` | sigma; CI bounds; Sharpe; VaR/CVaR; Kelly |
| `L220` | 05/15 | REALIZED_VOL_30D | GRMN | 15.34% | % 1-month | 2026-08-07 | population stdev of 30 daily adjusted returns x sqrt(21) on `L002` | `HISTORICAL` | `DERIVED` | sigma; CI bounds; Sharpe; VaR/CVaR; Kelly |
| `L221` | 05/15 | REALIZED_VOL_30D | EXPE | 12.68% | % 1-month | 2026-08-07 | population stdev of 30 daily adjusted returns x sqrt(21) on `L002` | `HISTORICAL` | `DERIVED` | sigma; CI bounds; Sharpe; VaR/CVaR; Kelly |
| `L222` | 05/15 | REALIZED_VOL_30D | BKNG | 12.38% | % 1-month | 2026-08-07 | population stdev of 30 daily adjusted returns x sqrt(21) on `L002` | `HISTORICAL` | `DERIVED` | sigma; CI bounds; Sharpe; VaR/CVaR; Kelly |
| `L223` | 05/15 | REALIZED_VOL_30D | WTW | 9.65% | % 1-month | 2026-08-07 | population stdev of 30 daily adjusted returns x sqrt(21) on `L002` | `HISTORICAL` | `DERIVED` | sigma; CI bounds; Sharpe; VaR/CVaR; Kelly |
| `L224` | 05/15 | REALIZED_VOL_30D | CRL | 13.55% | % 1-month | 2026-08-07 | population stdev of 30 daily adjusted returns x sqrt(21) on `L002` | `HISTORICAL` | `DERIVED` | sigma; CI bounds; Sharpe; VaR/CVaR; Kelly |
| `L301` | 05/07 | beta vs SPY (60d) | DASH | 1.1917 | beta | 2026-08-07 | cov(r, r_SPY, ddof=0)/var(r_SPY) over 60 return intervals on `L002` | `HISTORICAL` | `DERIVED` | Macro_Z beta slot; Treynor; IR; sleeve beta |
| `L302` | 05/07 | beta vs SPY (60d) | ABNB | 0.7421 | beta | 2026-08-07 | cov(r, r_SPY, ddof=0)/var(r_SPY) over 60 return intervals on `L002` | `HISTORICAL` | `DERIVED` | Macro_Z beta slot; Treynor; IR; sleeve beta |
| `L303` | 05/07 | beta vs SPY (60d) | GEN | 0.4017 | beta | 2026-08-07 | cov(r, r_SPY, ddof=0)/var(r_SPY) over 60 return intervals on `L002` | `HISTORICAL` | `DERIVED` | Macro_Z beta slot; Treynor; IR; sleeve beta |
| `L304` | 05/07 | beta vs SPY (60d) | VEEV | 0.1662 | beta | 2026-08-07 | cov(r, r_SPY, ddof=0)/var(r_SPY) over 60 return intervals on `L002` | `HISTORICAL` | `DERIVED` | Macro_Z beta slot; Treynor; IR; sleeve beta |
| `L305` | 05/07 | beta vs SPY (60d) | HPQ | 0.4424 | beta | 2026-08-07 | cov(r, r_SPY, ddof=0)/var(r_SPY) over 60 return intervals on `L002` | `HISTORICAL` | `DERIVED` | Macro_Z beta slot; Treynor; IR; sleeve beta |
| `L306` | 05/07 | beta vs SPY (60d) | WSM | 0.9798 | beta | 2026-08-07 | cov(r, r_SPY, ddof=0)/var(r_SPY) over 60 return intervals on `L002` | `HISTORICAL` | `DERIVED` | Macro_Z beta slot; Treynor; IR; sleeve beta |
| `L307` | 05/07 | beta vs SPY (60d) | TECH | 0.7110 | beta | 2026-08-07 | cov(r, r_SPY, ddof=0)/var(r_SPY) over 60 return intervals on `L002` | `HISTORICAL` | `DERIVED` | Macro_Z beta slot; Treynor; IR; sleeve beta |
| `L308` | 05/07 | beta vs SPY (60d) | DXCM | 0.2453 | beta | 2026-08-07 | cov(r, r_SPY, ddof=0)/var(r_SPY) over 60 return intervals on `L002` | `HISTORICAL` | `DERIVED` | Macro_Z beta slot; Treynor; IR; sleeve beta |
| `L309` | 05/07 | beta vs SPY (60d) | CPAY | 0.2729 | beta | 2026-08-07 | cov(r, r_SPY, ddof=0)/var(r_SPY) over 60 return intervals on `L002` | `HISTORICAL` | `DERIVED` | Macro_Z beta slot; Treynor; IR; sleeve beta |
| `L310` | 05/07 | beta vs SPY (60d) | NTAP | 1.4032 | beta | 2026-08-07 | cov(r, r_SPY, ddof=0)/var(r_SPY) over 60 return intervals on `L002` | `HISTORICAL` | `DERIVED` | Macro_Z beta slot; Treynor; IR; sleeve beta |
| `L311` | 05/07 | beta vs SPY (60d) | BAX | 0.6615 | beta | 2026-08-07 | cov(r, r_SPY, ddof=0)/var(r_SPY) over 60 return intervals on `L002` | `HISTORICAL` | `DERIVED` | Macro_Z beta slot; Treynor; IR; sleeve beta |
| `L312` | 05/07 | beta vs SPY (60d) | GPN | 0.8468 | beta | 2026-08-07 | cov(r, r_SPY, ddof=0)/var(r_SPY) over 60 return intervals on `L002` | `HISTORICAL` | `DERIVED` | Macro_Z beta slot; Treynor; IR; sleeve beta |
| `L313` | 05/07 | beta vs SPY (60d) | MET | -0.0820 | beta | 2026-08-07 | cov(r, r_SPY, ddof=0)/var(r_SPY) over 60 return intervals on `L002` | `HISTORICAL` | `DERIVED` | Macro_Z beta slot; Treynor; IR; sleeve beta |
| `L314` | 05/07 | beta vs SPY (60d) | SWK | 1.6043 | beta | 2026-08-07 | cov(r, r_SPY, ddof=0)/var(r_SPY) over 60 return intervals on `L002` | `HISTORICAL` | `DERIVED` | Macro_Z beta slot; Treynor; IR; sleeve beta |
| `L315` | 05/07 | beta vs SPY (60d) | PH | 0.5754 | beta | 2026-08-07 | cov(r, r_SPY, ddof=0)/var(r_SPY) over 60 return intervals on `L002` | `HISTORICAL` | `DERIVED` | Macro_Z beta slot; Treynor; IR; sleeve beta |
| `L316` | 05/07 | beta vs SPY (60d) | PFE | -0.0451 | beta | 2026-08-07 | cov(r, r_SPY, ddof=0)/var(r_SPY) over 60 return intervals on `L002` | `HISTORICAL` | `DERIVED` | Macro_Z beta slot; Treynor; IR; sleeve beta |
| `L317` | 05/07 | beta vs SPY (60d) | TPR | 0.7401 | beta | 2026-08-07 | cov(r, r_SPY, ddof=0)/var(r_SPY) over 60 return intervals on `L002` | `HISTORICAL` | `DERIVED` | Macro_Z beta slot; Treynor; IR; sleeve beta |
| `L318` | 05/07 | beta vs SPY (60d) | FAST | 0.3731 | beta | 2026-08-07 | cov(r, r_SPY, ddof=0)/var(r_SPY) over 60 return intervals on `L002` | `HISTORICAL` | `DERIVED` | Macro_Z beta slot; Treynor; IR; sleeve beta |
| `L319` | 05/07 | beta vs SPY (60d) | INSM | 0.8074 | beta | 2026-08-07 | cov(r, r_SPY, ddof=0)/var(r_SPY) over 60 return intervals on `L002` | `HISTORICAL` | `DERIVED` | Macro_Z beta slot; Treynor; IR; sleeve beta |
| `L320` | 05/07 | beta vs SPY (60d) | GRMN | 0.2193 | beta | 2026-08-07 | cov(r, r_SPY, ddof=0)/var(r_SPY) over 60 return intervals on `L002` | `HISTORICAL` | `DERIVED` | Macro_Z beta slot; Treynor; IR; sleeve beta |
| `L321` | 05/07 | beta vs SPY (60d) | EXPE | 0.3997 | beta | 2026-08-07 | cov(r, r_SPY, ddof=0)/var(r_SPY) over 60 return intervals on `L002` | `HISTORICAL` | `DERIVED` | Macro_Z beta slot; Treynor; IR; sleeve beta |
| `L322` | 05/07 | beta vs SPY (60d) | BKNG | 0.4459 | beta | 2026-08-07 | cov(r, r_SPY, ddof=0)/var(r_SPY) over 60 return intervals on `L002` | `HISTORICAL` | `DERIVED` | Macro_Z beta slot; Treynor; IR; sleeve beta |
| `L323` | 05/07 | beta vs SPY (60d) | WTW | -0.3291 | beta | 2026-08-07 | cov(r, r_SPY, ddof=0)/var(r_SPY) over 60 return intervals on `L002` | `HISTORICAL` | `DERIVED` | Macro_Z beta slot; Treynor; IR; sleeve beta |
| `L324` | 05/07 | beta vs SPY (60d) | CRL | 0.6017 | beta | 2026-08-07 | cov(r, r_SPY, ddof=0)/var(r_SPY) over 60 return intervals on `L002` | `HISTORICAL` | `DERIVED` | Macro_Z beta slot; Treynor; IR; sleeve beta |
| `L401` | 05 | next earnings date | DASH | NO_PRINT_IN_WINDOW | date | 2026-08-07 | `L012` forward sweep — NO_PRINT_IN_WINDOW | `DELAYED` | `OBSERVED` | penalty 0.00; confidence cap |
| `L402` | 05 | next earnings date | ABNB | NO_PRINT_IN_WINDOW | date | 2026-08-07 | `L012` forward sweep — NO_PRINT_IN_WINDOW | `DELAYED` | `OBSERVED` | penalty 0.00; confidence cap |
| `L403` | 05 | next earnings date | GEN | NO_PRINT_IN_WINDOW | date | 2026-08-07 | `L012` forward sweep — NO_PRINT_IN_WINDOW | `DELAYED` | `OBSERVED` | penalty 0.00; confidence cap |
| `L404` | 05 | next earnings date | VEEV | 2026-08-26 | date | 2026-08-07 | `L012` forward sweep — CONFIRMED_CALENDAR | `DELAYED` | `OBSERVED` | penalty 0.00; confidence cap |
| `L405` | 05 | next earnings date | HPQ | 2026-08-26 | date | 2026-08-07 | `L012` forward sweep — CONFIRMED_CALENDAR | `DELAYED` | `OBSERVED` | penalty 0.00; confidence cap |
| `L406` | 05 | next earnings date | WSM | 2026-08-26 | date | 2026-08-07 | `L012` forward sweep — CONFIRMED_CALENDAR | `DELAYED` | `OBSERVED` | penalty 0.00; confidence cap |
| `L407` | 05 | next earnings date | TECH | NO_PRINT_IN_WINDOW | date | 2026-08-07 | `L012` forward sweep — NO_PRINT_IN_WINDOW | `DELAYED` | `OBSERVED` | penalty 0.00; confidence cap |
| `L408` | 05 | next earnings date | DXCM | NO_PRINT_IN_WINDOW | date | 2026-08-07 | `L012` forward sweep — NO_PRINT_IN_WINDOW | `DELAYED` | `OBSERVED` | penalty 0.00; confidence cap |
| `L409` | 05 | next earnings date | CPAY | NO_PRINT_IN_WINDOW | date | 2026-08-07 | `L012` forward sweep — NO_PRINT_IN_WINDOW | `DELAYED` | `OBSERVED` | penalty 0.00; confidence cap |
| `L410` | 05 | next earnings date | NTAP | 2026-08-26 | date | 2026-08-07 | `L012` forward sweep — CONFIRMED_CALENDAR | `DELAYED` | `OBSERVED` | penalty 0.00; confidence cap |
| `L411` | 05 | next earnings date | BAX | NO_PRINT_IN_WINDOW | date | 2026-08-07 | `L012` forward sweep — NO_PRINT_IN_WINDOW | `DELAYED` | `OBSERVED` | penalty 0.00; confidence cap |
| `L412` | 05 | next earnings date | GPN | NO_PRINT_IN_WINDOW | date | 2026-08-07 | `L012` forward sweep — NO_PRINT_IN_WINDOW | `DELAYED` | `OBSERVED` | penalty 0.00; confidence cap |
| `L413` | 05 | next earnings date | MET | NO_PRINT_IN_WINDOW | date | 2026-08-07 | `L012` forward sweep — NO_PRINT_IN_WINDOW | `DELAYED` | `OBSERVED` | penalty 0.00; confidence cap |
| `L414` | 05 | next earnings date | SWK | NO_PRINT_IN_WINDOW | date | 2026-08-07 | `L012` forward sweep — NO_PRINT_IN_WINDOW | `DELAYED` | `OBSERVED` | penalty 0.00; confidence cap |
| `L415` | 05 | next earnings date | PH | NO_PRINT_IN_WINDOW | date | 2026-08-07 | `L012` forward sweep — NO_PRINT_IN_WINDOW | `DELAYED` | `OBSERVED` | penalty 0.00; confidence cap |
| `L416` | 05 | next earnings date | PFE | NO_PRINT_IN_WINDOW | date | 2026-08-07 | `L012` forward sweep — NO_PRINT_IN_WINDOW | `DELAYED` | `OBSERVED` | penalty 0.00; confidence cap |
| `L417` | 05 | next earnings date | TPR | 2026-08-13 | date | 2026-08-07 | `L012` forward sweep — CONFIRMED_CALENDAR | `DELAYED` | `OBSERVED` | penalty 0.10; confidence cap |
| `L418` | 05 | next earnings date | FAST | NO_PRINT_IN_WINDOW | date | 2026-08-07 | `L012` forward sweep — NO_PRINT_IN_WINDOW | `DELAYED` | `OBSERVED` | penalty 0.00; confidence cap |
| `L419` | 05 | next earnings date | INSM | NO_PRINT_IN_WINDOW | date | 2026-08-07 | `L012` forward sweep — NO_PRINT_IN_WINDOW | `DELAYED` | `OBSERVED` | penalty 0.00; confidence cap |
| `L420` | 05 | next earnings date | GRMN | NO_PRINT_IN_WINDOW | date | 2026-08-07 | `L012` forward sweep — NO_PRINT_IN_WINDOW | `DELAYED` | `OBSERVED` | penalty 0.00; confidence cap |
| `L421` | 05 | next earnings date | EXPE | NO_PRINT_IN_WINDOW | date | 2026-08-07 | `L012` forward sweep — NO_PRINT_IN_WINDOW | `DELAYED` | `OBSERVED` | penalty 0.00; confidence cap |
| `L422` | 05 | next earnings date | BKNG | NO_PRINT_IN_WINDOW | date | 2026-08-07 | `L012` forward sweep — NO_PRINT_IN_WINDOW | `DELAYED` | `OBSERVED` | penalty 0.00; confidence cap |
| `L423` | 05 | next earnings date | WTW | NO_PRINT_IN_WINDOW | date | 2026-08-07 | `L012` forward sweep — NO_PRINT_IN_WINDOW | `DELAYED` | `OBSERVED` | penalty 0.00; confidence cap |
| `L424` | 05 | next earnings date | CRL | NO_PRINT_IN_WINDOW | date | 2026-08-07 | `L012` forward sweep — NO_PRINT_IN_WINDOW | `DELAYED` | `OBSERVED` | penalty 0.00; confidence cap |

Per-name rows are emitted for all 24 published names in four families
(`L101`–`L124` entry price, `L201`–`L224` sigma,
`L301`–`L324` beta, `L401`–`L424` earnings date). Technical-indicator
states for those names derive from `L019`, whose own input is `L002`; the working
`technical_indicators.json` is a `.work/` artifact and is not a durable dependency — every
value that affects a score, recommendation or forecast is persisted in `05` and
`15_predictions.json`.

## Technical indicator coverage

| Indicator / timeframe | Sourceable | UNAVAILABLE | Coverage |
|---|---|---|---|
| 20-bar momentum daily | 511 | 0 | 100.00% |
| 20-bar momentum monthly | 510 | 1 | 99.80% |
| 20-bar momentum weekly | 511 | 0 | 100.00% |
| MA alignment daily | 511 | 0 | 100.00% |
| MA alignment monthly | 504 | 7 | 98.63% |
| MA alignment weekly | 511 | 0 | 100.00% |
| MACD(12,26,9) daily | 511 | 0 | 100.00% |
| MACD(12,26,9) monthly | 508 | 3 | 99.41% |
| MACD(12,26,9) weekly | 511 | 0 | 100.00% |
| RSI(14) daily | 511 | 0 | 100.00% |
| RSI(14) monthly | 511 | 0 | 100.00% |
| RSI(14) weekly | 511 | 0 | 100.00% |
| Relative strength vs SPY daily | 511 | 0 | 100.00% |
| TD-9 daily | 511 | 0 | 100.00% |
| TD-9 monthly | 511 | 0 | 100.00% |
| TD-9 weekly | 511 | 0 | 100.00% |
| Volume ratio daily | 511 | 0 | 100.00% |
| Volume ratio monthly | 510 | 1 | 99.80% |
| Volume ratio weekly | 511 | 0 | 100.00% |

Every indicator clears the 70%-of-universe bar `rules.md § Financial Metrics and Score
Attribution` requires before a metric may contribute to `Adj Score`.

## Families with no fetch path

`Fund_Z` (`L022`) and `Sent_Z` (`L023`) are `UNAVAILABLE` across the entire universe, not
merely sparse. Per `rules.md § Family Aggregation` their displayed contribution is
`0.00 (UNAVAILABLE)`, they do not count toward the "3 of 4 families supportive" threshold, and
they pull the data-quality multiplier to 0.80 (`L021`). They are **not**
treated as neutral or supportive anywhere in this package.
