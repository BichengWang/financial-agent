# 08 Risk Review

## Committee Decision: **APPROVE** publication as **NO_TRADE**

## Checks

1. **Fabrication / price lineage** — PASS. Every published entry price is a live intraday print with per-ticker URL + retrieved_at (2026-07-07T15:52:47Z–16:02:07Z manifest), second-sourced vs Nasdaq (2026-07-07T16:05:51Z–16:06:15Z, max divergence 0.772% < 1% on all 34 checked symbols) and IBKR-corroborated on the ETFs (live session, `is_close: false`, max 0.168%). No bare numeric prices; every table field carries LIVE/HISTORICAL tags with observation dates.
2. **Sigma discipline** — PASS. All 22 names + 3 ETFs use REALIZED_VOL_30D with formula and history rows cited; no round sigmas, no blanket UNAVAILABLE.
3. **Score attribution** — PASS. Every Adj Score shows the full trace with family z-scores, DQ 0.80, penalties; UNAVAILABLE families displayed as 0.00 (UNAVAILABLE), never neutral-positive; missing metrics never counted supportive.
4. **mu calibration** — PASS. All mu from the percentile band; only documented -1pp exhaustion adjustments; clamp ±2pp respected (max applied |adj| = 1pp).
5. **Technical indicator lineage** — PASS. All TD-9/RSI/MACD/MA/momentum/VR/RS values cite technical_indicators.json (2026-07-07T16:02:20Z) + underlying history rows; exhaustion flags used as penalties only, never standalone signals. Note: 16/22 published names carry an exhaustion or high-vol flag — sleeve-level technical extension remains a monitoring concern (2nd consecutive day).
6. **GO-blocking discipline** — PASS. All five Required inputs grounded; the block is evidence threshold #2 (family coverage), correctly treated as a data-quality/coverage limitation producing NO_TRADE, not as an improper Enhancing-input GO block. Conversely, no GO was attempted with missing Required inputs.
7. **Prediction records** — PASS. 22 EQUITY_ALPHA records (each with score_explainability and ledger-backed benchmark_price SPY 747.62 @ 2026-07-07) + 3 MARKET_FORECAST records (SPY/QQQ/SOXX with mu_derivation blocks) + settlements: [] in 15_predictions.json.
8. **Event concentration** — NOTED. 35 penalized names universe-wide; in the published sleeve, DAL reports in ~2 days (est 2026-07-09 ±5d) with a fresh daily MACD BEARISH_CROSS. Because the sleeve is monitoring-only, the >2-names-inside-14d NO_TRADE trigger is not additionally binding (the run is already NO_TRADE); flagged for any GO run this week — Q2 season opens Thursday.
9. **Live-sounding language** — PASS. "Live/intraday" claims cite the LIVE-tagged fetch rows; no stale-as-current claims found.
10. **Carry-forward bindings** — PASS. DROP/DOWNGRADE/CARRY from 02 §5 enforced in 05/06 (verified: no DROP name in the published sleeve; UNH out; LIN/ABBV appended with full blocks; LLY ranked naturally).
11. **Settlement readiness** — NOTED (forward obligation). Tomorrow's run must settle the 12-record 06-10 vintage on grounded 2026-07-08 prices (alpha vs recorded SPY 728.31) and report the first realized calibration metrics. Any failure to fetch those prices is a publishing failure, not an excuse.

## Top Three Concerns (severity order)

1. **Two-family scoring persists** (7th consecutive run) — the evidence gate makes every trading-day run NO_TRADE by construction; the standing Track B amendment awaits HUMAN_REVIEW (see 13). Until decided, the system publishes settleable paper forecasts only.
2. **Sleeve-wide long-momentum exposure into an opening earnings season** — 16/22 names flagged stretched, the sleeve is uniformly long 60d momentum, and today's -7% SOXX session shows how fast that factor can unwind; a broader momentum break would hit the whole book at once. Mitigated by LOW confidence and the -1pp mu haircuts.
3. **Intraday-partial-bar basis** — entries and indicators use a ~38%-elapsed session; today's bar can still move materially into the close (yesterday's SOXX +4% pop became today's -7% break). Settlement on target dates uses those days' grounded prices regardless.

## Final Publication Recommendation

**NO_TRADE** — inputs valid and grounded, no investable set at the required evidence bar. Publish the full monitoring package with prediction records.
