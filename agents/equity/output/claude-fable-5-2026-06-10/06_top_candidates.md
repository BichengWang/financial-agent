# 06 Top Candidates

Run status context: final status is **NO_TRADE** (portfolio constraints — see 07/08). The investable set below passed every name-level evidence threshold; the failure is at portfolio level. All 12 ranked names carry full metrics blocks (05) and prediction records (`15_predictions.json`).

## Investable Set (≥ 80th pctl, ≥ 3/4 families non-negative, no family > 50% conviction, data completeness ≥ 85%, no hard stop)

| Rank | Ticker | Sector | Adj | Pctl | Why it qualifies | Confidence |
|---|---|---|---|---|---|---|
| 1 | MCK | Health Care | +0.787 | 100 | 4/4 families positive; green on unwind days; mu +6.0% | MEDIUM |
| 2 | COST | Staples | +0.691 | 97 | 4/4 families; quality defensive; mu +6.0% | MEDIUM |
| 3 | WMT | Staples | +0.624 | 93 | 4/4 families; consensus + regime fit; mu +5.0% | MEDIUM |
| 4 | CVX | Energy | +0.550 | 90 | 4/4 families; sector leadership; mu +5.0% | MEDIUM |
| 5 | UNH | Health Care | +0.541 | 86 | 4/4 families; recovery momentum; mu +4.0% | MEDIUM |

## Monitoring Sleeve (60–80th pctl, or ≥ 80 failing a name-level criterion; settleable, not executable)

| Ticker | Pctl | mu | Why monitored, not investable |
|---|---|---|---|
| MU | 83 | +1.0% (shaded) | ≥ 80th pctl but fails 3-of-4-families test (S, M negative), HV 101% > 2× sector median, earnings ~Jun 25 inside buffered window |
| XOM | 79 | +2.0% | 1 rank below the 80th-pctl bar |
| LIN | 76 | +2.0% | Below bar; cleanest low-vol profile in monitor sleeve |
| LLY | 72 | +2.0% | Below bar |
| NVDA | 69 | +1.0% | Carry-forward DOWNGRADE; crowding unwind |
| GOOGL | 66 | +1.0% | Carry-forward DOWNGRADE; best mega-cap YTD |
| ABBV | 62 | +1.0% | Below bar; defensive optionality |

## Near Misses

XOM (79th pctl) is the only near miss of note — one universe rank short of investable. It is not promoted: stretching the threshold to fix the portfolio's beta problem would be exactly the "weaken standards to force a publishable portfolio" pattern the non-negotiables prohibit (and its computed-beta profile is similar to CVX, so it would not fix the band anyway).

## Handoff to Portfolio Construction

Five investable names from three defensive sectors (2 HC, 2 Staples, 1 Energy). Flag to portfolio agent: 60d betas of this set are ≈ 0 to negative (computed, ledger rows) — beta-band feasibility must be checked before sizing for GO.
