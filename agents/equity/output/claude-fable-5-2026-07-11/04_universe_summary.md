# 04 Universe Summary — 2026-07-11

> **BACKFILLED 2026-07-12** — reconstructed from the session's committed 03 §Universe Handoff and support artifacts.

S&P 500 ∪ Nasdaq-100 via `build_index_universe.py`: 503 + 101 − 89 = **515 union** (universe_summary.json generated 2026-07-11T12:55:19Z). **512 eligible**; INDEX_UNION_PCTL (n=512); sampled fallback NOT used.

| Ticker | Action | Reason |
|---|---|---|
| SATS | REJECTED | Structural-stale (no prints since 07-02; carried since 07-08) |
| BF-B | REJECTED | Nasdaq vendor gap this session (no /chart data returned — nasdaq_verification_manifest.json failures); re-admitted 07-12 when the gap cleared |
| FDXF | REJECTED | 31 bars < 60 minimum |

Metric coverage identical in kind to the adjacent packages: price/volume + derived risk and the d/w/m technical indicator pack sourceable for all 512 (technical_indicators.json 2026-07-11T16:28:28Z, 520/521 OK); Fundamental and Sentiment families UNAVAILABLE universe-wide (DQ 0.80, confidence LOW, family gate unsatisfiable — Enhancing, never a GO blocker); earnings dates per the session's own full-universe fetch cited in 03 (manifest lost with the truncation; the backfilled scoring uses the 07-12 confirmed vintage, disclosed in 01/05).
