# 01 Preflight

## Data Freshness and Coverage Summary

| Domain | Status | Freshness Tag | Notes |
|---|---|---|---|
| U.S. equity prices | Partial | DELAYED | Sampled tickers have source-backed current/delayed quote pages. |
| Prior MoM prices | Available | HISTORICAL | Baseline top-5 May 12 prices are available from historical price pages. |
| Benchmark price | Partial | DELAYED | SPY quote available; full index breadth unavailable. |
| Volatility regime | Partial | DELAYED | Cboe VIX data available; candidate-level IV/skew unavailable. |
| Rates regime | Partial | HISTORICAL | FRED DGS10 latest official observation is 2026-06-05. |
| Sector rotation | Partial | DELAYED | XLV and XLP quote pages support defensive-rotation inference. |
| Fundamentals | Partial | DELAYED | StockAnalysis company pages provide revenue, net income, EPS, beta, target, and earnings-date fields for sampled names. |
| Analyst revisions | Weak | DELAYED | Consensus targets and article snippets are available, but no full revision tape is wired. |
| Options skew / IV | Missing | UNAVAILABLE | Required for `GO`, unavailable for candidates. |
| Short interest / borrow | Incomplete | UNAVAILABLE | Some pages disclose short interest, but no complete, synchronized feed is wired. |
| Execution spread / market impact | Missing | UNAVAILABLE | No bid-ask or execution-quality feed. |
| Covariance / drawdown | Missing | UNAVAILABLE | No validated correlation or 95th percentile drawdown feed. |

## Validation Result

- Methodology check: PASS.
- Source ledger check: PASS for claims used in reflection and review-only scoring.
- Trade-readiness check: FAIL.
- Recommended run status: `REVIEW_ONLY`.

## Source Ledger

Required schema:

