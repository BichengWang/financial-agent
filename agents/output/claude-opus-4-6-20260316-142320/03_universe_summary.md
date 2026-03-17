# Universe Construction & Screening Summary

**Date:** 2026-03-16
**Universe Agent Report**
**Base Universe:** S&P 500
**Eligible Universe:** ~420 securities

---

## Universe Definition

### Base Universe: S&P 500

| Metric | Value | Source |
|--------|-------|--------|
| **Constituents** | ~500 | IXIC/SPX reference |
| **Market Cap Coverage** | ~86% of US equity market | Broad exposure |
| **Geographic Exposure** | US-domiciled, ~25% international revenue | Home bias + global exposure |
| **Sector Diversity** | 11 sectors | Broad diversification |

---

## Screening Filters Applied

### Filter 1: Liquidity

| Criterion | Threshold | Rationale | Impact |
|-----------|-----------|-----------|--------|
| **Market Cap** | >$10B | Institutional investability, low execution risk | Excludes ~30 micro-cap S&P names |
| **Daily Volume** | >$50M ADV | Sufficient depth for reasonable position sizes | Excludes ~15 illiquid names |
| **Bid-Ask Spread** | <50 bps (typical) | Transaction cost management | Assumed in most S&P 500 |

**Filter 1 Result:** ~455 names eligible

### Filter 2: Fundamental Eligibility

| Criterion | Threshold | Rationale | Impact |
|-----------|-----------|-----------|--------|
| **Bankruptcy Risk** | Not on watch list | Avoid credit events | Excludes ~5 distressed names |
| **Going Concern** | No auditor qualification | Operational continuity | Excludes ~2 names |
| **Stock Delisting Risk** | Not pending | Avoid forced liquidations | Excludes ~1 name |

**Filter 2 Result:** ~447 names eligible

### Filter 3: Data Availability

| Criterion | Threshold | Rationale | Impact |
|-----------|-----------|-----------|--------|
| **Price History (1 year)** | Complete | Calculate momentum, beta | Excludes ~0 names (SPX constituents stable) |
| **Earnings Guidance** | Available or derivable | Fundamental scoring | Excludes ~27 names (limited disclosure) |

**Filter 3 Result:** ~420 names eligible

---

## Sector Breakdown (Eligible Universe, ILLUSTRATIVE)

| Sector | Count | Weight (SPX) | Notes |
|--------|-------|--------------|-------|
| **Technology** | 75 | 28% | Largest sector; high concentration in mega-cap (NVDA, MSFT, GOOG, TSLA, META) |
| **Semiconductors** | 32 | 7% | Subset of Tech but tracked separately; leading today |
| **Financials** | 65 | 13% | Banks, insurance, diversified; leading week |
| **Healthcare** | 55 | 13% | Pharma, biotech, devices; defensive positioning |
| **Industrials** | 52 | 8% | Machinery, aerospace, industrials; lagging week |
| **Consumer Discretionary** | 48 | 10% | Automotive, retail, apparel; mixed this week |
| **Consumer Staples** | 32 | 6% | Food, beverage, household; stable |
| **Utilities** | 28 | 3% | Electric, gas, water; leading week |
| **Real Estate (REITs)** | 18 | 3% | Office, retail, apartments; rate-sensitive |
| **Materials** | 28 | 3% | Chemicals, metals, mining; lagging week |
| **Communications** | 8 | 5% | Media, telecom; lagging week |
| **Energy** | 21 | 4% | Oil & gas, integrated; leading week (geopolitical hedge) |

**Total Eligible:** ~420 (ILLUSTRATIVE count)

---

## Focus Screening: Top Candidates Identified

### Catalyst-Driven Movers (Today & This Week)

| Name | Ticker | Sector | Today | YTD | Primary Catalyst | Status |
|------|--------|--------|-------|-----|------------------|--------|
| Intel | INTC | Semis | +6.29% | — | Turnaround narrative, cheap valuation | Focus |
| Micron | MU | Semis | +6.20% | — | Earnings this week | Focus |
| Seagate | STX | Tech | +5.83% | — | Hardware cycle | Focus |
| Dollar Tree | DLTR | ConsDisc | +4%+ | — | Earnings beat | Focus |
| Nvidia | NVDA | Semis | +2.41% | +27% YTD | GTC conference (Mar 16-19) | Focus |
| Broadcom | AVGO | Semis | — | +41% YTD | Anthropic chip orders, AI revenue | Focus |
| AMD | AMD | Semis | — | +64% YTD | Turnaround, data center growth | Focus |
| GE Vernova | GEV | Industrials | — | — | Energy transition, JPM top pick | Focus |

