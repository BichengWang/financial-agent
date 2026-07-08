# Preflight

**Date:** 2026-06-07  
**Data status:** `MIXED_DELAYED`  
**Recommended publication mode:** `REVIEW_ONLY`

## Preflight Summary

The run can proceed for research and monitoring, but not for live trade publication. The latest equity data available in this run is the Friday, 2026-06-05 close. The cash market is closed on Sunday, 2026-06-07, and the June 5 session was a material regime event: large-cap technology and semiconductors sold off while VIX rose to 21.51.

The correct status is `REVIEW_ONLY` because live execution-quality inputs remain unavailable.

## Data Coverage

| Data Family | Status | Source / Lineage | Impact |
| --- | --- | --- | --- |
| Equity prices | `DELAYED` | MarketBeat chart pages for individual tickers and ETFs | Usable for returns and sample-relative ranking; not enough for execution. |
| Volume | `DELAYED` | MarketBeat chart pages | Confirms sampled names are liquid; not a substitute for ADV/slippage model. |
| VIX | `LIVE/OFFICIAL DELAYED` | Cboe VIX historical CSV, latest 2026-06-05 close 21.51 | Valid regime input. |
| Rates | `DELAYED` | Multpl 10Y close 4.55% on 2026-06-05; ALFRED confirms latest DGS10 vintage | Valid macro input, not an intraday rates feed. |
| Labor data | `OFFICIAL` | BLS May 2026 Employment Situation, payrolls +172,000 | Valid macro catalyst input. |
| FOMC calendar | `OFFICIAL` | Federal Reserve calendar, next meeting 2026-06-16 to 2026-06-17 | Valid event-risk input. |
| Earnings dates | `MIXED` | Company announcements where available; cadence estimate otherwise | Penalize or exclude near events. |
| Beta/correlation/drawdown | `N/A` | No validated risk engine available | Blocks `GO`. |
| Options IV/skew | `N/A` | No options feed available | Caps confidence. |
| Short interest | `N/A` | No current feed available | Caps sentiment confidence. |

## Validation Notes

| Check | Result | Notes |
| --- | --- | --- |
| U.S.-listed, liquid universe | Partial | Sampled 60 liquid U.S.-listed equities plus ETFs for regime; not a full universe. |
| Price > $5 | Pass in sampled universe | All scored names exceed threshold. |
| Market cap > $2B | Pass by large/mid-cap sampling design | Not independently revalidated name-by-name. |
| Bid/ask spread < 50 bps | `N/A` | No quote-book feed. |
| Event calendar | Partial | `ORCL` has confirmed June 10 earnings, inside 14-day window; excluded from candidates. |
| Data completeness >= 85% | Partial | Candidate-level completeness is 85%-88% for public evidence, but portfolio risk completeness fails. |

## Stop-Criteria Decision

The run is not `HALTED` because price, macro, and regime lineage is explicit and sufficient for review analysis. It is not `GO` because the risk model and execution data are missing. It is not `NO_TRADE` because the sampled process can still identify a credible watchlist. Final mode: `REVIEW_ONLY`.
