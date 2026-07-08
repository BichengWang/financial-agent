# 01 Preflight — Source Ledger

Run: `claude-opus-4-8` · 2026-06-30 (Tuesday) · Data mode **LIVE** · Status **NO_TRADE**

This ledger is the grounding gate. No downstream artifact introduces a price, return, vol, beta, drawdown, earnings date, target, CI, technical-indicator state, or sizing input that is not derivable from a row here. Allowed `freshness_tag` / `claim_type` values per `rules.md § Source Ledger Contract`.

## Retrieval Provenance

| Source | Tool | Retrieved (UTC) | Scope |
|---|---|---|---|
| IBKR real-time snapshots (connected market-data tool) | `Interactive_Brokers_IBKR.get_price_snapshot` | 2026-06-30 ~15:55–16:12Z | LIVE last/bid-ask for SPY, QQQ, SOXX, MU, AMD, UNH, LLY (7-name grounding + ETF sleeve) |
| IBKR contract search | `search_contracts` | 2026-06-30 ~15:50–16:10Z | contract_id resolution |
| Yahoo chart fetch — analytics | `fetch_analytics.py` (urllib, query2.finance.yahoo.com) | 2026-06-30 15:59:32Z | 1y daily OHLCV → realized vol, beta, drawdown, momentum, return-series for all 38 symbols |
| Yahoo chart fetch — technicals | `technical_indicators.py` | 2026-06-30 16:01:51Z | 5y daily OHLCV → TD-9, RSI(14), MACD(12,26,9), MA, momentum, RS daily/weekly/monthly; artifact `technical_indicators.json` |

**Data-integrity cross-check (connected tool vs web feed).** Every IBKR LIVE snapshot was compared to the same-symbol Yahoo latest close; all 7 agree within 0.30%, establishing the Yahoo feed as a faithful same-session source for the broad screening universe:

| Symbol | IBKR LIVE (L) | Yahoo close (L) | Δ% |
|---|---|---|---|
| SPY | 745.17 | 745.79 | 0.08% |
| QQQ | 734.34 | 734.31 | 0.00% |
| SOXX | 636.03 | 636.31 | 0.04% |
| MU | 1146.00 | 1147.28 | 0.11% |
| AMD | 576.46 | 578.00 | 0.27% |
| UNH | 416.49 | 416.08 | 0.10% |
| LLY | 1209.29 | 1208.32 | 0.08% |

Per the Price Sourcing Standard, the 7 sampled symbols are grounded by a connected market-data tool; the remaining universe is same-session Yahoo intraday (single web source) validated against the connected tool within 0.30%. Because the run is **NO_TRADE** (no sizing, no execution; monitoring forecasts are paper), broad-universe prices are tagged `DELAYED`/`OBSERVED` with this validation disclosed; per-name dual-sourcing was not performed for the 28 non-sampled names and is recorded as a data-quality note, not a GO blocker (the run does not seek GO).

## Ledger — Prices (entry)

| id | field | entity | value | unit | observation_date | source | freshness_tag | claim_type | used_by |
|---|---|---|---|---|---|---|---|---|---|
| L001 | last | SPY | 745.17 | USD | 2026-06-30 | IBKR get_price_snapshot (retrieved_at 2026-06-30T15:55Z) | LIVE | OBSERVED | 03 ETF block, 15 |
| L002 | last | QQQ | 734.34 | USD | 2026-06-30 | IBKR snapshot | LIVE | OBSERVED | 03 ETF block, 15 |
| L003 | last | SOXX | 636.03 | USD | 2026-06-30 | IBKR snapshot | LIVE | OBSERVED | 03 ETF block, 15 |
| L004 | last | UNH | 416.49 | USD | 2026-06-30 | IBKR snapshot (bid/ask 416.55/416.84) | LIVE | OBSERVED | 05, 06, 15 |
| L005 | last | LLY | 1209.29 | USD | 2026-06-30 | IBKR snapshot (bid/ask 1208.99/1210.00) | LIVE | OBSERVED | 05, 06, 15 |
| L006 | last | MU | 1146.00 | USD | 2026-06-30 | IBKR snapshot | LIVE | OBSERVED | 05, 15 |
| L007 | last | AMD | 576.46 | USD | 2026-06-30 | IBKR snapshot | LIVE | OBSERVED | 05, 15 |
| L008 | close | V | 342.92 | USD | 2026-06-30 | Yahoo chart (validated within 0.3% of connected tool, sample L001–L007) | DELAYED | OBSERVED | 05, 06, 15 |
| L009 | close | BAC | 57.19 | USD | 2026-06-30 | Yahoo chart (validated feed) | DELAYED | OBSERVED | 05, 06, 15 |
| L010 | close | CAT | 1064.99 | USD | 2026-06-30 | Yahoo chart | DELAYED | OBSERVED | 05, 15 |
| L011 | close | GE | 372.11 | USD | 2026-06-30 | Yahoo chart | DELAYED | OBSERVED | 05, 15 |
| L012 | close | SO | 96.42 | USD | 2026-06-30 | Yahoo chart | DELAYED | OBSERVED | 05, 15 |
| L013 | close | LIN | 519.75 | USD | 2026-06-30 | Yahoo chart | DELAYED | OBSERVED | 05, 15 |
| L014 | close | JPM | 328.25 | USD | 2026-06-30 | Yahoo chart | DELAYED | OBSERVED | 05, 15 |
| L015 | close | JNJ | 255.88 | USD | 2026-06-30 | Yahoo chart | DELAYED | OBSERVED | 05, 15 |
| L016 | close | HD | 351.79 | USD | 2026-06-30 | Yahoo chart | DELAYED | OBSERVED | 05, 15 |
| L017 | close | TSLA | 416.07 | USD | 2026-06-30 | Yahoo chart | DELAYED | OBSERVED | 05, 15 |
| L018 | close | PG | 146.06 | USD | 2026-06-30 | Yahoo chart | DELAYED | OBSERVED | 05, 15 |
| L019 | close | (remaining 20 universe names) | see 04/05 tables | USD | 2026-06-30 | Yahoo chart (validated feed) | DELAYED | OBSERVED | 04, 05 |

