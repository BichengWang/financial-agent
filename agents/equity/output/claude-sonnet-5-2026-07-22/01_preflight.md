# 01 Preflight — Source Ledger — 2026-07-22

## Coverage Summary

- **Total ledger rows:** 313
- **claim_type:** OBSERVED 96, DERIVED 202, INFERRED 4, UNAVAILABLE 11 (0 ILLUSTRATIVE — this is a `DELAYED` live-data run, not `ILLUSTRATIVE_MODE`)
- **freshness_tag:** HISTORICAL 226 (2026-07-21 technical/history basis), DELAYED 75 (2026-07-22 official-close entry prices for new candidates/ETFs, today's 17 settlements via the `TARGET_DATE_CLOSE` mechanism, and earnings-date fetches), LIVE 1 (13-week T-bill rate, published same-day), UNAVAILABLE 11 (vendor-empty earnings dates on names that recently reported; see `§ Earnings Preflight` below)
- **Status eligibility:** all 5 Required inputs (`rules.md § Input Classification`) are grounded — see `00_run_manifest.md § GO-Gate Table`. The `NO_TRADE` final status is a factor-scoring evidence-threshold outcome, not a Source Ledger or data-integrity gap.

## Price Basis (see `00_run_manifest.md § Price Basis Disclosure` for full rationale)

- **Technical/derived-analytics basis:** 2026-07-21 (last close in the Nasdaq bulk historical fetch at run time — Nasdaq's historical endpoint lags the same-day close by design for hours after the bell).
- **Entry-price basis:** 2026-07-22 official close, fetched per-name via `api.nasdaq.com/api/quote/{sym}/info`, accepted only when `secondaryData.lastTradeTimestamp` carries the `"Closed at Jul 22, 2026 4:00 PM ET"` marker. Cross-checked for SPY against IBKR MCP `get_price_snapshot` (contract 756733): AH last 748.23 vs official close 747.48 (0.10% apart — consistent with the documented AH-tape-vs-primary-close artifact, not a data error). The same 2026-07-22 official-close basis is also used to settle today's 17 matured predictions, declared via the `TARGET_DATE_CLOSE` mechanism (`timing_flag` + timezone-aware `settled_at` ≥ 16:00 ET) accepted as a Track B change by a concurrent `gpt-5-2026-07-22` run and adopted here on rebase — see `00_run_manifest.md § Prediction Settlement Summary`.

## Earnings Preflight Scope

Earnings dates were fetched for the top-35-by-pre-penalty-score names plus the 14 reflection carry-forward tickers (48 names), then a bounded second pass (+6: MCO, WAT, USB, MTB, INCY, SNA) after post-penalty re-ranking pulled them into the top 20 — matching `agents.md`'s shortlist-scoped earnings preflight (not fetched universe-wide). A further 9 near-miss entrants (CTAS, A, EBAY, WELL, UNP, EIX, KHC, AMP, LH) remained unfetched after the bounded second pass and are excluded-with-disclosure from the published Ranked Candidate Table in `05`/`06` rather than silently published penalty-free. 11 of the 54 fetched names returned `VENDOR_EMPTY` ("Our vendor, Zacks Investment Research, hasn't provided us with the upcoming earnings report date") — these are large, closely-followed names (GOOGL, GS, GE, BAC, JPM, TRV, MMM, UNH, BNY, PAYX, SCHW, NTRS, MTB, MCO, USB) that most likely just reported this cycle (mid-July bank/industrial earnings season); per `daily-investment-run-playbook` convention, these get a `+~91d` cadence estimate from `run_date`, landing outside the 14-day penalty window, so no earnings penalty applies to them today.

## Source Ledger

| ID | artifact | field | ticker/entity | value | unit | observation_date | source | freshness_tag | claim_type | used_by |
|---|---|---|---|---|---|---|---|---|---|---|
| L0001 | universe_summary.json | sp500_count | S&P 500 | 503 | count | 2026-06-21 | turtle-trader/universe/sp500.json cache | HISTORICAL | OBSERVED | 04 |
| L0002 | universe_summary.json | nasdaq100_count | Nasdaq-100 | 101 | count | 2026-06-21 | turtle-trader/universe/nasdaq100.json cache | HISTORICAL | OBSERVED | 04 |
| L0003 | universe_summary.json | union_count | S&P500∪NDX100 | 515 | count | 2026-07-22 | build_index_universe.py output | HISTORICAL | DERIVED | 04,05 |
| L0004 | eligible_universe.txt | excluded_FDXF | FDXF | 38 bars < 60d minimum; listing age <6mo | n/a | 2026-07-21 | Nasdaq bulk historical fetch | HISTORICAL | OBSERVED | 04 |
| L0005 | 01_preflight.md | vix_close | VIX | 17.05 | index pts | 2026-07-21 | cdn.cboe.com/api/global/us_indices/daily_prices/VIX_History.csv | HISTORICAL | OBSERVED | 03 |
| L0006 | 01_preflight.md | vix_60d_avg | VIX | 17.34 | index pts | 2026-07-21 | derived from VIX_History.csv | HISTORICAL | DERIVED | 03 |
| L0007 | 01_preflight.md | rf_13wk_coupon_equiv | US 13-Week T-Bill | 3.84 | % annual | 2026-07-22 | home.treasury.gov daily treasury bill rates CSV | LIVE | OBSERVED | 05,06,07 |
| L0008 | 03_regime_and_data.md | close_2026-07-21 | SPY | 748.28 | USD | 2026-07-21 | Nasdaq bulk historical api.nasdaq.com/api/quote/.../historical | HISTORICAL | OBSERVED | 03,05 |
| L0009 | 03_regime_and_data.md | entry_close_2026-07-22 | SPY | 747.48 | USD | 2026-07-22 | api.nasdaq.com/api/quote/SPY/info secondaryData (official close marker) | DELAYED | OBSERVED | 03,15 |
| L0010 | 03_regime_and_data.md | ma20 | SPY | 744.98 | USD | 2026-07-21 | derived from bulk historical closes | HISTORICAL | DERIVED | 03 |
| L0011 | 03_regime_and_data.md | ma50 | SPY | 744.88 | USD | 2026-07-21 | derived from bulk historical closes | HISTORICAL | DERIVED | 03 |
| L0012 | 03_regime_and_data.md | rvol_30d | SPY | 4.02 | % | 2026-07-21 | derived: daily-return stdev * sqrt(21) | HISTORICAL | DERIVED | 03,15 |
| L0013 | 03_regime_and_data.md | dd_60d | SPY | -1.49 | % | 2026-07-21 | derived: close/60d-high - 1 | HISTORICAL | DERIVED | 03 |
| L0014 | 03_regime_and_data.md | close_2026-07-21 | QQQ | 708.97 | USD | 2026-07-21 | Nasdaq bulk historical api.nasdaq.com/api/quote/.../historical | HISTORICAL | OBSERVED | 03,05 |
| L0015 | 03_regime_and_data.md | entry_close_2026-07-22 | QQQ | 705.35 | USD | 2026-07-22 | api.nasdaq.com/api/quote/QQQ/info secondaryData (official close marker) | DELAYED | OBSERVED | 03,15 |
| L0016 | 03_regime_and_data.md | ma20 | QQQ | 714.67 | USD | 2026-07-21 | derived from bulk historical closes | HISTORICAL | DERIVED | 03 |
| L0017 | 03_regime_and_data.md | ma50 | QQQ | 719.29 | USD | 2026-07-21 | derived from bulk historical closes | HISTORICAL | DERIVED | 03 |
| L0018 | 03_regime_and_data.md | rvol_30d | QQQ | 8.08 | % | 2026-07-21 | derived: daily-return stdev * sqrt(21) | HISTORICAL | DERIVED | 03,15 |
| L0019 | 03_regime_and_data.md | dd_60d | QQQ | -4.98 | % | 2026-07-21 | derived: close/60d-high - 1 | HISTORICAL | DERIVED | 03 |
| L0020 | 03_regime_and_data.md | beta_60d_vs_spy | QQQ | 1.742 | ratio | 2026-07-21 | derived: 60d OLS slope vs SPY daily returns | HISTORICAL | DERIVED | 03,15 |
| L0021 | 03_regime_and_data.md | rs_20d_vs_spy | QQQ | -4.45 | % | 2026-07-21 | derived: 20d return spread vs SPY | HISTORICAL | DERIVED | 03 |
| L0022 | 03_regime_and_data.md | rs_60d_vs_spy | QQQ | 3.21 | % | 2026-07-21 | derived: 60d return spread vs SPY | HISTORICAL | DERIVED | 03 |
| L0023 | 03_regime_and_data.md | close_2026-07-21 | SOXX | 552.69 | USD | 2026-07-21 | Nasdaq bulk historical api.nasdaq.com/api/quote/.../historical | HISTORICAL | OBSERVED | 03,05 |
| L0024 | 03_regime_and_data.md | entry_close_2026-07-22 | SOXX | 555.52 | USD | 2026-07-22 | api.nasdaq.com/api/quote/SOXX/info secondaryData (official close marker) | DELAYED | OBSERVED | 03,15 |
| L0025 | 03_regime_and_data.md | ma20 | SOXX | 575.27 | USD | 2026-07-21 | derived from bulk historical closes | HISTORICAL | DERIVED | 03 |
| L0026 | 03_regime_and_data.md | ma50 | SOXX | 567.92 | USD | 2026-07-21 | derived from bulk historical closes | HISTORICAL | DERIVED | 03 |
| L0027 | 03_regime_and_data.md | rvol_30d | SOXX | 20.70 | % | 2026-07-21 | derived: daily-return stdev * sqrt(21) | HISTORICAL | DERIVED | 03,15 |
| L0028 | 03_regime_and_data.md | dd_60d | SOXX | -15.62 | % | 2026-07-21 | derived: close/60d-high - 1 | HISTORICAL | DERIVED | 03 |
| L0029 | 03_regime_and_data.md | beta_60d_vs_spy | SOXX | 3.817 | ratio | 2026-07-21 | derived: 60d OLS slope vs SPY daily returns | HISTORICAL | DERIVED | 03,15 |
| L0030 | 03_regime_and_data.md | rs_20d_vs_spy | SOXX | -16.14 | % | 2026-07-21 | derived: 20d return spread vs SPY | HISTORICAL | DERIVED | 03 |
| L0031 | 03_regime_and_data.md | rs_60d_vs_spy | SOXX | 19.70 | % | 2026-07-21 | derived: 60d return spread vs SPY | HISTORICAL | DERIVED | 03 |
| L0032 | 02_reflection.md | settlement_entry_price | CAT | 994.45 | USD | 2026-06-24 | gpt-5-2026-06-24/15_predictions.json | HISTORICAL | OBSERVED | 02 |
| L0033 | 02_reflection.md | settlement_settle_price | CAT | 889.38 | USD | 2026-07-22 | api.nasdaq.com/api/quote/CAT/info secondaryData (official close marker; TARGET_DATE_CLOSE) | DELAYED | OBSERVED | 02 |
| L0034 | 02_reflection.md | settlement_benchmark_price_spy | CAT | 747.48 | USD | 2026-07-22 | api.nasdaq.com/api/quote/SPY/info secondaryData (official close marker) | DELAYED | OBSERVED | 02 |
| L0035 | 02_reflection.md | settlement_entry_price | GOOGL | 345.29 | USD | 2026-06-24 | gpt-5-2026-06-24/15_predictions.json | HISTORICAL | OBSERVED | 02 |
| L0036 | 02_reflection.md | settlement_settle_price | GOOGL | 342.09 | USD | 2026-07-22 | api.nasdaq.com/api/quote/GOOGL/info secondaryData (official close marker; TARGET_DATE_CLOSE) | DELAYED | OBSERVED | 02 |
| L0037 | 02_reflection.md | settlement_benchmark_price_spy | GOOGL | 747.48 | USD | 2026-07-22 | api.nasdaq.com/api/quote/SPY/info secondaryData (official close marker) | DELAYED | OBSERVED | 02 |
| L0038 | 02_reflection.md | settlement_entry_price | GE | 365.88 | USD | 2026-06-24 | gpt-5-2026-06-24/15_predictions.json | HISTORICAL | OBSERVED | 02 |
| L0039 | 02_reflection.md | settlement_settle_price | GE | 341.23 | USD | 2026-07-22 | api.nasdaq.com/api/quote/GE/info secondaryData (official close marker; TARGET_DATE_CLOSE) | DELAYED | OBSERVED | 02 |
| L0040 | 02_reflection.md | settlement_benchmark_price_spy | GE | 747.48 | USD | 2026-07-22 | api.nasdaq.com/api/quote/SPY/info secondaryData (official close marker) | DELAYED | OBSERVED | 02 |
| L0041 | 02_reflection.md | settlement_entry_price | LLY | 1117.26 | USD | 2026-06-24 | gpt-5-2026-06-24/15_predictions.json | HISTORICAL | OBSERVED | 02 |
| L0042 | 02_reflection.md | settlement_settle_price | LLY | 1163.01 | USD | 2026-07-22 | api.nasdaq.com/api/quote/LLY/info secondaryData (official close marker; TARGET_DATE_CLOSE) | DELAYED | OBSERVED | 02 |
| L0043 | 02_reflection.md | settlement_benchmark_price_spy | LLY | 747.48 | USD | 2026-07-22 | api.nasdaq.com/api/quote/SPY/info secondaryData (official close marker) | DELAYED | OBSERVED | 02 |
| L0044 | 02_reflection.md | settlement_entry_price | FCX | 61.84 | USD | 2026-06-24 | gpt-5-2026-06-24/15_predictions.json | HISTORICAL | OBSERVED | 02 |
| L0045 | 02_reflection.md | settlement_settle_price | FCX | 64.99 | USD | 2026-07-22 | api.nasdaq.com/api/quote/FCX/info secondaryData (official close marker; TARGET_DATE_CLOSE) | DELAYED | OBSERVED | 02 |
| L0046 | 02_reflection.md | settlement_benchmark_price_spy | FCX | 747.48 | USD | 2026-07-22 | api.nasdaq.com/api/quote/SPY/info secondaryData (official close marker) | DELAYED | OBSERVED | 02 |
| L0047 | 02_reflection.md | settlement_entry_price | GS | 1076.91 | USD | 2026-06-24 | gpt-5-2026-06-24/15_predictions.json | HISTORICAL | OBSERVED | 02 |
| L0048 | 02_reflection.md | settlement_settle_price | GS | 1098.38 | USD | 2026-07-22 | api.nasdaq.com/api/quote/GS/info secondaryData (official close marker; TARGET_DATE_CLOSE) | DELAYED | OBSERVED | 02 |
| L0049 | 02_reflection.md | settlement_benchmark_price_spy | GS | 747.48 | USD | 2026-07-22 | api.nasdaq.com/api/quote/SPY/info secondaryData (official close marker) | DELAYED | OBSERVED | 02 |
| L0050 | 02_reflection.md | settlement_entry_price | BAC | 57.73 | USD | 2026-06-24 | gpt-5-2026-06-24/15_predictions.json | HISTORICAL | OBSERVED | 02 |
| L0051 | 02_reflection.md | settlement_settle_price | BAC | 61.655 | USD | 2026-07-22 | api.nasdaq.com/api/quote/BAC/info secondaryData (official close marker; TARGET_DATE_CLOSE) | DELAYED | OBSERVED | 02 |
| L0052 | 02_reflection.md | settlement_benchmark_price_spy | BAC | 747.48 | USD | 2026-07-22 | api.nasdaq.com/api/quote/SPY/info secondaryData (official close marker) | DELAYED | OBSERVED | 02 |
| L0053 | 02_reflection.md | settlement_entry_price | CVX | 171.45 | USD | 2026-06-24 | gpt-5-2026-06-24/15_predictions.json | HISTORICAL | OBSERVED | 02 |
| L0054 | 02_reflection.md | settlement_settle_price | CVX | 192.96 | USD | 2026-07-22 | api.nasdaq.com/api/quote/CVX/info secondaryData (official close marker; TARGET_DATE_CLOSE) | DELAYED | OBSERVED | 02 |
| L0055 | 02_reflection.md | settlement_benchmark_price_spy | CVX | 747.48 | USD | 2026-07-22 | api.nasdaq.com/api/quote/SPY/info secondaryData (official close marker) | DELAYED | OBSERVED | 02 |
| L0056 | 02_reflection.md | settlement_entry_price | UNH | 405.8 | USD | 2026-06-24 | gpt-5-2026-06-24/15_predictions.json | HISTORICAL | OBSERVED | 02 |
| L0057 | 02_reflection.md | settlement_settle_price | UNH | 431.33 | USD | 2026-07-22 | api.nasdaq.com/api/quote/UNH/info secondaryData (official close marker; TARGET_DATE_CLOSE) | DELAYED | OBSERVED | 02 |
| L0058 | 02_reflection.md | settlement_benchmark_price_spy | UNH | 747.48 | USD | 2026-07-22 | api.nasdaq.com/api/quote/SPY/info secondaryData (official close marker) | DELAYED | OBSERVED | 02 |
| L0059 | 02_reflection.md | settlement_entry_price | EQIX | 1095.0 | USD | 2026-06-24 | gpt-5-2026-06-24/15_predictions.json | HISTORICAL | OBSERVED | 02 |
| L0060 | 02_reflection.md | settlement_settle_price | EQIX | 1028.74 | USD | 2026-07-22 | api.nasdaq.com/api/quote/EQIX/info secondaryData (official close marker; TARGET_DATE_CLOSE) | DELAYED | OBSERVED | 02 |
| L0061 | 02_reflection.md | settlement_benchmark_price_spy | EQIX | 747.48 | USD | 2026-07-22 | api.nasdaq.com/api/quote/SPY/info secondaryData (official close marker) | DELAYED | OBSERVED | 02 |
| L0062 | 02_reflection.md | settlement_entry_price | JPM | 333.45 | USD | 2026-06-24 | gpt-5-2026-06-24/15_predictions.json | HISTORICAL | OBSERVED | 02 |
| L0063 | 02_reflection.md | settlement_settle_price | JPM | 348.35 | USD | 2026-07-22 | api.nasdaq.com/api/quote/JPM/info secondaryData (official close marker; TARGET_DATE_CLOSE) | DELAYED | OBSERVED | 02 |
| L0064 | 02_reflection.md | settlement_benchmark_price_spy | JPM | 747.48 | USD | 2026-07-22 | api.nasdaq.com/api/quote/SPY/info secondaryData (official close marker) | DELAYED | OBSERVED | 02 |
| L0065 | 02_reflection.md | settlement_entry_price | NVDA | 199.0 | USD | 2026-06-24 | gpt-5-2026-06-24/15_predictions.json | HISTORICAL | OBSERVED | 02 |
| L0066 | 02_reflection.md | settlement_settle_price | NVDA | 212.06 | USD | 2026-07-22 | api.nasdaq.com/api/quote/NVDA/info secondaryData (official close marker; TARGET_DATE_CLOSE) | DELAYED | OBSERVED | 02 |
| L0067 | 02_reflection.md | settlement_benchmark_price_spy | NVDA | 747.48 | USD | 2026-07-22 | api.nasdaq.com/api/quote/SPY/info secondaryData (official close marker) | DELAYED | OBSERVED | 02 |
| L0068 | 02_reflection.md | settlement_entry_price | V | 332.23 | USD | 2026-06-24 | gpt-5-2026-06-24/15_predictions.json | HISTORICAL | OBSERVED | 02 |
| L0069 | 02_reflection.md | settlement_settle_price | V | 353.47 | USD | 2026-07-22 | api.nasdaq.com/api/quote/V/info secondaryData (official close marker; TARGET_DATE_CLOSE) | DELAYED | OBSERVED | 02 |
| L0070 | 02_reflection.md | settlement_benchmark_price_spy | V | 747.48 | USD | 2026-07-22 | api.nasdaq.com/api/quote/SPY/info secondaryData (official close marker) | DELAYED | OBSERVED | 02 |
| L0071 | 02_reflection.md | settlement_entry_price | AAPL | 293.08 | USD | 2026-06-24 | gpt-5-2026-06-24/15_predictions.json | HISTORICAL | OBSERVED | 02 |
| L0072 | 02_reflection.md | settlement_settle_price | AAPL | 325.89 | USD | 2026-07-22 | api.nasdaq.com/api/quote/AAPL/info secondaryData (official close marker; TARGET_DATE_CLOSE) | DELAYED | OBSERVED | 02 |
| L0073 | 02_reflection.md | settlement_benchmark_price_spy | AAPL | 747.48 | USD | 2026-07-22 | api.nasdaq.com/api/quote/SPY/info secondaryData (official close marker) | DELAYED | OBSERVED | 02 |
| L0074 | 02_reflection.md | settlement_entry_price | SPY | 733.24 | USD | 2026-06-24 | gpt-5-2026-06-24/15_predictions.json | HISTORICAL | OBSERVED | 02 |
| L0075 | 02_reflection.md | settlement_settle_price | SPY | 747.48 | USD | 2026-07-22 | api.nasdaq.com/api/quote/SPY/info secondaryData (official close marker; TARGET_DATE_CLOSE) | DELAYED | OBSERVED | 02 |
| L0076 | 02_reflection.md | settlement_entry_price | QQQ | 710.62 | USD | 2026-06-24 | gpt-5-2026-06-24/15_predictions.json | HISTORICAL | OBSERVED | 02 |
| L0077 | 02_reflection.md | settlement_settle_price | QQQ | 705.35 | USD | 2026-07-22 | api.nasdaq.com/api/quote/QQQ/info secondaryData (official close marker; TARGET_DATE_CLOSE) | DELAYED | OBSERVED | 02 |
| L0078 | 02_reflection.md | settlement_entry_price | SOXX | 601.5 | USD | 2026-06-24 | gpt-5-2026-06-24/15_predictions.json | HISTORICAL | OBSERVED | 02 |
| L0079 | 02_reflection.md | settlement_settle_price | SOXX | 555.52 | USD | 2026-07-22 | api.nasdaq.com/api/quote/SOXX/info secondaryData (official close marker; TARGET_DATE_CLOSE) | DELAYED | OBSERVED | 02 |
| L0080 | 01_preflight.md | entry_price | BBY | 87.115 | USD | 2026-07-22 | api.nasdaq.com/api/quote/BBY/info secondaryData (official close marker) | DELAYED | OBSERVED | 05,06,07,15 |
| L0081 | 01_preflight.md | beta_60d | BBY | 0.666 | ratio | 2026-07-21 | derived: 60d OLS slope vs SPY (Nasdaq bulk historical closes) | HISTORICAL | DERIVED | 05,06,07 |
| L0082 | 01_preflight.md | sigma_30d_realized_vol | BBY | 8.28 | % | 2026-07-21 | derived: daily-return stdev(30d)*sqrt(21) | HISTORICAL | DERIVED | 05,06,07,15 |
| L0083 | 01_preflight.md | tech_z | BBY | 1.309 | z-score | 2026-07-21 | derived: winsorized cross-sectional z of mom20/60,rs20/60,volratio,ma_align | HISTORICAL | DERIVED | 05 |
| L0084 | 01_preflight.md | macro_z | BBY | 0.827 | z-score | 2026-07-21 | derived: winsorized cross-sectional z of sigma30,dd60,beta-dist-from-1 | HISTORICAL | DERIVED | 05 |
| L0085 | 01_preflight.md | td9_d_w_m | BBY | BUY_SETUP_1/SELL_SETUP_4/SELL_SETUP_3 | state | 2026-07-21 | technical_indicators.json | HISTORICAL | DERIVED | 05,06 |
| L0086 | 01_preflight.md | rsi14_d_w_m | BBY | 71.05/64.3/55.97 | 0-100 | 2026-07-21 | technical_indicators.json | HISTORICAL | DERIVED | 05,06 |
| L0087 | 01_preflight.md | macd_state_d_w_m | BBY | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | state | 2026-07-21 | technical_indicators.json | HISTORICAL | DERIVED | 05,06 |
| L0088 | 01_preflight.md | next_earnings_date | BBY | 2026-08-27 | date | 2026-07-22 | api.nasdaq.com/api/analyst/BBY/earnings-date | DELAYED | INFERRED | 05,06 |
| L0089 | 01_preflight.md | entry_price | DDOG | 245.77 | USD | 2026-07-22 | api.nasdaq.com/api/quote/DDOG/info secondaryData (official close marker) | DELAYED | OBSERVED | 05,06,07,15 |
| L0090 | 01_preflight.md | beta_60d | DDOG | 0.3 | ratio | 2026-07-21 | derived: 60d OLS slope vs SPY (Nasdaq bulk historical closes) | HISTORICAL | DERIVED | 05,06,07 |
| L0091 | 01_preflight.md | sigma_30d_realized_vol | DDOG | 12.35 | % | 2026-07-21 | derived: daily-return stdev(30d)*sqrt(21) | HISTORICAL | DERIVED | 05,06,07,15 |
| L0092 | 01_preflight.md | tech_z | DDOG | 1.596 | z-score | 2026-07-21 | derived: winsorized cross-sectional z of mom20/60,rs20/60,volratio,ma_align | HISTORICAL | DERIVED | 05 |
| L0093 | 01_preflight.md | macro_z | DDOG | -0.206 | z-score | 2026-07-21 | derived: winsorized cross-sectional z of sigma30,dd60,beta-dist-from-1 | HISTORICAL | DERIVED | 05 |
| L0094 | 01_preflight.md | td9_d_w_m | DDOG | BUY_SETUP_3/SELL_SETUP_4/SELL_SETUP_3 | state | 2026-07-21 | technical_indicators.json | HISTORICAL | DERIVED | 05,06 |
| L0095 | 01_preflight.md | rsi14_d_w_m | DDOG | 53.94/71.09/72.52 | 0-100 | 2026-07-21 | technical_indicators.json | HISTORICAL | DERIVED | 05,06 |
| L0096 | 01_preflight.md | macd_state_d_w_m | DDOG | BELOW_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | state | 2026-07-21 | technical_indicators.json | HISTORICAL | DERIVED | 05,06 |
| L0097 | 01_preflight.md | next_earnings_date | DDOG | 2026-08-06 | date | 2026-07-22 | api.nasdaq.com/api/analyst/DDOG/earnings-date | DELAYED | OBSERVED | 05,06 |
| L0098 | 01_preflight.md | entry_price | GEN | 25.58 | USD | 2026-07-22 | api.nasdaq.com/api/quote/GEN/info secondaryData (official close marker) | DELAYED | OBSERVED | 05,06,07,15 |
| L0099 | 01_preflight.md | beta_60d | GEN | 0.47 | ratio | 2026-07-21 | derived: 60d OLS slope vs SPY (Nasdaq bulk historical closes) | HISTORICAL | DERIVED | 05,06,07 |
| L0100 | 01_preflight.md | sigma_30d_realized_vol | GEN | 10.39 | % | 2026-07-21 | derived: daily-return stdev(30d)*sqrt(21) | HISTORICAL | DERIVED | 05,06,07,15 |
| L0101 | 01_preflight.md | tech_z | GEN | 1.323 | z-score | 2026-07-21 | derived: winsorized cross-sectional z of mom20/60,rs20/60,volratio,ma_align | HISTORICAL | DERIVED | 05 |
| L0102 | 01_preflight.md | macro_z | GEN | 0.199 | z-score | 2026-07-21 | derived: winsorized cross-sectional z of sigma30,dd60,beta-dist-from-1 | HISTORICAL | DERIVED | 05 |
| L0103 | 01_preflight.md | td9_d_w_m | GEN | BUY_SETUP_1/SELL_SETUP_4/SELL_SETUP_3 | state | 2026-07-21 | technical_indicators.json | HISTORICAL | DERIVED | 05,06 |
| L0104 | 01_preflight.md | rsi14_d_w_m | GEN | 54.63/56.76/52.37 | 0-100 | 2026-07-21 | technical_indicators.json | HISTORICAL | DERIVED | 05,06 |
| L0105 | 01_preflight.md | macd_state_d_w_m | GEN | BEARISH_CROSS/ABOVE_SIGNAL/BELOW_SIGNAL | state | 2026-07-21 | technical_indicators.json | HISTORICAL | DERIVED | 05,06 |
| L0106 | 01_preflight.md | next_earnings_date | GEN | 2026-08-06 | date | 2026-07-22 | api.nasdaq.com/api/analyst/GEN/earnings-date | DELAYED | OBSERVED | 05,06 |
| L0107 | 01_preflight.md | entry_price | DOC | 22.17 | USD | 2026-07-22 | api.nasdaq.com/api/quote/DOC/info secondaryData (official close marker) | DELAYED | OBSERVED | 05,06,07,15 |
| L0108 | 01_preflight.md | beta_60d | DOC | 0.596 | ratio | 2026-07-21 | derived: 60d OLS slope vs SPY (Nasdaq bulk historical closes) | HISTORICAL | DERIVED | 05,06,07 |
| L0109 | 01_preflight.md | sigma_30d_realized_vol | DOC | 7.08 | % | 2026-07-21 | derived: daily-return stdev(30d)*sqrt(21) | HISTORICAL | DERIVED | 05,06,07,15 |
| L0110 | 01_preflight.md | tech_z | DOC | 1.335 | z-score | 2026-07-21 | derived: winsorized cross-sectional z of mom20/60,rs20/60,volratio,ma_align | HISTORICAL | DERIVED | 05 |
| L0111 | 01_preflight.md | macro_z | DOC | 1.003 | z-score | 2026-07-21 | derived: winsorized cross-sectional z of sigma30,dd60,beta-dist-from-1 | HISTORICAL | DERIVED | 05 |
| L0112 | 01_preflight.md | td9_d_w_m | DOC | SELL_SETUP_5/SELL_SETUP_5/SELL_SETUP_4 | state | 2026-07-21 | technical_indicators.json | HISTORICAL | DERIVED | 05,06 |
| L0113 | 01_preflight.md | rsi14_d_w_m | DOC | 69.08/69.03/59.23 | 0-100 | 2026-07-21 | technical_indicators.json | HISTORICAL | DERIVED | 05,06 |
| L0114 | 01_preflight.md | macd_state_d_w_m | DOC | BULLISH_CROSS/ABOVE_SIGNAL/ABOVE_SIGNAL | state | 2026-07-21 | technical_indicators.json | HISTORICAL | DERIVED | 05,06 |
| L0115 | 01_preflight.md | next_earnings_date | DOC | 2026-08-04 | date | 2026-07-22 | api.nasdaq.com/api/analyst/DOC/earnings-date | DELAYED | OBSERVED | 05,06 |
| L0116 | 01_preflight.md | entry_price | DVA | 231.95 | USD | 2026-07-22 | api.nasdaq.com/api/quote/DVA/info secondaryData (official close marker) | DELAYED | OBSERVED | 05,06,07,15 |
| L0117 | 01_preflight.md | beta_60d | DVA | 0.585 | ratio | 2026-07-21 | derived: 60d OLS slope vs SPY (Nasdaq bulk historical closes) | HISTORICAL | DERIVED | 05,06,07 |
| L0118 | 01_preflight.md | sigma_30d_realized_vol | DVA | 5.91 | % | 2026-07-21 | derived: daily-return stdev(30d)*sqrt(21) | HISTORICAL | DERIVED | 05,06,07,15 |
| L0119 | 01_preflight.md | tech_z | DVA | 1.265 | z-score | 2026-07-21 | derived: winsorized cross-sectional z of mom20/60,rs20/60,volratio,ma_align | HISTORICAL | DERIVED | 05 |
| L0120 | 01_preflight.md | macro_z | DVA | 1.095 | z-score | 2026-07-21 | derived: winsorized cross-sectional z of sigma30,dd60,beta-dist-from-1 | HISTORICAL | DERIVED | 05 |
| L0121 | 01_preflight.md | td9_d_w_m | DVA | SELL_SETUP_7/SELL_SETUP_7/SELL_SETUP_6 | state | 2026-07-21 | technical_indicators.json | HISTORICAL | DERIVED | 05,06 |
| L0122 | 01_preflight.md | rsi14_d_w_m | DVA | 70.04/81.47/74.16 | 0-100 | 2026-07-21 | technical_indicators.json | HISTORICAL | DERIVED | 05,06 |
| L0123 | 01_preflight.md | macd_state_d_w_m | DVA | BELOW_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | state | 2026-07-21 | technical_indicators.json | HISTORICAL | DERIVED | 05,06 |
| L0124 | 01_preflight.md | next_earnings_date | DVA | 2026-08-04 | date | 2026-07-22 | api.nasdaq.com/api/analyst/DVA/earnings-date | DELAYED | INFERRED | 05,06 |
| L0125 | 01_preflight.md | entry_price | MMM | 170.79 | USD | 2026-07-22 | api.nasdaq.com/api/quote/MMM/info secondaryData (official close marker) | DELAYED | OBSERVED | 05,06,07,15 |
| L0126 | 01_preflight.md | beta_60d | MMM | 0.41 | ratio | 2026-07-21 | derived: 60d OLS slope vs SPY (Nasdaq bulk historical closes) | HISTORICAL | DERIVED | 05,06,07 |
| L0127 | 01_preflight.md | sigma_30d_realized_vol | MMM | 8.37 | % | 2026-07-21 | derived: daily-return stdev(30d)*sqrt(21) | HISTORICAL | DERIVED | 05,06,07,15 |
| L0128 | 01_preflight.md | tech_z | MMM | 1.033 | z-score | 2026-07-21 | derived: winsorized cross-sectional z of mom20/60,rs20/60,volratio,ma_align | HISTORICAL | DERIVED | 05 |
| L0129 | 01_preflight.md | macro_z | MMM | 0.72 | z-score | 2026-07-21 | derived: winsorized cross-sectional z of sigma30,dd60,beta-dist-from-1 | HISTORICAL | DERIVED | 05 |
| L0130 | 01_preflight.md | td9_d_w_m | MMM | SELL_SETUP_6/SELL_SETUP_1/SELL_SETUP_1 | state | 2026-07-21 | technical_indicators.json | HISTORICAL | DERIVED | 05,06 |
| L0131 | 01_preflight.md | rsi14_d_w_m | MMM | 68.5/62.48/61.47 | 0-100 | 2026-07-21 | technical_indicators.json | HISTORICAL | DERIVED | 05,06 |
| L0132 | 01_preflight.md | macd_state_d_w_m | MMM | BULLISH_CROSS/ABOVE_SIGNAL/BELOW_SIGNAL | state | 2026-07-21 | technical_indicators.json | HISTORICAL | DERIVED | 05,06 |
| L0133 | 01_preflight.md | next_earnings_date | MMM | VENDOR_EMPTY (recent print, +~91d cadence, outside 14d window) | n/a | 2026-07-22 | api.nasdaq.com/api/analyst/MMM/earnings-date | UNAVAILABLE | UNAVAILABLE | 05,06 |
| L0134 | 01_preflight.md | entry_price | TRV | 372.06 | USD | 2026-07-22 | api.nasdaq.com/api/quote/TRV/info secondaryData (official close marker) | DELAYED | OBSERVED | 05,06,07,15 |
| L0135 | 01_preflight.md | beta_60d | TRV | -0.74 | ratio | 2026-07-21 | derived: 60d OLS slope vs SPY (Nasdaq bulk historical closes) | HISTORICAL | DERIVED | 05,06,07 |
| L0136 | 01_preflight.md | sigma_30d_realized_vol | TRV | 9.48 | % | 2026-07-21 | derived: daily-return stdev(30d)*sqrt(21) | HISTORICAL | DERIVED | 05,06,07,15 |
| L0137 | 01_preflight.md | tech_z | TRV | 1.357 | z-score | 2026-07-21 | derived: winsorized cross-sectional z of mom20/60,rs20/60,volratio,ma_align | HISTORICAL | DERIVED | 05 |
| L0138 | 01_preflight.md | macro_z | TRV | 0.031 | z-score | 2026-07-21 | derived: winsorized cross-sectional z of sigma30,dd60,beta-dist-from-1 | HISTORICAL | DERIVED | 05 |
| L0139 | 01_preflight.md | td9_d_w_m | TRV | SELL_SETUP_3/SELL_SETUP_8/SELL_SETUP_4 | state | 2026-07-21 | technical_indicators.json | HISTORICAL | DERIVED | 05,06 |
| L0140 | 01_preflight.md | rsi14_d_w_m | TRV | 75.41/76.2/74.02 | 0-100 | 2026-07-21 | technical_indicators.json | HISTORICAL | DERIVED | 05,06 |
| L0141 | 01_preflight.md | macd_state_d_w_m | TRV | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | state | 2026-07-21 | technical_indicators.json | HISTORICAL | DERIVED | 05,06 |
| L0142 | 01_preflight.md | next_earnings_date | TRV | VENDOR_EMPTY (recent print, +~91d cadence, outside 14d window) | n/a | 2026-07-22 | api.nasdaq.com/api/analyst/TRV/earnings-date | UNAVAILABLE | UNAVAILABLE | 05,06 |
| L0143 | 01_preflight.md | entry_price | CRWD | 188.42 | USD | 2026-07-22 | api.nasdaq.com/api/quote/CRWD/info secondaryData (official close marker) | DELAYED | OBSERVED | 05,06,07,15 |
| L0144 | 01_preflight.md | beta_60d | CRWD | 1.387 | ratio | 2026-07-21 | derived: 60d OLS slope vs SPY (Nasdaq bulk historical closes) | HISTORICAL | DERIVED | 05,06,07 |
| L0145 | 01_preflight.md | sigma_30d_realized_vol | CRWD | 15.92 | % | 2026-07-21 | derived: daily-return stdev(30d)*sqrt(21) | HISTORICAL | DERIVED | 05,06,07,15 |
| L0146 | 01_preflight.md | tech_z | CRWD | 1.469 | z-score | 2026-07-21 | derived: winsorized cross-sectional z of mom20/60,rs20/60,volratio,ma_align | HISTORICAL | DERIVED | 05 |
| L0147 | 01_preflight.md | macro_z | CRWD | -0.215 | z-score | 2026-07-21 | derived: winsorized cross-sectional z of sigma30,dd60,beta-dist-from-1 | HISTORICAL | DERIVED | 05 |
| L0148 | 01_preflight.md | td9_d_w_m | CRWD | BUY_SETUP_2/SELL_SETUP_4/SELL_SETUP_3 | state | 2026-07-21 | technical_indicators.json | HISTORICAL | DERIVED | 05,06 |
| L0149 | 01_preflight.md | rsi14_d_w_m | CRWD | 52.91/67.07/72.45 | 0-100 | 2026-07-21 | technical_indicators.json | HISTORICAL | DERIVED | 05,06 |
| L0150 | 01_preflight.md | macd_state_d_w_m | CRWD | BELOW_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | state | 2026-07-21 | technical_indicators.json | HISTORICAL | DERIVED | 05,06 |
| L0151 | 01_preflight.md | next_earnings_date | CRWD | 2026-08-26 | date | 2026-07-22 | api.nasdaq.com/api/analyst/CRWD/earnings-date | DELAYED | INFERRED | 05,06 |
| L0152 | 01_preflight.md | entry_price | PANW | 335.28 | USD | 2026-07-22 | api.nasdaq.com/api/quote/PANW/info secondaryData (official close marker) | DELAYED | OBSERVED | 05,06,07,15 |
| L0153 | 01_preflight.md | beta_60d | PANW | 1.486 | ratio | 2026-07-21 | derived: 60d OLS slope vs SPY (Nasdaq bulk historical closes) | HISTORICAL | DERIVED | 05,06,07 |
| L0154 | 01_preflight.md | sigma_30d_realized_vol | PANW | 15.68 | % | 2026-07-21 | derived: daily-return stdev(30d)*sqrt(21) | HISTORICAL | DERIVED | 05,06,07,15 |
| L0155 | 01_preflight.md | tech_z | PANW | 1.574 | z-score | 2026-07-21 | derived: winsorized cross-sectional z of mom20/60,rs20/60,volratio,ma_align | HISTORICAL | DERIVED | 05 |
| L0156 | 01_preflight.md | macro_z | PANW | -0.075 | z-score | 2026-07-21 | derived: winsorized cross-sectional z of sigma30,dd60,beta-dist-from-1 | HISTORICAL | DERIVED | 05 |
| L0157 | 01_preflight.md | td9_d_w_m | PANW | BUY_SETUP_2/SELL_SETUP_9/SELL_SETUP_3 | state | 2026-07-21 | technical_indicators.json | HISTORICAL | DERIVED | 05,06 |
| L0158 | 01_preflight.md | rsi14_d_w_m | PANW | 58.84/71.71/75.11 | 0-100 | 2026-07-21 | technical_indicators.json | HISTORICAL | DERIVED | 05,06 |
| L0159 | 01_preflight.md | macd_state_d_w_m | PANW | BELOW_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | state | 2026-07-21 | technical_indicators.json | HISTORICAL | DERIVED | 05,06 |
| L0160 | 01_preflight.md | next_earnings_date | PANW | 2026-08-17 | date | 2026-07-22 | api.nasdaq.com/api/analyst/PANW/earnings-date | DELAYED | INFERRED | 05,06 |
| L0161 | 01_preflight.md | entry_price | VTRS | 17.01 | USD | 2026-07-22 | api.nasdaq.com/api/quote/VTRS/info secondaryData (official close marker) | DELAYED | OBSERVED | 05,06,07,15 |
| L0162 | 01_preflight.md | beta_60d | VTRS | 0.242 | ratio | 2026-07-21 | derived: 60d OLS slope vs SPY (Nasdaq bulk historical closes) | HISTORICAL | DERIVED | 05,06,07 |
| L0163 | 01_preflight.md | sigma_30d_realized_vol | VTRS | 8.77 | % | 2026-07-21 | derived: daily-return stdev(30d)*sqrt(21) | HISTORICAL | DERIVED | 05,06,07,15 |
| L0164 | 01_preflight.md | tech_z | VTRS | 1.09 | z-score | 2026-07-21 | derived: winsorized cross-sectional z of mom20/60,rs20/60,volratio,ma_align | HISTORICAL | DERIVED | 05 |
| L0165 | 01_preflight.md | macro_z | VTRS | 0.438 | z-score | 2026-07-21 | derived: winsorized cross-sectional z of sigma30,dd60,beta-dist-from-1 | HISTORICAL | DERIVED | 05 |
| L0166 | 01_preflight.md | td9_d_w_m | VTRS | SELL_SETUP_5/SELL_SETUP_2/SELL_SETUP_9 | state | 2026-07-21 | technical_indicators.json | HISTORICAL | DERIVED | 05,06 |
| L0167 | 01_preflight.md | rsi14_d_w_m | VTRS | 64.94/65.98/69.84 | 0-100 | 2026-07-21 | technical_indicators.json | HISTORICAL | DERIVED | 05,06 |
| L0168 | 01_preflight.md | macd_state_d_w_m | VTRS | ABOVE_SIGNAL/BULLISH_CROSS/ABOVE_SIGNAL | state | 2026-07-21 | technical_indicators.json | HISTORICAL | DERIVED | 05,06 |
| L0169 | 01_preflight.md | next_earnings_date | VTRS | 2026-08-06 | date | 2026-07-22 | api.nasdaq.com/api/analyst/VTRS/earnings-date | DELAYED | OBSERVED | 05,06 |
| L0170 | 01_preflight.md | entry_price | PAYX | 110.74 | USD | 2026-07-22 | api.nasdaq.com/api/quote/PAYX/info secondaryData (official close marker) | DELAYED | OBSERVED | 05,06,07,15 |
| L0171 | 01_preflight.md | beta_60d | PAYX | -0.717 | ratio | 2026-07-21 | derived: 60d OLS slope vs SPY (Nasdaq bulk historical closes) | HISTORICAL | DERIVED | 05,06,07 |
| L0172 | 01_preflight.md | sigma_30d_realized_vol | PAYX | 9.36 | % | 2026-07-21 | derived: daily-return stdev(30d)*sqrt(21) | HISTORICAL | DERIVED | 05,06,07,15 |
| L0173 | 01_preflight.md | tech_z | PAYX | 1.222 | z-score | 2026-07-21 | derived: winsorized cross-sectional z of mom20/60,rs20/60,volratio,ma_align | HISTORICAL | DERIVED | 05 |
| L0174 | 01_preflight.md | macro_z | PAYX | 0.072 | z-score | 2026-07-21 | derived: winsorized cross-sectional z of sigma30,dd60,beta-dist-from-1 | HISTORICAL | DERIVED | 05 |
| L0175 | 01_preflight.md | td9_d_w_m | PAYX | SELL_SETUP_8/SELL_SETUP_9/SELL_SETUP_2 | state | 2026-07-21 | technical_indicators.json | HISTORICAL | DERIVED | 05,06 |
| L0176 | 01_preflight.md | rsi14_d_w_m | PAYX | 63.14/60.77/46.36 | 0-100 | 2026-07-21 | technical_indicators.json | HISTORICAL | DERIVED | 05,06 |
| L0177 | 01_preflight.md | macd_state_d_w_m | PAYX | ABOVE_SIGNAL/ABOVE_SIGNAL/BELOW_SIGNAL | state | 2026-07-21 | technical_indicators.json | HISTORICAL | DERIVED | 05,06 |
| L0178 | 01_preflight.md | next_earnings_date | PAYX | VENDOR_EMPTY (recent print, +~91d cadence, outside 14d window) | n/a | 2026-07-22 | api.nasdaq.com/api/analyst/PAYX/earnings-date | UNAVAILABLE | UNAVAILABLE | 05,06 |
| L0179 | 01_preflight.md | entry_price | SCHW | 100.8 | USD | 2026-07-22 | api.nasdaq.com/api/quote/SCHW/info secondaryData (official close marker) | DELAYED | OBSERVED | 05,06,07,15 |
| L0180 | 01_preflight.md | beta_60d | SCHW | -0.301 | ratio | 2026-07-21 | derived: 60d OLS slope vs SPY (Nasdaq bulk historical closes) | HISTORICAL | DERIVED | 05,06,07 |
| L0181 | 01_preflight.md | sigma_30d_realized_vol | SCHW | 7.85 | % | 2026-07-21 | derived: daily-return stdev(30d)*sqrt(21) | HISTORICAL | DERIVED | 05,06,07,15 |
| L0182 | 01_preflight.md | tech_z | SCHW | 1.047 | z-score | 2026-07-21 | derived: winsorized cross-sectional z of mom20/60,rs20/60,volratio,ma_align | HISTORICAL | DERIVED | 05 |
| L0183 | 01_preflight.md | macro_z | SCHW | 0.38 | z-score | 2026-07-21 | derived: winsorized cross-sectional z of sigma30,dd60,beta-dist-from-1 | HISTORICAL | DERIVED | 05 |
| L0184 | 01_preflight.md | td9_d_w_m | SCHW | BUY_SETUP_1/SELL_SETUP_8/SELL_SETUP_1 | state | 2026-07-21 | technical_indicators.json | HISTORICAL | DERIVED | 05,06 |
| L0185 | 01_preflight.md | rsi14_d_w_m | SCHW | 56.92/58.64/61.03 | 0-100 | 2026-07-21 | technical_indicators.json | HISTORICAL | DERIVED | 05,06 |
| L0186 | 01_preflight.md | macd_state_d_w_m | SCHW | BEARISH_CROSS/ABOVE_SIGNAL/BELOW_SIGNAL | state | 2026-07-21 | technical_indicators.json | HISTORICAL | DERIVED | 05,06 |
| L0187 | 01_preflight.md | next_earnings_date | SCHW | VENDOR_EMPTY (recent print, +~91d cadence, outside 14d window) | n/a | 2026-07-22 | api.nasdaq.com/api/analyst/SCHW/earnings-date | UNAVAILABLE | UNAVAILABLE | 05,06 |
| L0188 | 01_preflight.md | entry_price | CVS | 108.09 | USD | 2026-07-22 | api.nasdaq.com/api/quote/CVS/info secondaryData (official close marker) | DELAYED | OBSERVED | 05,06,07,15 |
| L0189 | 01_preflight.md | beta_60d | CVS | -0.02 | ratio | 2026-07-21 | derived: 60d OLS slope vs SPY (Nasdaq bulk historical closes) | HISTORICAL | DERIVED | 05,06,07 |
| L0190 | 01_preflight.md | sigma_30d_realized_vol | CVS | 6.31 | % | 2026-07-21 | derived: daily-return stdev(30d)*sqrt(21) | HISTORICAL | DERIVED | 05,06,07,15 |
| L0191 | 01_preflight.md | tech_z | CVS | 1.539 | z-score | 2026-07-21 | derived: winsorized cross-sectional z of mom20/60,rs20/60,volratio,ma_align | HISTORICAL | DERIVED | 05 |
| L0192 | 01_preflight.md | macro_z | CVS | 0.621 | z-score | 2026-07-21 | derived: winsorized cross-sectional z of sigma30,dd60,beta-dist-from-1 | HISTORICAL | DERIVED | 05 |
| L0193 | 01_preflight.md | td9_d_w_m | CVS | SELL_SETUP_8/SELL_SETUP_9/SELL_SETUP_4 | state | 2026-07-21 | technical_indicators.json | HISTORICAL | DERIVED | 05,06 |
| L0194 | 01_preflight.md | rsi14_d_w_m | CVS | 74.29/73.23/70.16 | 0-100 | 2026-07-21 | technical_indicators.json | HISTORICAL | DERIVED | 05,06 |
| L0195 | 01_preflight.md | macd_state_d_w_m | CVS | BULLISH_CROSS/ABOVE_SIGNAL/ABOVE_SIGNAL | state | 2026-07-21 | technical_indicators.json | HISTORICAL | DERIVED | 05,06 |
| L0196 | 01_preflight.md | next_earnings_date | CVS | 2026-08-05 | date | 2026-07-22 | api.nasdaq.com/api/analyst/CVS/earnings-date | DELAYED | OBSERVED | 05,06 |
| L0197 | 01_preflight.md | entry_price | MCO | 489.73 | USD | 2026-07-22 | api.nasdaq.com/api/quote/MCO/info secondaryData (official close marker) | DELAYED | OBSERVED | 05,06,07,15 |
| L0198 | 01_preflight.md | beta_60d | MCO | -0.042 | ratio | 2026-07-21 | derived: 60d OLS slope vs SPY (Nasdaq bulk historical closes) | HISTORICAL | DERIVED | 05,06,07 |
| L0199 | 01_preflight.md | sigma_30d_realized_vol | MCO | 9.22 | % | 2026-07-21 | derived: daily-return stdev(30d)*sqrt(21) | HISTORICAL | DERIVED | 05,06,07,15 |
| L0200 | 01_preflight.md | tech_z | MCO | 0.997 | z-score | 2026-07-21 | derived: winsorized cross-sectional z of mom20/60,rs20/60,volratio,ma_align | HISTORICAL | DERIVED | 05 |
| L0201 | 01_preflight.md | macro_z | MCO | 0.427 | z-score | 2026-07-21 | derived: winsorized cross-sectional z of sigma30,dd60,beta-dist-from-1 | HISTORICAL | DERIVED | 05 |
| L0202 | 01_preflight.md | td9_d_w_m | MCO | BUY_SETUP_1/SELL_SETUP_4/SELL_SETUP_1 | state | 2026-07-21 | technical_indicators.json | HISTORICAL | DERIVED | 05,06 |
| L0203 | 01_preflight.md | rsi14_d_w_m | MCO | 54.94/56.23/55.57 | 0-100 | 2026-07-21 | technical_indicators.json | HISTORICAL | DERIVED | 05,06 |
| L0204 | 01_preflight.md | macd_state_d_w_m | MCO | ABOVE_SIGNAL/ABOVE_SIGNAL/BELOW_SIGNAL | state | 2026-07-21 | technical_indicators.json | HISTORICAL | DERIVED | 05,06 |
| L0205 | 01_preflight.md | next_earnings_date | MCO | VENDOR_EMPTY (recent print, +~91d cadence, outside 14d window) | n/a | 2026-07-22 | api.nasdaq.com/api/analyst/MCO/earnings-date | UNAVAILABLE | UNAVAILABLE | 05,06 |
| L0206 | 01_preflight.md | entry_price | USB | 64.465 | USD | 2026-07-22 | api.nasdaq.com/api/quote/USB/info secondaryData (official close marker) | DELAYED | OBSERVED | 05,06,07,15 |
| L0207 | 01_preflight.md | beta_60d | USB | 0.18 | ratio | 2026-07-21 | derived: 60d OLS slope vs SPY (Nasdaq bulk historical closes) | HISTORICAL | DERIVED | 05,06,07 |
| L0208 | 01_preflight.md | sigma_30d_realized_vol | USB | 6.40 | % | 2026-07-21 | derived: daily-return stdev(30d)*sqrt(21) | HISTORICAL | DERIVED | 05,06,07,15 |
| L0209 | 01_preflight.md | tech_z | USB | 0.787 | z-score | 2026-07-21 | derived: winsorized cross-sectional z of mom20/60,rs20/60,volratio,ma_align | HISTORICAL | DERIVED | 05 |
| L0210 | 01_preflight.md | macro_z | USB | 0.802 | z-score | 2026-07-21 | derived: winsorized cross-sectional z of sigma30,dd60,beta-dist-from-1 | HISTORICAL | DERIVED | 05 |
| L0211 | 01_preflight.md | td9_d_w_m | USB | SELL_SETUP_6/SELL_SETUP_8/SELL_SETUP_2 | state | 2026-07-21 | technical_indicators.json | HISTORICAL | DERIVED | 05,06 |
| L0212 | 01_preflight.md | rsi14_d_w_m | USB | 65.18/69.52/67.36 | 0-100 | 2026-07-21 | technical_indicators.json | HISTORICAL | DERIVED | 05,06 |
| L0213 | 01_preflight.md | macd_state_d_w_m | USB | BELOW_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | state | 2026-07-21 | technical_indicators.json | HISTORICAL | DERIVED | 05,06 |
| L0214 | 01_preflight.md | next_earnings_date | USB | VENDOR_EMPTY (recent print, +~91d cadence, outside 14d window) | n/a | 2026-07-22 | api.nasdaq.com/api/analyst/USB/earnings-date | UNAVAILABLE | UNAVAILABLE | 05,06 |
| L0215 | 01_preflight.md | entry_price | MTB | 250.8 | USD | 2026-07-22 | api.nasdaq.com/api/quote/MTB/info secondaryData (official close marker) | DELAYED | OBSERVED | 05,06,07,15 |
| L0216 | 01_preflight.md | beta_60d | MTB | 0.198 | ratio | 2026-07-21 | derived: 60d OLS slope vs SPY (Nasdaq bulk historical closes) | HISTORICAL | DERIVED | 05,06,07 |
| L0217 | 01_preflight.md | sigma_30d_realized_vol | MTB | 6.10 | % | 2026-07-21 | derived: daily-return stdev(30d)*sqrt(21) | HISTORICAL | DERIVED | 05,06,07,15 |
| L0218 | 01_preflight.md | tech_z | MTB | 0.762 | z-score | 2026-07-21 | derived: winsorized cross-sectional z of mom20/60,rs20/60,volratio,ma_align | HISTORICAL | DERIVED | 05 |
| L0219 | 01_preflight.md | macro_z | MTB | 0.849 | z-score | 2026-07-21 | derived: winsorized cross-sectional z of sigma30,dd60,beta-dist-from-1 | HISTORICAL | DERIVED | 05 |
| L0220 | 01_preflight.md | td9_d_w_m | MTB | SELL_SETUP_8/SELL_SETUP_8/SELL_SETUP_2 | state | 2026-07-21 | technical_indicators.json | HISTORICAL | DERIVED | 05,06 |
| L0221 | 01_preflight.md | rsi14_d_w_m | MTB | 64.96/68.13/68.21 | 0-100 | 2026-07-21 | technical_indicators.json | HISTORICAL | DERIVED | 05,06 |
| L0222 | 01_preflight.md | macd_state_d_w_m | MTB | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | state | 2026-07-21 | technical_indicators.json | HISTORICAL | DERIVED | 05,06 |
| L0223 | 01_preflight.md | next_earnings_date | MTB | VENDOR_EMPTY (recent print, +~91d cadence, outside 14d window) | n/a | 2026-07-22 | api.nasdaq.com/api/analyst/MTB/earnings-date | UNAVAILABLE | UNAVAILABLE | 05,06 |
| L0224 | 01_preflight.md | entry_price | BAC | 61.655 | USD | 2026-07-22 | api.nasdaq.com/api/quote/BAC/info secondaryData (official close marker) | DELAYED | OBSERVED | 05,06,07,15 |
| L0225 | 01_preflight.md | beta_60d | BAC | 0.241 | ratio | 2026-07-21 | derived: 60d OLS slope vs SPY (Nasdaq bulk historical closes) | HISTORICAL | DERIVED | 05,06,07 |
| L0226 | 01_preflight.md | sigma_30d_realized_vol | BAC | 5.58 | % | 2026-07-21 | derived: daily-return stdev(30d)*sqrt(21) | HISTORICAL | DERIVED | 05,06,07,15 |
| L0227 | 01_preflight.md | tech_z | BAC | 0.728 | z-score | 2026-07-21 | derived: winsorized cross-sectional z of mom20/60,rs20/60,volratio,ma_align | HISTORICAL | DERIVED | 05 |
| L0228 | 01_preflight.md | macro_z | BAC | 0.882 | z-score | 2026-07-21 | derived: winsorized cross-sectional z of sigma30,dd60,beta-dist-from-1 | HISTORICAL | DERIVED | 05 |
| L0229 | 01_preflight.md | td9_d_w_m | BAC | BUY_SETUP_2/SELL_SETUP_8/SELL_SETUP_2 | state | 2026-07-21 | technical_indicators.json | HISTORICAL | DERIVED | 05,06 |
| L0230 | 01_preflight.md | rsi14_d_w_m | BAC | 66.47/69.12/69.4 | 0-100 | 2026-07-21 | technical_indicators.json | HISTORICAL | DERIVED | 05,06 |
| L0231 | 01_preflight.md | macd_state_d_w_m | BAC | BEARISH_CROSS/ABOVE_SIGNAL/ABOVE_SIGNAL | state | 2026-07-21 | technical_indicators.json | HISTORICAL | DERIVED | 05,06 |
| L0232 | 01_preflight.md | next_earnings_date | BAC | VENDOR_EMPTY (recent print, +~91d cadence, outside 14d window) | n/a | 2026-07-22 | api.nasdaq.com/api/analyst/BAC/earnings-date | UNAVAILABLE | UNAVAILABLE | 05,06 |
| L0233 | 01_preflight.md | entry_price | EXPD | 177.53 | USD | 2026-07-22 | api.nasdaq.com/api/quote/EXPD/info secondaryData (official close marker) | DELAYED | OBSERVED | 05,06,07,15 |
| L0234 | 01_preflight.md | beta_60d | EXPD | 0.287 | ratio | 2026-07-21 | derived: 60d OLS slope vs SPY (Nasdaq bulk historical closes) | HISTORICAL | DERIVED | 05,06,07 |
| L0235 | 01_preflight.md | sigma_30d_realized_vol | EXPD | 6.78 | % | 2026-07-21 | derived: daily-return stdev(30d)*sqrt(21) | HISTORICAL | DERIVED | 05,06,07,15 |
| L0236 | 01_preflight.md | tech_z | EXPD | 1.125 | z-score | 2026-07-21 | derived: winsorized cross-sectional z of mom20/60,rs20/60,volratio,ma_align | HISTORICAL | DERIVED | 05 |
| L0237 | 01_preflight.md | macro_z | EXPD | 0.862 | z-score | 2026-07-21 | derived: winsorized cross-sectional z of sigma30,dd60,beta-dist-from-1 | HISTORICAL | DERIVED | 05 |
| L0238 | 01_preflight.md | td9_d_w_m | EXPD | SELL_SETUP_1/SELL_SETUP_9/SELL_SETUP_2 | state | 2026-07-21 | technical_indicators.json | HISTORICAL | DERIVED | 05,06 |
| L0239 | 01_preflight.md | rsi14_d_w_m | EXPD | 65.59/67.88/72.07 | 0-100 | 2026-07-21 | technical_indicators.json | HISTORICAL | DERIVED | 05,06 |
| L0240 | 01_preflight.md | macd_state_d_w_m | EXPD | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | state | 2026-07-21 | technical_indicators.json | HISTORICAL | DERIVED | 05,06 |
| L0241 | 01_preflight.md | next_earnings_date | EXPD | 2026-08-04 | date | 2026-07-22 | api.nasdaq.com/api/analyst/EXPD/earnings-date | DELAYED | OBSERVED | 05,06 |
| L0242 | 01_preflight.md | entry_price | TMO | 526.71 | USD | 2026-07-22 | api.nasdaq.com/api/quote/TMO/info secondaryData (official close marker) | DELAYED | OBSERVED | 05,06,07,15 |
| L0243 | 01_preflight.md | beta_60d | TMO | 0.379 | ratio | 2026-07-21 | derived: 60d OLS slope vs SPY (Nasdaq bulk historical closes) | HISTORICAL | DERIVED | 05,06,07 |
| L0244 | 01_preflight.md | sigma_30d_realized_vol | TMO | 8.80 | % | 2026-07-21 | derived: daily-return stdev(30d)*sqrt(21) | HISTORICAL | DERIVED | 05,06,07,15 |
| L0245 | 01_preflight.md | tech_z | TMO | 1.219 | z-score | 2026-07-21 | derived: winsorized cross-sectional z of mom20/60,rs20/60,volratio,ma_align | HISTORICAL | DERIVED | 05 |
| L0246 | 01_preflight.md | macro_z | TMO | 0.642 | z-score | 2026-07-21 | derived: winsorized cross-sectional z of sigma30,dd60,beta-dist-from-1 | HISTORICAL | DERIVED | 05 |
| L0247 | 01_preflight.md | td9_d_w_m | TMO | BUY_SETUP_2/SELL_SETUP_9/SELL_SETUP_1 | state | 2026-07-21 | technical_indicators.json | HISTORICAL | DERIVED | 05,06 |
| L0248 | 01_preflight.md | rsi14_d_w_m | TMO | 57.2/54.48/50.43 | 0-100 | 2026-07-21 | technical_indicators.json | HISTORICAL | DERIVED | 05,06 |
| L0249 | 01_preflight.md | macd_state_d_w_m | TMO | BEARISH_CROSS/ABOVE_SIGNAL/BULLISH_CROSS | state | 2026-07-21 | technical_indicators.json | HISTORICAL | DERIVED | 05,06 |
| L0250 | 01_preflight.md | next_earnings_date | TMO | 2026-07-23 | date | 2026-07-22 | api.nasdaq.com/api/analyst/TMO/earnings-date | DELAYED | OBSERVED | 05,06 |
| L0251 | 01_preflight.md | entry_price | FTNT | 155.05 | USD | 2026-07-22 | api.nasdaq.com/api/quote/FTNT/info secondaryData (official close marker) | DELAYED | OBSERVED | 05,06,07,15 |
| L0252 | 01_preflight.md | beta_60d | FTNT | 0.895 | ratio | 2026-07-21 | derived: 60d OLS slope vs SPY (Nasdaq bulk historical closes) | HISTORICAL | DERIVED | 05,06,07 |
| L0253 | 01_preflight.md | sigma_30d_realized_vol | FTNT | 11.02 | % | 2026-07-21 | derived: daily-return stdev(30d)*sqrt(21) | HISTORICAL | DERIVED | 05,06,07,15 |
| L0254 | 01_preflight.md | tech_z | FTNT | 1.352 | z-score | 2026-07-21 | derived: winsorized cross-sectional z of mom20/60,rs20/60,volratio,ma_align | HISTORICAL | DERIVED | 05 |
| L0255 | 01_preflight.md | macro_z | FTNT | 0.776 | z-score | 2026-07-21 | derived: winsorized cross-sectional z of sigma30,dd60,beta-dist-from-1 | HISTORICAL | DERIVED | 05 |
| L0256 | 01_preflight.md | td9_d_w_m | FTNT | BUY_SETUP_2/SELL_SETUP_9/SELL_SETUP_5 | state | 2026-07-21 | technical_indicators.json | HISTORICAL | DERIVED | 05,06 |
| L0257 | 01_preflight.md | rsi14_d_w_m | FTNT | 55.34/80.4/77.62 | 0-100 | 2026-07-21 | technical_indicators.json | HISTORICAL | DERIVED | 05,06 |
| L0258 | 01_preflight.md | macd_state_d_w_m | FTNT | BELOW_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | state | 2026-07-21 | technical_indicators.json | HISTORICAL | DERIVED | 05,06 |
| L0259 | 01_preflight.md | next_earnings_date | FTNT | 2026-07-29 | date | 2026-07-22 | api.nasdaq.com/api/analyst/FTNT/earnings-date | DELAYED | OBSERVED | 05,06 |
| L0260 | 01_preflight.md | entry_price | UNH | 431.33 | USD | 2026-07-22 | api.nasdaq.com/api/quote/UNH/info secondaryData (official close marker) | DELAYED | OBSERVED | 05,06,07,15 |
| L0261 | 01_preflight.md | beta_60d | UNH | -0.168 | ratio | 2026-07-21 | derived: 60d OLS slope vs SPY (Nasdaq bulk historical closes) | HISTORICAL | DERIVED | 05,06,07 |
| L0262 | 01_preflight.md | sigma_30d_realized_vol | UNH | 7.29 | % | 2026-07-21 | derived: daily-return stdev(30d)*sqrt(21) | HISTORICAL | DERIVED | 05,06,07,15 |
| L0263 | 01_preflight.md | tech_z | UNH | 1.007 | z-score | 2026-07-21 | derived: winsorized cross-sectional z of mom20/60,rs20/60,volratio,ma_align | HISTORICAL | DERIVED | 05 |
| L0264 | 01_preflight.md | macro_z | UNH | 0.567 | z-score | 2026-07-21 | derived: winsorized cross-sectional z of sigma30,dd60,beta-dist-from-1 | HISTORICAL | DERIVED | 05 |
| L0265 | 01_preflight.md | td9_d_w_m | UNH | SELL_SETUP_1/SELL_SETUP_9/SELL_SETUP_4 | state | 2026-07-21 | technical_indicators.json | HISTORICAL | DERIVED | 05,06 |
| L0266 | 01_preflight.md | rsi14_d_w_m | UNH | 62.36/70.4/54.32 | 0-100 | 2026-07-21 | technical_indicators.json | HISTORICAL | DERIVED | 05,06 |
| L0267 | 01_preflight.md | macd_state_d_w_m | UNH | BELOW_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | state | 2026-07-21 | technical_indicators.json | HISTORICAL | DERIVED | 05,06 |
| L0268 | 01_preflight.md | next_earnings_date | UNH | VENDOR_EMPTY (recent print, +~91d cadence, outside 14d window) | n/a | 2026-07-22 | api.nasdaq.com/api/analyst/UNH/earnings-date | UNAVAILABLE | UNAVAILABLE | 05,06 |
| L0269 | 01_preflight.md | entry_price | JPM | 348.35 | USD | 2026-07-22 | api.nasdaq.com/api/quote/JPM/info secondaryData (official close marker) | DELAYED | OBSERVED | 05,06,07,15 |
| L0270 | 01_preflight.md | beta_60d | JPM | 0.298 | ratio | 2026-07-21 | derived: 60d OLS slope vs SPY (Nasdaq bulk historical closes) | HISTORICAL | DERIVED | 05,06,07 |
| L0271 | 01_preflight.md | sigma_30d_realized_vol | JPM | 6.68 | % | 2026-07-21 | derived: daily-return stdev(30d)*sqrt(21) | HISTORICAL | DERIVED | 05,06,07,15 |
| L0272 | 01_preflight.md | tech_z | JPM | 0.265 | z-score | 2026-07-21 | derived: winsorized cross-sectional z of mom20/60,rs20/60,volratio,ma_align | HISTORICAL | DERIVED | 05 |
| L0273 | 01_preflight.md | macro_z | JPM | 0.878 | z-score | 2026-07-21 | derived: winsorized cross-sectional z of sigma30,dd60,beta-dist-from-1 | HISTORICAL | DERIVED | 05 |
| L0274 | 01_preflight.md | td9_d_w_m | JPM | BUY_SETUP_2/SELL_SETUP_8/SELL_SETUP_2 | state | 2026-07-21 | technical_indicators.json | HISTORICAL | DERIVED | 05,06 |
| L0275 | 01_preflight.md | rsi14_d_w_m | JPM | 62.73/67.25/71.1 | 0-100 | 2026-07-21 | technical_indicators.json | HISTORICAL | DERIVED | 05,06 |
| L0276 | 01_preflight.md | macd_state_d_w_m | JPM | BELOW_SIGNAL/ABOVE_SIGNAL/BELOW_SIGNAL | state | 2026-07-21 | technical_indicators.json | HISTORICAL | DERIVED | 05,06 |
| L0277 | 01_preflight.md | next_earnings_date | JPM | VENDOR_EMPTY (recent print, +~91d cadence, outside 14d window) | n/a | 2026-07-22 | api.nasdaq.com/api/analyst/JPM/earnings-date | UNAVAILABLE | UNAVAILABLE | 05,06 |
| L0278 | 01_preflight.md | entry_price | AAPL | 325.89 | USD | 2026-07-22 | api.nasdaq.com/api/quote/AAPL/info secondaryData (official close marker) | DELAYED | OBSERVED | 05,06,07,15 |
| L0279 | 01_preflight.md | beta_60d | AAPL | 0.413 | ratio | 2026-07-21 | derived: 60d OLS slope vs SPY (Nasdaq bulk historical closes) | HISTORICAL | DERIVED | 05,06,07 |
| L0280 | 01_preflight.md | sigma_30d_realized_vol | AAPL | 9.95 | % | 2026-07-21 | derived: daily-return stdev(30d)*sqrt(21) | HISTORICAL | DERIVED | 05,06,07,15 |
| L0281 | 01_preflight.md | tech_z | AAPL | 0.757 | z-score | 2026-07-21 | derived: winsorized cross-sectional z of mom20/60,rs20/60,volratio,ma_align | HISTORICAL | DERIVED | 05 |
| L0282 | 01_preflight.md | macro_z | AAPL | 0.387 | z-score | 2026-07-21 | derived: winsorized cross-sectional z of sigma30,dd60,beta-dist-from-1 | HISTORICAL | DERIVED | 05 |
| L0283 | 01_preflight.md | td9_d_w_m | AAPL | SELL_SETUP_9/SELL_SETUP_4/SELL_SETUP_3 | state | 2026-07-21 | technical_indicators.json | HISTORICAL | DERIVED | 05,06 |
| L0284 | 01_preflight.md | rsi14_d_w_m | AAPL | 64.54/66.21/69.41 | 0-100 | 2026-07-21 | technical_indicators.json | HISTORICAL | DERIVED | 05,06 |
| L0285 | 01_preflight.md | macd_state_d_w_m | AAPL | ABOVE_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | state | 2026-07-21 | technical_indicators.json | HISTORICAL | DERIVED | 05,06 |
| L0286 | 01_preflight.md | next_earnings_date | AAPL | 2026-07-30 | date | 2026-07-22 | api.nasdaq.com/api/analyst/AAPL/earnings-date | DELAYED | OBSERVED | 05,06 |
| L0287 | 01_preflight.md | entry_price | V | 353.47 | USD | 2026-07-22 | api.nasdaq.com/api/quote/V/info secondaryData (official close marker) | DELAYED | OBSERVED | 05,06,07,15 |
| L0288 | 01_preflight.md | beta_60d | V | -0.358 | ratio | 2026-07-21 | derived: 60d OLS slope vs SPY (Nasdaq bulk historical closes) | HISTORICAL | DERIVED | 05,06,07 |
| L0289 | 01_preflight.md | sigma_30d_realized_vol | V | 6.73 | % | 2026-07-21 | derived: daily-return stdev(30d)*sqrt(21) | HISTORICAL | DERIVED | 05,06,07,15 |
| L0290 | 01_preflight.md | tech_z | V | 0.611 | z-score | 2026-07-21 | derived: winsorized cross-sectional z of mom20/60,rs20/60,volratio,ma_align | HISTORICAL | DERIVED | 05 |
| L0291 | 01_preflight.md | macro_z | V | 0.484 | z-score | 2026-07-21 | derived: winsorized cross-sectional z of sigma30,dd60,beta-dist-from-1 | HISTORICAL | DERIVED | 05 |
| L0292 | 01_preflight.md | td9_d_w_m | V | SELL_SETUP_7/SELL_SETUP_5/SELL_SETUP_3 | state | 2026-07-21 | technical_indicators.json | HISTORICAL | DERIVED | 05,06 |
| L0293 | 01_preflight.md | rsi14_d_w_m | V | 58.57/61.13/60.86 | 0-100 | 2026-07-21 | technical_indicators.json | HISTORICAL | DERIVED | 05,06 |
| L0294 | 01_preflight.md | macd_state_d_w_m | V | ABOVE_SIGNAL/ABOVE_SIGNAL/BELOW_SIGNAL | state | 2026-07-21 | technical_indicators.json | HISTORICAL | DERIVED | 05,06 |
| L0295 | 01_preflight.md | next_earnings_date | V | 2026-07-28 | date | 2026-07-22 | api.nasdaq.com/api/analyst/V/earnings-date | DELAYED | OBSERVED | 05,06 |
| L0296 | 01_preflight.md | entry_price | LLY | 1163.01 | USD | 2026-07-22 | api.nasdaq.com/api/quote/LLY/info secondaryData (official close marker) | DELAYED | OBSERVED | 05,06,07,15 |
| L0297 | 01_preflight.md | beta_60d | LLY | 0.032 | ratio | 2026-07-21 | derived: 60d OLS slope vs SPY (Nasdaq bulk historical closes) | HISTORICAL | DERIVED | 05,06,07 |
| L0298 | 01_preflight.md | sigma_30d_realized_vol | LLY | 9.40 | % | 2026-07-21 | derived: daily-return stdev(30d)*sqrt(21) | HISTORICAL | DERIVED | 05,06,07,15 |
| L0299 | 01_preflight.md | tech_z | LLY | 0.619 | z-score | 2026-07-21 | derived: winsorized cross-sectional z of mom20/60,rs20/60,volratio,ma_align | HISTORICAL | DERIVED | 05 |
| L0300 | 01_preflight.md | macro_z | LLY | 0.451 | z-score | 2026-07-21 | derived: winsorized cross-sectional z of sigma30,dd60,beta-dist-from-1 | HISTORICAL | DERIVED | 05 |
| L0301 | 01_preflight.md | td9_d_w_m | LLY | SELL_SETUP_1/BUY_SETUP_1/SELL_SETUP_3 | state | 2026-07-21 | technical_indicators.json | HISTORICAL | DERIVED | 05,06 |
| L0302 | 01_preflight.md | rsi14_d_w_m | LLY | 53.52/63.45/66.09 | 0-100 | 2026-07-21 | technical_indicators.json | HISTORICAL | DERIVED | 05,06 |
| L0303 | 01_preflight.md | macd_state_d_w_m | LLY | BELOW_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | state | 2026-07-21 | technical_indicators.json | HISTORICAL | DERIVED | 05,06 |
| L0304 | 01_preflight.md | next_earnings_date | LLY | 2026-08-05 | date | 2026-07-22 | api.nasdaq.com/api/analyst/LLY/earnings-date | DELAYED | OBSERVED | 05,06 |
| L0305 | 01_preflight.md | entry_price | GE | 341.23 | USD | 2026-07-22 | api.nasdaq.com/api/quote/GE/info secondaryData (official close marker) | DELAYED | OBSERVED | 05,06,07,15 |
| L0306 | 01_preflight.md | beta_60d | GE | 1.166 | ratio | 2026-07-21 | derived: 60d OLS slope vs SPY (Nasdaq bulk historical closes) | HISTORICAL | DERIVED | 05,06,07 |
| L0307 | 01_preflight.md | sigma_30d_realized_vol | GE | 9.17 | % | 2026-07-21 | derived: daily-return stdev(30d)*sqrt(21) | HISTORICAL | DERIVED | 05,06,07,15 |
| L0308 | 01_preflight.md | tech_z | GE | 0.1 | z-score | 2026-07-21 | derived: winsorized cross-sectional z of mom20/60,rs20/60,volratio,ma_align | HISTORICAL | DERIVED | 05 |
| L0309 | 01_preflight.md | macro_z | GE | 0.798 | z-score | 2026-07-21 | derived: winsorized cross-sectional z of sigma30,dd60,beta-dist-from-1 | HISTORICAL | DERIVED | 05 |
| L0310 | 01_preflight.md | td9_d_w_m | GE | BUY_SETUP_4/BUY_SETUP_2/SELL_SETUP_3 | state | 2026-07-21 | technical_indicators.json | HISTORICAL | DERIVED | 05,06 |
| L0311 | 01_preflight.md | rsi14_d_w_m | GE | 42.72/55.59/66.13 | 0-100 | 2026-07-21 | technical_indicators.json | HISTORICAL | DERIVED | 05,06 |
| L0312 | 01_preflight.md | macd_state_d_w_m | GE | BELOW_SIGNAL/ABOVE_SIGNAL/ABOVE_SIGNAL | state | 2026-07-21 | technical_indicators.json | HISTORICAL | DERIVED | 05,06 |
| L0313 | 01_preflight.md | next_earnings_date | GE | VENDOR_EMPTY (recent print, +~91d cadence, outside 14d window) | n/a | 2026-07-22 | api.nasdaq.com/api/analyst/GE/earnings-date | UNAVAILABLE | UNAVAILABLE | 05,06 |