# 01 — Preflight and Source Ledger — 2026-08-04

Basis **2026-08-03 completed close**. Fire window **intraday 2026-08-04T12:05:00-04:00**
(CNBC `curmktstatus` = `REG_MKT`). Every fact used downstream appears below or is `UNAVAILABLE`.

## Price Sourcing Standard — grounding result

The Price Sourcing Standard requires a connected market-data tool **or** two independent web sources
agreeing within 1%. IBKR MCP was unavailable this run (connector connection invalidated — a
documented failed fetch), so grounding rests on **three** independent web sources.

**Intraday field rule (`REG_MKT`)** — the three fire windows have three *different* correct fields,
and using the wrong one manufactures fake disagreements:

| Source | Field carrying the last COMPLETED close | Field carrying the live tape |
|---|---|---|
| stockanalysis.com | last bar `c` (dated 2026-08-03) | — (no partial same-day bar published at fire time) |
| CNBC quote | `previous_day_closing` | `last` (gated on `last_time`) |
| Nasdaq quote summary | `PreviousClose` | `primaryData.lastSalePrice` |

| Grounding metric | Result |
|---|---|
| Symbols verified (published set + core ETFs) | 28 |
| Symbols with ≥3 independent sources agreeing within 0.1% | 28 |
| Maximum cross-source deviation | **0.0000%** |
| Confirmation re-reads required | 0 |
| Ex-dividend `c != a` on the basis bar (whole universe) | 2 — LVS, MET (neither is in the published set) |

All three sources agreed **to the cent on every symbol**, so no confirmation pass was needed.

## Corporate-action basis split (Track B, 2026-07-26)

Two CSV trees are materialized from the same fetch: **adjusted close `a` drives every
return/indicator computation** (momentum, relative strength, realized/downside vol, beta, tracking
error, drawdown, and the `technical_indicators.py` input), while **raw close `c` drives every
entry, target and CI price**. `technical_indicators.py::load_csv_history` prefers the `Close`
column over `AdjClose`, so the adjusted tree writes adjusted values into `Close`.

Neither tree is committed (~72 MB, and `agents/equity/.work/` is gitignored). `L-HIST-001` records
the source URL, retrieval timestamp, per-symbol bar counts and last raw/adjusted closes, which makes
the trees regenerable.

## Source Ledger — infrastructure and macro

| artifact | field | ticker/entity | value | unit | observation_date | source | freshness_tag | claim_type | used_by |
|---|---|---|---|---|---|---|---|---|---|
| `L-UNI-001` | union_count | S&P 500 ∪ Nasdaq-100 | 515 | tickers | 2026-08-04 | `build_index_universe.py` on local constituent caches | HISTORICAL | DERIVED | `04`, percentile label |
| `L-UNI-002` | sp500_count / fetched_at | S&P 500 cache | 503 @ 2026-06-21 | tickers | 2026-06-21 | `agents/equity/turtle-trader/universe/sp500.json` | HISTORICAL | OBSERVED | `04` |
| `L-UNI-003` | nasdaq100_count / fetched_at | Nasdaq-100 cache | 101 @ 2026-06-21 | tickers | 2026-06-21 | `agents/equity/turtle-trader/universe/nasdaq100.json` | HISTORICAL | OBSERVED | `04` |
| `L-HIST-001` | daily OHLCV history (raw close `c` + adjusted close `a`) | 519 symbols | 519/519 symbols, modal 1255 bars, all last bars 2026-08-03 | bars | 2026-08-03 | `stockanalysis.com/api/symbol/{s\\|e}/{SYM}/history?range=5Y` — retrieved_at `2026-08-04T16:07:21.531242+00:00` | HISTORICAL | OBSERVED | all return/indicator math (adjusted), all entry/target/CI prices (raw) |
| `L-MACRO-VIX` | VIX close | ^VIX | 15.86 | index points | 2026-08-03 | `cdn.cboe.com VIX_History.csv` | HISTORICAL | OBSERVED | `03` regime evidence |
| `L-MACRO-RF` | 3-month T-bill (13-wk bank discount) | US Treasury | 3.75 | percent annual | 2026-08-03 | `US Treasury daily_treasury_bill_rates (13-wk bank discount)` (FRED `fredgraph.csv` timed out) | HISTORICAL | OBSERVED | Sharpe / Sortino / Treynor `rf_1m` |
| `L-SCREEN-001` | marketCap + sector | 7095 listed symbols | 7095 rows | USD / GICS-style label | 2026-08-04 | `api.nasdaq.com/api/screener/stocks?tableonly=true&limit=10000&download=true` | LIVE | OBSERVED | universe filters, `sector_lead` slot |
| `L-EARN-SWEEP` | forward earnings calendar | 512 scored names | 28 business days 2026-08-04…2026-09-10, 0 transport failures, 3050 dated rows | dates | 2026-08-04 | `api.nasdaq.com/api/calendar/earnings?date=YYYY-MM-DD` | LIVE | OBSERVED | `days_to_earnings`, 14-day penalty |
| `L-SET-001` | canonical settlement ledger | all models | n=515 EQ / 90 MF, eff_n=1/1, 0 conflicts | records | 2026-08-04 | `settlement_ledger.py --as-of 2026-08-04` | HISTORICAL | DERIVED | `02 § 0`, calibration binding |
| `L-IBKR-000` | prior close cross-check | SPY / QQQ / SOXX | `UNAVAILABLE` | USD | 2026-08-04 | IBKR MCP `get_price_snapshot` — connector connection invalidated | UNAVAILABLE | UNAVAILABLE | documented failed fetch; grounding stands on 3 web sources |

## Source Ledger — grounded prices (28 rows)

