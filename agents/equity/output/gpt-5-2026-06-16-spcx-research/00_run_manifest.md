# SPCX Single-Name Research Manifest - 2026-06-16

## Run Scope

- Request: deep research SPCX one-month price scenarios.
- Reference system: `investments/equity/daily_investment_system/main.md`.
- Adaptation: single-name research package, not a full 5-10 name portfolio run.
- Final status: `REVIEW_ONLY`.
- Data mode: `DELAYED_PARTIAL`.
- Anchor price: `SPCX $192.50`, `DELAYED`, observation date `2026-06-15`, retrieved from Nasdaq quote endpoint at `2026-06-15 22:03:47 PDT`.
- Target date: `2026-07-15`, one month after the latest verified close used as anchor.

## Status Rationale

`REVIEW_ONLY` is mandatory under the referenced system because SPCX has only two public trading sessions as of the anchor date. A required input for `GO` is about 60 trading days of price history for beta, realized volatility, drawdown, and correlation. That input cannot exist yet.

## GO-Gate Table

| Required input | Status | Evidence / attempt |
|---|---|---|
| Grounded entry price | Grounded | Nasdaq quote endpoint: `$192.50`; NY Post cross-check: `$192.45`; difference `0.03%`. |
| About 60 trading days of history | Failed | SPCX IPO trading began `2026-06-12`; insufficient history by construction. |
| Sigma via fallback chain | Failed | No 30d realized vol; no verified IV30/option chain used; sector median would be a weak proxy for an idiosyncratic low-float mega-IPO. |
| Next earnings date | Unavailable | No verified earnings calendar source found during this focused run. |
| Sampled universe | Not applicable | Single-name research, not a ranked daily universe run. |

## Artifact Checklist

| File | Status |
|---|---|
| `00_run_manifest.md` | Present |
| `01_preflight.md` | Present |
| `09_final_report.md` | Present |
| `15_scenario_forecast.json` | Present |
| Full daily package files `02`-`08`, `13`, formal `15_predictions.json` | Not produced; this is not a ranked portfolio run. |

