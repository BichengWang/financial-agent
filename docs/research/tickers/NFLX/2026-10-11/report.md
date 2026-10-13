# Netflix (NASDAQ: NFLX) — research as of 2026-10-11

[Research index](../../../index.md#2026-10-11) · [Run guidance](../../../README.md) · [Evidence](data/evidence.json) · [Calculations](data/calculations.json) · [Audit](data/audit.json)

**Research stance: attractive for further diligence, conditionally; not a verified allocation recommendation.**
The business has valuable content-scale economics, but monetization is growing much faster than measured viewing and disclosure is becoming less frequent.
The model's probability-weighted present target is **$96.72** (rounded), versus the observed **$70.30** regular-session close.
That target depends on a published adjusted FY2027 EPS forecast, future execution, assumed terminal multiples and the illustrative exit forward-PE/holding-period convention discussed below; it is not established intrinsic value.
Artifacts: `data/evidence.json`, engine-generated `data/calculations.json`, this `report.md`, and engine-generated `data/audit.json` in this directory.

## Grounding

### Security, source quality and snapshot
Netflix common stock trades on NASDAQ Global Select Market in USD, with one vote per common share; no ADR conversion or competing public common class is used. [issuer-2025-10k]
Information richness is **A**, but coverage richness is not economic certainty: consensus, issuer-selected engagement measures and vendor accounting standardization can reinforce the same narrative.
AI can compare public documents and arithmetic; it cannot inspect viewer-level churn, private sports contracts, content profitability or advertiser incremental-return data.

| Canonical fact | Value and actual period | Evidence and definition |
|---|---|---|
| Price | $70.30, 2026-10-09 16:00 EDT | Final regular-session close; StockAnalysis and ChartExchange historical table [sa-quote] [cx-price] |
| Shares used for cap check | 4,164,000,000, approximate latest disclosed base | **Estimate** for October capitalization; rounded June 30 actual outstanding shares, not EPS denominator [sa-balance] |
| Actual disclosed shares | 4,163,939,676, 2026-06-30 | Exact SEC-linked live search extract; not an exact October share register [issuer-q2-10q-search] |
| Market capitalization | $292,720,000,000, October 9 snapshot | Headline observations; CMC October 10 weekend carry-forward at same $70.30 [sa-marketcap] [cmc-marketcap] |
| Revenue | $45,183,036,000, FY ended 2025-12-31 | Consolidated annual, primary thousands normalized to dollars; independent rounded observation [issuer-2025-10k] [sa-income] |
| Net income | $10,981,201,000, FY ended 2025-12-31 | Consolidated GAAP income; not FY2026 fee-boosted earnings [issuer-2025-10k] [sa-income] |
| Operating cash flow | $10,149,273,000, FY ended 2025-12-31 | Includes content cash payments [issuer-2025-10k] [sa-cashflow] |
| Capital expenditure | $688,220,000, same FY2025 | Positive PPE cash purchases, not film amortization or content additions [issuer-2025-10k] [sa-cashflow] |
| Cash and equivalents | $9,099,232,000, 2026-06-30 | Excludes $28,678,000 short-term investments and restricted cash [issuer-q2-2026] [sa-balance] |
| Debt | $14,462,836,000, 2025-12-31 | Note-debt carrying value excluding operating leases; independent $14.46B search observation [issuer-2025-10k] [macroaxis-debt-search] |
| GAAP diluted EPS | $2.53, FY ended 2025-12-31 | Fully split-adjusted; independent same-period observation [issuer-2025-10k] [sa-income] |

### Explicit split and accounting reconciliation
The ten-for-one stock split was effected November 14, 2025; vendor trading-event date November 17 is the first split-adjusted trading session, not a contradiction. [issuer-2025-10k] [cx-price]
All price, shares, historical EPS and forecast EPS here use the post-split basis: $2.53 annual EPS must not become $25.30 alongside a $70.30 share price.
Q2 diluted weighted-average shares of 4,261 million are an earnings denominator and must not replace the actual June 30 share count. [issuer-q2-2026]
ChartExchange's header reports $70.31 at 15:59:59 EDT; its final-day table agrees with StockAnalysis at $70.30. After-hours $70.32 is a different timestamp. [cx-price] [sa-quote]
StockAnalysis's cap history row $292.73B differs from its $292.72B headline by rounding/timing; the native cap check reconciles without hiding either observation. [sa-marketcap]
Distinct quote/cap publishers may share feeds; publisher count alone does not prove independently collected exchange data.

Latest primary SEC-linked book debt is $14,309,306,000 at June 30, 2026; the letter's $14.4B gross debt is rounded principal, not precisely the same carrying-value measure. [issuer-q2-10q-search] [issuer-q2-2026]
FY2025 standardized vendor debt $16.976B includes operating leases, versus issuer note debt $14.462836B and lease liabilities $2.513001B separately. Do not call the larger figure a debt contradiction. [issuer-2025-10k] [sa-balance]
Vendor balance-sheet PPE includes reclassifications and is not a capital-spending measure. The cash-flow PPE-purchase line determines capex.
Issuer FY2025 repurchases $9.127167B exclude $46.165M award-settlement taxes; the vendor's $9.173B buyback row combines them. [issuer-2025-10k] [sa-cashflow]

## Business

### Who pays, for what, and why return
Households pay recurring fees for convenient, broad and localized entertainment; advertisers pay for access to opted-in audiences; members return for a changing slate and discovery experience instead of assembling many narrower subscriptions. [issuer-2025-10k] [issuer-q1-2026]
This is potentially a “right business” because a largely fixed content slate can be monetized globally, but monthly cancellation means value must be earned repeatedly.
Netflix reports **one operating segment**, not independently audited subscription, advertising, games and sports profit pools. Regional revenue is not regional operating profit. [issuer-2025-10k]

| FY2025 geography | Reported revenue | Economic driver and constraint |
|---|---:|---|
| US/Canada | $19,957,152,000 | Pricing and advertising; mature household penetration increases elasticity risk |
| EMEA | $14,514,646,000 | Local production and broad distribution; language complexity, quotas and levies |
| Latin America | $5,357,521,000 | Plan choice and distribution partnerships; inflation/FX and purchasing power |
| Asia-Pacific | $5,353,717,000 | Local hits and mobile accessibility; lower price points and formidable local platforms |

Regional values are issuer annual observations, not estimates of identical regional margins. [issuer-2025-10k]

### Five-year evidence, not an extrapolated straight line
| Fiscal year ended December 31 | Revenue, $B rounded | Operating margin | Net income, $B rounded | OCF, $B rounded | FCF, $B rounded |
|---|---:|---:|---:|---:|---:|
| 2021 | 29.698 | 20.86% | 5.116 | 0.39261 | -0.13198 |
| 2022 | 31.616 | 17.82% | 4.492 | 2.026 | 1.619 |
| 2023 | 33.723 | 20.62% | 5.408 | 7.274 | 6.926 |
| 2024 | 39.001 | 26.71% | 8.712 | 7.361 | 6.922 |
| 2025 | 45.183 | 29.49% | 10.981 | 10.149 | 9.461 |

Historical rows are **observed vendor series**, not additional native recomputations; issuer exact FY2023–FY2025 statements support the recent trend. [sa-income] [sa-cashflow] [issuer-2025-10k]
Gross margins in the same vendor series were 41.64%, 39.37%, 41.54%, 46.06% and 48.49% respectively. These do not eliminate content-production reinvestment requirements.
The 2022 setback and nearly flat 2023–2024 FCF demonstrate that subscription recurring revenue does not create mechanically smooth cash flow.

### Latest quarter and maturation
Q2 2026 revenue was $12.559938B, growth 13.4%, and operating margin 33.4% versus 34.1% a year earlier; EPS was $0.80 versus $0.72. [issuer-q2-2026]
Revenue growth slowed from Q1's 16.2%; Q3 guidance is 11.7%, while full-year revenue guidance is $51.0–$51.4B and operating margin 31.5%. Guidance is an estimate, not a realized result.
Q2 regional revenue growth was UCAN 10%, EMEA 14%, LATAM 21% and APAC 16%; these are reported-dollar growth rates with differing FX effects. [issuer-q2-2026]
Paid sharing enforcement can convert existing free consumption into revenue without creating equivalent new viewing; its finite conversion opportunity must not be capitalized as perpetual subscriber acceleration. [issuer-2025-10k]
Price changes in the US, Mexico and Spain were described as consistent with expectations; publicly observed cohort churn or incremental lifetime value is absent. [issuer-q2-2026]

Advertising exceeded $1.5B in FY2025, more than 2.5x FY2024, and management targets approximately $3B in FY2026. [issuer-q4-2025] [issuer-q2-2026]
The Q1 US ad plan cost $8.99 and represented over 60% of signups in advertising countries; that is a **signup mix**, not 60% of all memberships or viewing. [issuer-q1-2026]
More than 4,000 advertisers and programmatic access broaden demand, but total ad-tier economics depend on foregone subscription ARPU, ad fill, CPMs, measurement and retention.
No independently observed ad-tier revenue-per-member or contribution margin is available; a lower subscription price is not automatically incremental profit.

### Content cash economics
FY2025 gross content additions were $17.096617B, liability change was a $0.610838B cash-flow deduction, and amortization was $16.422166B. These are distinct accounting components. [issuer-2025-10k]
Content cash spending belongs inside **operating cash flow**; subtracting content amortization or content additions again from OCF would manufacture a false FCF number. [issuer-content-accounting]
Conversely, adding back film amortization to net income while ignoring content replenishment would manufacture excessive cash earnings.
Licensed originals need not be owned IP: the accounting slides distinguish MGM's *Wednesday* and Paramount's *Emily in Paris* from owned productions. [issuer-content-accounting]
Produced titles require cash before release; accelerated viewing-based amortization begins on availability, with over 90% expected within four years. Useful life and tax incentives matter.
FY2025 production incentives lowered amortization by approximately $1B; this is a geographic policy exposure, not proof the content is costless. [issuer-2025-10k]
The circle-of-competence boundary is slate-level cash discipline and member value, not predicting every hit or claiming private rights-contract economics are known.

## Moat

| Candidate advantage | Evidence | Counterevidence and competitive response | Falsifying indicator / durability |
|---|---|---|---|
| Global content scale | Broad regional revenues; non-English titles exceed one-third of H1 viewing; one title can travel globally | Content rights can be territorial; licensors and talent can capture the surplus; Amazon/Disney have deep resources | Content spend persistently outgrows revenue without retention benefit; moderately durable |
| Brand and habit | Over 325M paid memberships in Q4; service reaches an audience approaching one billion | Memberships are not unique viewers; cancellations/rejoins are easy; household budgets constrain subscriptions | Multiple price changes impair revenue growth and independent share; medium confidence |
| Discovery/delivery technology | Open Connect and personalized recommendations lower friction; AI tools extend production and ads workflows | Powerful competing platforms can reproduce technology; unobserved cost savings are not booked as moat value | Product changes fail to improve retention or viewing; supporting advantage, not monopoly |
| Pricing power | 2025 growth and margin expansion; 2026 price changes described as going well | Paid-sharing and mix obscure elasticity; pricing can outrun engagement temporarily | Weak volume/viewing plus revenue deceleration after increases; conditional |
| Advertising scale | Larger advertiser base, programmatic access and premium live inventory | YouTube/Meta/Amazon have superior measurement scale; member annoyance limits ad load | Ad revenue misses guidance despite rising inventory; emerging, not proven |

Evidence: [issuer-2025-10k] [issuer-q4-2025] [issuer-q1-2026] [issuer-q2-2026].
This is primarily a **scale/content-distribution advantage**, not a strong direct user-to-user network effect: another member does not directly improve my viewing as a messaging participant would.
Switching costs are low; habit and exclusive availability differ from costly enterprise migration.
The economic flywheel can widen with better global monetization, but supplier bargaining, sports renewal prices and abundant free content can narrow it.
Ten-year durability is plausible for the platform and brand; current margins and premium valuation deserve materially less certainty.

## Management

### Decisions and observed outcomes
| Decision | Original rationale and observed subsequent result | Stewardship interpretation |
|---|---|---|
| Advertising / paid-sharing monetization | Broaden affordable access and collect previously unmonetized usage; FY2025 ads above $1.5B | Evidence of adaptation, but no public cohort economics proving every dollar repeatable |
| Warner Bros acquisition bid then withdrawal | January proposed acquisition as strategic acceleration; April says only at right price, declined higher offer and received $2.8B fee | Walking away is evidence of price discipline; proposed scale of borrowing was real risk, not an existing asset |
| Buyback resumption and authorization | Q2 buybacks $4.7B; April additional $25B authorization | Excess-cash return potentially useful; authorization is not cash available or proof shares bought cheaply |
| InterPositive acquisition | March filmmaking AI tools; Q1 acquisitions cash line $585.744M | Reinvestment option, not verified synergy or recurring earnings uplift |
| Founder transition | Hastings stopped executive role in 2025 and would not seek June 2026 Board re-election | Institution now tested without founder Board role; product/content leadership depth matters |

Sources: [issuer-q4-2025] [issuer-q1-2026] [issuer-q2-2026] [issuer-proxy-2026].
FY2025 technology/development expense was $3.391390B; capital allocation includes ongoing product work and content, not only financial repurchases. [issuer-2025-10k]
FY2025 SBC was $368.449M, added back in OCF but still an ownership cost; options outstanding and potential future issuance must be monitored. [issuer-2025-10k] [issuer-q2-10q-search]
Buybacks shrink actual share count, but cash spent is not an automatic addition to model targets: EPS assumptions already include an implicit net-dilution outcome.
No dividend is added to valuation or assumed promised.

### Incentives and candor
The 2025 bonus emphasized FX-neutral operating margin (65%) and revenue (35%); long-term equity was equally PSUs/RSUs, with PSUs tied to three-year relative TSR. [issuer-proxy-2026]
This aligns with profitable growth better than subscriber volume alone, but annual margin incentives can reward deferred spend and TSR can amplify multiple-focused behavior.
Ownership guidelines require six-times salary for co-CEOs and three-times for other executives within five years; guidelines are not proof of current beneficial ownership or unencumbered investment.
The Board rejected Hoag's 2025 resignation after a failed majority vote, explaining attendance circumstances; improved 2025 attendance is mitigating evidence, not restoration of shareholder consent. [issuer-proxy-2026]
Related-party production work involving Sarandos' family is disclosed with review policy; no independent fairness appraisal was obtained, and no misconduct finding is asserted.
Reduced routine subscriber disclosure and now annual engagement publication make management's “quality and variety” claim less externally falsifiable. [issuer-q2-2026]
Candor is mixed: explicit fee and FCF timing explanations help, while less frequent leading-indicator disclosure raises the burden on independent measurement.

## Inversion

### Strongest opposing thesis
Netflix may have harvested a finite paid-sharing pool and repriced a mature audience while engagement barely grows; recurring rights inflation then captures monetization gains, and slower disclosure hides weakening unit economics until profit forecasts reset.
A falling share price alone does not falsify that bear thesis or prove cheapness.

| Failure mechanism | Timing / severity | Observable early warning | Mitigation and model treatment |
|---|---|---|---|
| Pricing/paid-sharing maturation | Next several quarters; material growth reset | Sub-10% revenue growth across several quarters, churn evidence or declining viewing share | Affordable ads can protect access; bear EPS growth 2% and 18x exit |
| Ad monetization disappoints | 2026–2028; meaningful but not total-business extinction | Missing approximately $3B 2026 target; agency complaints or higher ad load with poor engagement | Better programmatic tools; base does not assume exponential ad growth indefinitely |
| Live rights bidding war | Renewals over several years; cash commitments can ratchet higher | Spend share rises without retained cohorts/advertiser yield; events produce one-month joins | Selective rather than full-league approach; lower bear multiple captures weaker reinvestment returns |
| Content accounting masks deterioration | Slate-cycle/estimate revisions; material margin and cash-flow hit | Content cash ratio rises while viewing flat; slower amortization revisions or impairment | Monitor gross additions, liabilities, incentives and cash taxes together |
| Capital-allocation overreach | Event-driven; potentially severe | New leveraged mega-deal or buybacks consuming liquidity before content obligations | Past bid withdrawal encouraging; no acquisition synergies assumed |
| Disclosure/governance slippage | Immediate monitoring problem; can become thesis veto | Further metric withdrawal, unexplained adjustments or repeated disregard of votes | Demand independent measurement; do not compensate an integrity veto with a discount rate |

Ordinary seasonality and tax timing differ from business failure: Q2 FCF fell to $1.525168B from $2.267369B, with higher taxes partly associated with the termination fee. [issuer-q2-2026]
FY2025 FCF benefited from a roughly $700M Brazil deposit moving into 2026; extrapolating that high year without the disclosed cash timing would anchor incorrectly. [issuer-q4-2025]
Historical analogy: pay-TV demonstrated that distribution scale can eventually transfer value to sports rights owners; Netflix differs through global on-demand libraries and lower bundling lock-in, so the analogy is a risk mechanism, not a prediction.
Unmodeled tails include prolonged strikes, regional bans, litigation, privacy constraints, outages during major live events and a transformative acquisition. No invented individual tail probabilities are assigned.

## Industry

Entertainment demand is enduring; the relevant productivity gain is global digital distribution and localized discovery, not an assumption that every premium studio captures all streaming growth. [issuer-2025-10k]
Value chain: creative talent/IP owners → producers/licensors → Netflix's aggregation, discovery and delivery → households; a second path runs advertiser/agency → ad-tech measurement → opted-in viewers.
Households have bargaining power through cancellation; suppliers have bargaining power through unique IP/live rights; platforms with ecosystem profits can subsidize rival content.
Alternatives include YouTube, social video, gaming, piracy, linear TV and local broadcasters, not just competing subscription services. [issuer-2025-10k] [issuer-q1-2026]

Independent MediaPost coverage of Nielsen's June 2026 Gauge reports Netflix US TV share 7.9% versus 8.3% a year earlier, while YouTube reached 13.5% and Prime 4.2%. [mediapost-gauge]
That is counterevidence to a uniformly widening attention moat, but not a global/mobile share estimate; the article warns that universe-estimate recalibration may change streaming measures.
Issuer H1 global hours grew only 2%, versus much faster revenue growth; price, mix and conversion can explain divergence, but viewing per cohort cannot be reconstructed from these aggregates. [issuer-q2-2026]
Company-promoted less-than-45% broadband-household TAM penetration and approximately 5% global TV view share are **issuer estimates**, not audited addressable-revenue measures. No numerical TAM valuation is used. [issuer-q1-2026]

Live economics require incremental subscription lifetime value plus ad contribution to exceed rights, production, technical and marketing costs, after allowing for one-event churn.
Management expects live to represent just over 5% of 2026 content spend but approximately 1% of hours, while accounting for six of ten largest signup days over five years. [issuer-q2-2026]
That can be rational acquisition spending, but signup records without retained cohorts do not establish an attractive rights IRR.
Topical live content is expensed when aired and lacks the same long-tail library option as a durable series; rights renewals can reset rents upward. [issuer-content-accounting]
Games, podcasts and AI may extend entertainment moments and improve production efficiency; no separate commercial valuation is assigned without segment cash evidence.
Regulatory production quotas, local levies and changes in production incentives can reduce global-scale gains. [issuer-2025-10k]

## Valuation

### Native historical calculations
`calculate data/evidence.json --output data/calculations.json` produced the saved Decimal outputs summarized below; rounding is for display, and none proves independent market truth.

| Native metric | Display output | Interpretation |
|---|---:|---|
| Implied cap | $292,729,200,000.00 | $70.30 times approximate 4.164B share base |
| Absolute relative cap deviation | 0.00003142935228204427439191035802131729980869 | Below graph 0.01 tolerance; does not verify October exact shares |
| FY2025 FCF | $9,461,053,000 | Same-period annual OCF minus positive PPE purchases |
| FY2025 FCF/current-cap yield | 3.2321% | Rounded; historical cash numerator, current cap denominator, not forward owner-earnings yield |
| Price/FY2025 GAAP diluted EPS | 27.79x | Rounded; historical annual EPS basis, not vendor TTM PE |

Vendor TTM EPS $3.17 contains FY2026's fee-boosted quarter; its 22.15 PE must not be represented as the native FY2025 calculation. [sa-quote] [issuer-q1-2026]
Cash conversion includes SBC, working capital, production incentives and tax timing; issuer FCF is not necessarily distributable owner earnings.
FY2026 $12.5B FCF guidance includes the termination-fee benefit; do not treat that gain as a perpetual entertainment cash stream. [issuer-q1-2026] [issuer-q2-2026]

### Conditional earnings-multiple model, not DCF
Basis is published **FY2027 adjusted consensus EPS $3.81**, kind `estimate`, observed October 11; the source explicitly labels forecast EPS non-GAAP. [sa-forecast]
It is not GAAP historical EPS, and its detailed adjustment bridge is unavailable. Choosing 2027 avoids directly compounding the 2026 termination-fee quarter but does not independently verify normalization.
The model configures **five EPS compounding steps** from FY2027 and assumes a **five-year holding/discount period**. The retained convention interprets the result as a forward FY2032 earnings proxy capitalized at an illustrative October2031 exit; that is potentially coherent forward-PE economics, not a verified exact target date.
This specific exit-forward-PE assumption does not claim FY2032 earnings are earned by October2031. Explicit calendar alignment and the appropriate earnings window at exit remain unverified in the saved inputs.
Required return is **11% USD nominal**, an assumption above the **5.24% October 9 ten-year Treasury par yield**; the additional compensation is judgment, not a CAPM estimate. [treasury-20261009]
Dividend/interim distributions are excluded; terminal EPS growth includes assumed net share changes, so repurchase dollars are not added again.

| Case / assumed probability | EPS CAGR assumption / exit forward PE | Conditional terminal price | Price-only CAGR (%) | Discounted present target at 11% |
|---|---|---:|---:|---:|
| Bear / 30% | 2% / 18x | $75.72 | 1.4959% | $44.93 |
| Base / 50% | 11% / 26x | $166.92 | 18.8808% | $99.06 |
| Bull / 20% | 17% / 34x | $284.01 | 32.2134% | $168.55 |

Dollar displays round saved native outputs to cents; price CAGR converts saved `annualized_return` fractions to percent and rounds to four decimals. It is `(terminal price / $70.30)^(1/5) − 1`, not historical YoY return, assumed EPS CAGR or each intervening year's stock return. Probabilities sum to one and are analytical assumptions, not observed outcome frequencies; exact outputs remain in `data/calculations.json`.
**Bear:** post-conversion household growth matures, ads cannibalize subscription mix, and rights/content costs absorb pricing; 2% EPS growth and 18x value a slower but still profitable service.
**Base:** regional expansion, disciplined pricing and maturing ads preserve profitable growth; 11% EPS growth allows modest net buyback benefit but less leverage than recent monetization catch-up; 26x rewards durable scale while recognizing renewal needs and low switching costs.
**Bull:** incremental ad contribution and international monetization grow faster than content cost, with selective live and technology improving retention/costs; 17% EPS growth and 34x require proven double-digit compounding, not merely games/podcast popularity.
The premium bull multiple is justified only if forward growth remains high at maturity; a temporary growth spurt followed by price/rights saturation would not deserve it.

Native probability-weighted present target: **$96.72** (rounded).
Sensitivity is visible in the cases: the bear discounted value is well below $70.30, while base/bull are above; the conclusion reverses if bear economics dominate or the adjusted EPS basis proves overstated.
The consensus 12-month target $92.55 is sourced context, not corroboration of a five-year model or a substitute for these assumptions. [sa-forecast]
No unsupported reverse-DCF, perpetual cash-flow or rights-IRR calculation is presented as tool-verified.

## Decision

**Conditionally attractive for further diligence**, rather than a definitive purchase/portfolio instruction: current price does not require the bull case in this particular model, but forecast quality, the exit forward-PE/holding-period alignment and attention trends must be resolved before reliance.
Business quality is high-confidence recurring aggregation; moat durability is medium-confidence scale/habit; stewardship is mixed-to-positive with an explicit governance caveat; price attractiveness is conditional on the adjusted EPS bridge and timing convention.
Buffett's durability lens favors distribution scale, Duan's business/people lens favors repeat member value and a willingness to walk away from a bid, Munger's inversion warns about finite monetization harvest, and Li Lu's structural lens recognizes digital distribution while refusing to assume all value stays with Netflix.
These are analytical lenses, not simulated endorsements or investor quotations.

### Actionable research review triggers
- At the reported October 20 earnings date, compare realized Q3 revenue and operating margin with $12.860B and 33.2% guidance; separate amortization timing from demand. [sa-quote] [issuer-q2-2026]
- Reconstruct recurring FY2026 earnings/cash excluding the termination fee using disclosed tax effects; obtain the analyst FY2027 adjustment bridge rather than subtracting mismatched periods.
- Observe pricing retention, ad revenue realization against approximately $3B guidance, and ad-tier mix/measurement; require cohort evidence before calling signups durable growth.
- Compare independent TV-viewing trends with global title data, allowing for Nielsen methodology changes and no longer semiannual issuer aggregate disclosure.
- Obtain renewed live-rights cost/retention evidence, exact latest shares and buyback prices before attributing economic return to capital deployment.
- Reconsider if several quarters combine sub-10% revenue growth, rising content cash needs and falling independent share; suspend the thesis for evidence of accounting opacity or severe governance deterioration.

If trading stopped for five years, global member demand and replenishable content cash economics—not the target—would support continued study; unknown renewal and cancellation economics remain reasons to refuse ownership.
AI research confidence is relatively high on FY2025 statements and dated quote, lower on current share count, forecast adjustments and private unit economics; investment certainty remains intrinsically low.

## Limitations and audit

All nine graph nodes were executed in dependency order through retained sourcing, business/moat/stewardship/inversion/industry analysis, native valuation, synthesis and final artifact audit.
The pre-date/return-review native audit was **PROVISIONAL** (exit1), with warning `required fact shares: estimate, not verified reported data` and no BLOCKED findings. That earlier verdict did not validate the forward-PE calendar convention; consult `data/audit.json` for saved machine findings. This report review did not execute a new native audit.
Required share count is deliberately **estimate**, despite exact June 30 primary shares: October's contemporaneous register after subsequent issuance/buybacks was not independently observed.
Historical required income/cash-flow facts use the latest complete FY ended December 31, 2025, not an implied current run rate; cash is June 30, debt's corroborated canonical is December 31, with latest debt separately disclosed.
Primary/issuer mirrors count as Netflix, not separate independent publishers; vendor publishers may share underlying feeds.
SEC direct reader returned a company index, raw fetch returned HTTP403; exact Q2 shares/book debt therefore use narrowly retained live search excerpts, not a claimed full-document fetch.
Macroaxis's dated debt snippet was observed through live search but full-page fetch was HTTP403; no broader page claims are made. Alternative Nasdaq/Yahoo/Morningstar routes were attempted, not fabricated into corroboration.
Yahoo and Fiscal.ai returned HTTP429; Google Finance unsupported; YCharts HTTP405; GuruFocus HTTP403. These failures are not retained as financial observations.
Forecast adjustments, ad-tier contribution margins, subscriber churn cohorts, precise live-rights cash costs, local profitability and title-level economic returns remain unresolved.
No full 2026 realized fiscal cash-flow result exists in this scan; Q2 cash is not October cash, and forward EPS is not GAAP fact.
Model excludes unmodeled severe tails, dividends and interim cash distributions; assumed net dilution/growth and terminal PE dominate the target.
Date/return audit limitation: consistent arithmetic does not certify a five-calendar-year forecast. October2031/FY2032 is the retained illustrative forward-PE convention, whose calendar implementation is not validated by the saved model inputs; see the [batch return audit](../../../batches/2026-10-11/return-audit.md).
Native calculations/audit recompute arithmetic and structural evidence-contract consistency, not web truth, forecast accuracy, securities suitability or investment approval.
No permanent tests, build, lint or formatting checks were run; no orders, broker actions, outside checkout or non-NFLX files were modified.

### Retained source links
Every retained source has a local excerpt in `data/evidence.json`; citation IDs below link to the observed documents/pages.
- [issuer-2025-10k](https://s22.q4cdn.com/959853165/files/doc_financials/2025/ar/99482238-46b2-4d0d-b292-40e6781bdf03.pdf) — audited annual statements and accounting.
- [issuer-q4-2025](https://s22.q4cdn.com/959853165/files/doc_financials/2025/q4/FINAL-Q4-25-Shareholder-Letter.pdf) — FY2025 outcome and cash timing.
- [issuer-q1-2026](https://ir.netflix.net/files/doc_financials/2026/q1/FINAL-Q1-26-Shareholder-Letter.pdf) — fee, ads, acquisition withdrawal and leadership.
- [issuer-q2-2026](https://s22.q4cdn.com/959853165/files/doc_financials/2026/q2/FINAL-Q2-26-Shareholder-Letter.pdf) — latest quarter and guidance.
- [issuer-q2-10q-search](https://www.sec.gov/Archives/edgar/data/1065280/000106528026000212/nflx-20260630.htm) — narrowly observed primary search extract.
- [issuer-proxy-2026](https://s22.q4cdn.com/959853165/files/doc_financials/2025/ar/Netflix-2026-Proxy-Statement.pdf) — governance/incentives/related parties.
- [issuer-content-accounting](https://s22.q4cdn.com/959853165/files/doc_downloads/2025/IR-Content-Accounting-Slides-May-2025.pdf) — content recognition, cash and amortization.
- [sa-quote](https://stockanalysis.com/stocks/nflx/) and [cx-price](https://chartexchange.com/symbol/nasdaq-nflx/historical/) — independently observed closing-price tables.
- [sa-income](https://stockanalysis.com/stocks/nflx/financials/income-statement/), [sa-cashflow](https://stockanalysis.com/stocks/nflx/financials/cash-flow-statement/) and [sa-balance](https://stockanalysis.com/stocks/nflx/financials/balance-sheet/) — historical and balance observations.
- [sa-marketcap](https://stockanalysis.com/stocks/nflx/market-cap/) and [cmc-marketcap](https://companiesmarketcap.com/netflix/marketcap/) — capitalization snapshots.
- [macroaxis-debt-search](https://www.macroaxis.com/financial-statements/NFLX/Short-Long-Term-Debt-Total) — observed dated FY2025 debt search snippet.
- [sa-forecast](https://stockanalysis.com/stocks/nflx/forecast/) — explicitly adjusted analyst estimates.
- [mediapost-gauge](https://www.mediapost.com/publications/article/417308/streaming-climbs-to-485-per-last-lame-duck-edit.html) — independent viewing-share counterevidence and measurement caveat.
- [treasury-20261009](https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_yield_curve&field_tdr_date_value_month=202610) — common retained primary ten-year yield.
