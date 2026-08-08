# 01 — Preflight and Source Ledger

Run `2026-08-06` · model `claude-opus-5` · price basis **`2026-08-05`** · data mode `DELAYED`.

This ledger is written **before** reflection, scoring, portfolio construction or risk
review consumes any fact downstream.

## Source Ledger

| row | artifact | field | ticker/entity | value | unit | observation_date | source | freshness_tag | claim_type | used_by |
|---|---|---|---|---|---|---|---|---|---|---|
| L001 | price history | daily OHLCV 5y (raw close `c`) | 511 scored names + SPY/QQQ/SOXX/TLT | 519 symbols, median 1255 bars | USD | 2026-08-05 | stockanalysis.com/api/symbol/{s\\|e}/{SYM}/history?range=5Y (retrieved_at 2026-08-06T15:22:42Z) | HISTORICAL | OBSERVED | entry/target/CI prices; settlement prices |
| L002 | price history | daily adjusted close `a` | 511 scored names + core ETFs | same series, adjusted field | USD | 2026-08-05 | stockanalysis.com/api/symbol/{s\\|e}/{SYM}/history?range=5Y (retrieved_at 2026-08-06T15:22:42Z) | HISTORICAL | OBSERVED | ALL return/indicator math (Track B 2026-07-26) |
| L003 | price verification | entry price cross-check | 27 published symbols | 27/27 grounded, max dev 0.0000% | USD | 2026-08-05 | stockanalysis `c` + CNBC `previous_day_closing` + Nasdaq summary `PreviousClose` (retrieved_at 2026-08-06T15:30:46Z) | HISTORICAL | OBSERVED | Price Sourcing Standard gate |
| L004 | technical_indicators.json | TD-9 / RSI(14) / MACD / MA / momentum / volume / RS | 519 symbols, daily+weekly+monthly | full pack | mixed | 2026-08-05 | `technical_indicators.py --tickers SPY QQQ SOXX TLT --tickers-file eligible_universe.txt --benchmark SPY --range 5y --history-dir .work/{run}/adj` (formula: rules.md § Technical Indicator Pack Definition) | DERIVED | DERIVED | `Tech_Z` slots; displayed indicator states |
| L005 | run_computed_manifest.json | `Tech_Z` / `Macro_Z` / `Composite_Z` / `Adj Score` | 511 scored names | see `05_factor_scores.md` | z-score | 2026-08-05 | formula: rules.md § Financial Metrics and Score Attribution; slot definitions per the Metric Definition Table in `05` (inputs L001-L004, L006-L010) | DERIVED | DERIVED | ranking, percentile, mu selection |
| L006 | universe_summary.json | index-union constituent counts | S&P 500 ∪ Nasdaq-100 | 515 union (503/101, 89 overlap) | count | 2026-06-21 | `build_index_universe.py` on local constituent caches | HISTORICAL | OBSERVED | eligible universe; percentile labels |
| L007 | nasdaq_screener.json | market cap + sector | 511 scored names | one call, 7,160 rows | USD / category | 2026-08-06 | `api.nasdaq.com/api/screener/stocks?tableonly=true&limit=10000&offset=0&download=true` | DELAYED | OBSERVED | universe filters; `sector_lead` slot; sector table |
| L008 | earnings_sweep.json | next earnings date | all 515 universe names | 92 CONFIRMED_CALENDAR, 423 NO_PRINT_IN_WINDOW, 58 inside 14d | date | 2026-08-06 | `api.nasdaq.com/api/calendar/earnings?date=YYYY-MM-DD` swept over 27/27 business days (retrieved_at 2026-08-06T15:25:48Z) | DELAYED | OBSERVED | 14-day earnings penalty; event-concentration flag |
| L009 | VIX_History.csv | VIX close | ^VIX | 15.81 | index level | 2026-08-05 | `cdn.cboe.com/api/global/us_indices/daily_prices/VIX_History.csv` | HISTORICAL | OBSERVED | regime classification |
| L010 | treasury_bills_2026.csv | 13-week bank discount rate | US T-bill | 3.74% | annual % | 2026-08-05 | `home.treasury.gov/.../daily-treasury-rates.csv/2026/all?type=daily_treasury_bill_rates` | HISTORICAL | OBSERVED | rf_1m in Sharpe/Sortino/Treynor/Calmar |
| L011 | run_computed_manifest.json | beta vs SPY (60d) | 511 scored names | see `05` | ratio | 2026-08-05 | formula: `cov(r, r_SPY, ddof=0) / var(r_SPY)` on 60 daily adjusted returns (input L002) | DERIVED | DERIVED | `beta` slot; Treynor; IR; sleeve feasibility |
| L012 | run_computed_manifest.json | REALIZED_VOL_30D (1-month sigma) | 24 published names + 3 ETFs | see `05` / `03` | return sd | 2026-08-05 | formula: population stdev of trailing 30 daily adjusted returns x sqrt(21) (input L002) | DERIVED | DERIVED | sigma; CI bounds; VaR/CVaR; Kelly |
| L013 | run_computed_manifest.json | 60d max drawdown | 511 scored names | see `05` | return | 2026-08-05 | formula: worst peak-to-trough over the 61 most recent adjusted closes, stored signed negative (input L002) | DERIVED | DERIVED | `dd60` slot; Calmar; tail-risk driver |
| L014 | run_computed_manifest.json | tracking error (1m) | 24 published names | see `05` | return sd | 2026-08-05 | formula: population stdev of beta-adjusted residuals vs SPY over 60 daily returns x sqrt(21) (inputs L002, L011) | DERIVED | DERIVED | Information Ratio |
| L015 | run_computed_manifest.json | downside sigma (1m) | 24 published names | see `05` | return sd | 2026-08-05 | formula: population stdev of NEGATIVE daily adjusted returns in the trailing 30 x sqrt(21) (input L002) | DERIVED | DERIVED | Sortino |
| L016 | run_computed_manifest.json | beta vs TLT (60d) | 511 scored names | see `05` | ratio | 2026-08-05 | formula: `cov(r, r_TLT, ddof=0) / var(r_TLT)` on 60 daily adjusted returns (input L002) | DERIVED | DERIVED | `rate_sens` slot |
| L017 | settlement_manifest.json | canonical rolling calibration | all models, all vintages | EQ n=643 eff_n=2; MF n=108 eff_n=1 | count/ratio | 2026-08-06 | `settlement_ledger.py --output-dir agents/equity/output --as-of 2026-08-06` | DERIVED | DERIVED | reflection §0; Track A gating |
| L018 | settlements_this_run.json | settlement prices | 48 distinct tickers | 98 settlements at the 2026-08-05 close | USD | 2026-08-05 | stockanalysis.com/api/symbol/{s\\|e}/{SYM}/history?range=5Y (input L001) | HISTORICAL | OBSERVED | realized return / alpha / direction / CI / z |
| L019 | price_verification.json | vendor identity (exchange + currency) | 27 published symbols | all US exchanges, all USD | category | 2026-08-06 | CNBC quote fields `exchange` / `currencyCode` | LIVE | OBSERVED | guards against ticker reassignment — see § Vendor identity hazard |
| L020 | run_computed_manifest.json | Fund_Z / Sent_Z | all 511 names | `UNAVAILABLE` | z-score | 2026-08-06 | no fetch path wired at universe scale (rules.md § SHADOW Diagnostic Tooling) | UNAVAILABLE | UNAVAILABLE | excluded from Adj Score; blocks evidence thresholds 2/3/4 |

