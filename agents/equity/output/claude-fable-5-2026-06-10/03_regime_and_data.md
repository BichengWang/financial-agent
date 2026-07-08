# 03 Regime and Data

Data/Regime agent output. All figures cite Source Ledger rows in `01_preflight.md`.

## Data Validation

- Mode: **DELAYED** (tool-fetched intraday quotes + 3-month daily histories, retrieval timestamps logged). Eligible for GO at reduced exposure per Data Mode Taxonomy.
- Coverage: 30/30 universe names with grounded last price, 1-day change, 30d historical vol; 25/30 with YTD; 11 daily-close series (62 bars each). Zero fabricated or recalled values.
- Lineage: single brokerage tool (IBKR MCP) for all prices; formulas cited for every derived metric.

## Regime Classification: **HIGH_VOL** (transition from BULL)

| Evidence | Observation (ledger rows) | Read |
|---|---|---|
| Index trend | SPY 728.31, -4.2% off 2026-06-03 ATH 760.39 in 5 sessions; still +5.0% over 1m, +11.0% YTD | Sharp pullback inside an uptrend |
| Volatility | VIX 19.87 → 21.36 intraday (+7.5%); SPY 30d HV 12.4% but realized accelerating (June 5: -2.6% day on 59M shares) | Vol regime shifting up |
| Rates | TLT 84.94, +0.51% over 1m, YTD -0.25% | **No rate shock** — distinguishes this from the May-29/June-5 narrative in prior cross-model logs |
| Growth vs broad | QQQ -1.59% today vs SPY -1.19%; QQQ +20.4% YTD | High-beta led both the rally and the unwind |
| Cross-section today | Green: CVX +2.3%, XOM +1.6%, COST +1.2%, AAPL +0.9%, WMT +0.8%, MCK +0.8% / Red: CAT -6.2%, ETN -6.1%, AVGO -4.6%, VST -5.0%, AMD -4.9%, MU -4.7% | Textbook crowding unwind: AI-capex complex sold, defensives + energy bid |
| Crowding markers | MU +212% YTD @ 101% HV; AMD +111% @ 86%; AVGO HV 71% post-earnings | Blow-off momentum profiles now in sharp drawdown |

Implication for factor weights (within policy): macro/regime family scores favor energy leadership, staples/healthcare defensives, low HV; penalize HV>60% crowded momentum during the unwind. No baseline family-weight mutation (that requires evolution-policy evidence); the tilt is expressed through the regime family's per-name scores as designed.

## Event Concentration

- FOMC: ~2026-06-16/17 (cadence, `ESTIMATED (±2d)`) — inside the 2-6w horizon for all names; portfolio-level macro event risk noted.
- Earnings inside buffered 19d window: **MU (~2026-06-25 ±5d)** — penalized -0.10 and confidence-capped LOW. All other ranked names report ≥ ~5 weeks out.

## Universe Handoff

30-name sampled universe built per protocol (composition and rejection log in `04_universe_summary.md`). No name failed inclusion filters: all are US-primary, mega/large-cap (> $2B), high-ADV (> $20M), > $5, seasoned listings; no halts, no corporate-action ambiguity among fetched names.

## Stop-Rule Check

No HALT condition: benchmark data present, lineage clear, zero unresolved critical inputs among top-ranked candidates, universe ≥ 30. Run proceeds to scoring.
