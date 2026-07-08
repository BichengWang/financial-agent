# 08 Risk Review

## Committee Decision

`REJECT` the portfolio and approve `NO_TRADE` publication.

## Top Concerns

1. **Protected beta band failure.** The maximum NAV beta contribution from the investable set is 0.384, below the 0.90-1.10 requirement. This is a composition failure, not a data-integrity halt.
2. **No legal repair within one revision.** High-beta names that could repair beta either fail factor-family support or the 80th percentile threshold. Adding them would weaken the evidence bar.
3. **Enhancing inputs absent.** Options IV/skew, short interest, and full-universe feeds are unavailable. They are not GO blockers, but they keep confidence capped at MEDIUM for most names.

## Checklist

| Risk Check | Result |
|---|---|
| Fabricated or unsupported prices | PASS — every entry price has Yahoo/Nasdaq rows. |
| Missing sigma source | PASS — all ranked names use `REALIZED_VOL_30D`. |
| Missing prediction records | PASS — all investable, monitor, and core ETF forecasts are in `15_predictions.json`. |
| Source Ledger coverage | PASS — 242 rows. |
| Portfolio beta | FAIL — 0.384 max NAV beta. |
| Pairwise correlation | PASS — 0.253. |
| Drawdown | PASS — 3.83% parametric 95% 1m drawdown at max weights. |
| Sector concentration | PASS on NAV exposure. |

## Final Publication Recommendation

Publish `NO_TRADE`. Do not publish a model portfolio or position sizes.
