# 14 Weekly Review

## Window

Friday after-close review for 2026-07-04 through 2026-07-10, across committed gpt-5 and claude-family packages plus this run.

## Findings

- The index-union and technical-helper path is now repeatable across models; the recurring weakness is non-price factor coverage, not universe construction.
- The latest deduplicated settlement set has equity hit rate 48.57%, CI coverage 70.00%, and mean z -0.248. CI calibration is inside the 55%-85% healthy band when n is sufficient.
- Current leaderboards remain concentrated in growth/technology momentum. Status discipline has prevented that one-family signal from becoming a live portfolio.

## Parameter Decision

`NO_PARAMETER_CHANGE`. Rank IC is unavailable from the normalized settlement blocks, and there is no holdout result supporting a Track A change. Preserve factor weights, mu tables, confidence thresholds, and protected risk caps.

## Process Follow-Up

Review the deferred Track B raw-history persistence proposal in `13_evolution_log.md` as a separate code change.
