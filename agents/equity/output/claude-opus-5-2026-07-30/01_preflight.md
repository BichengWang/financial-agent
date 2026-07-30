# 01 — Preflight & Source Ledger — 2026-07-30

Run `claude-opus-5-2026-07-30` · basis close **2026-07-29** · fired 2026-07-30T10:06:00-04:00 (intraday, pre-close).
Every fact used downstream appears below or is explicitly `UNAVAILABLE`.

## Retrieval summary

| Source | Role | Result |
|---|---|---|
| `stockanalysis.com/api/symbol/{s\|e}/{SYM}/history?range=5Y` | Bulk 5y daily bars (primary) | 519/519 symbols, all last bars `2026-07-29` |
| `quote.cnbc.com/.../restQuote` | Independent close verification | `curmktstatus=REG_MKT`; `previous_day_closing` = last completed close |
| IBKR MCP `get_price_snapshot` | Market-data-tool cross-check | SPY/QQQ/SOXX exact to the cent (`prior-close` empty during RTH → `last − change`) |
| `api.nasdaq.com/api/calendar/earnings` | Forward earnings sweep | 27/27 business days, complete |
| `api.nasdaq.com/api/analyst/{sym}/earnings-date` | Sweep cross-validation | 7 agree, 0 disagree, 18 vendor-empty |
| `api.nasdaq.com/api/screener/stocks` | Market cap + GICS sector | 7,077 rows |
| `cdn.cboe.com/.../VIX_History.csv` | VIX regime input | close 20.66 on 2026-07-29 |
| `home.treasury.gov/.../daily_treasury_bill_rates` | Risk-free rate | 13-week bank discount 3.70% |

### Price Sourcing Standard compliance

Every `entry_price` and every settlement price satisfies the two-independent-source rule:

- **Published set (24 names):** 30/30 agree within 0.1% between
  stockanalysis.com and CNBC. Largest disagreement
  0.0000%.
- **Settlement set (47 names):** 47/47 agree within 0.1%. Largest
  disagreement 0.0000%.
- **Core ETFs:** a third source (IBKR) matches both to the cent — SPY 729.46,
  QQQ 661.73, SOXX 465.00.

No confirmation re-read pass was required this run (no name disagreed by more than 0.1%).

### Corporate-action basis check

Return and indicator math uses the **adjusted** close (`a`); entry, target and CI prices use the
**raw** close (`c`) — Track B accepted 2026-07-26. Scanning last-bar `c` vs `a` across the
universe found **3** name(s) with an
ex-dividend adjustment on the 2026-07-29 bar
(CAG, CFG, STZ).
None are in the published set.

## Source Ledger — global rows

