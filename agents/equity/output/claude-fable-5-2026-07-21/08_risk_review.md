# 08 Risk Review — 2026-07-21 (claude-fable-5)

Risk Committee review of the `05`/`06`/`07` package per `agents.md § Risk Committee Agent Prompt`.

## Review Checklist

1. **Fabricated or weakly supported inputs:** None found. All 513/514 eligible-universe prices, technical indicators, and derived metrics trace to `01` ledger rows citing Yahoo v8 chart fetches and `technical_indicators.json`. FDXF is correctly excluded rather than hand-filled.
2. **Overfitting / unvalidated signal claims:** None — Tech_Z/Macro_Z formulas are disclosed in `01`/`05` and applied uniformly across the universe; no per-name special-casing.
3. **Excessive event concentration:** **Flagged** — 5 of the top-20 carry earnings inside the buffered window, exceeding the 2-name NO_TRADE trigger. Correctly surfaced in `03` and `07`, not suppressed.
4. **Correlation / sector crowding:** Not computed (no portfolio drafted — feasibility pre-check failed first, correctly per Task 0 sequencing). No violation, since no weights were forced through despite this gap.
5. **Portfolio beta drift outside the band:** **Confirmed structural** — mean top-20 beta −0.175 against the 0.90-1.10 band; correctly identified as infeasible before any weights were drafted, per `07`.
6. **Thesis quality below stated confidence:** All 20 names carry `LOW` confidence, consistent with the structural family-count rule — no name overstates its confidence.
7. **Mismatch between report and shared rules:** None found. `Adj Score` formula, mu Calibration Table application, and Sigma Fallback Chain usage all match `rules.md` verbatim.
8. **Price/derived-field citation violations:** None — every `entry_price` in `05`/`06` carries `price_date` (2026-07-20) and `price_tag` (`DELAYED`); no name shows `target_price`/CI populated while `entry_price` is unverified.
9. **Sigma violations:** None — every published name's sigma cites `REALIZED_VOL_30D` explicitly; no round/unsourced sigma values found.
10. **Score-attribution violations:** None — every `Adj Score` in `05` carries a full score trace (family z-scores, DQ, penalties, positive/negative drivers, ledger-row pointer). Fund_Z/Sent_Z are correctly displayed as `0.00 (UNAVAILABLE)`, never as neutral-and-silently-counted.
11. **Source Ledger violations:** None — spot-checked 6 of 20 published names (TRV, SCHW, ADP, DOC, UNP, PSX) against `01`; all price, technical-indicator, and earnings-date claims trace to a ledger row.
12. **Live-sounding or stale-as-current claims:** None found — all `DELAYED` prices are dated 2026-07-20 explicitly; no "current"/"latest"/"validated" language used without a ledger citation.
13. **Improper GO-blocking:** None — all 5 Required inputs are grounded (`00` GO-Gate Table); the run correctly does **not** block on the missing Enhancing inputs (options IV, short interest, bid-ask, analyst tape, institutional flow, GICS sector) — it caps DQ/confidence instead, exactly as `rules.md § Input Classification` prescribes.
14. **Missing prediction records:** None — all 20 top-20 names plus SPY/QQQ/SOXX `MARKET_FORECAST` records are present in `15_predictions.json` with `score_explainability` populated for every `EQUITY_ALPHA` record.
15. **Technical indicator pack violations:** None — every TD-9/RSI/MACD value cites `technical_indicators.json`; no field is treated as a standalone trade signal (exhaustion flags are correctly used only as a penalty input, not a directional call).

## Decision

**APPROVE.** The package is internally consistent, fully ledger-backed, and correctly reaches `NO_TRADE` through two independent, disclosed channels: (1) the structural evidence-threshold gate (Fund_Z/Sent_Z universe-wide `UNAVAILABLE`), and (2) portfolio beta-band infeasibility plus earnings-window concentration on the candidate pool itself. No revision requested — there is nothing a revision pass could fix; both blockers are structural, not process errors.

**Final publication recommendation: NO_TRADE.**
