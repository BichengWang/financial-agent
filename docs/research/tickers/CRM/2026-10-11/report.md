# Salesforce (NYSE: CRM): Agentforce must expand the wallet, not merely replace seats

[Research index](../../../index.md#2026-10-11) · [Run guidance](../../../README.md) · [Evidence](data/evidence.json) · [Calculations](data/calculations.json) · [Audit](data/audit.json)

As of **2026-10-11**. USD common equity; research only, no brokerage or execution instructions.
**Research stance: watchlist; good installed-base economics, insufficient demonstrated valuation cushion.**
Regular-session reference: **$229.13, 2026-10-09 at 16:00 EDT**; not the $228.83 after-hours print. [sa-stats] [fiscal-quote]
The conditional model produces a probability-weighted present target of **$226.16** (rounded); this is not a validated intrinsic-value target, and the FY2028-to-exit timing assumption remains unverified.

## Grounding

### Security, calendar and information quality
Salesforce is the NYSE-listed common stock CRM, denominated in USD, without an ADR conversion or a dual-class voting structure. [crm-10k] [crm-proxy]
The observed quote publisher records the last split as four-for-one on April 18, 2013; quote and modern EPS are on the post-split basis. [sa-stats]
**FY2026 means February 1, 2025–January 31, 2026**, not calendar 2026. The latest completed quarter is **Q2 FY2027, ended July 31, 2026**. [crm-10k] [crm-q2]
Information richness is **A**, but customer deployment economics and separately reconciled Agentforce revenue are much less observable than headline metrics.
AI research confidence is moderate-to-high for annual statements and dated quote; moderate for source normalization; low-to-moderate for incremental AI unit economics.
Abundant issuer promotion, analyst consensus and vendor-standardized tables create anchoring and selection bias, not economic certainty.

### Canonical required facts
Values in this table are actual dollars/shares, not millions silently relabeled; all fact definitions and individual observations are retained in data/evidence.json.

| Fact | Canonical value | Actual period/basis | Observation trail |
|---|---:|---|---|
| Price | $229.13 | October 9 regular-session close | [sa-stats], independently observed [fiscal-quote] search excerpt |
| Shares | 823,000,000 | **Estimate:** approximate August 20 issuer cover count carried to October 9 model | [crm-q2-cover], [sa-stats], [sa-balance] |
| Market cap | $188,570,000,000 | October 9 close; rounded snapshot | [sa-stats], [cmc-cap] weekend carry-forward |
| Revenue | $41,525,000,000 | Consolidated FY2026 ended January 31, 2026 | [crm-10k], [scout-financials], [sa-history] |
| Net income | $7,457,000,000 | Consolidated annual GAAP, not adjusted | [crm-10k], [scout-financials], [sa-history] |
| Operating cash flow | $14,996,000,000 | FY2026, not current-quarter cash flow | [crm-10k], [scout-financials], [sa-history] |
| Capital expenditure | $594,000,000 | Positive cash spend, same FY2026 as OCF | [crm-10k], [scout-financials], [sa-history] |
| Cash/equivalents | $8,310,000,000 | July 31, 2026; excludes securities | [crm-q2-cover], [sa-balance], [scout-financials] |
| Debt | $14,439,000,000 | **Historical January 31, 2026 borrowings**, excluding leases | [crm-10k], [scout-financials] |
| Diluted EPS | $7.80 | FY2026 GAAP, not adjusted or forward | [crm-10k], [scout-financials], [sa-history] |

Current shares are not independently certified on October 9. The 823 million issuer cover figure is approximate and dated August 20; the ASR has an October final settlement. [crm-q2-cover] [crm-q2]
Do not replace outstanding common shares with 821 million Q2 diluted weighted-average shares, or the 956 million FY2026 EPS denominator. [scout-financials] [crm-10k]
CompaniesMarketCap explicitly labels its same $188.57 billion snapshot October 10, a Saturday; evidence normalizes its market-session basis to the unchanged Friday close, not a Saturday trade. [cmc-cap]
Fiscal.ai's dated close was actually observed through search; its direct page returned HTTP429. It is not represented as a fully fetched quote page. [fiscal-quote]
The primary July cover/cash excerpts were observed by targeted search; SEC document reads returned an issuer index, then raw HTTP403. [crm-q2-cover]

### Accounting reconciliation and liquidity
January debt is **not** the current balance: July noncurrent borrowings are **$39.288 billion**, with zero current borrowings in the detailed secondary statement. [crm-q2-cover] [scout-financials]
July cash/equivalents exclude **$3.093 billion** of marketable securities and the strategic investment portfolio; unrestricted immediate distributability has not been proven. [sa-balance]
Vendor standardized debt of **$42.376 billion** July and **$17.711 billion** January includes lease classifications; it cannot corroborate lease-excluded borrowings. [sa-balance]
No mixed-date net-cash or enterprise-value calculation is presented using July cash and January debt.
Stock Analysis' overview operating income of $8.917 billion differs from **primary GAAP $8.331 billion**; primary GAAP wins, and that standardized observation is not adopted. [sa-history] [crm-10k]
Its statistics summary labels $11.40 billion cash/equivalents, but the detailed table shows this includes investments; canonical cash is the detailed $8.310 billion. [sa-stats] [sa-balance]

## Business

### Why customers pay
Businesses pay Salesforce for maintained customer records, sales/service workflows, integration and governed automation; they renew because replacing embedded processes is disruptive, while alternatives include competing suites and internally assembled tools. [crm-10k]
That is a comprehensible recurring enterprise application business; the unresolved question is how much new AI value remains with Salesforce rather than customers or model suppliers.

| Revenue driver | FY2026 subscription revenue | Economics and interpretation |
|---|---:|---|
| Agentforce Sales | $9.028bn | Core seller workflow; reported 8% growth, not demonstrated seat growth |
| Agentforce Service | $9.818bn | Service cases and field workflows; 8% growth; most exposed to agent-driven human-seat substitution |
| Platform, Slack and Other | $8.882bn | 23% growth, including $388m Informatica subscription revenue; not pure Agentforce revenue |
| Marketing and Commerce | $5.428bn | 3% growth: mature execution and advertising-commerce exposure |
| Integration and Analytics | $6.232bn | 8% growth; term-license recognition makes quarterly revenue less smooth |
| Total subscription/support | $39.388bn | Distinct from $2.137bn professional services/other |

All offering values and growth rates are issuer FY2026 disclosures. Renaming clouds “Agentforce” in FY2026 did not itself change the revenue allocation. [crm-10k]
Geographic revenue was Americas $27.193bn, Europe $10.017bn and Asia Pacific $4.315bn; attributed by contracting entity, not necessarily customer location. [crm-10k]
No customer exceeded 10% of annual revenue. Detailed customer cohorts, supplier concentration and offering-level profit are not retained; cross-subsidization remains possible. [crm-10k]
Multi-tenant software and distribution support scale; selling, R&D, employee compensation, integration and cloud/inference capacity remain genuine costs. [crm-10k]
Low reported capex does not mean AI hosting is costless: external infrastructure spend can be an operating expense, and acquisitions are outside the simple FCF definition.

### Five-year trajectory, without inventing continuous detail
| Fiscal year ended January 31 | FY2022 | FY2023 | FY2024 | FY2025 | FY2026 |
|---|---:|---:|---:|---:|---:|
| Revenue, $bn | 26.492 | 31.352 | 34.857 | 37.895 | 41.525 |
| Gross profit, $bn | 19.466 | 22.992 | 26.316 | 29.252 | 32.255 |
| Net income, $bn | 1.444 | 0.208 | 4.136 | 6.197 | 7.457 |
| Diluted GAAP EPS, $ | 1.48 | 0.21 | 4.20 | 6.36 | 7.80 |
| OCF, $bn | 6.000 | 7.111 | 10.234 | 13.092 | 14.996 |
| Positive capex, $bn | 0.717 | 0.798 | 0.736 | 0.658 | 0.594 |

The complete five-year series is observed secondary history; primary FY2024–FY2026 statements corroborate the recent rows. [sa-history] [crm-10k]
Reported GAAP operating margins were **3.3%, 14.4%, 19.0%, 20.1%** for FY2023–FY2026; adjusted were **22.5%, 30.5%, 33.0%, 34.1%**. [crm-proxy]
A comparable FY2022 primary margin observation was not retained; it is not extrapolated from the standardized vendor operating-income row.
The improvement is meaningful, but historical profit variability and recurring adjustments argue against treating every EPS increment as durable operating productivity.

### Latest-quarter monetization and backlog
Q2 FY2027 revenue was **$11.345bn**, subscription/support **$10.820bn**, operating income **$2.331bn** versus **$2.332bn** a year earlier. [scout-financials]
Headline 11% revenue growth includes **$456m Informatica**; subscription 12% growth includes **$440m**. Organic performance must be separated from purchased growth. [crm-q2]
Current RPO is **$33.5bn**, up **14% Y/Y and constant currency**, while total RPO is **$66.3bn**, up **11%**. [crm-q2]
January's $72.4bn total RPO is not a same-season comparator: renewals and revenue recognition make quarter-end timing important. [crm-10k] [crm-q2]
cRPO is useful contracted forward revenue, not cash already earned, a guarantee of collectibility, or standalone AI profitability.
Management reports nearly **$3.9bn Agentforce/Data 360 ARR**, and Agentforce over **$1.5bn**, but expands the latter definition to AI offerings, Slackbot and Headless 360 effective this quarter. [crm-q2]
The FY2026 combined ARR already included **$1.1bn Informatica Cloud ARR**; neither combined growth nor redefined Agentforce ARR is a clean organic cohort comparison. [crm-fy26-release] [crm-q2]
Initial FY2027 OCF growth guidance of **9–10%** has become **4–5%** by Q2, despite higher revenue guidance; compare the changed cash outlook, not only the growth narrative. [crm-fy26-release] [crm-q2]
**7.0bn cumulative AWUs**, including **3.2bn this quarter**, and **104trillion ingested records** are adoption/activity measures; they do not establish paid realized revenue or gross profit. [crm-q2]
The next proof is incremental paid consumption, renewals and total wallet expansion after displaced seats, not a larger token or record counter.

## Moat

| Candidate advantage | Evidence | Counterevidence and response | Falsifying indicator |
|---|---|---|---|
| Workflow switching costs | Customer permissions, metadata, business logic, integrations and developer ecosystem [crm-10k] | Better AI interfaces can leave Salesforce as a lower-priced backend; APIs make some replacement easier | Core renewals weaken or retained customers reduce total spend despite AI use |
| Data/governance context | Data 360 unifies data; zero-copy access and Informatica broaden connectivity [crm-10k] [crm-q2] | Zero-copy interoperability may lower data captivity; governance can be built outside Salesforce | Customers run agents elsewhere without increasing Salesforce economics |
| Distribution and suite scope | Existing cross-selling relationships and connected applications [crm-10k] | Microsoft can bundle productivity, Dynamics and agents; specialist service agents attack individual workloads [msft-competition] | More expensive selling effort but slower core-cloud growth |
| Platform ecosystem | Administrators, AppExchange and integration tooling [crm-10k] | Ecosystem is not a consumer network effect; agents can commoditize custom interfaces | New extensions migrate outside the platform while API charges fail to offset losses |
| Pricing power | Expanded SKUs and configurable consumption [crm-pricing] | Issuer says pricing was not a significant FY26 growth driver; swaps can transfer, not enlarge budgets [crm-10k] | Credit adoption rises while net revenue per retained account stagnates |

Durability judgment: strong switching-cost foundation, **moderate confidence**, not a proven unassailable ten-year AI moat.
Over the observed period, profits and breadth improved, but Sales/Service growth has matured and acquisition-driven complexity increased.
A well-funded rival can replicate visible software features more easily than customer trust and installed processes; it need not replicate the full company to take the incremental profit pool.
Customers may capture productivity savings first; employees capture SBC; infrastructure/model providers receive compute spend. Revenue leadership alone cannot show shareholder capture.
Actual churn, net retention, realized price and per-agent gross margin were not independently collected; these remain hypotheses, not hidden factual assumptions.

## Management

### Capital allocation and stewardship
| Decision | Dated evidence and outcome | Stewardship assessment |
|---|---|---|
| Profit discipline and R&D | FY2026 GAAP operating margin20.1%; R&D$5.993bn [crm-10k] | Significant reinvestment continues; improved adjusted margins are not a substitute for GAAP costs |
| Informatica integration | Closed November2025; FY2026 acquisitions net cash$9.268bn; adds revenue and data foundations [crm-10k] | Strategically coherent, but purchased growth and acquired intangibles must earn their cost |
| FY2026 repurchases/dividends | Issuer headline repurchases$12.7bn, dividends$1.6bn; cash-flow repurchases$12.596bn, dividends$1.587bn [crm-10k] [crm-proxy] | Transaction headline, settlement cash and taxes are not identical definitions |
| FY2027 $25bn ASR | Initial103m shares delivered; final settlement expected October2026 [crm-q2] | Shrinks EPS denominator but debt financing consumes optionality; not free organic growth |
| Fin acquisition | Closed September10; more than30,000 companies; joins AI Labs [crm-fin] | Adds rapid-deployment agents beside configurable Agentforce; channel overlap and product coherence need proof |
| Contentful acquisition | Completed September1; composable content layer [crm-contentful] | Broadens orchestration, but adds another integration task rather than proven near-term return |

FY2026 SBC was **$3.509bn**, compared with cash repurchases **$12.596bn**; both are real observed amounts, not a computed net-owner-earnings figure. [crm-10k] [scout-financials]
First-half FY2027 SBC was **$1.763bn** and cash repurchases **$27.332bn**, with **$24.842bn** net debt issuance proceeds. [scout-financials]
Repurchases exceed SBC in dollars, but employee issuance and purchase prices determine actual net dilution; accounting SBC is not the same as share issuance value.
Current balances and EPS denominators reflect financial engineering as well as operating performance; future per-share growth must not receive a second automatic buyback uplift in the model.
Q2 GAAP EPS **$4.29** and adjusted **$5.90** coexist with **$2.613bn strategic investment gains** and essentially flat operating income. [crm-q2] [scout-financials]
Neither GAAP earnings inflated by investment marks nor adjusted earnings excluding recurring stock compensation is a clean owner-profit measure.

### Alignment, candor and succession
The proxy records one vote per share and no dual-class structure; Benioff beneficial ownership **2.8%** includes certain exercisable/near-vesting awards, not outright ownership of every listed share. [crm-proxy]
His FY2026 total compensation was **$49.379252m**; intended annual equity targets rise from **$36m FY2026 to $48m FY2027**, distinct from ASC718 reported compensation. [crm-proxy]
Additional proposed equity reserves of34m plan shares and20m ESPP shares are capacity, not already-issued dilution; their continuing use matters. [crm-proxy]
The proxy discloses TIME-affiliated business and aircraft reimbursements under related-party oversight. Disclosure is not proof of abuse, nor independent proof of arm's-length fairness. [crm-proxy]
The Governance Committee reviews CEO succession, but no independently evaluated successor readiness was retained; founder dependence remains material. [crm-proxy]
Management's expanded ARR definition is disclosed; the analytical responsibility is to resist calling it like-for-like AI growth. [crm-q2]
Stewardship confidence is mixed: credible profit discipline and disclosure, offset by recurring dilution, large compensation and renewed acquisition/debt commitments.

## Inversion

The strongest opposing thesis is **not that CRM disappears**: it is that useful AI makes the installed business a slower-growing utility while competition captures incremental agent economics.
Seat conversion can inflate AI adoption metrics without growing customer budgets; investment gains and buybacks can mask stagnating operating profit. [crm-pricing] [crm-q2] [scout-financials]

| Failure mechanism | Timing/severity | Observable warning and falsification | Model treatment |
|---|---|---|---|
| AI displaces paid human seats faster than usage expands | Next several renewals; durable growth impairment | Through FY2028, Agentforce activity rises but Sales/Service growth and paid total-wallet expansion weaken | Bear EPS−2% CAGR,11x exit multiple |
| ARR reclassification/purchased growth mistaken for organic acceleration | FY2027–FY2028; thesis overstatement | H2 FY2027 organic reacceleration commitment fails after separating Informatica, Fin, Contentful and FX | Base growth contingent on clean organic disclosure |
| AI cost and implementation burden absorb value | Deployment/renewal cycle; margin compression | More forward-deployed support, lower GAAP margins and little paid consumption conversion | Bear compression; no assumption AWUs map one-for-one to revenue |
| Acquisitions overlap or impair | Several years; return/cash optionality damage | Product roadmap fragmentation, weak acquired retention, goodwill charges, rising integration spend | Base17x ceiling; bull requires proven integration |
| Debt-funded repurchases crowd out resilience | Financing/refinancing years; amplified downside | Debt persists while sustainable cash generation weakens and buybacks continue |11.5% hurdle plus bear earnings/multiple path |
| Governance failure, major data breach or AI liability | Discrete event; potentially catastrophic | Material permissions failures, loss of enterprise trust, unremediated integrity concerns | **Not probabilistically captured** by ordinary three-case model |

Falsifiable favorable catalyst: H2 FY2027 organic reacceleration persists into FY2028, with stable-to-improving GAAP economics after removing strategic-investment gains.
Falsifiable unfavorable catalyst: cRPO performance falls materially below the issuer's approximately14% Q3 growth expectation while seat reductions accelerate. [crm-q2]
The ASP/seat tradeoff resembles earlier license-to-subscription shifts, but agents can eliminate users entirely; the analogy does not prove successful revenue replacement.
Bias checks: do not anchor to peak share prices, consensus “Buy,” $63bn company targets, or the low adjusted PE without checking the underlying earnings definition.
Unmodeled tails include cyber incidents, AI privacy/copyright liability, impairment, counterparty stress and abrupt founder transition; no invented probabilities are assigned.

## Industry

Customer acquisition, service resolution, governed data and compliant workflow execution are enduring productivity needs; “digital labor TAM” is not automatically Salesforce revenue.
Value chain: enterprise budgets → applications/data/integration → agent execution → model/cloud infrastructure → measurable business outcome.
Salesforce's opportunity is the trusted action layer and installed distribution, not necessarily ownership of the best underlying model. [crm-10k]
Flex Agreements permit swapping user licenses into credits and back; the issuer's 2025 launch rates were$2/conversation or20credits/$0.10 action, with employee usage also licensed per user. [crm-pricing]
Those are **dated announced prices**, not verified October2026 realized rates; bundling/free allowances and negotiated contracts limit revenue inference from usage.
Fin's rapid deployment on existing help desks complements enterprise customization, but can also reduce demand for heavyweight implementation. Its issuer-reported76% average resolution is not independently audited customer ROI. [crm-fin]
Microsoft's older FY26 Q1 observation shows Dynamics365 growth18% and Microsoft365Commercial cloud17%, with Copilot helping revenue per user. [msft-competition]
This establishes active competing distribution, not a same-quarter CRM market-share comparison; differing fiscal calendars and product scopes prohibit simplistic ranking.
Other suite vendors, data platforms, specialist agents and internal development are substitution routes identified in the issuer's competitive risk discussion. [crm-10k]
Buyers can demand credits that fit unchanged budgets; model/infrastructure suppliers can capture inference costs; privacy, permissioning and deployment work constrain adoption.
No independent numerical market-size estimate is retained. Promotional TAM, data-platform ARR and application ARR are not added together to manufacture an addressable market.
Bounded drivers for valuation: bear assumes substitution dominates; base assumes modest core growth plus paid AI expansion; bull requires sustained wallet expansion and integration success.
Long-term institution status depends on retaining workflow authority as interfaces change; durable demand does not guarantee durable vendor economics.

## Valuation

### Native calculations and earnings basis
All supported arithmetic below comes from the requested native calculate CLI and the saved evidence, not from vendor ratios or mental recomputation.
| Metric | Engine result | Interpretation |
|---|---:|---|
| Price × estimated outstanding shares | $188,573,990,000.00 | Not proof of the actual October9 share count |
| Absolute relative market-cap deviation | 0.00002115925120644853370101288646126107015962 | Within graph1% tolerance; rounded cap explains small difference |
| FY2026 OCF less same-year capex | $14,402,000,000 | Historical FCF, before SBC economic cost and acquisitions |
| Historical FCF / current reported cap | 7.6375% | Rounded; not a current-quarter or normalized yield |
| Price / FY2026 GAAP diluted EPS | 29.38x | Rounded; not vendor21.23x TTM or adjusted PE |

Historical FCF excludes acquisition spending, employee dilution and financed repurchases; it is not Buffett-style owner earnings or a perpetuity value.
The model starts with **$16.02 FY2028 adjusted consensus EPS**, observed October11; forecast page explicitly says EPS is non-GAAP. FY2027 forecast is$16.75, FY2026 adjusted$12.52 versus GAAP$7.80. [sa-forecast] [crm-10k]
FY2028 is selected instead of mechanically compounding the FY2027 spike; the publisher does not fully reconcile each adjustment or future investment-gain treatment.
The EPS basis is a forecast, not a fact about future earnings, and does not deduct every economic cost merely because it is called “adjusted.”
Exit multiples are correspondingly restrained; the bear/bull ranges also address forecast-basis risk. A GAAP-normalized alternative would require explicit tax/gain/SBC reconciliation not supplied here.
The engine configures **five EPS compounding steps**, not a dated horizon from the research day. It treats FY2028 adjusted EPS (year ending January31,2028) as initial earning capacity and assumes a **five-year holding/discount period**; that current-run-rate normalization is unverified. Literal fiscal increments lead to FY2033 earnings, whose use at the assumed exit is not justified by an explicit forward-PE timing convention in the saved inputs.
Required return is an explicit **11.5% assumption**, above the contemporary **5.24% ten-year Treasury par yield observed October9**. [treasury-20261009]
The equity hurdle compensates minority ownership and enterprise spending/financing exposure; monetization failure is also modeled directly in growth and multiple assumptions.

### Conditional earnings-multiple model, not DCF
| Case | Probability | EPS CAGR assumption | Exit adjusted PE | Conditional terminal price | Price-only CAGR (%) | Discounted present target at 11.5% |
|---|---:|---:|---:|---:|---:|---:|
| Bear |30%|−2%|11x|$159.29|−7.0133%|$92.43|
| Base |50%|8%|17x|$400.16|11.7969%|$232.20|
| Bull |20%|14%|23x|$709.44|25.3622%|$411.66|
Dollar displays round saved native outputs to cents; price CAGR multiplies saved `annualized_return` fractions by100 and rounds to four decimals. It is `(terminal price / $229.13)^(1/5) − 1` under the holding-period assumption, not historical YoY growth, EPS CAGR or a yearly stock-price path.

**Bear:** mature seat budgets contract, conversion mainly reallocates spend, interest/integration costs pressure per-share earnings;11x fits an ex-growth, leveraged adjusted-earnings business.
**Base:** core workflows endure, organic growth reaccelerates moderately and AI expands some customer wallets;8% EPS growth allows operating leverage but not heroic repeat investment marks;17x recognizes quality with SBC/debt constraints.
**Bull:** paid-agent deployment broadens across installed accounts and acquisitions integrate cleanly;14% EPS growth and23x require a sustained faster-growth platform, not just usage statistics.
Probabilities are judgmental assumptions:30% downside because replacement/integration risks are substantial;50% moderate execution;20% sustained stronger execution. They are not observed event frequencies.
The engine's weighted present target is **$226.16** (rounded), slightly below the observed$229.13 price.
The base present target alone is close to market price: modestly weaker growth, a lower multiple or poorer forecast normalization would remove the apparent cushion.
The bullish terminal price is highly sensitive to an assumption that Salesforce captures AI productivity; it is not comparable to a one-year analyst target. [sa-forecast]
Dividends, interim cash flows and transaction costs are excluded; EPS scenarios incorporate assumed net share effects, with no separately added buyback value. Returns are price-only, not full IRRs.
No reverse DCF, perpetual growth solution, independently verified fair value or claim that current pricing ensures the equity hurdle is made.

## Decision

| Lens | Conclusion/confidence | Evidence that could change it |
|---|---|---|
| Duan: right business | Recurring useful workflows; moderate-high confidence | Large-account renewals or spend structurally weaken despite continued product use |
| Buffett: durability | Installed processes stronger than temporary model features; moderate confidence | Agents move workflow authority elsewhere and Salesforce cannot monetize API/backend access |
| Duan/Buffett: stewardship | Mixed, not a veto based on current disclosures | Persistent expensive dilution, further debt-financed deals without clean organic economics |
| Munger: inversion | Seat substitution and adjusted-EPS optimism are credible | Paid cohort economics demonstrate larger total wallets after replaced seats |
| Li Lu: structural opportunity | Enterprise automation endures; capture uncertain | AI becomes mostly a low-cost bundled feature outside Salesforce |
| Price | Little modeled safety margin at$229.13; conditional only | Better reconciled earnings or materially lower valuation provides robust downside resilience |

**Watchlist rather than a definitive attractive-price conclusion.** Business resilience supports continued diligence; the probability-weighted model does not offer an evident margin of safety.
A five-year market closure would be tolerable only if retention, recurring paid workflows and after-compensation cash economics remain intact—not because agent counters keep rising.
Review next Q3 FY2027 release for cRPO versus approximately14% guidance, organic revenue bridges, paid Agentforce cohorts and acquisition-adjusted GAAP margins. [crm-q2]
Review October ASR settlement disclosures and the next filing's actual outstanding shares rather than assuming today's vendor count is definitive.
Thesis-breakers: repeated failure of promised organic reacceleration, falling total retained-customer wallets, impaired governance trust, or deterioration in debt service capacity masked by investment marks.
Highest-value diligence: speak with procurement/admin users about seat-credit swaps, integration workload, effective action pricing, measured ROI and renewals after free allowances expire.
Research confidence and business certainty remain distinct: annual statement agreement does not narrow the genuine bear-to-bull outcome range.
No allocation, broker action or order is recommended, and a provisional evidence verdict cannot be overridden by spreadsheet precision.

## Limitations and audit

### Evidence and model boundaries
Current outstanding shares are **estimated**, not actual October9 independently matched observations; this prevents fully verified status even though capitalization arithmetic reconciles.
Required annual reported facts retain independent publisher observations; SEC/issuer mirrors are not counted as independent publishers. Vendor-derived tables share the underlying issuer statements, but were separately observed published compilations.
Price corroboration includes a directly observed Fiscal.ai search result, not its blocked page. The July primary cover/cash source is also a retained search excerpt, not a full-document retrieval.
The historical canonical debt is January31 while cash is July31; dates are explicit, current debt is separately disclosed, and no mismatched-date net-liquidity subtraction is used.
SBC, lease classification, acquisition spending, unrealized investment gains, weighted-average shares and reported/adjusted EPS are separated rather than smoothed into convenient agreement.
Combined FY2026 ARR includes purchased Informatica; the retained issuer release establishes the component but does not independently corroborate its definition or ongoing profitability. [crm-fy26-release]
Agent-level margin, net retention, current negotiated pricing, acquisition returns and successor readiness remain unresolved; they are not fabricated as numerical facts.
Five-year history beyond the latest primary comparative years comes from a retained secondary compilation; continuous five-year offering/margin/cohort detail is not claimed.
Scenario probabilities, growth, multiples and hurdle rate are explicit assumptions; adjusted EPS is a sourced estimate whose full economic normalization is unavailable.
Date/return audit limitation: saved arithmetic does not establish an exact target date or validate the FY2028-to-exit alignment. The small base-case cushion and watchlist assessment remain conditional on that unresolved timing as well as adjusted-EPS economics; see the [batch return audit](../../../batches/2026-10-11/return-audit.md).
The original native audit checked implemented schema, provenance consistency, dates, headings and arithmetic, not the EPS-to-price calendar alignment. Consult `data/audit.json` for saved machine findings; artifact consistency does not independently certify source or investment truth.

### Retained source register
Every entry below has a locally retained relevant excerpt in data/evidence.json; access date2026-10-11.
- [crm-10k] [Salesforce FY2026 Form10-K PDF](https://d18rn0p25nwr6d.cloudfront.net/CIK-0001108524/124f523f-1f0b-4e13-8076-23cfd73951cf.pdf): primary annual accounts and business.
- [crm-q2] [Latest issuer Q2 FY2027 release](https://www.salesforce.com/news/press-releases/2026/08/26/fy27-q2-earnings/): quarter trends, ARR definition and guidance.
- [crm-fy26-release] [Issuer FY2026 annual results](https://www.salesforce.com/news/press-releases/2026/02/25/fy26-q4-earnings/): combined ARR acquisition component and initial guidance, superseded where applicable by Q2.
- [crm-q2-cover] [July2026 Form10-Q](https://www.sec.gov/Archives/edgar/data/1108524/000110852426000190/crm-20260731.htm): actually observed targeted search cover/cash/debt excerpts; full body unavailable.
- [sa-history] [Stock Analysis financial history](https://stockanalysis.com/stocks/crm/financials/): independent annual series, with standardized-operating-income conflict excluded.
- [sa-balance] [Stock Analysis detailed balance sheet](https://stockanalysis.com/stocks/crm/financials/balance-sheet/): cash/investments and lease-inclusive debt reconciliation.
- [sa-stats] [Stock Analysis quote/statistics](https://stockanalysis.com/stocks/crm/statistics/): timestamped close, rounded capitalization and vendor shares.
- [fiscal-quote] [Fiscal.ai CRM](https://fiscal.ai/company/NYSE-CRM): retained dated search-result price excerpt only.
- [cmc-cap] [CompaniesMarketCap snapshot](https://companiesmarketcap.com/salesforce/marketcap/): independently observed rounded cap, weekend date limitation.
- [scout-financials] [Ticker Scout financial tables](https://tickerscout.ai/crm/financials/): separately published annual/quarterly statements and gain explanations.
- [sa-forecast] [Stock Analysis adjusted forecasts](https://stockanalysis.com/stocks/crm/forecast/): dated observed estimate, not GAAP or endorsement of consensus.
- [crm-pricing] [Agentforce flexible pricing announcement](https://www.salesforce.com/news/press-releases/2025/05/15/agentforce-flexible-pricing-news/): dated seat-credit conversion mechanism.
- [crm-fin] [Fin acquisition closing](https://www.salesforce.com/news/press-releases/2026/09/10/salesforce-completes-acquisition-of-fin/): September10 completion and issuer product claims.
- [crm-contentful] [Contentful announcement/closing update](https://www.salesforce.com/news/stories/salesforce-signs-definitive-agreement-to-acquire-contentful/): September1 closing supersedes original future tense.
- [crm-proxy] [2026 proxy PDF](https://s205.q4cdn.com/626266368/files/doc_financials/2026/ar/Salesforce-FY26-Proxy-Statement.pdf): governance, compensation and margins.
- [msft-competition] [Microsoft FY26 Q1 performance](https://www.microsoft.com/en-us/investor/earnings/fy-2026-q1/productivity-and-business-processes-performance): older primary competitor distribution evidence.
- [treasury-20261009] [Treasury October2026 yield curve](https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_yield_curve&field_tdr_date_value_month=202610): shared retained10-year5.24% observation, not newly refetched.

### Execution disclosure
Observed tools: live read/web_search, native graph, plan, calculate and audit. Initial native audit returned **PROVISIONAL**, with one warning: **“required fact shares: estimate, not verified reported data.”** The report's status disclosure is then re-audited against the final exact saved artifacts.
Permanent tests, builds, linters and formatters were intentionally not run. No external checkout, broker connection or execution system was used.
