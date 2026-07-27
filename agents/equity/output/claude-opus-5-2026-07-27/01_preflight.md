# 01 Preflight — Source Ledger — 2026-07-27

Published before reflection, scoring, portfolio construction, or risk review used any fact
downstream. Schema and allowed enumerations: `rules.md § Source Ledger Contract`.

## Run Context

- Run fired **2026-07-27T09:55-04:00** — intraday Monday, 2026-07-27 session in progress.
- Last completed session: **2026-07-24**.
- Data mode `DELAYED`. Entry basis = 2026-07-24 unadjusted close (L002); return/indicator basis =
  2026-07-24 adjusted close (L003); live 2026-07-27 tape = observation only (L050, L051).

## Price Sourcing Standard — Gate Result

`rules.md § Price Sourcing Standard` requires either a connected market-data tool **or** two
independent web sources agreeing within 1%. **Both were satisfied.**

| Check | Result |
|---|---|
| Symbols verified | 28 (24 published + SPY, QQQ, SOXX, TLT) |
| Source A | stockanalysis.com 5Y history, field `c` (L002) |
| Source B | CNBC restQuote `previous_day_closing` (L004) |
| Exact to the cent | 27 of 28 |
| Max divergence | 0.396451% (BNY) |
| All within 1% | **True** |
| Brokerage-tool confirmation | SPY 738.93, QQQ 684.23, SOXX 527.01 — all exact (L005–L007) |

**Why `previous_day_closing` is the right CNBC field today.** The 2026-07-24 package logged a gotcha:
on a *post-close* run, `previous_day_closing` returns T−1 and manufactures fake disagreements, so
`last` gated on `last_time == run_date` must be used. **That inverts for an intraday fire.** With
`curmktstatus = REG_MKT` and `last_time = 2026-07-27T10:09:35.973-0400`, CNBC's `last` is the live
2026-07-27 tape and `previous_day_closing` *is* the 2026-07-24 official close — which is exactly the basis
this run needs. Both fields were captured; each is used for its own purpose and neither is
substituted for the other.

**BNY, the one non-exact symbol.** CNBC reports
`previous_day_closing` 158.28 against the stockanalysis close
158.91, a 0.396451% gap. CNBC's
own `last` for the name equals 158.91 — i.e. the 2026-07-24 close —
so the name had not printed on the 2026-07-27 tape when the snapshot was taken and CNBC's prior-close
field is carrying a stale reference. The independently-run `gpt-5-2026-07-27` package reported the
identical 0.396451% BNY divergence, so this is a reproducible vendor artifact, not a fetch error. It
is far inside the 1% gate; the stockanalysis close is used, and BNY is excluded from the live
intraday observation in `10`.

## Source Ledger