| artifact | field | ticker/entity | value | unit | observation_date | source | freshness_tag | claim_type | used_by |
|---|---|---|---|---|---|---|---|---|---|
| L001 | index_union_universe | UNIVERSE | 515 | tickers | 2026-07-30 | build_index_universe.py + local constituent caches | HISTORICAL | DERIVED | 03,04,05 |
| L002 | sp500_cache_fetched_at | UNIVERSE | 2026-06-21 | date | 2026-06-21 | agents/equity/turtle-trader/universe/sp500.json | HISTORICAL | OBSERVED | 04 |
| L003 | nasdaq100_cache_fetched_at | UNIVERSE | 2026-06-21 | date | 2026-06-21 | agents/equity/turtle-trader/universe/nasdaq100.json | HISTORICAL | OBSERVED | 04 |
| L004 | price_history_bulk | UNIVERSE+ETF | 519 symbols x 5y daily | bars | 2026-07-29 | stockanalysis.com/api/symbol/{s|e}/{SYM}/history?range=5Y | HISTORICAL | OBSERVED | 03,05,07 |
| L005 | vix_close | ^VIX | 20.66 | index | 2026-07-29 | cdn.cboe.com/api/global/us_indices/daily_prices/VIX_History.csv | HISTORICAL | OBSERVED | 03 |
| L006 | vix_prior_close | ^VIX | 18.21 | index | 2026-07-28 | cdn.cboe.com VIX_History.csv | HISTORICAL | OBSERVED | 03 |
| L007 | risk_free_13w | US T-BILL | 3.70 | % annual | 2026-07-29 | home.treasury.gov daily_treasury_bill_rates CSV | HISTORICAL | OBSERVED | 05,07 |
| L008 | rf_1m | US T-BILL | 0.3083 | % monthly | 2026-07-29 | DERIVED = rf_annual / 12 (L-RF) | HISTORICAL | DERIVED | 05 |
| L009 | earnings_calendar_sweep | UNIVERSE | 27/27 days, 3487 symbols | count | 2026-07-30 | api.nasdaq.com/api/calendar/earnings?date=YYYY-MM-DD | LIVE | OBSERVED | 05 |
| L010 | market_cap_sector | UNIVERSE | 7,077 rows | records | 2026-07-30 | api.nasdaq.com/api/screener/stocks | LIVE | OBSERVED | 04,05,07 |
| L011 | etf_close | SPY | 729.46 | USD | 2026-07-29 | stockanalysis.com + CNBC previous_day_closing + IBKR (last - change) | HISTORICAL | OBSERVED | 03,05,07 |
| L012 | etf_beta_60d | SPY | 1.0000 | ratio | 2026-07-29 | DERIVED = OLS slope of daily returns vs SPY over 60 sessions | HISTORICAL | DERIVED | 03 |
| L013 | etf_rvol_30d | SPY | 3.57 | % 1m | 2026-07-29 | DERIVED = stdev(30d daily returns) * sqrt(21) | HISTORICAL | DERIVED | 03 |
| L014 | etf_close | QQQ | 661.73 | USD | 2026-07-29 | stockanalysis.com + CNBC previous_day_closing + IBKR (last - change) | HISTORICAL | OBSERVED | 03,05,07 |
| L015 | etf_beta_60d | QQQ | 1.7022 | ratio | 2026-07-29 | DERIVED = OLS slope of daily returns vs SPY over 60 sessions | HISTORICAL | DERIVED | 03 |
| L016 | etf_rvol_30d | QQQ | 6.96 | % 1m | 2026-07-29 | DERIVED = stdev(30d daily returns) * sqrt(21) | HISTORICAL | DERIVED | 03 |
| L017 | etf_close | SOXX | 465.00 | USD | 2026-07-29 | stockanalysis.com + CNBC previous_day_closing + IBKR (last - change) | HISTORICAL | OBSERVED | 03,05,07 |
| L018 | etf_beta_60d | SOXX | 3.6391 | ratio | 2026-07-29 | DERIVED = OLS slope of daily returns vs SPY over 60 sessions | HISTORICAL | DERIVED | 03 |
| L019 | etf_rvol_30d | SOXX | 18.86 | % 1m | 2026-07-29 | DERIVED = stdev(30d daily returns) * sqrt(21) | HISTORICAL | DERIVED | 03 |
| L020 | tlt_close | TLT | 82.85 | USD | 2026-07-29 | stockanalysis.com + CNBC | HISTORICAL | OBSERVED | 05 |
| L021 | spy_ma20 | SPY | 745.79 | USD | 2026-07-29 | DERIVED = mean(adjusted close, 20 sessions) | HISTORICAL | DERIVED | 03 |
| L022 | spy_ma50 | SPY | 743.83 | USD | 2026-07-29 | DERIVED = mean(adjusted close, 50 sessions) | HISTORICAL | DERIVED | 03 |
| L023 | spy_rvol_30d | SPY | 3.57 | % 1m | 2026-07-29 | DERIVED = stdev(30d returns) * sqrt(21) | HISTORICAL | DERIVED | 03 |
| L024 | spy_drawdown_60d | SPY | -4.49 | % | 2026-07-29 | DERIVED = close / max(close, 60 sessions) - 1 | HISTORICAL | DERIVED | 03 |

## Source Ledger — per-name rows (published set)

