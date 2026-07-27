# 04 Universe Summary — 2026-07-27

## Index-Union Construction

`build_index_universe.py` succeeded, so the normal daily path applies and **no sampled fallback was
used**. Every percentile in this package is labelled `INDEX_UNION_PCTL (n=514)`.

| Field | Value |
|---|---|
| S&P 500 constituents | 503 |
| Nasdaq-100 constituents | 101 |
| Overlap | 89 |
| **Union** | **515** |
| S&P 500 cache | `agents/equity/turtle-trader/universe/sp500.json`, `fetched_at` 2026-06-21T21:05:56Z |
| Nasdaq-100 cache | `agents/equity/turtle-trader/universe/nasdaq100.json`, `fetched_at` 2026-06-21T21:05:56Z |
| Scoreable after filters | **514** |
| Ranked (≥ 60th pctl, carry `mu`) | 206 |
| Published monitoring sleeve | 24 |
| Investable | **0** |

The caches are 36 days old. Per `rules.md § Index-Union Universe Protocol` rule 5 that is logged and
used, not a reason to fall back to a 30-name sample; a refresh is a maintenance task. `MRSH` in the
caches is a confirmed real constituent (Marsh & McLennan), not a typo for MMC — it is not "fixed".

## Inclusion / Exclusion Log

| Filter | Threshold | Enforced | Result |
|---|---|---|---|
| U.S. primary exchange | required | yes | index membership implies it |
| Market cap | > $2B | yes (L010) | 513 pass, 1 `UNAVAILABLE` |
| Average daily dollar volume | > $20M over 20 sessions | yes (L018) | all scoreable names pass |
| Price | > $5 | yes (L002) | all scoreable names pass |
| Listing age | > 6 months (≥126 bars) | yes (L012) | **1 rejection** |
| Traded ≥ 80% of last 60 sessions | required | yes (L012) | all pass |
| Bid-ask spread ≤ 50bp | required | **NOT ENFORCEABLE** | no spread tape wired (L048) — disclosed as a coverage gap, not silently passed |
| Halted / pending delisting | excluded | partial | no halt feed; no halted name detected in the fetched bars |
| Unresolved corporate-action ambiguity | excluded | yes | handled by the adjusted-close basis (L003) rather than by exclusion |

### Rejection log

| Ticker | Reason |
|---|---|
| FDXF | listing age: 40 bars < 126 (~6 months) |

**FDXF** is the FedEx freight spin-off; its first bar is 2026-05-28, giving
40 bars against the 126-bar (~6-month) minimum. It is
legitimately excluded and becomes eligible around 2026-11-27. This matches the 2026-07-24 finding.

### Market-cap gap, disclosed

**BF-B** (Brown-Forman class B) is the one name whose market cap could not be sourced (L055): the
Nasdaq screener returns its `BF/B` row with an empty `marketCap` field, and the stockanalysis quotes
endpoint carries no market-cap field. **It is recorded `UNAVAILABLE` and not estimated.** BF-B ranks
412 of 514 (pctl 19.88), far below the 60th-percentile ranking
floor, so the gap affects no published number. It is retained rather than dropped because price and
ADV20 both pass and it is an S&P 500 constituent.

## Metric Coverage Summary

Which `rules.md § Financial Metrics and Score Attribution` inputs are sourceable across the eligible
universe. **This is the table that decides the run's status.**

| Metric group | Sourceable | Coverage | Contributes to `Adj Score`? | Note |
|---|---|---|---|---|
| Price / return history | 514/514 | 100% | yes | L002, L003, L012 |
| Realized vol, downside vol | 514/514 | 100% | yes (Macro_Z, sigma) | L013, L014 |
| Beta, tracking error | 514/514 | 100% | yes (Macro_Z) | L015, L016 |
| Max drawdown 60d | 514/514 | 100% | yes (Macro_Z) | L017 |
| VaR95 / CVaR95 | 206/206 ranked | 100% | diagnostic + negative driver | L031 |
| Kelly / 0.25 Kelly | 206/206 ranked | 100% | investability gate + sizing | L032 |
| Technical pack (TD-9, RSI, MACD, MA, momentum, volume, RS) | 518/518 | 100% | yes (Tech_Z) | L019–L021 |
| Next earnings date | 57/514 | 11.1% | penalty only, on grounded names | L022–L026 |
| **Fundamental family** | **0/514** | **0%** | **NO — `UNAVAILABLE`** | L046 |
| **Sentiment / positioning family** | **0/514** | **0%** | **NO — `UNAVAILABLE`** | L047 |
| Options IV / skew, short interest, bid-ask, revisions, ownership | 0/514 | 0% | no | L048, Enhancing only |

### Why `Fund_Z` and `Sent_Z` are `UNAVAILABLE` rather than zero

`rules.md § Financial Metrics and Score Attribution` allows a metric into `Adj Score` only when it is
sourceable for **at least 70% of the eligible universe**. `fundamental_diagnostics.py` and
`sentiment_diagnostics.py` exist and work — the 2026-07-16 shadow run covered 24 real names with 100%
sourceability and zero lineage violations — but 24 names is ~4.7% of this universe, nowhere near 70%.
Both tools also emit `"gating_status": "SHADOW"`, and `rules.md § SHADOW Diagnostic Tooling` forbids
folding them into `Adj Score`, the evidence-threshold count, or the confidence label until a run
explicitly promotes the family. **No shadow output is cited as a scoring input anywhere in this
package.** Clearing this needs Phase 2 of
`agents/equity/plan/2026-07-15-claude-fable-5-top-priority.md`: bulk EDGAR `companyfacts.zip` plus a
threaded Nasdaq sentiment fetch across all 514 names.

The consequence is structural and is the reason this run cannot publish `GO`: with two of four
families `UNAVAILABLE`, Evidence Threshold #2 (≥3 of 4 families non-negative) is **unreachable for
every name in the universe**, however strong its technicals.

## Technical Indicator Coverage

Per timeframe, across all 518 symbols handed to the helper (515 universe + 3 core ETFs):

| Indicator | Daily | Weekly | Monthly |
|---|---|---|---|
| TD-9 setup | 518/518 | 518/518 | 518/518 |
| RSI(14) | 518/518 | 518/518 | 518/518 |
| MACD(12,26,9) line/signal/histogram/state | 518/518 | 518/518 | 518/518 |
| MA20 / MA50 / alignment | 518/518 | 518/518 | 518/518 |
| 20/60-bar momentum | 518/518 | 518/518 | 518/518 |
| 20-bar volume ratio | 518/518 | 518/518 | 518/518 |
| Relative strength vs SPY (20/60) | 518/518 | 518/518 | 518/518 |

No indicator field is hand-filled anywhere in this package. Every displayed value traces to
`technical_indicators.json` (L019–L021) plus the underlying adjusted-close history row (L003).
