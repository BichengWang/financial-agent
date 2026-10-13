# Invesco QQQ ETF (Nasdaq: QQQ): Nasdaq growth exposure, not innovation at any price

[Research index](../../../index.md#2026-10-11) · [Run guidance](../../../README.md) · [Evidence](data/evidence.json) · [Calculations](data/calculations.json) · [Audit](data/audit.json)

As of 2026-10-11. USD exchange-traded fund units; no ADR conversion. Research stance: **watchlist; fund-specific diligence, no validated target or allocation approval**. This is conditional research, not an order or investment guarantee.

## Grounding

### Security, dates and source quality
Invesco QQQ ETF trades on Nasdaq as QQQ in USD. The actual latest observed regular-session close is **$751.27 per fund unit at 2026-10-09 16:00 EDT**, timestamp `2026-10-09T16:00:00-04:00` [sa-quote]. No after-hours observation, NAV or analyst target substitutes for that price. The current canonical price does not have two precisely dated publisher observations; this remains an explicit evidence gap.

Information richness is **A for mandate/fund implementation, B for independent precisely dated fund-metric corroboration**. Sponsor pages/documents are primary evidence; two sponsor URLs are one publisher. The independent price publisher is Stock Analysis. Abundant promotional performance material is not evidence of future economic resilience. AI text retrieval and interpretation can misread dates/definitions; retained excerpts enable reconstruction, not a claim of exhaustive document review.

### Dated fund facts
| Fact | Value / units | Period and basis | Source |
|---|---:|---|---|
| Market price |$751.27 USD/fund unit |October 9 regular close |[sa-quote] |
| Actual fund units |673,650,000 units |2026-10-09 |[fund-api] |
| NAV |$751.231311 USD/fund unit |2026-10-09; net assets per unit, not quote |[fund-api] |
| Fund net assets/AUM |$506,066,972,518.96 USD |2026-10-09; **not quoted corporate capitalization** |[fund-api] |
| Annual expense ratio |0.18% |Current observed sponsor/prospectus basis |[fund-api] |
| Corporate revenue, net income, OCF, capex, cash, debt, EPS |N/A |Not comparable operating-company facts; precise reasons in evidence |[data/evidence.json] |
| Reported corporate market capitalization |N/A |AUM cannot satisfy corporate cap definition |[data/evidence.json] |

All ten required native keys remain present. Investment income, portfolio purchases, cash allocations, Treasury assets andNAV changes are not silently recast as corporate revenue, capex, liquidity, debt orEPS. Corporate five-year financial-history requests are intentionally inapplicable, not replaced by invented fund earnings. The native tool can multiply price by fund units, but that arithmetic does not verify current units or sourced market capitalization.

## Business

### Purchased service and portfolio economics
Investors pay an annual 0.18% expense ratio for a tradable Nasdaq-100 portfolio rather than replicating its securities and index changes. Nasdaq's primary methodology describes a modified-market-cap index of large Nasdaq-listed non-financial companies, not an unconstrained innovation picker. The fund and index rebalance quarterly and reconstitute annually [sponsor].

The October 9 sponsor API reports NAV$751.231311, net assets$506,066,972,518.96 and 673,650,000 fund units [fund-api]. Its field `marketValue` equals net assets and is not evidence of quoted-unit market capitalization. The sponsor holdings API includes common stock, ADRs, index futures and cash/contra-futures; not every row is a company [holdings-api].

Underlying earnings derive from chips, software, platforms, commerce and other included businesses. [INFERENCE] Growth can accrue to suppliers or consumers and be offset by heavy reinvestment; being listed on Nasdaq is not a quality screen. No fund corporate revenue trend is fabricated. The semiannual statement reports$940,885,102 net investment income and$997,771,988 distributions for six months ended March 31,2026, distinct from corporate net income or revenue [semiannual].

## Moat

| Candidate advantage | Evidence | Counterevidence / falsifier |
|---|---|---|
| Liquid established wrapper | March 10,1999 inception; sponsor API 30-day average volume 34,271,377 units [fund-api] | Historical volume cannot guarantee exit depth; other wrappers can track the same index |
| Exposure to scalable franchises | October 9 NVDA 8.250119%, AAPL 7.335376%, MSFT 5.93204% [holdings-api] | Underlying moats do not create ETF pricing power or protect a high entry multiple |
| Rules-based concentration controls | Modified market capitalization weighting [index-methodology] | Caps constrain weights at specified index events, not an equal-weight or permanent ceiling guarantee |

The September 30 sector API reports technology 68.008948%, consumer discretionary 15.137549% and telecommunications 5.913605% [sectors-api]. Its classification is not SPY's GICS basis. [INFERENCE] QQQ has durable utility as concentrated growth exposure, not as a risk-free compounding franchise. Switching wrappers is easy; shareholder value is tied to underlying businesses rather than Invesco shareholder profits. Falsifiers include structural earnings erosion among leaders and long-run tracking slippage beyond explainable costs.

## Management

### Governance changed; do not recycle the old UIT story
The March 31,2026 report states that classification changed from a unit investment trust to an open-end management investment company after the December 19,2025 close. Invesco Capital Management LLC is adviser, and the new agreement sets a 0.18% unitary management fee; most service expenses are paid from it, but specified transaction/tax/extraordinary costs remain outside it [semiannual].

| Decision | Observed result | Stewardship implication |
|---|---|---|
| Conversion approved December 19,2025 | New board/advisory arrangement; objective unchanged [semiannual] | Governance structure changed, not the Nasdaq-100 investment thesis |
| Fee convention changed |0.18% unitary fee versus prior 0.20% operating-expense cap [semiannual] | Assess actual net costs; historical fee data should not be silently overwritten |
| Distributions and tax treatment | Quarterly net investment-income dividends, generally annual realized taxable capital-gain distributions [semiannual] | Yield/distribution policy is not fixed cash interest |

Creations/redemptions at NAV through authorized participants are not corporate buybacks; retail holders trade in the secondary market [semiannual]. [INFERENCE] Institution-level continuity reduces single-manager dependence, but index rules, custody and AP capacity remain operational dependencies. Sponsor marketing ranks and historical outperformance are not independent proof of future value.

## Inversion

| Risk | Mechanism / severity | Review trigger |
|---|---|---|
| Technology and growth-duration concentration | Higher discount rates or weak monetization can compress many holdings simultaneously | Earnings/cash conversion at leading issuers, not just fund inflows |
| Listing/index selection bias | Large non-financial Nasdaq businesses omit banks and many competing companies | Changing leadership outside the eligible universe |
| Index and AP constraints | Rebalances/forced changes plus market disruption can impair tracking or widen discounts | Persistent tracking divergence and impaired contemporaneous liquidity |
| Holdings-data ambiguity | Different inclusion dates or ancillary-line counts can misstate apparent diversification | Reconcile sponsor count definitions before issuer-level aggregation |

The fund is non-diversified and sponsor warns of greater volatility and foreign-issuer risks [sponsor]. The holdings API reports 106 rows/count versus 102 in fundDetails and 103 on the independent overview; definitions/dates are not fully reconciled [holdings-api, fund-api, sa-overview]. Keep this visible, not silently declare 102 operating businesses. [INFERENCE] The informed bear case is that the innovation narrative is already paid for while margins/cash conversion disappoint; it does not require innovation to stop. No invented tail probability is used.

## Industry

[INFERENCE] QQQ participates in digital productivity and platform scale through its selected businesses; it does not represent the entire US economy or all scientific innovation. Semiconductor cyclicality, AI hardware spending, enterprise software budgets, advertising and consumer demand remain distinct drivers. The September 30 sector weights and October 9 top holdings show a heavily technology-linked exposure [sectors-api, holdings-api].

Nasdaq permits eligible multiple share classes and ADRs, excludes financial-industry companies/REITs, and employs modified listed-share market capitalizations with low-float limits. Annual selection ranks and quarterly rules can retain or add companies; fast-entry rules can temporarily take the index above 100 [index-methodology]. Consequently 100 in the name is a methodology objective, not proof of exactly 100 contemporaneous securities. Alternatives are broad-market, different growth or same-index funds; no unsourced competitor price/fee claims are substituted for diligence.

## Valuation

### Fund NAV comparison
Observed October 9 market close$751.27 is not the independently observed sponsor NAV$751.231311; the two quantities are close, but no native premium/discount computation is provided [sa-quote, fund-api]. The API `marketValue` is not market price and cannot be used as capitalization. A same-date premium should be judged with executable bid/ask, fair-valued holdings and creation liquidity, not NAV alone.

Independent vendor P/E 29.62 is an undated overview portfolio statistic, not QQQ GAAP diluted EPS and not native-tool verified [sa-overview]. The sponsor raw holdings and NAV are more useful than fabricating a composite EPS target. Underlying margins, reinvestment and multiples matter economically; distributions must be included for total returns and personal tax results vary [semiannual].

### Actual native calculation output
`calculate` exited **0** and generated `data/calculations.json`.

| Native key | Actual output | Interpretation |
|---|---:|---|
| `implied_market_cap` |$506,093,035,500.00 USD |Price times fund units only |
| `market_cap_deviation` |null |No comparable reported corporate capitalization |
| `free_cash_flow` |null |Operating-company OCF/capex inapplicable |
| `free_cash_flow_yield` |null |No corporate FCF or reported corporate cap |
| `pe` |null |No corporate GAAP dilutedEPS |
| `valuation` |null |Corporate EPS forecast model intentionally omitted |

Shares and price both refer to October 9; the product measures quoted-unit value arithmetically, not an independently reported corporate cap. No earnings-multiple forecast, terminal share-price target, CAGR or guaranteed return is asserted.

## Decision

**Watchlist as concentrated Nasdaq-100 exposure, not a substitute for a diversified equity core without overlap review.** Confidence is high on observed fee/NAV/units and index mandate, medium on holdings-count reconciliation, and low on any point expected return. NVIDIA, Apple, Microsoft and Micron lead the sponsor October 9 list; those exposures overlap substantially with broad-market/semiconductor holdings [holdings-api].

Review triggers: changed methodology or mandate, unexplained tracking error, sustained trading discounts, increased concentration and weakening underlying earnings/cash generation. Break the investment case if the fund no longer reliably implements the intended exposure or the investor cannot tolerate growth-sector drawdowns. Five-year market closure tests the underlying enterprises, not the liquidity ranking. No sponsor slogan or historical rank proves an adequate margin of safety.

## Limitations and audit

Latest October 9 market close has one precisely dated publisher; Yahoo historical access returnedHTTP 429. Sponsor October 9 units agree numerically with vendor 673.65 million, but the vendor does not separately date its units field, so it is not asserted as independent same-period corroboration. Sponsor count 102 versus holdings 106 and vendor 103 requires definition/date reconciliation. The March 31 semiannual PDF shows marketprice$966.18 versusNAV$577.44 alongside similar NAV/market returns: this anomalous historical market-price observation is retained but **not accepted as canonical quote or explained by an invented split/FX correction**. The US factsheet request returned HTML country selection instead ofPDF; US/HK product details were role-selection bodies. Actual browser-observed API URLs recovered current fund data; no client scaffold is retained. Sponsor fee 0.18% is current; older HK promotional 0.20% data is a different vintage, not a same-period corroboration.

Corporate facts remain explicit N/A for their ETF-specific definitions; the EPS valuation configuration is deliberately absent. Thus a completed fund analysis can remain **PROVISIONAL under a corporate-oriented native evidence policy**, without being an unfinished company-model placeholder. Fund-specific optional facts have supported units/periods, but largely one primary publisher. No forecast, target, CAGR, FCF or bond repricing result is represented as native-verified. Personal taxes, execution cost, distributions and unmodeled tails preclude translating a qualitative watchlist stance into a guaranteed return.

The native audit checks the exact saved report, evidence and calculation consistency. It does not fetch independent sources, validate sponsor data truth, certify index economics or approve an investment. Actual CLI outcome: **PROVISIONAL, exit 1**, saved in `data/audit.json`. It reports 19 warnings: price and shares require two publisher observations; eight required corporate definitions are unavailable (each with fact and required-fact warnings); valuation is intentionally omitted. There are no error-severity findings. Calculate exited 0; the uv dependency-field deprecation warning is unrelated to research arithmetic.

### Retained source trail
- [hk-overview](https://www.invesco.com/hk/en/etf/qqq.html): Invesco; March 2026-vintage Hong Kong overview. Retained historical 0.20% ongoing-charge disclosure is not the canonical current US fee.
- [index-methodology](https://indexes.nasdaq.com/docs/Methodology_NDX.pdf): Nasdaq; Nasdaq-100 index methodology, copyright 2026. Relevant observed text retained in `data/evidence.json`; access date 2026-10-11.
- [sponsor](https://www.invesco.com/qqq-etf/en/about.html): Invesco; Holdings & Sector Allocations of Invesco QQQ. Relevant observed text retained in `data/evidence.json`; access date 2026-10-11.
- [fund-api](https://dng-api.invesco.com/cache/v 1/accounts/en_US/shareclasses/QQQ?idType=ticker&variationType=fundDetails&productType=ETF): Invesco; QQQ observed sponsor fundDetails API. Relevant observed text retained in `data/evidence.json`; access date 2026-10-11.
- [holdings-api](https://dng-api.invesco.com/cache/v 1/accounts/en_US/shareclasses/QQQ/holdings/fund?idType=ticker&interval=monthly&productType=ETF): Invesco; QQQ sponsor holdings API selected observed fields. Relevant observed text retained in `data/evidence.json`; access date 2026-10-11.
- [sectors-api](https://dng-api.invesco.com/cache/v 1/accounts/en_US/shareclasses/QQQ/weightedHoldings/fund?idType=ticker&productType=ETF&breakdown=sector): Invesco; QQQ sponsor sector API. Relevant observed text retained in `data/evidence.json`; access date 2026-10-11.
- [semiannual](https://www.invesco.com/content/dam/invesco/hk/en/pdf/qqq-semi-annual-report-en.pdf): Invesco; QQQ March 31 2026 semiannual financial statements. Relevant observed text retained in `data/evidence.json`; access date 2026-10-11.
- [sa-quote](https://stockanalysis.com/etf/qqq/history/): Stock Analysis; QQQ historical prices. Relevant observed text retained in `data/evidence.json`; access date 2026-10-11.
- [sa-overview](https://stockanalysis.com/etf/qqq/): Stock Analysis; QQQ independent overview. Relevant observed text retained in `data/evidence.json`; access date 2026-10-11.

Failed access and attempted alternatives are retained in `source_access_attempts`; an unavailable page is not cited as a successful observation.
