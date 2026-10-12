# Intel Corporation (NASDAQ: INTC) — Investment Research Report

> Four-master framework: Buffett · Munger · Duan Yongping · Li Lu
> Research date: **Sunday, 2026-10-11** (US markets closed; no session since Friday)
> Quote used: **$104.70 — regular-session close, Friday 2026-10-09, 4:00 PM EDT** (StockAnalysis and Yahoo Finance, identical). After-hours last: $104.43 (7:59 PM EDT, 2026-10-09). No historical quote has been substituted for the current one.
> Latest reported financial period: **Q2 FY2026 (quarter ended 2026-06-27)**, earnings release 2026-07-23, 10-Q filed 2026-07-24. Last full year: **FY2025 (ended 2025-12-27)**.
> Next catalyst: **Q3 FY2026 results on Thursday 2026-10-29, after market close** (Intel press release, 2026-10-06). All figures in this report predate that release.
> Currency: USD throughout. "M" = millions, "B" = billions.
> **Status: provisional research output — not fully audit-approved.** The data-sample audit passed, but the valuation audit failed with the actual risk-free rate. A diagnostic pass using the tool's stale default does not resolve that failure. See Appendix B and Limitations.

---

## 0. AI Research Bias Self-Awareness

### Information-richness rating: **Grade A (information-rich)**

Intel has been listed since 1971, is covered by about 49 sell-side analysts (StockAnalysis, updated 2026-10-06), files full SEC disclosures, and was one of the most-discussed stocks of 2026 (government equity stake, Nvidia/SoftBank investments, a $23B stock sale, Apple and Terafab foundry headlines).

**Grade-A trap.** Consensus is strong, and AI output tends to converge on it. With Intel, though, the "consensus" itself is split. The share price ($104.70) has moved far from the analyst rating mix: 32 of 49 rate it Hold, and Morningstar's fair value is $105 with no moat assigned. This report therefore focuses on the **counter-test**. What exactly is a $553B market cap paying for, and which parts of the bull narrative are verified facts versus unverified expectations?

**AI research limitations (declared up front):**
1. **Real-time feed unavailable.** The Interactive Brokers real-time quote tool was not authorized in this session. The quote comes from two public web sources (StockAnalysis, Yahoo Finance) showing the same Friday close.
2. **Macrotrends blocked.** Macrotrends, the project's designated primary US source, returned HTTP 403 to automated fetches. Macrotrends values appear only via search-engine snippets. SEC filings (8-K earnings releases, 10-Q, 10-K) were therefore used as the primary source, with StockAnalysis as the independent second source.
3. **Unofficial data.** Several high-impact facts are not officially disclosed: 18A yields (analyst estimates only), the Apple foundry relationship (unconfirmed by either company), and Terafab terms (non-binding).
4. **Q3 not yet reported.** Q3 FY2026 results arrive 18 days after this report. Q3 cash flow, the escrow-share mark-to-market and segment trends are unknown.

**Bias checklist:**
- [x] Is my sense of certainty coming from the business or from data volume? — Data volume is high, but business certainty is low (foundry outcome binary, AI CPU cycle young). Treated accordingly.
- [x] If half the data disappeared, would the conclusion change? — The valuation conclusion would not. It rests on a few robust numbers: market cap, record profits and current profits.
- [x] Is the analysis just echoing consensus? — No. Consensus price target ($118.05) is above the price, while this report's valuation is well below it. The divergence is explained in Section 7.
- [x] Could a "little data, great business" case be underrated? — Not applicable. The opposite risk applies: a large volume of narrative may make a still-unprofitable foundry look more certain than it is.

---

## 1. Data Collection — Key Facts

### 1.1 Quote and capital structure

| Item | Value | Source / note |
|------|-------|---------------|
| Share price (close 2026-10-09) | $104.70 | StockAnalysis; Yahoo Finance |
| Previous close (2026-10-08) | $107.08 | StockAnalysis; Yahoo |
| 52-week range | $32.89 – $142.35 | StockAnalysis; Yahoo (high set intraday 2026-06-30) |
| Drawdown from 52-week high | -26.4% | financial_rigor.py |
| 2026 YTD (vs 2025 close $36.90) | +183.7% | financial_rigor.py |
| Shares outstanding, 10-Q cover (as of 2026-07-17) | 5,044M | Q2 FY26 10-Q |
| Shares sold Aug 2026 incl. full greenshoe | 242.1M | 8-K 2026-08-12 (210,526,315 + 31,578,947 at $95.00) |
| Shares outstanding, estimated current | 5,286.1M | 10-Q + 8-K (excludes post-July RSU vesting/escrow movements) |
| Market cap (price × shares) | $553.5B | financial_rigor.py; Yahoo $553.455B (0.00%), StockAnalysis $550.15B (0.60%) |
| Enterprise value (estimate) | $567.2B | Mcap + debt $50.5B + NCI $15.6B − cash/STI $29.7B − est. net offering proceeds $22.65B |
| Beta (5Y monthly) | 2.23 | Yahoo; StockAnalysis |
| Short interest (record date 2026-09-30) | 3.32% | MarketBeat (167.2M shares) |
| Dividend | 0 | Suspended since Q4 2024 |

### 1.2 Five-year financials (GAAP, fiscal years)

| Metric (USD M) | FY21 | FY22 | FY23 | FY24 | FY25 |
|------|------|------|------|------|------|
| Revenue | 79,024 | 63,054 | 54,228 | 53,101 | 52,853 |
| GAAP gross margin | 55.4% | 42.6% | 40.0% | 32.7% | 34.8% |
| GAAP operating income | 19,456 | 2,334 | 93 | -11,678 | -2,214 |
| Net income attributable to Intel | 19,868 | 8,014 | 1,689 | -18,756 | -267 |
| Diluted EPS (USD) | 4.86 | 1.94 | 0.40 | -4.38 | -0.06 |
| R&D | 15,190 | 17,528 | 16,046 | 16,546 | 13,774 |
| Operating cash flow | 29,456 | 15,433 | 11,471 | 8,288 | 9,697 |
| Gross capex (Intel definition) | 18,733 | 24,844 | 25,750 | 25,122 | 17,672 |
| FCF (OCF − investing-section capex) | 9,127 | -9,411 | -14,279 | -15,656 | -4,949 |
| Intel "adjusted FCF" | 11,258 | -4,075 | -11,853 | -2,228 | -1,612 |
| Cash + short-term investments | 29,253 | 28,338 | 25,034 | 22,062 | 37,416 |
| Total debt (short + long term) | 38,101 | 42,051 | 49,266 | 50,011 | 46,585 |
| Dividend per share (USD) | 1.39 | 1.46 | 0.74 | 0.375 | 0 |

Sources: Intel Q4 earnings releases FY21–FY25 (SEC 8-K) and FY2025 10-K; StockAnalysis annual statements. Macrotrends snippets match revenue, net income, EPS, R&D and OCF.

**Definition notes:**
- StockAnalysis reports a "standardized" gross profit and operating income. For FY24 and FY25 its figures exclude impairment and accelerated depreciation charges in cost of sales, so they differ from GAAP. GAAP figures are used here.
- Intel's adjusted FCF nets government incentives and partner (SCIP) contributions against capex. The OCF − capex line does not.

**Facts:** Revenue fell 33% from FY21 to FY25 (CAGR -9.6%, financial_rigor.py). GAAP net income went from a $19.9B record (FY21) to two consecutive annual losses. FCF on the plain OCF − capex basis was negative for four straight years (FY22–FY25).

### 1.3 Last four quarters

Quarter ends: Q3 FY25 = Sep 27 2025; Q4 FY25 = Dec 27 2025; Q1 FY26 = Mar 28 2026; Q2 FY26 = Jun 27 2026.

| Metric (USD M) | Q3 FY25 | Q4 FY25 | Q1 FY26 | Q2 FY26 |
|------|------|------|------|------|
| Revenue | 13,653 | 13,674 | 13,577 | 16,128 |
| GAAP gross margin | 38.2% | 36.1% | 39.4% | 40.4% |
| Non-GAAP gross margin | 40.0% | 37.9% | 41.0% | 41.8% |
| GAAP operating income | 683 | 580 | -3,136 | 1,796 |
| GAAP net income | 4,063 | -591 | -3,728 | -11,033 |
| GAAP EPS (USD) | 0.90 | -0.12 | -0.73 | -2.16 |
| Non-GAAP EPS (USD) | 0.23 | 0.15 | 0.29 | 0.42 |
| Operating cash flow | 2,546 | 4,288 | 1,096 | 7,006 |
| Gross capex (Intel) | 2,956 | 4,021 | 4,963 | 2,652 |
| Intel adjusted FCF | 896 | 2,222 | -2,016 | -8,419 |
| Weighted diluted shares (M) | 4,531 | 4,856 | 5,083 | 5,104 |

Sources: Intel 8-K earnings releases Q3 FY25–Q2 FY26 and 10-Qs. StockAnalysis matches revenue, net income, EPS and OCF exactly.

