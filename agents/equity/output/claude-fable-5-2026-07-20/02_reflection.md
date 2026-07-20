# 02 Reflection — 2026-07-20 (claude-fable-5)

Standalone MoM reflection per runbook.md §02. Monday intraday run (12:21 ET); every settlement and MoM price below is the 2026-07-17 close (last completed session), Nasdaq-historical primary verified by IBKR tool snapshots (nasdaq_verification_manifest.json; max divergence 0.186%). Ledger rows cited from 01_preflight.md.

## 0. Prediction Settlement

**Due inventory at run open: 68 keys** (canonical settlement ledger, `--as-of 2026-07-20`; settlement_manifest.json). All 68 are the June forecast basket republished across four weekend vintages — gpt-5 2026-06-20 (target 07-18), gpt-5 2026-06-21 + gemini-3.5-flash 2026-06-21 (target 07-19), gpt-5 2026-06-22 (target 07-20) — 14 equities + SPY/QQQ/SOXX each, identical 2026-06-18 entry bases. Weekend targets settle at the last close at-or-before target (`WEEKEND_TARGET`); today's-target records settle at the latest completed close because this run executes intraday (`TARGET_EQ_RUN_DATE`) per rules.md §Settlement Rules. Settle prices: L022–L038.

**Evidence-concentration note:** because the four vintages are copies of one basket, today's 68 settlements contribute four highly correlated observations per name, not independent evidence. The canonical key (model, vintage, ticker, type, target_date) keeps them distinct by design; rolling metrics below should be read with that concentration in mind.

**This run's settlements (56 EQUITY_ALPHA + 12 MARKET_FORECAST):** EQ 24/56 HIT (42.9%), 40/56 IN_CI (71.4%), mean z −0.368. MF 0/12 HIT on raw direction, 4/12 IN_CI, mean z −1.00 — every June core-ETF record forecast upside into a tape that finished lower (SOXX worst: entries near 600 vs 521.81 settle).

