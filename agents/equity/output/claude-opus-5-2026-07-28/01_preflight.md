# 01 Preflight — Source Ledger — 2026-07-28

Published **before** reflection, scoring, portfolio construction or risk review uses any fact
downstream. Schema and allowed tag values: `rules.md § Source Ledger Contract`.

**Retrieval window:** 2026-07-28T08:05:00-04:00 (all fetches this run). **Price basis:** 2026-07-27 close — the last
completed session, because this run fires pre-open.

**Grounding summary.** 28 of 28 published names and core ETFs are grounded by
**two independent sources** on the unadjusted close (L002 + L005), with a third corroborator for the
ETFs (L006). Nasdaq and stockanalysis agree **exactly to the cent on 28/28**
(max difference 0.000000%). The single CNBC disagreement is an ex-dividend basis
artifact, diagnosed in L054 — not a fetch error and not a price dispute.

| artifact | field | ticker/entity | value | unit | observation_date | source | freshness_tag | claim_type | used_by |
|---|---|---|---|---|---|---|---|---|---|
| L001 | index union universe | S&P500 ∪ NDX100 | 515 tickers (503/101, overlap 89) | count | 2026-07-27 | build_index_universe.py → universe_summary.json; caches fetched_at 2026-06-21T21:05:56Z | HISTORICAL | OBSERVED | 03, 04, 05 |
| L002 | daily close (raw, unadjusted) | 519 symbols | 2026-07-27 bar present for all 519 | USD | 2026-07-27 | stockanalysis.com/api/symbol/{s\|e}/{SYM}/history?range=5Y field `c`; retrieved_at 2026-07-28T08:05:00-04:00 | HISTORICAL | OBSERVED | entry/target/CI prices, 02, 03, 05, 06, 07, 15 |
| L003 | daily close (split+dividend adjusted) | 519 symbols | 2026-07-27 bar present for all 519 | USD | 2026-07-27 | same endpoint, field `a`; retrieved_at 2026-07-28T08:05:00-04:00 | HISTORICAL | OBSERVED | ALL return/vol/beta/momentum/indicator math (Track B 2026-07-26) |
| L004 | independent close cross-check #1 | 28 published names + ETFs | 27/28 exact to the cent; 1 disagreement (PAYX, see L054) | USD | 2026-07-27 | quote.cnbc.com/quote-html-webservice/restQuote (curmktstatus PRE_MKT) | DELAYED | OBSERVED | Price Sourcing Standard, 08 |
| L005 | independent close cross-check #2 | 28 published names + ETFs | 28/28 exact to the cent, max diff 0.000000% | USD | 2026-07-27 | api.nasdaq.com/api/quote/{sym}/info secondaryData.lastSalePrice, gated on the "Closed at Jul 27, 2026 4:00 PM ET" marker | DELAYED | OBSERVED | Price Sourcing Standard, 08 |
| L006 | core ETF close cross-check #3 | SPY, QQQ, SOXX | SPY 739.09, QQQ 682.12, SOXX 516.23 — all exact to the cent vs L002 | USD | 2026-07-27 | IBKR MCP get_price_snapshot (conids 756733 / 320227571 / 12658194); prior-close empty pre-market so prior close = last − change | LIVE | OBSERVED | 03, 08 |
| L007 | VIX close | ^VIX | 18.67 (2026-07-27), 20d mean 16.8795 | index | 2026-07-27 | cdn.cboe.com/api/global/us_indices/daily_prices/VIX_History.csv | HISTORICAL | OBSERVED | 03 |
| L008 | risk-free rate | 13-week T-bill | 3.82% annual → 0.3183% 1-month | pct | 2026-07-27 | home.treasury.gov daily_treasury_bill_rates 2026 CSV, 13-week bank discount (FRED fredgraph.csv timed out; documented fallback) | OFFICIAL_FILING | OBSERVED | Sharpe, Sortino, Treynor, Calmar (L030–L033) |
| L009 | market cap + sector/industry | 7,016 US listings | 514 of 515 union names matched; 2 market cap `UNAVAILABLE` | USD / label | 2026-07-27 | api.nasdaq.com/api/screener/stocks?tableonly=true&limit=10000&download=true | DELAYED | OBSERVED | 04 inclusion filters, 05 thesis, 07 sector table |
| L010 | technical indicator pack | 519 tickers | TD-9 / RSI(14) / MACD(12,26,9) / MA / momentum / volume / RS on daily, weekly, monthly | mixed | 2026-07-27 | technical_indicators.py --history-dir <adjusted-close csv tree> --benchmark SPY --range 5y → technical_indicators.json | DERIVED | DERIVED | 05 Tech_Z, 06, 07, 09, 15 |
| L011 | price-history fetch manifest | 519 symbols | 519 OK / 0 failed in 26.5s at 8 workers; every symbol's last bar = 2026-07-27 | count | 2026-07-27 | price_history_fetch_manifest.json | DERIVED | OBSERVED | 00, 04, 08 |
| L012 | 20-day average daily dollar volume | 514 names | min 42.2M, median 372.1M | USD/day | 2026-07-27 | Σ(close×volume)/20 over the last 20 raw bars; inputs L002 | DERIVED | DERIVED | 04 liquidity filter |
| L013 | 30-day realized volatility (1-month) | 514 names + 3 ETFs | universe median 9.36%; 2× penalty threshold 18.72% | pct | 2026-07-27 | stdev(last 30 daily adjusted returns) × sqrt(21); inputs L003 | DERIVED | DERIVED | sigma for every forecast, 05, 07, 15 |
| L014 | downside deviation (1-month) | 514 names | stdev of NEGATIVE daily returns only, last 30 sessions, × sqrt(21) | pct | 2026-07-27 | inputs L003; distinct from L013 (the 2026-07-21 Sortino fix) | DERIVED | DERIVED | Sortino (L031) |
| L015 | 60-day beta vs SPY | 514 names + 3 ETFs | 213 of 514 names (41.44%) carry NEGATIVE beta | ratio | 2026-07-27 | OLS slope of daily adjusted returns vs SPY over the trailing 60 aligned sessions; inputs L003 | DERIVED | DERIVED | Macro_Z, Treynor, 07 feasibility, 03 |
| L016 | tracking error (1-month) | 514 names | stdev of beta-adjusted residual returns over the same 60 sessions × sqrt(21) | pct | 2026-07-27 | inputs L003, L015 | DERIVED | DERIVED | Information Ratio (L032) |
| L017 | 60-day max drawdown | 514 names + 3 ETFs | worst peak-to-trough on adjusted closes over the trailing 60 sessions | pct | 2026-07-27 | inputs L003 | DERIVED | DERIVED | Macro_Z, Calmar, 05, 07 |
| L018 | 20d / 60d momentum and relative strength vs SPY | 514 names + 3 ETFs | momentum_20d_pct, momentum_60d_pct, relative_strength_20d/60d_vs_benchmark_pct | pct | 2026-07-27 | technical_indicators.json (L010), computed on adjusted closes | DERIVED | DERIVED | Tech_Z, 05, 06, 09 |
| L019 | TD-9 / RSI(14) / MACD(12,26,9) / MA alignment | 514 names + 3 ETFs | daily, weekly and monthly states per name | state / index | 2026-07-27 | technical_indicators.json (L010); TD Sequential setup only, Wilder RSI, EMA(12,26,9) | DERIVED | DERIVED | Tech_Z, penalties, 05, 06, 09, 15 |
| L020 | 20-day volume ratio | 514 names | volume_ratio_20d from the indicator pack | ratio | 2026-07-27 | technical_indicators.json (L010) | DERIVED | DERIVED | Tech_Z |
| L021 | family z-scores | 514 names | Tech_Z from 8 metric z-scores, Macro_Z from 3; each winsorized at the 5th/95th pctl then z-scored | z | 2026-07-27 | inputs L013, L015, L017, L018, L019, L020; method rules.md § Family Aggregation | DERIVED | DERIVED | Adj Score, 05, 15 |
| L022 | earnings preflight — pass 1 | top-40 pre-penalty ranks | 40 names fetched, 0 transport failures | count | 2026-07-27 | api.nasdaq.com/api/analyst/{sym}/earnings-date (data.announcement / data.reportText free text) | DELAYED | OBSERVED | 05 penalties, 06, 15 |
| L023 | earnings preflight — pass 2 (convergence) | post-penalty top-40 entrants | 18 further names fetched, 0 transport failures; post-penalty top-20 fully grounded ⇒ converged | count | 2026-07-27 | same endpoint; cap 4 passes / 60 names — used 2 passes / 58 names | DELAYED | OBSERVED | 05 penalties, 06, 15 |
| L024 | earnings resolution mix | 58 grounded names | CONFIRMED 31, ESTIMATED_CADENCE 22, ESTIMATED_PRINT_WEEK 5 | count | 2026-07-27 | earnings_calendar_manifest.json | DERIVED | DERIVED | 05, 06, 08 |
| L025 | vendor-empty print signature | 27 vendor-empty names | print-like iff \|1d move\| ≥ 3.5% OR (volume ≥ 1.8× trailing median AND \|1d move\| ≥ 1.5%), last 12 sessions | rule | 2026-07-27 | gpt-5-2026-07-27 13_evolution_log Track B, ACCEPTED, effective 2026-07-28 — **this run is the first to apply it**; inputs L002 | DERIVED | DERIVED | 05 penalties |
| L026 | names never earnings-grounded, excluded from publication | 7 top-30 entrants | DXCM, BXP, BAC, FRT, KVUE, FFIV, SO | list | 2026-07-27 | a name whose earnings were never resolved would read downstream as penalty-free (Track B 2026-07-27) — excluded rather than published | DERIVED | INFERRED | 05, 06, 08 |
| L027 | mu calibration table | 206 ranked names | percentile band → prior mu; **no positive per-name adjustment applied anywhere** | pct | 2026-07-27 | rules.md § mu Calibration Table | DERIVED | DERIVED | 05, 06, 15 |
| L028 | target price | 24 published names | target = entry × (1 + mu) | USD | 2026-07-27 | rules.md § Price and Target Citation Standard; inputs L002, L027 | DERIVED | DERIVED | 05, 06, 15 |
| L029 | 70% CI bounds | 24 published names | entry × (1 + mu ∓ 1.04σ) | USD | 2026-07-27 | inputs L002, L013, L027 | DERIVED | DERIVED | 05, 06, 15 |
| L030 | Forecast Sharpe | 24 published names | (mu − rf_1m) / sigma | ratio | 2026-07-27 | inputs L008, L013, L027 | DERIVED | DERIVED | 05, 06, 07 |
| L031 | Sortino | 24 published names | (mu − rf_1m) / downside_sigma_1m | ratio | 2026-07-27 | inputs L008, L014, L027 | DERIVED | DERIVED | 05, 06, 07 |
| L032 | Information Ratio | 24 published names | (mu − beta × SPY_mu) / tracking_error_1m | ratio | 2026-07-27 | inputs L015, L016, L027 and the NEUTRAL SPY prior +0.50% | DERIVED | DERIVED | 05, 06, 07 |
| L033 | Treynor / Calmar | 24 published names | (mu − rf_1m) / beta; (mu − rf_1m) / \|max_dd_60d\| | ratio | 2026-07-27 | inputs L008, L015, L017, L027 | DERIVED | DERIVED | 05 diagnostics |
| L034 | Kelly | 24 published names | raw = mu / sigma²; 0.25×Kelly bounded by the 5% single-name NAV cap | fraction of NAV | 2026-07-27 | inputs L013, L027; rules.md § Risk Controls | DERIVED | DERIVED | 05, 07 |
| L035 | VaR95 / CVaR95 (1-month, parametric) | 24 published names | mu − 1.65σ and mu − 2.06σ, normality assumed and stated | pct | 2026-07-27 | inputs L013, L027 | DERIVED | DERIVED | 05, 07 |
| L036 | data quality multiplier | 514 names | 0.8 universe-wide (notable coverage gaps) | multiplier | 2026-07-27 | rules.md § Data Quality Multiplier; driven by L046, L047, L048 | DERIVED | INFERRED | Adj Score, 05, evidence threshold #4 |
| L037 | penalties | 514 names | 67 names penalised: earnings ≤14d 34, RVol > 2× median 30, TD9-9 + RSI≥70 4 | score | 2026-07-27 | rules.md § Risk Controls, § TD-9 Definition; inputs L013, L019, L024 | DERIVED | DERIVED | Adj Score, 05, 08 |
| L038 | Adj Score | 514 names | (0.30×Fund_Z + 0.30×Tech_Z + 0.25×Sent_Z + 0.15×Macro_Z) × DQ − Penalties | score | 2026-07-27 | inputs L021, L036, L037; Fund_Z and Sent_Z enter as 0.00 and are labelled `UNAVAILABLE`, never neutral | DERIVED | DERIVED | 05, 06, 09, 15 |
| L039 | adjusted-score percentile | 514 names | `INDEX_UNION_PCTL (n=514)`; pctl = (n − rank) / (n − 1) × 100 | pctl | 2026-07-27 | inputs L038 | DERIVED | DERIVED | 05 mu bands, 06, 07 |
| L040 | core ETF market forecast — SPY | SPY | entry 739.09, mu +0.50%, sigma 3.64%, beta 1.0000 | mixed | 2026-07-27 | rules.md § Core ETF Market Forecast; inputs L002, L003, L013, L015; Regime prior for NEUTRAL = +0.50%; no +/-1.0pp adjustment applied. | DERIVED | DERIVED | 03, 09, 15 |
| L041 | core ETF market forecast — QQQ | QQQ | entry 682.12, mu +0.86%, sigma 7.27%, beta 1.7200 | mixed | 2026-07-27 | rules.md § Core ETF Market Forecast; inputs L002, L003, L013, L015; beta_to_SPY x SPY mu = 1.7200 x +0.50% = +0.86%; no +/-1.5pp adjustment applied (known formula defect disclosed in 03/13, not silently overridden). | DERIVED | DERIVED | 03, 09, 15 |
| L042 | core ETF market forecast — SOXX | SOXX | entry 516.23, mu +1.82%, sigma 18.58%, beta 3.6474 | mixed | 2026-07-27 | rules.md § Core ETF Market Forecast; inputs L002, L003, L013, L015; beta_to_SPY x SPY mu = 3.6474 x +0.50% = +1.82%; no +/-1.5pp adjustment applied (known formula defect disclosed in 03/13, not silently overridden). | DERIVED | DERIVED | 03, 09, 15 |
| L043 | canonical settlement ledger | all models, all vintages | 540 candidate rows → 260 EQ + 48 MF canonical, 0 conflicts, due 0 | count | 2026-07-27 | settlement_ledger.py --as-of 2026-07-28 | DERIVED | OBSERVED | 02 § 0, 13 |
| L044 | rolling calibration metrics | canonical settlements | EQ: hit 50.77%, CI 74.62%, mean z -0.1973, n 260, eff_n 1; MF: hit 20.83%, CI 68.75%, mean z -0.6872, n 48, eff_n 1; weighted-mean rank IC -0.1715 | mixed | 2026-07-27 | settlement_manifest.json rolling_metrics | DERIVED | OBSERVED | 02 § 0, 05 calibration binding, 13 |
| L045 | MoM baseline selection | gpt-5-2026-06-30 | CROSS_MODEL_BASELINE, 28d old, exact target hit; tie with claude-opus-4-8-2026-06-30 resolved and BOTH computed (81 field differences) | path | 2026-07-27 | agents.md § Orchestrator Step 2 | DERIVED | INFERRED | 00, 02 |
| L046 | Fundamental family | universe-wide | `UNAVAILABLE` — no fetch path wired at universe scale | z | 2026-07-27 | rules.md § SHADOW Diagnostic Tooling; Phase 2 of the 2026-07-15 plan not attempted | UNAVAILABLE | UNAVAILABLE | 05 Fund_Z, evidence threshold #2, DQ |
| L047 | Sentiment / Positioning family | universe-wide | `UNAVAILABLE` — no short-interest, options, revision or ownership feed | z | 2026-07-27 | rules.md § SHADOW Diagnostic Tooling | UNAVAILABLE | UNAVAILABLE | 05 Sent_Z, evidence threshold #2, DQ |
| L048 | Enhancing input block | universe-wide | IV/skew, short interest, bid-ask tape, revision tape, ownership flow all `UNAVAILABLE` | mixed | 2026-07-27 | rules.md § Input Classification — caps confidence and gross exposure, never blocks GO | UNAVAILABLE | UNAVAILABLE | 00 GO-gate, 05 DQ, 08 |
| L049 | portfolio feasibility pre-check | 103-name ≥80th-pctl pool | max attainable sleeve beta 0.899853 vs floor 0.90 ⇒ short by 0.000147 | beta | 2026-07-27 | mean of the 20 highest betas (5% cap ⇒ ≥20 names); inputs L015, L039; agents.md § Portfolio Construction Task 0 | DERIVED | DERIVED | 00, 07, 08, 09 |
| L050 | pairwise correlation matrix | top-10 published sleeve | average pairwise correlation 0.1931 vs cap 0.45 — PASS | corr | 2026-07-27 | 60-day adjusted daily returns; inputs L003 | DERIVED | DERIVED | 07, 08 |
| L051 | sleeve sigma and 95th-pctl 1-month drawdown | top-10 published sleeve, equal weight | sigma_1m 4.59%, dd95 7.57% vs cap 8% — PASS | pct | 2026-07-27 | dd95 = 1.65 × portfolio_sigma_1m (normality stated); inputs L003, L050 | DERIVED | DERIVED | 07, 08 |
| L052 | sector concentration | 24 published names | Consumer Discretionary 2; Consumer Staples 1; Energy 1; Finance 7; Health Care 3; Industrials 8; Real Estate 2 | count | 2026-07-27 | sector_manifest.json; inputs L009 | DERIVED | DERIVED | 07, 08 |
| L053 | disclosed judgment — defensive Macro polarity | 514 names | lower beta, lower realized vol and shallower drawdown score BETTER this run | polarity | 2026-07-27 | regime-conditional reading of L015/L013/L017 under a NEUTRAL rotation (41.44% of the universe at negative beta); NOT a family-weight change | DERIVED | INFERRED | 05, 08 |
| L054 | ex-dividend basis artifact | PAYX (published), FAST, ASML | PAYX raw close 115.48 vs adjusted 114.29 (1.030% gap) — CNBC reports the DIVIDEND-ADJUSTED prior close, Nasdaq and stockanalysis `c` report the actual 115.48 | USD | 2026-07-27 | 3 of 519 symbols carry an ex-date on 2026-07-28; entry price uses the unadjusted close per the 2026-07-26 rule, corroborated by Nasdaq to the cent (L005) | HISTORICAL | OBSERVED | 02, 05, 08, 15 |
| L055 | eff_n projection | canonical settlement pool | all 308 canonical settlements span only 20 days (2026-07-08 → 2026-07-28), shorter than the 28-day window itself ⇒ eff_n is pinned at 1; next window opens 2026-08-05, first qualifying target date 2026-08-05 (43 pending) | date | 2026-07-27 | derived from settlement_manifest.json canonical target dates and the outstanding prediction inventory across all packages | DERIVED | DERIVED | 02 § 0, 13 |

## Coverage

| claim_type | rows |
|---|---|
| `OBSERVED` | 15 |
| `DERIVED` | 33 |
| `INFERRED` | 4 |
| `UNAVAILABLE` | 3 |
| `ILLUSTRATIVE` | 0 |
| **total** | **55** |

No metric contributes to `Adj Score`, a penalty, a confidence label or a sizing decision without a row
above. `Fund_Z` and `Sent_Z` are recorded as `UNAVAILABLE` (L046, L047) and enter the score arithmetic
as `0.00` **labelled `UNAVAILABLE`** — never as a neutral or supportive contribution.
