# 01 Preflight — Source Ledger — 2026-07-29

Published **before** reflection, scoring, portfolio construction, or risk review used any fact
downstream. Every price, return, volatility, beta, earnings date, target, CI bound, drawdown,
ratio, technical-indicator state, and sizing input below has a row here or is `UNAVAILABLE`.

## Run Basis

Pre-open fire at 08:05 ET on 2026-07-29. The price basis is the **2026-07-28 close** — the last completed
session. At this hour no vendor is mid-update, so a single consistent basis serves both the
indicator math and the entry prices; there is no split T-1-technical / same-day-entry
reconciliation to carry.

## Price Sourcing Standard — Compliance

`rules.md § Price Sourcing Standard` requires a market-data tool **or** two independent web sources
agreeing within 1%, with `retrieved_at` recorded.

- **Primary** (stockanalysis.com/api/symbol/{s|e}/{SYM}/history?range=5Y): all 519/519 symbols, 5y daily bars, 25.8s, zero failures.
  Retrieved 2026-07-29T12:55:53Z.
- **Second and third sources** for every published name and core ETF: CNBC `restQuote` and
  Nasdaq `quote/{sym}/info`. Retrieved 2026-07-29T13:05:53Z.
- **Result: 28 of 28 symbols matched exact to the cent.** Zero symbols exceeded the 0.1%
  re-read threshold, so no confirmation pass was required.
- **Fourth source for the core ETFs**: IBKR `get_price_snapshot`. `prior-close` is empty pre-market
  (as on 2026-07-27 and 2026-07-28), so prior close = `last - change`: SPY 740.86, QQQ 675.49,
  SOXX 491.46 — all three exact against the primary (L012).

Every entry price is `HISTORICAL` / `OBSERVED` at observation date 2026-07-28. No price is `APPROX - sourced`.

## Corporate-Action Basis

Per the Track B rule accepted 2026-07-26: **adjusted** close `a` drives every return, momentum,
relative-strength, volatility, downside-deviation, beta, tracking-error and drawdown input and is
what `technical_indicators.py` consumed; **unadjusted** close `c` is the entry, target and CI basis.

A universe-wide scan of last-bar `c` vs `a` found **1 of 519 symbols** carrying an ex-dividend
adjustment on the basis bar: **WST** (`c` 337.00 vs `a` 336.78). WST is not in the published set, but
it *is* in the settlement cohort — settled at the unadjusted 337.00 per the 2026-07-15 precedent
(settle unadjusted-entry predictions at the unadjusted close, disclosed).

## Source Ledger

