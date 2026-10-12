# Novo Nordisk (NYSE: NVO ADR): metabolic franchise under price, pipeline and capacity pressure

[Research index](../../../index.md#2026-10-11) · [Run guidance](../../../README.md) · [Evidence](data/evidence.json) · [Calculations](data/calculations.json) · [Audit](data/audit.json)

As of2026-10-11. Conditional research, not an order or investment approval.

## Grounding

NYSE ADR quoted in USD, issuer reporting in **DKK under IFRS**, December fiscal year. **One ADR equals one B share** nominalDKK0.10; Copenhagen B shares and NYSE ADRs were split2:1 inSeptember2023, onSeptember13 and20 respectively [nvo-annual,sa-stats]. A/B have equivalent economic units but different votes: A100 versus B10 perDKK0.10; foundation-controlled governance is not equal to US ADR voting control. Regular closing ADR quote **$38.64, October9 2026 at16:00 EDT**; after-hours$38.62 excluded [sa-quote].

TickerLandia independently observes the split-adjusted ADR closing price $38.64 onOctober9 [tl-quote]. It supplies no intraday clock; the16:00 EDT timestamp is Stock Analysis's observed clock.

Information richness A in financial/clinical disclosure, but this package is provisional in currency/model terms. Reported FY2025 financial truth remains **DKK309.064b sales,102.434b profit,119.102b OCF,60.140b PP&E spend,23.03 diluted EPS** [nvo-annual,sa-fin]. Required USD engine inputs are **translation estimates**, not issuer-reported USD or native-tool FX verification. Flow/EPS estimates divide by6.62DKK/USD, balance estimates by6.35. These come from issuer note4.4's2025 average/year-end rates **applied for hedged currencies**, so are explicitly historical translation proxies, not independently sourced spot/October2026 rates. Mixing current USD price directly with DKK EPS23.03 would produce a meaningless multiple; this package does not do so. Raw DKK values and rates are preserved in evidence.json.

CashDKK26.464b excludes498m marketable securities. BorrowingsDKK130.958b include8.572b lease liabilities; this differs from issuer net-debt definition excluding leases and subtracting cash/securities [nvo-annual,sa-balance]. Actual2025 outstanding shares4.444b are not4.465b issued or4.4477b diluted weighted-average; June2026 vendor actual shares4.428b are used for quote reconciliation [sa-balance]. This count covers both economic classes, not ADRs actually deposited.

Vendor cap headline169.11b conflicts with its **dated October9 history row171.40b**. The latter reconciles with4.428b economic units times$38.64; headline is retained but rejected as comparable corroboration [sa-cap]. No claim that a second page from Stock Analysis independently verifies cap. Reported vendor operating-income140.618bDKK also differs from issuer127.658b; standardized figure is not used as IFRS operating profit [sa-fin,nvo-annual].

### Canonical native facts

|Fact|Value and unit|Period / status|Source IDs|
|---|---:|---|---|
|price|38.64 USD/share|2026-10-09 regular-session close; reported|[sa-quote], [tl-quote]|
|shares|4428000000 shares|June 2026 filing-date actual shares; observed 2026-10-11; reported|[sa-stats], [sa-balance]|
|market_cap|171400000000 USD|2026-10-09 regular-session close; reported|[sa-cap]|
|revenue|46686404833.836858 USD|FY2025 ended 2025-12-31; estimate|[nvo-annual], [sa-fin]|
|net_income|15473413897.280967 USD|FY2025 ended 2025-12-31; estimate|[nvo-annual], [sa-fin]|
|operating_cash_flow|17991238670.694864 USD|FY2025 ended 2025-12-31; estimate|[nvo-annual], [sa-fin]|
|capital_expenditure|9084592145.015106 USD|FY2025 ended 2025-12-31; estimate|[nvo-annual], [sa-fin]|
|cash|4167559055.118110 USD|2025-12-31; estimate|[nvo-annual], [sa-balance]|
|debt|20623307086.614173 USD|2025-12-31; estimate|[nvo-annual], [sa-balance]|
|eps|3.478852 USD/share|FY2025 ended 2025-12-31; estimate|[nvo-annual], [sa-fin]|

## Business

Patients repeatedly need diabetes/obesity medicines, and governments, insurers or self-pay patients pay Novo through prescription channels for glucose control, weight management and approved outcomes indications; alternatives include Lilly/other drugs, insulin, lifestyle care and surgery. Repeat treatment does not guarantee adherence, reimbursement or stable net pricing.

| FY2025 product | Sales DKK bn | Economic driver / caution |
|---|---:|---|
|Ozempic|127.089|Injectable semaglutide diabetes; access and competitive pressure |
|Wegovy|79.106|Obesity/outcomes; same semaglutide concentration |
|Rybelsus|22.093|Oral semaglutide diabetes; delivery economics differ |
|Rare blood/endocrine|11.955 /5.959|More diversified specialty products |
Vendor product series [sa-fin]; brand diversification does not eliminate common-molecule risk.

| Fiscal year | Sales DKK bn | Net profit DKK bn | OCF DKK bn | PP&E cash DKK bn |
|---|---:|---:|---:|---:|
|2021|140.800|47.757|55.000|6.335|
|2022|176.954|55.525|78.887|12.146|
|2023|232.261|83.683|108.908|25.806|
|2024|290.403|100.988|120.968|47.164|
|2025|309.064|102.434|119.102|60.140|
Observed annualreport/vendor series [nvo-annual,sa-fin]. Sales expansion slowed in2025 while capex rose; issuer gross margin81.0% and operating margin41.3% versus84.7%/44.2% in2024 are reported observations, not native-derived ratios [nvo-annual].

Q22026 adjusted salesDKK78.488b grew7% CER; H1 adjusted148.551b grew2%; Q2 adjusted gross margin78.2%, operating margin42.5%. August4 guidance revised adjusted sales/operating growth to0% to-6%CER, with lower DKK growth from currency [nvo-q2]. This supersedes the annualreport's earlier-5% to-13% outlook, not a promise of reaccelerating reported EPS. The adjusted P&L excludes **USD4.2b one-off noncash340B rebate-provision reversal**; reported/TTM growth may overstate underlying demand. Pill prescription claims use internal self-pay and IQVIA estimates—not randomized clinical outcomes or independently measured net realized price.

PP&E spend is not all reinvestment:2025 intangible purchasesDKK29.973b largely business development, and2024 acquisition of three former Catalent fill-finish sites USD11.7b materially affected old-definition FCF [nvo-annual]. Maintenance/growth distinction and capacity-unit returns are unavailable. Circle of competence includes mature metabolic-drug/access economics; clinical mechanism selection and future generic-entry timing remain uncertain.

## Moat

| Advantage | Evidence | Counterevidence / falsifier |
|---|---|---|
| Clinical outcomes package | FDA cardiovascular indication and event trial [fda-cv] | Outcomes in established CVD population do not prove primary-prevention benefit or every formulation's equivalence |
| Semaglutide IP | Active ingredient US2032, China2026, Europe/Japan2031 [nvo-annual] | Country patent cliff inside investment horizon; extra formulation/use patents do not guarantee all exclusivity |
| Manufacturing/reach | Large API/fill-finish capex,52Wegovy markets by2025 [nvo-annual] | OAI/warning letter at Bloomington2025; high invested capital without reliable output is not moat |
| Delivery portfolio | Oral and higher-dose Wegovy approvals; pipeline [nvo-q2] | Lilly oral/next-generation rivalry and lower prices; prescription volumes not profit |

FDA's March2024 indication rests on randomized double-blind placebo-controlled trial of over17,600 participants receiving standard-of-care/lifestyle counseling. MACE occurred6.5% with Wegovy versus8%placebo in adults with established cardiovascular disease and overweight/obesity [fda-cv]. These are observed incidence percentages, not an invented absolute survival gain. Body-weight loss endpoints in other trials cannot be substituted for this outcome. Historical thyroid/MTC/MEN2 and GI/pancreatitis/gallbladder warnings constrain treatment; dated release is not current labeling advice.

Pipeline is not assured moat: Q2 presentation states ZEUS ziltivekimab failed its primary time-to-first3-pointMACE endpoint, HR0.99 with95%CI0.88–1.11 in6,376ASCVD/CKD participants, despite inflammatory-pathway biomarker improvement; serious infections more frequent [nvo-q2]. Biomarker suppression did not establish clinical efficacy. CagriSema US decision was expected Q4; zenagamtide phase3 programs were underway/planned—not approved future revenue. [INFERENCE] Metabolic know-how likely endures, but five-year commercial leadership has become less secure and ten-year returns require replacement IP.

## Management

| Decision | Observed result | Stewardship judgment |
|---|---|---|
| Capacity acquisitions/build |2024 Catalent sites and2025 PP&E60.140bDKK [nvo-annual] | Strategic supply access; utilization, compliance and debt costs now matter |
|2025 transformation | About9,000positions reduced; annualized8bDKK savings from2026 intended for reinvestment [nvo-annual] | Cost reset acknowledges unsustainable hypergrowth staffing; savings not guaranteed distributable profit |
| Leadership/board changes | Doustdar succeeded Jorgensen; board renewed after Foundation disagreement [nvo-annual] | Control can favor long-term purpose but limits ADR minority influence; governance not presumed benign |
| Access/price reductions | Self-pay/channel and government frameworks [nvo-annual,nvo-q2] | More patients can coexist with lower revenue per patient |

Diluted IFRS EPS23.03 versus adjusted26.17 in2025 includes different impairment/amortization/restructuring treatment; adjusted measures should not erase economic research/acquisition failures [nvo-annual].2026 adjusted definitions also exclude major legal/noncash matters; 340B reversal is particularly material. Founder/foundation stewardship does not prove minority-owner alignment. Detailed current compensation targets, related-party fairness and succession planning were not independently retained. [INFERENCE] Scientific/manufacturing capabilities can survive CEO turnover; capital pacing and pipeline portfolio discipline must still improve.

## Inversion

| Risk | Mechanism / timing | Warning / mitigation |
|---|---|---|
| Net-price erosion | US payer/self-pay access traded for price now | Compare underlying adjusted volume and price, not headline340B benefit |
| Regional patent expiry | China2026, Europe/Japan2031, US2032 | Country mix/generic entry; no unsupported identical global cliff |
| Pipeline underperformance | CagriSema/zenagamtide depend on efficacy,tolerability,approval | Use exact endpoints/estimands; failed ZEUS illustrates biomarker trap |
| Overbuilt capacity/debt | Multiyear API/fill-finish cash demands | Watch utilization, warning-letter remediation, capex and lease debt |
| Currency/ADR ownership | USD shareholder return differs from DKK earnings | Keep DKK truth and estimate basis; no current spot FX claim |
| Legal/quality safety | Product liability,340B, recalls, OAI | Discrete potentially severe tail; not forced into a probability |

Strong bear thesis is not that obesity is unimportant: it is that a bigger treated population with cheaper competing medicines delivers less profit to Novo while fixed capacity stays expensive. Historic patent-cliff analogues suggest possible sharp regional erosion but do not identify precise launch dates, tender prices or which secondary patents withstand challenge. A material safety/quality intervention or failure of pipeline differentiation can be thesis-breaking. Avoid anchoring on the2021-24 growth curve or interpreting the decline in quoted ADR as proof of value.

## Industry

Discovery/trials/IP, regulated API/fill-finish, distribution, prescribing and reimbursement jointly set metabolic-drug economics. Durable chronic demand and potential disease modification are real; company-promoted population/TAM is not used as a numeric sales forecast. Funding coverage, side effects, adherence and access-price tradeoffs bound the serviceable market.

Lilly's tirzepatide and oral competition can displace Novo despite category growth; alternative combinations and delivery forms matter. Novo's2026 presentation reports approved Wegovy7.2mg and oral launches in new markets, but claims such as strongest volume launch are promotional operational comparisons with internally estimated TRx, not clinical superiority [nvo-q2]. Cardiovascular evidence may help payers justify access, yet plan budgets can still require prior authorization/rebates. Regional generics can expand affordable use while eroding incumbent economics [nvo-annual]. [INFERENCE] In twenty years Novo may remain a major metabolic institution; today's semaglutide monopoly-like margin cannot be assumed permanent.

## Valuation

**No EPS-growth price-target configuration is published.** Positive FY2025 IFRS earnings permit a historical multiple, but unsupported current USD earning capacity, a material2026 one-off rebate reversal, price/guidance reset and country-specific patent cliffs make a smooth fixed-growth model misleading. This is a completed valuation-applicability decision, not an unfinished target.

Engine historical P/E uses estimated translated FY2025 EPS **$3.478852 perADR** (DKK23.03/6.62), not DKK23.03 directly against USD38.64, nor vendor unspecified-FX TTM$4.00. It is a historical proxy multiple, **not current normalized or forward P/E**. Balance conversion uses6.35 rather than6.62 because stocks and flows require different historical conventions. These proxy conversions are separate researcher arithmetic and are not native-verified FX.

Native cash subtraction is OCF lessPP&E. It differs from issuer's2025 old-definition FCFDKK28.295b because intangibles, business acquisitions/settlements and related items remain outside the native metric; native DKK-equivalent subtractionDKK58.962b corresponds to vendor standard FCF, not issuer old-definition distributable cash [nvo-annual,sa-fin].2026 issuer FCF redefinition also moves to OCF lessPP&E [nvo-annual,nvo-q2]. A low historical multiple and positive cash yield can be deserved if profit falls or patent replacement consumes cash. The meaningful diligence question is sustainable underlying DKK profit and capex after rebates/price competition—not an unsupported target or reverseDCF.

### Native calculations

|Metric|Actual engine result|Interpretation|
|---|---:|---|
|Implied equity capitalization|$171,097,920,000.00|Price × selected actual economic share snapshot, not enterprise value|
|Cap deviation|0.1762%|Relative deviation, below1% tolerance; not source-truth certification|
|Historical OCF less cash PP&E|$8,906,646,525.68|FY2025; estimated FX inputs|
|Historical cash yield|5.1964%|Historical cash subtraction / observed rounded cap|
|Historical P/E|11.1071×|FY2025 estimated USD IFRS diluted EPS basis|

All these outputs are from [data/calculations.json](data/calculations.json). Annual balances are dated2025, not current2026 liquidity. FCF omits acquisitions, SBC dilution and debt service; insurer reserves or future factory investment are not discretionary owner cash.

## Decision

**Watchlist / attractive for deeper turnaround diligence, not a validated bargain.** Duan's repeated patient need and Li Lu's disease-treatment importance support business relevance; Buffett's protection erodes by jurisdiction; stewardship is resetting under concentrated control; Munger's inversion centers price/patent/capacity rather than a numerical TAM. Historical estimated multiple is modest, but underlying2026 earnings and future reinvestment are not sufficiently reconciled for a defensible USD target.

Review underlying sales excluding340B reversal, sustained net-price/volume mix, peer comparative endpoints, oral adherence/economics, CagriSema regulatory decision, regional generic entry and manufacturing remediation. Thesis-breaking conditions include sustained profit erosion despite volume expansion, major quality restrictions or failed replacement differentiation. AI evidence confidence medium on annual DKK facts and low-to-medium on USD normalization; economic certainty lower. No execution, allocation or guaranteed return is implied.

## Limitations and audit

Coverage is substantive but provisional: quote/share/capitalization generally lack two independent publishers; multiple issuer URLs and vendor pages do not add publisher independence. Annual required statements are historical, while quarterly updates are separately dated. Narrow debt aggregations are estimates; NVO required USD fundamentals are explicitly estimated FX proxies. Market-cap numerical reconciliation is not exact contemporaneous share verification. No current full proxy, product-level margins, patient retention, maintenance-capex split or confidential claims/quality/clinical data was retained. Three scenarios cannot represent catastrophic safety, legal, regulatory or operational tails. Sources and observed excerpts are retained in evidence.json; no publisher identity is inferred from a mirror host.

Access limitations: Novo issuer annualPDF,Q2presentation and DKK vendor statements fetched. Vendor cap headline conflicts with dated history; history row retained as canonical. No sourced contemporary spot FX; historical applied rates disclosed as estimate.

Native calculate exited **0**; valuation output is **null**, intentionally. Initial audit exited **1**, status **PROVISIONAL**, for price/share/capitalization coverage, all seven estimated USD fundamentals and omitted valuation. Independent dated price corroboration is now retained; the final audit is recorded in [data/audit.json](data/audit.json), with share/cap publisher gaps, seven FX-estimated fundamentals and omitted target intentionally unresolved. Offline arithmetic/schema checks do not verify exchange rates or source truth and are not investment approval.

### Retained source trail
- [nvo-annual](https://www.novonordisk.com/content/dam/nncorp/global/en/investors/irmaterial/annual_report/2026/novo-nordisk-annual-report-2025.pdf): Novo Nordisk, Annual Report 2025; observed2026-10-11.
- [nvo-q2](https://www.novonordisk.com/content/dam/nncorp/global/en/investors/pdfs/financial-results/2026/Q2-2026-Full%20presentation.pdf): Novo Nordisk, Q2 2026 investor presentation; observed2026-10-11.
- [sa-fin](https://stockanalysis.com/stocks/nvo/financials/): Stock Analysis, DKK annual financial overview; observed2026-10-11.
- [sa-balance](https://stockanalysis.com/stocks/nvo/financials/balance-sheet/): Stock Analysis, DKK balance sheet definitions; observed2026-10-11.
- [sa-stats](https://stockanalysis.com/stocks/nvo/statistics/): Stock Analysis, Capitalization snapshot; observed2026-10-11.
- [sa-cap](https://stockanalysis.com/stocks/nvo/market-cap/): Stock Analysis, Dated capitalization history; observed2026-10-11.
- [sa-quote](https://stockanalysis.com/stocks/nvo/history/): Stock Analysis, ADR regular closing price history; observed2026-10-11.
- [fda-cv](https://www.fda.gov/news-events/press-announcements/fda-approves-first-treatment-reduce-risk-serious-heart-problems-specifically-adults-obesity-or): U.S. Food and Drug Administration, Wegovy cardiovascular indication approval March8 2024; observed2026-10-11.
- [tl-quote](https://tickerlandia.com/en/stocks/novo-nordisk-nvo): TickerLandia dated split-adjusted ADR price history; observed2026-10-11.