**One-off items that dominate GAAP results (facts from filings):**
- **Q3 FY25:** +$5,452M gain on the Altera/Mobileye divestitures.
- **Q1 FY26:** $4,070M restructuring and other charges, mainly Mobileye goodwill impairment, plus a $1,090M escrow-share mark-to-market loss.
- **Q2 FY26:** a **$12,529M non-cash mark-to-market loss** on shares held in escrow for the US Department of Commerce (Secure Enclave program). This equals $2.45 per share and is the entire reason for the GAAP loss.
- **Q2 FY26 adjusted FCF** includes the **$14.2B buyback of Apollo's 49% stake in the Ireland Fab 34 joint venture** (closed 2026-04-08).

**TTM (Q3 FY25 – Q2 FY26):**

| TTM metric | Value | Source |
|------|------|------|
| Revenue | $57,032M | Sum of 8-Ks; StockAnalysis TTM (0.00%) |
| GAAP net income | -$11,289M | Sum of 8-Ks; StockAnalysis TTM (0.00%) |
| GAAP EPS | -$2.30 | StockAnalysis (TTM NI ÷ average shares); sum of quarters = -$2.11 |
| Non-GAAP EPS | $1.09 | Sum of quarterly non-GAAP EPS (financial_rigor.py) |
| Non-GAAP net income | $5,472M | Sum of quarters |
| Operating cash flow | $14,936M | Sum of 8-Ks; StockAnalysis $14.94B |
| FCF (OCF − investing capex $12,105M) | $2,831M | StockAnalysis |
| FCF (OCF − Intel gross capex $14,592M) | $344M | Calculated |
| Intel adjusted FCF | -$7,317M | Sum of 8-Ks (includes $14.2B Apollo buyback) |

### 1.4 Segments (Q2 FY26 and TTM)

| Segment (USD M) | Q2 FY26 revenue | YoY | Q2 FY26 op. income | Op. margin | TTM revenue | TTM op. income |
|------|------|------|------|------|------|------|
| Client Computing & Physical AI (CCPG, ex-CCG) | 8,877 | +12.8% | 2,343 | 26.4% | 33,332 | 9,762 |
| Data Center & AI (DCAI) | 6,262 | +59.0% | 2,474 | 39.5% | 20,168 | 6,230 |
| Intel Foundry | 5,765 | +30.5% | -2,089 | -36.2% | 19,928 | -9,356 |
| All other (Mobileye etc.) | 701 | -33.4% | 230 | n/m | 2,896 | 424 |
| Intersegment eliminations | -5,477 | — | 254 | — | — | — |
| Corporate unallocated | — | — | -1,416 | — | — | — |

Source: Q2 FY26 8-K (Q2 FY25 comparatives: CCG 7,871; DCAI 3,939; Foundry 4,417; All other 1,053). TTM is the sum of four quarterly 8-Ks. All calculations use financial_rigor.py.

**Foundry external revenue:**

| Period | External foundry revenue | Source |
|------|------|------|
| Q2 FY26 | $293M | Q2 FY26 10-Q |
| H1 FY26 | $467M | Q2 FY26 10-Q |
| FY2025 | $307M | FY2025 10-K |

External revenue is **5.1% of Foundry segment revenue**; the other ~95% is Intel's own products billed internally. For scale: TrendForce's Q2 2026 top-10 foundry ranking totals $53.49B, with TSMC at 72.5%. Intel's $293M would sit below the #10 player, PSMC ($432M).

Intel Foundry has now posted **10 consecutive quarterly operating losses** (Mark Lapedus, 2026-07-24). CFO Zinsner's internal breakeven target is end-2027, and he acknowledged it "could slip to end-2028" (Deutsche Bank conference, 2026-08-26, via TIKR).

### 1.5 Balance sheet and liquidity

| Item (USD M) | 2025-12-27 | 2026-06-27 | Source |
|------|------|------|------|
| Cash and equivalents | 14,265 | 12,874 | 10-Q |
| Short-term investments | 23,151 | 16,853 | 10-Q |
| Total cash + STI | 37,416 | 29,727 | 10-Q; StockAnalysis $29.73B |
| Short-term debt | 2,499 | 1,988 | 10-Q |
| Long-term debt | 44,086 | 48,549 | 10-Q |
| Total debt | 46,585 | 50,537 | 10-Q; StockAnalysis $50.54B |
| Intel stockholders' equity | 114,281 | 87,542 | 10-Q |
| Non-controlling interests | 12,079 | 15,601 | 10-Q (Brookfield Arizona SCIP $13,428M) |
| Total assets | 211,429 | 202,439 | 10-Q |
| Escrow-share derivative liability | ~2,700 | ~15,600 | 10-Q |

**Pro forma for the August 2026 offering (estimate):**
- Gross proceeds were $23.0B. Net proceeds are estimated at about $22.65B; the 8-K does not state net proceeds including the greenshoe.
- That lifts cash + STI to about **$52.4B**, against $50.5B of debt, i.e. **net cash of about +$1.8B before Q3 operating cash flows**.
- Book equity rises to about **$110.2B**, or BVPS ≈ $20.85.

These are estimates, pending the Q3 10-Q.

### 1.6 Ownership

| Holder | Shares | % of ~5,286M | Terms / source |
|------|------|------|------|
| US government (Dept. of Commerce) | 433.3M | 8.2% | Bought at $20.47 ($8.9B) in Aug 2025. 143M were still in escrow at 2026-06-27. Also holds a warrant for 241M shares at $20, exercisable only if Intel's foundry ownership falls below 51% (10-Q) |
| Vanguard | 404.5M | 8.1% (as of 2025-12-31) | 2026 proxy |
| BlackRock | 341.1M | 6.8% (as of 2025-12-31) | 2026 proxy |
| Nvidia | 214.8M | 4.06% | Bought at $23.28 ($5B); closed 2025-12-26. Worth ≈ $22.5B at $104.70 |
| SoftBank | 87.0M | 1.6% | Bought at $23.00 ($2B); closed 2025-09-26 |
| CEO Lip-Bu Tan | 1,331,640 | 0.025% | Form 4 (Aug 2026); worth ≈ $139.4M at $104.70 |
| All insiders | — | 0.07% | StockAnalysis |

Roughly **977M new shares** were issued to the government, SoftBank, Nvidia and August-2026 public buyers within 12 months. Weighted diluted shares rose **21.0%** from Q2 FY25 (4,369M) to the current estimate.

### 1.7 Consensus (as of 2026-10-06 to 2026-10-11)

| Item | Value | Source |
|------|------|------|
| FY2026E revenue | $63.10B | Yahoo; StockAnalysis (43 analysts) |
| FY2026E non-GAAP EPS | $1.52 | Yahoo; StockAnalysis (41 analysts; range $1.12–$1.74) |
| FY2027E revenue | $72.41B | Yahoo; StockAnalysis (47 analysts) |
| FY2027E non-GAAP EPS | $2.08 | Yahoo; StockAnalysis (47 analysts; range $1.45–$3.44) |
| Q3 FY26 guidance — revenue | $15.8–16.8B | Q2 FY26 8-K |
| Q3 FY26 guidance — non-GAAP EPS | $0.38 | Q2 FY26 8-K |
| Average price target | $118.05 | StockAnalysis (49 analysts: 15 Buy/Strong Buy, 32 Hold, 2 Sell) |
| Average price target (alt.) | $109.06 | MarketBeat (50 analysts) |
| Morningstar fair value | $105 | Morningstar 2026-07-24 (no moat, Very High uncertainty) |

> Full cross-validation log (financial_rigor.py output) is in **Appendix A**.

---

## 2. Business Nature — Duan Yongping's "Right Business"

### One-sentence definition

**Intel is a vertically integrated chipmaker: an x86 CPU franchise that still earns good money (CCPG + DCAI ≈ $16.0B TTM operating income) funds a capital-hungry contract-manufacturing bet (Intel Foundry, -$9.4B TTM operating loss) that has not yet found meaningful outside customers.**

### Revenue structure (Q2 FY26 external revenue mix)

```
Q2 FY26 consolidated revenue $16.1B (segment revenue before eliminations)
CCPG (PC CPUs)        ██████████████████████████████████  $8.9B  (+13% YoY)
DCAI (server CPUs)    ████████████████████████            $6.3B  (+59% YoY)
Foundry (internal)    █████████████████████▌              $5.5B  (eliminated on consolidation)
Foundry (external)    █                                   $0.3B
All other             ██▋                                 $0.7B
```

CCPG + DCAI account for 93.9% of consolidated Q2 revenue. Foundry is overwhelmingly an internal cost center that bills Intel's own product groups.

### Five-year profitability trend

```
GAAP net income (USD B)          GAAP gross margin
FY21  ████████████████████ 19.9   55.4%
FY22  ████████ 8.0                42.6%
FY23  ██ 1.7                      40.0%
FY24  (-18.8) ███████████████████ 32.7%   ← loss
FY25  (-0.3)                      34.8%   ← loss
TTM   (-11.3) ███████████ (incl. -$13.6B H1 FY26 non-cash escrow MTM)   38.6%
```

### Business-model canvas

