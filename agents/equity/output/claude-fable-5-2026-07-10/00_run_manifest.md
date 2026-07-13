# 00 Run Manifest — 2026-07-10

> **BACKFILLED 2026-07-12** — the 2026-07-10 session truncated (~22:45 ET / ~02:45Z) after publishing 01, 02, 03, 04, 10, 11, `15_predictions.json`, `eligible_universe.txt`, `universe_summary.json`, `technical_indicators.json`, `chart_repair_manifest.json`, and `nasdaq_close_manifest.json`, but before writing 00, 05–09, 12, 13, 14. Those nine artifacts were reconstructed on 2026-07-12 from the committed session data (each carries its own banner). The forecast record itself (15) was published contemporaneously — nothing in the backfill alters it.

| Field | Value |
| --- | --- |
| Date | 2026-07-10 (Friday — live session, executed post-close ~17:47–22:45 ET) |
| Model | claude-fable-5 |
| Run mode | Scheduled-task run of `investments/equity/daily_investment_system/main.md` |
| Data mode | **DELAYED** — official 2026-07-10 closing prints fetched post-close; Yahoo v8 IP-throttled (HTTP 429, three documented attempts) → inherited 2026-07-09 5y series + Nasdaq official-close tail repair 07-06..07-10 (517/519, retrieved 2026-07-11T02:05–02:11Z) + IBKR MCP corroboration (max divergence 0.244%, after-hours drift) |
| Status target | GO if live-data constraints pass; otherwise NO_TRADE |
| Final status | **NO_TRADE** (recorded contemporaneously in 15_predictions.json; family-coverage evidence threshold #2) |
| Retrieved at | Nasdaq /chart official closes 2026-07-11T02:05–02:11Z; last-sale /info corroboration 01:55–02:02Z; IBKR MCP 02:12–02:13Z; two-source verification universe-wide max 0.005% (WYNN) |
| Agents executed | Orchestrator, Data/Regime, Factor Scoring — completed; Portfolio Construction / Risk Committee / Evolution — **session truncated** (retrospective versions backfilled 2026-07-12) |
| Outstanding blockers | Fundamental + Sentiment families unwired (10th consecutive scoring run); Yahoo IP throttle (transient — did not recur 07-12) |
| Reflection baseline | `investments/equity/output/claude-fable-5-2026-06-10` — SAME_MODEL_BASELINE (window 2026-05-26..2026-06-19, target 2026-06-12, baseline 2d from target, folder 30d old) |
| Prediction settlement summary | 0 settled — none due (scanned 38 ledgers, 751 OPEN rows); next wave 2026-07-12 (20 records). Rolling calibration carried at n=29: hit 51.7%, CI 72.4%, mean z -0.218, weighted rank IC -0.007 (MEDIUM freeze active) |
| Source Ledger coverage | OBSERVED 44; DERIVED 123; INFERRED 24; ILLUSTRATIVE 0; UNAVAILABLE 0 (191 rows) |
| Status eligibility | All 5 Required inputs grounded → GO-eligible on data; **NO_TRADE on evidence thresholds** (0 investable < 5) |
| Core ETF Market Forecast Block | PRESENT — 03 + three MARKET_FORECAST records in 15 |
| Universe | 515 union; **512 eligible** (SATS structural-stale, BF-B Nasdaq vendor gap, FDXF short history); INDEX_UNION_PCTL (n=512); sampled fallback NOT used |
| rf note | ^IRX 3.682% (2026-07-09 close, 1d lag disclosed — no fetchable 07-10 print); ratios use rf_1m 0.307% |

## State Transition Log

`PRECHECK -> REFLECTION (0 settled) -> DATA_OK (Nasdaq tail repair) -> TECHNICALS_OK -> SCORED -> [SESSION TRUNCATED]` — the prediction ledger (15) published before truncation; `PORTFOLIO_DRAFT / RISK_REVIEW / PUBLISHED / EVOLUTION_REVIEW` completed retrospectively 2026-07-12 with recorded status NO_TRADE upheld.

## GO-Gate Table (Required inputs only)

| Required Input | Status | Evidence | Blocks GO? |
| --- | --- | --- | --- |
| Grounded entry price | PASS | Official Nasdaq closes + inherited verified series; universe-wide two-source max 0.005% | No |
| ~60 trading days history | PASS | 5y bars through 2026-07-10 (repaired) for 519 symbols | No |
| Sigma via fallback chain | PASS | REALIZED_VOL_30D for every published name and ETF | No |
| Next earnings date | PASS | 384-name cadence-estimate map (±5d, INFERRED); 179 inside ≤19d buffered window penalized | No |
| Index-union universe | PASS | 503∪101−89 = 515; support artifacts published | No |

## Artifact Checklist

| Artifact | Status |
| --- | --- |
| 01–04, 10, 11, 15, support | PRESENT (contemporaneous) |
| 00, 05, 06, 07, 08, 09, 12, 13, 14 | **BACKFILLED 2026-07-12** (each carries a banner + provenance) |
| 15_predictions.json (24 EQUITY_ALPHA + 3 MARKET_FORECAST, 0 settlements) | PRESENT — publishing gate satisfied contemporaneously |