| Ticker | Vintage (model) | Entry | Target Date | mu | Settle 07-17 | Realized | SPY Return | Alpha | Direction | CI | z | Flag |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| AVGO | 2026-06-21 (gemini-3.5-flash) | 411.35 | 2026-07-19 | +1.0% | 370.825 | -9.85% | -0.46% | -9.39% | MISS | IN_CI | -0.58 | WEEKEND_TARGET |
| BAC | 2026-06-21 (gemini-3.5-flash) | 56.2 | 2026-07-19 | +3.0% | 61.27 | +9.02% | -0.46% | +9.48% | HIT | IN_CI | +0.97 | WEEKEND_TARGET |
| CAT | 2026-06-21 (gemini-3.5-flash) | 985.82 | 2026-07-19 | +6.0% | 880.28 | -10.71% | -0.46% | -10.24% | MISS | OUT_CI_LOW | -1.36 | WEEKEND_TARGET |
| CVX | 2026-06-21 (gemini-3.5-flash) | 173.63 | 2026-07-19 | +2.0% | 187.38 | +7.92% | -0.46% | +8.38% | HIT | IN_CI | +0.79 | WEEKEND_TARGET |
| EQIX | 2026-06-21 (gemini-3.5-flash) | 1092.19 | 2026-07-19 | +2.0% | 1020.0 | -6.61% | -0.46% | -6.15% | MISS | OUT_CI_LOW | -1.53 | WEEKEND_TARGET |
| ETN | 2026-06-21 (gemini-3.5-flash) | 421.77 | 2026-07-19 | +1.0% | 399.99 | -5.16% | -0.46% | -4.70% | MISS | IN_CI | -0.45 | WEEKEND_TARGET |
| FCX | 2026-06-21 (gemini-3.5-flash) | 68.68 | 2026-07-19 | +4.0% | 58.38 | -15.00% | -0.46% | -14.54% | MISS | OUT_CI_LOW | -1.21 | WEEKEND_TARGET |
| GE | 2026-06-21 (gemini-3.5-flash) | 357.64 | 2026-07-19 | +5.0% | 348.83 | -2.46% | -0.46% | -2.00% | MISS | IN_CI | -0.74 | WEEKEND_TARGET |
| GOOGL | 2026-06-21 (gemini-3.5-flash) | 368.03 | 2026-07-19 | +6.0% | 346.77 | -5.78% | -0.46% | -5.31% | MISS | OUT_CI_LOW | -1.42 | WEEKEND_TARGET |
| GS | 2026-06-21 (gemini-3.5-flash) | 1096.56 | 2026-07-19 | +5.0% | 1065.22 | -2.86% | -0.46% | -2.40% | MISS | IN_CI | -0.78 | WEEKEND_TARGET |
| JPM | 2026-06-21 (gemini-3.5-flash) | 325.22 | 2026-07-19 | +2.0% | 341.1 | +4.88% | -0.46% | +5.34% | HIT | IN_CI | +0.39 | WEEKEND_TARGET |
| LIN | 2026-06-21 (gemini-3.5-flash) | 512.15 | 2026-07-19 | +1.0% | 513.22 | +0.21% | -0.46% | +0.67% | HIT | IN_CI | -0.14 | WEEKEND_TARGET |
| LLY | 2026-06-21 (gemini-3.5-flash) | 1098.57 | 2026-07-19 | +4.0% | 1179.11 | +7.33% | -0.46% | +7.79% | HIT | IN_CI | +0.37 | WEEKEND_TARGET |
| QQQ | 2026-06-21 (gemini-3.5-flash) | 740.62 | 2026-07-19 | +2.9% | 695.33 | -6.12% | N/A | N/A | MISS (raw) | OUT_CI_LOW | -1.18 | WEEKEND_TARGET |
| SOXX | 2026-06-21 (gemini-3.5-flash) | 639.45 | 2026-07-19 | +5.6% | 521.81 | -18.40% | N/A | N/A | MISS (raw) | OUT_CI_LOW | -1.24 | WEEKEND_TARGET |
| SPY | 2026-06-21 (gemini-3.5-flash) | 746.74 | 2026-07-19 | +2.0% | 743.29 | -0.46% | N/A | N/A | MISS (raw) | IN_CI | -0.58 | WEEKEND_TARGET |
| UNH | 2026-06-21 (gemini-3.5-flash) | 400.96 | 2026-07-19 | +2.0% | 426.09 | +6.27% | -0.46% | +6.73% | HIT | IN_CI | +0.56 | WEEKEND_TARGET |
| AVGO | 2026-06-20 (gpt-5) | 411.35 | 2026-07-18 | +1.0% | 370.825 | -9.85% | -0.46% | -9.39% | MISS | IN_CI | -0.58 | WEEKEND_TARGET |
| BAC | 2026-06-20 (gpt-5) | 56.2 | 2026-07-18 | +3.0% | 61.27 | +9.02% | -0.46% | +9.48% | HIT | IN_CI | +0.97 | WEEKEND_TARGET |
| CAT | 2026-06-20 (gpt-5) | 985.82 | 2026-07-18 | +6.0% | 880.28 | -10.71% | -0.46% | -10.24% | MISS | OUT_CI_LOW | -1.36 | WEEKEND_TARGET |
| CVX | 2026-06-20 (gpt-5) | 173.63 | 2026-07-18 | +2.0% | 187.38 | +7.92% | -0.46% | +8.38% | HIT | IN_CI | +0.79 | WEEKEND_TARGET |
| EQIX | 2026-06-20 (gpt-5) | 1092.19 | 2026-07-18 | +2.0% | 1020.0 | -6.61% | -0.46% | -6.15% | MISS | OUT_CI_LOW | -1.53 | WEEKEND_TARGET |
| ETN | 2026-06-20 (gpt-5) | 421.77 | 2026-07-18 | +1.0% | 399.99 | -5.16% | -0.46% | -4.70% | MISS | IN_CI | -0.45 | WEEKEND_TARGET |
| FCX | 2026-06-20 (gpt-5) | 68.68 | 2026-07-18 | +4.0% | 58.38 | -15.00% | -0.46% | -14.54% | MISS | OUT_CI_LOW | -1.21 | WEEKEND_TARGET |
| GE | 2026-06-20 (gpt-5) | 357.64 | 2026-07-18 | +5.0% | 348.83 | -2.46% | -0.46% | -2.00% | MISS | IN_CI | -0.74 | WEEKEND_TARGET |
| GOOGL | 2026-06-20 (gpt-5) | 368.03 | 2026-07-18 | +6.0% | 346.77 | -5.78% | -0.46% | -5.31% | MISS | OUT_CI_LOW | -1.42 | WEEKEND_TARGET |
| GS | 2026-06-20 (gpt-5) | 1096.56 | 2026-07-18 | +5.0% | 1065.22 | -2.86% | -0.46% | -2.40% | MISS | IN_CI | -0.78 | WEEKEND_TARGET |
| JPM | 2026-06-20 (gpt-5) | 325.22 | 2026-07-18 | +2.0% | 341.1 | +4.88% | -0.46% | +5.34% | HIT | IN_CI | +0.39 | WEEKEND_TARGET |
| LIN | 2026-06-20 (gpt-5) | 512.15 | 2026-07-18 | +1.0% | 513.22 | +0.21% | -0.46% | +0.67% | HIT | IN_CI | -0.14 | WEEKEND_TARGET |
| LLY | 2026-06-20 (gpt-5) | 1098.57 | 2026-07-18 | +4.0% | 1179.11 | +7.33% | -0.46% | +7.79% | HIT | IN_CI | +0.37 | WEEKEND_TARGET |
| QQQ | 2026-06-20 (gpt-5) | 740.62 | 2026-07-18 | +2.9% | 695.33 | -6.12% | N/A | N/A | MISS (raw) | OUT_CI_LOW | -1.18 | WEEKEND_TARGET |
| SOXX | 2026-06-20 (gpt-5) | 639.45 | 2026-07-18 | +5.6% | 521.81 | -18.40% | N/A | N/A | MISS (raw) | OUT_CI_LOW | -1.24 | WEEKEND_TARGET |
| SPY | 2026-06-20 (gpt-5) | 746.74 | 2026-07-18 | +2.0% | 743.29 | -0.46% | N/A | N/A | MISS (raw) | IN_CI | -0.58 | WEEKEND_TARGET |
| UNH | 2026-06-20 (gpt-5) | 400.96 | 2026-07-18 | +2.0% | 426.09 | +6.27% | -0.46% | +6.73% | HIT | IN_CI | +0.56 | WEEKEND_TARGET |
| AVGO | 2026-06-21 (gpt-5) | 411.35 | 2026-07-19 | +1.0% | 370.825 | -9.85% | -0.46% | -9.39% | MISS | IN_CI | -0.58 | WEEKEND_TARGET |
| BAC | 2026-06-21 (gpt-5) | 56.2 | 2026-07-19 | +3.0% | 61.27 | +9.02% | -0.46% | +9.48% | HIT | IN_CI | +0.97 | WEEKEND_TARGET |
| CAT | 2026-06-21 (gpt-5) | 985.82 | 2026-07-19 | +6.0% | 880.28 | -10.71% | -0.46% | -10.24% | MISS | OUT_CI_LOW | -1.36 | WEEKEND_TARGET |
| CVX | 2026-06-21 (gpt-5) | 173.63 | 2026-07-19 | +2.0% | 187.38 | +7.92% | -0.46% | +8.38% | HIT | IN_CI | +0.79 | WEEKEND_TARGET |
| EQIX | 2026-06-21 (gpt-5) | 1092.19 | 2026-07-19 | +2.0% | 1020.0 | -6.61% | -0.46% | -6.15% | MISS | OUT_CI_LOW | -1.53 | WEEKEND_TARGET |
| ETN | 2026-06-21 (gpt-5) | 421.77 | 2026-07-19 | +1.0% | 399.99 | -5.16% | -0.46% | -4.70% | MISS | IN_CI | -0.45 | WEEKEND_TARGET |
| FCX | 2026-06-21 (gpt-5) | 68.68 | 2026-07-19 | +4.0% | 58.38 | -15.00% | -0.46% | -14.54% | MISS | OUT_CI_LOW | -1.21 | WEEKEND_TARGET |
| GE | 2026-06-21 (gpt-5) | 357.64 | 2026-07-19 | +5.0% | 348.83 | -2.46% | -0.46% | -2.00% | MISS | IN_CI | -0.74 | WEEKEND_TARGET |
| GOOGL | 2026-06-21 (gpt-5) | 368.03 | 2026-07-19 | +6.0% | 346.77 | -5.78% | -0.46% | -5.31% | MISS | OUT_CI_LOW | -1.42 | WEEKEND_TARGET |
| GS | 2026-06-21 (gpt-5) | 1096.56 | 2026-07-19 | +5.0% | 1065.22 | -2.86% | -0.46% | -2.40% | MISS | IN_CI | -0.78 | WEEKEND_TARGET |
| JPM | 2026-06-21 (gpt-5) | 325.22 | 2026-07-19 | +2.0% | 341.1 | +4.88% | -0.46% | +5.34% | HIT | IN_CI | +0.39 | WEEKEND_TARGET |
| LIN | 2026-06-21 (gpt-5) | 512.15 | 2026-07-19 | +1.0% | 513.22 | +0.21% | -0.46% | +0.67% | HIT | IN_CI | -0.14 | WEEKEND_TARGET |
| LLY | 2026-06-21 (gpt-5) | 1098.57 | 2026-07-19 | +4.0% | 1179.11 | +7.33% | -0.46% | +7.79% | HIT | IN_CI | +0.37 | WEEKEND_TARGET |
| QQQ | 2026-06-21 (gpt-5) | 740.62 | 2026-07-19 | +2.9% | 695.33 | -6.12% | N/A | N/A | MISS (raw) | OUT_CI_LOW | -1.18 | WEEKEND_TARGET |
| SOXX | 2026-06-21 (gpt-5) | 639.45 | 2026-07-19 | +5.6% | 521.81 | -18.40% | N/A | N/A | MISS (raw) | OUT_CI_LOW | -1.24 | WEEKEND_TARGET |
| SPY | 2026-06-21 (gpt-5) | 746.74 | 2026-07-19 | +2.0% | 743.29 | -0.46% | N/A | N/A | MISS (raw) | IN_CI | -0.58 | WEEKEND_TARGET |
| UNH | 2026-06-21 (gpt-5) | 400.96 | 2026-07-19 | +2.0% | 426.09 | +6.27% | -0.46% | +6.73% | HIT | IN_CI | +0.56 | WEEKEND_TARGET |
| AVGO | 2026-06-22 (gpt-5) | 411.35 | 2026-07-20 | +1.0% | 370.825 | -9.85% | -0.46% | -9.39% | MISS | IN_CI | -0.58 | TARGET_EQ_RUN_DATE |
| BAC | 2026-06-22 (gpt-5) | 56.2 | 2026-07-20 | +3.0% | 61.27 | +9.02% | -0.46% | +9.48% | HIT | IN_CI | +0.97 | TARGET_EQ_RUN_DATE |
| CAT | 2026-06-22 (gpt-5) | 985.82 | 2026-07-20 | +6.0% | 880.28 | -10.71% | -0.46% | -10.24% | MISS | OUT_CI_LOW | -1.36 | TARGET_EQ_RUN_DATE |
| CVX | 2026-06-22 (gpt-5) | 173.63 | 2026-07-20 | +2.0% | 187.38 | +7.92% | -0.46% | +8.38% | HIT | IN_CI | +0.79 | TARGET_EQ_RUN_DATE |
| EQIX | 2026-06-22 (gpt-5) | 1092.19 | 2026-07-20 | +2.0% | 1020.0 | -6.61% | -0.46% | -6.15% | MISS | OUT_CI_LOW | -1.53 | TARGET_EQ_RUN_DATE |
| ETN | 2026-06-22 (gpt-5) | 421.77 | 2026-07-20 | +1.0% | 399.99 | -5.16% | -0.46% | -4.70% | MISS | IN_CI | -0.45 | TARGET_EQ_RUN_DATE |
| FCX | 2026-06-22 (gpt-5) | 68.68 | 2026-07-20 | +4.0% | 58.38 | -15.00% | -0.46% | -14.54% | MISS | OUT_CI_LOW | -1.21 | TARGET_EQ_RUN_DATE |
| GE | 2026-06-22 (gpt-5) | 357.64 | 2026-07-20 | +5.0% | 348.83 | -2.46% | -0.46% | -2.00% | MISS | IN_CI | -0.74 | TARGET_EQ_RUN_DATE |
| GOOGL | 2026-06-22 (gpt-5) | 368.03 | 2026-07-20 | +6.0% | 346.77 | -5.78% | -0.46% | -5.31% | MISS | OUT_CI_LOW | -1.42 | TARGET_EQ_RUN_DATE |
| GS | 2026-06-22 (gpt-5) | 1096.56 | 2026-07-20 | +5.0% | 1065.22 | -2.86% | -0.46% | -2.40% | MISS | IN_CI | -0.78 | TARGET_EQ_RUN_DATE |
| JPM | 2026-06-22 (gpt-5) | 325.22 | 2026-07-20 | +2.0% | 341.1 | +4.88% | -0.46% | +5.34% | HIT | IN_CI | +0.39 | TARGET_EQ_RUN_DATE |
| LIN | 2026-06-22 (gpt-5) | 512.15 | 2026-07-20 | +1.0% | 513.22 | +0.21% | -0.46% | +0.67% | HIT | IN_CI | -0.14 | TARGET_EQ_RUN_DATE |
| LLY | 2026-06-22 (gpt-5) | 1098.57 | 2026-07-20 | +4.0% | 1179.11 | +7.33% | -0.46% | +7.79% | HIT | IN_CI | +0.37 | TARGET_EQ_RUN_DATE |
| QQQ | 2026-06-22 (gpt-5) | 740.62 | 2026-07-20 | +2.9% | 695.33 | -6.12% | N/A | N/A | MISS (raw) | OUT_CI_LOW | -1.18 | TARGET_EQ_RUN_DATE |
| SOXX | 2026-06-22 (gpt-5) | 639.45 | 2026-07-20 | +5.6% | 521.81 | -18.40% | N/A | N/A | MISS (raw) | OUT_CI_LOW | -1.24 | TARGET_EQ_RUN_DATE |
| SPY | 2026-06-22 (gpt-5) | 746.74 | 2026-07-20 | +2.0% | 743.29 | -0.46% | N/A | N/A | MISS (raw) | IN_CI | -0.58 | TARGET_EQ_RUN_DATE |
| UNH | 2026-06-22 (gpt-5) | 400.96 | 2026-07-20 | +2.0% | 426.09 | +6.27% | -0.46% | +6.73% | HIT | IN_CI | +0.56 | TARGET_EQ_RUN_DATE |
**Rolling calibration (canonical settlement ledger, post-settlement; settlement_manifest.json `rolling_metrics`):**

