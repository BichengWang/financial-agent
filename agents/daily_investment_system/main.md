# Quantitative Equity Research Prompt System — v3.2

Modular, multi-agent, self-evolving prompt system for short-horizon U.S. equity selection.

Four files, no subdirectories:

- `main.md` — entrypoint (this file).
- `runbook.md` — schedule, scheduler, and dated-output specification.
- `rules.md` — shared research system + stop criteria + evolution policy; every agent obeys all three parts.
- `agents.md` — orchestrator + five specialist stage prompts, in execution order.
- `../output/` (repo path `investments/equity/output/`) — dated run artifacts only; prompts and specs live here.

## Primary Goal

Generate the best **5–10 U.S. equity long candidates** for a **2–6 week horizon**, optimizing:

1. Expected 1-month Information Ratio.
2. Portfolio coherence under explicit risk limits.
3. Reliability of the research process over headline conviction.

If fewer than 10 names pass the thresholds, return fewer. Never fill the list to hit a count.

## Execution

Execute the **Orchestrator** (first section of `agents.md`). It loads `rules.md` + `runbook.md`, then drives the stages of `agents.md` in order:

| Stage | Agent (`agents.md`) | Artifacts |
|---|---|---|
| 0. Reflection (orchestrator-owned) | § Orchestrator — Reflection Stage | `02_reflection.md` |
| 1. Data & regime | § Data and Regime | `03` |
| 2. Factor scoring | § Factor Scoring | `04`, `05` |
| 3. Portfolio construction | § Portfolio Construction | `06`, `07` |
| 4. Risk committee | § Risk Committee | `08` |
| 5. Evolution | § Evolution | `13` |

The orchestrator also publishes `00`, `01` (Source Ledger), `09`, and `15_predictions.json` per `runbook.md`.

State machine — a run is a state machine, not an essay:

`PRECHECK -> REFLECTION -> DATA_OK -> SCORED -> PORTFOLIO_DRAFT -> RISK_REVIEW -> PUBLISHED -> CLOSE_LOGGED -> EVOLUTION_REVIEW`

Hard stop at any stage → `HALTED`. Valid inputs but no trade set meeting the quality bar → `NO_TRADE`.

## Reflection (summary)

Before any new scoring, the orchestrator settles matured predictions, then selects a month-over-month baseline and publishes standalone `02_reflection.md`. Procedure and baseline algorithm: `agents.md § Orchestrator`. Artifact contents: `runbook.md § 02_reflection.md`. Two invariants: never use a folder less than 21 days old as the MoM baseline, and always record the baseline path + flag in `00` and `02`.

## Self-Evolution (summary)

After close, review all models' output packages from the trailing 7 days, compare forecast vs realized, and propose at most one bounded change per run under `rules.md § Evolution Policy`. Log every accepted or rejected change in `13_evolution_log.md`.

## Non-Negotiable Rules

- Never fabricate live market data.
- Every price used for entry, settlement, or MoM comparison must satisfy the Price Sourcing Standard in `rules.md`; otherwise it is `UNAVAILABLE`.
- Never score a raw-return Hit/Miss where benchmark data exists — grounding is to predicted alpha and the stated CI.
- If live or delayed data is unavailable, switch explicitly to `ILLUSTRATIVE_MODE`.
- Never weaken risk limits to force a publishable portfolio.
- Never mutate protected rules in `rules.md § Evolution Policy` without human approval.
- Always publish exactly one status: `GO`, `NO_TRADE`, `REVIEW_ONLY`, or `HALTED`.
- A run that ranks any name is not `PUBLISHED` until `15_predictions.json` exists — without it nothing the run forecast can ever be settled.
- Every run that analyzes or ranks tickers also analyzes and forecasts the core ETFs — **SPY, QQQ, SOXX** — and includes their `MARKET_FORECAST` records in `15_predictions.json` (`rules.md § Core ETF Market Forecast`).
- Never cite an **Enhancing** input (options IV/skew, short interest, bid-ask tape, full-universe feed) as a `GO` blocker; only the five **Required** inputs in `rules.md § Input Classification` may block `GO`.
- Every ranked equity `Adj Score` must include score attribution from source metrics to family z-scores to final score per `rules.md § Financial Metrics and Score Attribution`.

## Deliverables

Publish the full dated package per `runbook.md` (artifact table + per-artifact requirements). The `01_preflight.md` Source Ledger and `02_reflection.md` are the grounding gates: reflection completes before scoring begins, and its carry-forward decisions bind factor scoring when ledger-backed.
