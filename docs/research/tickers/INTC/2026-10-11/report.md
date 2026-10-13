# Intel Corporation (NASDAQ: INTC): native investment research

[Research index](../../../index.md#2026-10-11) · [Run guidance](../../../README.md) · [Evidence](data/evidence.json) · [Calculations](data/calculations.json) · [Audit](data/audit.json)

As of **2026-10-11** · USD · **PROVISIONAL research, not an allocation recommendation**.
Observed regular-session close: **$104.70**, October 9, 2026, 16:00:01 EDT (Yahoo); StockAnalysis rounds the timestamp to 16:00 EDT.
Conditional five-year probability-weighted present-price benchmark: **$47.96**, not a validated fair value or a DCF.
This report completes the nine repository graph nodes. The imported `archive/claude-trial.md` is preserved, not treated as independent evidence.

## Grounding

Intel common stock trades on the Nasdaq Global Select Market; the filing identifies common stock with $0.001 par value, not an ADR. [intel-q226-10q]
Information richness is **A: abundant**, but investment certainty is substantially lower than the volume of commentary suggests.
The date is a Sunday: Friday's actual close is the latest completed regular session, not a historical substitute chosen to fit a thesis.
[sa-quote] and the recovered real Yahoo browser text [yahoo-quote] independently show $104.70; both also show $104.43 after hours.
The native quote time retains Yahoo's actual one-second timestamp; the minute-resolution StockAnalysis time is compatible.
All observations were recovered from successful source reads/browser observations made on October 11; failed requests were not relabeled evidence.

| Required fact | Canonical value | Period, definition and observations |
|---|---:|---|
| Price | $104.70 | October 9 regular close; [sa-quote], [yahoo-quote] |
| Shares | approximately 5,286,105,262 | Estimate: rounded July 17 filing count plus August offering/option; not reported October shares [intel-q226-10q], [intel-offering] |
| Market capitalization | $553.455B | Yahoo October 9 snapshot; StockAnalysis $550.15B retained, not erased [yahoo-quote], [sa-quote] |
| Revenue | $52.853B | FY2025 ended December 27, consolidated [intel-fy25], [sa-financials] |
| Net income | −$267M | FY2025 attributable to Intel; not the +$26M total before noncontrolling interests [intel-fy25], [sa-financials] |
| Operating cash flow | $9.697B | FY2025 consolidated [intel-fy25], [sa-financials] |
| Capital expenditure | $14.646B | FY2025 investing-section PP&E cash outflow, positive spending basis [intel-fy25], [sa-financials] |
| Cash and equivalents | $12.874B | June 27, 2026 consolidated balance sheet [intel-q226], [sa-balance] |
| Debt | $50.537B | June 27 current debt $1.988B plus long-term debt $48.549B [intel-q226], [sa-balance] |
| GAAP diluted EPS | −$0.06 | FY2025 attributable to Intel, not adjusted EPS [intel-fy25], [sa-financials] |

Every required reported fact retains two publisher observations in `data/evidence.json`; the required share fact is honestly an estimate.
The issuer's SEC mirror remains an Intel publication. Two Intel documents never count as two independent publishers.
StockAnalysis financial normalization is an independently observed publisher, not an independent audit of Intel's underlying books.
Quote publishers differ in their capitalization/share snapshots. Their cap observations are within the engine's 1% tolerance, not identical.
The July 17 cover reports **5,044 million** actual shares, versus June 27 balance-sheet **5,043 million** and Q2 EPS **5,104 million** weighted shares. [intel-q226-10q], [intel-q226], [sa-balance]
The August 12 8-K records **210,526,315** shares at **$95** and full exercise on August 11 of the **31,578,947** additional-share option. [intel-offering]
Our approximation assumes the announced closing and adds those transactions to a filing count rounded to millions; intervening awards and escrow releases remain unknown.
The pricing release expected an August 12 closing; these observations do not constitute a final October 9 share-register confirmation. [intel-offering-pr]
Cash excludes **$16.853B** short-term investments and **$723M** legally restricted cash in other assets; none is labeled freely distributable parent cash. [sa-balance], [intel-q226-10q]
Debt excludes separately classified lease obligations. StockAnalysis's June lease rows are unavailable, not evidence of zero leases. [sa-balance]
Its FY2025 standardized debt includes lease rows and must not be silently compared with issuer debt on a supposedly identical definition.

### Five-year observations and accounting boundary

The following historical values are observed annual StockAnalysis figures, with FY2025 checked directly against the issuer. USD billions except EPS. [sa-financials], [intel-fy25]

| Fiscal year-end | Revenue | Intel-attributable net income | GAAP diluted EPS | Operating cash flow | Investing-section PP&E spend |
|---|---:|---:|---:|---:|---:|
| 2021-12-25 | 79.024 | 19.868 | 4.86 | 29.456 | 20.329 |
| 2022-12-31 | 63.054 | 8.014 | 1.94 | 15.433 | 24.844 |
| 2023-12-30 | 54.228 | 1.689 | 0.40 | 11.471 | 25.750 |
| 2024-12-28 | 53.101 | −18.756 | −4.38 | 8.288 | 23.944 |
| 2025-12-27 | 52.853 | −0.267 | −0.06 | 9.697 | 14.646 |

Older years are contextual secondary observations, not claimed to have the same primary-source depth as the canonical FY2025 inputs.
StockAnalysis standardized operating income/gross profit differs from issuer GAAP treatment of some charges: neither is substituted for GAAP segment or consolidated results.
No continuous five-year GAAP margin series is claimed; the retained evidence supports the annual revenue/earnings/cash-flow table and current quarterly margins.
AI limitations: no live exchange feed, customer interviews, wafer-yield audit, or privately negotiated foundry contracts were obtained.
The strongest bias is treating the 2026 share-price narrative as proof of foundry economics; the counter-test is external customer cash profitability.

## Business

OEMs, enterprises and cloud operators buy Intel processors for compatible computing performance; they return when products remain economical and software works, with AMD and Arm routes as alternatives.
Intel also manufactures wafers, substrates and packaging, mostly for its own product businesses, and sells limited services to external customers. [intel-q226-10q]
These are recurring hardware purchases, not contractual subscription revenue; refresh cycles and customer inventory can move reported demand sharply.

| Business | Q2 FY2026 revenue / operating income | Economic interpretation |
|---|---|---|
| Client Computing and Physical AI | $8.877B / $2.343B | PCs/edge platforms; product replacement cycle and competition [intel-q226] |
| Data Center and AI | $6.262B / $2.474B | Server/product demand; agentic AI can help CPUs but does not guarantee Intel captures accelerator spending [intel-q226] |
| Total Intel Products | $15.139B / $4.817B | Profitable product segments under the transfer-price framework [intel-q226] |
| Intel Foundry | $5.765B / −$2.089B | Predominantly internal sales; cannot be valued as $5.765B external foundry revenue [intel-q226] |
| Consolidated | $16.128B / $1.796B | After intersegment eliminations, other businesses and unallocated costs [intel-q226] |

FY2025 Products operating income was **$12.739B**; Foundry lost **$10.318B** on **$17.826B** segment revenue. [intel-fy25]
The product franchise is economically different from an emerging third-party foundry. Combining their headline revenues would double count internal manufacturing.
Foundry's market-like transfer prices are managerial estimates, not independent customer auctions establishing the stand-alone value of its factories. [intel-q226-10q]
Actual external foundry/assembly/test revenue was **$293M** in Q2 and **$467M** in the first half; first-half growth was primarily Altera's transition to an external customer. [intel-q226-10q]
That reclassification is not proof of a large new leading-edge design win, and external revenue alone says nothing about external contribution margin.
Segment profits exclude corporate stock compensation, restructuring and certain acquisition charges; they are not distributable owner earnings. [intel-q226-10q]
Most consolidated depreciation is incurred in Foundry, absorbed into inventory and product costs; a clean stand-alone segment depreciation allocation is impracticable. [intel-q226-10q]
The consolidated history shows a much smaller revenue base and much weaker earnings than FY2021 despite a current product-cycle recovery. [sa-financials]
Q2 GAAP gross margin was **40.4%**, operating margin **11.1%**, GAAP EPS **−$2.16**, and adjusted EPS **+$0.42**. [intel-q226]
The giant GAAP loss is not equivalent to a giant operating cash loss: the escrow derivative is a major noncash reconciling item. [intel-q226-10q]
But removing it does not remove the contractual dilution/economic allocation underlying the arrangement.

### Cash conversion and reinvestment

FY2025 plain native FCF is **−$4.949B** using the same annual operating-cash-flow and investing-capex period; it is not Intel's adjusted FCF.
The issuer additionally shows **$3.026B** PP&E payments in financing activities, government incentives and partner contributions. [intel-fy25]
Thus even plain investing-section FCF does not capture all equipment-related cash reinvestment; it is not maintenance spending or owner earnings.
First-half 2026 OCF was **$8.102B**, investing-section PP&E outflow **$6.192B**, with further **$1.423B** PP&E and **$832M** finance-lease payments in financing. [intel-q226]
Do not mix the $7.0B Q2-only OCF headline with the first-half capex table or call the resulting number annual FCF.
The **$14.2B** Apollo Ireland interest repurchase sits outside ordinary capex and still consumes shareholders' cash. [intel-q226-10q]
Supplier terms, customer program timing and inventory management can improve near-term OCF and reverse later; the filing expressly warns about this. [intel-q226-10q]
Circle of competence: product demand and disclosed cash flows are interpretable; process yield, competitive cost per good die and private external commitments are not established.

## Moat

The defensible candidate is the installed software/platform ecosystem and execution capability, not a categorical monopoly over future compute.

| Candidate advantage | Supporting evidence | Counterevidence / competitor response | Falsifying indicator |
|---|---|---|---|
| x86 software compatibility | Existing product franchise produces segment profits [intel-q226] | AMD supplies x86 without Intel's foundry burden [amd-q226] | Profitable workloads migrate despite compatibility advantages |
| Scale and manufacturing learning | 18A products entered high-volume production; management reports yield/cycle-time improvement [intel-q226-10q], [intel-q226] | Foundry still reports large operating losses | Added volume fails to improve cash cost or Foundry losses |
| Domestic leading-edge optionality | Issuer cites US leading-edge logic R&D/manufacturing position [intel-government] | Policy funding buys equity; geographic scarcity is not commercial pricing power | Government-backed capacity cannot obtain profitable external demand |
| Technology and packaging | 18A-P risk production and 14A development progress [intel-q226-10q] | Customer qualification and rival technology routes remain real | Repeated design/slippage problems or uneconomic yields |

The filing attributes much of product ASP improvement to premium mix and less to demand-based pricing, partly offsetting input costs. [intel-q226-10q]
That is weaker evidence of durable like-for-like pricing power than a headline ASP increase suggests.
No measured churn, retention, customer migration cost or comparable good-die economics were retained; these moat claims remain hypotheses.
External foundry requires customer trust, tools, IP, process qualification and long design lead times, not simply available clean rooms. [INFERENCE]
A profitable internal product can coexist with an externally uncompetitive fab: its transfer price does not settle customer economics.
Over the observed five years the consolidated profit evidence supports a **narrowed**, not widened, advantage. [sa-financials]
Ten-year durability is uncertain: AMD can preserve software compatibility while AWS can migrate controlled workloads to custom Arm chips. [amd-q226], [aws-graviton5]
Customers and equipment/material suppliers may capture part of the productivity benefit rather than Intel equity holders.
Confidence: moderate that the product ecosystem has value; low that Foundry currently demonstrates durable third-party economic profit.

## Management

Assess stewardship through cash commitments and per-share outcomes, not share-price appreciation alone.

| Dated decision | Observed rationale/result | Stewardship test |
|---|---|---|
| 2025 government equity agreement | $8.9B funding through common equity, sourced partly from prior grant commitments [intel-government] | Funding resilience is bought with ownership transfer, not free operating profit |
| Q2 2026 Ireland SCIP buyout | $14.2B repurchase of Apollo's 49%; funded partly through debt [intel-q226-10q] | Requires future full-owner fab cash returns to justify expenditure |
| Q2 2026 commitment to complete 14A | Internal products planned; expansion pace tied to committed demand [intel-q226-10q] | Distinguish development commitment from signed profitable external orders |
| August 2026 common offering | $95 pricing and full option exercise, expanding common ownership claims [intel-offering], [intel-offering-pr] | Liquidity improvement must be evaluated per share, not only as gross capital raised |

Government's announced stake was **9.9% at that transaction**, not a verified current percentage after later issuances. [intel-government]
It is described as passive, without board representation or additional governance/information rights; it generally votes with the board, subject to exceptions.
A warrant becomes exercisable if Intel ceases to own at least **51%** of Foundry, constraining easy spin-out narratives. [intel-government], [intel-q226-10q]
The 10-Q quantifies up to **241M** warrant shares at **$20** and permits net cash or net share settlement; it is not automatically exercised today.
Lip-Bu Tan's equity-linked package and required **$25M** share purchase/holding provide alignment evidence, not proof of good allocation. [intel-proxy]
Annual long-term incentives use **60% PSUs / 40% options**; TSR-linked awards emphasize stock outcomes, not a direct permanent owner-earnings test. [intel-proxy]
The proxy also describes non-GAAP operating metrics in bonus targets; adjusted performance can differ materially from common-owner economics. [intel-proxy]
Tan-affiliated Walden funds and family connections appear in disclosed Intel Capital transactions; the Audit Committee reviewed/approved them. [intel-proxy]
Approval is process evidence, not independent proof of transaction fairness. Related-party allocation deserves continuing scrutiny without an unsupported misconduct allegation.
Management gives concrete ramp and demand statements, but yield improvement is not a disclosed independently comparable yield percentage. [intel-q226]
Succession and execution depend on engineering teams and customer qualification, not only CEO network access; a detailed succession assessment was not established.
Stewardship verdict: funding/execution flexibility improved, but large reinvestment, dilution and overlapping investment relationships require a higher diligence bar.

## Inversion

The strongest bear case is that improving product earnings fund an indefinitely subscale external foundry while investors prepay for distant successes.

| Failure mechanism | Timing / severity | Early warning | Mitigation and model treatment |
|---|---|---|---|
| 18A/14A good-die economics remain weak | Multi-year; potentially structural | Rising equipment spend without loss reduction | Demand-gated expansion helps; bear EPS decline, lower exit multiple |
| CPU-cycle demand mistaken for durable share gains | Next several quarters; material | Pricing/mix normalizes or competitors grow faster | Base case requires sustained per-share recovery, not annualizing one quarter |
| AMD or Arm displaces valuable workloads | Multi-year; structural | Better workloads migrate while Intel segment margins fade | Bull weight limited; no monopoly assumption |
| External commitments disappoint | Multi-year; severe for foundry thesis | Design evaluations produce no binding demand/pricing | No separate Apple/Terafab contract value assigned |
| Dilution outruns operating improvement | Continuing; material per share | New financing/escrow/award shares rise faster than earnings | EPS scenarios must be interpreted after dilution, not fixed-share enterprise growth |
| Cash reinvestment and partner obligations surprise | Immediate to multi-year; high | Financing-section payments and buyouts absorb reported OCF | FCF benchmark explicitly incomplete for owner earnings |
| Governance or policy terms become adverse | Discrete; potentially severe | Related-party terms weaken or government conditions constrain options | Unmodeled veto risk, not hidden in the hurdle rate |
| Supply, export or geopolitical disruption | Discrete; severe | Component shortages or market-access restrictions | Explicit unmodeled tails; no invented catastrophe probability |

Q2 escrow losses were **$12.5B**, with a **$15.6B** derivative liability at June 27; a rising stock price can worsen accounting results through this contract. [intel-q226-10q]
There were **143M** unreleased escrow shares; the filing separately reports rounded **71M** noncontingently issuable and **71M** contingently issuable components.
The rounded components are not an exact share-register reconciliation; no invented missing million is supplied.
Loss-period diluted EPS excludes otherwise antidilutive awards/contract shares; the Q2 denominator does not measure future profitable-period dilution. [intel-q226-10q]
A lower escrow mark-to-market loss would not establish better manufacturing returns; conversely the current mark is not ordinary operating expense.
Historical Intel earnings capacity provides context, not proof that the old industry position returns after factories, competition and share counts change.
Anchoring controls: old peak profits, the $104.70 stock price, government endorsement and sell-side targets are not valuation inputs establishing economic value.
Our three cases do not model bankruptcy, forced structural separation, integrity failure or geopolitical shutdown; the bear case is not the maximum loss.
Falsification of the bearish conclusion requires durable per-share cash earnings and profitable external demand, not only headlines or one strong quarter.

## Industry

Long-lived demand for computing productivity is plausible; the value-capture route is contested among CPU designers, foundries, hyperscalers and accelerator suppliers.
AI can increase CPU orchestration, inference and memory/networking needs, while also shifting spend toward accelerators and customers' own silicon.
Intel's Q2 DCAI growth and improved Products profit are evidence of participation, not proof of ownership of the entire AI value chain. [intel-q226]
AMD's Q2 revenue was **$11.536B**, GAAP gross margin **54%**, operating income **$1.990B**, and Data Center revenue **$6.7B**, up **107%**. [amd-q226]
AMD Data Center includes EPYC and Instinct GPUs: it is not a clean CPU-only market-share comparison with Intel DCAI.
AMD's growth demonstrates a strong competitor benefiting from the same demand wave, so Intel cannot assume industry growth equals proprietary share gains.
AWS made Graviton5 C9g/C9gd instances generally available in June, claiming up to **25%** more compute performance than prior Graviton4 C8g/C8gd. [aws-graviton5]
This is an AWS promotional generation-to-generation comparison, not independently benchmarked superiority over every Intel workload.
Still, actual availability establishes the Arm substitution route rather than a merely hypothetical challenger.
Intel reports component/substrate/memory constraints persisting into next year; stronger demand can still require cash-intensive supply expansion. [intel-q226-10q]
No numerical TAM is asserted: issuer-promoted AI opportunity is not evidence of Intel's serviceable external foundry revenue.
Reuters' October 7 report says Intel remains involved in Terafab, TSMC cooperation remains possible, and both chipmakers did not immediately comment. [reuters-terafab]
That report is Reuters hosted by The Star, not independent The Star reporting; it supplies no binding Intel volumes, wafer prices, capex split or profit terms.
Apple-related foundry claims in prior trial context are not confirmed by retained primary contracts; **no Apple optionality premium is separately priced**.
The same applies to Terafab: optional outcomes enter the qualitative bull narrative, never as reported contracted earnings.
The 10-Q distinguishes 14A evaluations by potential significant customers from actual committed demand. [intel-q226-10q]
Bounded drivers: bear assumes erosion despite demand; base requires a durable product recovery with narrowing foundry losses; bull requires successful profitable execution beyond internal qualification.
If competitors/hyperscalers capture the productivity gains and Intel's cash returns fail to improve, the civilization-level computing tailwind does not accrue to Intel shareholders.

## Valuation

`data/calculations.json` is generated by the native CLI from saved evidence, not hand-edited; every supported number below comes from its output.

| Native metric | Actual output / interpretation |
|---|---|
| Price × approximate shares | $553,455,220,931.40; not a reported market cap |
| Absolute cap deviation | 0.0000003991858417 as a fraction; tiny versus canonical Yahoo cap, without curing share uncertainty |
| FY2025 free cash flow | −$4,949,000,000; annual OCF less investing-section capex |
| Historical FCF yield | −0.8942%; FY2025 FCF / October quote capitalization, not current earnings yield |
| GAAP P/E | null because FY2025 diluted EPS is negative |

Positive EPS anchor: **$1.52 FY2026 non-GAAP adjusted analyst consensus**, observed October 11 on StockAnalysis. [sa-forecast]
Its publisher explicitly labels EPS/forward PE adjusted, compares FY2025 with **$0.42**, and shows **$2.08** next-year EPS.
The same forecast table shows negative FY2026 net income; using positive adjusted EPS must never imply positive reported GAAP earnings.
We deliberately do not use GAAP −$0.06 or TTM publisher EPS discrepancies as a positive earnings basis.
The model configures **five EPS compounding steps** from FY2026 adjusted EPS and assumes a **five-year holding/discount period**. A fiscal progression suggests FY2031 earnings, not a verified FY2031 price date; treating the forecast as initial earning capacity and aligning it to an exit remain unverified run-rate/timing conventions.
Current risk-free reference: **5.24% 10-year Treasury par yield, October 9**, converted to **0.0524**. [treasury-20261009]
The **12%** required return is our explicit nominal USD equity assumption, above Treasury; it is not a replacement market-rate observation.
It expresses equity opportunity cost. Business execution risks appear in the cases; discrete governance/geopolitical tails remain outside them.

| Case | EPS CAGR assumption / exit multiple / probability | Conditional terminal price | Price-only CAGR (%) | Discounted present target at 12% |
|---|---|---:|---:|---:|
| Bear | −5% / 15× / 35% | $17.64 | −29.9640% | $10.01 |
| Base | +20% / 22× / 45% | $83.21 | −4.4908% | $47.22 |
| Bull | +35% / 30× / 20% | $204.47 | +14.3240% | $116.02 |
Dollar displays round saved native outputs to cents; price CAGR converts saved `annualized_return` fractions to percent and rounds to four decimals. It is `(terminal price / $104.70)^(1/5) − 1`, not historical YoY growth, assumed EPS CAGR or a prediction of each intervening year's stock return.

Bear: flat-to-eroding economic competitiveness overwhelms the current rebound; 15× is already a positive-earnings survivor assumption, not liquidation value.
Base: +20% per-share growth assumes meaningful operational recovery, a narrower foundry burden and continuing product profitability; it is demanding relative to the five-year history.
Its 22× exit assigns growth-franchise value but restrains premium pricing for capital intensity and competition.
Bull: +35% sustained EPS growth requires successful process/customer execution and product demand capture with dilution absorbed in per-share earnings.
A 30× exit is deliberately generous for a durable growth outcome; it is not supported merely by a peer's current quoted multiple.
Probabilities **35%/45%/20%** are subjective research weights, not measured frequencies: evidence supports recovery but not profitable external foundry certainty.
The CLI's weighted present target is **$47.96** (rounded); the $104.70 quote offers no safety margin under these assumptions.
Only the generous bull case exceeds the quote after applying the required-return hurdle; a much higher bull weight or better EPS economics could reverse the assessment.
This sensitivity is conceptual, not a separately calculated or audited alternate target. The conclusion is therefore conditional, not a universal upper bound.
No separate capital value is added for government backing, Apple, Terafab, factories or packaging, avoiding double counting them against the same assumed EPS recovery.
This is an **earnings-multiple terminal-price model**, not a full DCF, owner-earnings valuation, guaranteed IRR or total-return forecast.
It excludes dividends, interim cash distributions, financing transactions and explicit share paths; EPS growth must absorb economic dilution for results to apply.
Adjusted EPS excludes real owner costs such as stock compensation; weak cash conversion or ongoing capex can make even this model too generous.

## Decision

**Research conclusion: avoid at the observed price for a conservative new-purchase thesis; watch the operating turnaround for evidence, not an execution instruction.**
The product franchise is real and Q2 recovery is material, but a product recovery is not the same as a proved attractive combined product-plus-foundry investment.
The conditional benchmark falls far below $104.70 despite substantial base-case growth and a generous bull case.

| Lens | Conclusion / confidence | Observation that could change it |
|---|---|---|
| Duan: business | Products understandable; foundry/customer economics unproved / moderate | Durable independently priced profitable customer demand |
| Buffett: durability | Ecosystem valuable but contested / moderate-low | Sustained cash pricing power through competitor cycles |
| Duan/Buffett: stewardship | Financing flexibility, dilution and governance mixed / moderate | Transparent high-return reinvestment and improving per-share owner cash flow |
| Munger: inversion | Large execution and optionality risks / high confidence in risk existence | External commitments, cost evidence and loss narrowing remove failure mechanisms |
| Li Lu: structural demand | Computing opportunity strong, value capture uncertain / moderate | Intel captures rising productivity value rather than funding others' gains |
| Price | Unattractive under stated model / conditional | Better per-share cash economics or materially lower price |

Review after **October 29, 2026** Q3 results, scheduled after market close; no future results were assumed. [intel-q3-date]
Review triggers: new actual shares, offering cash/proceeds and post-offering liquidity; first-half-to-Q3 cash-flow/capex continuity; foundry losses and real external demand.
Additional triggers: signed customer economics, commercial yield/cost evidence, dilution reconciliation, AMD/Arm adoption and governance disclosures.
Thesis breakers include persistent capital spending without acceptable cash returns, repeat process misses, material integrity concerns or loss of economically valuable product demand.
Five-year ownership would need evidence of engineering/customer economics and financing resilience; abundant news coverage and a spreadsheet are insufficient.
Research confidence is high for the retained canonical statement/quote observations, lower for current capitalization precision, and low for future manufacturing/customer outcomes.
No validated target, portfolio sizing, brokerage action or orders follow from this provisional report.

## Limitations and audit

All canonical materials remain here: [data/evidence.json](data/evidence.json), [data/calculations.json](data/calculations.json), this report and [data/audit.json](data/audit.json).
The native audit is offline schema/citation/arithmetic consistency, not a fresh web audit, issuer-accounting certification, recommendation or authorization to trade.
Current shares remain **estimated**, using a rounded July filing count and the offering/option; there is no invented reported October 9 actual share count.
The StockAnalysis/Yahoo cap difference is disclosed and retained within tolerance; exact security/time/share synchronization is not proven.
Nine required reported facts have two distinct publisher observations; share estimation remains the expected provisional finding rather than being disguised as a verified reported fact.
Other limitations: independently audited yields, customer contract economics, maintenance capex, future dilution and current post-offering balance-sheet cash were not established.
Older historical years have less primary-document corroboration; standardized margins, TTM EPS and aggregate investment balances are not silently treated as equivalent GAAP facts.
The government agreement and escrow derivative introduce legal/economic complexities the simple positive adjusted EPS model cannot fully represent.
Date/return audit limitation: numerical consistency cannot certify calendar alignment. The five-year holding-period comparison is conditional, and the FY2026 adjusted anchor is not independently established as current normalized earning capacity; see the [batch return audit](../../../batches/2026-10-11/return-audit.md).
SEC reads previously returned index/403 results; direct Yahoo/fiscal reads returned short fetch errors. Successful issuer PDF/browser routes were recovered instead, without fabricating those failures into observations.
The old trial's stale-default risk-free diagnostic was not used. This model retains the real October 9 Treasury rate and a separately justified higher hurdle.
The source investigation did not run builds, tests, linters or formatters. Current layout migration and integration checks are recorded in [batch verification](../../../batches/2026-10-11/verification.json).
Historical execution before the ticker-namespace cutover recalculated the optimized package successfully; its old paths are historical only. The current recipe is `uv run --python 3.12 python skills/equity-investment-research/scripts/research.py calculate docs/research/tickers/INTC/2026-10-11/data/evidence.json --output docs/research/tickers/INTC/2026-10-11/data/calculations.json`.
The corresponding historical audit returned **PROVISIONAL**, exit code **1**, before this date/return review. The current recipe is `uv run --python 3.12 python skills/equity-investment-research/scripts/research.py audit docs/research/tickers/INTC/2026-10-11 --output docs/research/tickers/INTC/2026-10-11/data/audit.json`; the earlier findings included two warnings:
- `required fact shares: estimate, not verified reported data`
- `fact process_yield: unavailable`
No BLOCKED errors were reported in that earlier audit; it did not certify the model calendar. Consult `data/audit.json` for saved machine findings. This report review did not execute a new native audit.

### Retained source ledger

The source IDs cited above link directly to the observed document publishers; complete excerpts, dates, units and fact observations are retained in `data/evidence.json`.
[sa-quote]: https://stockanalysis.com/stocks/intc/ "StockAnalysis quote and capitalization"
[yahoo-quote]: https://finance.yahoo.com/quote/INTC/ "Yahoo actual recovered browser quote"
[intel-fy25]: https://www.intc.com/news-events/press-releases/detail/1759/intel-reports-fourth-quarter-and-full-year-2025-financial-results "Intel FY2025 results and cash flows"
[sa-financials]: https://stockanalysis.com/stocks/intc/financials/ "StockAnalysis independent financial normalization"
[intel-q226]: https://www.intc.com/news-events/press-releases/detail/1776/intel-reports-second-quarter-2026-financial-results "Intel Q2 FY2026 results"
[intel-q226-10q]: https://www.intc.com/filings-reports/all-sec-filings/content/0000050863-26-000157/0000050863-26-000157.pdf "Intel 10-Q PDF; same publisher as Intel IR"
[sa-balance]: https://stockanalysis.com/stocks/intc/financials/balance-sheet/ "StockAnalysis cash debt leases and shares"
[sa-forecast]: https://stockanalysis.com/stocks/intc/forecast/ "Adjusted analyst forecast, not reported GAAP"
[intel-proxy]: https://d1io3yog0oux5.cloudfront.net/_a0dbd358c0dfe27d139bef6d4198de40/intel/db/888/9249/file/INTC_PXY_2026_+ADA.pdf "Intel proxy compensation and related parties"
[intel-government]: https://www.intc.com/news-events/press-releases/detail/1748/intel-and-trump-administration-reach-historic-agreement-to "Government equity agreement"
[intel-offering]: https://www.intc.com/filings-reports/all-sec-filings/content/0001193125-26-346806/d117670d8k.htm "Intel August 12 8-K actual browser observation"
[intel-offering-pr]: https://www.intel.com/content/www/us/en/newsroom/news/corporate/intel-announces-upsize-and-pricing-of-20-billion-common-stock-offering.html "Offering pricing and expected closing"
[amd-q226]: https://ir.amd.com/news-events/press-releases/detail/1295/amd-reports-second-quarter-2026-financial-results "AMD competitor results"
[aws-graviton5]: https://aws.amazon.com/about-aws/whats-new/2026/06/ec2-c9g-c9gd-instances-graviton5-processors-available/ "AWS Graviton5 availability and promoted performance"
[reuters-terafab]: https://www.thestar.com.my/tech/tech-news/2026/10/07/intel-to-keep-working-on-musk039s-terafab-chipmaking-venture-bloomberg-news-reports "Reuters syndicated by The Star"
[intel-q3-date]: https://www.intc.com/news-events/press-releases/detail/1782/intel-to-report-third-quarter-2026-financial-results "Intel next earnings date"
[treasury-20261009]: https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_yield_curve&field_tdr_date_value_month=202610 "Observed October 9 10-year par yield"