| Metric | EQUITY_ALPHA (n=175) | Healthy Range | Verdict |
|---|---|---|---|
| Hit rate | 51.4% | > 50% | Inside, barely |
| CI coverage | 77.1% | 55–85% (target 70%) | Healthy |
| Mean z | −0.24 | −0.5 to +0.5 | Inside; drifting negative |
| Rank IC (weighted, per-vintage) | **−0.049** | > 0 | **Failing → MEDIUM confidence cap binds** |

`MARKET_FORECAST` line (separate per rules.md): n=30, direction accuracy **20.0%**, CI coverage 60.0%, mean z −0.77. The market-forecast sleeve is now past the 20-record Track A evidence bar and is the primary calibration problem — taken up in 13_evolution_log.md.

Files scanned: all `agents/equity/output/*/15_predictions.json` (71 dated packages) via `settlement_ledger.py`; 369 candidate rows → 205 canonical (175 EQ + 30 MF), 77 audit-only, 87 rejected (pre-07-12 timing violations), 0 conflicts, due inventory 0 after this run.

## 1. Prior Run Summary

Prior same-model run: **claude-fable-5-2026-07-17** (Friday at-the-close) — NO_TRADE (14th consecutive on the family-coverage gate), regime NEUTRAL with HIGH_VOL watch, DELAYED mode, 23 EQUITY_ALPHA + 3 MARKET_FORECAST records published (all targets 2026-08-14, none due today). Top-5: DOC +0.414, MNST +0.408, EXPD +0.406, TRV +0.346, JBHT +0.337. gpt-5's last package is also 07-17 (pre-open); no other model has run since.

