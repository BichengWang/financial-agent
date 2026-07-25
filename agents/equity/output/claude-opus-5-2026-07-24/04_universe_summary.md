# 04 Universe Summary — 2026-07-24

## Construction

Normal index-union path. `build_index_universe.py` ran with default cache paths and succeeded; the Sampled Universe Protocol was **not** used and was not permitted.

```bash
python3 agents/equity/daily_investment_system/build_index_universe.py \
  --output-tickers agents/equity/output/claude-opus-5-2026-07-24/eligible_universe.txt \
  --output-summary agents/equity/output/claude-opus-5-2026-07-24/universe_summary.json
```

| Count | Value | Source |
|---|---|---|
| S&P 500 constituents | 503 | `agents/equity/turtle-trader/universe/sp500.json`, `fetched_at` 2026-06-21T21:05:56Z |
| Nasdaq-100 constituents | 101 | `agents/equity/turtle-trader/universe/nasdaq100.json`, `fetched_at` 2026-06-21T21:05:56Z |
| Overlap | 89 | — |
| **Union (eligible universe)** | **515** | `universe_summary.json`, ledger row L134 |
| Scored after filters | **514** | `run_computed_manifest.json` |

Caches are 33 days old. Per `rules.md § Index-Union Universe Protocol` #5 they are used as-is and their `fetched_at` values logged; refreshing them is a maintenance task, never a reason to fall back to a 30-name sample. All percentile ranks in `05`/`06`/`07`/`09` are labelled **`INDEX_UNION_PCTL (n=514)`**.

Note: `MRSH` appears in the caches and is a real NYSE listing (Marsh & McLennan), confirmed 2026-07-21 — it is **not** a typo for `MMC` and was not "corrected".

## Inclusion Filter Results

| Filter | Threshold | Names failing |
|---|---|---|
| Listing | U.S. primary exchange | 0 |
| Market cap | > $2B | 0 (index membership implies it; not separately re-sourced) |
| Average daily dollar volume | > $20M over 20 sessions | **0** — universe minimum is $34.9M, 5th pctl $123.0M, median $393.8M |
| Price | > $5 | **0** — universe minimum is $8.21, 5th pctl $26.25, median $141.06 |
| Listing age | > 6 months | **1 — `FDXF`** |

## Exclusion / Rejection Log

| Ticker | Reason | Evidence |
|---|---|---|
| `FDXF` | **Excluded.** Recent spin-off: only 41 daily bars, first 2026-05-27. Fails both the >6-month listing-age filter and the 60-bar minimum history required for beta, correlation, drawdown and realized vol. | Nasdaq historical returned 41 rows; `technical_indicators.json` records `status: UNAVAILABLE` |

No other name was excluded. Notably, **no name was dropped for a fetch failure** — the three symbols that resisted the bulk pass were all recovered rather than discarded:

| Ticker | Issue | Resolution |
|---|---|---|
| `BRK-B` | Nasdaq rejects hyphen notation | Refetched as `BRK.B` → 1,307 bars |
| `BF-B` | Unavailable on Nasdaq under any notation | IBKR MCP `get_price_history`, conid 4931 → 1,255 bars |
| `SATS` | Ticker renamed to `ECHO` (EchoStar) upstream | Fetched as `ECHO`, stored as `SATS.csv`, rename disclosed |

`BF-B` carries 1,255 bars (5 years) and is fully scored. Minimum bar count across the scored universe is 186 (a recent addition), median 1,307 — comfortably above the 60-bar `GO` minimum and the 252-day target lookback for all but a handful of names.

## Metric Coverage Summary

Which `rules.md § Financial Metrics and Score Attribution` inputs are sourceable across the eligible universe:

