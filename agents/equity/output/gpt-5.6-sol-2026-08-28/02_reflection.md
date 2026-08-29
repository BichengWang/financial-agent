# 02 — Reflection · 2026-08-28

## 0. Prediction Settlement

All dated `15_predictions.json` packages were re-scanned with the canonical settlement ledger.
At fire, **2** keys were due; **0** settled; **2** remain due; conflicts **0**. Both are EQR
(L008):
`claude-opus-5|2026-07-26|2026-08-23` and
`gpt-5|2026-07-27|2026-08-24`. StockAnalysis rejects the stale symbol, Nasdaq no longer lists it,
CNBC resolves it to an unrelated foreign issuer, and VMRK is a possible successor. The system
therefore records `UNSETTLEABLE_CORPORATE_ACTION` and does not infer a conversion ratio.

| Type | Raw n | 28d eff_n | Hit rate | CI coverage | Mean z | Track A |
|---|---:|---:|---:|---:|---:|---|
| EQUITY_ALPHA | 1355 | 2 | 37.49% | 71.88% | -0.5553 | INSUFFICIENT_EFFECTIVE_N |
| MARKET_FORECAST | 201 | 2 | 40.11% | 90.55% | -0.1848 | INSUFFICIENT_EFFECTIVE_N |

Weighted equity rank IC is **-0.0495**. Confidence remains capped
at MEDIUM. No settlement table rows exist for this run because no due key was safely settleable.

## 1. Prior Run / MoM baseline selection

Window 2026-07-14..2026-08-07; target
2026-07-31. Selected **`agents/equity/output/gpt-5-2026-07-30`** with
**CROSS_MODEL_BASELINE** under Rule 8(a): gpt-5 is the same GPT model family as gpt-5.6-sol (L009).

| Candidate | Δ days | EQ n | Hit | CI | Mean alpha | Mean z | Disposition |
|---|---|---|---|---|---|---|---|
| agents/equity/output/gpt-5-2026-07-30 | 1 | 20 | 20.00% | 80.00% | -3.77% | -0.5917 | SELECTED |
| agents/equity/output/claude-opus-5-2026-07-30 | 1 | 24 | 16.67% | 66.67% | -7.20% | -0.8667 | TIED_ALTERNATIVE |
| agents/equity/output/claude-opus-5-2026-08-01 | 1 | 0 | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | TIED_ALTERNATIVE_NOT_YET_DUE |

The two matured July 30 books are qualitatively invariant: both have negative mean alpha and
sub-50% hit rates. Invariance across all ties is **UNAVAILABLE**, because the August 1 book targets
August 29 and is not due.

## 2. MoM Price & Return Table

