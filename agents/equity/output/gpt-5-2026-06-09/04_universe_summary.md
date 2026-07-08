# 04 Universe Summary

## Universe Construction

This run used a constrained, source-backed sample rather than a full U.S. equity universe. The sample was selected from:

- Prior automation monitors: AZO, UNH, MCK, JPM, XOM, CAT, WMT, ABBV, GS, PG.
- Defensive sector rotation evidence: XLV and XLP session outperformance (L005-L006).
- MoM reflection candidates from the cross-model baseline: MSFT, NVDA, META, GOOGL, AMZN (L008, L011-L025).

## Eligibility Checks

| Filter | Status | Notes |
|---|---|---|
| U.S. primary listing | PASS for sampled names | StockAnalysis pages identify NYSE/Nasdaq listings for sampled candidates. |
| Price > $5 | PASS for sampled candidates | All review-only monitors exceed $5. |
| Market cap > $2B | PASS for sourced candidates | Pages show large-cap / mega-cap market caps where observed. |
| Liquidity > $20M ADV | INCOMPLETE | Current volume is available for some names, but 20-day dollar volume is not fully derived. |
| Bid-ask spread < 50 bps | UNAVAILABLE | Blocks `GO`. |
| Full trading-session coverage | UNAVAILABLE | Blocks `GO`. |
| Event calendar | PARTIAL | Earnings-date fields exist on pages, but no complete calendar feed is wired. |

## Review-Only Monitor Set

| Ticker | Sector | Entry Price | Price Tag | Beta | Earnings Date Field | Rationale | Ledger Rows |
|---|---|---:|---|---:|---|---|---|
| MCK | Healthcare | 783.75 | DELAYED | 0.32 | 2026-05-07 | Healthcare distribution, strong source-backed growth snapshot, low beta. | L030-L034 |
| PG | Consumer Staples | 148.30 | DELAYED | 0.38 | 2026-07-28 | Defensive staples exposure and positive earnings-growth snapshot. | L035-L039 |
| WMT | Consumer Staples | 118.61 | DELAYED | 0.60 | 2026-05-21 | Staples retail, strong buy consensus, positive revenue/net income/EPS growth. | L040-L044 |
| ABBV | Healthcare | 226.43 | DELAYED | 0.31 | 2026-04-29 | Low beta healthcare, buy consensus, forward multiple support. | L045-L049 |
| JPM | Financials | 312.82 | DELAYED | 1.00 | 2026-07-14 | Large-bank quality, beta closer to market, buy consensus. | L050-L054 |
| XOM | Energy | 148.73 | DELAYED | 0.15 | 2026-05-01 | Energy hedge and buy consensus, but fundamentals are negative YoY. | L055-L059 |
| AZO | Consumer Discretionary | 3125.82 | DELAYED | 0.35 | 2026-05-26 | Auto-parts defensiveness and target upside, offset by recent target cuts. | L060-L064 |
| UNH | Healthcare | 412.50 | DELAYED | 0.65 | 2026-07-28 | Healthcare recovery watch, but consensus target is below sampled price. | L065-L069 |

## Near Misses

| Ticker | Reason | Ledger Rows |
|---|---|---|
| CAT | High beta 1.60 and only modest target upside; not ideal under rate/vol pressure. | L070-L074 |
| GS | Hold consensus and target downside despite strong earnings growth; skip for top monitors. | L075-L079 |

## Coverage Gap

Because the full U.S. universe was not screened and critical risk feeds are unavailable, the universe stage recommends `REVIEW_ONLY`. It does not support `GO` or a formally investable subset.