Full 38-symbol grounded close set lives in run artifact `analytics.json` (`latest_close`, `latest_date=2026-06-30`) and `technical_indicators.json` (`daily.close`).

## Ledger — Price history (drives all derived risk analytics)

| id | field | entity | value | unit | observation_date | source | freshness_tag | claim_type | used_by |
|---|---|---|---|---|---|---|---|---|---|
| L100 | 1y daily OHLCV | all 38 symbols | ≥250 bars/sym | series | 2025-06→2026-06-30 | Yahoo chart via fetch_analytics.py (retrieved 2026-06-30T15:59:32Z) | HISTORICAL | OBSERVED | sigma, beta, corr, drawdown, momentum |
| L101 | 5y daily OHLCV | all 38 symbols | ~1255 bars/sym | series | 2021-06→2026-06-30 | Yahoo chart via technical_indicators.py (retrieved 2026-06-30T16:01:51Z) | HISTORICAL | OBSERVED | TD-9/RSI/MACD daily/weekly/monthly |

## Ledger — Derived risk/return analytics (formulas + input rows)

Each row is `DERIVED`; formula and input rows named. Per-symbol values in `analytics.json`; representative rows shown.

| id | field | entity | value | formula / inputs | freshness_tag | claim_type | used_by |
|---|---|---|---|---|---|---|---|
| L200 | sigma_1m (REALIZED_VOL_30D) | per name | e.g. UNH 7.6%, V 5.7%, MU 35.0%, SOXX 20.5% | stdev(last 30 daily returns from L100) × √21 | DERIVED | DERIVED | 05, 07, 15 (sigma) |
| L201 | rvol_30d_annual | per name | e.g. SPY 15.4%, SOXX 71.1%, MU 121% | stdev(30d returns L100) × √252 | DERIVED | DERIVED | 05 penalties, 03 |
| L202 | beta_60d vs SPY | per name | e.g. UNH −0.16, V −0.01, LLY 0.22, BAC 0.32, CAT 1.93, GE 1.25, MU 4.16, QQQ 1.564, SOXX 3.171 | cov(r_i, r_SPY)/var(r_SPY) over last 60 common days (L100) | DERIVED | DERIVED | 05, 06, 07, 15, 03 |
| L203 | max_drawdown_60d | per name | e.g. SPY −4.5%, UNH −6.1%, NFLX −34.2% | min peak-to-trough over last 60 closes (L100) | DERIVED | DERIVED | 05, 07 |
| L204 | momentum_20d / 60d | per name | see 05 / technical_indicators.json | close[-1]/close[-21 or -61] − 1 | DERIVED | DERIVED | 05 Tech_Z |
| L205 | relative_strength_20d/60d vs SPY | per name | see 05 | mom_i − mom_SPY (L204) | DERIVED | DERIVED | 05 Tech_Z/Sent_Z |
| L206 | downside_dev_1m | per name | see analytics.json | stdev(negative daily returns, 60d) × √21 | DERIVED | DERIVED | 05 Sortino |
| L207 | tracking_error_1m | per name | see metrics.json | stdev(r_i − beta_i·r_SPY, 60d) × √21 | DERIVED | DERIVED | 05 IR, 08 |
| L208 | avg_pairwise_corr (top-8 ranked) | basket | 0.084 | mean off-diagonal of 60d daily-return corr matrix (L100) | DERIVED | DERIVED | 07, 08 |
| L209 | Sharpe / Sortino / Treynor / IR / Kelly / VaR95 / CVaR95 | per name | see 05 table | rules.md § Ratio Definitions; rf not sourced → Sharpe/Sortino/Treynor `RAW_DIAGNOSTIC` (mu/σ form) | DERIVED | DERIVED | 05, 06 |
| L210 | 20d ADV (USD) | per name | e.g. NVDA $31.9bn, SPY $45.6bn, PLD $0.58bn | mean(close×volume, 20d) (L100) | DERIVED | DERIVED | 04 liquidity |