| Ticker | Prior Date | Prior Price | Current Date | Current Price | MoM Return | SPY Return | Alpha | Hit/Miss | CI |
|---|---|---|---|---|---|---|---|---|---|
| PAYX | 2026-07-30 | $116.33 | 2026-08-27 | $126.48 | 8.73% | 3.97% | 4.76% | HIT | IN_CI; L159,L160,L161 |
| TRV | 2026-07-30 | $375.99 | 2026-08-27 | $369.33 | -1.77% | 3.97% | -5.74% | MISS | IN_CI; L162,L163,L164 |
| CTAS | 2026-07-30 | $206.79 | 2026-08-27 | $204.15 | -1.28% | 3.97% | -5.24% | MISS | IN_CI; L165,L166,L167 |
| WTW | 2026-07-30 | $336.05 | 2026-08-27 | $339.58 | 1.05% | 3.97% | -2.91% | MISS | IN_CI; L168,L169,L170 |
| ADP | 2026-07-30 | $263.87 | 2026-08-27 | $284.68 | 7.89% | 3.97% | 3.92% | HIT | IN_CI; L171,L172,L173 |
| AON | 2026-07-30 | $366.57 | 2026-08-27 | $349.56 | -4.64% | 3.97% | -8.61% | MISS | OUT_CI_LOW; L174,L175,L176 |
| PCG | 2026-07-30 | $17.78 | 2026-08-27 | $17.95 | 0.96% | 3.97% | -3.01% | MISS | IN_CI; L177,L178,L179 |
| LH | 2026-07-30 | $315.53 | 2026-08-27 | $336.54 | 6.66% | 3.97% | 2.69% | HIT | IN_CI; L180,L181,L182 |
| BBY | 2026-07-30 | $87.82 | 2026-08-27 | $83.56 | -4.85% | 3.97% | -8.82% | MISS | OUT_CI_LOW; L183,L184,L185 |
| INCY | 2026-07-30 | $122.99 | 2026-08-27 | $127.74 | 3.86% | 3.97% | -0.10% | MISS | IN_CI; L186,L187,L188 |
| MRSH | 2026-07-30 | $191.51 | 2026-08-27 | $190.00 | -0.79% | 3.97% | -4.75% | MISS | IN_CI; L189,L190,L191 |
| AWK | 2026-07-30 | $136.81 | 2026-08-27 | $136.69 | -0.09% | 3.97% | -4.05% | MISS | IN_CI; L192,L193,L194 |
| BXP | 2026-07-30 | $71.67 | 2026-08-27 | $69.97 | -2.37% | 3.97% | -6.34% | MISS | IN_CI; L195,L196,L197 |
| BRO | 2026-07-30 | $70.87 | 2026-08-27 | $71.39 | 0.73% | 3.97% | -3.23% | MISS | IN_CI; L198,L199,L200 |
| SJM | 2026-07-30 | $122.21 | 2026-08-27 | $131.84 | 7.88% | 3.97% | 3.91% | HIT | IN_CI; L201,L202,L203 |
| BAX | 2026-07-30 | $26.75 | 2026-08-27 | $25.93 | -3.07% | 3.97% | -7.03% | MISS | IN_CI; L204,L205,L206 |
| AAPL | 2026-07-30 | $333.43 | 2026-08-27 | $314.58 | -5.65% | 3.97% | -9.62% | MISS | OUT_CI_LOW; L207,L208,L209 |
| SYK | 2026-07-30 | $348.04 | 2026-08-27 | $322.12 | -7.45% | 3.97% | -11.41% | MISS | OUT_CI_LOW; L210,L211,L212 |
| PM | 2026-07-30 | $192.00 | 2026-08-27 | $190.48 | -0.79% | 3.97% | -4.76% | MISS | IN_CI; L213,L214,L215 |
| RTX | 2026-07-30 | $214.38 | 2026-08-27 | $212.08 | -1.07% | 3.97% | -5.04% | MISS | IN_CI; L216,L217,L218 |

Selected-book summary: n=20, hit rate 20.00%, CI coverage 80.00%, mean alpha -3.77%, mean z -0.5917.

## 3. Theme-Level Performance

The selected book's defensive/low-beta tilt **failed** against a rising benchmark: mean alpha was
-3.77% and only 4/20 forecasts were HIT. The negative result is consistent with the tied Claude
book, so it is not an artifact of the same-family tie break. This is an INFERRED assessment from
the ledger-backed MoM table and canonical metrics (L007).

## 4. Regime Shift Assessment

The current regime is **BULL** (L006); SPY remains above its 20d and 50d averages, while VIX
is 14.43. The prior book's defensive ordering did not participate in the benchmark path. Existing
factor weights are not changed because Track A evidence remains blocked at eff_n=2.

## 5. Carry-Forward Decisions

Decisions use the pre-binding `INDEX_UNION_PCTL (n=507)` cross-section: CARRY ≥80,
DOWNGRADE 60–80, DROP <60. DROP names were removed before final scoring.

