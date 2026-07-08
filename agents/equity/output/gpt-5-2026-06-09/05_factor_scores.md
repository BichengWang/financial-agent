# 05 Factor Scores

## Scoring Note

The scores below are review-only ordinal scores. They are not live trade forecasts. Each score is an `INFERRED` ledger row that uses source-backed price, beta, consensus, earnings-date, fundamentals, and regime rows while applying a hard penalty for missing options, short-interest, execution-quality, and covariance/drawdown feeds (L090-L093).

No name clears the investable threshold because data completeness is below 85%.

## Ranked Candidate Table

| Ticker | Company | Entry Price | Price Date | Price Tag | Adj Score | Pctl | Beta | 30d RVol | Days to Earnings | mu | sigma | Sigma Source | Target Price | Target Date | 70% CI Lo | 70% CI Hi | Ledger Rows | Confidence | Primary Thesis | Key Risk |
|---|---|---:|---|---|---:|---:|---:|---|---|---|---|---|---|---|---|---|---|---|---|---|
| MCK | McKesson | 783.75 | 2026-06-09 | DELAYED | 0.74 | 93 | 0.32 | UNAVAILABLE | prior field 2026-05-07 | N/A | UNAVAILABLE | UNAVAILABLE | N/A | N/A | N/A | N/A | L030-L034, L100 | MEDIUM | Healthcare distribution growth with low beta. | No IV/skew/covariance feed; post-earnings revision tape incomplete. |
| PG | Procter & Gamble | 148.30 | 2026-06-09 | DELAYED | 0.72 | 92 | 0.38 | UNAVAILABLE | 49 | N/A | UNAVAILABLE | UNAVAILABLE | N/A | N/A | N/A | N/A | L035-L039, L101 | MEDIUM | Defensive staples exposure in rate/vol regime. | Growth modest; bid-ask and covariance unavailable. |
| WMT | Walmart | 118.61 | 2026-06-09 | DELAYED | 0.69 | 90 | 0.60 | UNAVAILABLE | prior field 2026-05-21 | N/A | UNAVAILABLE | UNAVAILABLE | N/A | N/A | N/A | N/A | L040-L044, L102 | MEDIUM | Staples retail with strong buy consensus and earnings growth. | Valuation rich; earnings date field is historical, no next calendar feed. |
| ABBV | AbbVie | 226.43 | 2026-06-09 | DELAYED | 0.68 | 89 | 0.31 | UNAVAILABLE | prior field 2026-04-29 | N/A | UNAVAILABLE | UNAVAILABLE | N/A | N/A | N/A | N/A | L045-L049, L103 | MEDIUM | Low-beta healthcare with buy consensus and dividend support. | Trailing EPS growth negative; no options/borrow feed. |
| JPM | JPMorgan Chase | 312.82 | 2026-06-09 | DELAYED | 0.65 | 87 | 1.00 | UNAVAILABLE | 35 | N/A | UNAVAILABLE | UNAVAILABLE | N/A | N/A | N/A | N/A | L050-L054, L104 | MEDIUM | Market-beta financial quality with buy consensus. | Rate and credit sensitivity; bearish put-flow snippet not in model feed. |
| XOM | Exxon Mobil | 148.73 | 2026-06-09 | DELAYED | 0.62 | 84 | 0.15 | UNAVAILABLE | prior field 2026-05-01 | N/A | UNAVAILABLE | UNAVAILABLE | N/A | N/A | N/A | N/A | L055-L059, L105 | LOW | Energy hedge if geopolitical/oil risk persists. | Revenue, net income, and EPS snapshots are negative. |
| AZO | AutoZone | 3125.82 | 2026-06-09 | DELAYED | 0.59 | 81 | 0.35 | UNAVAILABLE | prior field 2026-05-26 | N/A | UNAVAILABLE | UNAVAILABLE | N/A | N/A | N/A | N/A | L060-L064, L106 | LOW | Defensive auto-parts demand with target upside. | Recent post-earnings target cuts and weak EPS snapshot. |
| UNH | UnitedHealth | 412.50 | 2026-06-09 | DELAYED | 0.56 | 78 | 0.65 | UNAVAILABLE | 49 | N/A | UNAVAILABLE | UNAVAILABLE | N/A | N/A | N/A | N/A | L065-L069, L107 | LOW | Healthcare recovery monitor with recent upgrade mentions. | Consensus target below sampled price; earnings snapshot weak. |

## Top 20 Names

Only 10 sampled names have enough source-backed current pages for this run. The top 8 are review-only monitors. CAT and GS are near misses. A top-20 full-universe table is unavailable because no full universe feed is wired.

## Recommended Investable Subset

None. Fewer than 5 names clear the investable threshold because the critical risk fields in L090-L093 are unavailable.

## Driver Summary

| Factor Family | Current Effect | Evidence |
|---|---|---|
| Fundamental | Mixed positive for MCK, WMT, PG; negative for XOM, UNH, AZO, ABBV on some earnings rows. | L034, L039, L044, L049, L059, L064, L069 |
| Technical / Price | Insufficient for investable ranking. | 30d return series and realized vol feed unavailable. |
| Sentiment / Positioning | Weak partial support from consensus ratings and targets only. | L032, L037, L042, L047, L052, L057, L062, L067 |
| Macro / Regime | Favors lower-beta healthcare and staples; penalizes high-beta growth carry-forward. | L001-L006, L011-L025 |

## Recommendation Metrics Blocks

Every monitor has source-backed entry price, date, and price tag. Target price, 70% CI, and executable `mu` are intentionally `N/A` because sigma and portfolio risk inputs are unavailable.

| Ticker | entry_price | price_date | price_tag | target_price | target_date | mu | sigma | sigma_source | ci_70_lo | ci_70_hi | ledger_rows |
|---|---:|---|---|---|---|---|---|---|---|---|---|
| MCK | 783.75 | 2026-06-09 | DELAYED | N/A | N/A | N/A | UNAVAILABLE | UNAVAILABLE | N/A | N/A | L030-L034, L090-L093, L100 |
| PG | 148.30 | 2026-06-09 | DELAYED | N/A | N/A | N/A | UNAVAILABLE | UNAVAILABLE | N/A | N/A | L035-L039, L090-L093, L101 |
| WMT | 118.61 | 2026-06-09 | DELAYED | N/A | N/A | N/A | UNAVAILABLE | UNAVAILABLE | N/A | N/A | L040-L044, L090-L093, L102 |
| ABBV | 226.43 | 2026-06-09 | DELAYED | N/A | N/A | N/A | UNAVAILABLE | UNAVAILABLE | N/A | N/A | L045-L049, L090-L093, L103 |
| JPM | 312.82 | 2026-06-09 | DELAYED | N/A | N/A | N/A | UNAVAILABLE | UNAVAILABLE | N/A | N/A | L050-L054, L090-L093, L104 |
| XOM | 148.73 | 2026-06-09 | DELAYED | N/A | N/A | N/A | UNAVAILABLE | UNAVAILABLE | N/A | N/A | L055-L059, L090-L093, L105 |
| AZO | 3125.82 | 2026-06-09 | DELAYED | N/A | N/A | N/A | UNAVAILABLE | UNAVAILABLE | N/A | N/A | L060-L064, L090-L093, L106 |
| UNH | 412.50 | 2026-06-09 | DELAYED | N/A | N/A | N/A | UNAVAILABLE | UNAVAILABLE | N/A | N/A | L065-L069, L090-L093, L107 |
