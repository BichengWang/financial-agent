# 04 Universe Summary — 2026-07-29

## Construction

| Source | Count | Cache fetched_at | Current-run treatment |
|---|---|---|---|
| S&P 500 | 503 | 2026-06-21T21:05:56Z | Cached constituent list retained per Index-Union protocol |
| Nasdaq-100 | 101 | 2026-06-21T21:05:56Z | Cached constituent list retained per Index-Union protocol |
| Overlap | 89 | N/A | Deduplicated |
| Union | 515 | N/A | Candidate universe |

Core ETFs are separate and do not count toward the union. Percentiles are `INDEX_UNION_PCTL (n=504)`.

## Inclusion and exclusion log

- 515 names passed through the deterministic union helper.
- 514 names had sourceable price/technical inputs.
- `FDXF` is excluded because it has 43 daily bars and is younger than six months; no emergency sampled fallback was used.
- Ten prior-run `DROP` decisions were binding under Reflection, leaving 504 names in the score cross-section.
- All 20 published names have an exact next earnings-event date; the hard-halt check is 0/20 unresolved.

| Ticker | Exclusion |
|---|---|
| FDXF | listing age and 43 bars below 6-month/60-bar threshold |
| AMAT | binding DROP from gpt-5-2026-07-01 reflection baseline |
| CNC | binding DROP from gpt-5-2026-07-01 reflection baseline |
| HOOD | binding DROP from gpt-5-2026-07-01 reflection baseline |
| INTC | binding DROP from gpt-5-2026-07-01 reflection baseline |
| KLAC | binding DROP from gpt-5-2026-07-01 reflection baseline |
| LRCX | binding DROP from gpt-5-2026-07-01 reflection baseline |
| PANW | binding DROP from gpt-5-2026-07-01 reflection baseline |
| SNDK | binding DROP from gpt-5-2026-07-01 reflection baseline |
| UAL | binding DROP from gpt-5-2026-07-01 reflection baseline |
| WST | binding DROP from gpt-5-2026-07-01 reflection baseline |

## Metric coverage

| Metric Group | Sourceable Count | UNAVAILABLE Count | DQ / Confidence Effect |
|---|---|---|---|
| Adjusted price history / liquidity | 514 | 1 | Required input; 504 entered scoring after reflection exclusions |
| Technical / Price family | 504 | 0 | Production family; contributes to Tech_Z |
| Macro / Regime family | 504 | 0 | Production family; contributes to Macro_Z |
| Fundamental family | 0 | 504 | UNAVAILABLE; lowers DQ and fails family gate, but is not Required-input completeness |
| Sentiment / Positioning family | 0 | 504 | UNAVAILABLE; lowers DQ and fails family gate, but is not Required-input completeness |
| Earnings horizon / next date | 514 | 1 | 335 exact + 179 grounded lower bounds; published 20 are exact and 0/20 unresolved |
| Market cap / GICS | 515 / 514 | 0 / 0 | One-day delayed metadata cache disclosed |

## Technical indicator coverage

| Indicator | Daily | Weekly | Monthly | Note |
|---|---|---|---|---|
| TD-9 | 517/518 | 517/518 | 517/518 | Counts include 514 sourceable equities + 3 ETFs; FDXF has 43 bars |
| RSI(14) | 517/518 | 517/518 | 516/518 | Counts include 514 sourceable equities + 3 ETFs; FDXF has 43 bars |
| MACD(12,26,9) | 517/518 | 517/518 | 512/518 | Counts include 514 sourceable equities + 3 ETFs; FDXF has 43 bars |
| MA alignment | 517/518 | 516/518 | 509/518 | Counts include 514 sourceable equities + 3 ETFs; FDXF has 43 bars |
| 20/60-bar momentum | 517/518 | 516/518 | 508/518 | Counts include 514 sourceable equities + 3 ETFs; FDXF has 43 bars |
| 20-bar volume ratio | 517/518 | 517/518 | 515/518 | Counts include 514 sourceable equities + 3 ETFs; FDXF has 43 bars |
| Relative strength vs SPY | 517/518 | 516/518 | 508/518 | Counts include 514 sourceable equities + 3 ETFs; FDXF has 43 bars |
