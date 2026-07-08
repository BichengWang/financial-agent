# 04 Universe Summary

Run `claude-opus-4-8` · 2026-06-30 · Sampled Universe Protocol (no full-screen feed wired).

## Construction

Per `rules.md § Sampled Universe Protocol`: (1) carry-forward `CARRY` names from `02_reflection.md` (LLY, UNH, GE, LIN); (2) the 2–4 largest liquid S&P 500 names from each of the 11 GICS sectors; (3) theme-watchlist names with a stated catalyst (PLTR — AI/gov software; MU — memory up-cycle). **35 equities**, all with grounded prices and liquidity. Percentiles are labeled `SAMPLED_PCTL (n=35)`. ETFs SPY/QQQ/SOXX are a separate forecast sleeve (03), not universe members.

| Sector | Count | Names |
|---|---|---|
| Information Technology | 8 | AAPL, MSFT, NVDA, AVGO, AMD, NOW, MU, PLTR |
| Communication Services | 3 | GOOGL, META, NFLX |
| Consumer Discretionary | 3 | AMZN, TSLA, HD |
| Consumer Staples | 3 | WMT, COST, PG |
| Financials | 4 | JPM, BAC, GS, V |
| Health Care | 3 | LLY, UNH, JNJ |
| Industrials | 3 | GE, CAT, RTX |
| Energy | 2 | XOM, CVX |
| Materials | 2 | LIN, FCX |
| Utilities | 2 | NEE, SO |
| Real Estate | 2 | PLD, AMT |

## Inclusion Log (all 35 INCLUDED)

Every name clears the inclusion filters (`rules.md § Universe Construction`): U.S. primary listing, market cap > $2B, 20d ADV > $20M, price > $5, listing age > 6m. Entry prices grounded 2026-06-30 (LIVE = IBKR; others = validated Yahoo, 01). 20d ADV from L210 (all ≫ $20M threshold; minimum PLD $0.58bn).

| Ticker | Sector | Entry | Tag | 20d ADV $mm | Ticker | Sector | Entry | Tag | 20d ADV $mm |
|---|---|---|---|---|---|---|---|---|---|
| AAPL | Info Tech | 288.71 | DELAYED | 19120 | JPM | Financials | 328.25 | DELAYED | 3080 |
| MSFT | Info Tech | 370.18 | DELAYED | 17979 | BAC | Financials | 57.19 | DELAYED | 2068 |
| NVDA | Info Tech | 198.18 | DELAYED | 31902 | GS | Financials | 1012.72 | DELAYED | 2515 |
| AVGO | Info Tech | 376.46 | DELAYED | 14525 | V | Financials | 342.92 | DELAYED | 2813 |
| AMD | Info Tech | 576.46 | LIVE | 15915 | LLY | Health Care | 1209.29 | LIVE | 3778 |
| NOW | Info Tech | 97.56 | DELAYED | 2785 | UNH | Health Care | 416.49 | LIVE | 2850 |
| MU | Info Tech | 1146.00 | LIVE | 59387 | JNJ | Health Care | 255.88 | DELAYED | 2068 |
| PLTR | Info Tech | 116.66 | DELAYED | 5147 | GE | Industrials | 372.11 | DELAYED | 1749 |
| GOOGL | Comm Svcs | 357.22 | DELAYED | 14142 | CAT | Industrials | 1064.99 | DELAYED | 3601 |
| META | Comm Svcs | 557.05 | DELAYED | 10305 | RTX | Industrials | 188.50 | DELAYED | 971 |
| NFLX | Comm Svcs | 72.73 | DELAYED | 3624 | XOM | Energy | 136.37 | DELAYED | 2429 |
| AMZN | Cons Disc | 239.72 | DELAYED | 14526 | CVX | Energy | 167.85 | DELAYED | 1564 |
| TSLA | Cons Disc | 416.07 | DELAYED | 18633 | LIN | Materials | 519.75 | DELAYED | 1304 |
| HD | Cons Disc | 351.79 | DELAYED | 1707 | FCX | Materials | 62.90 | DELAYED | 983 |
| WMT | Cons Staples | 113.76 | DELAYED | 2766 | NEE | Utilities | 88.14 | DELAYED | 973 |
| COST | Cons Staples | 937.86 | DELAYED | 2353 | SO | Utilities | 96.42 | DELAYED | 648 |
| PG | Cons Staples | 146.06 | DELAYED | 1357 | PLD | Real Estate | 136.81 | DELAYED | 580 |
| | | | | | AMT | Real Estate | 164.21 | DELAYED | 629 |

## Exclusion / Sampling Disclosure

No sampled name failed price, liquidity, history, or earnings-cadence requirements. Non-sampled S&P 500 constituents were not scored (no full-universe feed). Sampling rule disclosed above; percentiles labeled `SAMPLED_PCTL (n=35)` throughout 05/06. IT is intentionally over-weighted in the *screen* (8 names) to capture the semis/memory leadership and the mega-cap-software breakdown both ends of the dispersion — this affects screening breadth only, not portfolio caps.

## Metric Coverage Summary

| Metric Group | Sourceable | UNAVAILABLE | DQ / Confidence Effect | Notes |
|---|---|---|---|---|
| Risk / return | 35/35 | 0 | Genuine input | sigma, rvol, beta, drawdown, Sharpe/Sortino/IR/Treynor/Kelly/VaR/CVaR from fetched history (L200–L209) |
| Technical / price | 35/35 | 0 | Genuine input (Tech_Z) | momentum, RS, MA, MACD, RSI, TD-9, volume (L300–L304) |
| Fundamental / quality | 35/35 **proxy** | true fundamentals 0/35 | **Proxy only** → DQ 0.80 | Realized-quality proxy: Calmar (mom/|DD|), low realized vol, shallow drawdown. **No** earnings-revision/margin/FCF feed |
| Sentiment / positioning | 35/35 **proxy** | true positioning 0/35 | **Proxy only** → DQ 0.80, conf ≤ MEDIUM | Price/volume positioning proxy: RS_20d, RSI-position, 20d volume ratio. **No** short-interest/options-skew/analyst-revision feed |
| Enhancing feeds | 0/35 | 35/35 | Confidence capped MEDIUM, gross-exposure note | Options IV/skew, borrow, bid-ask tape, analyst revisions, institutional flow, risk-free rate |

**Data-quality consequence (material).** Two of four factor families (Fundamental, Sentiment) are scored on **price-derived proxies**, not independent feeds. This is disclosed, caps the data-quality multiplier at **0.80** for every name, caps all confidence at **MEDIUM**, and means cross-family signal overlaps (momentum/RS appear in more than one family) — a known limitation that inflates apparent multi-family confirmation and is weighed against the investability gate in 05/08. It does **not** by itself block GO (Enhancing classification), but it is the reason no name carries HIGH confidence this run.

## Technical Indicator Coverage

Daily / weekly / monthly TD-9, RSI(14), MACD(12,26,9), MA alignment, 20/60 momentum, 20-bar volume ratio, and relative strength vs SPY are available for all 35 equities and SPY/QQQ/SOXX via `technical_indicators.json` (status OK, 38/38). No timeframe is `UNAVAILABLE`.
