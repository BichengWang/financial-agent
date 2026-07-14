# 13 Evolution Log — 2026-07-14

## Run Context

| Field | Value |
|---|---|
| Date / Status / Regime | 2026-07-14 / NO_TRADE (weekday, family gate) / NEUTRAL |
| Evaluation window | Trailing 7 days: claude-fable-5 07-07..07-13, gpt-5 07-07..07-13 — all models, all packages |
| Ledger status | 17 settled this run (gpt-5 06-16 vintage); cross-model deduped base n=135 EQ + 12 MF; 45 ledgers scanned |
| Baseline flag | SAME_MODEL_BASELINE (claude-fable-5-2026-06-10), no gap flag |

## What Worked

1. **The codified source chain (07-13 Track B) survived its first full test on day one.** Yahoo 429-blocked for a second consecutive session; the chain executed exactly as written — Nasdaq bulk 517/519 in ~177s, BF-B via IBKR conid 4931, SATS→ECHO handled, 13/13 exact IBKR verification — zero improvisation, zero unresolved failures. A repeat of last run's mid-run scramble cost nothing today.
2. **Confirmed-dates preflight caught two window-flips** (V and IQV both landed at exactly 14d) and correctly cadence-estimated a vendor-empty post-print name (FAST) — third run as standard procedure, working as designed each time.
3. **Sigma honesty is paying calibration dividends**: today's 17 settlements ran 13/14 EQ IN_CI and the two brutal reversals (FCX -14.7% raw, SOXX -9.7% raw) both stayed inside their wide, REALIZED_VOL_30D-derived CIs. CI coverage 77.8% sits near the 70% target from above.
4. **Sortino wired**: downside series persisted this run, closing the 07-13 gap (no more RAW_DIAG n/a in the ratio pack).

## What Failed / Weak Spots

1. **Regime-prior MF mu is now 5/12 on direction, with all 7 misses being mu-positive calls into flat/falling tapes** (today: SPY/QQQ/SOXX all MISS; SOXX -9.66% vs +7.3% forecast is the worst ETF call in the ledger). The BULL/NEUTRAL priors express a structural long bias the 4-week tape hasn't rewarded since mid-June. Track A material; evidence at n=12 of the ≥20 threshold.
2. **Rank IC slightly negative two vintages running** (06-15: -0.08, 06-16: -0.046), both in flat-SPY windows; weighted mean holds at +0.093 (n=77). Consistent hypothesis: the momentum-led composite separates well in trending tapes, poorly in thematic-dispersion tapes. Below action threshold; if weighted IC ≤ 0 at n≥20, the MEDIUM cap binds automatically.
3. **Fund/Sent unwiring: 12th consecutive run** — the standing structural GO blocker; unchanged, unresolvable at run level.

## Primary Diagnosis

**Factor calibration** (MF regime-prior mu bias) — the category today's new evidence (3 MF misses, all one-directional) most cleanly isolates. Below its Track A evidence threshold; no scoring change proposable yet.

## Proposed Change (exactly one)

- **Classification: Track B (spec consistency — settlement-timing codification). MANDATORY per rules.md §Two-Track: flagged in two consecutive evolution logs (07-12 §standing, 07-13 §weak-spot 3).**
- **Problem statement:** the settlement-timing conventions (`TARGET_EQ_RUN_DATE`, `WEEKEND_TARGET`) governed 20 settlements on 07-13 and 17 today, yet existed only in artifacts and session memory — a reproducibility hole: a fresh model executing rules.md §Settlement Rules literally could hold same-day-target predictions open or settle them on intraday prints (exposing artifacts: 07-13 02 §0 header; this run's L017).
- **Change:** codified both conventions into `rules.md §Settlement Rules` (applied this run): settle at target-date close when it exists; `WEEKEND_TARGET` → last close at-or-before target; `TARGET_EQ_RUN_DATE` → latest completed close for pre-open/intraday runs; never intraday prints, never held open past target.
- **Hypothesis:** identical settlement behavior across models/runs without folk knowledge; zero change to scoring math.
- **Validation (Track B three-condition standard):** (1) problem statement cites exposing artifacts; (2) weakens no protected rule or grounding gate — it pins settlement to completed closes, strengthening the Price Sourcing Standard's intent; (3) logged here with **HUMAN_REVIEW** flag; effective immediately (applied to this run's own 17 settlements), revert by deleting the codified block.
- **Decision: ACCEPT** (Track B; the one change this run).

## Standing Items (not new proposals)

- **Fundamental/Sentiment feed unwiring — 12th consecutive run**; standing HUMAN_REVIEW escalation (wire a source, or formally adopt a 2-family investable standard) remains the binding constraint on ever publishing GO (first raised 07-01).
- **MF regime-prior mu bias** — Track A candidate, trigger at ≥20 MF settlements (now 12). Interim: none (mu table is evolution-agent-only with evidence).
- **REIT sigma floor** — Track A candidate; today's PLD IN_CI settlement weakens the pattern (n=4: 3 OUT_CI_LOW, 1 IN_CI); DOC settlement 08-10 remains the live test.
- **Rank IC in flat tapes** — diagnostic accumulating (2 consecutive negative vintages); automatic MEDIUM cap binds if weighted IC ≤ 0 at n≥20 joinable.
- Track A calibration: none proposed — CI 77.8%, mean z -0.179, weighted IC +0.093 all in band; freeze criteria not triggered.

## Effective Next Step

Wednesday 2026-07-15 run: banks/insurers wave prints begin (ELV/JBHT/MTB/PNC/BNY tomorrow AM; STT/UNH/GE Thursday) — expect the financials complex to start re-entering the leaderboard as penalty windows clear; UNH/GE re-evaluation queued for after Thursday's prints; watch whether Monday's semi break extends (SOXX below both MAs) or the Tuesday intraday bounce (L016 manifest) holds.