## 2. MoM Price & Return Table

Baseline: **claude-fable-5-2026-06-10** — the only same-model folder in the 45→21-day window (2026-06-05..2026-06-29); 12 days off the 06-22 target → **BASELINE_WINDOW_GAP** (L040-class row: L040/base row in 01). Prior prices are the baseline ledger's 06-10 entries (OFFICIAL from its 15_predictions.json); current prices are the 07-17 closes (L022–L038 / per-name rows). CI columns: the baseline's 07-08-target CIs settled canonically on 07-08 — not re-scored here; `IN_CI/OUT_CI` therefore N/A in this monthly table.

| Ticker | Prior Date | Prior Price | Current Date | Current Price | MoM Return | SPY Return | Alpha | Hit/Miss | Notes |
|---|---|---|---|---|---|---|---|---|---|
| MCK | 2026-06-10 | 790.22 | 2026-07-17 | 841.39 | +6.48% | +2.46% | +4.01% | HIT | prior adj 0.787 |
| COST | 2026-06-10 | 980.45 | 2026-07-17 | 940.87 | -4.04% | +2.46% | -6.50% | MISS | prior adj 0.691 |
| WMT | 2026-06-10 | 119.83 | 2026-07-17 | 114.24 | -4.66% | +2.46% | -7.13% | MISS | prior adj 0.624 |
| CVX | 2026-06-10 | 191.01 | 2026-07-17 | 187.38 | -1.90% | +2.46% | -4.36% | MISS | prior adj 0.55 |
| UNH | 2026-06-10 | 407.13 | 2026-07-17 | 426.09 | +4.66% | +2.46% | +2.20% | HIT | prior adj 0.541 |
| XOM | 2026-06-10 | 151.35 | 2026-07-17 | 147.36 | -2.64% | +2.46% | -5.10% | MISS | prior adj 0.522 |
| LIN | 2026-06-10 | 509.2 | 2026-07-17 | 513.22 | +0.79% | +2.46% | -1.67% | MISS | prior adj 0.51 |
| MU | 2026-06-10 | 891.66 | 2026-07-17 | 848.95 | -4.79% | +2.46% | -7.25% | MISS | prior adj 0.428 |
| LLY | 2026-06-10 | 1138.16 | 2026-07-17 | 1179.11 | +3.60% | +2.46% | +1.14% | HIT | prior adj 0.247 |
| NVDA | 2026-06-10 | 201.65 | 2026-07-17 | 202.81 | +0.58% | +2.46% | -1.89% | MISS | prior adj 0.175 |
| GOOGL | 2026-06-10 | 356.64 | 2026-07-17 | 346.77 | -2.77% | +2.46% | -5.23% | MISS | prior adj 0.162 |
| ABBV | 2026-06-10 | 225.82 | 2026-07-17 | 254.49 | +12.70% | +2.46% | +10.23% | HIT | prior adj 0.134 |
SPY 2026-06-10 → 2026-07-17: 725.43 → 743.29 = **+2.46%** (L039/mom_spy). Basket: **4/12 alpha-positive, mean alpha −1.80%** (vs −1.77% at the 07-17 check — stable drift). Note: ABBV 07-17 close here is 254.49 (Nasdaq historical consolidated); the 07-17 at-close package printed 254.59 (primary official close) — 0.04% tape-class divergence, disclosed, both grounded.