| artifact | field | ticker/entity | value | unit | observation_date | source | freshness_tag | claim_type | used_by |
|---|---|---|---|---|---|---|---|---|---|
| L-PX-GRMN | entry_price | GRMN | 294.83 | USD | 2026-07-29 | stockanalysis.com history + CNBC `previous_day_closing` (agree 0.0000%) | HISTORICAL | OBSERVED | 05,06,07,15 |
| L-TI-GRMN | technical_pack | GRMN | TD9 S3/S5/S1; RSI 80.0/71.0/68.7; MACD ABOVE/BULL_X/BULL_X; MA BULL/BULL/BULL | state | 2026-07-29 | `technical_indicators.json` ← `technical_indicators.py` on fetched adjusted bars (L-PX-GRMN) | HISTORICAL | DERIVED | 05,06 |
| L-RM-GRMN | risk_metrics | GRMN | beta60 +0.1610; sigma 15.47%; downside_vol 4.17%; maxDD60 -7.03%; TE 12.40% | ratio/% | 2026-07-29 | DERIVED from L-PX-GRMN + SPY returns per `rules.md § Computed Risk Analytics` | HISTORICAL | DERIVED | 05,07 |
| L-ER-GRMN | next_earnings_date | GRMN | >2026-07-30+37d (NO_PRINT_IN_WINDOW) | date | 2026-07-30 | api.nasdaq.com forward calendar sweep | LIVE | OBSERVED | 05,07,08 |
| L-PX-BBY | entry_price | BBY | 90.17 | USD | 2026-07-29 | stockanalysis.com history + CNBC `previous_day_closing` (agree 0.0000%) | HISTORICAL | OBSERVED | 05,06,07,15 |
| L-TI-BBY | technical_pack | BBY | TD9 S4/S9/S3; RSI 73.6/69.4/61.8; MACD ABOVE/ABOVE/ABOVE; MA BULL/BULL/BULL | state | 2026-07-29 | `technical_indicators.json` ← `technical_indicators.py` on fetched adjusted bars (L-PX-BBY) | HISTORICAL | DERIVED | 05,06 |
| L-RM-BBY | risk_metrics | BBY | beta60 +0.7504; sigma 8.88%; downside_vol 5.26%; maxDD60 -8.93%; TE 12.84% | ratio/% | 2026-07-29 | DERIVED from L-PX-BBY + SPY returns per `rules.md § Computed Risk Analytics` | HISTORICAL | DERIVED | 05,07 |
| L-ER-BBY | next_earnings_date | BBY | 2026-08-27 (CONFIRMED_CALENDAR) | date | 2026-07-30 | api.nasdaq.com forward calendar sweep | LIVE | OBSERVED | 05,07,08 |
| L-PX-IQV | entry_price | IQV | 247.56 | USD | 2026-07-29 | stockanalysis.com history + CNBC `previous_day_closing` (agree 0.0000%) | HISTORICAL | OBSERVED | 05,06,07,15 |
| L-TI-IQV | technical_pack | IQV | TD9 S5/S6/S2; RSI 80.8/70.0/59.6; MACD ABOVE/ABOVE/BULL_X; MA BULL/UNAVAIL/UNAVAIL | state | 2026-07-29 | `technical_indicators.json` ← `technical_indicators.py` on fetched adjusted bars (L-PX-IQV) | HISTORICAL | DERIVED | 05,06 |
| L-RM-IQV | risk_metrics | IQV | beta60 +0.1521; sigma 15.86%; downside_vol 5.88%; maxDD60 -10.23%; TE 14.76% | ratio/% | 2026-07-29 | DERIVED from L-PX-IQV + SPY returns per `rules.md § Computed Risk Analytics` | HISTORICAL | DERIVED | 05,07 |
| L-ER-IQV | next_earnings_date | IQV | >2026-07-30+37d (NO_PRINT_IN_WINDOW) | date | 2026-07-30 | api.nasdaq.com forward calendar sweep | LIVE | OBSERVED | 05,07,08 |
| L-PX-NTAP | entry_price | NTAP | 173.23 | USD | 2026-07-29 | stockanalysis.com history + CNBC `previous_day_closing` (agree 0.0000%) | HISTORICAL | OBSERVED | 05,06,07,15 |
| L-TI-NTAP | technical_pack | NTAP | TD9 S7/S4/S4; RSI 60.6/71.4/69.8; MACD ABOVE/ABOVE/ABOVE; MA BULL/BULL/BULL | state | 2026-07-29 | `technical_indicators.json` ← `technical_indicators.py` on fetched adjusted bars (L-PX-NTAP) | HISTORICAL | DERIVED | 05,06 |
| L-RM-NTAP | risk_metrics | NTAP | beta60 +1.4199; sigma 12.82%; downside_vol 7.92%; maxDD60 -15.81%; TE 18.09% | ratio/% | 2026-07-29 | DERIVED from L-PX-NTAP + SPY returns per `rules.md § Computed Risk Analytics` | HISTORICAL | DERIVED | 05,07 |
| L-ER-NTAP | next_earnings_date | NTAP | 2026-08-26 (CONFIRMED_CALENDAR) | date | 2026-07-30 | api.nasdaq.com forward calendar sweep | LIVE | OBSERVED | 05,07,08 |
| L-PX-BXP | entry_price | BXP | 72.97 | USD | 2026-07-29 | stockanalysis.com history + CNBC `previous_day_closing` (agree 0.0000%) | HISTORICAL | OBSERVED | 05,06,07,15 |
| L-TI-BXP | technical_pack | BXP | TD9 S4/S9/S2; RSI 70.3/67.9/58.2; MACD BULL_X/ABOVE/BULL_X; MA BULL/UNAVAIL/BULL | state | 2026-07-29 | `technical_indicators.json` ← `technical_indicators.py` on fetched adjusted bars (L-PX-BXP) | HISTORICAL | DERIVED | 05,06 |
| L-RM-BXP | risk_metrics | BXP | beta60 +0.3475; sigma 8.51%; downside_vol 5.78%; maxDD60 -5.33%; TE 7.63% | ratio/% | 2026-07-29 | DERIVED from L-PX-BXP + SPY returns per `rules.md § Computed Risk Analytics` | HISTORICAL | DERIVED | 05,07 |
| L-ER-BXP | next_earnings_date | BXP | >2026-07-30+37d (NO_PRINT_IN_WINDOW) | date | 2026-07-30 | api.nasdaq.com forward calendar sweep | LIVE | OBSERVED | 05,07,08 |
| L-PX-TRV | entry_price | TRV | 389.01 | USD | 2026-07-29 | stockanalysis.com history + CNBC `previous_day_closing` (agree 0.0000%) | HISTORICAL | OBSERVED | 05,06,07,15 |
| L-TI-TRV | technical_pack | TRV | TD9 S9/S9/S9; RSI 74.7/80.0/77.4; MACD ABOVE/ABOVE/ABOVE; MA BULL/BULL/BULL | state | 2026-07-29 | `technical_indicators.json` ← `technical_indicators.py` on fetched adjusted bars (L-PX-TRV) | HISTORICAL | DERIVED | 05,06 |
| L-RM-TRV | risk_metrics | TRV | beta60 -0.5904; sigma 9.65%; downside_vol 3.55%; maxDD60 -5.96%; TE 7.62% | ratio/% | 2026-07-29 | DERIVED from L-PX-TRV + SPY returns per `rules.md § Computed Risk Analytics` | HISTORICAL | DERIVED | 05,07 |
| L-ER-TRV | next_earnings_date | TRV | >2026-07-30+37d (NO_PRINT_IN_WINDOW) | date | 2026-07-30 | api.nasdaq.com forward calendar sweep | LIVE | OBSERVED | 05,07,08 |
| L-PX-INCY | entry_price | INCY | 127.10 | USD | 2026-07-29 | stockanalysis.com history + CNBC `previous_day_closing` (agree 0.0000%) | HISTORICAL | OBSERVED | 05,06,07,15 |
| L-TI-INCY | technical_pack | INCY | TD9 S4/S9/S2; RSI 69.9/71.3/76.5; MACD ABOVE/ABOVE/ABOVE; MA BULL/BULL/BULL | state | 2026-07-29 | `technical_indicators.json` ← `technical_indicators.py` on fetched adjusted bars (L-PX-INCY) | HISTORICAL | DERIVED | 05,06 |
| L-RM-INCY | risk_metrics | INCY | beta60 -0.2423; sigma 11.86%; downside_vol 2.59%; maxDD60 -9.50%; TE 11.04% | ratio/% | 2026-07-29 | DERIVED from L-PX-INCY + SPY returns per `rules.md § Computed Risk Analytics` | HISTORICAL | DERIVED | 05,07 |
| L-ER-INCY | next_earnings_date | INCY | >2026-07-30+37d (NO_PRINT_IN_WINDOW) | date | 2026-07-30 | api.nasdaq.com forward calendar sweep | LIVE | OBSERVED | 05,07,08 |
| L-PX-GEHC | entry_price | GEHC | 71.90 | USD | 2026-07-29 | stockanalysis.com history + CNBC `previous_day_closing` (agree 0.0000%) | HISTORICAL | OBSERVED | 05,06,07,15 |
| L-TI-GEHC | technical_pack | GEHC | TD9 S2/S1/S1; RSI 68.8/54.3/49.2; MACD BULL_X/BULL_X/BELOW; MA BULL/UNAVAIL/UNAVAIL | state | 2026-07-29 | `technical_indicators.json` ← `technical_indicators.py` on fetched adjusted bars (L-PX-GEHC) | HISTORICAL | DERIVED | 05,06 |
| L-RM-GEHC | risk_metrics | GEHC | beta60 -0.2556; sigma 14.84%; downside_vol 6.96%; maxDD60 -8.17%; TE 11.76% | ratio/% | 2026-07-29 | DERIVED from L-PX-GEHC + SPY returns per `rules.md § Computed Risk Analytics` | HISTORICAL | DERIVED | 05,07 |
| L-ER-GEHC | next_earnings_date | GEHC | >2026-07-30+37d (NO_PRINT_IN_WINDOW) | date | 2026-07-30 | api.nasdaq.com forward calendar sweep | LIVE | OBSERVED | 05,07,08 |
| L-PX-FICO | entry_price | FICO | 1373.08 | USD | 2026-07-29 | stockanalysis.com history + CNBC `previous_day_closing` (agree 0.0000%) | HISTORICAL | OBSERVED | 05,06,07,15 |
| L-TI-FICO | technical_pack | FICO | TD9 S3/S5/S1; RSI 67.9/55.6/48.6; MACD ABOVE/ABOVE/BELOW; MA BULL/UNAVAIL/UNAVAIL | state | 2026-07-29 | `technical_indicators.json` ← `technical_indicators.py` on fetched adjusted bars (L-PX-FICO) | HISTORICAL | DERIVED | 05,06 |
| L-RM-FICO | risk_metrics | FICO | beta60 -0.0943; sigma 11.94%; downside_vol 8.12%; maxDD60 -15.85%; TE 12.60% | ratio/% | 2026-07-29 | DERIVED from L-PX-FICO + SPY returns per `rules.md § Computed Risk Analytics` | HISTORICAL | DERIVED | 05,07 |
| L-ER-FICO | next_earnings_date | FICO | >2026-07-30+37d (NO_PRINT_IN_WINDOW) | date | 2026-07-30 | api.nasdaq.com forward calendar sweep | LIVE | OBSERVED | 05,07,08 |
| L-PX-ADP | entry_price | ADP | 273.37 | USD | 2026-07-29 | stockanalysis.com history + CNBC `previous_day_closing` (agree 0.0000%) | HISTORICAL | OBSERVED | 05,06,07,15 |
| L-TI-ADP | technical_pack | ADP | TD9 S3/S6/S2; RSI 73.5/67.5/56.7; MACD ABOVE/ABOVE/BELOW; MA BULL/UNAVAIL/BULL | state | 2026-07-29 | `technical_indicators.json` ← `technical_indicators.py` on fetched adjusted bars (L-PX-ADP) | HISTORICAL | DERIVED | 05,06 |
| L-RM-ADP | risk_metrics | ADP | beta60 -0.7288; sigma 10.15%; downside_vol 4.35%; maxDD60 -7.49%; TE 9.12% | ratio/% | 2026-07-29 | DERIVED from L-PX-ADP + SPY returns per `rules.md § Computed Risk Analytics` | HISTORICAL | DERIVED | 05,07 |
| L-ER-ADP | next_earnings_date | ADP | >2026-07-30+37d (NO_PRINT_IN_WINDOW) | date | 2026-07-30 | api.nasdaq.com forward calendar sweep | LIVE | OBSERVED | 05,07,08 |
| L-PX-F | entry_price | F | 15.28 | USD | 2026-07-29 | stockanalysis.com history + CNBC `previous_day_closing` (agree 0.0000%) | HISTORICAL | OBSERVED | 05,06,07,15 |
| L-TI-F | technical_pack | F | TD9 S4/S3/S1; RSI 66.3/59.5/60.0; MACD ABOVE/ABOVE/ABOVE; MA UNAVAIL/BULL/BULL | state | 2026-07-29 | `technical_indicators.json` ← `technical_indicators.py` on fetched adjusted bars (L-PX-F) | HISTORICAL | DERIVED | 05,06 |
| L-RM-F | risk_metrics | F | beta60 +1.7300; sigma 7.95%; downside_vol 3.55%; maxDD60 -23.39%; TE 13.45% | ratio/% | 2026-07-29 | DERIVED from L-PX-F + SPY returns per `rules.md § Computed Risk Analytics` | HISTORICAL | DERIVED | 05,07 |
| L-ER-F | next_earnings_date | F | >2026-07-30+37d (NO_PRINT_IN_WINDOW) | date | 2026-07-30 | api.nasdaq.com forward calendar sweep | LIVE | OBSERVED | 05,07,08 |
| L-PX-HUM | entry_price | HUM | 365.41 | USD | 2026-07-29 | stockanalysis.com history + CNBC `previous_day_closing` (agree 0.0000%) | HISTORICAL | OBSERVED | 05,06,07,15 |
| L-TI-HUM | technical_pack | HUM | TD9 B5/B1/S3; RSI 41.5/64.3/57.8; MACD BELOW/ABOVE/ABOVE; MA UNAVAIL/BULL/UNAVAIL | state | 2026-07-29 | `technical_indicators.json` ← `technical_indicators.py` on fetched adjusted bars (L-PX-HUM) | HISTORICAL | DERIVED | 05,06 |
| L-RM-HUM | risk_metrics | HUM | beta60 +0.6202; sigma 10.98%; downside_vol 7.96%; maxDD60 -10.75%; TE 12.93% | ratio/% | 2026-07-29 | DERIVED from L-PX-HUM + SPY returns per `rules.md § Computed Risk Analytics` | HISTORICAL | DERIVED | 05,07 |
| L-ER-HUM | next_earnings_date | HUM | >2026-07-30+37d (NO_PRINT_IN_WINDOW) | date | 2026-07-30 | api.nasdaq.com forward calendar sweep | LIVE | OBSERVED | 05,07,08 |
| L-PX-CPAY | entry_price | CPAY | 392.85 | USD | 2026-07-29 | stockanalysis.com history + CNBC `previous_day_closing` (agree 0.0000%) | HISTORICAL | OBSERVED | 05,06,07,15 |
| L-TI-CPAY | technical_pack | CPAY | TD9 S4/S3/S4; RSI 69.0/64.7/61.9; MACD ABOVE/ABOVE/BULL_X; MA BULL/BULL/BULL | state | 2026-07-29 | `technical_indicators.json` ← `technical_indicators.py` on fetched adjusted bars (L-PX-CPAY) | HISTORICAL | DERIVED | 05,06 |
| L-RM-CPAY | risk_metrics | CPAY | beta60 +0.4596; sigma 9.49%; downside_vol 6.11%; maxDD60 -10.52%; TE 11.37% | ratio/% | 2026-07-29 | DERIVED from L-PX-CPAY + SPY returns per `rules.md § Computed Risk Analytics` | HISTORICAL | DERIVED | 05,07 |
| L-ER-CPAY | next_earnings_date | CPAY | 2026-08-05 (CONFIRMED_CALENDAR) | date | 2026-07-30 | api.nasdaq.com forward calendar sweep | LIVE | OBSERVED | 05,07,08 |
| L-PX-PAYX | entry_price | PAYX | 122.13 | USD | 2026-07-29 | stockanalysis.com history + CNBC `previous_day_closing` (agree 0.0000%) | HISTORICAL | OBSERVED | 05,06,07,15 |
| L-TI-PAYX | technical_pack | PAYX | TD9 S3/S9/S2; RSI 76.1/71.8/55.5; MACD ABOVE/ABOVE/BELOW; MA BULL/UNAVAIL/BULL | state | 2026-07-29 | `technical_indicators.json` ← `technical_indicators.py` on fetched adjusted bars (L-PX-PAYX) | HISTORICAL | DERIVED | 05,06 |
| L-RM-PAYX | risk_metrics | PAYX | beta60 -0.6127; sigma 9.89%; downside_vol 4.25%; maxDD60 -6.35%; TE 9.05% | ratio/% | 2026-07-29 | DERIVED from L-PX-PAYX + SPY returns per `rules.md § Computed Risk Analytics` | HISTORICAL | DERIVED | 05,07 |
| L-ER-PAYX | next_earnings_date | PAYX | >2026-07-30+37d (NO_PRINT_IN_WINDOW) | date | 2026-07-30 | api.nasdaq.com forward calendar sweep | LIVE | OBSERVED | 05,07,08 |
| L-PX-FTNT | entry_price | FTNT | 153.22 | USD | 2026-07-29 | stockanalysis.com history + CNBC `previous_day_closing` (agree 0.0000%) | HISTORICAL | OBSERVED | 05,06,07,15 |
| L-TI-FTNT | technical_pack | FTNT | TD9 S1/B1/S5; RSI 50.1/74.3/76.5; MACD BELOW/ABOVE/ABOVE; MA UNAVAIL/BULL/BULL | state | 2026-07-29 | `technical_indicators.json` ← `technical_indicators.py` on fetched adjusted bars (L-PX-FTNT) | HISTORICAL | DERIVED | 05,06 |
| L-RM-FTNT | risk_metrics | FTNT | beta60 +0.9246; sigma 10.40%; downside_vol 3.21%; maxDD60 -10.10%; TE 15.94% | ratio/% | 2026-07-29 | DERIVED from L-PX-FTNT + SPY returns per `rules.md § Computed Risk Analytics` | HISTORICAL | DERIVED | 05,07 |
| L-ER-FTNT | next_earnings_date | FTNT | >2026-07-30+37d (NO_PRINT_IN_WINDOW) | date | 2026-07-30 | api.nasdaq.com forward calendar sweep | LIVE | OBSERVED | 05,07,08 |
| L-PX-SJM | entry_price | SJM | 126.35 | USD | 2026-07-29 | stockanalysis.com history + CNBC `previous_day_closing` (agree 0.0000%) | HISTORICAL | OBSERVED | 05,06,07,15 |
| L-TI-SJM | technical_pack | SJM | TD9 S9/S3/S1; RSI 70.8/69.3/60.0; MACD ABOVE/ABOVE/ABOVE; MA BULL/BULL/UNAVAIL | state | 2026-07-29 | `technical_indicators.json` ← `technical_indicators.py` on fetched adjusted bars (L-PX-SJM) | HISTORICAL | DERIVED | 05,06 |
| L-RM-SJM | risk_metrics | SJM | beta60 -0.8211; sigma 9.92%; downside_vol 4.59%; maxDD60 -8.42%; TE 9.87% | ratio/% | 2026-07-29 | DERIVED from L-PX-SJM + SPY returns per `rules.md § Computed Risk Analytics` | HISTORICAL | DERIVED | 05,07 |
| L-ER-SJM | next_earnings_date | SJM | 2026-08-26 (CONFIRMED_CALENDAR) | date | 2026-07-30 | api.nasdaq.com forward calendar sweep | LIVE | OBSERVED | 05,07,08 |
| L-PX-MRSH | entry_price | MRSH | 197.59 | USD | 2026-07-29 | stockanalysis.com history + CNBC `previous_day_closing` (agree 0.0000%) | HISTORICAL | OBSERVED | 05,06,07,15 |
| L-TI-MRSH | technical_pack | MRSH | TD9 S3/S6/S1; RSI 74.1/65.8/53.6; MACD ABOVE/ABOVE/BELOW; MA BULL/UNAVAIL/BULL | state | 2026-07-29 | `technical_indicators.json` ← `technical_indicators.py` on fetched adjusted bars (L-PX-MRSH) | HISTORICAL | DERIVED | 05,06 |
| L-RM-MRSH | risk_metrics | MRSH | beta60 -0.9095; sigma 9.62%; downside_vol 4.38%; maxDD60 -6.28%; TE 7.70% | ratio/% | 2026-07-29 | DERIVED from L-PX-MRSH + SPY returns per `rules.md § Computed Risk Analytics` | HISTORICAL | DERIVED | 05,07 |
| L-ER-MRSH | next_earnings_date | MRSH | >2026-07-30+37d (NO_PRINT_IN_WINDOW) | date | 2026-07-30 | api.nasdaq.com forward calendar sweep | LIVE | OBSERVED | 05,07,08 |
| L-PX-BRO | entry_price | BRO | 74.87 | USD | 2026-07-29 | stockanalysis.com history + CNBC `previous_day_closing` (agree 0.0000%) | HISTORICAL | OBSERVED | 05,06,07,15 |
| L-TI-BRO | technical_pack | BRO | TD9 S3/S9/S1; RSI 70.9/59.2/46.4; MACD ABOVE/ABOVE/BELOW; MA BULL/UNAVAIL/UNAVAIL | state | 2026-07-29 | `technical_indicators.json` ← `technical_indicators.py` on fetched adjusted bars (L-PX-BRO) | HISTORICAL | DERIVED | 05,06 |
| L-RM-BRO | risk_metrics | BRO | beta60 -0.9543; sigma 11.45%; downside_vol 4.16%; maxDD60 -6.59%; TE 9.52% | ratio/% | 2026-07-29 | DERIVED from L-PX-BRO + SPY returns per `rules.md § Computed Risk Analytics` | HISTORICAL | DERIVED | 05,07 |
| L-ER-BRO | next_earnings_date | BRO | >2026-07-30+37d (NO_PRINT_IN_WINDOW) | date | 2026-07-30 | api.nasdaq.com forward calendar sweep | LIVE | OBSERVED | 05,07,08 |
| L-PX-HPQ | entry_price | HPQ | 28.41 | USD | 2026-07-29 | stockanalysis.com history + CNBC `previous_day_closing` (agree 0.0000%) | HISTORICAL | OBSERVED | 05,06,07,15 |
| L-TI-HPQ | technical_pack | HPQ | TD9 S4/S3/S3; RSI 72.8/66.3/55.9; MACD ABOVE/ABOVE/BULL_X; MA BULL/UNAVAIL/UNAVAIL | state | 2026-07-29 | `technical_indicators.json` ← `technical_indicators.py` on fetched adjusted bars (L-PX-HPQ) | HISTORICAL | DERIVED | 05,06 |
| L-RM-HPQ | risk_metrics | HPQ | beta60 +0.6196; sigma 11.63%; downside_vol 6.21%; maxDD60 -24.35%; TE 16.62% | ratio/% | 2026-07-29 | DERIVED from L-PX-HPQ + SPY returns per `rules.md § Computed Risk Analytics` | HISTORICAL | DERIVED | 05,07 |
| L-ER-HPQ | next_earnings_date | HPQ | 2026-08-26 (CONFIRMED_CALENDAR) | date | 2026-07-30 | api.nasdaq.com forward calendar sweep | LIVE | OBSERVED | 05,07,08 |
| L-PX-RTX | entry_price | RTX | 215.25 | USD | 2026-07-29 | stockanalysis.com history + CNBC `previous_day_closing` (agree 0.0000%) | HISTORICAL | OBSERVED | 05,06,07,15 |
| L-TI-RTX | technical_pack | RTX | TD9 S6/S9/S1; RSI 71.2/67.9/75.4; MACD ABOVE/ABOVE/ABOVE; MA BULL/BULL/BULL | state | 2026-07-29 | `technical_indicators.json` ← `technical_indicators.py` on fetched adjusted bars (L-PX-RTX) | HISTORICAL | DERIVED | 05,06 |
| L-RM-RTX | risk_metrics | RTX | beta60 -0.0200; sigma 9.65%; downside_vol 5.21%; maxDD60 -5.58%; TE 8.66% | ratio/% | 2026-07-29 | DERIVED from L-PX-RTX + SPY returns per `rules.md § Computed Risk Analytics` | HISTORICAL | DERIVED | 05,07 |
| L-ER-RTX | next_earnings_date | RTX | >2026-07-30+37d (NO_PRINT_IN_WINDOW) | date | 2026-07-30 | api.nasdaq.com forward calendar sweep | LIVE | OBSERVED | 05,07,08 |
| L-PX-CTAS | entry_price | CTAS | 216.53 | USD | 2026-07-29 | stockanalysis.com history + CNBC `previous_day_closing` (agree 0.0000%) | HISTORICAL | OBSERVED | 05,06,07,15 |
| L-TI-CTAS | technical_pack | CTAS | TD9 S4/S6/S1; RSI 78.1/69.4/61.1; MACD ABOVE/ABOVE/BELOW; MA BULL/UNAVAIL/BULL | state | 2026-07-29 | `technical_indicators.json` ← `technical_indicators.py` on fetched adjusted bars (L-PX-CTAS) | HISTORICAL | DERIVED | 05,06 |
| L-RM-CTAS | risk_metrics | CTAS | beta60 -0.2736; sigma 9.95%; downside_vol 4.44%; maxDD60 -7.19%; TE 8.93% | ratio/% | 2026-07-29 | DERIVED from L-PX-CTAS + SPY returns per `rules.md § Computed Risk Analytics` | HISTORICAL | DERIVED | 05,07 |
| L-ER-CTAS | next_earnings_date | CTAS | >2026-07-30+37d (NO_PRINT_IN_WINDOW) | date | 2026-07-30 | api.nasdaq.com forward calendar sweep | LIVE | OBSERVED | 05,07,08 |
| L-PX-IEX | entry_price | IEX | 229.52 | USD | 2026-07-29 | stockanalysis.com history + CNBC `previous_day_closing` (agree 0.0000%) | HISTORICAL | OBSERVED | 05,06,07,15 |
| L-TI-IEX | technical_pack | IEX | TD9 S4/S1/S9; RSI 62.9/68.8/60.8; MACD BULL_X/ABOVE/ABOVE; MA BULL/BULL/UNAVAIL | state | 2026-07-29 | `technical_indicators.json` ← `technical_indicators.py` on fetched adjusted bars (L-PX-IEX) | HISTORICAL | DERIVED | 05,06 |
| L-RM-IEX | risk_metrics | IEX | beta60 +0.5294; sigma 5.17%; downside_vol 3.04%; maxDD60 -5.98%; TE 5.29% | ratio/% | 2026-07-29 | DERIVED from L-PX-IEX + SPY returns per `rules.md § Computed Risk Analytics` | HISTORICAL | DERIVED | 05,07 |
| L-ER-IEX | next_earnings_date | IEX | >2026-07-30+37d (NO_PRINT_IN_WINDOW) | date | 2026-07-30 | api.nasdaq.com forward calendar sweep | LIVE | OBSERVED | 05,07,08 |
| L-PX-DVA | entry_price | DVA | 240.96 | USD | 2026-07-29 | stockanalysis.com history + CNBC `previous_day_closing` (agree 0.0000%) | HISTORICAL | OBSERVED | 05,06,07,15 |
| L-TI-DVA | technical_pack | DVA | TD9 S2/S8/S6; RSI 69.5/81.3/74.7; MACD BELOW/ABOVE/ABOVE; MA BULL/BULL/BULL | state | 2026-07-29 | `technical_indicators.json` ← `technical_indicators.py` on fetched adjusted bars (L-PX-DVA) | HISTORICAL | DERIVED | 05,06 |
| L-RM-DVA | risk_metrics | DVA | beta60 +0.5793; sigma 5.51%; downside_vol 2.87%; maxDD60 -6.31%; TE 15.06% | ratio/% | 2026-07-29 | DERIVED from L-PX-DVA + SPY returns per `rules.md § Computed Risk Analytics` | HISTORICAL | DERIVED | 05,07 |
| L-ER-DVA | next_earnings_date | DVA | 2026-08-04 (CONFIRMED_CALENDAR) | date | 2026-07-30 | api.nasdaq.com forward calendar sweep | LIVE | OBSERVED | 05,07,08 |
| L-PX-VRSK | entry_price | VRSK | 213.15 | USD | 2026-07-29 | stockanalysis.com history + CNBC `previous_day_closing` (agree 0.0000%) | HISTORICAL | OBSERVED | 05,06,07,15 |
| L-TI-VRSK | technical_pack | VRSK | TD9 S3/S9/S1; RSI 70.4/59.8/45.3; MACD ABOVE/ABOVE/BELOW; MA BULL/UNAVAIL/UNAVAIL | state | 2026-07-29 | `technical_indicators.json` ← `technical_indicators.py` on fetched adjusted bars (L-PX-VRSK) | HISTORICAL | DERIVED | 05,06 |
| L-RM-VRSK | risk_metrics | VRSK | beta60 -0.9481; sigma 10.60%; downside_vol 4.01%; maxDD60 -13.08%; TE 9.87% | ratio/% | 2026-07-29 | DERIVED from L-PX-VRSK + SPY returns per `rules.md § Computed Risk Analytics` | HISTORICAL | DERIVED | 05,07 |
| L-ER-VRSK | next_earnings_date | VRSK | >2026-07-30+37d (NO_PRINT_IN_WINDOW) | date | 2026-07-30 | api.nasdaq.com forward calendar sweep | LIVE | OBSERVED | 05,07,08 |

## `UNAVAILABLE` rows (material, recorded not estimated)

| field | entity | reason | effect |
|---|---|---|---|
| `Fund_Z` | all 513 scored names | No wired fundamental fetch path at universe scale; SHADOW tooling covers ≈4.7% vs the 70% bar in `rules.md § Financial Metrics and Score Attribution` | Family `UNAVAILABLE`; contributes `0.00`; blocks Evidence Threshold 2 |
| `Sent_Z` | all 513 scored names | Same — no analyst-revision / short-interest feed at universe scale | Family `UNAVAILABLE`; contributes `0.00`; blocks Evidence Threshold 2 |
| `IV30` | all names | No options feed wired | Sigma falls to chain step 2 (`REALIZED_VOL_30D`) — succeeded for every name |
| `market_cap` | BF-B | Nasdaq screener `marketCap` field empty (reproducible vendor gap, first logged 2026-07-27) | Name excluded from scoring; not estimated |
| bid-ask spread tape | all names | Not fetchable in this environment | Enhancing only — cannot block `GO` |

## Preflight verdict

Data mode **`DELAYED`**. All five Required inputs grounded. Proceed to Reflection.
