# Daily Run Schedule

Use Eastern Time and skip nothing — U.S. market holidays still produce an `ILLUSTRATIVE_MODE` `REVIEW_ONLY` artifact set so the audit trail is unbroken.

## Daily Cadence (Weekdays)

| Time (ET) | Stage | Owner | Required Output | Scheduled? |
|---|---|---|---|---|
| 07:27 | Pre-open publish (full pipeline 00→08 + 12) | Orchestrator | `00_run_manifest.md` … `08_final_report.md`, `12_evolution_log.md` | Yes — `CronCreate` job `56841f5d` (durable, weekdays) |
| 12:15 | Midday monitor | Orchestrator | `09_midday_monitor.md` | No (manual / future scheduler) |
| 15:45 | Pre-close check | Orchestrator | `10_preclose_check.md` | No |
| 16:20 | Close log | Orchestrator | `11_close_log.md` | No |
| 17:00 | Daily evolution review | Evolution Agent | `12_evolution_log.md` (if not folded into 07:27 publish) | No |

## Weekly And Monthly Cadence

| Time | Stage | Owner | Required Output | Scheduled? |
|---|---|---|---|---|
| Friday 17:15 | Weekly parameter review | Evolution Agent | `13_weekly_review.md` | No |
| Last trading day of month 17:30 | Structural review | Evolution Agent | `14_monthly_review.md` | No |

## Scheduling Mechanism

- **Current:** Claude Code `CronCreate` job `56841f5d`, fires `27 7 * * 1-5` (07:27 ET, Mon–Fri), durable (`.claude/scheduled_tasks.json`).
- **Renewal:** Recurring `CronCreate` jobs auto-expire **7 days after creation**. Recreate weekly with the same schema until a more permanent scheduler is wired.
- **Idle gating:** Jobs only fire while the Claude Code REPL is idle (not mid-query). If the REPL is busy at 07:27, the run defers until idle.
- **Catch-up:** Durable one-shot tasks missed while the REPL was closed are surfaced for catch-up. Recurring tasks do not catch up — they wait for the next scheduled fire.
- **Off-minute:** 07:27 (not 07:30) avoids fleet-wide minute-zero pile-up per `CronCreate` guidance.

## Path To A More Permanent Scheduler

When weekly recreation becomes annoying, promote in this order:

1. **macOS launchd** plist invoking `claude -p ".../prompt/main.md" --output-format json` — survives reboots, no 7-day expiry, runs even without an active Claude REPL.
2. **GitHub Actions cron** workflow — runs in cloud, commits the dated output folder back to the repo, useful as a regression harness for the prompt stack itself. Best when you want a public commit history of every run.

## Scheduling Rules

1. The 07:27 publish slot is the default final recommendation time.
2. If the run is `NO_TRADE`, `REVIEW_ONLY`, or `HALTED`, still publish the output package on schedule.
3. Midday and pre-close reviews do not change the morning thesis unless a stop criterion is triggered.
4. The evolution pass never edits protected rules autonomously.
5. US market holidays still publish an `ILLUSTRATIVE_MODE` artifact set — no skipped days in the dated output folder.

## Minimum Daily Deliverables

Every weekday run must produce at least:

1. Run manifest.
2. Embedded prior-month reflection.
3. Regime and preflight note.
4. Top candidates or explicit no-trade logic.
5. Portfolio proposal or no-trade decision.
6. Risk review.
7. Final report.
8. Close log.
9. Evolution log.
