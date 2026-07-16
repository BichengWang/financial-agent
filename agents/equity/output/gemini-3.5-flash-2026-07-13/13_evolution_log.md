# 13 Evolution Log — 2026-07-13

## Run Context

| Field | Value |
|---|---|
| Date / Status / Regime | 2026-07-13 / NO_TRADE (weekday, family gate) / NEUTRAL |
| Evaluation window | Trailing 7 days: gemini-3.5-flash 07-06..07-12, gpt-5 07-06..07-12 — all models, all packages |
| Ledger status | 20 settled this run (gpt-5 06-15 vintage); cross-model deduped base n=121 EQ + 9 MF; 44 ledgers scanned |
| Baseline flag | SAME_MODEL_BASELINE (gemini-3.5-flash-2026-06-21), no gap flag |

## What Worked

1. **The 07-12 Track B change paid for itself on day one.** Confirmed-dates preflight (accepted Friday, HUMAN_REVIEW) ran as standard step today and caught **FFIV flipping INTO the ≤14d window** (confirmed 07-27 = exactly 14d today vs 15d Friday) — precisely the window-flip class the change targeted. The -0.10 penalty applied on a confirmed date, not an estimate.
2. **Source-outage resilience.** Yahoo returned HTTP 429 for the entire session — the first full-session primary outage. The run pivoted to the Nasdaq historical API (515-name bulk, ~50s, comma-stripping per the known quirk), resolved three symbol-level failures three different ways (BRK.B dot-notation; SATS→ECHO rename discovery; BF-B via IBKR conid 4931), and verified with 12/12 exact IBKR priorClose matches. Zero unresolved failures.
3. **Carry-forward discipline keeps compounding evidence:** LLY 4th consecutive settled HIT, ANET 3rd large HIT (+11.85% today), LIN recovered its watch (HIT), ABBV repeat HIT (+11.51%, though OUT_CI_HIGH).

## What Failed / Weak Spots

1. **REIT sigma calibration is now a pattern, not an anecdote: n=3.** PLD settled OUT_CI_LOW again today (z -1.20), joining AMT (-1.38) and Friday's PLD — every REIT settlement in the ledger has broken below its 70% CI. REALIZED_VOL_30D appears to under-state REIT downside vol in this tape. DOC (rank 7 today, sigma 7.8%) is the live test: settles 08-10.
2. **The 06-15 vintage's rank IC is slightly negative (-0.08, n=17)** after two strongly positive vintages — single-vintage noise on current evidence (weighted IC +0.124 at n=63), but it coincides with a flat-SPY month where alpha dispersion was thematic (commodity/REIT/mega-tech down vs industrial/HC up). Watch whether IC degrades in low-dispersion tapes.
3. **Settlement-timing convention is folk knowledge.** TARGET_EQ_RUN_DATE (pre-open runs settling at the prior close) and WEEKEND_TARGET are applied consistently but live in artifacts/memory, not rules.md §Settlement Rules.

## Primary Diagnosis

**Factor calibration** (REIT sigma) — the one miss category today's new evidence isolates; but it is Track A material below its evidence threshold (3 settlements ≠ 20).

## Proposed Change (exactly one)

- **Classification: Track B (process/data-sourcing — no scoring math altered).**
- **Problem statement:** The prompt stack names Yahoo as the de-facto bulk history source; today's full-session 429 outage (artifact: this package's `price_history_fetch_manifest.json` and 03 §Data Mode) forced an undocumented mid-run pivot. The working fallback chain exists only as session knowledge.
- **Change:** codify the **price-history source chain** as standard procedure: (1) bulk primary — Yahoo v8 chart API; (2) bulk fallback — Nasdaq historical API (`assetclass=stocks|etf`, strip `$`/commas, dot-notation for B-classes, check ticker renames); (3) per-name straggler — IBKR MCP `get_price_history`; (4) verification — IBKR `prior_close` snapshots on every published symbol when the two bulk sources are not independently available (single-web-source runs). VIX from CBOE official CSV; rf from FRED DTB3.
- **Hypothesis:** documented chain removes the single-source availability risk from the Required-input #2 grounding path with zero change to scoring; a future outage costs minutes, not a HALT-risk.
- **Validation (Track B three-condition standard):** (1) problem statement above cites the exposing artifacts; (2) weakens no protected rule or grounding gate — it strengthens the Price Sourcing Standard's redundancy; (3) logged here with **HUMAN_REVIEW** flag; effective next run unless reverted.
- **Decision: ACCEPT** (Track B; the one change this run).

## Standing Items (not new proposals)

- **Fundamental/Sentiment feed unwiring — 11th consecutive run**; the standing HUMAN_REVIEW escalation (wire a source, or formally accept a 2-family investable standard) remains pending (first raised 07-01). This is the binding constraint on ever publishing GO.
- **REIT sigma floor** — Track A candidate; trigger: DOC settlement 08-10 or the ledger reaching ≥20 REIT-relevant settlements. Interim: none (rules give no basis to hand-adjust sigma without evidence).
- **Settlement-timing codification** (TARGET_EQ_RUN_DATE / WEEKEND_TARGET into rules.md §Settlement Rules) — queued Track B candidate for a future run (one-change-per-run limit).
- Track A calibration: none proposed — CI 76.0%, mean z -0.165, weighted IC +0.124 all in band; freeze criteria not triggered.

## Effective Next Step

Tuesday 2026-07-14 run: apply the codified source chain; banks wave prints begin (BAC tomorrow) — expect leaderboard reshaping as names exit the penalty window; re-evaluate UNH/GE after 07-16; DOC is the REIT-sigma live test.
