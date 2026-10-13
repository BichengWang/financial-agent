# Amazon (NASDAQ: AMZN) — evidence-first research scan

[Research index](../../../index.md#2026-10-11) · [Run guidance](../../../README.md) · [Evidence](data/evidence.json) · [Calculations](data/calculations.json) · [Audit](data/audit.json)

Research date: **2026-10-11**. Currency: USD. Research stance: **watchlist; attractive business, insufficient demonstrated price cushion**.
Quote: **$262.43, regular-session close 2026-10-09 16:00 EDT (UTC−04:00)**. [sa-quote] [gf-quote]
Conditional probability-weighted present target: **$271.67**; this is a provisional model output, not a validated fair value or execution instruction.

## Grounding

### Security, evidence and periods
Amazon common stock trades on Nasdaq in USD; this is not an ADR or an unmatched dual-class calculation.
The issuer reports common shares and no preferred shares outstanding; the actual common count below excludes unvested awards. [amzn-q2]
Information richness is **A**: extensive filings, segment reporting, financial aggregators and analyst coverage.
Coverage richness is not economic certainty: consensus is strongly favorable, and forecast EPS embeds adjustments that are not bridged here. [sa-forecast]
AI limitations include extraction errors, aggregation conventions, stale balance sheets and inability to establish contract profitability or customer retention from releases.
The most recent issuer financial results retrieved are for the June quarter; the October 29 earnings date on the quote page is only estimated. [amzn-q2] [sa-quote]
The canonical flow facts use **TTM ended June 30, 2026**, not an invented September result or mismatched annual cash-flow periods.
Balance-sheet and actual share-count facts are **June 30, 2026**, not current October balances.
Historical complete years below end **December 31** of the stated year; five-year trend context is separately labeled.

| Canonical fact | Value | Period and definition | Observed publishers |
| --- | ---: | --- | --- |
| Price | $262.43 | Oct 9 regular close, current quoted share basis | Stock Analysis; GuruFocus |
| Shares | 10,783,000,000 | June 30 actual common outstanding, not diluted weighted average | Amazon; Stock Analysis |
| Market cap | $2,830,000,000,000 | Oct 9 rounded reported capitalization | Stock Analysis; FinHacker |
| Revenue | $775,680,000,000 | Consolidated TTM | Amazon; Stock Analysis |
| Net income | $135,281,000,000 | Consolidated GAAP TTM, investment marks included | Amazon; Stock Analysis |
| Operating cash flow | $161,403,000,000 | Consolidated TTM | Amazon; Stock Analysis |
| Capital expenditure | $173,028,000,000 | Positive gross cash PP&E purchases, same TTM | Amazon; Stock Analysis |
| Cash | $78,213,000,000 | June 30 cash and equivalents only | Amazon; Stock Analysis |
| Debt | $251,635,000,000 | June 30 standardized vendor debt including leases | Stock Analysis only; primary bridge unresolved |
| EPS | $12.44 | GAAP diluted TTM, not normalized | Amazon; Stock Analysis |

Table provenance: [amzn-q2] [sa-fin] [sa-bs] [sa-cap] [fh-cap] [sa-quote] [gf-quote].
Source financial tables expressed in millions are explicitly converted into dollars/shares in data/evidence.json.
Issuer IR and SEC are the same underlying issuer for financial corroboration; they do not constitute independent publishers.
FinHacker observes the same rounded cap through EDGAR/Bloomberg/Yahoo aggregation, not a new primary measurement. [fh-cap]
June shares are independently corroborated; exact October shares are not. The quote page's rounded 10.79B is not substituted into the actual historical count.
Native implied cap is $2,829,782,690,000.00; relative deviation from reported cap is **0.00007678798586572438162544169611307420494700**, below the 1% policy tolerance.
This arithmetic consistency does not prove a perfectly time-aligned capitalization census.

### Cash, capex and debt conventions
Cash excludes **$44.775B marketable securities** and the vendor's **$283M restricted cash**; consolidated cash is not asserted to be freely distributable. [amzn-q2] [sa-bs]
Gross-spend native FCF is **−$11.625B**, whereas issuer net-spend FCF is **−$7.604B**. Both use the same TTM OCF. [amzn-q2] [sa-fin]
The difference is the issuer's **$4.021B PP&E sales/incentive proceeds**; the native engine uses gross cash purchases, without that offset.
Neither measure deducts all acquisitions or all financing outlays; neither is automatically distributable owner earnings.
TTM finance-lease principal payments were **$1.599B**, financing-obligation principal **$308M**, and finance-lease asset additions **$4.048B**. [amzn-q2]
Operating-lease asset additions were **$24.897B** and the increase in PP&E acquired but not yet paid was **$29.267B**; those are not gross cash capex. [amzn-q2]
Operating-lease cash costs already affect OCF; simply deducting all lease payments again would double-count some costs.
Vendor total debt includes lease/current/noncurrent classifications; its $137.794B standardized long-term debt differs from the issuer's narrower $128.894B line. [sa-bs] [amzn-q2]
No incompatible primary value is falsely entered as corroboration; the exact bridge remains a material evidence gap and no net-debt ratio is claimed.
Alternative Trefis read displays $223.2B debt in a Now10/11/26 valuation table, without a compatible June30 balance period/definition [trefis-debt]. WallStSmart's updated page mixes a $223.23B header and older visible long-term-debt history; Finbox/Yahoo failed. A search-linked FastEDGAR debt note belonged to Jazz Pharmaceuticals, not Amazon, and was rejected. Concrete source findings and remaining $8.900B classification bridge are retained in [corroboration review](../../../batches/2026-10-11/corroboration-review.md); none is fabricated corroboration.

## Business

### Who pays and why
Consumers pay for selection, convenience and rapid delivery; sellers pay to access demand and fulfillment; advertisers buy purchase-intent reach; enterprises pay AWS for compute, storage and managed services.
They return when convenience, conversion or operational reliability exceeds the alternative; Walmart/direct shopping, competing ad platforms and Azure/Google Cloud remain real alternatives.
Duan's right-business lens supports Amazon's recurring utility, not the proposition that every Amazon initiative earns attractive returns.

| Engine | Latest observed economics | Revenue/cost mechanism |
| --- | --- | --- |
| North America | Q2 sales $116.177B; operating income $9.123B; reported margin 7.9% | Retail, seller services, advertising and subscriptions; logistics density matters |
| International | Q2 sales $42.197B; operating income $1.717B; margin 4.1% | Similar mix, with local competition, FX and expansion costs |
| AWS | Q2 sales $42.232B; operating income $16.621B; margin 39.4% | Usage/contracts; hardware, power, depreciation and engineering are major costs |
| Advertising | Q2 revenue $19.809B, growth 26% | Sponsored/display/video demand; not separately reported operating profit |
| Third-party services | Q2 revenue $46.780B, growth 16% | Commissions and fulfillment/shipping fees, not the full merchant sale |
| Subscriptions | Q2 revenue $13.730B, growth 12% | Prime and digital subscriptions, with content and service costs |

All table values are issuer-reported Q2 ended June 30, 2026. [amzn-q2]
AWS, ads and marketplace mix can make consolidated revenue quality improve without identical retail unit economics.
Advertising is embedded across geographic segment results; adding a speculative ad profit to segment earnings would double-count.
Issuer claims AI and chips each exceed $25B annual revenue run rates; these are overlapping views of AWS, not additive segments or guaranteed annual sales. [amzn-q2]

### Five-year history and current trend
| FY ended Dec 31 | Revenue $B | GAAP net income $B | Vendor gross margin | Vendor operating margin | OCF $B | Gross cash capex $B |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 2021 | 469.822 | 33.364 | 42.03% | 5.29% | 46.327 | 61.053 |
| 2022 | 513.983 | −2.722 | 43.80% | 2.60% | 46.752 | 63.645 |
| 2023 | 574.785 | 30.425 | 46.98% | 6.41% | 84.946 | 52.729 |
| 2024 | 637.959 | 59.248 | 48.85% | 10.75% | 115.877 | 82.999 |
| 2025 | 716.924 | 77.670 | 50.29% | 11.15% | 139.514 | 131.819 |

Historical series and margins are observed vendor data, not independently corroborated five-year calculations or native ratio outputs. [sa-fin]
The pattern is a post-overbuild recovery followed by a new investment wave; prior margin recovery cannot establish AI cash returns.
FY2021–2025 AWS revenues were $62.202B/$80.096B/$90.757B/$107.556B/$128.725B; advertising $31.160B/$37.739B/$46.906B/$56.214B/$68.635B. [sa-fin]
Latest AWS year-over-year quarterly growth progressed from 17% in Q1/Q2 2025 to 20%, 24%, 28% and **37% in Q2 2026**. [amzn-q2]
Q2 consolidated operating income was $27.461B; the **$62.647B GAAP net income** also contains **$53.415B pretax other income**, primarily Anthropic-related. [amzn-q2]
That mark is not retail/cloud operating profit, not recurring cash income, and not a researcher-derived normalized EPS adjustment.
Prime Day moved to June; Q2/Q3 growth comparisons must account for that event shift before declaring a new organic retail growth rate. [amzn-q2] [cnbc-q2]
Shipping cost growth of 19% exceeded paid-unit growth of 17% in Q2; speed gains therefore do not alone demonstrate falling cost per unit. [amzn-q2]
Circle of competence: platform monetization and consolidated accounting are understandable; frontier-model demand, GPU economics and individual megawatt contracts are not verified here.

## Moat

| Candidate advantage | Evidence | Counterevidence / competitor response | Durability and falsifier |
| --- | --- | --- | --- |
| Fulfillment density and Prime habit | Record speeds; over 40% more first-half same-day/overnight items; geographic profits positive [amzn-q2] | Faster delivery also consumes inventory/capital; Walmart can use local stores and customers can multi-home | Medium-high; persistent delivery slowdown and shrinking geographic profit despite volume growth falsify improvement |
| Marketplace selection and demand loop | Third-party unit mix 61%; seller services growing 16% [amzn-q2] | High fees can cause seller exit; FTC challenges fulfillment/discount practices [ftc-antitrust] | Medium-high but rule-dependent; falling seller participation and lower conversion undermine loop |
| AWS switching and service breadth | Large existing workloads, custom chips, managed model/agent services, accelerating revenue [amzn-q2] | Multi-cloud, open software and rival AI stacks lower lock-in; migration/churn not disclosed here | Medium-high for installed workloads, less proven for new AI; share losses with pricing concessions weaken claim |
| Purchase-intent advertising | Ads growth 26%, directly adjacent to shopping [amzn-q2] | Ad saturation degrades relevance; rivals have intent and merchant channels | Medium; declining advertiser conversion/renewal despite rising load would signal rent extraction |
| Custom silicon cost advantage | Trainium commitments and Graviton adoption are issuer claims [amzn-q2] | NVIDIA ecosystem and rapid hardware cycles; public price-performance claims are not audited customer TCO | Medium hypothesis; poor utilization or discounts without margin recovery refute it |

Scale is not itself a moat: benefits must survive competition and accrue to per-share economics rather than solely cheaper customer prices.
Five-year cloud/ads growth and recovered geographic profitability suggest broader capability, but no retained retention or independent market-share series proves moat widening. [sa-fin]
Ten-year persistence is plausible for logistics/service ecosystems; individual model and chip leads can turn over much faster.
Buffett's durability lens favors the customer habit and enterprise infrastructure over headline AI run rates.
The moat can be strong while shareholder returns remain mediocre if maintaining it requires increasingly expensive reinvestment.

## Management

### Capital allocation and stewardship
| Dated decision | Observed outcome / concern | Research judgment |
| --- | --- | --- |
| Continued infrastructure expansion after FY2022 weakness | Geographic profits recovered and AWS accelerated, but gross-spend cash generation weakened [sa-fin] [amzn-q2] | Operational recovery is evidence, not a blanket endorsement of the next cycle |
| 2026 AI capacity build | CNBC reports capex plan rose from $200B to $220B, chiefly memory inflation; AWS demand accelerating [cnbc-q2] | Demand may justify capacity, but rising input prices can transfer value to suppliers |
| Anthropic investment strategy | Q2 $53.415B pretax other income; deployment commitments intertwine investment and cloud demand [amzn-q2] | Marks should not validate operational allocation skill or recurring profits |
| Retaining capital rather than repurchasing | No H1 2025/2026 repurchases; $6.1B authorization remaining June 30 [sec-buybacks] | Reinvestment dominates; unused authorization is not an anti-dilution program |
| Prime enrollment practices | $2.5B 2025 settlement with revised redress order September 2026 [ftc-prime] | Concrete stewardship/candor concern; not dismissed because the dollar penalty is affordable |

TTM SBC of **$19.314B** is added back in OCF but remains an economic compensation cost; H1 SBC was $10.070B. [amzn-q2]
Actual common shares increased from 10.731B at year-end 2025 to 10.783B June 2026; declining quarterly SBC does not mean no dilution. [amzn-q2] [sa-bs]
No dividend is reported on the current quote page. R&D/engineering is intertwined with technology/infrastructure expense; it is not an independently disclosed economic-return series. [sa-quote] [amzn-q2]
The $39.767B H1 acquisitions/nonmarketable investments/other investing line is composite, not all acquisition purchase price; allocation economics cannot be inferred from the label. [amzn-q2]
CEO Andy Jassy's comments articulate demand and reinvestment; strong AWS outcomes support operational competence but capacity claims are still management claims. [amzn-q2] [cnbc-q2]
No complete proxy compensation, beneficial ownership, related-party or succession review was obtained; exact incentive alignment and governance confidence remain provisional.
Only a single common class is documented here; founder economic influence is not treated as a demonstrated dual-class voting structure.
Succession resilience likely rests on AWS and operations organizations [INFERENCE], but key-person dependence and executive incentives are not quantified.
Duan's right-people lens is mixed: demonstrated execution and customer utility coexist with a substantiated settlement and incomplete alignment evidence.

## Inversion

The strongest bear case is **not** that Amazon lacks demand: it is that extraordinary AI demand and noncash marks conceal a lower-return, capital-intensive earnings stream.
Merchant ads/fees and speed improvements can sustain accounting margins while funding hardware replacement, compensation and logistics consumes the distributable cash.
A low GAAP PE during an investment-mark windfall can anchor investors to the wrong denominator.

| Failure mechanism | Timing / severity | Early warning and falsifiable review trigger | Mitigation / valuation treatment |
| --- | --- | --- | --- |
| AI capacity earns sub-hurdle returns | Several-year depreciation/utilization cycle; high | Research trigger: two quarters AWS growth below 20% while capex remains elevated and cash conversion deteriorates | Stage capacity and improve silicon efficiency; bear EPS growth and lower exit multiple |
| Lab concentration/circular demand | Funding cycle; high | Investment commitments grow while counterparties' external cash funding or paid workload demand weakens | Contract/funding diligence; unmodeled counterparty tail, not assumed zero |
| Retail speed becomes uneconomic | Near-term quarters; medium-high | Geographic margins retreat despite unit growth; shipping inflation remains above units | Density/automation may offset; base growth only if profits and cash improve together |
| Marketplace/Prime remedies weaken monetization | Litigation-dependent; potentially structural | Binding restrictions on eligibility, ranking or fees; repeat enrollment/cancellation violations | Compliance/customer trust; bear de-rating, severe restructuring outside three cases |
| Ad overload damages the flywheel | Multi-year; medium-high | Worse search satisfaction and merchant conversion, falling seller participation | Protect relevance and seller economics; lower growth/multiple |
| Energy, memory or supply bottlenecks | Near-term through multi-year; high | Delayed capacity, rising hardware prices and higher debt funding | Supplier diversity/contract discipline; base assumes moderation, bull requires productive capacity |

Numerical review thresholds above are research assumptions, not issuer guidance or asserted probabilities.
Munger's inversion lens: capital spending justified by backlog can resemble past telecom buildouts; AWS's reusable services and existing customers differ, so analogy is not proof of a bust.
Unknown terminal regulation, major cybersecurity failure, lab insolvency and forced separation are unmodeled tails; the three cases are not an exhaustive loss distribution.
Bias controls: separate adjusted EPS from GAAP, compare net/gross capex, confront regulatory evidence, and do not adopt the Strong Buy consensus as a probability estimate.
The 25%/50%/25% case weights are subjective model assumptions, not statistical frequencies.

## Industry

Li Lu's evolution lens favors enduring needs for convenient commerce, scalable computing and automated workflows, rather than assuming every AI dollar is incremental economic surplus.
Amazon sits at several chokepoints: consumer demand aggregation, seller logistics, purchase-intent advertising and enterprise infrastructure.
Value can migrate upstream to memory/chip/power suppliers, downstream to customers through lower prices, or to software/model providers rather than accrue to AWS.
CNBC's $220B capex report specifically attributes the increase to memory costs; capacity shortages can coexist with lower investment returns. [cnbc-q2]
Retail rivals include Walmart, direct brands, specialist marketplaces and lower-price cross-border platforms; cloud rivals include Azure, Google and specialized infrastructure providers.
These are alternative channels, not retained quantitative market-share estimates; no numerical TAM or winner-take-all share claim is used.
CNBC reports strong Azure/Google Cloud growth, but differing scale, definitions and fiscal periods prevent direct market-share inference. [cnbc-q2]
AI/chip run rates overlap and backlog is contracted future work, not present revenue or separately verified cash profitability. [amzn-q2] [cnbc-q2]
The original FTC marketplace complaint attacks the very restrictions that may strengthen the flywheel; the 2026 Prime settlement update is separate consumer-protection evidence. [ftc-antitrust] [ftc-prime]
The latest marketplace trial schedule/remedy outlook, cross-border tariff economics and independent merchant/customer surveys are not verified.
Scenario boundaries: mature retail is not assigned perpetual hypergrowth; faster service mix can support double-digit EPS growth, while AI replacement capex and competition constrain the multiple.
If AWS growth rises but economic cash generation and utilization do not improve, the industry tailwind has not necessarily accrued to owners.

## Valuation

### Native calculations and earnings basis
data/calculations.json was produced by the repository-native **calculate** CLI from retained evidence; supported outputs below are not hand-built ratios.
| Metric | Native result | Interpretation |
| --- | ---: | --- |
| Implied market cap | $2,829,782,690,000.00 | Oct price × dated June actual shares; not exact current shares |
| Absolute relative cap deviation | 0.00007678798586572438162544169611307420494700 | Rounded cap reconciles within 1% policy |
| Historical gross-spend FCF | −$11,625,000,000 | TTM ending June 30, not FY or forward owner earnings |
| FCF / reported capitalization | −0.4108% | Historical negative gross-capex yield, rounded from saved native result |
| GAAP trailing PE | 21.10x | Rounded; depressed by investment marks, not a normalized valuation multiple |

Model anchor is **$8.31 FY2026 consensus adjusted forecast EPS**, observed October 11; forecast year ends December 31, 2026. [sa-forecast]
It is an **estimate**, not GAAP EPS, not the TTM $12.44, and not researcher-verified normalized owner earnings.
The vendor explicitly labels EPS non-GAAP adjusted; its full tax, investment-mark and SBC bridge is unavailable, so the target is less reliable than the arithmetic.
The model configures **five EPS compounding steps** from the FY2026 forecast and assumes a **five-year holding/discount period**. Five fiscal-year increments would suggest FY2031 earnings, but capitalizing that basis at a holding-period exit requires an unverified earnings-to-price alignment; the saved inputs establish neither an exact target date nor a validated current run rate.
Required return is an assumed **11% nominal USD**, above the observed **5.24% 10-year Treasury par yield on October 9, 2026**. [treasury-20261009]
The equity hurdle reflects opportunity cost and ordinary equity variability; discrete operating risks are expressed in scenarios and regulatory tails remain explicit.

| Scenario | EPS CAGR assumption | Exit PE assumption | Probability | Conditional terminal price | Price-only CAGR (%) | Discounted present target at 11% |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Bear | 2% | 18× | 25% | $165.15 | −8.8467% | $98.01 |
| Base | 13% | 28× | 50% | $428.70 | 10.3132% | $254.41 |
| Bull | 22% | 36× | 25% | $808.54 | 25.2385% | $479.83 |

Dollar displays round saved native outputs to cents; price CAGR displays multiply saved `annualized_return` fractions by 100 and round to four decimals. CAGR is `(terminal price / $262.43)^(1/5) − 1`, not historical YoY growth, assumed EPS CAGR or an annual stock-price forecast. Exact Decimal strings and cumulative price-only returns remain in `data/calculations.json`.
**Weighted present target: $271.67** (rounded).
Bear: AI returns disappoint, replacement spending remains high, retail competition persists and platform restrictions constrain rents; 18× rewards durable infrastructure without a growth premium.
Base: AWS/ads compound with moderated retail growth, density improves and dilution is absorbed; 13% per-share earnings growth slows materially from recent cloud/ads growth, and 28× reflects strong recurring utility with real reinvestment needs.
Bull: productive AI capacity/custom silicon and ad/retail efficiency support 22% per-share growth; 36× requires sustained premium growth and improving cash conversion, not simply more Anthropic marks.
Probabilities emphasize the operating base but retain symmetric downside/upside case weight; they are judgmental, not fitted to analyst targets.
The base annualized price return falls below the assumed hurdle; current price is close to the weighted present result rather than an obvious margin of safety.
Sensitivity is visibly large across terminal multiples/growth; a moderate deterioration from base toward bear overwhelms the small weighted-present cushion.
This is an **earnings-multiple conditional model, not a DCF**: it excludes dividends, interim distributable cash, separate enterprise/debt adjustments and unmodeled discrete events.
EPS growth assumptions must absorb dilution and recurring compensation economics; no explicit share-count forecast or separate SBC addback is modeled.
Segment mix, hardware depreciation policies and reinvestment make a single consolidated PE particularly incomplete; no sum-of-parts profit guesses are used.

## Decision

**Watchlist / further operating diligence, not a validated target or allocation recommendation.**
Business attractiveness is high: utility, demand aggregation and cloud capability are evidenced; price attractiveness is only moderate and model/evidence confidence is lower.
Buffett lens: customer/service durability is plausible; cloud cash economics after replacement investment remain the critical missing owner-earnings link.
Duan lens: right business largely supported; right people/alignment incomplete and Prime practices warrant scrutiny rather than assumed trust.
Munger lens: avoid mistaking a low mark-inflated PE and growing backlog for distributable returns.
Li Lu lens: productive computing and commerce can endure, but shareholder capture must be shown through utilization and cash economics.
Review the next filed earnings, separately adjusting Prime Day timing, AWS/ad growth, regional margins and gross versus net cash spending definitions.
Escalate diligence on AI contract funding, maintenance/replacement capex, merchant retention, compensation dilution and the full debt/lease bridge.
Thesis breaks if productive capacity fails to improve cash generation, geographic profit recovery reverses structurally, or platform remedies destroy the core seller/customer value exchange.
A substantially cheaper quote without worsening economics, or demonstrated durable cash conversion at current price, would improve the research case; no broker actions are authorized.
Research confidence: moderate in sourced accounting/operations, lower in normalized earnings, financing definitions and valuation; investment certainty remains inherently limited.

## Limitations and audit

The pre-date/return-review native audit was **PROVISIONAL** (exit1), with finding `fact debt: needs observations from two distinct publishers`. That earlier arithmetic/schema result did not validate the model's timing; consult `data/audit.json` for saved machine findings. Recomputation does not independently fetch facts or approve an investment.
Debt has only one directly matching publisher observation; vendor debt/lease scope cannot be fully bridged to the primary filing from fetched materials.
Required flows, cash, shares and EPS have issuer/vendor observations, while price and rounded cap have two observed publisher records; upstream vendor independence still requires judgment.
Quote is current for the latest completed US session, but cash/debt/shares are dated June 30; intervening financing and dilution are not fully incorporated.
Full 10-Q body retrieval returned an SEC company index; buyback evidence is the explicitly retained live search excerpt, not a claimed complete filing review.
Complete proxy, executive alignment, related parties, churn, merchant economics, independent chip TCO and AI contract profitability are not established.
Forecast EPS lacks a full GAAP/adjusted/SBC/tax reconciliation; historical GAAP marks are not relabeled normalized earnings.
Date/return audit limitation: arithmetic consistency does not validate the calendar horizon; price returns and discounted comparisons depend on the conditional five-year holding period and FY2026 earnings alignment. See the [batch return audit](../../../batches/2026-10-11/return-audit.md).
Five-year history is observed secondary context, not independently cross-verified for every year. Ratios in that history are vendor observations, not native computations.
No numerical TAM, regulatory outcome probability, exact October share census, maintenance-capex split or comprehensive DCF is fabricated.
The native graph, calculate and audit are the requested research tools; no tests/builds/linters, order routes or external output paths are used.

### Retained source register
- [amzn-q2] [Amazon Q2 2026 release and financial tables](https://s2.q4cdn.com/299287126/files/doc_earnings/2026/q2/earnings-result/AMZN-Q2-2026-Earnings-Release.pdf).
- [sa-quote] [Stock Analysis current AMZN quote](https://stockanalysis.com/stocks/amzn/).
- [gf-quote] [GuruFocus October 9 price observation](https://www.gurufocus.com/news/9117895/a-look-at-amazoncom-inc-amzn-after-33-gain-gf-value-25052-vs-price-26243); automated profitability wording is not adopted.
- [sa-fin] [Stock Analysis annual/TTM financials](https://stockanalysis.com/stocks/amzn/financials/).
- [sa-bs] [Stock Analysis standardized balance sheet](https://stockanalysis.com/stocks/amzn/financials/balance-sheet/).
- [sa-cap] [Stock Analysis dated capitalization](https://stockanalysis.com/stocks/amzn/market-cap/).
- [fh-cap] [FinHacker independently observed capitalization](https://www.finhacker.cz/en/stocks/amazon-market-cap/).
- [sa-forecast] [Stock Analysis adjusted consensus forecasts](https://stockanalysis.com/stocks/amzn/forecast/).
- [cnbc-q2] [CNBC Q2 earnings, capex and conference-call reporting](https://www.cnbc.com/2026/07/30/amazon-amzn-q2-earnings-report-2026.html).
- [sec-buybacks] [Amazon June 30 10-Q, retained search excerpt](https://www.sec.gov/Archives/edgar/data/1018724/000101872426000026/amzn-20260630.htm).
- [ftc-antitrust] [FTC original marketplace complaint allegations](https://search.ftc.gov/news-events/news/press-releases/2023/09/ftc-sues-amazon-illegally-maintaining-monopoly-power), not final findings.
- [ftc-prime] [FTC September 17, 2026 Prime redress update](https://search.ftc.gov/news-events/news/press-releases/2026/09/ftc-announces-additional-payments-consumers-stemming-ftcs-amazon-prime-settlement).
- [treasury-20261009] [Treasury October 2026 par-yield table](https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_yield_curve&field_tdr_date_value_month=202610), retained shared 10-year observation.
- [trefis-debt] [Actual Trefis debt display](https://www.trefis.com/data/companies/AMZN?from=AMZN-2026-06-02): $223.2B different snapshot/definition, not canonical corroboration.
