# 08 — Risk Committee Review *(backfilled)*

> **BACKFILLED 2026-08-07.** The 2026-08-06 session truncated after writing `00`-`04` and `15_predictions.json`; this artifact was reconstructed on 2026-08-07 from that folder's own committed data (`15_predictions.json` plus `00`-`04`) and from nothing else. Figures that the truncated session never persisted are marked `UNAVAILABLE` rather than recomputed: the 2026-08-06 run used the 2026-08-05 close as its basis, so substituting a later run's numbers would misstate what that run actually saw. No prediction record was created, altered or settled.

## Decision: `REJECT` — the set becomes `NO_TRADE`

No single revision could make any name investable: two of four evidence thresholds were
unsatisfiable rather than narrowly missed.

| # | Check | Finding (from the committed artifacts) | Verdict |
|---|---|---|---|
| 1 | Fabricated or weakly supported inputs | `00` records 27/27 published symbols grounded on 3 independent sources at 0.0000% max deviation | **PASS** |
| 2 | Overfitting / unvalidated signal claims | no parameter changed; Track A gated at `eff_n = 2 < 3` | **PASS** |
| 3 | Excessive event concentration | 0 of 24 published names carried an earnings penalty | **PASS** |
| 4 | Correlation / sector crowding | **UNAVAILABLE** — not persisted | unknown |
| 5 | Portfolio beta drift | attainable -0.2803 … +1.4145 straddles the band | **PASS** |
| 6 | Thesis quality below stated confidence | no name carries HIGH; 24 of 24 are LOW | **PASS** |
| 7 | Report / shared-rules mismatch | status and sleeve isolation conform | **PASS** |
| 8 | Price / derived-field citation violations | every record carries `price_date` + `price_tag`; targets and CIs derive from grounded prices | **PASS** |
| 9 | Sigma violations | all 27 records carry `REALIZED_VOL_30D` with a stated source | **PASS** |
| 10 | Score-attribution violations | all 24 records carry a full trace, family z-scores, slot z-scores, DQ, penalties and drivers | **PASS** |
| 11 | Source Ledger violations | `01_preflight.md` was published and is complete | **PASS** |
| 12 | Live-sounding or stale-as-current claims | prices described as the completed 2026-08-05 close, tagged `HISTORICAL` | **PASS** |
| 13 | Improper GO-blocking | `00` GO-Gate Table shows all 5 Required inputs grounded; no Enhancing input cited as a blocker | **PASS** |
| 14 | Missing prediction records | 24 EQUITY_ALPHA + 3 MARKET_FORECAST records, all with `score_explainability` (null on MF) | **PASS** |
| 15 | Technical indicator pack violations | every state cites `L004`; TD-9/RSI treated as exhaustion flags | **PASS** |

## Concerns

1. **Two factor families dark** — the structural cause of the `NO_TRADE`, unchanged across the
   series.
2. **Elevated RSI across the published set** — several names carry daily and weekly RSI above
   70 (e.g. the rank-1 name at daily 77.19 / weekly 81.16), which is an exhaustion flag against
   a leaderboard already dominated by trend persistence.
3. **Event concentration** — 0 names with earnings inside 14 days, above the
   stop-criteria threshold of 2.

## Publication recommendation

**`NO_TRADE`**, as published. No `HALTED` condition applied.

## Committee note on this backfill

The 2026-08-06 session truncated **after** `15_predictions.json` was written, so every forecast
that run made is recorded and settleable; nothing was lost from the prediction ledger. What was
lost is the narrative layer, reconstructed here. The committee's standing position that a
missing artifact is a process failure rather than a silent gap is why this backfill exists.
