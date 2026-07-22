# 08 Risk Review — 2026-07-22

## Committee Decision: `APPROVE` (as `NO_TRADE`)

The `07_portfolio_proposal.md` recommendation of `NO_TRADE` is approved as-is — no revision requested. There is no portfolio to challenge on sizing or composition grounds; the review below focuses on whether the upstream research artifacts (`01`–`06`) are internally consistent and free of fabrication before publication.

## Review Checklist

1. **Fabricated or weakly supported inputs:** None found. Every entry price in `05`/`06` carries `price_date`/`price_tag` and is grounded per the Price Sourcing Standard (Nasdaq quote-info official-close marker, cross-checked once against IBKR for SPY). Every `sigma` states `REALIZED_VOL_30D` as its source.
2. **Overfitting / unvalidated signal claims:** Tech_Z and Macro_Z use the same fixed signal menus and equal-weighting as every prior dated package (momentum/RS/volume/MA for Tech; realized vol/drawdown/beta-distance for Macro) — no new signal was introduced or curve-fit for today's names.
3. **Excessive event concentration:** Confirmed — 13 of 26 monitor-sleeve names carry an earnings-window penalty this cycle, and TMO reports tomorrow (1 day out). Correctly disclosed in `05`, `06`, and `07`; correctly cited as a secondary (non-binding) infeasibility factor in `07`, not silently absorbed into the score without penalty.
4. **Correlation / sector crowding:** Confirmed — Financials are 30.8% of the monitor sleeve (8/26 names). Correctly flagged in `07_portfolio_proposal.md § Secondary Infeasibility Evidence`; no portfolio was constructed, so no live crowding exists, but the disclosure is required for any future run that might promote this sleeve toward investable status.
5. **Portfolio beta drift outside the band:** N/A — no portfolio exists.
6. **Thesis quality below stated confidence:** Consistent — every name is `LOW` confidence, and every thesis is explicitly labeled `INFERRED` (sector + momentum/RS narrative), not asserted as fact. No name claims a fundamental or sentiment catalyst it cannot support.
7. **Mismatch between report and shared rules:** None found. The `NO_TRADE` status, the 26-name monitor-only publication, the mu-table application without sleeve override, and the DQ=0.80 multiplier all trace cleanly to `rules.md`.
8. **Price/derived-field citation violations:** None found. No `entry_price = N/A - unverified` appears anywhere in the published set; every `target_price`/CI bound is computed only where `entry_price` and `sigma` are both grounded.
9. **Sigma violations:** None found. Every published `sigma` states `REALIZED_VOL_30D` with an observation date; no blanket `sigma = UNAVAILABLE` appears anywhere in the ranked or monitor sleeve, satisfying the Sigma Fallback Chain's anti-caution-collapse requirement.
10. **Score-attribution violations:** None found. Every name's `Adj Score` in `05_factor_scores.md § Score Attribution` discloses `Fund_Z`, `Tech_Z`, `Sent_Z`, `Macro_Z`, `Composite_Z`, `DQ`, `Penalties`, and named top positive/negative drivers. `Fund_Z`/`Sent_Z` are explicitly `0.00 (UNAVAILABLE)`, never presented as neutral-but-supportive.
11. **Source Ledger violations:** None found. `01_preflight.md` carries 313 rows covering universe construction, macro (VIX, rf), Core ETF forecast inputs, settlement prices, and every candidate's entry price + derived technical/risk metrics.
12. **Live-sounding or stale-as-current claims:** None found. All 2026-07-22 entry prices are tagged `DELAYED` (not `LIVE`), and the technical/historical basis is explicitly disclosed as 2026-07-21 throughout — no artifact describes yesterday's data as "current."
13. **Improper GO-blocking:** Reviewed carefully — the `NO_TRADE` status is driven by evidence threshold #2 (a Required-tier factor-scoring gate under `rules.md § Evidence Thresholds`, not an Enhancing-input shortfall), so this is not a case of improperly blocking `GO` on missing Enhancing inputs (options IV/skew, short interest, etc., which are indeed missing but correctly *not* cited as the blocking reason anywhere in `00`, `05`, or `07`).
14. **Missing prediction records:** None found. All 26 monitor-sleeve names plus the 3 Core ETF `MARKET_FORECAST` records (SPY/QQQ/SOXX) are present in `15_predictions.json`, each with a complete `score_explainability` block (or `null` for the market-forecast records, as permitted). 17 settlements from `gpt-5-2026-06-24` are included in the same file's `settlements` block.
15. **Technical indicator pack violations:** None found. Every TD-9/RSI/MACD/MA/momentum/RS field in `05`/`06` cites `technical_indicators.json` lineage; TD-9 setup-9 and RSI overbought readings are treated strictly as penalty/confidence inputs (technical exhaustion flag), never as standalone buy/sell signals; FDXF's script failure is disclosed as `UNAVAILABLE`, not hidden.

## Top Three Concerns (severity order)

1. **Standing structural gap (carried forward, not new):** Fund_Z/Sent_Z remain unpromoted, which mechanically caps every run at `NO_TRADE`/`MONITOR`-only regardless of technical signal quality. This is a process limitation, not a data-integrity failure — flagged again in `13_evolution_log.md`, consistent with every dated package since 2026-07-15.
2. **Earnings-season concentration:** the current top-ranked technical names are disproportionately about to report (13/26 penalized, one tomorrow). If Fund_Z/Sent_Z were ever promoted without a corresponding review of event-risk sizing, a mechanically-constructed portfolio from today's exact ranked list would still likely breach the 2-name earnings-concentration guardrail.
3. **SOXX beta estimate (3.82) is regime-dependent and elevated versus SOXX's typical historical range (~1.3–1.8)** (`03_regime_and_data.md`) — correctly disclosed as such rather than smoothed into a "normal" number, but any downstream consumer of the Core ETF Market Forecast Block should treat the SOXX mu derivation (`beta × SPY mu`) as sensitive to this idiosyncratic-vol window, not a stable structural estimate.

## Required Fixes

None — no revision requested. Publish as `NO_TRADE`.

## Final Publication Recommendation

**`NO_TRADE`**
