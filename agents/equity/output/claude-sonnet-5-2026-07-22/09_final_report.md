# 09 Final Report

```text
══════════════════════════════════════════════════════
QUANTITATIVE EQUITY SELECTION REPORT — 2026-07-22
Run Status: NO_TRADE
Classification: INTERNAL — INVESTMENT COMMITTEE USE
══════════════════════════════════════════════════════
```

## Executive Summary

This run executed the full pipeline after today's close (fire time ~16:42 ET) using `DELAYED` public-market data — Nasdaq bulk historical for the 2026-07-21 technical/analytics basis, and Nasdaq quote-info official closes for 2026-07-22 entry prices, cross-checked once against IBKR for SPY. 17 predictions matured today (from `gpt-5-2026-06-24`) and settled at today's official close via the newly-accepted `TARGET_DATE_CLOSE` mechanism (see `02_reflection.md § 0`): 10 HIT / 4 MISS on the equity side and 1 HIT / 2 MISS on the Core ETF market-forecast side. 514 of 515 eligible-universe names were scored (FDXF excluded — recent spinoff, insufficient history); the strongest technical leadership sits in BBY, DDOG, GEN, DOC, and DVA, but **no name qualifies as investable** because Fund_Z/Sent_Z remain structurally `SHADOW`-only, making the required "3 of 4 factor families non-negative" evidence threshold permanently unreachable at today's scoring scope. 26 names publish to the monitoring sleeve with full forecast records; final status is `NO_TRADE`.

## MoM Reflection Summary

Baseline `gpt-5-2026-06-24` (`CROSS_MODEL_BASELINE`, exactly on the 28-day target) was `NO_TRADE` under a `BULL` regime call. Of its 14 ranked names, financials (GS, BAC, JPM) and healthcare (LLY, UNH) validated with positive alpha; industrials/materials (CAT, GE, FCX) largely failed on realized alpha despite one raw HIT. Carry-forward decisions: BAC, UNH, JPM, AAPL, V, LLY, GE **CARRY** into today's monitor sleeve; GS **DOWNGRADES** to the rejection log (penalty-driven floor breach); CAT, GOOGL, FCX, EQIX, NVDA **DROP** (structural technical deterioration). Today's settlement batch also surfaced a statistically significant rank-order inversion (mu-rank vs. realized-alpha-rank, Spearman −0.712, p=0.004, despite the strong 71.4% hit rate) — flagged for the 2026-07-31 structural review in `13_evolution_log.md`. Full detail in `02_reflection.md`.

## Regime Table

| Regime | Data Quality | Key Macro Risk |
|---|---|---|
| `NEUTRAL` (semiconductor high-vol pocket) | `DELAYED`, all 5 Required inputs grounded | SOXX -15.6% 60d drawdown with realized vol nearly doubling (16.7%→20.7%) and a sharp -16.1% 20d relative-strength reversal vs SPY, even as the broad market (SPY) sits flat on its own moving averages with VIX at its 60d average |

## Core ETF Market Forecast

| ETF | Entry | Price Date | mu | sigma | Target | 70% CI | Confidence |
|---|---:|---|---:|---:|---:|---|---|
| SPY | 747.48 | 2026-07-22 | +0.50% | 4.02% | 751.22 | 719.97–782.47 | MEDIUM |
| QQQ | 705.35 | 2026-07-22 | +0.87% | 8.08% | 711.49 | 652.23–770.76 | MEDIUM |
| SOXX | 555.52 | 2026-07-22 | +1.91% | 20.70% | 566.12 | 446.52–685.73 | MEDIUM |

Full derivation and relative-strength notes in `03_regime_and_data.md`.

## Ranked Candidates (Monitoring Sleeve — Investable Set Empty)

Top 10 by Adj Score (full 26-name table with score traces and technical states in `05_factor_scores.md`/`06_top_candidates.md`):