| artifact | field | ticker/entity | value | unit | observation_date | source | freshness_tag | claim_type | used_by |
|---|---|---|---|---|---|---|---|---|---|
| L001 | index union universe | S&P500 ∪ NDX100 | 515 tickers | count | 2026-07-29 | build_index_universe.py from local caches (sp500 fetched_at 2026-06-21T21:05:56Z) | HISTORICAL | OBSERVED | 03,04,05 |
| L002 | entry price (unadjusted close `c`) | 514 names | 2026-07-28 close | USD | 2026-07-28 | stockanalysis.com/api/symbol/{s|e}/{SYM}/history?range=5Y | HISTORICAL | OBSERVED | 05,06,07,15 |
| L003 | adjusted close `a` | 514 names | 2026-07-28 adj close | USD | 2026-07-28 | stockanalysis.com/api/symbol/{s|e}/{SYM}/history?range=5Y | HISTORICAL | OBSERVED | all return/indicator math |
| L004 | 5y daily bars | SPY | 1255 bars from 2021-07-28 | bars | 2026-07-28 | stockanalysis.com/api/symbol/{s|e}/{SYM}/history?range=5Y | HISTORICAL | OBSERVED | beta, RS, benchmark |
| L005 | 5y daily bars | QQQ | 1255 bars | bars | 2026-07-28 | stockanalysis.com/api/symbol/{s|e}/{SYM}/history?range=5Y | HISTORICAL | OBSERVED | 03 ETF block |
| L006 | 5y daily bars | SOXX | 1255 bars | bars | 2026-07-28 | stockanalysis.com/api/symbol/{s|e}/{SYM}/history?range=5Y | HISTORICAL | OBSERVED | 03 ETF block |
| L007 | 5y daily bars | TLT | 1255 bars | bars | 2026-07-28 | stockanalysis.com/api/symbol/{s|e}/{SYM}/history?range=5Y | HISTORICAL | OBSERVED | 03 regime cross-check |
| L008 | VIX close | ^VIX | 18.21 | index | 2026-07-28 | cdn.cboe.com/api/global/us_indices/daily_prices/VIX_History.csv | HISTORICAL | OBSERVED | 03 regime |
| L009 | 13-week T-bill bank discount | US 13W | 3.77% | pct/yr | 2026-07-28 | home.treasury.gov daily_treasury_bill_rates | HISTORICAL | OBSERVED | Sharpe/Sortino/Treynor rf |
| L010 | sector / industry / market cap | 514 names | sector+mktcap | text/USD | 2026-07-29 | api.nasdaq.com/api/screener/stocks (7,037 rows) | DELAYED | OBSERVED | 04,05,07 |
| L011 | entry-price 2nd/3rd source | 28 symbols | 28/28 exact to the cent | USD | 2026-07-28 | quote.cnbc.com restQuote + api.nasdaq.com/api/quote/{sym}/info | DELAYED | OBSERVED | Price Sourcing Standard |
| L012 | ETF prior close cross-check | SPY,QQQ,SOXX | 740.86 / 675.49 / 491.46 | USD | 2026-07-28 | IBKR get_price_snapshot, prior close = last - change (prior-close empty pre-market) | DELAYED | DERIVED | 03 ETF block |
| L013 | 30d realized vol | 514 names | stdev(30 daily adj returns) x sqrt(21) | pct | 2026-07-28 | DERIVED from L003 | HISTORICAL | DERIVED | sigma, VaR, CVaR, Kelly |
| L014 | 30d downside deviation | 514 names | stdev(negative daily returns, 30d) x sqrt(21) | pct | 2026-07-28 | DERIVED from L003 | HISTORICAL | DERIVED | Sortino |
| L015 | 60d beta vs SPY | 514 names | cov(r,rSPY)/var(rSPY), 60 trading days | ratio | 2026-07-28 | DERIVED from L003+L004 | HISTORICAL | DERIVED | Macro_Z, Treynor, feasibility |
| L016 | tracking error (1m) | 514 names | stdev(r - beta*rSPY, 60d) x sqrt(21) | pct | 2026-07-28 | DERIVED from L003+L004+L015 | HISTORICAL | DERIVED | Information Ratio |
| L017 | 20d / 60d momentum | 514 names | adj close ratio - 1 | pct | 2026-07-28 | DERIVED from L003 | HISTORICAL | DERIVED | Tech_Z |
| L018 | RS20 / RS60 vs SPY | 514 names | name momentum - SPY momentum | pp | 2026-07-28 | DERIVED from L003+L004 | HISTORICAL | DERIVED | Tech_Z |
| L019 | 60d max drawdown | 514 names | worst peak-to-trough over 60 bars | pct | 2026-07-28 | DERIVED from L003 | HISTORICAL | DERIVED | Macro_Z, tail risk |
| L020 | 20d volume ratio | 514 names | technical_indicators.json volume_ratio_20d | ratio | 2026-07-28 | technical_indicators.py from L003 bars | HISTORICAL | DERIVED | Tech_Z |
| L021 | TD-9 / RSI(14) / MACD / MA alignment | 519 tickers | daily, weekly, monthly | state/value | 2026-07-28 | technical_indicators.py -> technical_indicators.json | HISTORICAL | DERIVED | Tech_Z, penalties, 05/06/07 |
| L022 | next earnings date (primary) | 514 names | 317 in-window, 197 no print by 2026-09-04 | date | 2026-07-29 | api.nasdaq.com/api/calendar/earnings sweep 2026-07-29..2026-09-04, 28/28 days, 0 failures | DELAYED | OBSERVED | earnings penalty, confidence |
| L023 | next earnings date (corroboration) | 59 names | 25/25 agreement, 0 disagree | date | 2026-07-29 | api.nasdaq.com/api/analyst/{sym}/earnings-date | DELAYED | OBSERVED | validates L022 |
| L024 | earnings penalty | 272 names | -0.10 when buffered days-to-earnings <= 14 | score | 2026-07-29 | rules.md § Risk Controls, applied to L022 | HISTORICAL | DERIVED | Adj Score, confidence |
| L025 | volatility penalty | 0 names in published set | -0.05 when rvol30 > 2x universe median | score | 2026-07-28 | rules.md § Risk Controls; median 0.0968, threshold 0.1937 | HISTORICAL | DERIVED | Adj Score |
| L026 | TD-9 exhaustion penalty | see 05 | -0.05 when TD9 daily SELL_SETUP_9 and RSI14_d >= 70 | score | 2026-07-28 | rules.md § TD-9 Definition, from L021 | HISTORICAL | DERIVED | Adj Score |
| L027 | mu (calibration table) | 24 published | band by adjusted-score percentile, no per-name adjustment | pct | 2026-07-29 | rules.md § mu Calibration Table | HISTORICAL | DERIVED | 15_predictions.json |
| L028 | target price | 24 published | entry x (1 + mu) | USD | 2026-07-29 | DERIVED from L002+L027 | HISTORICAL | DERIVED | 05,06,15 |
| L029 | 70% CI bounds | 24 published | entry x (1 + mu +/- 1.04 sigma) | USD | 2026-07-29 | DERIVED from L002+L013+L027 | HISTORICAL | DERIVED | 05,06,15 |
| L030 | Forecast Sharpe | 24 published | (mu - rf_1m) / sigma | ratio | 2026-07-29 | DERIVED from L009+L013+L027; rf_1m=0.003142 | HISTORICAL | DERIVED | 05,06,07 |
| L031 | Sortino | 24 published | (mu - rf_1m) / downside sigma | ratio | 2026-07-29 | DERIVED from L009+L014+L027 | HISTORICAL | DERIVED | 05,06,07 |
| L032 | Information Ratio | 24 published | (mu - beta x SPY mu) / tracking error | ratio | 2026-07-29 | DERIVED from L015+L016+L027 | HISTORICAL | DERIVED | 05,06,07 |
| L033 | Treynor | 24 published | (mu - rf_1m) / beta | ratio | 2026-07-29 | DERIVED from L009+L015+L027 | HISTORICAL | DERIVED | 05 |
| L034 | Kelly raw and 0.25x | 24 published | mu / sigma^2, then 0.25x, capped at 5% NAV | fraction | 2026-07-29 | DERIVED from L013+L027, rules.md § Risk Controls | HISTORICAL | DERIVED | 05,07 sizing gate |
| L035 | VaR95 / CVaR95 | 24 published | mu - 1.65 sigma / mu - 2.06 sigma (normal) | pct | 2026-07-29 | DERIVED from L013+L027 | HISTORICAL | DERIVED | 05,07 |
| L036 | options IV / skew | universe | no feed wired | - | 2026-07-29 | no source | UNAVAILABLE | UNAVAILABLE | caps confidence; never a GO blocker |
| L037 | canonical settlement ledger | 44 settled | due inventory 0, conflicts 0 | count | 2026-07-29 | settlement_ledger.py --as-of 2026-07-29 | HISTORICAL | DERIVED | 02 § 0 |
| L038 | rolling calibration metrics | EQ + MF | EQ n=298 eff_n=1; MF n=54 eff_n=1 | metrics | 2026-07-29 | settlement_manifest.json rolling_metrics | HISTORICAL | DERIVED | 02 § 0, 05 calibration binding |
| L039 | MoM baseline | claude-fable-5-2026-07-01 | 24 names, hit 62.5% | package | 2026-07-29 | agents.md § Orchestrator Step 2 | HISTORICAL | OBSERVED | 02 § 1-5 |
| L040 | Adj Score | 514 names | (0.30 Fund_Z + 0.30 Tech_Z + 0.25 Sent_Z + 0.15 Macro_Z) x DQ - penalties | score | 2026-07-29 | rules.md § Financial Metrics and Score Attribution | HISTORICAL | DERIVED | 05,06,09,15 |
| L041 | INDEX_UNION_PCTL | 514 names | percentile rank over n=514 | pct | 2026-07-29 | DERIVED from L040 | HISTORICAL | DERIVED | mu band, evidence threshold #1 |
| L042 | regime label | market | NEUTRAL | label | 2026-07-28 | DERIVED from L004+L008+L021 (SPY vs MA20/MA50, VIX, momentum) | HISTORICAL | DERIVED | 03, ETF mu prior |
| L043 | core ETF mu | SPY,QQQ,SOXX | +0.5000% / +0.8654% / +1.8241% | pct | 2026-07-29 | rules.md § Core ETF Market Forecast; SPY = regime prior, QQQ/SOXX = beta x SPY mu | HISTORICAL | DERIVED | 03, 15 |
| L044 | core ETF sigma | SPY,QQQ,SOXX | 3.6764% / 7.3946% / 19.1803% | pct | 2026-07-28 | REALIZED_VOL_30D from L004-L006 | HISTORICAL | DERIVED | 03, 15 |
| L045 | portfolio feasibility | top pool | max attainable beta +0.9090 vs 0.90 floor | ratio | 2026-07-29 | DERIVED from L015; mean of 20 highest betas in >=80th-pctl pool | HISTORICAL | DERIVED | 07 Task 0 |
| L046 | Fund_Z | universe | no fundamental fetch path wired at universe scale | - | 2026-07-29 | rules.md § SHADOW Diagnostic Tooling (not promoted) | UNAVAILABLE | UNAVAILABLE | evidence threshold #2 blocked |
| L047 | Sent_Z | universe | no sentiment fetch path wired at universe scale | - | 2026-07-29 | rules.md § SHADOW Diagnostic Tooling (not promoted) | UNAVAILABLE | UNAVAILABLE | evidence threshold #2 blocked |
| L048 | short interest / borrow / bid-ask / analyst revisions | universe | no feed wired | - | 2026-07-29 | no source | UNAVAILABLE | UNAVAILABLE | caps confidence; never a GO blocker |
| L049 | data-quality multiplier | 514 names | 0.80 | factor | 2026-07-29 | rules.md § Data Quality Multiplier — notable coverage gaps (2 of 4 families UNAVAILABLE) | HISTORICAL | DERIVED | Adj Score, evidence threshold #4 |
| L050 | defensive Macro polarity | universe | applied=True | judgment | 2026-07-29 | INFERRED from L004+L006+L007+L015: SPY below MA20 and MA50, SOXX -24.97% from 60d high, 42.02% of universe at negative beta, TLT 20d -3.31% | HISTORICAL | INFERRED | 05 Macro_Z polarity |
| L051 | MoM tie-break non-invariance | 3 folders | fable-5 hit 62.5% vs gpt-5 hit 14.3% | pct | 2026-07-29 | DERIVED from L039 + gpt-5-2026-07-01 ledger | HISTORICAL | INFERRED | 02 § 1, 13 |

### Coverage

`OBSERVED` 12 · `DERIVED` 33 · `INFERRED` 2 · `UNAVAILABLE` 4 · `ILLUSTRATIVE` 0.

The four `UNAVAILABLE` rows (L036, L046, L047, L048) are all **Enhancing** inputs under
`rules.md § Input Classification`. They lower the data-quality multiplier to 0.80 and cap
confidence; per `rules.md`, none of them may block `GO`, and none is cited as a blocker anywhere
in this package.
