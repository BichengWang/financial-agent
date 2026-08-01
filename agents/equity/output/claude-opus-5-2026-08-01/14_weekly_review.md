# 14 — Weekly Parameter Review — week ending 2026-08-01

**Published late and by a Saturday run.** `runbook.md § Cadence` schedules this artifact for
Friday 17:15 ET. **No run fired on Friday 2026-07-31** — the last package before this one is
dated 2026-07-30. This run is the first since, so it owes the weekly review, and it is
written from the full week's evidence rather than stubbed.

> **AMENDED 2026-08-01 (post-publication, third scheduled fire ~19:05 ET).** Two rows below
> were stale on arrival. `gpt-5-2026-07-30` merged as PR #58 *after* this package merged as
> PR #57, so it was invisible when the roster was built; and this package's own status read
> `NO_09_ARTIFACT` only because `09_final_report.md` had not yet been written at the moment
> the roster was generated. Both are corrected, with originals preserved as *(was …)*. The
> conclusion strengthens rather than changes: the cross-model agreement now extends to a
> fourth shared date.

## Packages in the window (2026-07-25 … 2026-08-01, all models)

| Package | Date | Status |
|---|---|---|
| `claude-opus-5-2026-07-26` | 2026-07-26 | `NO_TRADE` |
| `claude-opus-5-2026-07-27` | 2026-07-27 | `NO_TRADE` |
| `gpt-5-2026-07-27` | 2026-07-27 | `NO_TRADE` |
| `claude-opus-5-2026-07-28` | 2026-07-28 | `NO_TRADE` |
| `gpt-5-2026-07-28` | 2026-07-28 | `NO_TRADE` |
| `claude-opus-5-2026-07-29` | 2026-07-29 | `NO_TRADE` |
| `gpt-5-2026-07-29` | 2026-07-29 | `NO_TRADE` |
| `claude-opus-5-2026-07-30` | 2026-07-30 | `NO_TRADE` |
| `gpt-5-2026-07-30` *(added by amendment)* | 2026-07-30 | `NO_TRADE` |
| `claude-opus-5-2026-08-01` | 2026-08-01 | `NO_TRADE` *(was `NO_09_ARTIFACT`)* |

Status distribution: **{'NO_TRADE': 10}** *(was {'NO_TRADE': 8, 'NO_09_ARTIFACT': 1})*. Every
package in the window published `NO_TRADE`.

## Cross-model comparison

`claude-opus-5` and `gpt-5` ran the same dates 07-27, 07-28, 07-29 and 07-30 and **agreed on
`NO_TRADE` every time**. That agreement is diagnostic: two independently-prompted models,
fetching from different vendor paths, reach the same conclusion because they hit the same
structural wall (`Fund_Z`/`Sent_Z` unavailable), not because of a shared judgement call. When
models diverge, the divergence is signal; when they converge on a *structural* blocker, it
confirms the blocker is real and not a prompt artifact.

## Parameter review

The weekly slot permits broader parameter changes than the daily light review. **No parameter
was changed this week, and none should have been**, for a reason worth stating explicitly:

| Parameter class | Reviewed? | Outcome |
|---|---|---|
| Family weights (0.30/0.30/0.25/0.15) | yes | **No change.** Re-weighting to compensate for two missing families would be reverse-engineering around a tooling gap and would silently redefine what the score means. |
| mu Calibration Table | yes | **No change — Track A, `eff_n`=1 < 3.** `DEFER`. |
| Core ETF mu prior table | yes | **No change — Track A, `eff_n`=1 < 3.** `DEFER`, despite a clearly diagnosed defect. |
| Sigma sourcing | yes | **No change.** CI coverage 70.16% is inside the 55–85% band and essentially on the 70% target — sigma is the part of this system that works. |
| Confidence calibration | yes | **No change.** The rank-IC binding already caps everything at `MEDIUM`. |
| Evidence thresholds | yes | **No change.** They are doing their job: they are the reason nothing unsupported has been published. |

## Calibration state at week end

| Metric | `EQUITY_ALPHA` | `MARKET_FORECAST` | Healthy |
|---|---|---|---|
| Raw `n` | 439 | 78 | ≥ 10 |
| `eff_n` | 1 | 1 | ≥ 3 for Track A |
| Hit rate | 42.37% | 20.27% | > 50% |
| CI coverage | 70.16% | 78.21% | 55–85% |
| Mean z | -0.4608 | -0.6633 | ±0.5 |
| Rank IC (weighted) | -0.1314 | n/a | > 0 |

The week added 92 equity and 15 market-forecast settlements. Raw `n` grew
347 → 439; **`eff_n` did not move**, exactly as the startup-transient
arithmetic predicts.

## The one thing that changed this week

The `Tech_Z` duplicate-signal defect was found and measured (see `13`). It had been silently
active in every package built on this engine, including all five `claude-opus-5` packages in
this window. It does **not** invalidate their settled predictions — those settle on realized
prices regardless of how the names were chosen — but it does mean the ranking that produced
them over-weighted momentum by 2×, which is directly relevant to the rank-inversion
diagnosis those packages recorded.

## Next week

Apply the deduplication from 2026-08-03. Watch for `eff_n` on `EQUITY_ALPHA` to increment to
2 on **2026-08-05** — the 2026-07-28 falsifiable
projection, still holding.
