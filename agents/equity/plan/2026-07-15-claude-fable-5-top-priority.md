# Top-Priority Improvement — 2026-07-15 run (claude-fable-5)

**Priority #1: wire a Fundamental + Sentiment data source so the family gate can ever open.**

## Why this outranks everything else

The 2026-07-15 run published **NO_TRADE for the 13th consecutive scoring session**, and the cause was identical every time: with `Fund_Z` and `Sent_Z` `UNAVAILABLE` universe-wide, at most 2 of 4 factor families are sourceable, so **no name — regardless of score — can satisfy evidence threshold #2 (≥3 of 4 families non-negative)**. Every other open issue (rank-IC decay in flat tapes, MF regime-prior mu bias, CI coverage nearing the 85% ceiling, the settlement double-count fixed this run) is calibration refinement on top of a system that is structurally incapable of publishing `GO`. Data-side, everything else is healthy: all five Required inputs grounded 13 runs running, 16/17 IBKR price verifications exact today, 514/514 universe coverage on price history and the technical pack.

The standing HUMAN_REVIEW escalation (first raised 07-01) offers two exits: (a) wire a feed, or (b) formally adopt a 2-family investable standard. Option (b) weakens the evidence architecture; option (a) is now demonstrably cheap, because this environment has proven exactly the fetch patterns needed.

## Concrete proposal (both families, free sources already proven in this repo's runs)

**Fundamental family — SEC EDGAR XBRL (`companyfacts`) as primary:**
- `https://data.sec.gov/api/xbrl/companyfacts/CIK{cik}.json` is free, official, unauthenticated (User-Agent header only), and bulk-downloadable as one `companyfacts.zip` (~1GB) for full-universe offline coverage — the same "bulk primary + straggler fallback" shape as the codified Nasdaq/IBKR price chain.
- Computable signals with 8+ quarters of facts: revenue acceleration, margin trajectory (gross/operating trend), ROE/ROIC level and trend, leverage (debt/equity), FCF yield vs EV (with shares outstanding + price already grounded), accrual quality (earnings vs OCF gap).
- Clears the ≥70%-of-universe sourceability rule for Adj Score contribution (rules.md §Financial Metrics) — ticker→CIK mapping via SEC's public `company_tickers.json`.

**Sentiment family — Nasdaq analyst/short-interest endpoints as primary:**
- `api.nasdaq.com/api/analyst/{sym}/ratings` (consensus + rating changes) and `/analyst/{sym}/targetprice` — the same host, headers, and threading already proven at 519 symbols in ~50s for prices and 54 symbols for earnings dates this run.
- Short-interest change from Nasdaq's published short-interest data (or FINRA's twice-monthly file) as the second signal; CBOE public put/call CSVs as an optional third.
- Two sourceable signals satisfy the ≥2-metrics-per-family floor; anything less leaves the family `UNAVAILABLE` per rules.

**Governance / rollout:**
1. **Track B change** (missing-fetch procedure fix — no scoring math changes: the 0.30/0.25 family weights and the trace formula already reserve these slots; activating real inputs cannot weaken a protected rule). Log with HUMAN_REVIEW; one run of shadow output (families computed and displayed but flagged `SHADOW — not yet gating`) before they count toward the 3-of-4 test.
2. Phase 1 (one session of work): shortlist-scale fetch (top-60 post-Tech/Macro + carry-forwards) to validate parsing and z-score construction; family still `UNAVAILABLE` for gating, published as diagnostics.
3. Phase 2: bulk `companyfacts.zip` + threaded Nasdaq sentiment for the full 514 universe; DQ multiplier rises from 0.80 toward 0.90; confidence cap LOW → MEDIUM where families confirm; the 3-of-4 gate becomes satisfiable and `GO` becomes reachable at reduced gross exposure (Enhancing gaps still cap at 50%).
4. Failure containment: per-name fetch failures degrade that name's family to `UNAVAILABLE` (never neutral); a bulk-source outage falls back to the shortlist-scale path with the same disclosure pattern as the price chain.

**Acceptance test:** a run where ≥70% of the eligible universe carries computed `Fund_Z` and `Sent_Z` with full ledger lineage, at least one name satisfies 3-of-4 non-negative families, and the risk committee finds zero fabrication/lineage violations in the new rows.

## Queue behind it (for context, not this proposal)

2. Regime-conditioned composite (rank IC now negative three consecutive vintages in flat tapes; weighted +0.040 at n=91 — Track A once the MEDIUM cap trips or n≥20 evidence supports a weighting change).
3. MF regime-prior mu bias (4/12 direction on the corrected base, all misses mu-positive; Track A at ≥20 settled MF).
4. Extend programmatic rendering to every numeric table (today's 06/09 hand-transcription errors were caught at review; generation should make the error class impossible).

— claude-fable-5, 2026-07-15 run (artifacts: `agents/equity/output/claude-fable-5-2026-07-15/`, esp. 08 §Top Three Concerns, 13 §Standing Items)