| Dimension | Intel |
|------|------|
| Sale type | One-time hardware sale (CPUs/platforms) to OEMs and hyperscalers; no subscription revenue |
| Customers | Dell 19%, Lenovo 12%, HP 12% of FY2025 revenue (43% combined; FY2025 10-K) |
| Model | IDM (designs + manufactures), now trying to sell manufacturing externally like TSMC |
| Ecosystem | x86 instruction set: decades of Windows, enterprise and data-center software |
| Capital intensity | Gross capex $17.7B in FY25 (33% of revenue); 2026 guided to more than $20B; 2027 "significantly above" 2026 (company claim, Q2 call) |

### Ecosystem stickiness

- **Fact:** x86 still runs most PCs and servers. Mercury Research Q2 2026 unit shares are Intel 69.7% client and 65.5% server (ex-IoT).
- **On the other hand:** Apple moved Macs off x86. Arm's share of client CPUs reached 15.3% in Q2 2026 (Mercury). AWS says Graviton was more than half of its new CPU capacity for three straight years (AWS, 2025-12-03). Lock-in is real but leaking.

### Gross margin versus peers (TTM, StockAnalysis as of 2026-10-09; Intel uses its GAAP TTM)

| Company | Gross margin | Model |
|------|------|------|
| Arm | 97.5% | IP licensing |
| Nvidia | 74.7% | Fabless, AI accelerators |
| TSMC | 64.2% | Pure-play foundry |
| Texas Instruments | 58.3% | Analog IDM |
| AMD | 55.7% | Fabless CPUs/GPUs |
| Qualcomm | 54.2% | Fabless + licensing |
| Intel | 38.6% | IDM + loss-making foundry |

**Why Intel's margin is low:**
- **Facts:** Foundry carries full fab depreciation on ~95% internal volume. Intel pays TSMC for outsourced tiles. It also lost pricing power to AMD during 2022–2024.
- **On the other hand:** non-GAAP gross margin rose from 29.7% (Q2 FY25) to 41.8% (Q2 FY26). Drivers were a server mix shift, CPU price increases at end-Q1 2026 (TrendForce, 2026-09-29) and lower 18A unit costs (company claim: Panther Lake cost down about 50% YTD).

### Operating leverage

- **Fact:** Q2 FY26 revenue rose 25% YoY. GAAP operating income swung from -$3,136M (Q1, impairment-heavy) to +$1,796M, and DCAI operating margin reached 39.5%. Headcount fell 24.4% from 108.9K (end-2024) to 82.3K (2026-06-27).
- **Counterpoint:** DCAI growth was mostly **price/mix**, not volume. Server units rose +9% YoY while ASP rose +48% (Q2 FY26 10-Q). Client units fell -8% while ASP rose +27%. Price-led growth reverses faster than volume-led growth when supply loosens.

### Duan Yongping's question: what makes this business good, in one sentence?

**Good:** an installed-base CPU franchise. The x86 compatibility base and enterprise qualification cycles keep about two-thirds of x86 unit share with Intel even after five years of share loss, and in a CPU-constrained AI market that franchise prints 26–40% segment margins.

**But on the other hand:** Duan's test is "a business you would happily own if the market closed for 10 years." Intel's whole-company economics are still dragged by Foundry losing about $2B+ per quarter, so the parent is not yet that business. TTM non-GAAP net income was $5.5B (9.6% of revenue), and TTM FCF was roughly break-even to negative depending on definition.

---

## 3. Moat Assessment — Buffett's "Economic Moat"

| Moat type | Evidence | Strength | 5-year trend |
|------|------|------|------|
| Brand / pricing power | Intel raised select CPU prices at end-Q1 2026 (TrendForce) and server ASP rose 48%. This is pricing power in a **shortage**. In 2022–2024, with supply ample, Intel lost share and margin to AMD | ★★☆☆☆ | Narrowed; temporarily firmer in 2026 |
| Switching costs | x86 binary compatibility and enterprise validation are real. But Apple's full migration and hyperscalers' own Arm CPUs (Graviton5, Axion, Cobalt 200) show the cost is affordable for large buyers | ★★★☆☆ | Narrowing |
| Network effects | x86 developer and software ecosystem; Arm has built a parallel one across mobile, cloud and Mac | ★★☆☆☆ | Narrowing |
| Scale | Intel is the largest US-based leading-edge manufacturer. But scale in foundry means *external wafer volume and learning-curve data*, where TSMC has 72.5% share and Intel under 1% | ★★☆☆☆ | Unclear |
| Technology / IP | 18A brings GAA transistors plus backside power (PowerVia) and is in high-volume production since early 2026 (10-Q). TechInsights estimates high-density cell density at 238 MTr/mm² for 18A vs 313 for TSMC N2, so Intel is still behind on density. Diamond Rapids slipped to 2027 (Intel at Computex 2026) | ★★★☆☆ | Gap with TSMC narrowed vs 2021–23; not closed |
| Policy / strategic asset (non-classical) | US government is an 8.2% holder; CHIPS funding converted to equity; "only US-headquartered leading-edge logic fab" status | ★★★☆☆ | Widened since 2025 |

**Moat trend:**
- **Past five years:** clearly narrower. AMD's server **revenue** share rose to 46.2% in Q1 2026 (Mercury, via Wccftech), and Intel's consolidated GAAP gross margin fell from 55.4% (FY21) to 34.8% (FY25).
- **Next five years:** contested and binary. One outcome is that 14A wins anchor customers and Intel becomes a credible Western second source. The other is that Intel becomes a product company that buys leading-edge wafers from TSMC. The FY2025 10-K itself says that without an external 14A customer, Intel may "pause or discontinue" 14A and shift to third-party foundries.

### Buffett's questions: will this moat still exist in 10 years, and what could destroy it?

The x86 franchise is likely to persist in a smaller form, the way mainframes persisted. The question is whether its economics survive Arm and AMD. A durable moat would have to come from manufacturing, and that is unproven: $293M of quarterly external revenue does not make a moat.

**What could destroy it:**
1. Hyperscalers completing their Arm migration.
2. No anchor 14A customer, so the fabs become a stranded cost.
3. A policy shift that removes the "American-made" premium.