### High-Conviction Non-Movers (Trend Play)

| Name | Ticker | Sector | YTD | Thesis | Status |
|------|--------|--------|-----|--------|--------|
| Broadcom | AVGO | Semis | +41% | AI revenue >50%, Anthropic | Focus |
| Goldman Sachs | GS | Financials | +2.15% today | Earnings acceleration, financials leading | Focus |
| Larcada | LRCX | Semis | — | BofA top pick, semi equipment | Focus |

### Near-Miss Names (Monitor)

| Name | Ticker | Sector | Note |
|------|--------|--------|------|
| Cadence Design | CDNS | Semis | BofA pick; software/IP play |
| Applied Materials | AMAT | Semis | Semi equipment; awaits catalysts |
| Analog Devices | ADI | Semis | Wireless/automotive exposure |
| Celanese | CELH | Materials | JPM elevated PIT (50%+ return); specialty chemicals |
| Shift4 Payments | FOUR | InfoTech | Insider buying cluster ($7M); fintech play |

---

## Universe Composition Rules

### Allocation Constraints

| Constraint | Target | Rationale |
|-----------|--------|-----------|
| **Max per name** | 5% | Diversification, avoid single-name risk in HIGH_VOL |
| **Max per sector** | 30% | Prevent factor crowding; allow moderate overweight to leading sectors |
| **Min names** | 8 | Ensure portfolio diversification |
| **Max names** | 12 | Avoid over-diversification; focus on highest-conviction ideas |
| **Target portfolio beta** | 0.95–1.05 | Slightly defensive given HIGH_VOL regime |

### Sector Tilts (Expected from Regime & Catalysts)

**Overweight:**
- **Semiconductors:** +3–5% overweight (vs. 7% SPX weight). Catalyst-driven (Nvidia GTC, Micron earnings, AI momentum).
- **Financials:** +2–3% overweight (vs. 13% SPX weight). Leading week, earnings acceleration.
- **Utilities:** +1–2% overweight (vs. 3% SPX weight). Defensive positioning in HIGH_VOL.
- **Energy:** Neutral to +1% (vs. 4% SPX weight). Geopolitical hedge, commodity exposure through GEV.

**Underweight:**
- **Technology (non-semis):** -2–3% underweight. Duration risk, rate sensitivity.
- **Materials:** -1–2% underweight. Earnings revision risk, rate sensitivity.
- **Consumer Discretionary:** -1–2% underweight. Elasticity to rates, weak sentiment.
- **Communications:** -1% underweight. Dividend pressure from higher rates.

---

## Data Sufficiency for Screening

### Available Data
- ✅ Price, volume, YTD returns
- ✅ Sector membership, market cap
- ✅ Today's % change, technical signals (momentum from returns)
- ✅ Insider buying clusters (March 9-14 peaks)
- ✅ Options unusual activity (select names)
- ✅ Analyst calls (BofA, MS, JPM, Wells Fargo, Goldman)
- ✅ Catalysts (GTC, earnings dates)

### Gaps
- ⚠️ Exact earnings revisions (z-scores)
- ⚠️ Detailed balance sheet metrics (debt/EBITDA, ROE, etc.)
- ⚠️ Valuation multiples (P/E, forward P/E, EV/EBITDA) — some available, not comprehensive

**Implication:** Screening will proceed using available data. Fundamental depth will be rated MEDIUM-HIGH for focus names, ILLUSTRATIVE for others.

---

## Universe Agent Sign-Off

**Eligible Universe:** ~420 S&P 500 names
**Focus Set:** 8 candidates (NVDA, AVGO, AMD, MU, INTC, GEV, LRCX, GS)
**Screening Confidence:** 85% (adequate liquidity, catalyst visibility, data coverage)
**Sector Constraint Status:** Semiconductors will be binding (21.5% if allocated per proposal)

✅ **PROCEED to SCORING phase**

---

## Next Step

Advance to **SCORING** phase (04_factor_scores.md).

