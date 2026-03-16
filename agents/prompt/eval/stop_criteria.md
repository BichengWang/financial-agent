# Stop Criteria

This document defines when the daily run must halt, downgrade to `NO_TRADE`, or stop the self-evolution loop.

## Run Status Options

- `GO`: publish a portfolio.
- `NO_TRADE`: inputs are valid, but no candidate set meets the quality bar.
- `HALTED`: the run must stop because process integrity is compromised.
- `REVIEW_ONLY`: publish analysis without a trade recommendation.

## Hard Halt Criteria

Set run status to `HALTED` immediately if any of the following is true:

1. Live or delayed benchmark data is missing and the system is not explicitly in `ILLUSTRATIVE_MODE`.
2. Data lineage is unclear for core fields such as price, volume, beta, or earnings date.
3. More than 20% of top-ranked candidates have unresolved missing critical inputs.
4. The universe filter leaves too few eligible names to produce a credible ranking set.
5. The portfolio cannot be brought inside beta, sector, or drawdown limits after one revision pass.
6. The risk committee agent identifies fabricated, inconsistent, or contradictory evidence.

## Downgrade To No-Trade

Set run status to `NO_TRADE` when:

1. Fewer than 5 names pass the investable threshold.
2. The best available candidates do not clear the 80th percentile adjusted-score threshold.
3. Average pairwise correlation of the feasible top set remains above `0.45`.
4. Event risk is too concentrated, including more than 2 names with earnings inside 14 calendar days.
5. Portfolio drawdown estimate at the 95th percentile exceeds `8%`.
6. The only way to publish is to overconcentrate into one sector or one factor family.

## Review-Only Mode

Set run status to `REVIEW_ONLY` when:

1. The methodology is valid, but the run is based on stale or delayed data that is too weak for positioning.
2. The system is intentionally being used as a dry run or paper-trade cycle.
3. The evidence is sufficient for scenario analysis but not for position sizing.

## Intra-Loop Revision Limit

To avoid endless agent churn, permit at most:

- 1 revision pass between the portfolio construction agent and the risk committee agent.
- 1 clarification request back to the factor scoring agent.

If the run still fails after those retries, stop and publish `NO_TRADE` or `HALTED`.

## Self-Evolution Stop Criteria

Stop the evolution cycle for the day if any of the following is true:

1. Fewer than 20 new closed observations are available for the evaluation window.
2. The proposed prompt or parameter change has no explicit hypothesis.
3. The proposed change cannot be tested on a holdout slice.
4. Out-of-sample Information Ratio improves by less than `0.05`.
5. Maximum drawdown worsens by more than `0.50%`.
6. Turnover rises by more than `25%` without a compensating improvement in hit rate or Information Ratio.
7. The proposal attempts to weaken protected guardrails.

## Freeze Criteria

Freeze parameter mutation entirely and require human review if:

1. Three consecutive evolution cycles reject all changes for lack of evidence.
2. Two accepted changes in a row worsen out-of-sample performance.
3. The system starts oscillating between materially different weights or thresholds without stable improvement.

When frozen, continue running the daily research loop, but do not apply new prompt mutations.
