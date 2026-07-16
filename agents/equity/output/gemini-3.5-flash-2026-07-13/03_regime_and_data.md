# 03 Regime and Data — 2026-07-13

## Data Mode: **DELAYED**

All prices are the 2026-07-10 Friday close, fetched this run (Monday 08:0x ET pre-open). Primary bulk source: Nasdaq historical API — 516/519 direct, BRK-B via dot-notation, SATS via its post-rename ticker **ECHO** (EchoStar changed symbol; same entity, series continuous), BF-B via IBKR MCP `get_price_history` (conid 4931) after the Nasdaq endpoint returned empty for the B-class (L002). **Yahoo chart API returned HTTP 429 for the entire session** — first full-session primary-source outage; the fallback chain held with zero unresolved failures (documented for 13). Verification: IBKR MCP snapshots on all 27 published symbols — **12/12 available `priorClose` fields match the Nasdaq closes to the cent (0.000%)**; the 15 without a priorClose field corroborated by IBKR pre-market last within ±1.75% movement-inclusive (L016). VIX from CBOE's official history CSV (L007); risk-free from FRED DTB3 (L008). All five Required-for-GO inputs are grounded; the missing inputs are Enhancing-class only (options IV/skew, short interest, analyst tape, fundamentals/sentiment feeds) → confidence caps, never GO blockers.

**Pre-market context note (not used in scoring):** IBKR pre-market lasts at ~08:30 ET: SPY -0.44%, QQQ -1.21%, SOXX **-3.33%** vs Friday close (L016). Monday's open is shaping risk-off in the growth/semis complex — consistent with the elevated-vol digestion this artifact describes. Scoring uses Friday's close throughout; this note is context for the 12:15 midday checkpoint.

## Regime Classification: **NEUTRAL** (8th consecutive session label; L019)

No session has elapsed since Friday's close — the label re-reads the same tape and holds:

| Evidence | Value | Ledger |
|---|---|---|
| SPY | 754.95 record close; above MA20 743.81 and MA50 741.24 (BULLISH alignment); dd from 60d high -0.61%; RSI-d 59 | L004, L010 |
| VIX | **15.03 = 60d low**; 20d mean 16.95 vs prior-20d 17.53 (falling) | L007 |
| QQQ | above MAs, but 30d rvol 29.2% ann ≈ 1.9x prior window (15.7%) | L005, L011 |
| SOXX | **below MA20** (581.34 vs 599.82), -11.25% from 60d high, 30d rvol 74.2% vs 43.6% prior | L006, L012 |
| TLT | quiet: 20d -0.48%, 60d -3.14%, rvol 9.2% | L009 |
| Rotation | QQQ/SPY RS 20d +0.50% / 60d +6.17%; SOXX/SPY 20d +3.16% / 60d +33.28% | L013 |

Not BULL: the growth/semis complex is digesting on ~2x realized vol beneath an index-level record — trend intact, internals unconfirmed. Not HIGH_VOL: VIX at a 60d low with a falling mean; vol is concentrated in one complex, not the tape. Not RATE_SHOCK (TLT quiet). **NEUTRAL** — record index, compressed implied vol, elevated-vol growth sleeve, defensive/low-vol cross-sectional leadership. Today's settlement evidence is regime-consistent: the 06-15 vintage's SPY HIT / QQQ MISS / SOXX MISS mirrors index-flat / growth-chop exactly (02 §0).

## Core ETF Market Forecast Block

NEUTRAL prior: SPY mu +0.5%; QQQ/SOXX = beta × SPY mu, no discretionary adjustments (L014). Sigma = REALIZED_VOL_30D. target_date 2026-08-10 (run+28d). CI = entry×(1+mu±1.04σ).

| ETF | Entry Price | Price Date | Price Tag | Trend (20d/50d) | 30d RVol | Beta vs SPY | mu | sigma | Sigma Source | Target Price | Target Date | 70% CI Lo | 70% CI Hi | Confidence | Ledger Rows |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SPY | 754.95 | 2026-07-10 | DELAYED | above both (BULLISH) | 15.1% ann (rising vs 10.0%) | 1.00 | +0.5% | 4.37% | REALIZED_VOL_30D | 758.72 | 2026-08-10 | 724.42 | 793.02 | MEDIUM | L004, L010, L014 |
| QQQ | 725.51 | 2026-07-10 | DELAYED | above both (BULLISH) | 29.2% ann (rising vs 15.7%) | 1.67 | +0.8% | 8.43% | REALIZED_VOL_30D | 731.31 | 2026-08-10 | 667.71 | 794.92 | MEDIUM | L005, L011, L014 |
| SOXX | 581.34 | 2026-07-10 | DELAYED | **below MA20** / above MA50 (MIXED) | 74.2% ann (rising vs 43.6%) | 3.49 | +1.7% | 21.43% | REALIZED_VOL_30D | 591.22 | 2026-08-10 | 461.65 | 720.79 | **LOW** | L006, L012, L014 |

Relative strength: QQQ/SPY +0.50% (20d) / +6.17% (60d); SOXX/SPY +3.16% (20d) / +33.28% (60d) — semis still lead over 60d but the 20d edge has compressed to a third of trend, and this morning's pre-market (-3.3%) extends the digestion (L013, L016). Regime-consistency: one line — a NEUTRAL tape with positive-but-small index mu, wide growth CIs, and the semis call at LOW confidence because trend (MIXED), vol (rising, 74%), and RS (compressing) do not align.

## Universe Handoff

`build_index_universe.py` succeeded: 503 S&P 500 + 101 Nasdaq-100, 89 overlap → **515 union** (caches fetched_at 2026-06-21 — stale-cache rule: use and log, refresh is maintenance; L001). Filters applied on fetched bars (L002): FDXF excluded (31 bars < 6-month listing age; also the one `technical_indicators.py` UNAVAILABLE). **514 eligible names** handed to factor scoring with `INDEX_UNION_PCTL (n=514)` labeling. SATS trades as ECHO since the EchoStar rename — series continuous, retained. Rejection log: 04. Event concentration: the confirmed **banks/financials earnings wave 07-14..07-17** (BAC 07-14; PNC/MTB/MS/JBHT 07-15; STT/USB/CFG/UNH/GE 07-16; RF 07-17) gates a heavily-financial leaderboard region — 04 §Earnings Penalty Roll. FOMC: next meeting ~07-28/29 (inside horizon, standard macro risk note). Ticker handoff to `technical_indicators.py`: SPY QQQ SOXX + eligible_universe.txt (executed; L003).

## Stop-Rule Assessment

No halt: data lineage clean, benchmark grounded, zero unresolved fetch failures. Recommendation to orchestrator: proceed to scoring; expect **NO_TRADE** at publication because the family-coverage gate (2/4 sourceable) structurally caps the investable set at zero — a construction outcome, not a data failure.