| artifact | field | ticker/entity | value | unit | observation_date | source | freshness_tag | claim_type | used_by |
|---|---|---|---|---|---|---|---|---|---|
| `L-PX-DXCM` | entry_price (raw close) | **DXCM** | 87.31 | USD | 2026-08-03 | stockanalysis 5Y bulk + 5D re-fetch; CNBC `previous_day_closing`; Nasdaq summary `PreviousClose` — 4 sources, max dev 0.0000% | HISTORICAL | OBSERVED | `05`,`06`,`15` entry/target/CI |
| `L-PX-BMY` | entry_price (raw close) | **BMY** | 65.47 | USD | 2026-08-03 | stockanalysis 5Y bulk + 5D re-fetch; CNBC `previous_day_closing`; Nasdaq summary `PreviousClose` — 4 sources, max dev 0.0000% | HISTORICAL | OBSERVED | `05`,`06`,`15` entry/target/CI |
| `L-PX-BEN` | entry_price (raw close) | **BEN** | 35.24 | USD | 2026-08-03 | stockanalysis 5Y bulk + 5D re-fetch; CNBC `previous_day_closing`; Nasdaq summary `PreviousClose` — 4 sources, max dev 0.0000% | HISTORICAL | OBSERVED | `05`,`06`,`15` entry/target/CI |
| `L-PX-BAX` | entry_price (raw close) | **BAX** | 28.10 | USD | 2026-08-03 | stockanalysis 5Y bulk + 5D re-fetch; CNBC `previous_day_closing`; Nasdaq summary `PreviousClose` — 4 sources, max dev 0.0000% | HISTORICAL | OBSERVED | `05`,`06`,`15` entry/target/CI |
| `L-PX-WTW` | entry_price (raw close) | **WTW** | 341.63 | USD | 2026-08-03 | stockanalysis 5Y bulk + 5D re-fetch; CNBC `previous_day_closing`; Nasdaq summary `PreviousClose` — 4 sources, max dev 0.0000% | HISTORICAL | OBSERVED | `05`,`06`,`15` entry/target/CI |
| `L-PX-COO` | entry_price (raw close) | **COO** | 74.23 | USD | 2026-08-03 | stockanalysis 5Y bulk + 5D re-fetch; CNBC `previous_day_closing`; Nasdaq summary `PreviousClose` — 4 sources, max dev 0.0000% | HISTORICAL | OBSERVED | `05`,`06`,`15` entry/target/CI |
| `L-PX-BBY` | entry_price (raw close) | **BBY** | 85.25 | USD | 2026-08-03 | stockanalysis 5Y bulk + 5D re-fetch; CNBC `previous_day_closing`; Nasdaq summary `PreviousClose` — 4 sources, max dev 0.0000% | HISTORICAL | OBSERVED | `05`,`06`,`15` entry/target/CI |
| `L-PX-FTNT` | entry_price (raw close) | **FTNT** | 163.21 | USD | 2026-08-03 | stockanalysis 5Y bulk + 5D re-fetch; CNBC `previous_day_closing`; Nasdaq summary `PreviousClose` — 4 sources, max dev 0.0000% | HISTORICAL | OBSERVED | `05`,`06`,`15` entry/target/CI |
| `L-PX-ROST` | entry_price (raw close) | **ROST** | 252.91 | USD | 2026-08-03 | stockanalysis 5Y bulk + 5D re-fetch; CNBC `previous_day_closing`; Nasdaq summary `PreviousClose` — 4 sources, max dev 0.0000% | HISTORICAL | OBSERVED | `05`,`06`,`15` entry/target/CI |
| `L-PX-NTAP` | entry_price (raw close) | **NTAP** | 182.92 | USD | 2026-08-03 | stockanalysis 5Y bulk + 5D re-fetch; CNBC `previous_day_closing`; Nasdaq summary `PreviousClose` — 4 sources, max dev 0.0000% | HISTORICAL | OBSERVED | `05`,`06`,`15` entry/target/CI |
| `L-PX-IQV` | entry_price (raw close) | **IQV** | 233.36 | USD | 2026-08-03 | stockanalysis 5Y bulk + 5D re-fetch; CNBC `previous_day_closing`; Nasdaq summary `PreviousClose` — 4 sources, max dev 0.0000% | HISTORICAL | OBSERVED | `05`,`06`,`15` entry/target/CI |
| `L-PX-KKR` | entry_price (raw close) | **KKR** | 106.56 | USD | 2026-08-03 | stockanalysis 5Y bulk + 5D re-fetch; CNBC `previous_day_closing`; Nasdaq summary `PreviousClose` — 4 sources, max dev 0.0000% | HISTORICAL | OBSERVED | `05`,`06`,`15` entry/target/CI |
| `L-PX-REGN` | entry_price (raw close) | **REGN** | 759.24 | USD | 2026-08-03 | stockanalysis 5Y bulk + 5D re-fetch; CNBC `previous_day_closing`; Nasdaq summary `PreviousClose` — 4 sources, max dev 0.0000% | HISTORICAL | OBSERVED | `05`,`06`,`15` entry/target/CI |
| `L-PX-TGT` | entry_price (raw close) | **TGT** | 149.35 | USD | 2026-08-03 | stockanalysis 5Y bulk + 5D re-fetch; CNBC `previous_day_closing`; Nasdaq summary `PreviousClose` — 4 sources, max dev 0.0000% | HISTORICAL | OBSERVED | `05`,`06`,`15` entry/target/CI |
| `L-PX-ZBRA` | entry_price (raw close) | **ZBRA** | 291.64 | USD | 2026-08-03 | stockanalysis 5Y bulk + 5D re-fetch; CNBC `previous_day_closing`; Nasdaq summary `PreviousClose` — 4 sources, max dev 0.0000% | HISTORICAL | OBSERVED | `05`,`06`,`15` entry/target/CI |
| `L-PX-ARES` | entry_price (raw close) | **ARES** | 138.57 | USD | 2026-08-03 | stockanalysis 5Y bulk + 5D re-fetch; CNBC `previous_day_closing`; Nasdaq summary `PreviousClose` — 4 sources, max dev 0.0000% | HISTORICAL | OBSERVED | `05`,`06`,`15` entry/target/CI |
| `L-PX-MSFT` | entry_price (raw close) | **MSFT** | 487.65 | USD | 2026-08-03 | stockanalysis 5Y bulk + 5D re-fetch; CNBC `previous_day_closing`; Nasdaq summary `PreviousClose` — 4 sources, max dev 0.0000% | HISTORICAL | OBSERVED | `05`,`06`,`15` entry/target/CI |
| `L-PX-GRMN` | entry_price (raw close) | **GRMN** | 304.76 | USD | 2026-08-03 | stockanalysis 5Y bulk + 5D re-fetch; CNBC `previous_day_closing`; Nasdaq summary `PreviousClose` — 4 sources, max dev 0.0000% | HISTORICAL | OBSERVED | `05`,`06`,`15` entry/target/CI |
| `L-PX-VEEV` | entry_price (raw close) | **VEEV** | 206.25 | USD | 2026-08-03 | stockanalysis 5Y bulk + 5D re-fetch; CNBC `previous_day_closing`; Nasdaq summary `PreviousClose` — 4 sources, max dev 0.0000% | HISTORICAL | OBSERVED | `05`,`06`,`15` entry/target/CI |
| `L-PX-PCAR` | entry_price (raw close) | **PCAR** | 132.06 | USD | 2026-08-03 | stockanalysis 5Y bulk + 5D re-fetch; CNBC `previous_day_closing`; Nasdaq summary `PreviousClose` — 4 sources, max dev 0.0000% | HISTORICAL | OBSERVED | `05`,`06`,`15` entry/target/CI |
| `L-PX-LH` | entry_price (raw close) | **LH** | 307.42 | USD | 2026-08-03 | stockanalysis 5Y bulk + 5D re-fetch; CNBC `previous_day_closing`; Nasdaq summary `PreviousClose` — 4 sources, max dev 0.0000% | HISTORICAL | OBSERVED | `05`,`06`,`15` entry/target/CI |
| `L-PX-COF` | entry_price (raw close) | **COF** | 217.68 | USD | 2026-08-03 | stockanalysis 5Y bulk + 5D re-fetch; CNBC `previous_day_closing`; Nasdaq summary `PreviousClose` — 4 sources, max dev 0.0000% | HISTORICAL | OBSERVED | `05`,`06`,`15` entry/target/CI |
| `L-PX-HIG` | entry_price (raw close) | **HIG** | 142.90 | USD | 2026-08-03 | stockanalysis 5Y bulk + 5D re-fetch; CNBC `previous_day_closing`; Nasdaq summary `PreviousClose` — 4 sources, max dev 0.0000% | HISTORICAL | OBSERVED | `05`,`06`,`15` entry/target/CI |
| `L-PX-WSM` | entry_price (raw close) | **WSM** | 239.80 | USD | 2026-08-03 | stockanalysis 5Y bulk + 5D re-fetch; CNBC `previous_day_closing`; Nasdaq summary `PreviousClose` — 4 sources, max dev 0.0000% | HISTORICAL | OBSERVED | `05`,`06`,`15` entry/target/CI |
| `L-PX-SPY` | entry_price (raw close) | **SPY** | 757.67 | USD | 2026-08-03 | stockanalysis + CNBC + Nasdaq — 4 sources, max dev 0.0000% | HISTORICAL | OBSERVED | `03` ETF block, `15` benchmark_price |
| `L-PX-QQQ` | entry_price (raw close) | **QQQ** | 700.07 | USD | 2026-08-03 | stockanalysis + CNBC + Nasdaq — 4 sources, max dev 0.0000% | HISTORICAL | OBSERVED | `03` ETF block / rate-sensitivity slot |
| `L-PX-SOXX` | entry_price (raw close) | **SOXX** | 507.68 | USD | 2026-08-03 | stockanalysis + CNBC + Nasdaq — 4 sources, max dev 0.0000% | HISTORICAL | OBSERVED | `03` ETF block / rate-sensitivity slot |
| `L-PX-TLT` | entry_price (raw close) | **TLT** | 82.19 | USD | 2026-08-03 | stockanalysis + CNBC + Nasdaq — 4 sources, max dev 0.0000% | HISTORICAL | OBSERVED | `03` ETF block / rate-sensitivity slot |

