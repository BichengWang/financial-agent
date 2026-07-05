# 08 Risk Review

## Committee Decision

`APPROVE` for `REVIEW_ONLY`; `REJECT` for `GO`.

## Top Concerns

1. Required earnings-date input is `UNAVAILABLE`, so live investability fails even though price/history/sigma are present.
2. Fundamental, revision, and sentiment families are unavailable; the leaderboard is driven almost entirely by technical relative strength.
3. The highest-ranked names cluster in semiconductors, storage, and software; a live sleeve would likely breach sector/correlation discipline without broader candidates.

## Lineage Checks

- Price and target lineage: present through Yahoo chart bars with 2026-07-02 observation dates.
- Sigma lineage: `REALIZED_VOL_30D` from fetched daily returns for every ranked name and ETF.
- Score attribution: present, but only the technical family is sourceable.
- Technical indicator lineage: every displayed TD-9, RSI, MACD, MA, momentum, volume, and relative-strength field comes from `technical_indicators.json`.
- Prediction records: present for all 20 ranked names plus SPY, QQQ, and SOXX.

## Publication Recommendation

Publish `REVIEW_ONLY`. Do not publish a live portfolio or `GO` recommendation.