| Ticker | Prior Score | Prior Thesis | MoM Return | Decision | Rationale |
|---|---|---|---|---|---|
| PAYX | +0.3734 | Price-led monitoring forecast; not investable while Fund_Z/Sent_Z remain unavailable. | 8.73% | DOWNGRADE | fell to 77.47 pctl (rank 115/507) — monitoring band only |
| TRV | +0.3636 | Price-led monitoring forecast; not investable while Fund_Z/Sent_Z remain unavailable. | -1.77% | DOWNGRADE | fell to 60.47 pctl (rank 201/507) — monitoring band only |
| CTAS | +0.3565 | Price-led monitoring forecast; not investable while Fund_Z/Sent_Z remain unavailable. | -1.28% | DROP | fell below the 60th-pctl rank floor to 54.74 (rank 230/507) |
| WTW | +0.3530 | Price-led monitoring forecast; not investable while Fund_Z/Sent_Z remain unavailable. | 1.05% | DOWNGRADE | fell to 74.51 pctl (rank 130/507) — monitoring band only |
| ADP | +0.3436 | Price-led monitoring forecast; not investable while Fund_Z/Sent_Z remain unavailable. | 7.89% | CARRY | still 87.94 pctl (rank 62/507) — investable-band percentile |
| AON | +0.3353 | Price-led monitoring forecast; not investable while Fund_Z/Sent_Z remain unavailable. | -4.64% | DROP | fell below the 60th-pctl rank floor to 56.92 (rank 219/507) |
| PCG | +0.3254 | Price-led monitoring forecast; not investable while Fund_Z/Sent_Z remain unavailable. | 0.96% | DROP | fell below the 60th-pctl rank floor to 30.24 (rank 354/507) |
| LH | +0.3062 | Price-led monitoring forecast; not investable while Fund_Z/Sent_Z remain unavailable. | 6.66% | CARRY | still 96.05 pctl (rank 21/507) — investable-band percentile |
| BBY | +0.3040 | Price-led monitoring forecast; not investable while Fund_Z/Sent_Z remain unavailable. | -4.85% | DOWNGRADE | fell to 73.32 pctl (rank 136/507) — monitoring band only |
| INCY | +0.2988 | Price-led monitoring forecast; not investable while Fund_Z/Sent_Z remain unavailable. | 3.86% | DOWNGRADE | fell to 75.49 pctl (rank 125/507) — monitoring band only |
| MRSH | +0.2968 | Price-led monitoring forecast; not investable while Fund_Z/Sent_Z remain unavailable. | -0.79% | DOWNGRADE | fell to 67.79 pctl (rank 164/507) — monitoring band only |
| AWK | +0.2892 | Price-led monitoring forecast; not investable while Fund_Z/Sent_Z remain unavailable. | -0.09% | DROP | fell below the 60th-pctl rank floor to 52.96 (rank 239/507) |
| BXP | +0.2837 | Price-led monitoring forecast; not investable while Fund_Z/Sent_Z remain unavailable. | -2.37% | DOWNGRADE | fell to 65.22 pctl (rank 177/507) — monitoring band only |
| BRO | +0.2795 | Price-led monitoring forecast; not investable while Fund_Z/Sent_Z remain unavailable. | 0.73% | DOWNGRADE | fell to 65.81 pctl (rank 174/507) — monitoring band only |
| SJM | +0.2791 | Price-led monitoring forecast; not investable while Fund_Z/Sent_Z remain unavailable. | 7.88% | CARRY | still 94.07 pctl (rank 31/507) — investable-band percentile |
| BAX | +0.2788 | Price-led monitoring forecast; not investable while Fund_Z/Sent_Z remain unavailable. | -3.07% | DOWNGRADE | fell to 66.40 pctl (rank 171/507) — monitoring band only |
| AAPL | +0.2750 | Price-led monitoring forecast; not investable while Fund_Z/Sent_Z remain unavailable. | -5.65% | DROP | fell below the 60th-pctl rank floor to 57.91 (rank 214/507) |
| SYK | +0.2703 | Price-led monitoring forecast; not investable while Fund_Z/Sent_Z remain unavailable. | -7.45% | DROP | fell below the 60th-pctl rank floor to 58.89 (rank 209/507) |
| PM | +0.2674 | Price-led monitoring forecast; not investable while Fund_Z/Sent_Z remain unavailable. | -0.79% | CARRY | still 85.97 pctl (rank 72/507) — investable-band percentile |
| RTX | +0.2656 | Price-led monitoring forecast; not investable while Fund_Z/Sent_Z remain unavailable. | -1.07% | DROP | fell below the 60th-pctl rank floor to 57.31 (rank 217/507) |

Counts: **4 CARRY**, **9 DOWNGRADE**,
**7 DROP**, **0 PROMOTE**.

## 6. Sign-Off

Baseline prices are HISTORICAL from the source ledger; August 27 closes are DELAYED and were
canonicalized by the prior post-close run. Reflection confidence: **MEDIUM** — all 20 selected-book
rows are settled, but the third tied book remains open. Structural issue: the two EQR keys require
human corporate-action reconciliation and remain deliberately due.
