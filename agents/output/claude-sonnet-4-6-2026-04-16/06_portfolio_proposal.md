# Portfolio Proposal: Paper-Trade Basket & Constraint Violations
## Claude Sonnet 4.6 | April 16, 2026

---

## Executive Summary

**Proposed Portfolio**: 5-stock equal-weighted (19–22% per position)

**Status**: PAPER-TRADE (REVIEW_ONLY classification; not authorized for live execution)

**Key Metric**: 100% allocation, 0% cash (vs March 16 portfolio: 29.5% equity / 70.5% cash)

**Committee Assessment**: ✅ Thesis quality HIGH | ⛔ Execution constraints VIOLATED | **Recommendation**: REVIEW_ONLY (see risk review)

---

## The Proposed Basket (April 16)

### Position Details

| Position | Ticker | Sector | Allocation | Price | Shares (for $1M) | Market Cap | Thesis |
|----------|--------|--------|-----------|-------|------------------|-----------|--------|
| 1 | AVGO | Semiconductors | 22% | $396.72 | 554 | $250B | Fabless wins |
| 2 | META | Communications | 20% | $671.58 | 298 | $800B | Data center capex |
| 3 | NVDA | Semiconductors | 20% | — | — | $2.5T | AI GPU leadership |
| 4 | GEV | Industrials | 19% | $841.27 | 226 | $120B | Infrastructure power |
| 5 | MSFT | Software | 19% | — | — | $3.0T | Enterprise AI, margins |
| **TOTAL** | — | — | **100%** | — | — | — | — |
| **CASH** | — | — | **0%** | — | — | — | **Fully invested** |

### Portfolio Characteristics

| Metric | Value | Assessment |
|--------|-------|-----------|
| **Weighted Avg Market Cap** | $1.3T | Mega-cap weighted |
| **Weighted Avg P/E (forward)** | 34x | Extended but growth-justified |
| **Weighted Avg Revenue Growth** | 18% | Healthy growth profile |
| **AI Exposure** | 90% | Heavy AI infrastructure weighting |
| **Tech Sector Weight** | 62% (AVGO+NVDA+META+MSFT) | High concentration |
| **Earnings Cluster (April 29)** | 60% (META+GEV+MSFT) | Single-event risk |

---

## Constraint Validation & Violations

### Hard Constraints (Portfolio Construction Rules)

#### Constraint #1: Maximum Position Size
**Rule**: No single position > 25% | **Proposed Portfolio**: AVGO 22% (✅ pass) | **Status**: ✅ **PASS**

#### Constraint #2: Sector Concentration
**Rule**: No sector > 40% | **Proposed Portfolio**: Tech 62% (AVGO 20% + NVDA 20% + META 20% + MSFT 19% = 79% semis+tech) | **Status**: ⚠️ **VIOLATION** (79% > 40%)

**Details**:
- Semiconductors: AVGO (22%) + NVDA (20%) = 42%
- Communications: META (20%)
- Software: MSFT (19%)
- Industrials: GEV (19%)

**Explanation**: AI mega-trend justifies concentration, but violates governance rules. BULL regime + April 29 earnings cluster heighten concentration risk.

#### Constraint #3: Minimum Diversification (5+ Holdings)
**Rule**: 5+ names minimum | **Proposed Portfolio**: AVGO, META, NVDA, GEV, MSFT (5 names) | **Status**: ✅ **PASS** (meets minimum)

#### Constraint #4: Maximum Earnings Cluster Exposure
**Rule**: No single week > 50% of portfolio | **Proposed Portfolio**: April 29 (META 20% + GEV 19% + MSFT 19% = 58%) | **Status**: ⚠️ **VIOLATION** (58% > 50%)

**Details**:
- April 23: AVGO 22% (earliest earnings, before cluster)
- April 29: META 20% + GEV 19% + MSFT 19% = 58%
- May 22: NVDA 20% (after cluster)

**Explanation**: April 29 cluster concentration is material risk. If guidance misses, 58% of portfolio exposed to simultaneous repricing.

#### Constraint #5: Data Quality Threshold
**Rule**: All holdings must have DQ ≥ 0.90 | **Proposed Portfolio**: All 5 DQ = 0.95 | **Status**: ✅ **PASS**

#### Constraint #6: Liquidity (Daily Volume)
**Rule**: $100M+ daily volume minimum | **Proposed Portfolio**: All 5 >> $1B daily | **Status**: ✅ **PASS** (mega-cap)