| Ticker | Entry | Pctl | mu | sigma | Target | Confidence | Key Risk |
|---|---:|---:|---:|---:|---:|---|---|
| BBY | 87.11 | 100.0 | +6.0% | 8.28% | 92.34 | LOW | Insufficient third supportive family |
| DDOG | 245.77 | 99.8 | +6.0% | 12.35% | 260.52 | LOW | Insufficient third supportive family |
| GEN | 25.58 | 99.6 | +6.0% | 10.39% | 27.11 | LOW | Insufficient third supportive family |
| DOC | 22.17 | 99.4 | +6.0% | 7.08% | 23.50 | LOW | Earnings-window penalty (13d) |
| DVA | 231.95 | 99.2 | +6.0% | 5.91% | 245.87 | LOW | Earnings-window penalty (13d) |
| MMM | 170.79 | 99.0 | +6.0% | 8.37% | 181.04 | LOW | Insufficient third supportive family |
| TRV | 372.06 | 98.8 | +6.0% | 9.48% | 394.38 | LOW | Insufficient third supportive family |
| CRWD | 188.42 | 98.6 | +6.0% | 15.92% | 199.73 | LOW | Insufficient third supportive family |
| PANW | 335.28 | 98.4 | +6.0% | 15.68% | 355.40 | LOW | Technical exhaustion flag |
| VTRS | 17.01 | 98.2 | +6.0% | 8.77% | 18.03 | LOW | Insufficient third supportive family |

## Portfolio Analytics / No-Trade Rationale

Investable set size is **0**. Evidence threshold #2 ("at least 3 of 4 factor families non-negative," `rules.md § Evidence Thresholds`) is structurally unreachable while Fund_Z/Sent_Z stay `SHADOW`-only — only Tech_Z and Macro_Z are ever countable toward the 3-of-4 requirement. Per `rules.md § Stop Criteria`, fewer than 5 investable names mechanically triggers `NO_TRADE`; the Portfolio Construction Agent's Task 0 feasibility pre-check stops before drafting any weights. Secondary (non-binding) infeasibility evidence — 30.8% Financials sector concentration and 13/26 names with earnings inside 14 days in the monitor sleeve — is disclosed in `07_portfolio_proposal.md` for completeness.

## Assumptions and Limitations

- All prices are `DELAYED` public-endpoint observations (Nasdaq bulk historical + quote-info), not a brokerage feed; cross-checked once against IBKR for SPY.
- Technical/derived analytics (beta, realized vol, drawdown, momentum, RS, TD-9/RSI/MACD) are computed on the 2026-07-21 close basis; entry prices for the settlement batch, Core ETFs, and 26 monitor-sleeve names are the 2026-07-22 official close, fetched separately (see `00_run_manifest.md § Price Basis Disclosure`).
- Fund_Z and Sent_Z are `SHADOW`-only and excluded from `Adj Score`, the evidence-threshold count, and the confidence label — this is a standing, disclosed limitation, not new to this run.
- Earnings preflight is scoped to the top-35-by-score + 14 reflection carry-forwards + a bounded 6-name second pass (48+6=54 names); 9 near-miss entrants (CTAS, A, EBAY, WELL, UNP, EIX, KHC, AMP, LH) remain unfetched and are excluded-with-disclosure from the published candidate table.
- Percentiles are full index-union percentiles (`INDEX_UNION_PCTL, n=514`), not a sampled fallback.
- Options IV/skew, short interest, bid-ask tape, analyst-revision tape, and institutional-flow data (all Enhancing-tier) were not fetched this run; consistent with every prior dated package.

## Next Scheduled Review

No scheduler is currently active (`runbook.md § Scheduler`: the last durable job expired). This run publishes `12_close_log.md` (real content, fires after today's close) and `13_evolution_log.md`. Next manual run should occur pre-open the next trading day (2026-07-23) or intraday per the runbook cadence.

## Sources

- Nasdaq bulk historical: `https://api.nasdaq.com/api/quote/{ticker}/historical`
- Nasdaq official-close quote info: `https://api.nasdaq.com/api/quote/{ticker}/info`
- Nasdaq earnings-date preflight: `https://api.nasdaq.com/api/analyst/{ticker}/earnings-date`
- CBOE VIX history: `https://cdn.cboe.com/api/global/us_indices/daily_prices/VIX_History.csv`
- U.S. Treasury daily bill rates: `https://home.treasury.gov/resource-center/data-chart-center/interest-rates/daily-treasury-rates.csv/...`
- IBKR MCP `get_price_snapshot` / `get_price_history` (SPY cross-check, BF-B history)