| artifact | field | ticker/entity | value | unit | observation_date | source | freshness_tag | claim_type | used_by |
|---|---|---|---|---|---|---|---|---|---|
| L001/03_regime | vix_spot | VIX | 19.55 | index points | 2026-06-09 | https://www.cboe.com/tradable-products/vix/ | DELAYED | OBSERVED | 03_regime_and_data, 09_final_report |
| L002/03_regime | vix_previous_close | VIX | 18.92 | index points | 2026-06-09 | https://www.cboe.com/tradable-products/vix/ | DELAYED | OBSERVED | 03_regime_and_data |
| L003/03_regime | ten_year_treasury | DGS10 | 4.55 | percent | 2026-06-05 | https://fred.stlouisfed.org/series/DGS10 | HISTORICAL | OBSERVED | 03_regime_and_data, 09_final_report |
| L004/03_regime | price_and_1d_change | SPY | 735.18; -0.55% | USD; percent | 2026-06-09 | https://stockanalysis.com/etf/spy/ | DELAYED | OBSERVED | 03_regime_and_data |
| L005/03_regime | price_and_1d_change | XLV | 154.91; +1.48% | USD; percent | 2026-06-09 | https://stockanalysis.com/etf/xlv/ | DELAYED | OBSERVED | 03_regime_and_data |
| L006/03_regime | price_and_1d_change | XLP | 83.90; +1.00% | USD; percent | 2026-06-09 | https://stockanalysis.com/etf/xlp/ | DELAYED | OBSERVED | 03_regime_and_data |
| L007/02_reflection | baseline_status | claude-opus-4-7-2026-05-12 | REVIEW_ONLY; ILLUSTRATIVE | status | 2026-05-12 | /Users/mac/my-code/diary/investments/equity/output/claude-opus-4-7-2026-05-12/00_run_manifest.md | HISTORICAL | OBSERVED | 02_reflection |
| L008/02_reflection | baseline_top5 | claude-opus-4-7-2026-05-12 | MSFT, NVDA, META, GOOGL, AMZN | tickers | 2026-05-12 | /Users/mac/my-code/diary/investments/equity/output/claude-opus-4-7-2026-05-12/04_factor_scores.md | HISTORICAL | OBSERVED | 02_reflection |
| L009/02_reflection | baseline_regime | claude-opus-4-7-2026-05-12 | NEUTRAL, low confidence placeholder | label | 2026-05-12 | /Users/mac/my-code/diary/investments/equity/output/claude-opus-4-7-2026-05-12/08_final_report.md | HISTORICAL | OBSERVED | 02_reflection |
| L010/02_reflection | baseline_portfolio | claude-opus-4-7-2026-05-12 | none; no investable set | text | 2026-05-12 | /Users/mac/my-code/diary/investments/equity/output/claude-opus-4-7-2026-05-12/08_final_report.md | HISTORICAL | OBSERVED | 02_reflection |
| L011/02_reflection | prior_close | MSFT | 407.77 | USD | 2026-05-12 | https://stockanalysis.com/stocks/msft/history/ | HISTORICAL | OBSERVED | 02_reflection |
| L012/02_reflection | current_price | MSFT | 404.25 | USD | 2026-06-09 | https://stockanalysis.com/stocks/msft/history/ | DELAYED | OBSERVED | 02_reflection |
| L013/02_reflection | mom_return | MSFT | -0.86 | percent | 2026-06-09 | formula: (L012/L011)-1 | DELAYED | DERIVED | 02_reflection |
| L014/02_reflection | prior_close | NVDA | 220.78 | USD | 2026-05-12 | https://stockanalysis.com/stocks/nvda/history/ | HISTORICAL | OBSERVED | 02_reflection |
| L015/02_reflection | current_price | NVDA | 206.84 | USD | 2026-06-09 | https://stockanalysis.com/stocks/nvda/history/ | DELAYED | OBSERVED | 02_reflection |
| L016/02_reflection | mom_return | NVDA | -6.31 | percent | 2026-06-09 | formula: (L015/L014)-1 | DELAYED | DERIVED | 02_reflection |
| L017/02_reflection | prior_close | META | 603.00 | USD | 2026-05-12 | https://stockanalysis.com/stocks/meta/history/ | HISTORICAL | OBSERVED | 02_reflection |
| L018/02_reflection | current_price | META | 589.64 | USD | 2026-06-09 | https://stockanalysis.com/stocks/meta/history/ | DELAYED | OBSERVED | 02_reflection |
| L019/02_reflection | mom_return | META | -2.22 | percent | 2026-06-09 | formula: (L018/L017)-1 | DELAYED | DERIVED | 02_reflection |
| L020/02_reflection | prior_close | GOOGL | 387.35 | USD | 2026-05-12 | https://stockanalysis.com/stocks/googl/history/ | HISTORICAL | OBSERVED | 02_reflection |
| L021/02_reflection | current_price | GOOGL | 365.92 | USD | 2026-06-09 | https://stockanalysis.com/stocks/googl/history/ | DELAYED | OBSERVED | 02_reflection |
| L022/02_reflection | mom_return | GOOGL | -5.53 | percent | 2026-06-09 | formula: (L021/L020)-1 | DELAYED | DERIVED | 02_reflection |
| L023/02_reflection | prior_close | AMZN | 265.82 | USD | 2026-05-12 | https://stockanalysis.com/stocks/amzn/history/ | HISTORICAL | OBSERVED | 02_reflection |
| L024/02_reflection | current_price | AMZN | 245.16 | USD | 2026-06-09 | https://stockanalysis.com/stocks/amzn/history/ | DELAYED | OBSERVED | 02_reflection |
| L025/02_reflection | mom_return | AMZN | -7.77 | percent | 2026-06-09 | formula: (L024/L023)-1 | DELAYED | DERIVED | 02_reflection |
| L030/05_scores | current_price | MCK | 783.75 | USD | 2026-06-09 | https://stockanalysis.com/stocks/mck/ | DELAYED | OBSERVED | 04_universe_summary, 05_factor_scores |
| L031/05_scores | beta | MCK | 0.32 | beta | 2026-06-09 | https://stockanalysis.com/stocks/mck/ | DELAYED | OBSERVED | 05_factor_scores, 07_portfolio_proposal |
| L032/05_scores | consensus_target | MCK | 949.73; Strong Buy | USD; rating | 2026-06-09 | https://stockanalysis.com/stocks/mck/ | DELAYED | OBSERVED | 05_factor_scores |
| L033/05_scores | earnings_date | MCK | 2026-05-07 | date | 2026-06-09 | https://stockanalysis.com/stocks/mck/ | DELAYED | OBSERVED | 05_factor_scores |
| L034/05_scores | fundamentals_snapshot | MCK | revenue +12.4%; net income +44.5%; EPS +49.2% | percent | 2026-06-09 | https://stockanalysis.com/stocks/mck/ | DELAYED | OBSERVED | 05_factor_scores |
| L035/05_scores | current_price | PG | 148.30 | USD | 2026-06-09 | https://stockanalysis.com/stocks/pg/ | DELAYED | OBSERVED | 04_universe_summary, 05_factor_scores |
| L036/05_scores | beta | PG | 0.38 | beta | 2026-06-09 | https://stockanalysis.com/stocks/pg/ | DELAYED | OBSERVED | 05_factor_scores, 07_portfolio_proposal |
| L037/05_scores | consensus_target | PG | 163.77; Buy | USD; rating | 2026-06-09 | https://stockanalysis.com/stocks/pg/ | DELAYED | OBSERVED | 05_factor_scores |
| L038/05_scores | earnings_date | PG | 2026-07-28 | date | 2026-06-09 | https://stockanalysis.com/stocks/pg/ | DELAYED | OBSERVED | 05_factor_scores |
| L039/05_scores | fundamentals_snapshot | PG | revenue +3.3%; net income +7.2%; EPS +8.6% | percent | 2026-06-09 | https://stockanalysis.com/stocks/pg/ | DELAYED | OBSERVED | 05_factor_scores |
| L040/05_scores | current_price | WMT | 118.61 | USD | 2026-06-09 | https://stockanalysis.com/stocks/wmt/ | DELAYED | OBSERVED | 04_universe_summary, 05_factor_scores |
| L041/05_scores | beta | WMT | 0.60 | beta | 2026-06-09 | https://stockanalysis.com/stocks/wmt/ | DELAYED | OBSERVED | 05_factor_scores, 07_portfolio_proposal |
| L042/05_scores | consensus_target | WMT | 137.93; Strong Buy | USD; rating | 2026-06-09 | https://stockanalysis.com/stocks/wmt/ | DELAYED | OBSERVED | 05_factor_scores |
| L043/05_scores | earnings_date | WMT | 2026-05-21 | date | 2026-06-09 | https://stockanalysis.com/stocks/wmt/ | DELAYED | OBSERVED | 05_factor_scores |
| L044/05_scores | fundamentals_snapshot | WMT | revenue +5.9%; net income +20.8%; EPS +21.4% | percent | 2026-06-09 | https://stockanalysis.com/stocks/wmt/ | DELAYED | OBSERVED | 05_factor_scores |
| L045/05_scores | current_price | ABBV | 226.43 | USD | 2026-06-09 | https://stockanalysis.com/stocks/abbv/ | DELAYED | OBSERVED | 04_universe_summary, 05_factor_scores |
| L046/05_scores | beta | ABBV | 0.31 | beta | 2026-06-09 | https://stockanalysis.com/stocks/abbv/ | DELAYED | OBSERVED | 05_factor_scores, 07_portfolio_proposal |
| L047/05_scores | consensus_target | ABBV | 253.55; Buy | USD; rating | 2026-06-09 | https://stockanalysis.com/stocks/abbv/ | DELAYED | OBSERVED | 05_factor_scores |
| L048/05_scores | earnings_date | ABBV | 2026-04-29 | date | 2026-06-09 | https://stockanalysis.com/stocks/abbv/ | DELAYED | OBSERVED | 05_factor_scores |
| L049/05_scores | fundamentals_snapshot | ABBV | revenue +9.5%; net income -13.3%; EPS -13.2% | percent | 2026-06-09 | https://stockanalysis.com/stocks/abbv/ | DELAYED | OBSERVED | 05_factor_scores |
| L050/05_scores | current_price | JPM | 312.82 | USD | 2026-06-09 | https://stockanalysis.com/stocks/jpm/ | DELAYED | OBSERVED | 04_universe_summary, 05_factor_scores |
| L051/05_scores | beta | JPM | 1.00 | beta | 2026-06-09 | https://stockanalysis.com/stocks/jpm/ | DELAYED | OBSERVED | 05_factor_scores, 07_portfolio_proposal |
| L052/05_scores | consensus_target | JPM | 342.19; Buy | USD; rating | 2026-06-09 | https://stockanalysis.com/stocks/jpm/ | DELAYED | OBSERVED | 05_factor_scores |
| L053/05_scores | earnings_date | JPM | 2026-07-14 | date | 2026-06-09 | https://stockanalysis.com/stocks/jpm/ | DELAYED | OBSERVED | 05_factor_scores |
| L054/05_scores | fundamentals_snapshot | JPM | revenue +2.9%; net income -1.3%; EPS +2.4% | percent | 2026-06-09 | https://stockanalysis.com/stocks/jpm/ | DELAYED | OBSERVED | 05_factor_scores |
| L055/05_scores | current_price | XOM | 148.73 | USD | 2026-06-09 | https://stockanalysis.com/stocks/xom/ | DELAYED | OBSERVED | 04_universe_summary, 05_factor_scores |
| L056/05_scores | beta | XOM | 0.15 | beta | 2026-06-09 | https://stockanalysis.com/stocks/xom/ | DELAYED | OBSERVED | 05_factor_scores, 07_portfolio_proposal |
| L057/05_scores | consensus_target | XOM | 169.91; Buy | USD; rating | 2026-06-09 | https://stockanalysis.com/stocks/xom/ | DELAYED | OBSERVED | 05_factor_scores |
| L058/05_scores | earnings_date | XOM | 2026-05-01 | date | 2026-06-09 | https://stockanalysis.com/stocks/xom/ | DELAYED | OBSERVED | 05_factor_scores |
| L059/05_scores | fundamentals_snapshot | XOM | revenue -4.1%; net income -23.7%; EPS -21.3% | percent | 2026-06-09 | https://stockanalysis.com/stocks/xom/ | DELAYED | OBSERVED | 05_factor_scores |
| L060/05_scores | current_price | AZO | 3125.82 | USD | 2026-06-09 | https://stockanalysis.com/stocks/azo/ | DELAYED | OBSERVED | 04_universe_summary, 05_factor_scores |
| L061/05_scores | beta | AZO | 0.35 | beta | 2026-06-09 | https://stockanalysis.com/stocks/azo/ | DELAYED | OBSERVED | 05_factor_scores, 07_portfolio_proposal |
| L062/05_scores | consensus_target | AZO | 3937.61; Buy | USD; rating | 2026-06-09 | https://stockanalysis.com/stocks/azo/ | DELAYED | OBSERVED | 05_factor_scores |
| L063/05_scores | earnings_date | AZO | 2026-05-26 | date | 2026-06-09 | https://stockanalysis.com/stocks/azo/ | DELAYED | OBSERVED | 05_factor_scores |
| L064/05_scores | fundamentals_snapshot | AZO | revenue +5.7%; net income -3.3%; EPS -1.7% | percent | 2026-06-09 | https://stockanalysis.com/stocks/azo/ | DELAYED | OBSERVED | 05_factor_scores |
| L065/05_scores | current_price | UNH | 412.50 | USD | 2026-06-09 | https://stockanalysis.com/stocks/unh/ | DELAYED | OBSERVED | 04_universe_summary, 05_factor_scores |
| L066/05_scores | beta | UNH | 0.65 | beta | 2026-06-09 | https://stockanalysis.com/stocks/unh/ | DELAYED | OBSERVED | 05_factor_scores, 07_portfolio_proposal |
| L067/05_scores | consensus_target | UNH | 407.38; Buy | USD; rating | 2026-06-09 | https://stockanalysis.com/stocks/unh/ | DELAYED | OBSERVED | 05_factor_scores |
| L068/05_scores | earnings_date | UNH | 2026-07-28 | date | 2026-06-09 | https://stockanalysis.com/stocks/unh/ | DELAYED | OBSERVED | 05_factor_scores |
| L069/05_scores | fundamentals_snapshot | UNH | revenue +9.7%; net income -45.5%; EPS -44.4% | percent | 2026-06-09 | https://stockanalysis.com/stocks/unh/ | DELAYED | OBSERVED | 05_factor_scores |
| L070/04_universe | current_price | CAT | 913.06 | USD | 2026-06-09 | https://stockanalysis.com/stocks/cat/ | DELAYED | OBSERVED | 04_universe_summary |
| L071/04_universe | beta | CAT | 1.60 | beta | 2026-06-09 | https://stockanalysis.com/stocks/cat/ | DELAYED | OBSERVED | 04_universe_summary |
| L072/04_universe | consensus_target | CAT | 936.99; Buy | USD; rating | 2026-06-09 | https://stockanalysis.com/stocks/cat/ | DELAYED | OBSERVED | 04_universe_summary |
| L073/04_universe | earnings_date | CAT | 2026-04-30 | date | 2026-06-09 | https://stockanalysis.com/stocks/cat/ | DELAYED | OBSERVED | 04_universe_summary |
| L074/04_universe | fundamentals_snapshot | CAT | revenue +11.9%; net income -5.1%; EPS -2.1% | percent | 2026-06-09 | https://stockanalysis.com/stocks/cat/ | DELAYED | OBSERVED | 04_universe_summary |
| L075/04_universe | current_price | GS | 1030.52 | USD | 2026-06-09 | https://stockanalysis.com/stocks/gs/ | DELAYED | OBSERVED | 04_universe_summary |
| L076/04_universe | beta | GS | 1.29 | beta | 2026-06-09 | https://stockanalysis.com/stocks/gs/ | DELAYED | OBSERVED | 04_universe_summary |
| L077/04_universe | consensus_target | GS | 947.60; Hold | USD; rating | 2026-06-09 | https://stockanalysis.com/stocks/gs/ | DELAYED | OBSERVED | 04_universe_summary |
| L078/04_universe | earnings_date | GS | 2026-07-14 | date | 2026-06-09 | https://stockanalysis.com/stocks/gs/ | DELAYED | OBSERVED | 04_universe_summary |
| L079/04_universe | fundamentals_snapshot | GS | revenue +16.0%; net income +21.4%; EPS +27.1% | percent | 2026-06-09 | https://stockanalysis.com/stocks/gs/ | DELAYED | OBSERVED | 04_universe_summary |
| L090/08_risk | options_iv_skew | candidate universe | UNAVAILABLE | text | 2026-06-09 | no connected options feed | UNAVAILABLE | UNAVAILABLE | 05_factor_scores, 08_risk_review |
| L091/08_risk | full_short_interest_borrow_feed | candidate universe | UNAVAILABLE | text | 2026-06-09 | no synchronized borrow/short-interest feed | UNAVAILABLE | UNAVAILABLE | 05_factor_scores, 08_risk_review |
| L092/08_risk | execution_spread_liquidity | candidate universe | UNAVAILABLE | text | 2026-06-09 | no bid-ask/execution-quality feed | UNAVAILABLE | UNAVAILABLE | 07_portfolio_proposal, 08_risk_review |
| L093/08_risk | covariance_drawdown_model | candidate universe | UNAVAILABLE | text | 2026-06-09 | no validated covariance/drawdown feed | UNAVAILABLE | UNAVAILABLE | 07_portfolio_proposal, 08_risk_review |
| L100/05_scores | review_adjusted_score | MCK | 0.74 | score | 2026-06-09 | inferred from L030-L034, L005, L090-L093 | DELAYED | INFERRED | 05_factor_scores |
| L101/05_scores | review_adjusted_score | PG | 0.72 | score | 2026-06-09 | inferred from L035-L039, L006, L090-L093 | DELAYED | INFERRED | 05_factor_scores |
| L102/05_scores | review_adjusted_score | WMT | 0.69 | score | 2026-06-09 | inferred from L040-L044, L006, L090-L093 | DELAYED | INFERRED | 05_factor_scores |
| L103/05_scores | review_adjusted_score | ABBV | 0.68 | score | 2026-06-09 | inferred from L045-L049, L005, L090-L093 | DELAYED | INFERRED | 05_factor_scores |
| L104/05_scores | review_adjusted_score | JPM | 0.65 | score | 2026-06-09 | inferred from L050-L054, L003, L090-L093 | DELAYED | INFERRED | 05_factor_scores |
| L105/05_scores | review_adjusted_score | XOM | 0.62 | score | 2026-06-09 | inferred from L055-L059, geopolitical/oil hedge context and L090-L093 | DELAYED | INFERRED | 05_factor_scores |
| L106/05_scores | review_adjusted_score | AZO | 0.59 | score | 2026-06-09 | inferred from L060-L064, target-cut news from source page, L090-L093 | DELAYED | INFERRED | 05_factor_scores |
| L107/05_scores | review_adjusted_score | UNH | 0.56 | score | 2026-06-09 | inferred from L065-L069 and recent upgrade snippets on source page | DELAYED | INFERRED | 05_factor_scores |

## Handoff to Reflection

Proceed with `CROSS_MODEL_BASELINE`. Because the prior baseline was itself `REVIEW_ONLY` and `ILLUSTRATIVE`, its names can inform process reflection but cannot be treated as a prior live portfolio.
