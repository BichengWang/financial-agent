# 00 Run Manifest — 2026-07-11

> **BACKFILLED 2026-07-12** — the 2026-07-11 session truncated after publishing 02, 03, `eligible_universe.txt`, `universe_summary.json`, `technical_indicators.json`, and `nasdaq_verification_manifest.json`. Everything else in this folder (00, 01, 04–16) was reconstructed on 2026-07-12 from the committed session data plus the identical, re-verified 2026-07-10 bars; each backfilled file carries its own banner and provenance.

| Field | Value |
| --- | --- |
| Date | 2026-07-11 (**Saturday — U.S. markets closed**; last completed session Friday 2026-07-10) |
| Model | claude-fable-5 |
| Run mode | Scheduled-task run of `investments/equity/daily_investment_system/main.md` (weekend rule: full REVIEW_ONLY set targeted) |
| Data mode | **DELAYED** — official 2026-07-10 closes; Yahoo v8 IP-throttled (HTTP 429) → inherited 2026-07-10 repaired series + current-session Nasdaq /chart re-verification **517/519 symbols at 0.0000% divergence** (retrieved 2026-07-11T16:03–16:11Z) + IBKR MCP closed-market snapshots reproducing the 07-09 closes |
| Status target | REVIEW_ONLY (weekend — no executable session) |
| Final status | **HALTED** — session truncated after stage 1 (process integrity: run ended mid-pipeline, before scoring, ledger, or review). Completed artifacts published per runbook §Output rule 3; the remainder backfilled 2026-07-12 |
| Agents executed | Orchestrator (reflection), Data/Regime — completed; Factor Scoring / Portfolio / Risk / Evolution — **not executed** (reconstructed retrospectively; see 05 banner) |
| Outstanding blockers | Fundamental + Sentiment families unwired; Yahoo IP throttle (2nd consecutive session; did not recur 07-12); session reliability (2nd consecutive truncation) |
| Reflection baseline | `investments/equity/output/claude-fable-5-2026-06-10` — SAME_MODEL_BASELINE (window 2026-05-27..2026-06-20, target 2026-06-13, baseline 3d from target, folder 31d old) |
| Prediction settlement summary | 0 settled — none due (scanned 40 ledgers, 801 OPEN rows; next wave 2026-07-12, 20 records). Rolling calibration carried at n=29 (hit 51.7%, CI 72.4%, mean z -0.218, weighted rank IC -0.007 — MEDIUM freeze active) |
| Source Ledger coverage | Reconstructed ledger: 191 rows — 60 OBSERVED / 130 DERIVED / 1 INFERRED (see 01 banner; rows L001–L047 carry the values the committed 02/03 cite) |
| Status eligibility | All 5 Required inputs grounded to the last completed session; REVIEW_ONLY target unreachable — run HALTED mid-pipeline |
| Core ETF Market Forecast Block | PRESENT in the committed 03 (SPY/QQQ/SOXX with mu derivation); **no MARKET_FORECAST prediction records exist** — the session died before 15 (see 15 note) |
| Universe | 515 union; **512 eligible** (SATS structural-stale, BF-B vendor gap this session, FDXF short history); INDEX_UNION_PCTL (n=512); sampled fallback NOT used |
| rf note | ^IRX 3.682% (2026-07-09 close, 2d lag disclosed); ratios use rf_1m 0.307% |

## State Transition Log

`PRECHECK -> REFLECTION (0 settled) -> DATA_OK -> [SESSION TRUNCATED -> HALTED]` — stages from TECHNICALS_OK onward reconstructed retrospectively 2026-07-12 (05–09); no contemporaneous forecasts exist for this date.

## GO-Gate Table (Required inputs only)

| Required Input | Status | Evidence | Blocks GO? |
| --- | --- | --- | --- |
| Grounded entry price | PASS | Inherited repaired series + same-session Nasdaq re-verification 517/519 @ 0.0000% | No |
| ~60 trading days history | PASS | 5y bars through 2026-07-10 | No |
| Sigma via fallback chain | PASS | REALIZED_VOL_30D computable universe-wide | No |
| Next earnings date | PASS (as of the session: fresh full-universe fetch cited in 03; manifest lost — backfill uses the 07-12 confirmed vintage) | No |
| Index-union universe | PASS | 503∪101−89 = 515; support artifacts published | No |

GO was never reachable: weekend rule (REVIEW_ONLY target) and the family gate; the terminal HALTED status reflects the truncation, not a data failure.

## Artifact Checklist

| Artifact | Status |
| --- | --- |
| 02, 03, eligible_universe.txt, universe_summary.json, technical_indicators.json, nasdaq_verification_manifest.json | PRESENT (contemporaneous) |
| 00, 01, 04, 05, 06, 07, 08, 09, 10, 11, 12, 13, 14, 16 | **BACKFILLED 2026-07-12** (banners + provenance per file) |
| 15_predictions.json | **PRESENT — empty by design**: no forecasts were recorded contemporaneously and none are created retroactively; the identical cross-section is recorded as OPEN forecasts in the 07-12 ledger |
