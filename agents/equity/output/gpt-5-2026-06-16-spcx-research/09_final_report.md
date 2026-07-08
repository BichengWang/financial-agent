# SPCX One-Month Scenario Research - 2026-06-16

```text
QUANTITATIVE SINGLE-NAME REVIEW - SPCX
Run Status: REVIEW_ONLY
Classification: INTERNAL - INVESTMENT COMMITTEE USE
```

## Executive Summary

SPCX now refers to Space Exploration Technologies Corp. Class A common stock, not the former Tuttle SPAC ETF ticker. The latest grounded anchor used here is Nasdaq delayed data for `2026-06-15`: `SPCX $192.50`, cross-checked against a reported close of `$192.45`. One-month target date is `2026-07-15`. My scenario-weighted one-month price estimate is about `$187`, with a rough central scenario band of `$135-$240`; that is a slightly negative expected return from the anchor with unusually large upside and downside tails. Status is `REVIEW_ONLY`, not `GO`, because SPCX has only two trading sessions and cannot satisfy the referenced system's 60-trading-day history, beta, realized-volatility, and event-calendar gates.

## Price Anchor And Data Quality

| Item | Value |
|---|---:|
| Anchor price | `$192.50` |
| Anchor date | `2026-06-15` |
| Cross-check | `$192.45`, within `0.03%` |
| IPO price | `$135.00` |
| First-day close | `$160.95` |
| Monday volume | `256.2M` shares |
| Data mode | `DELAYED_PARTIAL` |
| Formal recommendation status | `REVIEW_ONLY / no formal GO` |

Nasdaq's public page identifies SPCX as "Space Exploration Technologies Corp. Class A Common Stock"; the page itself shows delayed-data disclaimers and public-page data availability gaps, so I used the Nasdaq quote endpoint as the primary delayed quote source and external news reports as the cross-check.

## One-Month Scenario Tree

| Scenario | Probability | 2026-07-15 price range | Midpoint | Return vs `$192.50` | Main conditions |
|---|---:|---:|---:|---:|---|
| Extreme momentum / squeeze | 12% | `$250-$290` | `$270` | `+40%` | Float scarcity persists, retail/ETF demand stays dominant, broad beta remains risk-on. |
| Bull continuation | 18% | `$215-$245` | `$230` | `+19%` | IPO premium holds, greenshoe news and index/speculative demand offset valuation pushback. |
| Base consolidation | 35% | `$175-$205` | `$190` | `-1%` | No new supply shock before July; investors digest valuation near Monday close. |
| Bear repricing | 25% | `$130-$165` | `$148` | `-23%` | Stock retests first close/IPO range as valuation and profitability concerns dominate. |
| Stress / fundamental reset | 10% | `$80-$120` | `$100` | `-48%` | Analyst target/fair-value debate becomes the price anchor; broad mega-cap risk-off. |

Scenario-weighted expected price: about `$187`, or `-2.8%` from the `$192.50` anchor. The distribution is not normal: the upside can be violent because float is scarce, but the downside tail is larger because the stock is trading far above valuation anchors.

## Why The Setup Is So Wide

1. Float scarcity supports near-term momentum. Business Insider reported that only about `4.3%` of shares are publicly tradable and that the first time-based lockup release is `70` days after the IPO. That keeps forced insider supply mostly outside the one-month window, though any earnings-linked release terms still need a verified company calendar.
2. The IPO capital story is real. MarketWatch reported proceeds rose to more than `$85.7B` after the underwriters fully exercised the greenshoe option for `83.3M` additional shares.
3. Valuation pressure is severe. At the IPO price, MarketWatch cited a trailing price/sales ratio of `93.2x`; at `$192.50`, the same basis implies about `132.9x`. That leaves little room for execution disappointment.
4. Fundamentals are not yet supporting the market cap. Filing-based reporting cited `2025 revenue of $18.7B` and a `2025 net loss of $4.9B`, with Starlink as the major revenue engine.
5. Independent valuation anchors are much lower. The NY Post reported CFRA at a `sell` rating with a `$115` 12-month target and Morningstar's value estimate at `$63`. Those are not one-month targets, but they define the stress tail if momentum breaks.

## Trading View

I would not classify SPCX as a clean one-month long at `$192.50` under the referenced system. The short-term tape can still squeeze, but the expected-value setup is not attractive enough to offset missing history, missing verified event calendar, and very high valuation. For a long-biased trade, the risk/reward improves materially closer to `$150-$165`, where the first-day close becomes support and upside to `$215-$245` is less asymmetric. A breakout above `$205` can trade toward `$230-$245`, but that is momentum exposure, not valuation support.

## Watch List For Next Update

- Verified first earnings date and whether any earnings-linked lockup release can occur before late August.
- Nasdaq option chain / IV30 once reliably populated.
- Any index-inclusion timing for Nasdaq-100 or other passive flows.
- Follow-through volume: if volume falls sharply while price fails above `$205`, the bear-repricing probability rises.
- News on AI/data-center contract revenue conversion, capex pace, and Starlink profitability.

## Limitations

This is not financial advice. This is a research note using public delayed data and reported filing details. The scenario distribution is intentionally wide because SPCX lacks enough public history for beta, correlation, drawdown, and realized-volatility estimation.

