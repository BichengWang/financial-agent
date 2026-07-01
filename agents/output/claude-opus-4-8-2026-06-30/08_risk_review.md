# 08 Risk Review — Committee Decision

Run `claude-opus-4-8` · 2026-06-30. Adversarial review of the (null) portfolio and the `NO_TRADE` recommendation.

## Decision: **CONFIRM NO_TRADE** (publish analysis + paper monitoring forecasts)

The recommendation is sound and over-determined. Two independent protected-rule constraints (investable count < 5; beta band infeasible under the 5% cap) each force NO_TRADE, and the supporting evidence is computed and ledger-backed. No portfolio to approve/revise; the committee verifies grounding integrity and the prediction record.

## Top Three Concerns (severity order)

1. **Proxy factor families (HIGH).** Fundamental and Sentiment are price-derived proxies, not independent feeds (04/05). Momentum/RS overlap across families inflates apparent multi-family confirmation. *Mitigation in place:* DQ held at 0.80, confidence capped ≤ MEDIUM, "no family > 50% conviction" gate applied — which is precisely what disqualified the momentum-only names (AMD/CAT/MU/GE). Acceptable for a NO_TRADE/paper run; would need real feeds before any GO.
2. **Rotation-distorted 60d betas (MEDIUM).** The investable-grade names' near-zero/negative betas are a 60-session artifact. This is the mechanical cause of the beta-band infeasibility. The committee accepts the computed betas (rules mandate the 60d window) but flags that the *band itself* vs realized rotation betas is the recurring blocker — routed to evolution (13).
3. **Zero settled predictions in system history (MEDIUM).** Calibration metrics are `INSUFFICIENT_SETTLED_N`; the engine is unvalidated until the first maturity wave (~2026-07-08). Today's 15 paper forecasts are part of earning that evidence.

## Checklist Review (`agents.md § Risk Committee`)

| # | Check | Finding |
|---|---|---|
| 1 | Fabricated/weak inputs | None. 7 names IBKR-LIVE-grounded; full universe validated within 0.30% of connected tool (01). |
| 2 | Overfitting / unvalidated signal | Proxy overlap disclosed; DQ 0.80; no HIGH confidence. No signal claimed as validated. |
| 3 | Event concentration | Q2 earnings inside horizon flagged; UNH/BAC/JPM/JNJ ~14–15d carry penalty + LOW conf. |
| 4 | Correlation / sector crowding | Avg pairwise corr 0.05–0.08 (L208) — not binding. |
| 5 | Beta drift | The core issue: max achievable beta 0.03–0.59 << 0.90. Correctly → NO_TRADE, not a forced book. |
| 6 | Thesis vs confidence | All ≤ MEDIUM; exhausted/earnings names LOW. Consistent. |
| 7 | Report vs rules mismatch | None found. |
| 8 | Price/target citation | Every entry has price_date + tag (LIVE/DELAYED); targets/CI derived from grounded entry + table mu. No target on an unverified price. |
| 9 | Sigma violations | Every σ = REALIZED_VOL_30D with source; no blanket UNAVAILABLE; every ranked name settleable. ✓ |
| 10 | Score-attribution | Every Adj has trace, 4 family z's, DQ, penalties, ≥ drivers, ledger rows (05, 15). ✓ |
| 11 | Source Ledger | Prices, σ, β, DD, momentum, RS, TD9/RSI/MACD all in 01. ✓ |
| 12 | Live-sounding/stale | Prices tagged; "validated" used only for the documented cross-check; no unsupported "current/closed at." ✓ |
| 13 | Improper GO-blocking | Enhancing inputs (options/short/analyst/rf) are `UNAVAILABLE` → confidence/DQ caps, **not** GO blockers. NO_TRADE rests on protected rules (count, beta band), not on missing Enhancing feeds. ✓ |
| 14 | Missing prediction records | 15 equity records (every ranked name, both sleeves) + 3 ETF MARKET_FORECAST (SPY/QQQ/SOXX) + `settlements: []` with NO_PREDICTION_LEDGER note. `score_explainability` present on all equity records. ✓ |
| 15 | Technical pack violations | RSI/MACD/TD9 cite technical_indicators.json; TD9-9/RSI-extreme treated as exhaustion (penalty), not signals; no hidden script failures (38/38 OK). ✓ |

## Required Fixes

None blocking. One documentation note already satisfied: the manifest GO-Gate Table must show all five Required inputs grounded with NO_TRADE resting on portfolio-construction constraints (verified in 00).

## Final Publication Recommendation

**NO_TRADE.** Publish the full analysis, the Core ETF forecast, and the 15-name paper monitoring sleeve with prediction records. Route the structural beta-band-vs-rotation finding and the zero-settled-predictions gap to `13_evolution_log.md`.
