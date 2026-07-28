# 00 Run Manifest — 2026-07-28

**Final status: NO_TRADE**

| Field | Value |
|---|---|
| Run date / fire | 2026-07-28 Tuesday · pre-open |
| Model | gpt-5 |
| Run mode | Scheduled daily full pipeline |
| Data mode | DELAYED — 2026-07-27 completed close |
| Target date | 2026-08-25 |
| Final status | NO_TRADE |
| Universe | 515 eligible; 514 scored |
| Regime | NEUTRAL |

## State and blockers

The full state machine completed to publication. **NO_TRADE** is binding because no name can demonstrate 3 of 4 non-negative factor families when Fund_Z and Sent_Z are UNAVAILABLE, and DQ is 80%, below the 85% evidence gate (L029, L039–L040). The pctl80 beta shortfall is corroborating only: maximum attainable beta is 0.889447 versus the 0.90 floor (L033). Equal weighting the 20 published monitors also fails the sector cap because Industrials is 35% > 30% (L035).

## Reflection baseline

`agents/equity/output/gpt-5-2026-06-30` — **SAME_MODEL_BASELINE**, exact 28-day target, exception flag **NONE** (L038).

## Prediction settlement

This run independently recomputed 35 valid settlement candidates (29 EQUITY_ALPHA, 6 MARKET_FORECAST) under TARGET_EQ_RUN_DATE at the 2026-07-27 close. Because an earlier same-day package had already canonicalized the same keys, all 35 current rows are retained as audit-only same-tier duplicate agreements, not new canonical rows. Canonical totals remain equity raw n=260 / eff_n=1 and market raw n=48 / eff_n=1; due inventory and conflicts remain 0 (L036–L037).

## GO-Gate Table — Required inputs

| Required input | Status | Evidence |
|---|---|---|
| Grounded entry price | GROUNDED | 20 equities + 3 ETFs pass two-source gate; L002,L004–L006 |
| ~60 trading days history | GROUNDED | 514 equities scored; FDXF excluded for listing age; L002,L003,L044 |
| Sigma fallback | GROUNDED | REALIZED_VOL_30D population stdev for every published record; L011 |
| Next earnings date | GROUNDED | Published top20 fully grounded after bounded convergence; L019 |
| Index-union universe | GROUNDED | 515 eligible tickers; L001 |

Enhancing IV/skew, short interest, bid-ask tape, revisions, and ownership flows are UNAVAILABLE; they reduce DQ/confidence and are not incorrectly used as Required-input GO blockers (L041).

## Source Ledger Coverage

| claim_type | Rows |
|---|---|
| OBSERVED | 14 |
| DERIVED | 49 |
| INFERRED | 3 |
| UNAVAILABLE | 3 |
| ILLUSTRATIVE | 0 |
| TOTAL | 69 |

## Artifact checklist

`00`–`16`, `eligible_universe.txt`, `universe_summary.json`, `technical_indicators.json`, all required support manifests, and the SPY/QQQ/SOXX forecast block are present. `15_predictions.json` contains **20 EQUITY_ALPHA + 3 MARKET_FORECAST predictions and 35 settlements**; all 35 settlement rows are valid audit-only same-tier duplicate agreements, not new canonical rows.

## Outstanding blockers

1. Wire sourceable Fund_Z and Sent_Z feeds before an investable set can clear 3-of-4 families.
2. Track A calibration remains gated until eff_n ≥ 3.
3. Reassess beta and sector feasibility only after the evidence gates produce at least five investable names.