---

## Violation Summary

### Violation #1: Sector Concentration (Tech 62% vs 40% limit)

**Severity**: ⚠️ **MODERATE-HIGH**

**Root Cause**: AI mega-trend + BULL regime both favor tech concentration. Rejects (INTC, AMD, LRCX) all tech; financials (GS, JPM, BAC) under-weighted due to value rotation.

**Risk Impact**:
- If tech sector de-rates (multiple compression), 62% allocation amplifies drawdown
- April 16 signal: Tech outperforming (QQQ +0.68% vs SPY +0.04%), but not sustainable if macro deteriorates
- Estimated max drawdown (tech sector -15% decline): Portfolio -9.3% (vs SPY -7%)

**Potential Mitigation**:
1. **Reduce NVDA to 15%** (still top conviction)
2. **Add ETN (Eaton) 7%** instead of MSFT 19% → Maintain industrial diversification
3. **Rebalanced Portfolio**: AVGO 22%, NVDA 15%, META 20%, MSFT 12%, GEV 19%, ETN 12% = 100%
   - Tech: 57% (still high, but improved)
   - Industrials: 31% (GEV + ETN)
   - Communications: 12% (reduced)

**Governance Decision**: REVIEW_ONLY status prevents live execution, but violation documented for future runs.

---

### Violation #2: Earnings Cluster (April 29: 58% vs 50% limit)

**Severity**: ⚠️ **HIGH**

**Root Cause**: Meta, GEV, and MSFT all report April 29. Three mega-cap holdings clustered same week.

**Risk Impact**:
- **Single Event Risk**: If guidance disappoints (capex, growth, margins), 58% of portfolio reprices simultaneously
- **No Optionality**: Unlike diversified earnings calendar, April 29 miss = portfolio miss
- **Estimated Downside**: If cluster guidance misses, -10% to -15% drawdown potential (vs +5% to +10% if beats)

**Probability Assessment**:
- **Capex Positive Bias**: META, MSFT likely to raise/maintain capex guidance
- **Risk**: If inflation resurges or AI ROI questioned, capex guidance cuts possible
- **Base Case**: April 29 slight positive (60% probability) → guidance maintenance

**Mitigation Options**:
1. **Reduce April 29 Cluster**: 
   - Option A: Remove GEV (19%) → Reduces cluster to 39% (META 20% + MSFT 19%)
   - Option B: Reduce each by 5% (META 15%, GEV 14%, MSFT 14%) → Cluster = 43%
   
2. **Hedge April 29 Cluster**:
   - Buy puts on QQQ (20 April 29 strike, 20 delta) → $20–30 cost per $1M portfolio
   - Limits downside if cluster misses; caps upside ~2%

3. **Accept Risk**: Acknowledge 58% cluster; monitor April 23–29 closely
   - High conviction that guidance positive, but execution risk real

**Governance Decision**: REVIEW_ONLY + risk committee REJECT recommendation due to this violation.

---

## Comparison: March 16 Portfolio vs April 16 Proposed

### March 16 Portfolio (Claude Opus, GO status)
| Position | Allocation | Score | Status |
|----------|-----------|-------|--------|
| NVDA | 5.0% | 83 | Concentrated |
| AVGO | 4.5% | 78 | Concentrated |
| GEV | 4.0% | 77 | Concentrated |
| GS | 4.0% | 71 | Value hedge |
| AMD | 3.5% | 71 | ❌ Downgraded |
| LRCX | 3.0% | 71 | ❌ Downgraded |
| INTC | 3.0% | 68 | ❌ Downgraded |
| MU | 2.5% | 70 | ❌ Downgraded |
| **CASH** | **70.5%** | — | **Defensive** |

**March Assessment**: Highly defensive (70.5% cash), 29.5% equity, no single position > 5%. Regime HIGH_VOL+RATE_SHOCK justified caution.

### April 16 Portfolio (Claude Sonnet, REVIEW_ONLY status)
| Position | Allocation | Score | Status |
|----------|-----------|-------|--------|
| AVGO | 22% | 86.5 | ✅ Validated winner |
| META | 20% | 82.8 | ✅ Identified miss |
| NVDA | 20% | 81.9 | ✅ Stable leader |
| GEV | 19% | 78.3 | ✅ Thesis confirmed |
| MSFT | 19% | 74.7 | ✅ Quality play |
| **CASH** | **0%** | — | **Fully invested** |

