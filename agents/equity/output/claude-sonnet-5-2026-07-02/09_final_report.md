```
══════════════════════════════════════════════════════
QUANTITATIVE EQUITY SELECTION REPORT — 2026-07-02
Run Status: NO_TRADE
Classification: INTERNAL — INVESTMENT COMMITTEE USE
══════════════════════════════════════════════════════
```

## Executive Summary

The run completed the full state machine (`PRECHECK → REFLECTION → DATA_OK → TECHNICALS_OK → SCORED → PORTFOLIO_DRAFT → RISK_REVIEW → PUBLISHED → CLOSE_LOGGED → EVOLUTION_REVIEW`) and produced a fully IBKR-grounded, ledger-backed analysis, but no name clears the system's investability bar this run. Fundamental and Sentiment/Positioning factor families are `UNAVAILABLE` for every scored name (no fundamentals or positioning feed is connected in this environment, and Yahoo Finance web fallback is blocked by organizational egress policy), capping every candidate at a maximum of 2 of 4 supportive factor families against the required 3-of-4 threshold. A secondary, independent gap — no earnings-calendar feed — leaves every name's earnings-date field `UNAVAILABLE` rather than confirmed-clear. Both are genuine Required-input/Evidence-Threshold failures, not misapplied Enhancing-input caution. Twelve names are published in a `LOW`-confidence monitoring sleeve, fully forecast with `mu`/`sigma`/targets for future settlement, but zero positions are sized. Regime read: `BULL` (VIX 16.53, down sharply from the 21.51 spike that drove the prior cross-model baseline's `HIGH_VOL/RATE_SHOCK` call), with a one-week rotation wobble out of tech and into defensives layered on top of a strongly bullish month.

## MoM Reflection Summary

(Summarizes `02_reflection.md`; no new facts.) This is the first `claude-sonnet-5` run in this repository — no same-model baseline exists. The MoM baseline algorithm selected `gpt-5-2026-06-07` as a `CROSS_MODEL_BASELINE` (closest in-window package to the 28-day target, 3 days off target). That baseline was itself a sampled-universe `REVIEW_ONLY` run with no `15_predictions.json`, so no ledger-backed MoM return, alpha, or Hit/Miss could be computed for its monitoring names (`AZO`, `UNH`, `MCK`, `JPM`, `XOM`, `CAT`, `WMT`, `ABBV`, `GS`, `PG`) — only qualitative regime continuity was assessed. Reflection confidence: `LOW`. Prediction settlement: 0 predictions due this run across 20 scanned ledgers (352 total open records; earliest open `target_date` is 2026-07-08) — `INSUFFICIENT_SETTLED_N` for rolling calibration metrics.

## Regime Table

| Field | Value | Ledger Rows |
| --- | --- | --- |
| Regime | `BULL` (medium-high confidence) | L001–L016 |
| Data quality | Grounded/IBKR for scored names; universe breadth capped at 30/515 | — |
| Key macro risk | Weekly rotation wobble (tech -3.5%, defensives +2–5%) inside a bullish month; SOXX weekly TD-9 exhaustion signal (`SELL_SETUP_9`) at overbought RSI (72.5) | L007–L009 |

## Core ETF Market Forecast (summary — no new facts, see `03_regime_and_data.md`)

| ETF | Entry Price | mu | sigma | Target Price | 70% CI | Confidence |
| --- | ---: | ---: | ---: | ---: | --- | --- |
| SPY | 746.40 | +1.5% | 4.45% | 757.60 | [723.04, 792.15] | MEDIUM |
| QQQ | 725.59 | +2.4% | 8.35% | 742.79 | [679.77, 805.80] | MEDIUM |
| SOXX | 599.50 | +3.35% | 21.32% | 619.58 | [486.64, 752.53] | MEDIUM |

## Ranked Candidate Table (compact — top 12 monitoring sleeve; full 30-name table in `05_factor_scores.md`)

| Rank | Ticker | Adj Score | Confidence | mu | Key Technical State | Key Risk |
| ---: | --- | ---: | --- | ---: | --- | --- |
| 1 | MU | 0.1843 | LOW | +6.0% | 60d momentum +173%, beta 4.24 | Weekly+monthly TD9 SELL_SETUP_9 (double exhaustion) |
| 2 | META | 0.1574 | LOW | +6.0% | Daily MACD bullish cross, beta 1.23 | 60d DD -21.2%, negative RS vs SPY |
| 3 | AMD | 0.1366 | LOW | +5.0% | 60d momentum +146%, beta 3.95 | Weekly TD9 SELL_SETUP_9 |
| 4 | PLTR | 0.1144 | LOW | +4.0% | Beta 0.88 (near-neutral) | Worst 60d DD in sample (-33.2%) |
| 5 | CAT | 0.0843 | LOW | +4.0% | Full daily/weekly/monthly MACD alignment | Weekly/monthly RSI overbought (81/78) |
| 6 | MSFT | 0.0676 | LOW | +3.0% | Lowest tech-mega-cap beta (0.52) | MACD BELOW_SIGNAL all 3 timeframes |
| 7 | AAPL | 0.0617 | LOW | +2.0% | Weekly/monthly MACD above signal | Modest daily momentum only |
| 8 | PG | 0.0595 | LOW | +2.0% | Lowest beta in sample (0.02) | Weak momentum (+3.3% 60d); entry `DELAYED` |
| 9 | MCK | 0.0568 | LOW | +2.0% | Negative beta (-0.66) | Negative momentum contradicts diversifier thesis; entry `DELAYED` |
| 10 | AMZN | 0.0529 | LOW | +1.0% | Daily MACD bullish cross | Monthly MACD bearish cross (timeframe conflict) |
| 11 | UNH | 0.0389 | LOW | +1.0% | 60d momentum +52% (2nd highest) | RSI approaching overbought; weekly TD9 SELL_SETUP_9 |
| 12 | GOOGL | 0.0259 | LOW | +1.0% | Monthly MACD above signal | Daily/weekly MACD below signal; beta 1.49 |

## Portfolio Analytics / No-Trade Rationale

No portfolio is proposed. Per `07_portfolio_proposal.md`, the investable set is empty (0 of 30 names clear the 3-of-4-factor-family Evidence Threshold; earnings-date data is independently `UNAVAILABLE` for all names). Per `rules.md § Downgrade to NO_TRADE` #1 ("Fewer than 5 names pass the investable threshold"), the correct status is `NO_TRADE`. `08_risk_review.md` reviewed and approved this conclusion without requesting revision.

## Assumptions and Limitations

1. **Sampled, not full, universe**: 30 of 515 index-union names were scored (Sampled Universe Protocol), because Yahoo Finance web fetch is blocked by organizational egress policy in this session and per-name IBKR fetch for all 515 names exceeds this session's practical tool-call budget. Percentiles are `SAMPLED_PCTL (n=30)`.
2. **Two of four factor families are structurally unavailable** (Fundamental, Sentiment/Positioning) — no fundamentals or positioning feed is connected via the IBKR MCP tools in this environment.
3. **No earnings-calendar feed** — every name's `Days to Earnings` is `UNAVAILABLE`, not confirmed-clear.
4. **No risk-free rate source** — Sharpe/Sortino/Treynor/IR ratios are not computed this run (would be `RAW_DIAGNOSTIC` at best, and were not attempted without a settled mu/sigma base beyond the monitoring sleeve).
5. All prices are grounded via Interactive Brokers MCP (`get_price_history`/`get_price_snapshot`), tagged `LIVE`, `DELAYED`, or `HISTORICAL` per the Price Sourcing Standard; none are illustrative or estimated.

## Next Scheduled Review

Per `runbook.md § Cadence`, the next pre-open run is scheduled for the next weekday at 07:27 ET (no durable cron job is currently active — see `00_run_manifest.md`). The daily evolution review for this run is logged in `13_evolution_log.md`.