## 3. Theme-Level Performance

- **Validated — defensive pharma/managed care:** ABBV +10.23%, MCK +4.01%, UNH +2.20%, LLY +1.14% alpha. The only baseline theme with consistent positive alpha across both monthly checks.
- **Failed — mega-cap retail staples:** COST −6.50%, WMT −7.13%. Failed both checks; stays failed.
- **Failed — energy majors:** CVX −4.36%, XOM −5.10%. Crack-spread strength went to refiners (MPC ranks #14 today), not integrateds.
- **Failed/unstable — semis momentum:** MU −7.25%, NVDA −1.89%; MU has flipped sign at three consecutive monthly checks as the semis correction deepened (SOXX dd60 −20.3%, L016/blk_SOXX).
- **Partial — GOOGL:** −5.23% alpha; mega-cap tech underperformed the tape.

## 4. Regime Shift Assessment

Prior (06-10 vintage): BULL-leaning NEUTRAL, semis leadership. Current: **NEUTRAL with HIGH_VOL watch** — SPY 743.29 below MA20 745.02 and MA50 744.38 (L014/blk_SPY), VIX 18.77 < 20 trigger (L008), breadth still constructive at 63.4% above MA50 (L010), leadership rotated hard into low-vol defensives (REITs, insurers, staples, regionals — today's top-20). Factor-weight implication: unchanged weights, but Macro_Z's moderate-beta/low-vol tilt is doing the regime work; semis exposure remains a negative-selection signal until SOXX repairs its 20d RS (−13.27%, L017/rs).

## 5. Carry-Forward Decisions

| Ticker/Theme | Prior Score (07-17) | Prior Thesis | MoM Alpha | Decision | Rationale |
|---|---|---|---|---|---|
| UNH | +0.307 (#10) | Managed-care recovery post-print | +2.20% | **CARRY** | Alpha-positive both checks; ranks #41 (pctl 92.2) today on its own signal |
| LLY | +0.231 (#49) | GLP-1 defensive growth | +1.14% | **CARRY** | Alpha-positive; pctl 77.6 monitoring band |
| GE | +0.185 (#98) | Aerospace aftermarket | n/a (not in baseline) | **CARRY** | 07-17 PROMOTE held; pctl 68.8 monitoring band |
| ABBV | +0.107 (#176) | Skyrizi/Rinvoq momentum | +10.23% | **DOWNGRADE** | Best baseline alpha, but 07-31 print (11d, confirmed) −0.10 penalty pushes it below the 60th-pctl rank floor → unrankable this run (rejection log); revisit post-print |
| MCK | n/a | Distributor defensive | +4.01% | **DOWNGRADE** | Alpha-positive but pctl ~56 < 60 floor; not rankable, keep on watch |
| LIN | n/a (dropped 07-17) | Industrial gas quality | −1.67% | **DROP** | Settled MISS today (−1.7% alpha, 07-19 vintage); pctl 59.5 |
| COST/WMT/CVX/XOM/MU/NVDA/GOOGL | dropped earlier | — | all negative | **DROP (reaffirm)** | Failed both monthly checks |

Binding effect: CARRY names must appear in today's scored set (all three do, on their own ranks); DROP names stay out of the published sleeve absent new ledger evidence (none arrived).

## 6. Sign-Off

- Freshness: every settlement/MoM price is the 2026-07-17 close tagged DELAYED (fetched this run, ≤1 trading-day lag), dual-sourced Nasdaq + IBKR; baseline entries HISTORICAL/OFFICIAL from the 06-10 ledger.
- Reflection confidence: **MEDIUM** — settlement mechanics clean (0 conflicts, due 0), but the 68 settlements carry the four-copy concentration caveat, and the MoM baseline is 12d off target (BASELINE_WINDOW_GAP).
- Structural issues: (1) MF direction accuracy 20% over n=30 — past the Track A bar, addressed in 13; (2) the weekend-republication pattern (identical baskets, new vintage keys) inflates settled-n without adding information — flagged for the 07-31 structural review; (3) rank IC ≤ 0 sustains the MEDIUM cap → sleeve stays LOW.