**April Assessment**: Aggressive (100% equity, 0% cash), 22% largest position. Regime BULL justifies risk-on, but concentration violations noted.

### Portfolio Evolution: March → April

| Dimension | March | April | Change | Rationale |
|-----------|-------|-------|--------|-----------|
| **Equity Allocation** | 29.5% | 100% | +70.5% | Regime shift: HIGH_VOL → BULL |
| **Cash Allocation** | 70.5% | 0% | -70.5% | Risk-on positioning |
| **Largest Position** | NVDA 5% | AVGO 22% | +17% | AVGO validation (+22% gain) |
| **Number of Holdings** | 8 | 5 | -3 | Concentration for conviction |
| **Sector Concentration** | Low (diversified) | High (62% tech) | Significant | AI mega-trend dominance |
| **Earnings Cluster Risk** | Low | High (58%) | Significant | April 29 concentration |
| **Highest Score** | NVDA 83 | AVGO 86.5 | +3.5 | AVGO upgraded on validation |

---

## Paper-Trade Execution Plan (if approved)

### Entry Sequence (April 16–18)
Assuming REVIEW_ONLY was overridden and live execution authorized:

| Day | Action | Allocation | Rationale |
|-----|--------|-----------|-----------|
| **April 16** | **Build 50%** | AVGO 11%, META 10%, NVDA 10%, GEV 9.5%, MSFT 9.5% | Scale in; test liquidity |
| **April 17** | **Complete 50%** | AVGO 11%, META 10%, NVDA 10%, GEV 9.5%, MSFT 9.5% | Finish build; 2-day average |
| **April 18–20** | **Monitor** | Rebalance if drift > 2% | Hold through AVGO earnings (April 23) |
| **April 23–29** | **Cluster Period** | Monitor; reduce if April 23 miss | AVGO earnings + April 29 cluster |
| **April 30+** | **Reassess** | Re-run scorecard post-earnings | Cluster results determine holding |

### Position Limits (if live)
- **Max drawdown tolerance**: -15% (from entry)
- **Earnings event kill-switch**: If April 23 (AVGO) misses >> AND VIX spikes, unwind 50%
- **Cluster mis-step**: If April 29 (META, GEV, MSFT) guidance disappoints, rotate to ETN/GOOGL near-misses

### Monitoring Checkpoints
- **Daily**: EOD price check; VIX < 20 (BULL continuation)
- **April 23**: AVGO earnings analysis → Maintain / Reduce
- **April 29**: META, GEV, MSFT earnings → Critical reassessment
- **May 1**: Post-cluster regime check → Extend / Exit

---

## Risk Dashboard: Current Metrics

| Risk Metric | Value | Threshold | Status |
|-------------|-------|-----------|--------|
| **Portfolio Concentration (top 3)** | 62% | < 70% | ✅ Acceptable |
| **Sector Concentration (tech)** | 62% | < 40% | ⚠️ **VIOLATION** |
| **Earnings Cluster April 29** | 58% | < 50% | ⚠️ **VIOLATION** |
| **Valuation (weighted avg P/E)** | 34x | < 35x | ✅ Marginal |
| **Momentum (3M avg return)** | +12% | > +5% | ✅ Strong |
| **Liquidity (daily volume)** | > $500M avg | > $100M | ✅ Excellent |

---

## Recommendation

### Committee Vote (April 16)
**Proposed**: 100% equity, 5-stock portfolio | **Violations**: 2 (sector conc., earnings cluster) | **Status**: ⛔ **REJECT** → REVIEW_ONLY

**Rationale**:
- ✅ Thesis quality HIGH (all 5 candidates have strong conviction + validated momentum)
- ❌ Governance violations too material for live trading (62% tech, 58% earnings cluster)
- ✅ Data quality sufficient (DQ = 0.95 across all names)
- ⚠️ Recommend for paper-trading, backtesting, with April 29 monitoring

**Alternative Approvals**:
1. **REDUCE Size**: 60% equity / 40% cash → Halve position sizes, reduces violation impact
2. **REBALANCE Sector**: Swap MSFT (19%) for ETN (7%) + GEN (12%) → Reduces tech to 48%, industrials to 31%
3. **HEDGE Cluster**: Add QQQ 20 delta puts (April 29) → Reduces April 29 downside to -5% max

---

*Portfolio proposal completed by Claude Sonnet 4.6 on 2026-04-16. REVIEW_ONLY status prevents live execution. Violations documented for risk committee.*
