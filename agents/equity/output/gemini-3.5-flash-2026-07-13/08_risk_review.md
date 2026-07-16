# 08 Risk Review — 2026-07-13

## Committee Decision: **APPROVE for publication as NO_TRADE** (no revision required)

## Checks Performed (rules.md §Risk Committee checklist)

1. **Price/target lineage** — every published entry_price is DELAYED 2026-07-10 with date+tag and a ledger row; targets = entry×(1+mu) exactly; CI bounds = entry×(1+mu±1.04σ). Spot-verified DVA (232.80×1.05=244.44 ✓), FFIV (430.39×1.06=456.21 ✓), ABBV (248.08×1.01=250.56 ✓). PASS.
2. **Price verification** — 12/12 available IBKR priorClose fields match Nasdaq closes exactly; 15 others corroborated within premarket tolerance; the one >1.5% delta (HUM +1.73%) is a live premarket move on a name with no priorClose field, not a source disagreement (L016). PASS with note.
3. **Sigma lineage** — all 27 sigmas are REALIZED_VOL_30D with formula rows; no round free-handed sigma; MRNA's 25.5% (widest) traces to its actual 30d return stdev. PASS.
4. **Score attribution** — 24/24 names carry full traces (family z, DQ 0.80, penalties, drivers, ledger rows); missing families displayed 0.00 (UNAVAILABLE), never supportive; Sortino honestly n/a rather than imputed. PASS.
5. **Metric ledger coverage** — 223 ledger rows; every table value cross-references L-rows; settlement and MoM prices each have rows (L024-L055). PASS.
6. **Kelly discipline** — all 0.25×Kelly values cap-bound at 0.050 (5% NAV); none ≤0; none below the 2% NAV penalty line. PASS (academic — no sizing occurred).
7. **Technical indicator lineage** — all TD9/RSI/MACD/MA/momentum/VR/RS values trace to technical_indicators.json (L003) computed from the fetched bars; TD9-9/RSI-overbought treated as exhaustion penalties (-0.05, disclosed rule L022), never standalone signals; the one monthly-alignment gap (LIN) is displayed UNAVAILABLE. PASS.
8. **GO-blocking discipline** — the NO_TRADE arises from evidence threshold #2 (families) and stop-criteria downgrade #1 (<5 investable), NOT from missing Enhancing inputs; all five Required inputs are grounded (00 §GO-Gate). No improper GO-block. PASS.
9. **Prediction-record completeness** — 24 EQUITY_ALPHA records with score_explainability + benchmark_price, 3 MARKET_FORECAST records, 20 settlements recorded. `15_predictions.json` present → the run may transition to PUBLISHED. PASS.
10. **Live-sounding language** — the 03 premarket note is the only live claim; it cites IBKR retrieval timestamps (L017) and is excluded from scoring. PASS.

## Top Three Concerns (severity order)

1. **REIT sigma calibration (n=3 OUT_CI_LOW)** — PLD broke low again today (z -1.20); DOC sits at rank 7 with a 7.8% sigma. If DOC settles OUT_CI_LOW on 08-10, the evolution agent should propose a REIT-specific sigma-floor (Track A, needs ≥20 settled). Today: recorded, monitored, not actionable.
2. **Family-gate permanence** — 11th consecutive run where 2/4 families structurally forces NO_TRADE/REVIEW_ONLY. The standing HUMAN_REVIEW escalation (wire a fundamentals/sentiment source, or formally accept a 2-family investable standard) is the single highest-leverage open item in the system. Re-flagged in 13.
3. **Event-season density** — 23 of the pre-penalty top-50 are inside the ≤14d window this week; the published sleeve is therefore survivorship-shaped (what's left after the wave). Re-run composition materially changes after 07-17; treat this week's monitor sleeve accordingly.

## Final Publication Recommendation: **NO_TRADE** — publish full package.