`rf_1m` (risk-free) is **not sourced** this run → Sharpe, Sortino, Treynor, Calmar are labeled `RAW_DIAGNOSTIC` and computed as `mu/σ`, `mu/σ_down`, `mu/β` without a risk-free adjustment (`rules.md § Metric History and Grounding`).

## Ledger — Technical indicator pack (lineage to technical_indicators.json)

| id | field | entity | value | source | freshness_tag | claim_type | used_by |
|---|---|---|---|---|---|---|---|
| L300 | TD-9 setup d/w/m | all names | e.g. SOXX w/m = SELL_SETUP_9; GE d = SELL_SETUP_9; CVX/XOM/AMT d = BUY_SETUP_9 | technical_indicators.json (formula: close vs close 4 bars prior, capped 9) ← L101 | HISTORICAL | DERIVED | 05, 06, penalties |
| L301 | RSI(14) d/w/m | all names | e.g. SPY 54.6/63.0/72.2; SOXX 59.0/75.2/88.6; MU 59.6/82.3/91.6; NFLX 29.6/30.6/41.5 | technical_indicators.json (Wilder RSI) ← L101 | HISTORICAL | DERIVED | 05, 06, penalties |
| L302 | MACD(12,26,9) state d/w/m | all names | e.g. SPY BELOW/ABOVE/ABOVE; NVDA monthly BEARISH_CROSS; BAC/GE weekly→monthly BULLISH_CROSS | technical_indicators.json ← L101 | HISTORICAL | DERIVED | 05, 06 |
| L303 | MA20/MA50 + alignment d/w/m | all names | e.g. SPY/QQQ/SOXX all BULLISH d/w/m | technical_indicators.json ← L101 | HISTORICAL | DERIVED | 03, 05 |
| L304 | 20-bar volume ratio | all names | see technical_indicators.json | technical_indicators.json ← L101 | HISTORICAL | DERIVED | 05 Sent_Z |

## Ledger — Reflection / baseline

| id | field | entity | value | source | freshness_tag | claim_type | used_by |
|---|---|---|---|---|---|---|---|
| L400 | MoM baseline folder | — | `gemini-3-5-flash-2026-05-30` (ILLUSTRATIVE, REVIEW_ONLY, no 15_predictions.json) | dated-output scan | HISTORICAL | OBSERVED | 02 |
| L401 | matured OPEN predictions (target_date ≤ 2026-06-30) | all 17 ledgers | 0 (earliest maturity 2026-07-08) | scan of all `15_predictions.json` (290 records, all OPEN, target 2026-07-08…07-28) | HISTORICAL | OBSERVED | 02 settlement |
| L402 | baseline picks (ref-state) | — | META, LLY, NFLX, AVGO, NOW, UNH, GE, LIN | gemini baseline 06/07 (ILLUSTRATIVE_REF) | ILLUSTRATIVE_REF | ILLUSTRATIVE | 02 |
| L403 | grounded close ~2026-05-29 (MoM anchor) | baseline names + SPY | analytics.json `ref_close_0529` | Yahoo history (L100) | HISTORICAL | OBSERVED | 02 MoM table |

## Coverage Summary

| claim_type | count (categories) | note |
|---|---|---|
| OBSERVED | 7 LIVE prices + 31 validated-feed prices + 2 history series + baseline scan | prices & raw history |
| DERIVED | sigma, rvol, beta, drawdown, momentum, RS, downside-dev, TE, corr, Sharpe/Sortino/Treynor/IR/Kelly/VaR/CVaR, ADV, all TD9/RSI/MACD/MA states (38 symbols × multiple timeframes) | formulas + input rows named above |
| INFERRED | regime label rationale (03), thesis/catalyst notes (05/06) | judgment, cites L-rows |
| ILLUSTRATIVE | baseline picks (L402) | reference-state, never live-executable |
| UNAVAILABLE | options IV/skew, short interest/borrow, bid-ask tape (broad), analyst-revision tape, institutional flow, full-universe feed, risk-free rate | Enhancing inputs (not GO blockers) + rf (→ RAW_DIAGNOSTIC ratios) |

**Status eligibility from grounding:** All five Required inputs (`rules.md § Input Classification`) are grounded — see `00_run_manifest.md` GO-Gate Table. The run is **NO_TRADE** for portfolio-construction reasons (investable count < 5; beta band infeasible under the protected 5% single-name cap), **not** for any data-grounding failure. Enhancing inputs are `UNAVAILABLE` and cap confidence at `MEDIUM`; they do not block status.
