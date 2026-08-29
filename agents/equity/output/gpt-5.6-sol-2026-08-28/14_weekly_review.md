# 14 — Weekly Parameter Review · Week ending 2026-08-28

## Governance summary

This Friday review covers the August 22 and August 27 process acceptances and today's calibration
evidence. No parameter mutation is authorized.

| Item | Classification | Weekly evidence | Disposition |
|---|---|---|---|
| Dead-constituent / corporate-action screen (accepted Aug 22) | Track B | surfaced both EQR keys and prevented successor-ratio fabrication | **KEEP** |
| CNBC US-exchange + positive-volume identity gate (accepted Aug 27) | Track B | EQR now resolves to an unrelated foreign issuer; 23 legitimate published prices cross-check at 0% deviation | **KEEP; HUMAN_REVIEW implementation required** |
| Factor-weight recalibration | Track A | weighted rank IC -0.0495; 38 of 69 vintage ICs are non-positive | **DEFER** — eff_n 2<3 |
| Equity mu shrink | Track A | mean z -0.5553 below healthy floor -0.5 | **DEFER** — eff_n 2<3 |
| ETF interval tightening | Track A | MF CI coverage 90.55% >85% | **DEFER** — eff_n 2<3 |

## Stability and freeze review

The model remains at weights 30/30/25/15, unchanged calibration-table priors, 5% single-name cap,
30% sector cap, 0.90–1.10 beta band, 0.45 correlation cap and 8% drawdown cap. Formal freeze
criteria are not triggered: the week contains accepted Track B process changes, but neither changes
forecast math. Track A remains gate-frozen by insufficient independent windows.

## Next week

Monitor the projected equity eff_n increase on 2026-09-03 and
market-forecast increase on 2026-09-07. If the gate opens,
evaluate the single pre-registered factor-weight proposal in `13`; do not combine it with mu or
ETF-sigma changes.
