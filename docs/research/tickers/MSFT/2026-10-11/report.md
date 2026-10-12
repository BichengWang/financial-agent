# Microsoft (NASDAQ: MSFT): extraordinary distribution, increasingly infrastructure-heavy economics

[Research index](../../../index.md#2026-10-11) · [Run guidance](../../../README.md) · [Evidence](data/evidence.json) · [Calculations](data/calculations.json) · [Audit](data/audit.json)

As of 2026-10-11. USD ordinary common stock; fiscal year ends June 30.
Research stance: **watchlist; business attractive, present price offers little modeled cushion**.
This is conditional equity research, not an order, portfolio allocation or investment approval.

## Grounding

### Security, dates and information quality
Microsoft sells ordinary common stock on Nasdaq, ticker MSFT, in USD; this is not an ADR or a multi-class aggregation.
Regular-session closing quote is **$535.07 at 2026-10-09 16:00 EDT**, timezone timestamp `2026-10-09T16:00:00-04:00` [sa-quote].
The separately displayed $535.00 after-hours quote at 19:59 EDT is not the valuation price [sa-quote].
Latest complete fiscal year is **FY2026 ended 2026-06-30**; all required income/cash-flow facts below use that same annual period.
SEC's reader returned a company filing chronology listing the July 29, 2026 FY2026 10-K, not its contents; the April 29 10-Q was the latest quarterly filing listed [sec-filings].
The issuer FY26 Q4 release and full transcript were actually fetched; its detailed release tables are labeled unaudited, not represented here as an independently inspected audit opinion [msft-fy26].
Information richness is A: exceptional issuer coverage and abundant forecasts, but abundant commentary is not independent evidence of incremental AI returns.

### Canonical facts and reconciliation
| Fact | Value | Period / basis | Retained source IDs |
|---|---:|---|---|
| Price | $535.07 | Oct 9 regular close | [sa-quote], dated search excerpt [fc-close] |
| Shares | 7,427,000,000 | June 30 actual common outstanding; rounded millions | [msft-fy26], [sa-balance] |
| Market capitalization | $3,970,000,000,000 | Oct 9 vendor rounded snapshot; independent $3.974T/$3.98T | [sa-cap], [fh-cap], [public-cap] |
| Revenue | $331,839,000,000 | FY2026 consolidated | [msft-fy26], [sa-fin] |
| GAAP net income | $133,749,000,000 | FY2026 consolidated | [msft-fy26], [sa-fin] |
| Operating cash flow | $182,935,000,000 | FY2026 consolidated | [msft-fy26], [sa-fin] |
| Cash capital expenditure | $115,948,000,000 | FY2026 positive cash PP&E additions | [msft-fy26], [sa-fin] |
| Cash and equivalents | $20,935,000,000 | June 30; excludes investments | [msft-fy26], [sa-balance] |
| Bond/interest-bearing debt aggregation | $40,294,000,000 | June 30 estimate, excludes all leases | [msft-fy26], [sa-balance] |
| GAAP diluted EPS | $17.95 | FY2026; not adjusted or forward | [msft-fy26], [sa-fin] |

The actual balance-date 7.427 billion shares are not the FY2026 diluted weighted-average EPS denominator of 7.453 billion [msft-fy26].
They are not claimed to be the exact October 9 outstanding count; the vendor's 7.426 billion filing-date count is another snapshot [sa-balance].
No stock-split conversion was needed for the observed price/EPS basis; source figures are retained in their observed units.
Engine-implied capitalization from price and June shares is $3,973,964,890,000; relative deviation from reported cap is `0.0009987128463476070528967254408060453400504` [data/calculations.json].
That passes the 1% numeric tolerance but does not prove quote-date shares or independent cap verification.
CompaniesMarketCap displays $3.973 trillion and $535.07, but labels its end-of-day cap section October 10 and does not supply a quote clock [cmc-cap].
October 10 was a non-session publication date; numerical agreement is useful, but it is not silently converted into an observed October 9 timestamp.
The price has a second dated FinanceCharts search observation [fc-close], whose full page returned403. Recovered actual FinHacker $3.974T (Oct9,4PM ET) and Public $3.98T (Oct9) page reads independently corroborate rounded capitalization within1%; they do not verify exact October shares [fh-cap], [public-cap].

Cash excludes separately reported $55.908 billion short-term investments; neither cash nor investments are assumed unrestricted distributable owner cash [msft-fy26].
Debt aggregation uses directly observed $9.227 billion current plus $31.067 billion noncurrent bond debt and is explicitly kind `estimate`, not a reported all-in total.
Stock Analysis's $128.813 billion standardized total debt includes leases; $9.683 billion current and $78.836 billion noncurrent leases are separately visible [sa-balance].
These definitions are not competing observations of the same debt quantity; the larger total cannot corroborate the bond-only number.
Trading Economics' actually fetched metadata reports $40.29B debt for its June2026 fiscal quarter, numerically consistent with narrow debt, but omits lease scope and a full primary note [te-debt]. The issuer component normalization stays an estimate rather than being relabeled reported to obtain PASS.
Do not use the narrow debt fact to call Microsoft economically unlevered: infrastructure lease commitments matter.
Issuer IR and issuer SEC filings are one originating publisher; no duplicated issuer page is counted as independent corroboration.

## Business

### Why customers pay
Enterprises and individuals repeatedly pay Microsoft for productive, secure work and computing because their documents, identity, applications and operating processes already run on its stack; the alternative is a costly migration to rival or self-managed tools.
The attractive business is integrated enterprise workflow and infrastructure, not merely a temporary lead in a particular foundation model.

| FY2026 segment | Revenue / operating income | Revenue drivers and cost structure |
|---|---|---|
| Productivity and Business Processes | $139.996B / $83.879B | M365 subscriptions, premium security/Copilot tiers, LinkedIn and Dynamics; software distribution plus growing inference costs |
| Intelligent Cloud | $137.791B / $56.972B | Azure consumption and enterprise server offerings; datacenters, power, CPUs/GPUs, depreciation and support |
| More Personal Computing | $54.052B / $14.386B | Windows/device cycles, Xbox content and search advertising; weaker cyclical/consumer exposure |
All segment figures are fiscal-year reported values [msft-fy26]; Intelligent Cloud is not synonymous with Azure.
Customers range from SMB/frontline workers to major enterprises and governments across geographies; no precise geography mix or independently checked churn series was retained.
Subscription renewals and committed cloud consumption are recurring, but RPO is not cash or guaranteed realized margin.
On-premise recognition, advertising demand, hardware cycles and game releases are materially less smooth than a uniform subscription annuity.

### Five-year evidence, not extrapolated history
| Fiscal year ended June 30 | Revenue B | GAAP net income B | OCF B | Cash capex B | Vendor gross / operating margin |
|---|---:|---:|---:|---:|---|
| 2022 | 198.270 | 72.738 | 89.035 | 23.886 | 68.40% / 42.05% |
| 2023 | 211.915 | 72.361 | 87.582 | 28.107 | 68.92% / 41.77% |
| 2024 | 245.122 | 88.136 | 118.548 | 44.477 | 69.76% / 44.64% |
| 2025 | 281.724 | 101.832 | 136.162 | 64.551 | 68.82% / 45.62% |
| 2026 | 331.839 | 133.749 | 182.935 | 115.948 | 67.94% / 46.78% |
This historical series and margins were observed directly on Stock Analysis, not independently recomputed or fully cross-observed year by year [sa-fin].
The margin percentages are publisher observations, not native-engine verified ratios.
Growth and expense discipline have lifted operating margins even as AI mix and infrastructure depress gross margins.
Cash capex has accelerated sharply; vendor FY2024/FY2025/FY2026 FCF observations are $74.071B/$71.611B/$66.987B [sa-fin].
Higher accounting income therefore does not automatically produce higher distributable cash.

### Latest quarter and monetization
FY26 Q4 revenue was $90.007B, up 18%; Azure and other cloud services grew 43%, versus 40% in Q3 in CNBC's observation [msft-fy26], [cnbc-q4].
Azure fiscal-year revenue exceeded $100B, up 41%; it is an annual issuer statement, not a separately modeled quarterly dollar series [msft-call].
M365 Commercial cloud grew 14% reported and 16% after normalizing prior-year recognition; paid commercial seats grew 6% [msft-call].
Premium tiers, Copilot and E7 drove ARPU; over 30 million paid Copilot seats compare with over 20 million in April [msft-call], [cnbc-q4].
Paid licenses are more meaningful than free users, but do not reveal net realized ARPU, renewal retention or gross profit per inference-heavy seat.
Seats-plus-consumption billing can capture increased use and protect margins; it can also expose customers to budget surprises and incentivize usage restraint.
Issuer claims on usage intensity and model efficiency are promotional/operational evidence, not independently measured customer ROI.
FY27 Q1 guidance of roughly 45% constant-currency Azure growth is a forecast, not an observed result [msft-call].
Xbox content/services fell 10% and Windows OEM/devices fell 7% in Q4; consolidated AI strength should not hide weaker consumer units [msft-fy26].

### Accounting versus economics
FY2026 GAAP EPS $17.95 includes $0.67 from OpenAI investment gains; issuer-adjusted EPS is $17.28 [msft-fy26].
Q4 adjusted EPS $4.74 still sits alongside a disclosed $0.27 benefit from discrete items including an Anthropic gain; removing OpenAI alone does not make earnings entirely recurring.
OCF adds back $12.405B SBC and $38.534B depreciation/amortization/other; deferred-tax adjustments and working capital are material [msft-fy26].
Maintenance versus growth capex and workload-level incremental ROIC are unavailable; treating every infrastructure dollar as discretionary growth would overstate owner earnings.
Circle of competence: enterprise adoption economics are understandable; future model cost curves, power availability and short-lived chip residual values are not confidently forecastable.

## Moat

| Candidate advantage | Evidence | Counterevidence / competitor response | Falsifying indicator |
|---|---|---|---|
| Enterprise switching costs | Existing identity, permissions, workflow context and governance integrated into Copilot/Agent365 [msft-call] | Google, independent AI apps and open standards can sit above existing data; actual churn not disclosed | Large renewals reduce premium seats or migrate core workflows |
| Distribution and pricing power | Commercial seats +6%, cloud revenue +14% reported; Copilot/E5/E7 ARPU support [msft-call] | Bundling/recognition effects are not pure price increases; inference costs rise with use | Premium ARPU uplift fails while adoption/discounting increases |
| Cloud scale and scope | Azure >$100B; demand exceeds capacity and new capacity monetized in quarter [msft-call] | AWS/Google have comparable capital access; Nvidia/power suppliers can capture scarcity rents | Capacity comes online without consumption growth or cash-margin recovery |
| Developer/data ecosystem | GitHub, Fabric, identity and model catalog support connected workloads [msft-call] | User counts do not prove paid economics; multi-model portability may reduce lock-in | Customers keep workflows but route most profitable inference elsewhere |
| OpenAI technology access | Licensed IP through 2032 [msft-openai] | License is now non-exclusive; OpenAI may serve all clouds | AI product parity eliminates premium pricing before infrastructure pays back |

[INFERENCE] Enterprise switching costs plausibly persist ten years because replacing operational controls is harder than changing a model endpoint.
[INFERENCE] The five-year moat has widened in integration/distribution, while cash economics have become more capital-intensive and less obviously protected.
Technology leadership alone is a weaker moat than trust, workflow context and administration; a well-funded competitor can replicate a model feature faster than a customer's installed operating processes.
Microsoft, customers and chip/power suppliers share productivity gains; the shareholder share is not established by token volume.
Durability confidence is medium-high for enterprise relevance, medium for premium AI profitability; no independently retained cohort retention evidence supports a stronger claim.

## Management

| Decision | Rationale / observed result | Stewardship judgment |
|---|---|---|
| Azure/AI capacity expansion | Q4 headline capex $41B, cash PP&E $35.8B, finance leases $5.6B; demand quickly monetizes added capacity [msft-call] | Strong execution evidence; lifetime returns remain unmeasured |
| Broaden models and renegotiate OpenAI | Non-exclusive license, no Microsoft-to-OpenAI revenue share, primary cloud position with broader OpenAI distribution [msft-openai] | Reduces dependence on one model but concedes exclusivity |
| Buybacks and distributions | FY2026 cash-flow repurchases $22.271B and dividends $26.445B; SBC $12.405B [msft-fy26] | Capital allocation must be judged net of dilution and infrastructure obligations |
| Xbox reset / cost discipline | Impairment/severance disclosed; headcount down 2%; weakening consumer results [msft-call] | Recognizes failures rather than presenting every unit as AI success |
| Building useful-life change | Datacenters/offices 15 to 25 years from FY27; lease classification changes [msft-call] | Monitor transparency and economic commitments, not a superficial capex decline |

Common shares fell from 7.434B to 7.427B across June balance dates despite substantial cash repurchases [msft-fy26], [sa-balance].
That modest actual-share reduction is more relevant than gross repurchase dollars; SBC remains an economic cost even though added back in OCF.
Cash-flow repurchases/dividends are not automatically the same definition as the call's shareholder-return headline; settlement/tax-withholding/declared-versus-paid differences were not independently reconciled.
Q4 $41B headline capex and $35.8B cash plus $5.6B leases are rounded and not perfectly additive; no false precision or invented adjustment is used.
FY27 accounting changes can shift future leases from finance to operating classification without reducing physical investment; the approximately $175B calendar-2026 capex expectation must be read on that basis [msft-call].
Candor positives: explicit GAAP/adjusted reconciliation, capacity constraints, weak Xbox and lease-accounting disclosure.
Candor limit: management's efficiency claims and “fungible” infrastructure claim lack independently observed workload ROIC.
Nadella/Hood provide demonstrated execution but not proof of superior future returns; no current full proxy, compensation weights, related-party review or succession plan was successfully retained.
Ownership alignment and precise incentive quality therefore remain unverified; ordinary shares are not assumed to imply meaningful insider economic ownership.
[INFERENCE] Enterprise sales/product architecture should outlast a CEO, but partner negotiations and capital pacing remain key-person-sensitive.

## Inversion

The strongest bear case is not “Azure stops growing”: revenue can keep rising while replacement chips, depreciation, power and leases consume more of the shareholder surplus.
A useful analogy is a network/infrastructure buildout that monetizes traffic without rewarding all investors; unlike a single-purpose entrant, Microsoft has profitable software distribution and diversified workloads.
The analogy is a warning about returns, not a historical prediction.

| Failure mechanism | Timing / severity | Observable warning | Mitigation / model treatment |
|---|---|---|---|
| AI infrastructure outgrows monetization | FY27-31; sustained cash impairment | Lease-inclusive commitments rise, FCF weakens despite capacity relief | Slow short-lived equipment deployment; bear EPS growth 3% and 20x exit |
| Paid Copilot seats do not renew profitably | Next renewal cycles; premium tier economics disappoint | Seat growth decelerates, discounts rise, paid usage fails to support margins | Integrated governance/consumption pricing; base assumes moderate recurring conversion |
| OpenAI concentration and counterpart economics | Multi-year; commitments may not become cash | RPO ex-OpenAI weakens or major model-company collections deteriorate | Broader models/customer mix; lower bear multiple; catastrophic counterparty tails unmodeled |
| Competitive pricing / supplier scarcity rent | Current to five years; margin pressure | Cloud gross margin deteriorates after utilization improves | Custom silicon/efficiency, but no independently proven ROIC advantage |
| Lease classification masks capital burden | FY27 onward; mistaken valuation confidence | Reported capex falls while operating lease obligations/payments grow | Compare physical additions and all lease obligations, not cash capex alone |
| Security failure / regulation | Discrete; potentially severe trust damage | Repeated systemic incidents or adverse distribution remedies | Governance improvements; not concealed in a discount-rate increment |

RPO grew 84% overall but 25% excluding OpenAI; quarterly additions were outside frontier model companies [msft-call].
Nearly 90% of FY2026 cloud revenue was outside frontier model companies, which mitigates revenue concentration but does not settle backlog or receivable risk [msft-call].
CNBC's approximately 45% OpenAI share of January RPO is dated January, not a June concentration estimate [cnbc-q4].
The April amendment means OpenAI can now serve every product across any cloud; older exclusive-cloud narratives are obsolete [msft-openai].
Bias guardrails: do not anchor to the consensus $587.63 target, extrapolate the latest 43% Azure growth, or treat paid-seat publicity as net cash-margin evidence [sa-forecast].
Scenario probabilities are judgment, not observed frequencies; security disasters, geopolitical shutdowns and extreme counterparty failure can exceed the bear case.

## Industry

### Value chain and enduring demand
[INFERENCE] Secure computing, enterprise coordination and process automation are enduring productivity needs; a specific chatbot interface is not necessarily an enduring institution.
Microsoft operates infrastructure, developer platforms, enterprise data/identity controls and first-party applications; chip vendors, utilities and frontier labs sit upstream, enterprise IT budgets downstream.
AWS and Google Cloud provide substitutes and bargaining leverage; CNBC places Azure annual scale below AWS and above Google Cloud [cnbc-q4].
No current sector TAM, peer valuation table or precise market-share series was independently retained; numerical TAM claims are omitted rather than promoted company opportunity treated as fact.
Customer constraints include trustworthy outputs, organizational implementation, permissions, sovereignty, data quality and budget discipline—not simply a lack of model capability.
Supplier constraints include advanced chips, power, site commissioning and interconnect; current excess demand is not proof of permanent scarcity rents for Microsoft.

Capacity constraints are real management-reported near-term conditions: GPU dock-to-live times improved, 88 datacenters were added during FY2026, and another gigawatt was added in Q4 [msft-call].
[INFERENCE] Once supply catches up, utilization and competition rather than installed capacity alone determine returns.
Useful-life and lease-classification changes complicate industry comparisons: reported capex excludes operating leases while economic obligations do not disappear.
Model choice and own silicon can lower delivered cost; neither guarantees retained pricing power when rivals also improve efficiency.
The 3%/11%/17% EPS scenario growth range below intentionally normalizes well below latest Azure growth because the stock represents the whole company and infrastructure costs must be paid.

## Valuation

### Native arithmetic and accounting basis
`data/calculations.json` was generated by the requested native `research.py calculate` CLI; no handwritten calculation file or unsupported ratio is presented as engine verified.
Engine historical FCF is **$66.987B**, FY2026 OCF less same-period cash PP&E; historical FCF/current-cap yield is **1.6873%** (rounded).
Engine GAAP trailing PE is **29.81x** (rounded); exact metric values remain in `data/calculations.json`.
FCF excludes noncash finance lease additions and does not deduct SBC as an owner cost; it is not owner earnings or a fully lease-adjusted distributable amount.
No FY2026 annual OCF was subtracted from quarterly or calendar-2026 capex.

The valuation starts with **$19.77 FY2027 adjusted analyst EPS**, explicitly an estimate observed October 11, not GAAP EPS or issuer guidance [sa-forecast].
The vendor compares it with adjusted FY2026 $17.28; its EPS and forward PE are labeled non-GAAP adjusted.
Individual estimate-refresh dates and future GAAP adjustments are unavailable; the forecast can be wrong or differently normalized.
The observed Treasury 10-year par yield was **5.24% on 2026-10-09**, near the Treasury's 15:30 indicative bid-side observation [treasury-20261009].
Required return is an explicit **10.5% nominal USD assumption**, above that reference for equity duration and execution risk; discrete catastrophic risks remain outside the model.

### Five-year conditional earnings-multiple model
| Case | Probability | EPS CAGR assumption / exit PE | Conditional terminal price | Discounted present target at 10.5% | Price-only CAGR (%) |
|---|---:|---|---:|---:|---:|
| Bear | 30% | 3% / 20x | $458.38 | $278.23 | -3.0467% |
| Base | 50% | 11% / 28x | $932.78 | $566.20 | 11.7568% |
| Bull | 20% | 17% / 34x | $1,473.72 | $894.55 | 22.4619% |
Dollar displays round saved native outputs to cents; price CAGR converts saved `annualized_return` fractions to percent and rounds to four decimals. It is `(terminal price / $535.07)^(1/5) − 1`, not historical YoY growth, assumed EPS CAGR or annual stock-price forecasts.
Engine probability-weighted present target: **$545.48** (rounded).
At $535.07, that conditional model offers little cushion; it is not a validated intrinsic value.

Bear: demand persists but premium AI pricing stalls, supplier/lease costs absorb growth and mature infrastructure-heavy earnings merit 20x.
Base: Azure expands with improving utilization, M365 upselling continues, and EPS grows 11% after capital/depreciation burdens; 28x recognizes durable recurring software without indefinitely preserving a scarcity premium.
Bull: profitable Copilot consumption, widespread enterprise adoption and infrastructure efficiencies compound EPS 17%; 34x requires retained premium growth and pricing rather than mere compute expansion.
Probabilities 30%/50%/20% sum to one and are intentionally asymmetric because cash payback is less established than headline adoption.
A move from base to bear economics substantially changes present value; choosing the bull multiple because Microsoft's products are excellent would confuse business quality with price.
The model configures **five EPS compounding steps** from FY2027 EPS (year ending June30,2027); literal annual increments yield an FY2032 earnings proxy. It separately assumes a **five-year holding/discount period** for the price comparison, not a verified exact target date.
That future earnings proxy might be used under an explicit exit forward-PE convention, or the anchor might be normalized as initial earning capacity; neither alignment is established by the saved inputs. The existing discounting approximation is therefore unverified, not a calendar-exact FY2032 projection.
No DCF, perpetual-growth formula, peer-derived proof or unsupported reverse valuation is claimed.
Returns exclude dividends, interim cash flows, taxes and fees; future dilution must be reflected in scenario EPS, with no separate share-count trajectory modeled.

## Decision

**Watchlist, conditional and provisional.** Microsoft meets the understandable-business test, but today's price does not provide a comfortable modeled margin against infrastructure/counterparty uncertainty.
The approximately $545.48 weighted present result is a research sensitivity output, not a validated target or a definitive allocation recommendation.

| Lens | Conclusion / confidence | Disconfirming evidence |
|---|---|---|
| Right business | Integrated enterprise workflow/cloud; high | Renewals migrate away despite installed controls |
| Durability | Switching costs and distribution; medium-high | Competitive substitutes remove premium pricing |
| Stewardship | Capex execution/candor positives; medium | Obligations outgrow cash returns or proxy incentives reward only expansion |
| Inversion | Capital intensity is the central risk; high confidence in risk, low certainty on outcome | Lease-adjusted economics improve sustainably, weakening the bear case |
| Structural opportunity | Enterprise AI can raise productivity; medium | Adoption grows without measurable customer/payback economics |
| Price | Minimal modeled cushion; medium-low | Independently proven cash returns support stronger normalized earnings |

Review October 28 earnings, the next vendor-listed earnings date, for actual FY27Q1 results rather than treating guidance as achieved [sa-quote].
Demand independent customer renewal/ROI evidence; paid-seat counts alone are inadequate.
Track Azure acceleration versus capacity additions, cloud margins after utilization improves, Copilot net realized ARPU, and RPO/collections excluding OpenAI.
Obtain full FY2026 lease note and FY2027 operating-lease commitments before claiming incremental infrastructure returns or genuine capex moderation.
Obtain current proxy incentive weights/ownership/succession disclosures before a stronger stewardship judgment.
Thesis breaks if enterprise relevance erodes, recurring premium revenues fail to cover inference/replacement economics, or material trust/governance failures persist.
If markets closed for five years, durable operating workflows and recurring enterprise demand—not a consensus target—would support interest in the business; infrastructure financing risk would still require monitoring.
AI research confidence is high in retrieved statement values and moderate in interpretation; investment certainty is lower because economic rent allocation and future capital returns are unresolved.

## Limitations and audit

All nine graph nodes were executed in dependency order with their instruction references; the four canonical artifacts are local to this ticker directory.
Source evidence stores excerpts, periods, original units and IDs; a citation is an observed document/snippet, not a claim of independent on-site diligence.
Price is corroborated by a dated FinanceCharts search-result excerpt [fc-close], not a fetched full page. Capitalization now has strictly date-matched FinHacker and Public observations; CMC's date limitation is retained [fh-cap], [public-cap], [cmc-cap].
Debt is a stated component-aggregation estimate excluding leases, not a falsely corroborated reported total; all ten required keys remain present.
Five-year data and margins rely on one secondary publisher beyond the cross-observed latest annual fundamentals; no retention, exact geography or workload-ROIC series was independently retained.
Yahoo and Fiscal.ai direct reads returned HTTP429; the issuer filing mirror returned HTTP403; SEC's filing reader returned submissions metadata rather than full10-K text.
The annual-reports hub exposed FY2025 links despite the observed FY2026 release/filing chronology; it was not substituted for current financials.
A compensation search identified a dated performance-award filing, but its direct page also returned403; no precise compensation or alignment claim is based on that inaccessible page.
Issuer and SEC are the same originating publisher; secondary standardization can share underlying data inputs and is not an independent audit of issuer truth.
Current quote is dated October9; balance-sheet/share facts June30; annual cash flow is historical, not a current annualized run rate.
Adjusted forecast EPS, growth, exit multiples, probabilities and required return are model inputs; no independent verification or economic certainty is implied.
Date/return audit limitation: numerical consistency does not validate the fiscal/holding-period alignment. The small modeled cushion depends on this unresolved timing in addition to the adjusted-EPS bridge and reinvestment assumptions; see the [batch return audit](../../../batches/2026-10-11/return-audit.md).
Finance-lease additions, operating lease reclassification, replacement capex, SBC, interim distributions and unmodeled tails prevent interpreting calculated FCF/targets as owner earnings or full total-return IRRs.
The pre-date/return-review native audit was **PROVISIONAL** because required debt was a component-normalization estimate rather than verified directly reported data; the market-cap publisher gap is resolved. Consult `data/audit.json` for saved machine findings. The complete five-ticker source investigation is in [corroboration review](../../../batches/2026-10-11/corroboration-review.md).
That earlier audit found no implemented blocking structural or arithmetic findings, but did not validate FY2027/FY2032/holding-period alignment. Offline contract/citation/arithmetic consistency is not independent source verification or investment approval.

### Retained source links
- [msft-fy26](https://www.microsoft.com/en-us/Investor/earnings/FY-2026-Q4/press-release-webcast): issuer release, statements, segments and GAAP reconciliation.
- [msft-call](https://www.microsoft.com/en-us/investor/events/fy-2026/earnings-fy-2026-q4): issuer operational commentary, capex/leases and guidance.
- [sa-quote](https://stockanalysis.com/stocks/msft/): dated regular and after-hours prices.
- [sa-cap](https://stockanalysis.com/stocks/msft/market-cap/): dated rounded capitalization.
- [cmc-cap](https://companiesmarketcap.com/microsoft/marketcap/): numerical secondary cap/quote agreement with date limitations.
- [sa-fin](https://stockanalysis.com/stocks/msft/financials/): annual financial series and margins.
- [sa-balance](https://stockanalysis.com/stocks/msft/financials/balance-sheet/): outstanding shares, cash, debt and lease standardization.
- [sa-forecast](https://stockanalysis.com/stocks/msft/forecast/): adjusted forecast EPS and consensus context.
- [cnbc-q4](https://www.cnbc.com/2026/07/29/microsoft-msft-q4-earnings-report-2026.html): secondary quarter/capacity/Copilot interpretation.
- [msft-openai](https://blogs.microsoft.com/blog/2026/04/27/the-next-phase-of-the-microsoft-openai-partnership/): April partnership amendment; supersedes exclusivity assumptions.
- [sec-filings](https://www.sec.gov/Archives/edgar/data/0000789019/000119312526323660/msft-20260630.htm): observed filing chronology only; full document not returned.
- [treasury-20261009](https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_yield_curve&field_tdr_date_value_month=202610): retained shared primary Treasury observation.
- [fc-close](https://www.financecharts.com/stocks/MSFT): independently observed dated closing-price search excerpt; direct full-page fetch returned403.
- [fh-cap](https://www.finhacker.cz/en/stocks/microsoft-market-cap/): actual dated capitalization page read recovered from source history.
- [public-cap](https://public.com/stocks/msft/market-cap): actual dated rounded capitalization, trend commentary excluded.
- [te-debt](https://tradingeconomics.com/msft:us:debt): fetched metadata's rounded narrow-debt observation; lease definition not disclosed.
