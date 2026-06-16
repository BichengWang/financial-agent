# SPCX Source Ledger - 2026-06-16

Retrieval timestamp for shell-fetched Nasdaq quote rows: `2026-06-15 22:03:47 PDT`.

| artifact | field | ticker/entity | value | unit | observation_date | source | freshness_tag | claim_type | used_by |
|---|---|---:|---:|---|---|---|---|---|---|
| 09 | company / listing | SPCX | Space Exploration Technologies Corp. Class A Common Stock; Nasdaq-listed | text | 2026-06-15 | https://www.nasdaq.com/market-activity/stocks/spcx | DELAYED | OBSERVED | 09 |
| 09 | anchor price | SPCX | 192.50 | USD/share | 2026-06-15 | https://api.nasdaq.com/api/quote/SPCX/info?assetclass=stocks | DELAYED | OBSERVED | 09, 15 |
| 09 | anchor price cross-check | SPCX | 192.45 | USD/share | 2026-06-15 | https://nypost.com/2026/06/15/business/spacex-shares-jump-20-in-first-full-day-of-trading-after-historic-ipo/ | HISTORICAL | OBSERVED | 09 |
| 09 | price-source agreement | SPCX | 0.03 | percent difference | 2026-06-15 | formula: abs(192.50/192.45-1) | DELAYED | DERIVED | 09 |
| 09 | Monday trading volume | SPCX | 256227963 | shares | 2026-06-15 | https://api.nasdaq.com/api/quote/SPCX/info?assetclass=stocks | DELAYED | OBSERVED | 09 |
| 09 | IPO price | SPCX | 135.00 | USD/share | 2026-06-11 | https://www.marketwatch.com/livecoverage/spacex-ipo-stock-price-trading-elon-musk-spcx/card/spacex-has-officially-priced-its-ipo-setting-it-up-to-trade-friday-vajhiPzegDDS3uFoCLco | HISTORICAL | OBSERVED | 09 |
| 09 | Friday close | SPCX | 160.95 | USD/share | 2026-06-12 | https://www.businessinsider.com/spacex-ipo-live-updates-pricing-spcx-stock-2026-6 | HISTORICAL | OBSERVED | 09 |
| 09 | Monday return vs Friday close | SPCX | 19.6 | percent | 2026-06-15 | Nasdaq quote endpoint; formula: 192.50/160.95-1 | DELAYED | DERIVED | 09 |
| 09 | IPO proceeds after greenshoe | SPCX | 85.7 | USD billions | 2026-06-15 | https://www.marketwatch.com/story/spacexs-stock-jumps-as-the-company-reveals-its-ipo-has-raised-another-10-7-billion-fc7eaca1 | HISTORICAL | OBSERVED | 09 |
| 09 | underwriter option shares | SPCX | 83.3 | million shares | 2026-06-15 | https://www.marketwatch.com/story/spacexs-stock-jumps-as-the-company-reveals-its-ipo-has-raised-another-10-7-billion-fc7eaca1 | HISTORICAL | OBSERVED | 09 |
| 09 | public float | SPCX | 4.3 | percent of shares | 2026-06-15 | https://www.businessinsider.com/spacex-ipo-spcx-stock-lockup-period-expire-nasdaq-elon-musk-2026-6 | HISTORICAL | OBSERVED | 09 |
| 09 | Musk locked stake | SPCX | 42 | percent stake | 2026-06-15 | https://www.businessinsider.com/spacex-ipo-spcx-stock-lockup-period-expire-nasdaq-elon-musk-2026-6 | HISTORICAL | OBSERVED | 09 |
| 09 | first time-based lockup release | SPCX | 70 | days after IPO | 2026-06-15 | https://www.businessinsider.com/spacex-ipo-spcx-stock-lockup-period-expire-nasdaq-elon-musk-2026-6 | HISTORICAL | OBSERVED | 09 |
| 09 | 2025 revenue | SPCX | 18.7 | USD billions | 2025-12-31 | https://www.businessinsider.com/spacex-ipo-s1-public-filing-2026-5 | OFFICIAL_FILING | OBSERVED | 09 |
| 09 | 2025 net loss | SPCX | 4.9 | USD billions | 2025-12-31 | https://www.businessinsider.com/spacex-ipo-s1-public-filing-2026-5 | OFFICIAL_FILING | OBSERVED | 09 |
| 09 | 2025 Starlink revenue | SPCX | 11.39 | USD billions | 2025-12-31 | https://www.businessinsider.com/spacex-ipo-s1-public-filing-2026-5 | OFFICIAL_FILING | OBSERVED | 09 |
| 09 | IPO price-to-sales | SPCX | 93.2 | x | 2026-06-12 | https://www.marketwatch.com/livecoverage/spacex-ipo-stock-price-trading-elon-musk-spcx/card/spacex-revenue-has-to-soar-or-the-stock-has-to-drop-for-this-investor-to-get-bullish-XWf1OOexLaD1L7lYE9IY | HISTORICAL | OBSERVED | 09 |
| 09 | anchor price-to-sales | SPCX | 132.9 | x | 2026-06-15 | formula: 93.2 * 192.50 / 135.00 | DELAYED | DERIVED | 09 |
| 09 | analyst bear target | SPCX | 115 | USD/share | 2026-06-15 | https://nypost.com/2026/06/15/business/spacex-shares-jump-20-in-first-full-day-of-trading-after-historic-ipo/ | HISTORICAL | OBSERVED | 09 |
| 09 | Morningstar value estimate | SPCX | 63 | USD/share | 2026-06-15 | https://nypost.com/2026/06/15/business/spacex-shares-jump-20-in-first-full-day-of-trading-after-historic-ipo/ | HISTORICAL | OBSERVED | 09 |
| 09 | ticker transfer context | SPCX | Tuttle SPAC & New Issue ETF changed from SPCX to SPCK in April; SpaceX acquired SPCX ticker | text | 2026-06-04 | https://www.marketwatch.com/story/elon-musks-spacex-paid-to-secure-its-ticker-symbol-ahead-of-blockbuster-ipo-61a57e6b | HISTORICAL | OBSERVED | 09 |
| 09 | SPY price | SPY | 754.83 | USD/share | 2026-06-15 | https://api.nasdaq.com/api/quote/SPY/info?assetclass=etf | DELAYED | OBSERVED | 09 |
| 09 | QQQ price | QQQ | 744.00 | USD/share | 2026-06-15 | https://api.nasdaq.com/api/quote/QQQ/info?assetclass=etf | DELAYED | OBSERVED | 09 |
| 09 | SOXX price | SOXX | 628.45 | USD/share | 2026-06-15 | https://api.nasdaq.com/api/quote/SOXX/info?assetclass=etf | DELAYED | OBSERVED | 09 |