| artifact | field | ticker/entity | value | unit | observation_date | source | freshness_tag | claim_type | used_by |
|---|---|---|---|---|---|---|---|---|---|
| L001 | index_union_count | S&P500 ∪ NDX100 | 515 | tickers | 2026-07-27 | build_index_universe.py -> universe_summary.json (caches fetched_at 2026-06-21T21:05:56Z) | HISTORICAL | OBSERVED | 03, 04, 05 percentile base |
| L002 | close_raw | 515 universe symbols + 4 ETFs | per-symbol | USD | 2026-07-24 | stockanalysis.com/api/symbol/{s|e}/{SYM}/history?range=5Y field c; retrieved_at 2026-07-27T13:57Z | HISTORICAL | OBSERVED | entry_price / target_price / CI bounds (05, 06, 07, 09, 15) |
| L003 | close_adjusted | 515 universe symbols + 4 ETFs | per-symbol | USD | 2026-07-24 | stockanalysis.com/api/symbol/{s|e}/{SYM}/history?range=5Y field a; retrieved_at 2026-07-27T13:57Z | HISTORICAL | OBSERVED | ALL return/indicator math: momentum, RS, vol, downside vol, beta, TE, drawdown, technical_indicators.py input (Track B accepted 2026-07-26) |
| L004 | previous_day_closing | 28 published + ETF symbols | per-symbol | USD | 2026-07-24 | CNBC restQuote previous_day_closing; retrieved_at 2026-07-27T10:09:35.853610-04:00 | DELAYED | OBSERVED | independent 2nd source for the Price Sourcing Standard (01, 08) |
| L005 | prior_close_derived | SPY | 738.93 | USD | 2026-07-24 | IBKR MCP get_price_snapshot conid 756733: last 741.84 - change 2.91 (prior-close object empty during RTH); retrieved_at 2026-07-27T10:09-04:00 | LIVE | DERIVED | brokerage-tool confirmation of the SPY entry basis (01, 03, 08) |
| L006 | prior_close_derived | QQQ | 684.23 | USD | 2026-07-24 | IBKR MCP get_price_snapshot conid 320227571: last 685.32 - change 1.09 | LIVE | DERIVED | brokerage-tool confirmation of the QQQ entry basis (01, 03) |
| L007 | prior_close_derived | SOXX | 527.01 | USD | 2026-07-24 | IBKR MCP get_price_snapshot conid 12658194: last 517.24 - change (-9.77) | LIVE | DERIVED | brokerage-tool confirmation of the SOXX entry basis (01, 03) |
| L008 | vix_close | ^VIX | 18.58 | index | 2026-07-24 | cdn.cboe.com/api/global/us_indices/daily_prices/VIX_History.csv | HISTORICAL | OBSERVED | regime classification (03) |
| L009 | risk_free_13w | US T-bill | 3.81 | % annual | 2026-07-24 | home.treasury.gov daily_treasury_bill_rates 2026 (13 WEEKS BANK DISCOUNT) | HISTORICAL | OBSERVED | rf_1m = annual/12 in Sharpe / Sortino / Treynor / Calmar (05) |
| L010 | market_cap | 514 scoreable names | > $2B for all | USD | 2026-07-27 | api.nasdaq.com/api/screener/stocks?tableonly=true&limit=10000&download=true | DELAYED | OBSERVED | universe inclusion filter (04) |
| L011 | sector / industry | 514 scoreable names | GICS-style label | text | 2026-07-27 | api.nasdaq.com/api/screener/stocks?tableonly=true&limit=10000&download=true fields sector, industry | DELAYED | OBSERVED | sector concentration + thesis labels (05, 06, 07) |
| L012 | daily_bars_5y | 519 symbols | 1255 max / 40 min bars | bars | 2026-07-24 | stockanalysis.com/api/symbol/{s|e}/{SYM}/history?range=5Y; 519/519 fetched in 26.6s at 8 workers; see price_history_fetch_manifest.json | HISTORICAL | OBSERVED | every derived metric in 05, 07 |
| L013 | sigma_30d (REALIZED_VOL_30D) | 514 names + 4 ETFs | per-name | decimal | 2026-07-24 | DERIVED: stdev(last 30 daily returns of L003) x sqrt(21) | HISTORICAL | DERIVED | sigma, CI bounds, VaR/CVaR, Kelly, Sharpe, Macro_Z (05, 15) |
| L014 | downside_sigma_30d | 514 names | per-name | decimal | 2026-07-24 | DERIVED: stdev(negative daily returns in last 30 of L003) x sqrt(21) | HISTORICAL | DERIVED | Sortino (05) |
| L015 | beta_60d | 514 names + 4 ETFs | per-name | ratio | 2026-07-24 | DERIVED: OLS slope of daily returns vs SPY over trailing 60 sessions, from L003 | HISTORICAL | DERIVED | Macro_Z, Treynor, ETF mu, portfolio feasibility (05, 07) |
| L016 | tracking_error_1m | 514 names | per-name | decimal | 2026-07-24 | DERIVED: stdev(r_i - beta*r_SPY) over 60 sessions x sqrt(21), from L003, L015 | HISTORICAL | DERIVED | Information Ratio (05) |
| L017 | max_drawdown_60d | 514 names + 4 ETFs | per-name | decimal | 2026-07-24 | DERIVED: worst peak-to-trough over the last 60 bars of L003 | HISTORICAL | DERIVED | Macro_Z, Calmar, tail-risk drivers (05) |
| L018 | adv20_usd | 514 names | per-name | USD | 2026-07-24 | DERIVED: mean(raw close x volume) over last 20 bars, from L002, L012 | HISTORICAL | DERIVED | liquidity inclusion filter (04) |
| L019 | technical pack — daily | 518 symbols | TD9/RSI14/MACD/MA/mom/vol/RS | mixed | 2026-07-24 | technical_indicators.py --history-dir <adjusted-close CSVs from L003> -> technical_indicators.json (generated_at 2026-07-27T13:58:39Z) | HISTORICAL | DERIVED | Tech_Z inputs and all displayed indicator states (05, 06, 09) |
| L020 | technical pack — weekly | 518 symbols | TD9/RSI14/MACD/MA | mixed | 2026-07-24 | technical_indicators.json weekly block (same run as L019) | HISTORICAL | DERIVED | Tech_Z (MA + MACD weekly), displayed W states (05) |
| L021 | technical pack — monthly | 518 symbols | TD9/RSI14/MACD/MA | mixed | 2026-07-24 | technical_indicators.json monthly block (same run as L019) | HISTORICAL | DERIVED | displayed M states (05, 06); not a Tech_Z input |
| L022 | next_earnings_date — pass 1 | top 40 pre-earnings ranks | 40 names | date | 2026-07-27 | api.nasdaq.com/api/analyst/{sym}/earnings-date (data.announcement / data.reportText) | DELAYED | OBSERVED | 14-day earnings penalty (05) |
| L023 | next_earnings_date — pass 2 | ALL, VTRS, AJG, AFL | 4 names | date | 2026-07-27 | same endpoint as L022; post-penalty top-20 entrants | DELAYED | OBSERVED | 14-day earnings penalty (05) |
| L024 | next_earnings_date — pass 3 | WAB EQR ABBV PKG HST CVS MRK IQV CPAY AIZ BNY PFG MTB | 13 names | date | 2026-07-27 | same endpoint as L022; second-round top-20 entrants | DELAYED | OBSERVED | 14-day earnings penalty (05) |
| L025 | next_earnings_date — retries | CB DGX EG HST MRK PKG | 6 names | date | 2026-07-27 | same endpoint as L022; transient DNS/network failures re-fetched to resolution | DELAYED | OBSERVED | 14-day earnings penalty (05) |
| L026 | vendor_empty_resolution | CB EQR HIG MTB OKE PFG WRB | ESTIMATED_PRINT_WEEK (±5d) | rule | 2026-07-27 | INFERRED: vendor-empty AND no >=3.5% 1-day move in the last 12 sessions -> conservative penalized branch (rule tightened 2026-07-26 to require the price move, not volume alone) | DELAYED | INFERRED | earnings penalty on the buffered window (05) |
| L027 | mu | 206 ranked names | per-name +1.0% .. +6.0% | % | 2026-07-27 | rules.md § mu Calibration Table band for the name pctl; NO per-name adjustment applied | HISTORICAL | DERIVED | target price, CI, Sharpe, Kelly, VaR (05, 15) |
| L028 | target_price | 206 ranked names | per-name | USD | 2026-07-27 | DERIVED: entry_price (L002) x (1 + mu (L027)) | HISTORICAL | DERIVED | 05, 06, 15 |
| L029 | ci70_lo / ci70_hi | 206 ranked names | per-name | USD | 2026-07-27 | DERIVED: entry (L002) x (1 + mu (L027) ± 1.04 x sigma (L013)) | HISTORICAL | DERIVED | 05, 06, 15 |
| L030 | Sharpe / Sortino / IR / Treynor / Calmar | 206 ranked names | per-name | ratio | 2026-07-27 | DERIVED per rules.md § Ratio Definitions from L013, L014, L015, L016, L017, L027, rf_1m from L009 | HISTORICAL | DERIVED | 05, 06, 15 |
| L031 | VaR95 / CVaR95 | 206 ranked names | per-name | decimal | 2026-07-27 | DERIVED: mu - 1.65 sigma / mu - 2.06 sigma (normality assumed) from L013, L027 | HISTORICAL | DERIVED | 05, 06, 15 |
| L032 | kelly_raw / 0.25 Kelly | 206 ranked names | per-name | NAV fraction | 2026-07-27 | DERIVED: mu / sigma^2 and 0.25x, capped at the 5% single-name limit, from L013, L027 | HISTORICAL | DERIVED | investability gate, sizing, confidence cap (05, 07) |
| L033 | Tech_Z | 514 names | per-name | z-score | 2026-07-27 | DERIVED: 8 signals (mom20, mom60, RS20, RS60, MA align D+W, MACD state D+W, vol ratio 20d, RSI headroom 70-RSI14_d) from L019, L020; each winsorized at the 5th/95th pctl over the 514-name universe, z-scored, equal-weighted | HISTORICAL | DERIVED | Adj Score (05) |
| L034 | Macro_Z | 514 names | per-name | z-score | 2026-07-27 | DERIVED: 3 signals — beta_60d (L015, polarity −), sigma_30d (L013, polarity −), max_dd_60d (L017, polarity +); winsorized 5th/95th, z-scored, equal-weighted | HISTORICAL | DERIVED | Adj Score (05) |
| L035 | data_quality_multiplier | 514 names | 0.8 | multiplier | 2026-07-27 | rules.md § Data Quality Multiplier "0.80 for notable coverage gaps": 2 of 4 families UNAVAILABLE plus the entire Enhancing block | HISTORICAL | INFERRED | Adj Score; independently fails Evidence Threshold #4 (05, 08) |
| L036 | penalty — earnings <= 14d buffered | 40 names | -0.1 | score | 2026-07-27 | rules.md § Risk Controls, applied on the buffered window from L022-L026 | DELAYED | DERIVED | Adj Score, confidence cap LOW (05) |
| L037 | penalty — 30d RVol > 2x median | 31 names | -0.05 | score | 2026-07-27 | rules.md § Risk Controls; universe median sigma 0.0961, threshold 0.1922, from L013 | HISTORICAL | DERIVED | Adj Score (05) |
| L038 | penalty — TD9 sell-setup 9 + RSI14_d >= 70 | 4 names | -0.05 | score | 2026-07-27 | rules.md § TD-9 Definition (exhaustion confirmed by price action), from L019 | HISTORICAL | DERIVED | Adj Score (05) |
| L039 | pctl (INDEX_UNION_PCTL) | 514 names | per-name | percentile | 2026-07-27 | DERIVED: (n - rank)/(n - 1) x 100 over n=514 scoreable names, post-penalty | HISTORICAL | DERIVED | mu band, Evidence Threshold #1 (05) |
| L040 | ETF analysis block — SPY | SPY | trend/vol/dd/RS | mixed | 2026-07-24 | DERIVED from L002, L003, L013, L015, L017, L019 | HISTORICAL | DERIVED | Core ETF Market Forecast (03, 09, 15) |
| L041 | ETF analysis block — QQQ | QQQ | trend/vol/dd/RS | mixed | 2026-07-24 | DERIVED from L002, L003, L013, L015, L017, L019 | HISTORICAL | DERIVED | Core ETF Market Forecast (03, 09, 15) |
| L042 | ETF analysis block — SOXX | SOXX | trend/vol/dd/RS | mixed | 2026-07-24 | DERIVED from L002, L003, L013, L015, L017, L019 | HISTORICAL | DERIVED | Core ETF Market Forecast (03, 09, 15) |
| L043 | ETF analysis block — TLT | TLT | trend/vol/dd | mixed | 2026-07-24 | DERIVED from L002, L003, L013, L017 | HISTORICAL | DERIVED | regime cross-check only — not a forecast sleeve member (03) |
| L044 | canonical settlement ledger + rolling metrics | all models, all packages | EQ n=231 eff_n=1 / MF n=42 eff_n=1 | counts | 2026-07-27 | settlement_ledger.py --output-dir agents/equity/output --as-of 2026-07-27 -> settlement_manifest.json | HISTORICAL | DERIVED | Reflection § 0, calibration feedback binding, 13 |
| L045 | MoM baseline folder | gpt-5-2026-06-29 | CROSS_MODEL_BASELINE | path | 2026-07-27 | agents.md § Orchestrator Step 2: window 2026-06-12..2026-07-06, target 2026-06-29; no claude-opus-5 folder in window (all 3 are < 21d old) | HISTORICAL | OBSERVED | 02 § 1-5, 00 |
| L046 | Fund_Z | 514 names | UNAVAILABLE | z-score | 2026-07-27 | No fetch path wired at universe scale. rules.md § SHADOW Diagnostic Tooling: fundamental_diagnostics.py is SHADOW-gated and covered ~4.7% of the universe on 2026-07-16, far below the 70%-of-universe bar; Phase 2 bulk fetch not attempted | UNAVAILABLE | UNAVAILABLE | Evidence Threshold #2 failure (05, 08) |
| L047 | Sent_Z | 514 names | UNAVAILABLE | z-score | 2026-07-27 | No fetch path wired at universe scale; sentiment_diagnostics.py is SHADOW-gated, same 70%-coverage bar as L046 | UNAVAILABLE | UNAVAILABLE | Evidence Threshold #2 failure (05, 08) |
| L048 | Enhancing input block | universe | UNAVAILABLE | mixed | 2026-07-27 | Options IV/skew, short interest/borrow, bid-ask tape, analyst revision tape, institutional flow: no feed wired. rules.md § Input Classification — caps confidence and gross exposure, never blocks GO | UNAVAILABLE | UNAVAILABLE | DQ multiplier, confidence cap (05, 08) |
| L049 | portfolio beta feasibility | pctl>=80 pool (n=103) | 0.8519 | portfolio beta | 2026-07-27 | DERIVED: max attainable long-only portfolio beta under the 5% single-name cap = mean of the 20 highest betas in the pool (weights sum to 1.00), from L015 | HISTORICAL | DERIVED | Task-0 feasibility pre-check -> NO_TRADE (07, 08) |
| L050 | live intraday last | 28 published + ETF symbols | per-symbol | USD | 2026-07-27 | CNBC restQuote last, curmktstatus REG_MKT, last_time 2026-07-27T10:09:35.973-0400 | LIVE | OBSERVED | 10_midday_monitor observation only — never an entry/settle price |
| L051 | live intraday snapshot | SPY, QQQ, SOXX | last / change / volume | USD | 2026-07-27 | IBKR MCP get_price_snapshot, is_close false, ts 2026-07-27T10:09-04:00 | LIVE | OBSERVED | 10_midday_monitor observation only |
| L052 | regime classification | US equity market | NEUTRAL | label | 2026-07-24 | INFERRED from L008, L009, L040, L041, L042, L043; six evidence lines in 03 | HISTORICAL | INFERRED | SPY mu prior, Macro_Z polarity, 03, 09 |
| L053 | Macro_Z polarity — defensive | 514 names | lower beta / lower vol / shallower drawdown score better | polarity | 2026-07-27 | INFERRED regime-conditional reading of L052; NOT a family-weight change and NOT a permanent rule (Track A is gated off at eff_n=1) | HISTORICAL | INFERRED | Macro_Z sign convention (05) — disclosed because it shapes the leaderboard |
| L054 | settlement due inventory | all models | 0 | predictions | 2026-07-27 | L044: due_inventory 0, conflicts 0 — the gpt-5-2026-07-27 pre-open run settled all 34 keys that matured today before this run fired | HISTORICAL | OBSERVED | 02 § 0, 15 settlements block |
| L055 | market_cap | BF-B (Brown-Forman B) | UNAVAILABLE | USD | 2026-07-27 | api.nasdaq.com/api/screener/stocks?tableonly=true&limit=10000&download=true returns the BF/B row with an EMPTY marketCap field; stockanalysis quotes endpoint carries no market-cap field. Not estimated. | UNAVAILABLE | UNAVAILABLE | 04 inclusion-filter disclosure. BF-B ranks 412 of 514 (pctl 19.88), far below the 60th-pctl ranking floor, so the gap affects no published number. Retained rather than dropped because price and ADV20 both pass and the name is an S&P 500 constituent. |

## Coverage Summary

| Claim type | Rows | Freshness | Rows |
|---|---:|---|---:|
| `OBSERVED` | 17 | `LIVE` | 5 |
| `DERIVED` | 30 | `DELAYED` | 9 |
| `INFERRED` | 4 | `HISTORICAL` | 37 |
| `UNAVAILABLE` | 4 | `UNAVAILABLE` | 4 |
| `ILLUSTRATIVE` | 0 | `OFFICIAL_FILING` | 0 |

Four rows are `UNAVAILABLE` and each is material and disclosed rather than imputed: `Fund_Z` (L046),
`Sent_Z` (L047), the whole Enhancing block (L048), and BF-B's market cap (L055). Three rows are
`INFERRED` and each is judgment that is flagged where it acts: the vendor-empty earnings resolution
(L026), the regime label (L052), and the defensive `Macro_Z` polarity (L053).

**No metric contributes to `Adj Score`, a penalty, a confidence label, or a sizing decision without
a row above.** Missing metrics are recorded `UNAVAILABLE`; none is presented as neutral or supportive.