## Source Ledger — technical, risk and earnings rows (72 rows)

| artifact | field | ticker/entity | value | unit | observation_date | source | freshness_tag | claim_type | used_by |
|---|---|---|---|---|---|---|---|---|---|
| `L-TI-DXCM` | TD9 D/W/M · RSI14 D/W/M · MACD D/W/M · MA align · mom20/60 · vol ratio | **DXCM** | S5/S4/S2 · 72.6/67.8/53.5 · ABOVE/ABOVE/ABOVE · BULL/BULL/MIXE · +20.63%/+44.65% · 1.80x | mixed | 2026-08-03 | `technical_indicators.py --benchmark SPY --range 5y --history-dir <adj CSVs>` (formula: `rules.md § Technical Indicator Pack Definition`) ← `L-HIST-001` | HISTORICAL | DERIVED | `05` Tech_Z, `15` score_explainability |
| `L-RM-DXCM` | beta · TE · realized vol 30d · downside vol · max DD60 | **DXCM** | +0.205 · 14.18% · 15.33% · 6.38% · -13.86% | beta unitless, rest % 1-month | 2026-08-03 | `rules.md § Computed Risk Analytics` on 60 adjusted daily returns ← `L-HIST-001` | HISTORICAL | DERIVED | `05` Macro_Z, sigma, Sharpe/Sortino/IR, `07` |
| `L-EA-DXCM` | next earnings date | **DXCM** | no print in swept window | date | 2026-08-04 | `L-EARN-SWEEP` — `NO_PRINT_IN_WINDOW` | LIVE | OBSERVED | `05` 14-day penalty, `08` event concentration |
| `L-TI-BMY` | TD9 D/W/M · RSI14 D/W/M · MACD D/W/M · MA align · mom20/60 · vol ratio | **BMY** | S9/S7/S2 · 71.8/68.5/65.5 · ABOVE/ABOVE/ABOVE · BULL/BULL/BULL · +15.47%/+17.00% · 2.63x | mixed | 2026-08-03 | `technical_indicators.py --benchmark SPY --range 5y --history-dir <adj CSVs>` (formula: `rules.md § Technical Indicator Pack Definition`) ← `L-HIST-001` | HISTORICAL | DERIVED | `05` Tech_Z, `15` score_explainability |
| `L-RM-BMY` | beta · TE · realized vol 30d · downside vol · max DD60 | **BMY** | -0.203 · 8.20% · 8.67% · 4.92% · -9.32% | beta unitless, rest % 1-month | 2026-08-03 | `rules.md § Computed Risk Analytics` on 60 adjusted daily returns ← `L-HIST-001` | HISTORICAL | DERIVED | `05` Macro_Z, sigma, Sharpe/Sortino/IR, `07` |
| `L-EA-BMY` | next earnings date | **BMY** | no print in swept window | date | 2026-08-04 | `L-EARN-SWEEP` — `NO_PRINT_IN_WINDOW` | LIVE | OBSERVED | `05` 14-day penalty, `08` event concentration |
| `L-TI-BEN` | TD9 D/W/M · RSI14 D/W/M · MACD D/W/M · MA align · mom20/60 · vol ratio | **BEN** | S7/S1/S8 · 66.1/74.3/71.8 · BULL_X/ABOVE/ABOVE · BULL/BULL/BULL · +2.32%/+14.23% · 1.56x | mixed | 2026-08-03 | `technical_indicators.py --benchmark SPY --range 5y --history-dir <adj CSVs>` (formula: `rules.md § Technical Indicator Pack Definition`) ← `L-HIST-001` | HISTORICAL | DERIVED | `05` Tech_Z, `15` score_explainability |
| `L-RM-BEN` | beta · TE · realized vol 30d · downside vol · max DD60 | **BEN** | +1.095 · 6.84% · 8.12% · 5.18% · -6.42% | beta unitless, rest % 1-month | 2026-08-03 | `rules.md § Computed Risk Analytics` on 60 adjusted daily returns ← `L-HIST-001` | HISTORICAL | DERIVED | `05` Macro_Z, sigma, Sharpe/Sortino/IR, `07` |
| `L-EA-BEN` | next earnings date | **BEN** | no print in swept window | date | 2026-08-04 | `L-EARN-SWEEP` — `NO_PRINT_IN_WINDOW` | LIVE | OBSERVED | `05` 14-day penalty, `08` event concentration |
| `L-TI-BAX` | TD9 D/W/M · RSI14 D/W/M · MACD D/W/M · MA align · mom20/60 · vol ratio | **BAX** | S7/S9/S3 · 76.4/73.6/51.7 · ABOVE/ABOVE/ABOVE · BULL/MIXE/MIXE · +24.45%/+65.57% · 1.44x | mixed | 2026-08-03 | `technical_indicators.py --benchmark SPY --range 5y --history-dir <adj CSVs>` (formula: `rules.md § Technical Indicator Pack Definition`) ← `L-HIST-001` | HISTORICAL | DERIVED | `05` Tech_Z, `15` score_explainability |
| `L-RM-BAX` | beta · TE · realized vol 30d · downside vol · max DD60 | **BAX** | +0.644 · 12.40% · 14.23% · 6.11% · -7.19% | beta unitless, rest % 1-month | 2026-08-03 | `rules.md § Computed Risk Analytics` on 60 adjusted daily returns ← `L-HIST-001` | HISTORICAL | DERIVED | `05` Macro_Z, sigma, Sharpe/Sortino/IR, `07` |
| `L-EA-BAX` | next earnings date | **BAX** | no print in swept window | date | 2026-08-04 | `L-EARN-SWEEP` — `NO_PRINT_IN_WINDOW` | LIVE | OBSERVED | `05` 14-day penalty, `08` event concentration |
| `L-TI-WTW` | TD9 D/W/M · RSI14 D/W/M · MACD D/W/M · MA align · mom20/60 · vol ratio | **WTW** | S7/S7/S2 · 81.6/68.4/60.8 · ABOVE/ABOVE/BELOW · BULL/MIXE/BULL · +18.76%/+35.84% · 1.33x | mixed | 2026-08-03 | `technical_indicators.py --benchmark SPY --range 5y --history-dir <adj CSVs>` (formula: `rules.md § Technical Indicator Pack Definition`) ← `L-HIST-001` | HISTORICAL | DERIVED | `05` Tech_Z, `15` score_explainability |
| `L-RM-WTW` | beta · TE · realized vol 30d · downside vol · max DD60 | **WTW** | -0.367 · 9.12% · 9.85% · 2.98% · -6.18% | beta unitless, rest % 1-month | 2026-08-03 | `rules.md § Computed Risk Analytics` on 60 adjusted daily returns ← `L-HIST-001` | HISTORICAL | DERIVED | `05` Macro_Z, sigma, Sharpe/Sortino/IR, `07` |
| `L-EA-WTW` | next earnings date | **WTW** | no print in swept window | date | 2026-08-04 | `L-EARN-SWEEP` — `NO_PRINT_IN_WINDOW` | LIVE | OBSERVED | `05` 14-day penalty, `08` event concentration |
| `L-TI-COO` | TD9 D/W/M · RSI14 D/W/M · MACD D/W/M · MA align · mom20/60 · vol ratio | **COO** | S5/S1/S2 · 63.3/55.8/46.2 · BULL_X/ABOVE/BULL_X · BULL/MIXE/BEAR · +2.23%/+21.45% · 1.24x | mixed | 2026-08-03 | `technical_indicators.py --benchmark SPY --range 5y --history-dir <adj CSVs>` (formula: `rules.md § Technical Indicator Pack Definition`) ← `L-HIST-001` | HISTORICAL | DERIVED | `05` Tech_Z, `15` score_explainability |
| `L-RM-COO` | beta · TE · realized vol 30d · downside vol · max DD60 | **COO** | -0.380 · 9.17% · 8.75% · 5.20% · -7.67% | beta unitless, rest % 1-month | 2026-08-03 | `rules.md § Computed Risk Analytics` on 60 adjusted daily returns ← `L-HIST-001` | HISTORICAL | DERIVED | `05` Macro_Z, sigma, Sharpe/Sortino/IR, `07` |
| `L-EA-COO` | next earnings date | **COO** | 2026-09-09 | date | 2026-08-04 | `L-EARN-SWEEP` — `CONFIRMED_CALENDAR` | LIVE | OBSERVED | `05` 14-day penalty, `08` event concentration |
| `L-TI-BBY` | TD9 D/W/M · RSI14 D/W/M · MACD D/W/M · MA align · mom20/60 · vol ratio | **BBY** | B2/S9/S4 · 56.3/65.1/58.9 · BELOW/ABOVE/ABOVE · BULL/BULL/BULL · +9.29%/+47.19% · 1.20x | mixed | 2026-08-03 | `technical_indicators.py --benchmark SPY --range 5y --history-dir <adj CSVs>` (formula: `rules.md § Technical Indicator Pack Definition`) ← `L-HIST-001` | HISTORICAL | DERIVED | `05` Tech_Z, `15` score_explainability |
| `L-RM-BBY` | beta · TE · realized vol 30d · downside vol · max DD60 | **BBY** | +0.421 · 12.87% · 8.14% · 4.24% · -8.93% | beta unitless, rest % 1-month | 2026-08-03 | `rules.md § Computed Risk Analytics` on 60 adjusted daily returns ← `L-HIST-001` | HISTORICAL | DERIVED | `05` Macro_Z, sigma, Sharpe/Sortino/IR, `07` |
| `L-EA-BBY` | next earnings date | **BBY** | 2026-08-27 | date | 2026-08-04 | `L-EARN-SWEEP` — `CONFIRMED_CALENDAR` | LIVE | OBSERVED | `05` 14-day penalty, `08` event concentration |
| `L-TI-FTNT` | TD9 D/W/M · RSI14 D/W/M · MACD D/W/M · MA align · mom20/60 · vol ratio | **FTNT** | S4/S9/S6 · 61.3/77.7/78.4 · BELOW/ABOVE/ABOVE · BULL/BULL/BULL · +0.53%/+81.45% · 1.08x | mixed | 2026-08-03 | `technical_indicators.py --benchmark SPY --range 5y --history-dir <adj CSVs>` (formula: `rules.md § Technical Indicator Pack Definition`) ← `L-HIST-001` | HISTORICAL | DERIVED | `05` Tech_Z, `15` score_explainability |
| `L-RM-FTNT` | beta · TE · realized vol 30d · downside vol · max DD60 | **FTNT** | +0.968 · 15.84% · 10.70% · 3.32% · -10.10% | beta unitless, rest % 1-month | 2026-08-03 | `rules.md § Computed Risk Analytics` on 60 adjusted daily returns ← `L-HIST-001` | HISTORICAL | DERIVED | `05` Macro_Z, sigma, Sharpe/Sortino/IR, `07` |
| `L-EA-FTNT` | next earnings date | **FTNT** | no print in swept window | date | 2026-08-04 | `L-EARN-SWEEP` — `NO_PRINT_IN_WINDOW` | LIVE | OBSERVED | `05` 14-day penalty, `08` event concentration |
| `L-TI-ROST` | TD9 D/W/M · RSI14 D/W/M · MACD D/W/M · MA align · mom20/60 · vol ratio | **ROST** | S7/S4/S9 · 71.0/69.1/76.4 · ABOVE/BULL_X/ABOVE · BULL/BULL/BULL · +19.66%/+10.70% · 1.04x | mixed | 2026-08-03 | `technical_indicators.py --benchmark SPY --range 5y --history-dir <adj CSVs>` (formula: `rules.md § Technical Indicator Pack Definition`) ← `L-HIST-001` | HISTORICAL | DERIVED | `05` Tech_Z, `15` score_explainability |
| `L-RM-ROST` | beta · TE · realized vol 30d · downside vol · max DD60 | **ROST** | +0.219 · 9.86% · 8.84% · 7.54% · -13.03% | beta unitless, rest % 1-month | 2026-08-03 | `rules.md § Computed Risk Analytics` on 60 adjusted daily returns ← `L-HIST-001` | HISTORICAL | DERIVED | `05` Macro_Z, sigma, Sharpe/Sortino/IR, `07` |
| `L-EA-ROST` | next earnings date | **ROST** | 2026-08-20 | date | 2026-08-04 | `L-EARN-SWEEP` — `CONFIRMED_CALENDAR` | LIVE | OBSERVED | `05` 14-day penalty, `08` event concentration |
| `L-TI-NTAP` | TD9 D/W/M · RSI14 D/W/M · MACD D/W/M · MA align · mom20/60 · vol ratio | **NTAP** | S9/S5/S5 · 68.0/74.3/71.5 · ABOVE/ABOVE/ABOVE · BULL/BULL/BULL · +12.18%/+64.20% · 0.76x | mixed | 2026-08-03 | `technical_indicators.py --benchmark SPY --range 5y --history-dir <adj CSVs>` (formula: `rules.md § Technical Indicator Pack Definition`) ← `L-HIST-001` | HISTORICAL | DERIVED | `05` Tech_Z, `15` score_explainability |
| `L-RM-NTAP` | beta · TE · realized vol 30d · downside vol · max DD60 | **NTAP** | +1.439 · 17.76% · 12.08% · 7.52% · -15.81% | beta unitless, rest % 1-month | 2026-08-03 | `rules.md § Computed Risk Analytics` on 60 adjusted daily returns ← `L-HIST-001` | HISTORICAL | DERIVED | `05` Macro_Z, sigma, Sharpe/Sortino/IR, `07` |
| `L-EA-NTAP` | next earnings date | **NTAP** | 2026-08-26 | date | 2026-08-04 | `L-EARN-SWEEP` — `CONFIRMED_CALENDAR` | LIVE | OBSERVED | `05` 14-day penalty, `08` event concentration |
| `L-TI-IQV` | TD9 D/W/M · RSI14 D/W/M · MACD D/W/M · MA align · mom20/60 · vol ratio | **IQV** | B1/S7/S3 · 66.4/66.3/57.0 · ABOVE/ABOVE/ABOVE · BULL/MIXE/MIXE · +13.30%/+32.24% · 1.12x | mixed | 2026-08-03 | `technical_indicators.py --benchmark SPY --range 5y --history-dir <adj CSVs>` (formula: `rules.md § Technical Indicator Pack Definition`) ← `L-HIST-001` | HISTORICAL | DERIVED | `05` Tech_Z, `15` score_explainability |
| `L-RM-IQV` | beta · TE · realized vol 30d · downside vol · max DD60 | **IQV** | -0.211 · 13.93% · 15.39% · 4.64% · -10.23% | beta unitless, rest % 1-month | 2026-08-03 | `rules.md § Computed Risk Analytics` on 60 adjusted daily returns ← `L-HIST-001` | HISTORICAL | DERIVED | `05` Macro_Z, sigma, Sharpe/Sortino/IR, `07` |
| `L-EA-IQV` | next earnings date | **IQV** | no print in swept window | date | 2026-08-04 | `L-EARN-SWEEP` — `NO_PRINT_IN_WINDOW` | LIVE | OBSERVED | `05` 14-day penalty, `08` event concentration |
| `L-TI-KKR` | TD9 D/W/M · RSI14 D/W/M · MACD D/W/M · MA align · mom20/60 · vol ratio | **KKR** | S1/S6/S3 · 65.8/55.3/49.3 · ABOVE/ABOVE/BELOW · BULL/MIXE/MIXE · +11.03%/+5.93% · 1.53x | mixed | 2026-08-03 | `technical_indicators.py --benchmark SPY --range 5y --history-dir <adj CSVs>` (formula: `rules.md § Technical Indicator Pack Definition`) ← `L-HIST-001` | HISTORICAL | DERIVED | `05` Tech_Z, `15` score_explainability |
| `L-RM-KKR` | beta · TE · realized vol 30d · downside vol · max DD60 | **KKR** | +1.273 · 8.45% · 10.42% · 5.54% · -13.08% | beta unitless, rest % 1-month | 2026-08-03 | `rules.md § Computed Risk Analytics` on 60 adjusted daily returns ← `L-HIST-001` | HISTORICAL | DERIVED | `05` Macro_Z, sigma, Sharpe/Sortino/IR, `07` |
| `L-EA-KKR` | next earnings date | **KKR** | no print in swept window | date | 2026-08-04 | `L-EARN-SWEEP` — `NO_PRINT_IN_WINDOW` | LIVE | OBSERVED | `05` 14-day penalty, `08` event concentration |
| `L-TI-REGN` | TD9 D/W/M · RSI14 D/W/M · MACD D/W/M · MA align · mom20/60 · vol ratio | **REGN** | S5/S7/S1 · 76.4/60.4/52.8 · ABOVE/ABOVE/ABOVE · BULL/MIXE/MIXE · +16.84%/+5.45% · 1.06x | mixed | 2026-08-03 | `technical_indicators.py --benchmark SPY --range 5y --history-dir <adj CSVs>` (formula: `rules.md § Technical Indicator Pack Definition`) ← `L-HIST-001` | HISTORICAL | DERIVED | `05` Tech_Z, `15` score_explainability |
| `L-RM-REGN` | beta · TE · realized vol 30d · downside vol · max DD60 | **REGN** | +0.320 · 10.28% · 9.40% · 4.24% · -16.84% | beta unitless, rest % 1-month | 2026-08-03 | `rules.md § Computed Risk Analytics` on 60 adjusted daily returns ← `L-HIST-001` | HISTORICAL | DERIVED | `05` Macro_Z, sigma, Sharpe/Sortino/IR, `07` |
| `L-EA-REGN` | next earnings date | **REGN** | no print in swept window | date | 2026-08-04 | `L-EARN-SWEEP` — `NO_PRINT_IN_WINDOW` | LIVE | OBSERVED | `05` 14-day penalty, `08` event concentration |
| `L-TI-TGT` | TD9 D/W/M · RSI14 D/W/M · MACD D/W/M · MA align · mom20/60 · vol ratio | **TGT** | S6/S2/S9 · 69.5/68.2/65.0 · ABOVE/ABOVE/ABOVE · BULL/BULL/MIXE · +18.44%/+15.80% · 1.27x | mixed | 2026-08-03 | `technical_indicators.py --benchmark SPY --range 5y --history-dir <adj CSVs>` (formula: `rules.md § Technical Indicator Pack Definition`) ← `L-HIST-001` | HISTORICAL | DERIVED | `05` Tech_Z, `15` score_explainability |
| `L-RM-TGT` | beta · TE · realized vol 30d · downside vol · max DD60 | **TGT** | -0.164 · 10.26% · 10.03% · 5.84% · -10.69% | beta unitless, rest % 1-month | 2026-08-03 | `rules.md § Computed Risk Analytics` on 60 adjusted daily returns ← `L-HIST-001` | HISTORICAL | DERIVED | `05` Macro_Z, sigma, Sharpe/Sortino/IR, `07` |
| `L-EA-TGT` | next earnings date | **TGT** | 2026-08-19 | date | 2026-08-04 | `L-EARN-SWEEP` — `CONFIRMED_CALENDAR` | LIVE | OBSERVED | `05` 14-day penalty, `08` event concentration |
| `L-TI-ZBRA` | TD9 D/W/M · RSI14 D/W/M · MACD D/W/M · MA align · mom20/60 · vol ratio | **ZBRA** | S6/S7/S4 · 68.0/63.4/50.5 · ABOVE/ABOVE/ABOVE · BULL/MIXE/MIXE · +7.90%/+26.93% · 1.82x | mixed | 2026-08-03 | `technical_indicators.py --benchmark SPY --range 5y --history-dir <adj CSVs>` (formula: `rules.md § Technical Indicator Pack Definition`) ← `L-HIST-001` | HISTORICAL | DERIVED | `05` Tech_Z, `15` score_explainability |
| `L-RM-ZBRA` | beta · TE · realized vol 30d · downside vol · max DD60 | **ZBRA** | +1.396 · 13.00% · 11.19% · 4.43% · -16.64% | beta unitless, rest % 1-month | 2026-08-03 | `rules.md § Computed Risk Analytics` on 60 adjusted daily returns ← `L-HIST-001` | HISTORICAL | DERIVED | `05` Macro_Z, sigma, Sharpe/Sortino/IR, `07` |
| `L-EA-ZBRA` | next earnings date | **ZBRA** | 2026-08-04 | date | 2026-08-04 | `L-EARN-SWEEP` — `CONFIRMED_CALENDAR` | LIVE | OBSERVED | `05` 14-day penalty, `08` event concentration |
| `L-TI-ARES` | TD9 D/W/M · RSI14 D/W/M · MACD D/W/M · MA align · mom20/60 · vol ratio | **ARES** | S2/S3/S3 · 69.3/57.4/51.6 · ABOVE/ABOVE/BELOW · BULL/MIXE/MIXE · +13.74%/+13.00% · 1.66x | mixed | 2026-08-03 | `technical_indicators.py --benchmark SPY --range 5y --history-dir <adj CSVs>` (formula: `rules.md § Technical Indicator Pack Definition`) ← `L-HIST-001` | HISTORICAL | DERIVED | `05` Tech_Z, `15` score_explainability |
| `L-RM-ARES` | beta · TE · realized vol 30d · downside vol · max DD60 | **ARES** | +1.722 · 10.25% · 13.46% · 6.97% · -20.28% | beta unitless, rest % 1-month | 2026-08-03 | `rules.md § Computed Risk Analytics` on 60 adjusted daily returns ← `L-HIST-001` | HISTORICAL | DERIVED | `05` Macro_Z, sigma, Sharpe/Sortino/IR, `07` |
| `L-EA-ARES` | next earnings date | **ARES** | no print in swept window | date | 2026-08-04 | `L-EARN-SWEEP` — `NO_PRINT_IN_WINDOW` | LIVE | OBSERVED | `05` 14-day penalty, `08` event concentration |
| `L-TI-MSFT` | TD9 D/W/M · RSI14 D/W/M · MACD D/W/M · MA align · mom20/60 · vol ratio | **MSFT** | S5/S4/S2 · 78.3/64.0/57.0 · ABOVE/ABOVE/BELOW · BULL/MIXE/BULL · +26.09%/+18.06% · 1.74x | mixed | 2026-08-03 | `technical_indicators.py --benchmark SPY --range 5y --history-dir <adj CSVs>` (formula: `rules.md § Technical Indicator Pack Definition`) ← `L-HIST-001` | HISTORICAL | DERIVED | `05` Tech_Z, `15` score_explainability |
| `L-RM-MSFT` | beta · TE · realized vol 30d · downside vol · max DD60 | **MSFT** | +1.066 · 12.83% · 16.05% · 3.74% · -23.38% | beta unitless, rest % 1-month | 2026-08-03 | `rules.md § Computed Risk Analytics` on 60 adjusted daily returns ← `L-HIST-001` | HISTORICAL | DERIVED | `05` Macro_Z, sigma, Sharpe/Sortino/IR, `07` |
| `L-EA-MSFT` | next earnings date | **MSFT** | no print in swept window | date | 2026-08-04 | `L-EARN-SWEEP` — `NO_PRINT_IN_WINDOW` | LIVE | OBSERVED | `05` 14-day penalty, `08` event concentration |
| `L-TI-GRMN` | TD9 D/W/M · RSI14 D/W/M · MACD D/W/M · MA align · mom20/60 · vol ratio | **GRMN** | S6/S6/S2 · 79.9/73.1/69.9 · ABOVE/ABOVE/ABOVE · BULL/BULL/BULL · +24.28%/+26.06% · 0.86x | mixed | 2026-08-03 | `technical_indicators.py --benchmark SPY --range 5y --history-dir <adj CSVs>` (formula: `rules.md § Technical Indicator Pack Definition`) ← `L-HIST-001` | HISTORICAL | DERIVED | `05` Tech_Z, `15` score_explainability |
| `L-RM-GRMN` | beta · TE · realized vol 30d · downside vol · max DD60 | **GRMN** | +0.173 · 12.25% · 15.28% · 4.17% · -7.03% | beta unitless, rest % 1-month | 2026-08-03 | `rules.md § Computed Risk Analytics` on 60 adjusted daily returns ← `L-HIST-001` | HISTORICAL | DERIVED | `05` Macro_Z, sigma, Sharpe/Sortino/IR, `07` |
| `L-EA-GRMN` | next earnings date | **GRMN** | no print in swept window | date | 2026-08-04 | `L-EARN-SWEEP` — `NO_PRINT_IN_WINDOW` | LIVE | OBSERVED | `05` 14-day penalty, `08` event concentration |
| `L-TI-VEEV` | TD9 D/W/M · RSI14 D/W/M · MACD D/W/M · MA align · mom20/60 · vol ratio | **VEEV** | S6/S6/S2 · 63.8/56.8/47.4 · ABOVE/ABOVE/BELOW · BULL/MIXE/MIXE · +7.42%/+23.24% · 1.66x | mixed | 2026-08-03 | `technical_indicators.py --benchmark SPY --range 5y --history-dir <adj CSVs>` (formula: `rules.md § Technical Indicator Pack Definition`) ← `L-HIST-001` | HISTORICAL | DERIVED | `05` Tech_Z, `15` score_explainability |
| `L-RM-VEEV` | beta · TE · realized vol 30d · downside vol · max DD60 | **VEEV** | -0.004 · 13.32% · 12.76% · 5.36% · -18.82% | beta unitless, rest % 1-month | 2026-08-03 | `rules.md § Computed Risk Analytics` on 60 adjusted daily returns ← `L-HIST-001` | HISTORICAL | DERIVED | `05` Macro_Z, sigma, Sharpe/Sortino/IR, `07` |
| `L-EA-VEEV` | next earnings date | **VEEV** | 2026-08-26 | date | 2026-08-04 | `L-EARN-SWEEP` — `CONFIRMED_CALENDAR` | LIVE | OBSERVED | `05` 14-day penalty, `08` event concentration |
| `L-TI-PCAR` | TD9 D/W/M · RSI14 D/W/M · MACD D/W/M · MA align · mom20/60 · vol ratio | **PCAR** | B2/S9/S2 · 59.7/66.7/66.6 · ABOVE/ABOVE/ABOVE · BULL/BULL/BULL · +4.88%/+13.70% · 1.23x | mixed | 2026-08-03 | `technical_indicators.py --benchmark SPY --range 5y --history-dir <adj CSVs>` (formula: `rules.md § Technical Indicator Pack Definition`) ← `L-HIST-001` | HISTORICAL | DERIVED | `05` Tech_Z, `15` score_explainability |
| `L-RM-PCAR` | beta · TE · realized vol 30d · downside vol · max DD60 | **PCAR** | +1.034 · 7.83% · 8.90% · 3.95% · -5.86% | beta unitless, rest % 1-month | 2026-08-03 | `rules.md § Computed Risk Analytics` on 60 adjusted daily returns ← `L-HIST-001` | HISTORICAL | DERIVED | `05` Macro_Z, sigma, Sharpe/Sortino/IR, `07` |
| `L-EA-PCAR` | next earnings date | **PCAR** | no print in swept window | date | 2026-08-04 | `L-EARN-SWEEP` — `NO_PRINT_IN_WINDOW` | LIVE | OBSERVED | `05` 14-day penalty, `08` event concentration |
| `L-TI-LH` | TD9 D/W/M · RSI14 D/W/M · MACD D/W/M · MA align · mom20/60 · vol ratio | **LH** | B1/S7/S2 · 65.4/66.2/63.5 · ABOVE/ABOVE/ABOVE · BULL/BULL/BULL · +8.10%/+19.98% · 0.90x | mixed | 2026-08-03 | `technical_indicators.py --benchmark SPY --range 5y --history-dir <adj CSVs>` (formula: `rules.md § Technical Indicator Pack Definition`) ← `L-HIST-001` | HISTORICAL | DERIVED | `05` Tech_Z, `15` score_explainability |
| `L-RM-LH` | beta · TE · realized vol 30d · downside vol · max DD60 | **LH** | -0.106 · 7.08% · 7.92% · 3.41% · -6.20% | beta unitless, rest % 1-month | 2026-08-03 | `rules.md § Computed Risk Analytics` on 60 adjusted daily returns ← `L-HIST-001` | HISTORICAL | DERIVED | `05` Macro_Z, sigma, Sharpe/Sortino/IR, `07` |
| `L-EA-LH` | next earnings date | **LH** | no print in swept window | date | 2026-08-04 | `L-EARN-SWEEP` — `NO_PRINT_IN_WINDOW` | LIVE | OBSERVED | `05` 14-day penalty, `08` event concentration |
| `L-TI-COF` | TD9 D/W/M · RSI14 D/W/M · MACD D/W/M · MA align · mom20/60 · vol ratio | **COF** | S6/S2/S3 · 64.7/60.4/59.8 · BULL_X/ABOVE/BELOW · BULL/MIXE/BULL · +5.41%/+13.04% · 0.96x | mixed | 2026-08-03 | `technical_indicators.py --benchmark SPY --range 5y --history-dir <adj CSVs>` (formula: `rules.md § Technical Indicator Pack Definition`) ← `L-HIST-001` | HISTORICAL | DERIVED | `05` Tech_Z, `15` score_explainability |
| `L-RM-COF` | beta · TE · realized vol 30d · downside vol · max DD60 | **COF** | +1.005 · 8.16% · 8.96% · 5.87% · -7.77% | beta unitless, rest % 1-month | 2026-08-03 | `rules.md § Computed Risk Analytics` on 60 adjusted daily returns ← `L-HIST-001` | HISTORICAL | DERIVED | `05` Macro_Z, sigma, Sharpe/Sortino/IR, `07` |
| `L-EA-COF` | next earnings date | **COF** | no print in swept window | date | 2026-08-04 | `L-EARN-SWEEP` — `NO_PRINT_IN_WINDOW` | LIVE | OBSERVED | `05` 14-day penalty, `08` event concentration |
| `L-TI-HIG` | TD9 D/W/M · RSI14 D/W/M · MACD D/W/M · MA align · mom20/60 · vol ratio | **HIG** | B1/S7/S2 · 58.6/61.0/65.0 · ABOVE/ABOVE/BELOW · BULL/BULL/BULL · +3.82%/+7.56% · 1.22x | mixed | 2026-08-03 | `technical_indicators.py --benchmark SPY --range 5y --history-dir <adj CSVs>` (formula: `rules.md § Technical Indicator Pack Definition`) ← `L-HIST-001` | HISTORICAL | DERIVED | `05` Tech_Z, `15` score_explainability |
| `L-RM-HIG` | beta · TE · realized vol 30d · downside vol · max DD60 | **HIG** | -0.629 · 6.02% · 6.50% · 3.38% · -7.43% | beta unitless, rest % 1-month | 2026-08-03 | `rules.md § Computed Risk Analytics` on 60 adjusted daily returns ← `L-HIST-001` | HISTORICAL | DERIVED | `05` Macro_Z, sigma, Sharpe/Sortino/IR, `07` |
| `L-EA-HIG` | next earnings date | **HIG** | no print in swept window | date | 2026-08-04 | `L-EARN-SWEEP` — `NO_PRINT_IN_WINDOW` | LIVE | OBSERVED | `05` 14-day penalty, `08` event concentration |
| `L-TI-WSM` | TD9 D/W/M · RSI14 D/W/M · MACD D/W/M · MA align · mom20/60 · vol ratio | **WSM** | S1/S2/S3 · 63.1/65.0/68.4 · ABOVE/ABOVE/ABOVE · BULL/BULL/BULL · +7.49%/+29.03% · 0.98x | mixed | 2026-08-03 | `technical_indicators.py --benchmark SPY --range 5y --history-dir <adj CSVs>` (formula: `rules.md § Technical Indicator Pack Definition`) ← `L-HIST-001` | HISTORICAL | DERIVED | `05` Tech_Z, `15` score_explainability |
| `L-RM-WSM` | beta · TE · realized vol 30d · downside vol · max DD60 | **WSM** | +0.874 · 10.03% · 9.20% · 3.89% · -9.79% | beta unitless, rest % 1-month | 2026-08-03 | `rules.md § Computed Risk Analytics` on 60 adjusted daily returns ← `L-HIST-001` | HISTORICAL | DERIVED | `05` Macro_Z, sigma, Sharpe/Sortino/IR, `07` |
| `L-EA-WSM` | next earnings date | **WSM** | 2026-08-26 | date | 2026-08-04 | `L-EARN-SWEEP` — `CONFIRMED_CALENDAR` | LIVE | OBSERVED | `05` 14-day penalty, `08` event concentration |

## Coverage summary

| Coverage class | Count | Notes |
|---|---|---|
| `OBSERVED` | 59 | directly read from a cited source |
| `DERIVED` | 50 | computed from ledger rows with a named formula |
| `INFERRED` | 0 | no judgment-based numeric was used in scoring |
| `ILLUSTRATIVE` | 0 | run is `DELAYED`, not `ILLUSTRATIVE_MODE` |
| `UNAVAILABLE` | 1 | IBKR cross-check only; does not block any Required input |

## Families with no fetch path

`Fund_Z` and `Sent_Z` have **no ledger rows at universe scale** and are carried as
`0.00 (UNAVAILABLE)` in the score arithmetic per `rules.md § Family Aggregation`. They are never
described as neutral or supportive. This is the sole cause of the `NO_TRADE` status — see
`05 § Why zero names are investable`.
