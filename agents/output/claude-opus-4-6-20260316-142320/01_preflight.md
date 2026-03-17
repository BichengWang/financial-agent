# Preflight Data Coverage Report

**Date:** 2026-03-16
**Run Status:** PREFLIGHT (validation phase)
**Data Mode:** MIXED (LIVE benchmarks + ILLUSTRATIVE security-level factors)

---

## Data Coverage Summary

### Macro & Benchmark Data (LIVE)

| Category | Data Point | Value | Source | Status |
|----------|-----------|-------|--------|--------|
| **Equity Indices** | S&P 500 | 6,702.25 (+1.06%) | Market data | ✅ LIVE |
| | SPY | $669.54 (prev $662.29) | Market data | ✅ LIVE |
| | Dow Jones | +0.84% (+380 pts) | Market data | ✅ LIVE |
| | Nasdaq | +1.15% (+282 pts) | Market data | ✅ LIVE |
| **Volatility** | VIX | 24.29 (prev 27.19, -10.68%) | Market data | ✅ LIVE |
| | VIX spike history | >25 on Mar 11 (Iran conflict) | Market data | ✅ LIVE |
| **Fixed Income** | 10Y Treasury | 4.28% | Market data | ✅ LIVE |
| | 10Y range (2 weeks) | 3.96% to 4.28% (+32bps) | Market data | ✅ LIVE |
| | Fed expectations | 1 cut priced for 2026 | Market data | ✅ LIVE |
| **Macro Indicators** | PCE inflation | 2.8% annual | Economic data | ✅ LIVE |
| | Q4 GDP (revised) | 0.7% | Economic data | ✅ LIVE |
| **Currencies** | DXY (USD index) | ~100.3 (10-month high) | Market data | ✅ LIVE |
| **Commodities** | WTI crude | ~$94.88 (down $3.83 today) | Market data | ✅ LIVE |
| | Brent crude | ~$100.42 | Market data | ✅ LIVE |
| | Gold | $5,020 | Market data | ✅ LIVE |
| | Bitcoin | $73,860 | Market data | ✅ LIVE |

### Sector Performance (LIVE)

| Sector | Today | Week YTD | Status |
|--------|-------|----------|--------|
| Technology | Leader | Lagging | ✅ LIVE |
| Semiconductors | Strong | Leader | ✅ LIVE |
| Energy | Moderate | +2.5% | ✅ LIVE |
| Utilities | Moderate | +1% | ✅ LIVE |
| Industrials | Lagging | Lagging | ✅ LIVE |
| Materials | Lagging | Lagging | ✅ LIVE |
| Consumer Discretionary | Mixed | Lagging | ✅ LIVE |
| Consumer Staples | Not available | — | ⚠️ PARTIAL |
| Healthcare | Not available | — | ⚠️ PARTIAL |
| Financials | Positive | Leader | ✅ LIVE |
| Real Estate | Not available | — | ⚠️ PARTIAL |

### Security-Level Data (ILLUSTRATIVE)

| Data Class | Coverage | Mode | Notes |
|------------|----------|------|-------|
| **Price & Volume** | 100% (S&P 500) | LIVE | Real-time or end-of-day |
| **YTD Returns** | ~90% | LIVE | Gathered from web sources |
| **Today's % Change** | ~80% (focus names) | LIVE | Top movers reported |
| **Beta (market)** | ~60% | ILLUSTRATIVE | Estimated from 1-year history |
| **Momentum (6-mo)** | ~70% | ILLUSTRATIVE | Derived from price data |
| **Earnings Revisions (z-score)** | ~40% | ILLUSTRATIVE | Sparse data; no Bloomberg terminal |
| **Insider Transaction Flow** | ~60% | LIVE | Clusters detected Mar 9-14 |
| **Options Activity (unusual)** | ~50% | LIVE | High-volume contracts flagged |
| **Analyst Ratings** | ~70% | ILLUSTRATIVE | BofA, MS, JPM consensus noted |

### Known Gaps & Limitations

1. **Exact Betas & Correlations:** Without institutional data feed, betas estimated from YTD returns and historical volatility. Portfolio beta estimate (1.05) is ILLUSTRATIVE.
2. **Earnings Revisions Z-Scores:** No systematic Bloomberg NI data. Analyst commentary used as proxy.
3. **Factor Exposures (Value/Growth/Quality/Momentum):** Cross-sectional scores are ILLUSTRATIVE based on available metrics.
4. **Real-time Sector Weights:** S&P 500 weighting by sector taken from published indices; subject to lag.
5. **Options Implied Volatility:** Available for focus names; not comprehensive across universe.

### Data Freshness Assumptions

- **Prices & Indices:** As of ~10:30 AM ET, March 16, 2026
- **Macro Data:** Most recent official releases (PCE, GDP, Fed guidance)
- **Analyst Calls:** Latest (BofA, MS, JPM published Mar 14-16)
- **Insider Activity:** Aggregated through Mar 14
- **Options Flow:** As of Mar 15 close

---

## Data Quality Rating

**Overall:** 7.5 / 10

- ✅ **Macro & benchmark data:** 9/10 (live, reliable)
- ✅ **Sector & index data:** 8/10 (mostly live, minor lags)
- ⚠️ **Security-level fundamentals:** 6/10 (illustrative; gaps in earnings revisions)
- ⚠️ **Factor model inputs:** 5/10 (estimated; not Bloomberg-grade)
- ✅ **Sentiment & options:** 7/10 (good coverage on focus names)

---

## Implications for Pipeline

### Data Sufficiency
- **GO for regime classification:** Macro data is robust.
- **GO for candidate screening:** YTD returns, momentum, catalysts are well-sourced.
- **CAUTION for exact factor scores:** Use ranges and illustrative labels. Portfolio construction will use weights, not raw exposures.

### Constraints on Final Output
1. Candidate confidence levels will be MEDIUM or MEDIUM-HIGH (no VERY HIGH without full fundamental audit).
2. Portfolio beta estimate is directional, not precise.
3. Expected return/drawdown estimates are scenario-based, not statistically calibrated.
4. Evolution log will note that this run establishes a baseline; future runs will refine with richer data.

---

## Sign-Off

**Macro Agent:** Data coverage sufficient for HIGH_VOL regime classification. ✅ **PROCEED**

**Factor Scoring Agent:** Acknowledge ILLUSTRATIVE mode for security-level scores. Apply uncertainty buffers. ✅ **PROCEED**

**Risk Committee:** Flag that portfolio construction relies on estimates, not exact models. Will apply tighter constraints. ✅ **PROCEED**

---

## Next Step

Advance to **DATA_LOAD → REGIME_CLASS** phase (02_regime_and_data.md).

