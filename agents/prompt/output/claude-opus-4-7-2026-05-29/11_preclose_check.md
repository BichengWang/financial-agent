# 11 Pre-Close Check

## Status

**Suppressed-but-present.** Per the same logic as `10_midday_monitor.md`: no live data feed, no positions, `REVIEW_ONLY` publication. The audit trail is preserved by emitting this file; content is intentionally minimal.

## What Would Run In Live Mode

| Check | Expected behavior |
|---|---|
| Day-of-week effect on the 7 names | Document any name with > 1.5σ day-of-week move (Friday-specific) |
| Pre-close liquidity check | Confirm each name's last-30-min liquidity ≥ 20D ADV / 13 (i.e., no thin-tape entry trap) |
| Risk-limit re-verification | Re-run portfolio β, sector cap, correlation check on intraday-updated inputs |
| AVGO event window | Confirm AVGO is *not* held (today's portfolio correctly excludes it); no skip-the-print position to unwind |
| Pre-close override criteria | Trigger an unscheduled rebalance only if any name has hit a `stop_criteria.md` hard halt |

## Exceptions Logged

None.

## Handoff

Pass through to `12_close_log.md`.