## Price Sourcing Standard — grounding gate

`rules.md § Price Sourcing Standard` requires either a market-data tool or **two
independent web sources agreeing within 1%**. This run used **three** independent sources
for every published symbol.

| Field | Value |
|---|---|
| Symbols checked | 27 (24 published names + SPY/QQQ/SOXX) |
| Grounded | **27/27** |
| Independent sources per symbol | 3 (stockanalysis `c`, CNBC `previous_day_closing`, Nasdaq summary `PreviousClose`) |
| Max cross-vendor deviation | **0.0000%** |
| Confirmation re-reads required | 0 |
| Retrieved at | `2026-08-06T15:30:46Z` |

### Intraday (`REG_MKT`) vendor field semantics

The correct field differs by fire window — this is the third distinct rule set and getting
it wrong manufactures fake 1–8% disagreements:

| Vendor | Field carrying the **completed 2026-08-05 close** | Field carrying the **live tape** |
|---|---|---|
| CNBC | `previous_day_closing` | `last` (with `last_time` on 2026-08-06) |
| Nasdaq | summary `PreviousClose` | `primaryData.lastSalePrice` |
| stockanalysis | last bar `c` | not published intraday |

All 27 symbols returned `curmktstatus = REG_MKT`, confirming the session was open and the
intraday rule set applies.

### Vendor identity hazard — `EA` (new this run)

`EA` was fetched successfully and would have looked healthy on a naive check. It is
**delisted**:

| Probe | Result |
|---|---|
| stockanalysis last bar | `2026-08-04` (every other symbol: `2026-08-05`), 47,159,176 shares — ~11x its recent daily volume — in a 0.50-wide range around 209.70 |
| Nasdaq `quote/EA/info` | `rCode 400`, `"Symbol not exists."` |
| CNBC `EA` | resolves to **Energy Absolute PCL**, Stock Exchange of Thailand, **2.88 THB** |

The tape signature (volume spike into a pinned price) is a completed acquisition; the US
listing then ceased. **The hazard is CNBC's**: the released ticker now points at an
unrelated foreign company in a different currency, so a cross-vendor check that trusted
the symbol string would have compared 209.70 USD against 2.88 THB. `EA` is excluded under
`rules.md § Exclusion` ("halted or pending delisting securities"). Ledger row L019 records
the exchange/currency identity check that catches this class; it is this run's proposed
Track B change.

## Corporate-action basis check

Per Track B 2026-07-26 the run computes **all** return/indicator math on adjusted closes
and prices entries on raw closes. Scanning last-bar `c` vs `a` across all
519 fetched symbols found **1** carrying an ex-dividend
adjustment on the basis bar: `DHI`. None is in
the published set, so no published entry price is affected.

## Coverage summary and status eligibility

| Check | Result |
|---|---|
| Required inputs grounded | **5 of 5** |
| Published entry prices grounded | 27/27 |
| Universe earnings grounded | 515/515 (sweep complete) |
| Families available for scoring | 2 of 4 (`Tech_Z`, `Macro_Z`) |
| Families UNAVAILABLE | 2 of 4 (`Fund_Z`, `Sent_Z`) |
| Data quality multiplier | 0.80 |
| Status eligibility | `GO` **blocked by evidence thresholds 2/3/4**, not by any Required input |
