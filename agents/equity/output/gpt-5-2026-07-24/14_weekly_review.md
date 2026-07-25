# 14 Weekly Review — Friday 2026-07-24 (after close)

This run executed after the Friday 17:15 ET weekly parameter-review slot, so the review is substantive rather than a placeholder.

## Week in Review (2026-07-18 through 2026-07-24, all models)

- **Status line:** the 7 dated packages in the trailing seven-calendar-day window across claude-fable-5, claude-sonnet-5, gpt-5 converge on NO_TRADE. The repeated blocker is the same 2-of-4 production-family limitation, not missing Required market data (L010,L009).
- **Tape:** SPY closed 738.93, below its daily MA20/MA50 but with positive weekly/monthly structure. QQQ and SOXX retain negative 20-day SPY-relative strength (-5.12% and -16.34%), while SOXX is -19.54% below its 60-day high. The July 28–29 FOMC meeting remains inside the forecast horizon (L012,L014,L017,L021,L006).
- **Settlement/calibration:** canonical state is 189 equity and 33 market forecasts, with due=0 and conflicts=0. Equity hit rate is 52.91%, CI coverage 76.19%, mean z -0.2129, and weighted rank IC -0.093914 (L332,L333,L334).
- **Process controls:** the July 22 same-day `TARGET_DATE_CLOSE` clarification is effective. This run produced no new settlement row, but the canonical ledger revalidated all historical candidates under the new timing rule (L332).

## Parameter Review

| Parameter family | Decision | Rationale |
|---|---|---|
| Factor weights (0.30/0.30/0.25/0.15) | **No change** | A 0.05 Technical-to-Macro shift is proposed but lacks the required locked holdout replay (L336) |
| Equity mu calibration table | **No change** | Rank IC is non-positive, but no locked holdout replay demonstrates the required IR/hit-rate improvement (L333) |
| Core ETF priors | **No change** | Market direction accuracy is weak, but the evidence does not isolate a prior-table change from the current growth/semiconductor drawdown (L334,L019,L023) |
| Sigma sourcing | **No change** | Equity CI coverage remains inside the healthy 55%–85% range (L333) |
| Confidence calibration | **No change** | The MEDIUM cap from non-positive rank IC remains correct; two-family coverage lowers the published sleeve to LOW (L333,L010) |
| Protected risk limits | **No change** | No weekly evidence supports relaxing any protected limit (L336) |

## Weekly Decision

**NO_CHANGE_ACCEPTED.** The daily Track A Technical-to-Macro weight proposal remains deferred for lack of a disclosed holdout improvement. No Track B change is introduced because the July 22 settlement-timing clarification is already effective and the current run found no new schema inconsistency (L336,L332).

## Watch Items Into Next Week

1. Reassess the regime after the July 28–29 FOMC meeting; do not pre-emptively alter the NEUTRAL prior (L006,L011).
2. Run the locked Technical-to-Macro weight counterfactual on an independent holdout (L336).
3. Continue Phase 2 full-universe Fundamental/Sentiment coverage work; it remains the only path to a 3-of-4-capable production score (L010).
4. Monitor QQQ/SOXX daily weakness against still-positive weekly/monthly structure for a defensible NEUTRAL-to-HIGH_VOL transition (L018,L022).
