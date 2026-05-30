# Regime And Data

**Date:** 2026-05-29  
**Regime Label:** `BULL / NEUTRAL`  
**Confidence:** `MEDIUM`  
**Data State:** `MIXED_DELAYED`

## Regime Table

| Evidence | Reading | Interpretation | Tag |
| --- | --- | --- | --- |
| `SPY` | 757.28, 2026-05-29 delayed snapshot | Broad market is constructive | `DELAYED` |
| `QQQ` | 739.20, 2026-05-29 delayed snapshot | Growth leadership remains strong | `DELAYED` |
| `IWM` | 290.54, 2026-05-29 delayed snapshot | Small-cap participation is weaker than mega-cap growth | `DELAYED` |
| `VIX` | 15.32 close on 2026-05-29 | Low-to-moderate volatility, no stress regime | `DELAYED` |
| 10Y Treasury | 4.45% on 2026-05-28 | Rates are still high but not in fresh shock mode | `DELAYED` |
| 2Y Treasury | 3.99% on 2026-05-28 | Curve/rate backdrop is manageable for quality growth | `DELAYED` |
| Corporate OAS | 0.73 on 2026-05-28 | Credit spreads are not signaling immediate stress | `DELAYED` |
| FOMC calendar | June 16-17, 2026 next meeting | Macro event is outside the immediate 14-day equity earnings window | `OFFICIAL` |

## Regime Conclusion

The evidence supports a constructive but crowded AI-led tape. Volatility is low, large-cap growth remains leadership, and credit/rates are not forcing a defensive regime. The right classification is not pure `BULL` confidence because the sampled universe is highly exposed to the same AI-capex cycle.

## Current Market Snapshot

| Ticker | Close / Snapshot | Open | Volume | Note |
| --- | ---: | ---: | ---: | --- |
| `SPY` | 757.28 | 755.90 | 14,571,670 | Broad benchmark |
| `QQQ` | 739.20 | 737.84 | 13,897,918 | Growth benchmark |
| `AVGO` | 439.69 | 432.95 | 8,177,285 | Strong, but earnings on June 3 |
| `NVDA` | 216.59 | 214.58 | 50,570,930 | AI compute leadership |
| `GEV` | 965.61 | 997.00 | 1,246,617 | Volatile after strong MoM move |
| `MSFT` | 442.76 | 432.55 | 16,603,507 | AI/cloud platform strength |
| `ORCL` | 221.37 | 209.00 | 13,778,963 | Strong snapshot; early-June earnings risk |
| `PLTR` | 156.08 | 147.83 | 33,656,241 | High-momentum AI software |
| `ANET` | 157.42 | 156.42 | 2,159,689 | AI networking |

## Handoff To Factor Scoring

Prefer:

1. post-earnings AI infrastructure leaders with current operating validation,
2. power/electrification beneficiaries with backlog and order support,
3. platform/cloud names where AI demand is showing in revenue or backlog.

Penalize:

1. names with earnings inside 14 calendar days,
2. single-day earnings-gap moves with weak 2-6 week persistence evidence,
3. names whose role would worsen AI factor crowding without improving portfolio diversification.

## Sources

- Stooq quote snapshots: `https://stooq.com/q/l/`
- Cboe VIX history: `https://cdn.cboe.com/api/global/us_indices/daily_prices/VIX_History.csv`
- FRED rates/credit: `https://fred.stlouisfed.org/graph/fredgraph.csv`
- Federal Reserve FOMC calendar: `https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm`

