# Multi-Agent Quantitative Equity Research Pipeline — Run Manifest

**Date:** 2026-03-16
**Run ID:** 2026-03-16-LIVE-001
**Execution Mode:** LIVE
**Data Source:** Web-gathered financial data (March 16, 2026)
**State Machine:** PRECHECK → PREFLIGHT → DATA_LOAD → REGIME_CLASS → SCREENING → SCORING → CONSTRUCTION → RISK_REVIEW → APPROVAL → EXECUTION
**Current Status:** PRECHECK (manifest generation)

---

## Agent Roster

| Agent | Role | Status |
|-------|------|--------|
| **Market Data Agent** | Gather live market prices, indices, volatility, rates | ACTIVE |
| **Macro Agent** | Classify regime, assess macro shocks (rates, FX, commodities) | ACTIVE |
| **Fundamental Agent** | Score earnings, growth, profitability, balance sheet | STANDBY |
| **Technical Agent** | Score momentum, trend, support/resistance | ACTIVE |
| **Sentiment Agent** | Monitor insider activity, options flow, analyst calls | ACTIVE |
| **Universe Agent** | Screen securities against filters, universe construction | ACTIVE |
| **Factor Scoring Agent** | Compute cross-sectional scores (4-factor model) | ACTIVE |
| **Portfolio Construction Agent** | Optimize size and sector allocation | ACTIVE |
| **Risk Committee Agent** | Adversarial review, constraint checking | ACTIVE |
| **Execution Agent** | Generate final report, recommendation log | STANDBY (awaiting approval) |

---

## Pipeline Inputs

### Market Data Gathered
- **Benchmarks:** SPY, DIA, QQQ, VIX, 10Y Treasury
- **Commodities:** WTI crude, Brent, Gold, Bitcoin
- **Currencies:** DXY (USD index)
- **Rates:** 10Y yield, Fed expectations
- **Sector indices:** Technology, Semiconductors, Energy, Utilities, Materials, Industrials, Financials, Consumer Discretionary, Consumer Staples, Healthcare, Real Estate, Communications

### Security Universe
- **Base:** S&P 500 (~500 constituents)
- **Filters:** Market cap >$10B, daily volume >$50M, not in bankruptcy/delisting watch
- **Result:** ~420 eligible securities (ILLUSTRATIVE count)

### Known Catalysts (This Week)
- Nvidia GTC conference (Mar 16-19)
- Federal Reserve decision
- Micron (MU) earnings
- Alibaba (BABA), XPeng (XPEV), Lululemon (LULU) earnings

---

## Expected Outputs

| File | Purpose | Owner |
|------|---------|-------|
| `01_preflight.md` | Data coverage & sources | Market Data Agent |
| `02_regime_and_data.md` | Regime classification | Macro Agent |
| `03_universe_summary.md` | Universe construction | Universe Agent |
| `04_factor_scores.md` | Security-level factor scores | Factor Scoring Agent |
| `05_top_candidates.md` | Candidate screening & thesis | Fundamental + Technical Agents |
| `06_portfolio_proposal.md` | Initial portfolio construction | Portfolio Construction Agent |
| `07_risk_review.md` | Risk assessment & constraints | Risk Committee Agent |
| `08_final_report.md` | **MAIN DELIVERABLE** | Execution Agent |
| `09_midday_monitor.md` | Scheduled for 12:15 ET | Execution Agent |
| `10_preclose_check.md` | Scheduled for 15:45 ET | Execution Agent |
| `11_close_log.md` | Scheduled for 16:20 ET | Execution Agent |
| `12_evolution_log.md` | Baseline evolution review | Risk Committee Agent |

---

## Key Assumptions

1. **Data Freshness:** All prices & indices as of market open/mid-morning March 16, 2026
2. **Factor Data Stability:** Security-level factors (beta, correlations, z-scores) are ILLUSTRATIVE (no Bloomberg terminal)
3. **Execution Constraints:** Max 5% per name, max 30% per sector, target portfolio beta 0.95–1.05
4. **Event Risk:** MU (earnings this week), NVDA (GTC), others carry near-term catalysts
5. **Volatility Regime:** VIX 24.29 signals HIGH_VOL; portfolio positioned defensively

---

## Next Step

Proceed to **PREFLIGHT** phase (01_preflight.md) to validate data coverage.