| Metric group | Sourceable | UNAVAILABLE | Effect |
|---|---|---|---|
| Risk / return (Sharpe, Sortino, IR, Treynor, Calmar, beta, tracking error) | **514 / 514** | 0 | Feeds Technical and Macro families |
| Tail risk (60d max DD, VaR95, CVaR95) | **514 / 514** | 0 | Negative drivers and penalty input |
| Sizing (raw Kelly, 0.25×Kelly, cap status) | **514 / 514** | 0 | Investability gate and sizing |
| Technical (momentum, RS vs SPY, MA alignment, volume, TD-9, RSI, MACD ×3 timeframes) | **517 / 518 records** | 1 (`FDXF`) | Full `Tech_Z` |
| **Fundamental / quality** (revisions, margin, FCF yield, ROIC, leverage, valuation) | **0 / 514** | **514** | **`Fund_Z` UNAVAILABLE — data-quality and evidence-threshold effect, not a GO blocker** |
| **Sentiment / positioning** (analyst breadth, short interest, borrow, IV/skew, put/call) | **0 / 514** | **514** | **`Sent_Z` UNAVAILABLE — same** |
| GICS sector label | 68 / 76 shortlist names | 8 | Cosmetic in a `NO_TRADE` run; would matter for the 30% sector cap |
| Risk-free rate | 1 / 1 | 0 | Excess-return ratios are **not** `RAW_DIAGNOSTIC` this run |

**On `Fund_Z` / `Sent_Z`:** `fundamental_diagnostics.py` and `sentiment_diagnostics.py` exist and work, but `rules.md § SHADOW Diagnostic Tooling` holds them at `SHADOW` gating and forbids folding them into `Adj Score`, the evidence-threshold count, or the confidence label. The independent 70%-of-universe sourceability bar in `§ Financial Metrics and Score Attribution` also binds: the one completed shadow run covered ~4.7% of the universe. Promotion needs Phase 2 (bulk `companyfacts.zip` + threaded Nasdaq fetch across ~514 names), which this run did not attempt. This is the sole cause of `NO_TRADE`.

**Family availability across the scored universe:**

| Families available | Families non-negative | Names | Can ever clear evidence threshold #2 (≥3 of 4 non-negative)? |
|---|---|---|---|
| 2 (Tech, Macro) | 2 | 197 | **No** |
| 2 (Tech, Macro) | 1 | 182 | **No** |
| 2 (Tech, Macro) | 0 | 135 | **No** |

**0 of 514 names can satisfy evidence threshold #2** — with only two families ever countable, the 3-of-4 bar is unreachable by construction. This is the mechanical origin of `NO_TRADE`.

## Technical Indicator Coverage

From `technical_indicators.json` (518 records = 515 union + SPY/QQQ/SOXX):

| Timeframe | TD-9 | RSI(14) | MACD state | MA alignment |
|---|---|---|---|---|
| Daily | 517 (99.8%) | 517 (99.8%) | 517 (99.8%) | 517 (99.8%) |
| Weekly | 517 (99.8%) | 517 (99.8%) | 517 (99.8%) | 516 (99.6%) |
| Monthly | 517 (99.8%) | 515 (99.4%) | 511 (98.6%) | 503 (97.1%) |

Every timeframe clears the 70%-of-universe bar that `rules.md § Technical Indicator Pack Definition` requires before RSI and MACD may contribute to `Tech_Z`, so both contribute. The monthly shortfalls are names with fewer than ~35 monthly bars (MACD needs 26+9); they are recorded `UNAVAILABLE` per field rather than hand-filled. Momentum, volume ratio, and relative-strength support fields match the same coverage.

## Published Set Composition

26 names published to the monitoring sleeve (21 organic top-ranked with grounded earnings + 5 binding reflection carry-forwards).

| Dimension | Distribution |
|---|---|
| Sector | Industrials 8, Finance 7, Health Care 2, Energy 2, Utilities 1, Consumer Discretionary 1, Consumer Staples 1, label UNAVAILABLE 4 |
| `mu` band | +6.0% (≥95th pctl) ×21, +5.0% (90–95th) ×2, +2.0% (70–80th) ×3 |
| Penalty | 0.00 ×16, −0.05 ×3, −0.10 ×7 |
| Confidence | `LOW` ×26 |

Industrials + Finance account for 15 of 22 labelled names — a concentration that would breach the 30% single-sector cap in any live portfolio, and is one of the feasibility findings in `07`.

## Handoff to Factor Scoring

514 scored names, percentiles `INDEX_UNION_PCTL (n=514)`, data-quality multiplier 0.80 universe-wide, confidence capped at `MEDIUM` by the rank-IC binding and at `LOW` in practice by the family gap. Carry-forward decisions from `02 § 5` are binding: 2 `CARRY`, 3 `DOWNGRADE` admitted to the monitoring sleeve; 9 `DROP` names held out of the scored set.
