# 13 Evolution Log — 2026-07-15

## Run Context

| Field | Value |
|---|---|
| Date / Status / Regime | 2026-07-15 / NO_TRADE (weekday, family gate, 13th consecutive) / NEUTRAL (10th) |
| Evaluation window | Trailing 7 days: claude-fable-5 07-08..07-14, gpt-5 07-08..07-14, gemini-3.5-flash 07-13 (uncommitted working-tree package) — all models, all packages |
| Ledger status | 17 settled this run (gpt-5 06-17 vintage); **corrected rolling base: 91 EQ + 12 MF distinct** (49 prior ledger files, 1,001 records, 204 raw settlement rows scanned) |
| Baseline flag | SAME_MODEL_BASELINE (claude-fable-5-2026-06-10), no gap flag |

## What Worked

1. **The codified source chain absorbed its third consecutive Yahoo-blocked session without drama** — and produced the cleanest verification set yet (16/17 exact; the 17th was not an error but an ex-dividend adjustment the check itself surfaced). The chain now also catches corporate-action noise, not just outages.
2. **Sigma honesty produced the ledger's first perfect CI sweep on a 14-name vintage** (06-17: 14/14 IN_CI including FCX's −10.3%), with mean z −0.013 — near-zero aggregate bias at the vintage level.
3. **The confirmed-dates preflight caught six same-day window flips** (FTNT/HUM/LII/ESS/MAS/EBAY all at exactly 14d) and correctly reclassified nine vendor-empty names as print-week — without it, eight names scored on pre-print closes would have ranked penalty-free.
4. **Financials re-entry called a day early played out**: yesterday's "expect the complex to re-enter as penalties clear" materialized as BAC/GS/MS/ELV/STT/JPM percentiles in the 94–98 range — all correctly held behind event gates rather than published as conviction.

## What Failed / Weak Spots

1. **The rolling calibration base was over-counted ~48%** (reported 135 EQ; true distinct 77 before today). Cross-model duplicate settlements of the same prediction were tallied as independent observations, and 12 settlements were double-keyed under a missing-vintage variant. Every calibration read since 07-12 was computed on an inflated n — directionally the metrics survive (hit rate 55.6%→59.3%, CI 77.8%→83.5%, mean z −0.18→−0.14 on the corrected base), but MF direction is materially worse deduped (4/12 vs the 5/12-of-inflated-12 previously read).
2. **Rank IC: third consecutive negative vintage** (−0.083, −0.046, −0.248), weighted mean decayed to +0.040 (n=91). Today's inversion is textbook: the vintage's +6% mu names delivered the worst alpha (FCX −11.8%) while its +1% tail delivered the best (AAPL +4.9%). The momentum-led composite still cannot order names in a flat, thematically-rotating tape.
3. **Hand-transcription of numeric tables produced a publishable error caught at review**: an early 06 draft carried target/CI values that disagreed with the computed blocks (9 names affected; regenerated from `final_tables` before publication — 08 §2). The artifact-generation pattern (compute → render programmatically → hand-write narrative only) must extend to *every* numeric table, including summary artifacts.
4. **Fund/Sent unwiring: 13th consecutive run** — unchanged structural blocker.

## Primary Diagnosis

**Source grounding (evaluation-side)** — the settlement double-count is this run's clearest, most consequential finding: the system's own scorecard was mismeasured. Factor-calibration evidence (IC decay, MF mu bias) continues to accumulate but remains below its Track A thresholds.

## Proposed Change (exactly one)

- **Classification: Track B (process/reporting correction — settlement-identity dedupe for rolling calibration).**
- **Problem statement:** rules.md §Rolling Calibration Metrics says "over all settled predictions", but three models settling the same due vintage each wrote settlement rows, and reflections counted rows, not predictions — exposing artifacts: 07-14 02 §0 ("n=135 deduped" — actually raw-ish), today's 02 §0 recount (204 rows → 103 distinct), and the vintage-key variants (`gpt-5-2026-06-16` vs `2026-06-16` vs missing) that defeated the intended dedupe.
- **Change (applied this run):** rolling calibration metrics are computed on **strict prediction identity** — key (ticker, vintage date, target date), vintage normalized to its date and inferred from prediction records when a settlement row omits it; where duplicate settlements of one prediction disagree, close-based records are preferred over intraday-print records (consistent with the codified settlement-timing rules); core ETFs are always MARKET_FORECAST and never pooled with EQ metrics. Documented in 02 §0 and L023.
- **Hypothesis:** every future run reports the same n for the same evidence base regardless of how many models settled a vintage; calibration triggers (sigma-widening, MEDIUM cap, mu-table evidence thresholds) fire on true evidence counts, not row counts.
- **Validation (Track B three-condition standard):** (1) problem statement cites the exposing artifacts above; (2) weakens no protected rule or grounding gate — it tightens the evidence base that gates changes (the ≥20-settled Track A thresholds now count distinct predictions, which is *more* conservative); (3) logged here with **HUMAN_REVIEW** flag; effective this run, revert by restoring row-count aggregation.
- **Decision: ACCEPT** (Track B; the one change this run).

## Standing Items (not new proposals)

- **Fundamental/Sentiment feed unwiring — 13th consecutive run**; standing HUMAN_REVIEW escalation (wire a source, or formally adopt a 2-family investable standard) remains the binding constraint on ever publishing GO (first raised 07-01).
- **MF regime-prior mu bias** — Track A candidate; corrected evidence now **4/12 distinct with all 8 misses mu-positive**; trigger at ≥20 MF settlements (15 open-or-settled distinct MF exist; 12 settled).
- **Rank IC in flat tapes** — three consecutive negative vintages; the automatic MEDIUM cap binds if the weighted mean ≤ 0 at n≥20 joinable (currently +0.040 at n=91 — one ≈−0.25 vintage away). Track A calibration work becomes proposable the moment the trigger fires.
- **CI coverage 83.5%** — first time near the 85% too-wide ceiling on a corrected base; if two more runs print ≥85%, the tighten-intervals rule engages (would be Track A).
- **REIT sigma floor** — n=4, pattern weakened by 07-14's IN_CI; DOC (settles 08-10) remains the live test.
- **Numeric-table rendering** — after today's caught transcription error: extend programmatic rendering to all numeric tables (06-class summaries included). Process hygiene; noted for next run's assembly, no rules.md change required.

## Effective Next Step

Thursday 2026-07-16 run: STT/UNH/GE print pre-open — the managed-care/custody re-evaluation binding (02 §5) executes against post-print closes; expect the financials complex to begin clearing its penalty windows Friday (RF 07-17 closes the wave); watch whether the corrected weighted IC crosses zero when the 06-18 gpt-5 vintage (if any) or the 07-01 claude vintage (settles 07-29) lands; SOXX's reclaimed MA50 is the regime tell — a close back below it re-opens the "break" case.