**But on the other hand:** if agentic-AI workloads keep CPUs supply-constrained through 2028 (Intel's own expectation, Q2 call), even a narrowing moat can produce several years of strong profits.

---

## 4. Inversion and Risk List — Munger's "Invert, Always Invert"

### Failure paths (probabilities are the author's subjective estimates, not data)

| Path | Est. probability | Impact | Evidence |
|------|------|------|------|
| No anchor external 14A customer by mid-2027; 14A scaled back | 35% | High | No named 14A customer as of 2026-10-11. Terafab is non-binding, and Musk said on 2026-10-08 that Terafab is also talking to TSMC. Apple is unconfirmed |
| AI-capex cycle reverses; semis de-rate | 30% | Very high | Oct 8 sell-off on an FT report of an OpenAI revenue shortfall; July 2026 -35.4% monthly drawdown |
| Price-led DCAI growth fades as AMD Venice and Arm CPUs add supply | 30% | High | Server units +9% vs ASP +48%. AMD Venice (TSMC N2) ships about a year ahead of Diamond Rapids |
| PC downturn hits CCPG | 40% | Medium | IDC: Q3 2026 PC shipments -20.1% YoY; 2026 forecast -11.3%; memory inflation into 2027 |
| Further equity dilution | 50% | Medium | About 977M shares issued in 12 months. Consensus expects negative FCF in 2026–27 (TIKR) and 2027 capex "significantly above" 2026 |
| 18A/18A-P execution slips | 30% | High | Diamond Rapids slipped to 2027; Crescent Island AI GPU likely slips to 2027 (Tech Insider). Yields unofficial |
| Government shareholder / policy intervention | 15% | Medium | Warrant blocks a foundry spin below 51%; political pressure on the CEO (Aug 2025) |
| Taiwan Strait conflict | 5% | Extreme, sign ambiguous | Intel relies on TSMC for some tiles and on Asian supply chains, but would also be a strategic beneficiary |

### Historical analogies

| Analogy | Similarity | Outcome | Lesson for Intel |
|------|------|------|------|
| Cisco, 2000 | Real franchise, priced for perfection at the top of a capex boom | Price took more than 20 years to recover even though the business kept growing | A good outcome for the business can still be a bad outcome for the shareholder |
| IBM, 2010s | Legacy franchise funding a slow-growth pivot | A decade of stagnant value | "Surviving" ≠ "compounding" |
| AMD, 2015–2020 | Near-distress to leadership under a new CEO | Share price rose about 30-fold | Turnarounds can work, but AMD started from a tiny market cap; Intel starts at $553B |
| GlobalFoundries, 2018 | Leading-edge foundry without enough external volume | Abandoned 7nm | Without anchor customers, leading-edge fab economics do not close |
| Samsung Foundry, 2015–2026 | Deep pockets, leading-edge ambitions | 5.9% share in Q2 2026 (TrendForce) after a decade | Capital alone does not dislodge TSMC |

### Cross-disciplinary models

- **Learning curve (manufacturing):** yield learning scales with wafer volume across many designs. TSMC's 72.5% share is self-reinforcing. Intel's external volume is too small to learn from at that pace. This is the core structural headwind for Foundry.
- **Game theory (buyer power):** large chip designers want a second source, which gives Intel a seat at the table. But Bernstein's Stacy Rasgon (Sep 2026) notes that buyers tend to place *lower-priority* chips at a second source, which lowers the volume and pricing Intel can earn.
- **Reflexivity (Soros):**
  - **Up-leg:** a higher share price let Intel sell $23B of stock at $95, which funds capex, which supports the narrative.
  - **Down-leg:** the same channel works in reverse. Funding gets costlier exactly when the narrative weakens.
  - **Accounting echo:** escrow-share mark-to-market losses grow as the stock rises.
- **Technology adoption curve:** Arm in Windows PCs is still at roughly 4–6% (TrendForce estimate), i.e. early adopters. In cloud CPUs it is past the early majority at the largest hyperscalers.

### Bias check

- **Narrative bias:** "agentic AI needs more CPUs" is supported by data (Mercury: server CPU shipments +20% YoY in Q2 2026). But the data says *market* growth, not *Intel share gains*: AMD gained 7.3 points of server unit share year over year.
- **Recency/anchoring:** the $142.35 high and the +25% quarter are vivid. The 4-year FY22–FY25 record is not.
- **The author's own bias:** the ten-year framework (Section 7) uses a 10% USD discount rate and an exit P/E of about 11x, which penalizes *any* richly valued stock. As a check, Section 7 shows the conclusion holds even at r = 9% with the bull case.

### Bull case (strongest points, from named sources)

1. **Server CPU demand.** Agentic AI has made CPUs a bottleneck. HSBC (target $200, 2026-07-02) forecasts server CPU shipments +25% in 2026 and +30% in 2027. BofA ($145) sees the server CPU market above $170B by 2030 with Intel at about 25%.
2. **Strategic scarcity.** Intel is the only US-headquartered leading-edge logic manufacturer, backed by government, Nvidia and SoftBank equity.
3. **Margin recovery.** Recovery is visible: non-GAAP gross margin up 12.1 points YoY, and the Foundry operating loss narrowed to -$2.09B from -$3.17B.

### Bear case (strongest points)

1. Foundry has lost about $9.4B TTM on only $0.3B per quarter of external revenue, and the breakeven target has already been allowed to slip to end-2028 (CFO, 2026-08-26).
2. Growth is price-led in a shortage, while AMD continues to take share.
3. Heavy dilution and rising capex. JPMorgan (Underweight, $85) and Rosenblatt (Sell, $80) are the published bears. Morningstar assigns no moat.

### Munger's questions

**Where am I most likely wrong?**
1. The CPU shortage could last much longer than expected. If DCAI reached, say, $50B+ of revenue at a 40% margin, the bull case in Section 7 would be too low. This is an illustration, not a forecast.
2. A binding Apple, Nvidia or hyperscaler 14A commitment would re-rate Foundry from cost center to option.
3. If US long rates fell sharply from 5.24%, the framework's exit multiples would rise.

**Why would smart people not buy, or short?** Section 7.4 shows what a $553B price requires.
- **To earn 10% a year from here:** 2036 net income of about 4–8 times Intel's *record* year (FY2021, $19.9B).
- **Merely to break even over ten years:** 1.6–3.0 times that record.

The share price discounts the successful turnaround *and* a foundry win, with no margin for delay.

---

## 5. Management — Duan Yongping's "Right People" + Buffett's "Integrity"

### CEO Lip-Bu Tan: key decisions

Lip-Bu Tan has been CEO since 2025-03-18. Before that he was CEO of Cadence Design Systems (2009–2021) and founder of Walden International.

| Date | Decision | Result (as of 2026-10-11) | Score |
|------|------|------|------|
| 2025-03 | Bought $25.0M of stock at $23.96 under his offer letter; pay heavily equity-linked | Strong alignment signal; stake now worth about 4.4x cost | ★★★★★ |
| 2025-04 → 09 | Sold 51% of Altera to Silver Lake ($8.75B valuation) | Closed 2025-09-12; $4.3B net consideration | ★★★★☆ |
| 2025-07 | Cancelled Germany/Poland projects; headcount down to about 82K; slowed Ohio (fab 1 now 2030–31) | Opex discipline; non-GAAP gross margin +12 points YoY by Q2 FY26 | ★★★★☆ |
| 2025-08 → 12 | Converted CHIPS grants to government equity ($20.47); SoftBank ($23.00) and Nvidia ($23.28) investments | Solved the funding crisis. In hindsight about 735M shares were sold at $20.47–$23.28, today's price is 4.5–5.1x that, and the deal created the escrow MTM swings and a warrant that constrains strategy | ★★★☆☆ |
| 2025-11 | AI chief / CTO Sachin Katti left for OpenAI after about 7 months | Talent-retention warning; Tan took over AI directly | ★★☆☆☆ |
| 2026-04 | Bought back Apollo's 49% of Ireland Fab 34 for $14.2B | Removes expensive partner capital; costs roughly a full year of TTM operating cash flow ($14.9B); returns depend on Fab 34 utilization | ★★★☆☆ |
| 2026-04 | Joined Musk's Terafab as development partner | Non-binding; Musk confirms talks with TSMC (2026-10-08) | ★★☆☆☆ (pending) |
| 2026-Q2 | Committed to 14A high-volume ramp in 2028 without a named external customer | Raises capex to more than $20B (2026) | ★★★☆☆ (pending) |
| 2026-08 | Sold 242.1M shares at $95 ($23.0B gross); Tan bought $10M in the offering | Opportunistic: issued stock at about 4x the 2025 issue prices | ★★★★☆ |

### Capital allocation

| Dimension | Evidence | Score |
|------|------|------|
| Capex discipline | Gross capex cut from $25.75B (FY23) to $17.67B (FY25), but now rising again (more than $20B in 2026; 2027 "significantly above") | ★★★☆☆ |
| Asset sales | Altera 51%, Mobileye secondary, NAND (earlier); NEX retained | ★★★★☆ |
| Equity issuance | About 977M shares issued in 12 months: cheap in 2025 (survival), expensive in 2026 (opportunistic) | ★★★☆☆ |
| R&D | R&D cut from $17.5B (FY22) to $13.8B (FY25), still 26.1% of revenue; output to be proven at 14A | ★★★☆☆ |
| Shareholder returns | No dividend since Q4 2024; no buybacks | ★★☆☆☆ (necessary) |

### Shareholder alignment

- **Ownership:** Tan holds 1,331,640 shares (0.025% of the company, about $139M). That is personally meaningful and was bought with his own money twice. Insiders as a group hold only 0.07%.
- **Pay:**
  - **2025 reported pay:** $93.0M (2026 proxy). Ongoing long-term awards are 60% relative-TSR PSUs (vs the S&P 500) and 40% options.
  - **New-hire PSUs:** paid on absolute share-price gains, with maximum payout at roughly a tripling.
  - **Implication (observation):** at $104.70 the stock is about 4.4x the March 2025 reference price, so these incentives are currently "in the money". From here on, the incentive favors share-price performance over the 3–5-year vesting window.
- **Say-on-pay:** support rose from 72% (2025) to about 87% (2026).
- **Insider selling:** in 2026 there was modest selling by some executives: ex-CLO Miller Boise in February and May; Chandrasekaran 21,024 shares at $118.28 on 2026-05-29.

### Organization and culture

- **Executive churn has been high.** Departures since mid-2025 include the CCO, Intel Products CEO, CTO/AI chief and chief legal officer. Hires include Kechichian from Arm (data center), Katouzian from Qualcomm (client), Seok-Hee Lee, ex-SK hynix CEO (packaging), and Bawa (legal).
- **The board was refreshed:** Craig Barratt became independent chair on 2026-05-13.
- **Employee sentiment** is mixed (Glassdoor about 3.9/5, positive outlook about 42%). This is a weak signal.

### Duan Yongping's question: if the CEO retired, could Intel stay competitive?

**Probably less so in the near term.** Tan personally runs the AI group after Katti's exit. His customer network (as Cadence CEO and a venture investor) is central to the foundry-customer pitch. The executive bench is largely less than 18 months in role.

**On the other hand:** the CPU franchise does not depend on one person. And the new hires come from strong operating companies (Arm, Qualcomm, SK hynix).

---

## 6. Industry and Civilization Trends — Li Lu's Framework

### Is this a civilization-level paradigm shift?

Yes. AI compute is the largest capex wave in semiconductor history:
- **WSTS (2026-06-02)** forecasts the 2026 semiconductor market at **$1,511.2B (+89.9%)**, after $795.6B in 2025.
- **Gartner (2026-08-24)** forecasts $1,555.2B.
- **But on the other hand:** about **$803.9B of the 2026 total is memory (+249.5%)**, a price-driven surge, while "Micro" (MPU+MCU+DSP), Intel's core category, is forecast at $101.7B (+19.8%). Intel is not on the steepest part of the curve.

| Shift | Direction | Intel's position |
|------|------|------|
| AI accelerators (GPU/ASIC) | Nvidia, AMD, custom ASICs dominate | **Largely absent.** Gaudi faded; Crescent Island likely 2027; Jaguar Shores undated |
| Agentic AI → CPU demand | CPU:GPU ratio moving from 1:4–1:8 toward 1:1–1:2 (TrendForce 2026-09-29) | **Beneficiary**, but sharing gains with AMD EPYC and Arm (Graviton5, Nvidia Vera) |
| ISA shift: x86 → Arm | Arm 15.3% of client CPUs (Q2 2026, Mercury) | **Defender** |
| Supply-chain re-shoring | US/EU push for local leading-edge capacity | **Key beneficiary**, though TSMC Arizona (about $265B commitment) competes for the same role |
| Advanced packaging | EMIB/Foveros relevant to AI chip assembly | **Credible option.** Packaging chief hired; no named signed contracts found |

### TAM

| Market | Latest | Forecast | Source |
|------|------|------|------|
| Global semiconductors | $795.6B (2025) | $1,511.2B (2026F); $1,913.7B (2027F) | WSTS 2026-06-02 |
| Server CPU | about $30B (2025, per one analyst estimate) | More than $120B by 2030 (AMD claim); about $170B (BofA); $131.5B (Citi) | Company/analyst estimates, not comparable in scope |
| Foundry ("Foundry 2.0", broad) | about $320B (2025, Counterpoint) | about +14% in 2026 (TSMC view) | Analyst/company estimates |
| PC market (value) | — | $274B in 2026 (+1.6% value, -11.3% units) | IDC 2026-03-12 |

### Value-chain position and concentration

- **Customer concentration:** Dell, Lenovo and HP were 43% of FY2025 revenue, and **China billings were 24%** (10-K). That is exposure to both PC-cycle and export-control risk.
- **Supplier dependence:**
  - **ASML** is sole source for EUV and High-NA EUV.
  - **TSMC** makes some product tiles. If 14A stalls, Intel says it would shift more to TSMC (10-K).
  - **Substrates and memory** are cited as 2026 supply constraints.
- **Technology route risk:**
  - **Process:** GAA + backside power (18A) is ahead of TSMC on backside power timing but behind on density.
  - **14A:** depends on High-NA EUV adoption.
  - **ISA:** an Arm/RISC-V shift threatens x86 regardless of process success.

### Li Lu's question: 20 years from now, "Standard Oil of this era" or "3Com"?

**Most likely neither.** The evidence points to a durable but no-longer-dominant infrastructure supplier. One plausible end state is a sizable x86/AI-CPU franchise plus a policy-supported Western foundry that serves a minority of leading-edge demand.

**Standard Oil outcome:** this requires Intel to become *the* Western alternative to TSMC at scale, and there is no evidence of that yet ($293M per quarter external).

**3Com outcome:** this requires both CPU share collapse *and* foundry failure. The 2026 CPU shortage and government backing make that unlikely within a decade.

**The investment question is narrower than the civilizational one.** Even the favorable path is already in the price (Section 7).

---

## 7. Valuation and Margin of Safety — Buffett's "Intrinsic Value" + Duan's "Right Price"

### 7.1 Current market pricing (all ratios computed with financial_rigor.py)

| Metric | Value | Basis |
|------|------|------|
| Price | $104.70 | Close 2026-10-09 |
| Market cap | $553.5B | 5,286.1M shares |
| P/E (GAAP TTM) | n/m | GAAP EPS -$2.30 |
| P/E (non-GAAP TTM) | 96.1x | Non-GAAP EPS $1.09 |
| P/E (FY2026E) | 68.9x | Consensus $1.52 |
| P/E (FY2027E) | 50.3x | Consensus $2.08 |
| P/S (TTM) | 9.70x | Revenue/share $10.79 |
| P/S (FY2026E) | 8.77x | Consensus revenue $63.1B |
| P/B (reported) | 6.03x | BVPS $17.36 (2026-06-27 equity ÷ 5,044M) |
| P/B (pro forma, est.) | 5.02x | BVPS $20.85 incl. est. offering proceeds |
| EV / TTM sales (est.) | 9.95x | EV ≈ $567.2B |
| FCF yield (TTM) | 0.51% | FCF $2,831M (OCF − investing capex) |
| Dividend yield | 0.00% | Suspended |

### 7.2 Versus Intel's own history (StockAnalysis, fiscal year-end multiples)

| Fiscal year-end | P/S | P/B | EV/Sales |
|------|------|------|------|
| FY2021 | 2.64x | 2.19x | 2.69x |
| FY2022 | 1.73x | 1.06x | 1.98x |
| FY2023 | 3.91x | 1.93x | 4.40x |
| FY2024 | 1.65x | 0.83x | 2.22x |
| FY2025 | 3.27x | 1.37x | 3.75x |
| Now (TTM) | 9.70x | 6.03x | 9.95x |

Current P/S is **2.5x the highest year-end level of FY21–FY25**. FY2021 was a year when Intel earned a 25.1% net margin; today the TTM non-GAAP margin is 9.6%.

### 7.3 Versus peers (StockAnalysis, close 2026-10-09)

| Company | Market cap | Forward P/E | P/S (TTM) | Gross margin | Latest-qtr revenue growth |
|------|------|------|------|------|------|
| Nvidia | $5.54T | 19.0x | 18.3x | 74.7% | +105.9% |
| TSMC | $2.07T (StockAnalysis; ~$2.35T on ADR basis) | 20.3x | 14.8x | 64.2% | +36.1% (TWD) |
| AMD | $992.7B | 54.8x | 24.0x | 55.7% | +50.1% |
| Arm | $284.4B | 111.6x | 55.2x | 97.5% | +22.4% |
| Texas Instruments | $259.1B | 29.3x | 13.3x | 58.3% | +22.8% |
| Qualcomm | $187.4B | 18.9x | 4.25x | 54.2% | -4.0% |
| **Intel** | **$553.5B** | **68.9x (FY26E) / 62.0x (StockAnalysis NTM basis)** | **9.70x** | **38.6%** | **+25.4%** |

- **Facts:** Intel's forward P/E is above Nvidia, TSMC and AMD, while its gross margin is the lowest and its growth is in the middle of the pack.
- **On the other hand:** Intel's P/S is below AMD, Nvidia and TSMC. A bull would argue that margin normalization (towards 50%+) would compress the forward P/E quickly. That is a forecast, not a fact.

### 7.4 Reverse DCF: what does $553.5B imply?

To earn a **10% annual return** over 10 years (the dilution drag is set at 1.5%/yr, since there is no dividend), the 2036 market cap must reach **$1,643.7B**.

| 2036 exit P/E | Required 2036 net income | Multiple of FY2021 record ($19.9B) |
|------|------|------|
| 10.7x (perpetuity-model exit, Section 7.6) | $153.6B | 7.7x |
| 20x (generous market multiple) | $82.2B | 4.1x |

Even **just to break even** (0% IRR), the 2036 market cap must reach $642.3B. That requires net income of $60.0B at 10.7x or $32.1B at 20x, i.e. 1.6–3.0x Intel's all-time record profit.

**Conclusion of the reverse DCF:** the current price assumes Intel becomes a materially larger and more profitable company than at any point in its 55-year history. Depending on the exit multiple and required return, it needs 2036 earnings between 1.6x the record (to break even, at a 20x exit) and 7.7x the record (to earn 10%, at the 10.7x framework exit).

### 7.5 Three-year, three-scenario valuation (financial_rigor.py three-scenario)

Base: FY2026E consensus non-GAAP EPS $1.52; horizon 3 years (FY2029).

| Scenario | EPS growth p.a. | Target P/E | FY2029 EPS | Target price | vs $104.70 |
|------|------|------|------|------|------|
| Bull | 50% | 35x | $5.13 | $179.6 | +71.5% |
| Base | 25% | 25x | $2.97 | $74.2 | -29.1% |
| Bear | 5% | 15x | $1.76 | $26.4 | -74.8% |
| Probability-weighted (25/50/25) | — | — | — | $88.6 | -15.4% |

- **What the bull case needs:** FY2029 EPS of $5.13 means net income of about $27.1B, 1.36x the FY2021 record. It is attainable only if DCAI keeps its 2026 momentum *and* Foundry losses largely disappear by 2028.
- **The base case** follows consensus FY2027E (+37%) and then decelerates. It still lands 29% below today's price.
- **Discounted at 10%:** the base-case 2029 price is worth $55.7 today and the probability-weighted price is worth $66.6 today. The current price is 57%–88% above those values.

### 7.6 Ten-year discounted valuation (terminal_value.py)

**Step 1 — Inputs and rationale**

| Input | Value | Rationale |
|------|------|------|
| Currency | USD | Cash flows in USD |
| r (cost of capital) | **10.0%** (sensitivity 9.0% / 11.5%) | US 10-year Treasury **5.24%** (Treasury.gov par curve, 2026-10-09; FRED DGS10 5.22% on 2026-10-08) + ERP ≈ 4.8% × β 1.0. Using the tool's 5.18% ERP would give 10.4%, so 10% is slightly *generous* to the stock |
| β | 1.0 | Framework default. Measured 5Y β of 2.23 reflects discrete 2024–26 events (near-distress, government deal, dilutive raises); those are handled as scenarios/tail, not in r (rule C3) |
| ROIC (steady-state incremental) | **12%** | Between current stock ROIC 3.42% (StockAnalysis, TTM) and the FY2021 pre-foundry-buildout ROIC of 20.42% (StockAnalysis). Foundry is more capital-intensive and Intel no longer holds a CPU monopoly, so the 2021 level is not assumed. Sensitivity: ROIC 18% |
| g (perpetual, after 2036) | **2% / 3% / 4%** (bear / base / bull) | USD nominal; base ≤ 4% cap |

**Step 2 — Audit (C1/C2/C3).** Full output is in Appendix B.
- **With actual rf 5.24% → 【打回】FAIL on C1 only.** The tool hard-codes USD rf = 4.70% (calibrated 2026-08-14) and rejects any rf more than 0.5 pct away. The 10Y yield has risen 0.54 pct since calibration. This is a tool-calibration failure, not a currency mismatch. The tool was **not** modified, per instructions.
- **With rf omitted (tool default band) → 【准出】PASS.** C1 ✓ (r = 10% within [9.0%, 11.5%], g base 3% ≤ 4%). C2 ✓ (r − g = 8.0 / 7.0 / 6.0 pct). C3 ✓ (all discrete risks assigned to scenario or tail).
- **One 未建模 (unmodeled) warning:** escrow-share mark-to-market accounting swings (see Limitations).

**Exit P/E** = (1 − g/ROIC) / (r − g), ROIC = 12%:

| r | g = 2% | g = 3% | g = 4% | r − g widths (pct) |
|------|------|------|------|------|
| 9.0% | 11.9x | 12.5x | 13.3x* | 7.0 / 6.0 / 5.0* |
| 10.0% (main) | 10.4x | 10.7x | 11.1x | 8.0 / 7.0 / 6.0 |
| 11.5% | 8.8x | 8.8x | 8.9x | 9.5 / 8.5 / 7.5 |

\*r = 9%, g = 4% sits exactly at the 5-pct minimum. The tool flags it "directional reference only", and it is used **as a scenario, not a valuation**.

**Step 3 — 2036 terminal-year net income scenarios** (author's estimates; FY2026E revenue base $63.1B consensus)

| Scenario | Prob. | 2036 revenue | Net margin | 2036 net income | Logic |
|------|------|------|------|------|------|
| Bull | 20% | about $160B (9.8% CAGR) | 25% | $40.0B | DCAI keeps share in a much larger AI-CPU market; Foundry becomes profitable with anchor 14A customers; net income 2x the FY21 record |
| Base | 45% | about $110B (5.7% CAGR) | 17% | $18.7B | CPU franchise grows with AI; Foundry roughly breakeven-to-modest profit; net income ≈ FY21 record |
| Bear | 25% | about $65B (flat) | 8% | $5.2B | AMD/Arm share gains; 14A scaled back; persistent foundry drag |
| Tail | 10% | — | — | $1.5B | Foundry write-down / geopolitical shock / restructuring; dilution 3%/yr; exit 8.8x |

**10-year IRR at $553.5B market cap** (terminal_value.py irr; payout term = 0% dividend − 1.5% dilution, tail −3.0%):

| Scenario | Exit P/E (r = 10%) | 2036 market cap | IRR |
|------|------|------|------|
| Bull | 11.1x | $444.0B | -3.68% |
| Base | 10.7x | $200.1B | -11.17% |
| Bear | 10.4x | $54.1B | -22.25% |
| Tail | 8.8x | $13.2B | -34.17% |
| Probability-weighted | — | $193.7B | -14.74% |

**r sensitivity (rank stability check):**

| Scenario | IRR at r = 9% | IRR at r = 10% | IRR at r = 11.5% |
|------|------|------|------|
| Bull | -1.89% (scenario-only cell) | -3.68% | -5.82% |
| Base | -9.76% | -11.17% | -12.92% |
| Bear | -21.18% | -22.25% | -23.56% |
| Bull with ROIC 18% (exit 13.0x, r 10%) | — | -2.12% | — |

- The ranking (bull > base > bear) is stable at every r.
- **The sign is negative in every cell**, including the most generous one (r = 9%, bull, g = 4%). A 2-pct error in r does **not** flip the conclusion.

**Price implied by a 10% IRR hurdle** (2036 value ÷ 1.115^10 ÷ 5,286.1M shares):

| Scenario | Entry price for 10% IRR |
|------|------|
| Bull (r = 10%) | $28.3 |
| Bull (r = 9%, scenario-only) | $33.9 |
| Base | $12.7 |
| Probability-weighted | $12.3 |

**Unmodeled discrete risks (for the Limitations section):** escrow-share mark-to-market accounting swings. These are non-cash but drive GAAP EPS, book value and potentially sentiment.

### 7.7 Price ranges

| Lens | Range per share | Read-across |
|------|------|------|
| Ten-year framework (10% hurdle) | $12 – $34 | Strict, rate-sensitive; even the bull case requires ≤ $34 |
| Three-year scenarios, discounted at 10% | $56 – $67 | Base PV $55.7; probability-weighted PV $66.6 |
| Three-year scenario spread (undiscounted 2029) | $26 – $180 | Shows the binary nature |
| Sell-side / Morningstar | $105 – $118 | Morningstar FV $105; consensus PT $118.05; these use higher multiples and assume continued AI-CPU strength |

**Synthesis:**
- **Fair-value estimate: $56–$67 per share**, based on the three-year market-multiple lens discounted at 10%.
- **Value-investor "margin of safety" price: ≤ $34**, where even the strict ten-year framework's bull case clears a 10% hurdle.
- **At $104.70 the stock is 57%–88% above the fair-value range** and about 3x the margin-of-safety price.

### Buffett's question: if r is wrong by 2 points, does the conclusion flip?

No. IRR stays negative across r = 9%–11.5%, and even the bull scenario with an 18% ROIC is negative. The conclusion rests on the size of required future profits relative to Intel's record, not on the discount rate.

### Duan Yongping's question: if the market closed for 5 years, would you hold at this price?

No. A five-year hold at $104.70 needs FY2031 profits well above the FY2021 record just to keep pace with a 10% hurdle. The business has not earned a GAAP profit in a full year since FY2023, and its foundry will not reach internal breakeven before end-2027 at the earliest.

---

## 8. Integrated Decision Memo

### Summary

| Dimension | Conclusion | Confidence |
|------|------|------|
| Business quality (Duan) | Mixed. A profitable CPU franchise (CCPG + DCAI ≈ $16.0B TTM op. income) is carrying a deeply loss-making foundry (-$9.4B TTM). Whole-company economics are not yet a "right business" | ★★★★☆ |
| Moat (Buffett) | Narrow and contested. x86 lock-in is eroding; manufacturing moat unproven; strategic/policy support is the strongest new element | ★★★★☆ |
| Management (Duan + Buffett) | Capable and decisive, with real personal investment. Heavy executive churn; key-person dependence on Tan; mixed record on equity issuance timing | ★★★☆☆ |
| Biggest risk (Munger) | **Valuation**: the price discounts a turnaround *plus* a foundry win. Secondary: 14A customer failure, AI-capex cycle reversal, dilution | ★★★★★ |
| Civilization trend (Li Lu) | Partly aligned: AI-driven CPU demand and re-shoring help; Intel is absent from AI accelerators and on the defensive in the ISA shift | ★★★★☆ |
| Valuation (Buffett + Duan) | **Overvalued.** Fair value $56–$67 (3-yr lens) vs $104.70; 10-yr IRR negative in every scenario | ★★★★☆ |

### Final decision

| Strategy | Recommendation |
|------|------|
| **No position** | **Avoid / do not buy at $104.70.** Re-examine at ≤ $67 only if a binding 14A anchor customer is announced. A genuine value entry is ≤ $34 |
| **Existing holders** | **Trim; do not add.** The position is priced for success. A holder who wants turnaround optionality can keep a small residual position sized for a 50%+ drawdown (the stock fell 35.4% in July 2026 alone) |
| **Sell signals** | (1) DCAI growth decelerates sharply while server ASP gains reverse; (2) no binding external 14A customer by mid-2027; (3) another large equity raise; (4) Foundry operating loss not narrowing below $2B per quarter through 2027 |
| **Buy / add signals** | (1) Price ≤ $34; or (2) price ≤ $67 **and** a binding, prepaid 14A anchor commitment **and** a Foundry quarterly loss under $1B |

### Simulated commentary from the four masters

> *The following are simulated viewpoints constructed from each investor's published principles. They are not actual quotes.*

> **Buffett (simulated):** "Price is what you pay; value is what you get. Here you pay $553 billion for a company whose best-ever year earned under $20 billion, and which hasn't produced a full-year GAAP profit since 2023. I can admire Lip-Bu Tan's work and still decline the price. A turnaround that succeeds can still be a poor investment if you paid for the success in advance."

> **Munger (simulated):** "Invert it. What has to go right? The CPU shortage has to last, AMD and Arm have to stop taking share, 18A and 14A have to yield, Apple or someone like them has to sign real volume, and the stock can't be diluted much more. That's a long chain of 'ands'. And the company itself just sold $23 billion of stock at $95. When management sells, I listen."

> **Duan Yongping (simulated):** "Right business, right people, right price. The people may be right. The business is half right: the CPU part makes money, the foundry part burns it. The price is not right. If I don't understand how the foundry earns a return, I don't buy, no matter how good the story."

> **Li Lu (simulated):** "Civilizationally, the West needs leading-edge manufacturing at home, and Intel is the natural candidate. That is why it will probably survive. But survival is not compounding. Over 20 years, Intel's most likely role is an important but no-longer-dominant supplier. Today's price is paying for dominance."

---

## AI Analysis Confidence vs Investment Certainty

### AI analysis confidence: **High** (Grade-A data)

**Conclusions based on solid, cross-validated data:**
- Quote, market cap and share count: two sources plus SEC 8-K/10-Q arithmetic, 0.00–0.68% deviation.
- Five-year and TTM financials, segment results and balance sheet: SEC filings plus StockAnalysis, 0.00–0.01% deviation.
- Reverse-DCF finding (price requires 1.6–7.7x record profits by 2036): rests only on market cap, record profit and arithmetic.
- Market-share data (Mercury), PC shipments (IDC), industry forecasts (WSTS/Gartner): published third-party data, cited with dates.

**Conclusions based on reasoning with limited information:**
- 2036 profit scenarios and their probabilities: author's estimates.
- 18A yields: analyst estimates only (KeyBanc 85%, GF Securities about 80%).
- Apple, Terafab and other foundry engagements: unconfirmed or non-binding.
- Duration of the AI-driven CPU shortage: company claims plus analyst opinion.

### Investment certainty: **Low**

The business outcome is binary (Foundry succeeds or not) and depends on events 2–3 years out. AI-capex cycles are volatile, as shown by the -35.4% month in July 2026 and the -26.4% drawdown from the June high. Only one statement about Intel is high-certainty: **at $104.70 the margin of safety is negative under every scenario modeled here.**

### Items to verify on 2026-10-29 (Q3 FY26 results)

1. DCAI revenue and units vs ASP. Is growth still price-led?
2. Foundry operating loss and external revenue (Q2: -$2.09B / $293M).
3. Any named, binding 14A customer, and 2027 capex guidance.
4. The escrow-share mark-to-market line. The price at the end of Q3 (Sep 25 close $123.00) was below the late-June level (June month-end close $139.63), so a *gain* is possible in Q3; it is non-cash either way.
5. Updated share count and net proceeds of the August offering.

---

## Limitations

1. **Quote source.** IBKR real-time data was not authorized in this session. The quote is the 2026-10-09 close from StockAnalysis and Yahoo Finance; no Monday session had occurred at the time of writing.
2. **Macrotrends unavailable.** Macrotrends returned HTTP 403 to automated access, so the designated primary US source was replaced by SEC filings (primary) plus StockAnalysis (secondary). Macrotrends values were seen only via search snippets.
3. **terminal_value.py C1 calibration failure.** With the actual 10Y yield (5.24%), audit C1 fails because the tool's USD rf constant is 4.70%. The audit passes with the tool's default. The tool was not modified. If the band were re-centered on 5.24%, it would shift up about 0.5 pct; r = 10% would still fall inside it, and the IRR signs would not change (Section 7.6 sensitivity).
4. **Unmodeled risk (C3 warning):** escrow-share mark-to-market swings. These affect GAAP EPS and book value but not cash.
5. **Estimates:**
   - Share count (5,286.1M) excludes RSU vesting and escrow movements after 2026-07-17.
   - Net offering proceeds (about $22.65B), pro forma cash/BVPS and EV are estimates.
6. **Subjective inputs.** Failure-path probabilities, scenario probabilities and 2036 profit levels are judgments.
7. **Timing.** Q3 FY26 results (2026-10-29) may materially change the data.
8. **Index not refreshed.** The research index (`reports/README.md`, `reports/index.json`) was not refreshed, per instruction not to modify other files.

---

## Appendix A — Key Data Cross-Validation Record (financial_rigor.py)

| Check | Sources | Values | Deviation | Result |
|------|------|------|------|------|
| Price (close 2026-10-09) | StockAnalysis / Yahoo | $104.70 / $104.70 | 0.00% | ✅ |
| Shares (post-offering) | 10-Q + 8-K / Yahoo-implied / StockAnalysis | 5,286.1M / 5,286.1M / 5,250M | 0.00% / 0.68% | ✅ |
| Market cap (verify-market-cap) | Calc vs Yahoo | $553.46B vs $553.455B | 0.00% | ✅ |
| Market cap (verify-market-cap) | Calc vs StockAnalysis | $553.46B vs $550.15B | 0.60% | ✅ |
| FY2025 revenue | 10-K / StockAnalysis / Macrotrends snippet | $52,853M ×3 | 0.00% | ✅ |
| FY2025 GAAP net income | 10-K / StockAnalysis / Macrotrends snippet | -$267M ×3 | 0.00% | ✅ |
| TTM revenue | Sum of 8-Ks / StockAnalysis | $57,032M / $57,032M | 0.00% | ✅ |
| TTM GAAP net income | Sum of 8-Ks / StockAnalysis | -$11,289M / -$11,289M | 0.00% | ✅ |
| Q2 FY26 revenue | 8-K / StockAnalysis | $16,128M / $16,128M | 0.00% | ✅ |
| Cash + STI (2026-06-27) | 10-Q / StockAnalysis | $29,727M / $29,730M | 0.01% | ✅ |
| Total debt (2026-06-27) | 10-Q / StockAnalysis | $50,537M / $50,540M | 0.00% | ✅ |
| TTM operating cash flow | Sum of 8-Ks / StockAnalysis | $14,936M / $14,940M | 0.01% | ✅ |
| Management ownership | Form 4 / StockAnalysis | Tan 1,331,640 sh (0.025%); insiders 0.07% | — | ✅ (single-class stock; economic = voting) |

**verify-valuation output (price $104.70):**

| Metric | Output |
|------|------|
| P/E (non-GAAP TTM EPS $1.09) | 96.06x |
| P/B (BVPS $17.36) | 6.03x |
| P/FCF (FCF/share $0.5356) | 195.48x |
| FCF yield | 0.51% |
| P/S (revenue/share $10.789) | 9.70x |
| Dividend yield | 0.00% |

**Known definitional discrepancies (not errors):**
1. **GAAP vs StockAnalysis "standardized" figures.** StockAnalysis gross profit and operating income differ from GAAP for FY24 and FY25 by exactly the impairment and accelerated-depreciation charges in cost of sales.
2. **Three FCF definitions:** OCF − investing capex, OCF − Intel gross capex, and Intel adjusted FCF. These range from +$2.8B to -$7.3B TTM.
3. **TTM GAAP EPS:** -$2.30 (TTM net income ÷ average shares, StockAnalysis) vs -$2.11 (sum of quarterly EPS).
4. **StockAnalysis share count:** 5.25B, versus 5,286.1M estimated here. StockAnalysis appears to exclude the greenshoe shares.

## Appendix B — terminal_value.py Audit Output (final parameters)

```
Run 1: --currency USD --r 0.10 --roic 0.12 --g 0.02,0.03,0.04 --rf 0.0524 --beta 1.0
  C1 ✗  "无风险利率 5.24% 与 USD 的 4.70% 不符"  (tool constant calibrated 2026-08-14)
  C2 ✓  r-g = 8.0 / 7.0 / 6.0 pct; PE = 10.4x / 10.7x / 11.1x
  C3 ✓  8 risks → 情景/尾部档; 1 risk → 未建模 (escrow MTM)
  Verdict: 【打回】(C1 only)

Run 2: same parameters, --rf omitted (tool default USD band, Rf 4.70%)
  C1 ✓  r = 10% ∈ [9.0%, 11.5%]; base g 3.0% ≤ 4.0%
  C2 ✓  r-g = 8.0 / 7.0 / 6.0 pct
  C3 ✓  (1 未建模 warning: escrow-share MTM — disclosed in Limitations)
  Verdict: 【准出】
```

Discrete-risk assignment: 18A/14A process or yield failure → scenario; foundry external customers fail to materialize → scenario; Taiwan Strait conflict → tail; US government / policy intervention → scenario; accelerated Arm substitution → scenario; China export controls (24% of billings) → scenario; further equity dilution → scenario; AI-capex / memory-cycle reversal → scenario; escrow-share MTM → unmodeled.

Both runs were repeated with the final report parameters as the Step-4 pre-release re-audit (2026-10-11), with identical results.

## Appendix C — Report Audit (report_audit.py)

**Step 1 — extract:** `python3 tools/report_audit.py extract --report reports/INTC-investment-research-20261011.md --seed 20261011`
- 493 data points were extracted and 30 sampled (15% rate, capped at 30).
- **7 of the 30 were parser artifacts**, not data: digits inside source labels ("10-Q" ×2, "Q2 FY26 10-Q", "8-Ks"), calendar years in prose (2021, 2025) and "7nm". They were marked "not a data point" and skipped.

**Step 2 — re-fetch / recompute:** the remaining 23 points were checked against two sources each. Model outputs (IRR, scenario price, multiples) were checked by independent recomputation with financial_rigor.py.

**Step 3 — verdict:** **【准出】(PASS).** 23 checked: 23 pass, 0 warnings, 0 fails.

| Sampled point | Reported | Source 1 | Source 2 | Max dev. |
|------|------|------|------|------|
| Previous close 2026-10-08 | 107.08 | StockAnalysis history 107.08 | Yahoo 107.08 | 0.00% |
| Enterprise value (est.) | 567.2B | Recompute 567.22B | StockAnalysis 570.71B | 0.62% |
| Revenue FY22 | 63,054 | Intel Q4 FY23 8-K 63,054 | StockAnalysis 63,054 | 0.00% |
| Revenue FY21 | 79,024 | StockAnalysis 79,024 | Intel Q4 FY22 release 79.0B | 0.03% |
| GAAP gross margin FY25 | 34.8% | Intel Q4 FY25 release 34.8% | Macrotrends snippet 34.77% | 0.09% |
| Intel adjusted FCF FY22 | -4,075 | Intel Q4 FY23 8-K | Intel Q4 FY22 release | 0.00% |
| OCF Q3 FY25 | 2,546 | Intel Q3 FY25 8-K | StockAnalysis | 0.00% |
| Gross capex Q1 FY26 | 4,963 | Intel Q1 FY26 release | 10-Q H1 derivation | 0.00% |
| CCPG op. income Q2 FY26 | 2,343 | Q2 FY26 8-K | 10-Q segment note | 0.00% |
| Short-term investments 2026-06-27 | 16,853 | 10-Q | StockAnalysis | 0.00% |
| Total cash + STI 2026-06-27 | 29,727 | 10-Q | StockAnalysis | 0.00% |
| TSMC gross margin TTM | 64.2% | StockAnalysis 64.23% | Revenue-weighted quarterly 64.23% | 0.05% |
| Intel GAAP gross margin TTM | 38.6% | Sum of 8-Ks 38.60% | StockAnalysis (standardized) 38.87% | 0.70% |
| P/E non-GAAP TTM | 96.1x | financial_rigor 96.06x | — | 0.04% |
| FY2024 P/B | 0.83x | StockAnalysis 0.83x | Recompute 0.834x | 0.43% |
| Current P/B | 6.03x | StockAnalysis 6.03x | financial_rigor 6.03x | 0.00% |
| TSMC latest-qtr growth (TWD) | 36.1% | StockAnalysis 36.05% | Recompute 36.05% | 0.14% |
| Texas Instruments market cap | 259.1B | StockAnalysis 259.12B | Yahoo 259.125B | 0.01% |
| Bear 3-yr target price | 26.4 | Recompute 26.39 | three-scenario output 26.4 | 0.04% |
| Base IRR at r = 9% | -9.76% | Recompute -9.758% | terminal_value.py -9.76% | 0.02% |
| Bear IRR at r = 10% | -22.25% | Recompute -22.251% | terminal_value.py -22.25% | 0.00% |
| Morningstar fair value | 105 | morningstar.com | global.morningstar.com | 0.00% |
| P/FCF | 195.48x | Recompute 195.50x | StockAnalysis 194.33x | 0.59% |

**Step 4 — valuation re-audit:** see Appendix B. 【准出】 with the tool's default USD band; 【打回】 on C1 only when the actual 5.24% rf is passed (tool calibration; Limitations #3).

## Appendix D — Sources

**Primary (SEC / Intel):**
- Intel Q2 FY2026 earnings release, 8-K (2026-07-23): https://www.sec.gov/Archives/edgar/data/0000050863/000005086326000155/q226earningsrelease.htm
- Intel Q2 FY2026 10-Q (filed 2026-07-24): https://www.sec.gov/Archives/edgar/data/50863/000005086326000157/intc-20260627.htm
- Intel FY2025 10-K: https://www.sec.gov/Archives/edgar/data/50863/000005086326000011/intc-20251227.htm
- Intel Q1 FY2026 release: https://www.intc.com/news-events/press-releases/detail/1767/intel-reports-first-quarter-2026-financial-results/
- Intel Q4 FY2025 release: https://www.intc.com/news-events/press-releases/detail/1759/intel-reports-fourth-quarter-and-full-year-2025-financial-results
- Intel Q3 FY2025 release (8-K): https://www.sec.gov/Archives/edgar/data/50863/000005086325000169/q325earningsrelease.htm
- Intel Q4 FY2023 release (8-K): https://www.sec.gov/Archives/edgar/data/50863/000005086324000008/q423_earningsrelease.htm
- Intel Q4 FY2022 release: https://www.intc.com/news-events/press-releases/detail/1600/intel-reports-fourth-quarter-and-full-year-2022-financial
- August 2026 offering 8-K (greenshoe exercised 2026-08-11): https://www.sec.gov/Archives/edgar/data/0000050863/000119312526346806/d117670d8k.htm
- Intel Q3 FY2026 results date announcement (2026-10-06): https://www.intc.com/news-events/press-releases/detail/1782/intel-to-report-third-quarter-2026-financial-results
- Tan Form 4 (Aug 2026): https://www.sec.gov/Archives/edgar/data/0000050863/000005086326000177/form4.xml
- US government agreement (2025-08-22): https://www.intc.com/news-events/press-releases/detail/1748/intel-and-trump-administration-reach-historic-agreement-to

**Market data:**
- StockAnalysis — overview, statistics, financials, ratios, history, forecast: https://stockanalysis.com/stocks/intc/
- StockAnalysis — TSM and TXN statistics/financials: https://stockanalysis.com/stocks/tsm/statistics/ ; https://stockanalysis.com/stocks/txn/statistics/
- Yahoo Finance — quote and analysis: https://finance.yahoo.com/quote/INTC/
- US Treasury daily par yield curve (Oct 2026): https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_yield_curve&field_tdr_date_value_month=202610
- FRED DGS10: https://fred.stlouisfed.org/series/DGS10
- MarketBeat short interest / forecast: https://www.marketbeat.com/stocks/NASDAQ/INTC/short-interest/

**Industry / competition:**
- Mercury Research via HotHardware (2026-08-21): https://hothardware.com/news/amd-record-x86-market-share-cut-intels-chip-lead
- Mercury Research via Wccftech (2026-05-13): https://wccftech.com/amd-posts-record-server-cpu-revenue-in-q1-2026-red-team-commands-30-percent-market/amp/
- IDC PC shipments Q3 2026 (2026-10-08): https://www.idc.com/?p=121750
- IDC 2026 PC outlook (2026-03-12): https://www.idc.com/resource-center/press-releases/idc-cuts-2026-pc-outlook-to-11-3-as-memory-shortages-and-supply-chain-disruptions-persist-into-2027/
- WSTS forecast (2026-06-02): https://www.wsts.org/esraCMS/extension/media/f/WST/7618/WSTS_FC-Release-2026-May.pdf
- Gartner semiconductor forecast (2026-08-24): https://www.gartner.com/en/newsroom/press-releases/2026-08-24-gartner-forecasts-worldwide-semiconductor-revenue-to-reach-1-trillion-dollars-in-2026
- TrendForce foundry ranking Q2 2026 (2026-09-09): https://www.trendforce.com/presscenter/news/20260909-13225.html
- TrendForce agentic-AI CPU analysis (2026-09-29): https://www.trendforce.com/insights/agentic-ai-cpu-gpu
- AMD Q2 2026 results: https://ir.amd.com/news-events/press-releases/detail/1295/amd-reports-second-quarter-2026-financial-results
- Mark Lapedus on Intel Q2 (2026-07-24): https://marklapedus.substack.com/p/intel-posts-results-losses-mount
- TIKR on foundry breakeven (Zinsner, 2026-08-26): https://www.tikr.com/blog/intel-stock-fell-nearly-6-in-a-day-heres-the-foundry-deadline-that-matters-more
- Terafab update (2026-10-07): https://www.thestar.com.my/tech/tech-news/2026/10/07/intel-to-keep-working-on-musk039s-terafab-chipmaking-venture-bloomberg-news-reports

**Management / opinion:**
- Morningstar fair value update (2026-07-24): https://www.morningstar.com/stocks/intel-earnings-raising-fair-value-estimate-thanks-stunning-rise-server-cpu-demand ; https://global.morningstar.com/en-gb/stocks/intel-raising-our-fair-value-estimate-increased-server-cpu-optimism
- 2026 proxy extract: https://www.stocktitan.net/sec-filings/INTC/def-14a-intel-corp-definitive-proxy-statement-9f8b9f4b919f.html
- Intel leadership appointments (2026-05-04): https://www.intc.com/news-events/press-releases/detail/1768/intel-announces-leadership-appointments-to-advance-client
- CNBC on the offering (2026-08-10): https://www.cnbc.com/2026/08/10/intel-intc-stock-offering-ai.html
