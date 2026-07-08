# 13 Evolution Log

## Run Context

| Field | Value |
| --- | --- |
| Date | 2026-07-02 |
| Model | claude-sonnet-5 |
| Status | NO_TRADE |
| Regime | BULL |
| Evaluation window | Trailing 7 calendar days (2026-06-25 through 2026-07-02), all models |
| Ledger status | `INSUFFICIENT_SETTLED_N` — 0 settled predictions (earliest open `target_date` across all 20 scanned ledgers is 2026-07-08) |
| Baseline flag | `CROSS_MODEL_BASELINE` (`gpt-5-2026-06-07`) |

## Review Window: Packages Examined

`gpt-5-2026-06-28`, `gpt-5-2026-06-29`, `gpt-5-2026-06-30`, `gpt-5-2026-07-01`, `gemini-3.5-flash-2026-06-29`, `gemini-3.5-flash-2026-07-01`, `claude-opus-4-8-2026-06-30`, `claude-fable-5-2026-07-01`, plus this run.

## What Worked / What Failed

**Worked**: `build_index_universe.py` and `technical_indicators.py` both ran cleanly (515-name universe materialized; technical indicators computed 33/33 `OK` once redirected to the IBKR-sourced 30-name sample). The Reflection stage correctly identified `NO_PRIOR_BASELINE`-adjacent conditions (no same-model history) and selected a defensible cross-model baseline without fabricating a same-model one. The Risk Committee found no fabrication, no improper GO-blocking, and approved the package without a revision cycle.

**Failed / gap**: Every one of the 8 other-model packages examined in the trailing-7-day window that reached a final status also published `NO_TRADE`, and the recurring stated cause (where visible, e.g. `gpt-5-2026-07-01`) is the same one this run hit independently: missing fundamental/revision and positioning feeds prevent any name from meeting the "3 of 4 factor families" Evidence Threshold. One package in the window (`gemini-3.5-flash-2026-07-01`) is **incomplete** — only support artifacts (`eligible_universe.txt`, `technical_indicators.json`, `universe_summary.json`) exist, with no `00_run_manifest.md` or later artifacts, suggesting that run halted or was interrupted before publishing.

**New finding this run, not previously logged**: Yahoo Finance (`technical_indicators.py`'s built-in fallback) is blocked at this session's network egress layer with a confirmed organizational policy denial (403, `connect_rejected`, host `query2.finance.yahoo.com`), not a transient failure. This run spent ~4.3 minutes issuing and failing 515 sequential Yahoo fetch attempts before falling back to a 30-name IBKR-sourced Sampled Universe. Whether this network policy is a session-specific artifact or a durable feature of this execution environment is unknown from a single observation, but it is worth flagging for any future run in a similarly configured environment.

## Diagnosis

Primary diagnosis: **`data quality`** (source grounding / feed availability), consistent with the cross-model pattern above — this is now visible across at least 5 consecutive calendar days and 4 different models, which is stronger cross-model corroboration than any single run could establish alone.

Secondary diagnosis: **`output clarity`** — no artifact in this system currently instructs the orchestrator to attempt IBKR-first (skip the doomed Yahoo attempt) when Yahoo is known-blocked for the session, wasting fetch time and tool-call budget on a fallback that cannot succeed once the block is confirmed.

## Proposed Change (Track B — Process)

**Classification: Track B** (missing-fetch procedure fix / sequencing — no scoring math, thresholds, or protected rule is touched).

**Problem statement**: `main.md § Technical Indicator Helper` and `rules.md § Sigma Fallback Chain` both describe Yahoo Finance as the default/expected fallback path when IBKR data is unavailable for a name, with no guidance for the case where Yahoo itself is blocked at the network-policy level for an entire session. This run discovered that condition empirically (515 sequential failed fetch attempts, ~4.3 minutes) before falling back to the Sampled Universe Protocol. A future run in the same or a similarly restricted environment would repeat the same wasted attempt unless the orchestrator is told to check for a known-blocked fallback source first.

**Proposed change**: Add a one-line procedural note to `main.md § Technical Indicator Helper` (or `rules.md § Sigma Fallback Chain`): *"Before attempting the Yahoo Finance fallback across the full eligible universe, run one low-cost connectivity probe (a single-ticker Yahoo fetch, or an agent-proxy status check) to confirm the fallback source is reachable this session; if blocked, go directly to the Sampled Universe Protocol rather than exhausting the full universe list against a fallback known to fail."*

**Why this should help**: it converts a discovered ~4-minute, 515-call dead-end into a single diagnostic call, without changing any scoring math, threshold, or protected rule — purely a sequencing/efficiency fix to the missing-fetch procedure, squarely within Track B scope.

**Validation method** (Track B standard, per `rules.md § Two-Track Change Classification`):

1. Explicit problem statement citing the artifact that exposed it: this log, citing `01_preflight.md § Data-Source Disclosure` and `03_regime_and_data.md § Universe Handoff` from this run's package.
2. Does not weaken any protected rule or grounding gate: confirmed — it changes only the *order* of fetch attempts, not what counts as grounded, not any risk cap, not any evidence threshold.
3. Logged with `HUMAN_REVIEW` flag, takes effect next run unless reverted: see below.

## Decision

**`DEFER`** — flagged `HUMAN_REVIEW`. This is a one-session observation (this is the first run to hit the Yahoo block explicitly); per the Anti-Overfitting Rules ("do not promote a feature because of one or two anecdotal winners" — the inverse also holds for process changes based on one observed failure), the committee defers formal adoption into `main.md`/`rules.md` text pending a human decision on whether the block is durable across sessions or was specific to this run's network configuration. If a second consecutive run independently confirms the same Yahoo-block condition, this becomes mandatory Track B work per `rules.md`: *"A spec inconsistency flagged in two consecutive evolution logs... is mandatory Track B work, not optional."*

**Effective next step**: no `main.md`/`rules.md` edit is made this run. The next run's orchestrator should check whether Yahoo is still blocked before repeating the full 515-name fetch attempt, and if the block is confirmed a second time, this proposal should be promoted from `DEFER` to `ACCEPT` and the procedural note added.

## Track A Note

No Track A (performance/calibration) proposal is made this run — 0 settled predictions exist across all scanned ledgers (`INSUFFICIENT_SETTLED_N`), well short of the ≥20 settled-record minimum required by `rules.md § Acceptance Standard`. The mu Calibration Table and Core ETF mu prior table are unchanged.
