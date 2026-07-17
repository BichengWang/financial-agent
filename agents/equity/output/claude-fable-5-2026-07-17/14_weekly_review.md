# 14 Weekly Review — Friday 2026-07-17 (after close)

Due this run (Fri 17:15 ET slot; published ~17:00–17:30 ET window). gpt-5's same-date pre-open package correctly stubbed this as not-yet-due; this at-the-close run delivers it.

## Week in Review (Mon 07-13 – Fri 07-17, all models)

- **Status line:** every scoring run this week — gpt-5 (5 dailies), claude-fable-5 (07-13/07-14/07-15 + today), claude-haiku-4.5 (07-16) — published **NO_TRADE on the identical structural gate** (2/4 sourceable families). The system's abstention is consistent, cross-model, and correctly attributed; it is also now the sole blocker between healthy data and a publishable book.
- **Tape:** SPY rose through Wednesday (750.72 on 07-16) then broke Friday −1.01% to 743.15, closing below MA20/MA50 with a daily MACD bearish cross; VIX 15.67 (Wed) → 18.75 (Fri). Q2 earnings wave printed through the week (JPM/GS/MS/BAC/ELV/MTB/PNC/BNY → STT/UNH/GE/CFG/USB/TRV/RF/FITB/HBAN-class), rotating leadership into defensives and post-print financials by Friday's close.
- **Settlement/calibration:** canonical ledger grew to 119 EQ + 18 MF with 0 conflicts; weekly highlights — equity CI coverage 79.8% (healthy), hit rate 55.5%, weighted rank IC −0.009 (non-positive; five straight negative gpt-5 June vintages), MF direction 33% at n=18. The 07-15 strict-dedupe Track B and 07-14 timing conventions are holding up under multi-model concurrency (zero duplicate settlements in a two-runs-one-day week).

## Parameter Review (Evolution Agent, weekly scope)

| Parameter family | Decision | Rationale |
|---|---|---|
| Factor weights (0.30/0.30/0.25/0.15) | **No change** | Two families dark; reweighting the live pair would be overfitting to an incomplete architecture |
| mu Calibration Table / Core ETF priors | **No change** | Track A evidence bar not met: nothing settled since gpt-5's morning deferral (due 0); MF n=18 < 20 |
| Sigma sourcing (REALIZED_VOL_30D chain) | **No change** | CI coverage 79.8% in-band; no widening/tightening trigger |
| Exhaustion conventions (−0.05 / −1pp, band-floor suspension) | **No change** | Functioning as designed; 15/20 flagged names this run is tape information, not mis-calibration evidence |
| Confidence calibration | **No change** (MEDIUM cap sustained by rank IC ≤ 0) | Corrective path is family coverage (Phase 2), not label surgery |

Accepted this week (Track B lineage): 07-15 strict prediction-identity dedupe; 07-16 shadow-run milestone logging; 07-17 (today) at-the-close data path codification. All process-class; no protected rule touched.

## Watch Items Into Next Week

1. **HIGH_VOL trigger**: VIX close > 20 with SPY below both MAs → regime flips, SPY prior drops to 0.0%.
2. **Post-print entry cohort** (TRV/RF/FITB) — evaluate whether print-day momentum ranks persist or mean-revert; DOC's REIT-sigma live test settles on the 08-10 vintage.
3. **Baseline windows**: claude-fable-5-2026-07-01 ages past 21d on 07-22, ending the BASELINE_WINDOW_GAP era for this model.
4. **Phase 2 escalation** (standing): bulk fundamentals/sentiment across the full universe is the only path to a 3-of-4-capable run; every week without it is another week of structurally forced NO_TRADE.
