# 04 Universe Summary

## Construction

Sampled-universe protocol was used because no full U.S. equity screening feed is wired. The universe starts with carry-forward names sourceable in this environment, adds 2-3 large liquid names from each GICS sector, and includes current theme-watchlist names in AI infrastructure, capital markets, electrification, copper, and defensive health care.

| Sector | Members | Count |
| --- | --- | --- |
| Communication Services | GOOGL, META, NFLX | 3 |
| Consumer Discretionary | AMZN, TSLA, HD | 3 |
| Consumer Staples | COST, WMT, PG | 3 |
| Energy | XOM, CVX | 2 |
| Financials | JPM, BAC, GS, V | 4 |
| Health Care | LLY, UNH, JNJ | 3 |
| Industrials | CAT, GE, ETN | 3 |
| Information Technology | AAPL, MSFT, NVDA, AVGO, NOW | 5 |
| Materials | LIN, SHW, FCX | 3 |
| Real Estate | PLD, EQIX, CCI | 3 |
| Utilities | NEE, SO, DUK | 3 |

## Inclusion / Exclusion Log

All 35 sampled equities passed the U.S. listing, price > $5, and 20d average dollar-volume > $20M filters. No sampled name had unresolved corporate-action ambiguity in the fetched source rows.

| Ticker | Company | Adj Score | Reason |
| --- | --- | --- | --- |
| NVDA | NVIDIA | 41.2 | Below top-20 sampled score cut; retained in universe but not forecast. |
| DUK | Duke Energy | 38.2 | Below top-20 sampled score cut; retained in universe but not forecast. |
| PLD | Prologis | 35.3 | Below top-20 sampled score cut; retained in universe but not forecast. |
| NEE | NextEra Energy | 32.4 | Below top-20 sampled score cut; retained in universe but not forecast. |
| JNJ | Johnson & Johnson | 29.4 | Below top-20 sampled score cut; retained in universe but not forecast. |
| CCI | Crown Castle | N/A - below cut | Below top-20 sampled score cut; retained in universe but not forecast. |
| META | Meta Platforms | 23.5 | Below top-20 sampled score cut; retained in universe but not forecast. |
| WMT | Walmart | 20.6 | Below top-20 sampled score cut; retained in universe but not forecast. |
| AMZN | Amazon | 17.6 | Below top-20 sampled score cut; retained in universe but not forecast. |
| MSFT | Microsoft | 14.7 | Below top-20 sampled score cut; retained in universe but not forecast. |
| TSLA | Tesla | 11.8 | Below top-20 sampled score cut; retained in universe but not forecast. |
| XOM | Exxon Mobil | 8.8 | Below top-20 sampled score cut; retained in universe but not forecast. |
| COST | Costco | 5.9 | Below top-20 sampled score cut; retained in universe but not forecast. |
| NOW | ServiceNow | 2.9 | Below top-20 sampled score cut; retained in universe but not forecast. |
| NFLX | Netflix | 0.0 | Below top-20 sampled score cut; retained in universe but not forecast. |

## Metric Coverage Summary

| Metric Group | Sourceable Count | UNAVAILABLE Count | DQ / Confidence Effect | Notes |
| --- | --- | --- | --- | --- |
| Risk / return | 35 | 0 | Used in ranking diagnostics | Sharpe, Sortino, IR, Kelly, VaR, CVaR, beta, drawdown derived from fetched price history. |
| Technical / price | 35 | 0 | Used in Tech_Z | 20d/60d momentum, relative strength, MA alignment, volume confirmation, TD-9. |
| Fundamental / quality proxy | 35 | 0 | Used in Fund_Z | Nasdaq EPS surprise plus realized-risk quality proxies are sourceable for the sampled universe. |
| Sentiment / positioning proxy | 35 | 0 | Partial support only | Uses EPS surprise and price/volume confirmation; true analyst/short/options feeds unavailable. |
| Enhancing feeds | 0 | 35 | Confidence capped at MEDIUM | Options IV/skew, borrow, bid-ask, analyst revisions, institutional flow unavailable. |

## Handoff

Proceed to factor scoring with sampled percentiles labeled `SAMPLED_PCTL (n=35)`. Missing enhancing inputs reduce confidence but do not block `GO`; portfolio construction may still reject the book if protected risk constraints fail.
