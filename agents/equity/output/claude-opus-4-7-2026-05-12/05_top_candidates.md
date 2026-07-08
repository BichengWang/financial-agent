# 05 Top Candidates

⚠️ ILLUSTRATIVE — NOT LIVE DATA. **Zero names are investable today.** The list below is a schema-demonstration only. No name carries a tradeable thesis.

## Investable Set

| Rank | Ticker | Status |
|---:|---|---|
| — | — | None — investable promotion disabled in `ILLUSTRATIVE_MODE` (research_system §Evidence Thresholds, requires ≥85% data completeness; today 0%). |

## Schema-Demo Candidate Cards (Illustrative)

For each placeholder, the card structure mirrors what a live run would emit. **Every numeric is a placeholder**; thesis bullets are template patterns.

### MSFT — placeholder

- Composite Z (raw / adjusted / pctile): +1.18 / +0.83 / 99
- Confidence: `LOW` (capped — `ILLUSTRATIVE_MODE`)
- Expected α (1M, %): N/A — required σ unknowable.
- β vs SPY (60D): N/A
- 30D realized vol (ann.): N/A
- Days to earnings: N/A
- Thesis (template): "Cloud revenue acceleration; falsifier: Azure YoY growth prints below [X]% next quarter."
- Risks (template): "Mega-cap concentration unwind; rate-sensitivity to long-duration tech."

### NVDA — placeholder

- Composite Z: +1.18 / +0.83 / 99
- Confidence: `LOW`
- Thesis (template): "Data-center capex demand persistence; falsifier: hyperscaler capex guidance cut."
- Risks (template): "Single-product concentration; export-control re-rating."

### META — placeholder

- Composite Z: +1.13 / +0.79 / 98
- Confidence: `LOW`
- Thesis (template): "Ad-pricing reacceleration; falsifier: ARPU YoY < [Y]%."
- Risks (template): "Reality Labs burn surprise; regulatory."

### GOOGL — placeholder

- Composite Z: +1.02 / +0.71 / 97
- Confidence: `LOW`

### AMZN — placeholder

- Composite Z: +0.96 / +0.67 / 96
- Confidence: `LOW`

## Near-Misses (Illustrative)

AVGO, LLY, V, MA, UNH — all placeholder; would require live data to assess.

## Rejection Notes

- All names rejected from investable set on the same systemic ground: data completeness 0% across F/T/S families, failing `eval/research_system.md` §Evidence Thresholds item 4 (≥85% required).
- No name-specific rejection logic applies in `ILLUSTRATIVE_MODE`.

## Handoff to Portfolio Construction

Pass through with **empty investable set**. Portfolio construction agent should produce a `NO_TRADE` shape under `REVIEW_ONLY`, not a paper portfolio that could be misread as a recommendation.
