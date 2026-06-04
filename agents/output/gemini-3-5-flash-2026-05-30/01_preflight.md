# 01 Preflight

⚠️ ILLUSTRATIVE — NOT LIVE DATA. Schema and process check only.

## Preflight Summary

The run booted cleanly and all six prompt files (`00_orchestrator.md`, `01`–`05` agents) loaded without conflict. Shared system rules (`research_system.md`), stop criteria (`stop_criteria.md`), evolution policy (`evolution_policy.md`), schedule (`daily_schedule.md`), and output spec (`daily_output_spec.md`) were applied. **No market-data adapter is wired for this session.** The system therefore declares `ILLUSTRATIVE_MODE` rather than fabricating values to fill the schema.

The session itself falls on a non-trading day (Saturday 2026-05-30); the next U.S. cash session is Monday 2026-06-01. Because methodology validation can run any day but cannot produce a tradeable portfolio without a live feed, the orchestrator will converge on `REVIEW_ONLY`.

## Data Coverage

| Domain | Source expected | Status today | Tag |
|---|---|---|---|
| Benchmark spot (SPY, QQQ, IWM) | Vendor tape / IEX / consolidated | Not wired | `N/A` |
| Sector ETF tape (XL*) | Vendor tape | Not wired | `N/A` |
| VIX, VVIX, MOVE, term structure | CBOE / vendor | Not wired | `N/A` |
| Rates curve (UST 2/5/10/30, real yields) | FRED / Treasury direct | Not wired | `N/A` |
| FX (DXY, EURUSD, USDJPY) | Vendor tape | Not wired | `N/A` |
| Credit (HYG/LQD spreads, IG/HY OAS) | Vendor / FRED | Not wired | `N/A` |
| Single-name OHLCV (>$2B mcap, >$20M ADV) | Vendor tape | Not wired | `N/A` |
| Beta and 30-day realized vol | Computed from OHLCV | Non-computable | `N/A` |
| Earnings calendar (≤14 days lookahead) | Vendor calendar | Not wired | `N/A` |
| Options surface (skew, IV30, IV/RV) | OPRA / vendor | Not wired | `N/A` |
| Short interest (FINRA bi-monthly) | FINRA / S3 | Not wired | `N/A` |
| Analyst revisions / target changes | I/B/E/S / Refinitiv | Not wired | `N/A` |
| Insider transactions (Form 4) | SEC EDGAR | Not wired | `N/A` |
| Institutional ownership (13F) | SEC EDGAR | Not wired | `N/A` |
| Corporate actions / halts | NASDAQ / NYSE | Not wired | `N/A` |

Coverage: **0 of 15 critical feeds present**. Per `research_system.md` §Data Quality Multiplier, the multiplier would fall well below `0.70`; per the same file, no candidate may be ranked investable in this state.

## Freshness Validation

Not applicable — no fields ingested. No `LIVE`, `DELAYED`, or `STALE` tags emitted.

## Lineage Check

Not applicable — no fields ingested. The audit chain is preserved by *not writing* values rather than by stamping an unverifiable lineage.

## Validation Summary

| Check | Result |
|---|---|
| Shared system prompt loaded | Pass |
| Stop criteria loaded | Pass |
| Evolution policy loaded | Pass |
| Daily schedule loaded | Pass |
| Daily output spec loaded | Pass |
| Calendar awareness | Pass — Saturday non-trading day |
| Live or delayed data feed | **Fail (no feed wired)** |
| ILLUSTRATIVE_MODE declared | Pass |
| Non-fabrication contract honored | Pass — every numeric field tagged `N/A` |

## Hard Halt Decision

Per `stop_criteria.md` §Hard Halt item 1, missing benchmark data with no `ILLUSTRATIVE_MODE` declaration would trigger `HALTED`. We *do* declare `ILLUSTRATIVE_MODE` explicitly, which suppresses `HALTED` and routes the run to `REVIEW_ONLY` per §Review-Only Mode item 1.

## Handoff Note → Data/Regime Agent

> The eligible universe cannot be filtered today because no security-level tape is available. Pass through to the regime classifier with a low-confidence `NEUTRAL` placeholder. Factor scoring should return `N/A` for every family. The risk committee will reject any tradeable publication. Status target: `REVIEW_ONLY`.
