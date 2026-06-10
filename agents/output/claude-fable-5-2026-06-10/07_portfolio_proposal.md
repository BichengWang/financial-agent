# 07 Portfolio Proposal — Constraint Check FAILED → recommend NO_TRADE

The draft below is the best constraint-respecting attempt from the 5-name investable set. It fails the protected beta band, and the 5-name/3-sector shape cannot satisfy the 30% sector cap. Per the Failure Rule, the agent recommends **NO_TRADE** rather than forcing it. Published for auditability; **not executable**.

## Draft Weights (fractional-Kelly-capped, 5% single-name NAV cap, HIGH_VOL gross haircut)

| Ticker | NAV weight | Sleeve weight | Beta60 | sigma(1m) | Kelly note |
|---|---|---|---|---|---|
| MCK | 5.0% | 22.7% | −0.17 | 6.49% | 0.25×Kelly binds above cap → capped |
| COST | 4.5% | 20.5% | −0.14 | 7.77% | |
| WMT | 4.0% | 18.2% | +0.24 | 9.94% | |
| CVX | 4.5% | 20.5% | −0.88 | 7.28% | |
| UNH | 4.0% | 18.2% | +0.35 | 8.27% | |
| **Gross** | **22.0%** | 100% | | | Under the 50% missing-Enhancing cap by design |

## Portfolio Analytics (computed from 60d fetched histories — formulas in ledger DERIVED rows)

| Metric | Value | Limit | Verdict |
|---|---|---|---|
| Sleeve beta (Σ wᵢβᵢ, normalized) | **−0.14** | 0.90 – 1.10 | **FAIL** |
| Avg pairwise correlation (60d) | +0.18 | < 0.45 | PASS |
| Sleeve σ (1m, √(w′Σw)) | 4.68% | — | — |
| 95th-pctl 1M drawdown (1.65σ, normality stated) | 7.72% | ≤ 8% | PASS |
| Expected sleeve Sharpe (Σwᵢμᵢ / σ₁ₘ, annualized ≈ ×√12) | ≈ 1.9 (μ̄ ≈ +5.3% / 4.68% monthly) | — | High on paper — defensives bid |
| Sector concentration | HC 41%, Staples 39%, Energy 20% | ≤ 30%/sector | **FAIL ×2** |

## Correlation Matrix (60d daily returns)

|  | MCK | COST | WMT | CVX | UNH |
|---|---|---|---|---|---|
| MCK | 1 | .41 | .17 | .09 | .09 |
| COST | | 1 | .69 | .21 | .13 |
| WMT | | | 1 | −.03 | .03 |
| CVX | | | | 1 | .06 |
| UNH | | | | | 1 |

## Factor Exposure Summary

Long defensive-quality + energy; short nothing. Loadings: low-beta (dominant — and the source of the failure), anti-momentum-crowding, energy leadership. No single factor family contributes > 50% of any name's conviction (checked in 05), but the **portfolio** is one trade expressed five ways: "own what holds up in a vol spike."

## Revision Pass (1 allowed) — attempted and failed

1. **Beta**: max-tilting toward the highest-beta members (WMT +0.24, UNH +0.35) within 5% caps lifts sleeve beta to ≈ +0.1 — nowhere near 0.90. Adding beta requires names below the 80th-pctl bar (NVDA β1.84, GOOGL β1.56) — prohibited (threshold integrity) and they are DOWNGRADE/unwind names.
2. **Sector caps**: 5 names / 3 sectors cannot all sit ≤ 30%. Fixing requires ≥ 4 sectors in the investable set — does not exist today.

## Recommendation

**NO_TRADE** per `stop_criteria § Downgrade To No-Trade` #2/#6: the only publishable portfolio would overconcentrate in the defensive factor and violate the protected beta band; weakening either protected rule for publishability is prohibited. The five names remain ranked forecasts with full prediction records — the system still earns settlement evidence from today.

## Why excluded names stayed excluded

XOM (79th pctl): one rank below bar; would worsen sector concentration (Energy → 2 names) without fixing beta. All sub-60 names: mu table floor — not rankable.
