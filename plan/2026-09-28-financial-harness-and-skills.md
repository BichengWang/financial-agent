# Financial Harness + Skills: Spike and Architecture Proposal

**Date:** 2026-09-28 · **Status:** proposal, spike complete · **Scope:** the daily
equity research system (`agents/equity/daily_investment_system/`), `turtle-trader`,
and future financial agents in this repo.

**Decision requested:** approve the architecture below and start Phase 1
("validate, don't replace"). Phase 1 doesn't change how daily runs are executed.

## TL;DR

- **Problem.** Prompt-as-code v3.3 asks one model to be orchestrator, data engineer,
  calculator, bookkeeper, validator, and author, working from 104 KB (~26k tokens)
  of prose that every stage loads. The run history shows what that costs.
  The scoring engine is re-written from `rules.md` on every run. Machine-readable
  ledgers drift in schema, units, and meaning between runs and models. Accepted
  fixes stay in run logs and never reach the spec. Manifests claim files that were
  never written. The only `GO` in the history (03-16) was issued on illustrative
  data.
- **Proposal.** Three layers, one rule: *the model decides, code computes, the
  harness enforces.*
  - **Skills** (open Agent Skills format) carry when and why, and the judgment work.
  - A deterministic **harness** (Python) owns lifecycle, data provenance, the
    numeric policy, gates, rendering, and the ledgers.
  - The **runtime** (Claude Code, the Agent SDK, Codex, Gemini CLI) is swappable.
- **Spike.** Built the harness core under `src/financial_agent/harness/`:
  standard library only, 85 tests, mypy-clean. Parts: skills registry, policy as
  code, provenance ledger, gates, lifecycle, and a conformance audit. I ran it over
  all 95 dated run packages. Headlines:
  - **Arithmetic is not the problem; conventions are.** 0 formula errors on 1,877
    CI bounds, 1,574 VaR/CVaR values, 1,574 composite z-scores.
  - `adj_score` is stored as a 0–100 percentile in 15 packages (210 records).
  - VaR is stored in percent in 5 packages (106 records).
  - `kelly_025` follows 4 different conventions, and 4 models switch between them.
  - Settlement rows come in 35 different key-sets.
  - From the ledger alone, the gates reproduce the published status of 73 of 83
    runs. The 10 misses are explained below.
- **Recommendation.** Adopt. Phase 1 wires the publish gate into the run and CI,
  freezes a v1 ledger schema, and resolves 7 rule ambiguities the spike surfaced
  (§6). Everything else is phased behind exit criteria (§5).

---

## 1. How the system works today

```text
 cron/manual ──► model reads main.md + agents.md + rules.md + runbook.md (104 KB)
                   │
                   ├─ runs helpers by prose instruction: build_index_universe.py,
                   │  technical_indicators.py, settlement_ledger.py (+ SHADOW tools)
                   ├─ writes ad-hoc scripts in scratch: bulk fetch, scoring engine,
                   │  risk analytics, earnings sweep, liveness screen, tables
                   ├─ hand-writes ~180 Source Ledger rows, score traces, tables
                   ├─ reviews its own work (risk committee), proposes rule changes
                   └─ writes 12–17 artifacts (median 168 KB; recent 254 KB,
                      max 665 KB) to agents/equity/output/{model}-{date}/
```

| Responsibility | Today | Should be |
|---|---|---|
| Stage order, retries, revision budget | model reads `main.md` | code (state machine) |
| Fetching, cross-checking, freshness tags | model-written scripts per run | typed data adapters |
| Source Ledger (`01_preflight.md`) | typed by the model | generated from tool calls |
| mu, sigma, CI, Kelly, VaR, z-scores, score trace | re-implemented per run from `rules.md` | versioned kernels + policy file |
| Evidence thresholds, stop criteria, run status | model interprets prose | gate functions |
| Numeric tables in `05`/`06`/`07`/`09` | transcribed by the model | rendered from data |
| Regime call, thesis, catalysts, adversarial review, evolution hypotheses | model | model (unchanged) |

## 2. Evidence

### 2.1 Measured by the spike (`python -m financial_agent.harness audit`)

Data: 95 dated packages through 2026-09-03 (12 have no `15_predictions.json`),
1,877 prediction records, 2,022 settlement rows. The spike recomputes each record's
derived fields from that record's own inputs.

| Check | Records | Failures | Where |
|---|---|---|---|
| 70% CI bounds, target price, horizon, enums, required fields | 1,877 | **0** | — |
| Composite z, VaR95/CVaR95 formula (after unit normalization) | 1,574 | **0** | — |
| `adj_score` = composite × DQ − penalties | 1,574 | **234** | 210 store a 0–100 percentile (gpt-5 06-16→07-02, gemini 06-21/06-29); 24 skip DQ (fable 07-15) |
| VaR/CVaR stored as decimals | 1,574 | **106** | percent units in fable 07-14/15/17/21, opus-4-8 06-30 |
| `kelly_025` convention | 1,499 | 4 conventions | uncapped-decimal, capped-decimal, capped-percent, mixed units; opus-5, sonnet-5, gpt-5, fable each use 2 |
| `kelly_raw` = mu/σ² fallback, or method recorded | 1,499 | **388** unverifiable | the rules allow a beta-adjusted variant, but no record says which formula was used |
| mu within ±2pp of the calibration band | 227 | 1 | fable 07-01 UNH: pctl 87.3, prior +4%, published +1% |
| Core ETF forecasts present (rule effective 06-11) | 80 | 1 | gpt-5 06-11 |
| Settlement row schema | 2,022 | **35 key-sets** | legacy field names used 754 times (`settled_on`, `current_price`, …) |
| Run status in the ledger | 83 | 3 names, 3 missing | `run_status` ×28, `final_status` ×49, `status` ×3; `data_mode` missing in 22 |

Within a single run, conventions are consistent. They drift between runs and
models, which is what happens when a spec exists only as prose that each run
re-reads. The fields that drift feed calibration: `adj_score` feeds rank IC, and
`kelly_025` feeds the Kelly gates.

**Status replay.** `investability()` + `decide_status()` recompute the status from
the ledger alone. They agree with the published status on 73 of 83 packages.

- 4 misses are REVIEW_ONLY runs on the 07-03 market holiday and weekends. The
  replay has no trading calendar; the harness would (`settlement_ledger.py`
  already has one).
- 3 packages store no status at all.
- 2 are integrity halts (a truncated run; a post-hoc audit correction).
- 1 is a real deviation: sonnet-5 07-03 declared `DELAYED_PARTIAL` but published
  `NO_TRADE`. `rules.md` requires `REVIEW_ONLY` for that data mode.

### 2.2 From the run history (all 94 evolution logs, 87 risk reviews, git log)

| Failure class | Examples (evidence) |
|---|---|
| Engine re-implemented each run | "This run's engine was written from `rules.md`" (opus-5 07-27). Sortino silently equal to Sharpe "in every published table to date" (fable 07-21). Drawdown sign flipped on a rebuild (opus-5 08-03). Macro score irreproducible, error up to 0.293. |
| Hand transcription and counting | 9 wrong targets/ranges in one table, 14 wrong hand-written ranks (fable 07-15, `2cfc550`). "27/27" corrected to 26/27 (`3622dc5`). An over-claimed +0.06pp intraday alpha (`2146d21`). |
| Settlement bookkeeping | Calibration sample overstated ~48% (135 vs 77) by duplicate settlements. Conflicting intraday vs close cuts. Fixed by `settlement_ledger.py` (46 tests); runs since report 0 conflicts. Its own timing bugs (07-22, 08-07) were fixed once, in code, with tests. |
| Manifests written before files | 08-06, 08-14, 08-28 claimed unpublished artifacts. Gemini 05-30 says `08`/`09`/`13` were "written" but they don't exist. 5 truncated runs needed later backfills. Why they truncated isn't recorded. |
| Provenance | `gemini-3.5-flash-2026-07-13` is `claude-fable-5-2026-07-13` with the model name swapped. 11 of 17 files are byte-identical and the ledger is identical after the rename (verified). 08-10 then settled both copies. |
| Spec drift | About 14 of about 27 accepted Track B changes exist only in run logs (adjusted closes, earnings sweep, corporate-action screen, vendor finality, …). The 07-29 earnings rule never reached `rules.md:280`, and a later audit HALTED on the old wording (`563b838`). |
| Governance | 46 `HUMAN_REVIEW` flags; no human approval or revert of any is recorded. |
| Structural `NO_TRADE` | `Fund_Z`/`Sent_Z` `UNAVAILABLE` makes threshold #2 unsatisfiable, so no run since 07-01 could reach `GO`. The 07-15 plan counted 13 consecutive `NO_TRADE` scoring sessions; the 09-03 manifest still names it the sole blocker. A beta-band/5%-cap infeasibility was likewise found only after drafting, for weeks. |
| Scheduling and paths | Runs fired between 01:36 and 23:45 ET against a 07:27 spec. 12 of 18 trading days (08-03→08-26) have no run. 49 folders cite `investments/equity/…` and 7 contain `/Users/...` paths. `agents/equity/prompt/main.md` still points at `investments/`. |
| Cross-model reading | The same holiday was labelled three ways. Weekend runs publish `REVIEW_ONLY` (fable) or `NO_TRADE` (opus-5 08-22). |
| Context economics | Every stage loads 104 KB of prompt stack. The evolution stage is told to review the trailing 7 days of packages: 1.0–6.5 MB, roughly 0.25–1.6M tokens. |

### 2.3 Diagnosis

1. **Specs live in prose, so every run re-implements them.** That is the root of
   engine rewrites, convention drift, and cross-model disagreement.
2. **The model is the bookkeeper.** That is the root of transcription errors,
   miscounts, and false manifests.
3. **Nothing enforces invariants at write time.** That is the root of schema drift,
   "accepted" changes that never land, and clones that go unnoticed.

The counter-example is already in the repo. Once settlement bookkeeping moved
into `settlement_ledger.py`, runs stopped double-counting. When that code had bugs
of its own, they were fixed once, with tests, instead of being re-argued in every
run's prose.

## 3. Architecture

### 3.1 Principles

1. **The model decides, code computes, the harness enforces.** The model never
   types a number it didn't get from a tool, and never re-derives a formula.
2. **One source of truth per rule.** Numbers live in the policy file, formulas in
   kernels, invariants in gates, and procedure and judgment guidance in skills.
3. **Provenance by construction.** Facts enter only through calls that stamp
   source, `retrieved_at`, freshness, and claim type. The model cites row IDs.
4. **Portable.** Skills use the open Agent Skills format. Tools are reachable as a
   CLI and (Phase 4) over MCP. Correctness never depends on one vendor's hook
   semantics.
5. **Fail closed.** Missing means `UNAVAILABLE`, gates block, and hooks are only
   defense in depth.
6. **Decision support only.** The harness never places orders (§3.7).

### 3.2 Layers

```text
┌──────────── Agent runtime (swappable) ────────────────────────────────────┐
│ Claude Code / Agent SDK · Codex · Gemini CLI · (later) in-repo loop        │
│ sees: skill catalog (~100 tokens/skill) → activates skills on demand       │
└───────┬─────────────────────────────────────────────┬─────────────────────┘
        │ reads SKILL.md (progressive disclosure)       │ calls typed tools (CLI / MCP)
┌───────▼──────────────────────┐        ┌──────────────▼──────────────────────────┐
│ Skills  skills/<name>/       │ binds  │ Harness  src/financial_agent/harness/    │
│ SKILL.md + scripts/ +        │ via    │ lifecycle · tool gateway · provenance    │
│ references/ + assets/        │ fa-*   │ ledger · kernels · policy (TOML) ·       │
│ workflow · capability ·      │ meta-  │ gates · renderer · stores · audit/replay │
│ reference skills             │ data   └──────────────┬──────────────────────────┘
└──────────────────────────────┘                       │ adapters (cassette-recorded)
                                   ┌───────────────────▼──────────────────────────┐
                                   │ IBKR MCP (read-only) · Nasdaq · stockanalysis │
                                   │ SEC EDGAR · CNBC/CBOE · Treasury/FRED · CSV   │
                                   └──────────────────────────────────────────────┘
```

### 3.3 Harness components

| Component | Responsibility | Replaces | Spike |
|---|---|---|---|
| **Lifecycle** (`lifecycle.py`) | `PRECHECK → … → EVOLUTION_REVIEW` state machine; revision budget (1 risk revision, 1 scoring clarification); `PUBLISHED` only through a passing publish gate; transcript generated for `00` | `main.md` state machine, `rules.md § Intra-Loop Revision Limit` | built |
| **Tool gateway + adapters** | Typed fetchers with retries, fallback chains, vendor-finality and liveness screens, two-source cross-checks; every response recorded (cassette) for replay | model-written fetch scripts; Track B rules that exist only in logs | designed |
| **Provenance ledger + renderer** (`ledger.py`) | `observe` / `observe_price` / `derive` / `unavailable`. Derived rows inherit `UNAVAILABLE`. The Price Sourcing Standard is a function. `{{L012}}` citations render values. A lint blocks literal numbers in model text. `01` table generated | hand-typed Source Ledger and tables | built |
| **Kernels** | Pure, versioned, tested compute: universe, indicators, risk analytics, family z-scores and score trace, mu/sigma/CI, Kelly, feasibility pre-check, settlement, MoM baseline selection | per-run re-implementation | universe, indicators, settlement (plus the SHADOW family tools) exist as helpers today |
| **Policy** (`policy.py`, `equity_policy.toml`) | Every number in `rules.md` as data: weights, mu bands, regime priors, thresholds, caps, Kelly gates. Protected and Track A key prefixes. `check_mutation()` governs diffs using the *old* policy's limits | the numeric half of `rules.md` | built |
| **Gates** (`gates.py`) | `investability()` (evidence thresholds from the record's own inputs), `decide_status()` (stop criteria + Required vs Enhancing), `publish_gate()` (checklist from the directory + per-record audit) | risk-committee checklist items 8–15; `runbook.md` checklists | built |
| **Stores** | Append-only prediction and settlement ledgers with one typed writer and JSON Schema v1 (canonical names, decimal units, explicit `kelly_method`) | free-form `15_predictions.json` | audit only |
| **Audit / eval** (`audit.py`) | Conformance audit (§2.1); golden-run replay from cassettes; cross-model diff of the same day's inputs; content hash per package (catches clones) | none | audit built |

### 3.4 Skills

**Format.** The [open Agent Skills spec](https://agentskills.io/specification):

- a directory holding `SKILL.md` with YAML frontmatter;
- `name` ≤ 64 chars, `[a-z0-9-]`, matching the directory; `description` ≤ 1,024
  chars saying what and when;
- optional `license`, `compatibility`, `metadata` (string→string), `allowed-tools`;
- optional `scripts/`, `references/`, `assets/`, each loaded only when needed.

Harness binding rides in `metadata` under `fa-` keys, so skills stay valid for any
client:

```yaml
metadata:
  fa-stages: "RISK_REVIEW PUBLISHED"   # run states this skill serves
  fa-tools: "gate audit"               # harness tools it may call
  fa-writes: "none"                    # artifacts/sections it authors
  fa-version: "1"                      # quoted: other YAML parsers would make 1 a number
```

**What a skill must not contain:** numbers (they live in the policy), formulas
(kernels), or schemas (harness). It points to them and explains how to act on
their output. `skills/equity-publish-gate/SKILL.md` is the worked example.

**Taxonomy and migration of today's prompt files:**

| Skill | Kind | Built from | Model's job |
|---|---|---|---|
| `equity-daily-run` | workflow | `main.md`, orchestrator in `agents.md`, `runbook.md` cadence | drive stages via harness tools; write the manifest narrative |
| `equity-reflection` | workflow | `agents.md` Reflection, `runbook.md § 02` | interpret settlements and MoM; carry-forward decisions with reasons |
| `equity-regime-call` | workflow | Data and Regime agent | classify regime from the harness evidence pack; flag event concentration |
| `equity-thesis-writer` | workflow | Factor Scoring (narrative half) | thesis, catalysts, ±2pp mu adjustments with ledger-cited reasons |
| `equity-risk-committee` | workflow | Risk Committee agent (checklist items 1–7) | adversarial review in a fresh context, ideally a different model; items 8–15 become gates |
| `equity-evolution-review` | workflow | Evolution agent + `rules.md § Evolution Policy` | diagnose and hypothesize; emit a policy diff or a Track B PR |
| `equity-publish-gate` | capability | `runbook.md` checklists | run the gate; act on failures (**built**) |
| `market-data-grounding` | capability | Price Sourcing Standard, fallback chains, vendor rules from logs | choose adapters and handle `UNAVAILABLE` |
| `technical-indicators`, `fundamentals-edgar`, `sentiment-nasdaq`, `prediction-settlement` | capability | existing helpers | interpret outputs; never re-derive them |
| `turtle-trader` | capability | existing `agents/equity/turtle-trader/SKILL.md` | move to `skills/turtle-trader/` with `scripts/turtle.py` |
| `equity-research-policy` | reference | prose half of `rules.md` | why the rules exist; tables generated from the policy file |

**Context economics.** Today every stage loads about 26k tokens of rules. Under
skills, a stage loads the catalog (the spike's two skills cost about 290 tokens),
the active skill (under 5k tokens recommended), and the stage's inputs as harness
summaries. The evolution stage reads the audit and settlement manifests, not 1–6.5
MB of raw packages.

### 3.5 How a run executes

1. The scheduler calls `fa-harness run --model <id>`. The harness takes a lock on
   (model, date) and checks the trading calendar.
   - Non-trading day: the status comes from one calendar rule (decision 6 in §6),
     applied identically for every model.
2. **PRECHECK:** data adapters build the universe, fetch history, run the
   liveness/corporate-action screen, and write ledger rows.
   - **GO-reachability check:** can any name pass the thresholds with the data
     actually wired? If not, say so on day 1, not in run 13.
3. **REFLECTION:**
   - The settlement kernel settles due predictions.
   - `equity-reflection` has the model interpret the results and write narrative
     citing `{{L…}}`.
4. **DATA_OK → TECHNICALS_OK → SCORED:**
   - Kernels compute families, trace, mu/sigma/CI, and Kelly.
   - `equity-regime-call` and `equity-thesis-writer` supply the judgment fields.
     Each mu adjustment is bounded by the policy and must cite a row.
5. **PORTFOLIO_DRAFT:** a feasibility pre-check, then a sizing kernel; the model
   explains the exclusions.
6. **RISK_REVIEW:**
   - The gates run checklist items 8–15.
   - `equity-risk-committee` has the model (fresh context) attack the judgment
     calls (items 1–7).
   - The model may downgrade the status, never upgrade it.
7. **PUBLISHED:**
   - The renderer writes every numeric table.
   - `publish_gate()` passes, then the lifecycle moves.
   - The manifest checklist is generated from the directory.
8. **EVOLUTION_REVIEW:**
   - The model proposes one change.
   - Policy diffs go through `check_mutation()`; Track B changes become a PR with
     a test. "Accepted" means merged.

### 3.6 Runtime integration

| Concern | Claude Code / Agent SDK | Other runtimes (Codex, Gemini CLI, GPT) |
|---|---|---|
| Skills | project skills under `.claude/skills/<name>/` (symlink or sync from `skills/`); SDK loads them with `setting_sources=["project"]` | same directories (open format); `python -m financial_agent.harness skills catalog` emits the `<available_skills>` block for prompt injection |
| Tools | CLI today. Phase 4: the same functions as an MCP server (stdio), or in-process via the SDK's `create_sdk_mcp_server` | CLI or MCP |
| Enforcement | the harness itself (gates inside `publish`); `PreToolUse` hooks to deny order tools and direct writes to `agents/equity/output/` | the harness itself |
| Independence for review | subagent with its own context and model for `equity-risk-committee` | separate invocation with a different model |
| Scheduling | GitHub Actions `schedule` (e.g. `anthropics/claude-code-action`) or launchd calling the harness, replacing `CronCreate` jobs that expire after 7 days | same workflow, different runtime |

### 3.7 Safety

- **No order placement.** The IBKR connector available in this environment exposes
  order tools (`create_order_instruction`, …). Deny them in every runtime's tool
  config, and give the harness gateway a read-only adapter allow-list. Outputs stay
  decision support, as `turtle-trader` already states.
- **Fetched content is data, not instructions.** Adapters parse pages into typed
  fields, so the model sees values rather than raw scraped HTML. That shrinks the
  prompt-injection surface.
- **Secrets** come from the environment and never land in packages. The publish
  gate's "outside the contract" check already rejects stray files
  (`gpt-5-2026-07-30` carries 3.8 MB of working files today).

### 3.8 Where each part of `rules.md` goes

| `rules.md` section | Owner after migration |
|---|---|
| Non-Fabrication Contract, Source Ledger Contract, Price Sourcing Standard | ledger + adapters (code); one paragraph of rationale in `equity-research-policy` |
| Prediction Ledger, Settlement Rules, Rolling Metrics, Canonical Settlement Ledger | stores + settlement kernel (exists) |
| mu Calibration Table, Core ETF priors, Ratio Definitions, Sigma Fallback Chain, CI/target derivation | policy + kernels |
| Factor Architecture, Family Aggregation, Metric Pack, TD-9/RSI/MACD definitions | kernels (indicators already exist) + policy weights |
| Data Quality Multiplier | kernel: a deterministic function of coverage and freshness. Today the guideposts are prose judgment |
| Input Classification, Evidence Thresholds, Risk Controls, Confidence Labels, Stop Criteria | gates + policy |
| ILLUSTRATIVE_MODE | harness data mode (caps status and confidence automatically) + skill guidance |
| Regime classification, thesis quality, catalyst plausibility, risk-committee skepticism | **model**, through workflow skills |
| Evolution Policy | policy governance (`check_mutation`) + PR workflow + `equity-evolution-review` |

## 4. The spike

### 4.1 What was built

| Path | Lines | Purpose |
|---|---|---|
| `src/financial_agent/harness/skills.py` | 442 | Agent Skills parser/validator (strict YAML subset), registry, `<available_skills>` catalog, three disclosure levels, resource confinement, `fa-*` binding |
| `src/financial_agent/harness/policy.py` + `equity_policy.toml` | 234 + 134 | rules-as-code: mu bands, CI, VaR/CVaR, Kelly (gate and sizing views), score trace; `check_mutation()` governance |
| `src/financial_agent/harness/ledger.py` | 325 | provenance ledger, Price Sourcing Standard, `UNAVAILABLE` propagation, citation renderer, literal-number lint, `01` table |
| `src/financial_agent/harness/gates.py` | 217 | investability, status decision, publish gate |
| `src/financial_agent/harness/lifecycle.py` | 127 | state machine with revision budget and gated publish |
| `src/financial_agent/harness/audit.py` | 393 | conformance audit of prediction and settlement ledgers |
| `src/financial_agent/harness/__main__.py` | 164 | CLI: `skills validate` / `skills catalog`, `audit`, `gate`, `policy-check` |
| `skills/equity-publish-gate/SKILL.md` | 52 | worked example of a thin capability skill |
| `tests/harness/` | 972 | 85 tests, including pinned real-data findings and a `rules.md` ↔ policy parity check |

Everything is standard library only (Python 3.11+ for `tomllib`), matching the
helpers' design. It has no import coupling to the RL/DL packages.

```bash
PYTHONPATH=src python3 -m financial_agent.harness skills validate
PYTHONPATH=src python3 -m financial_agent.harness audit
PYTHONPATH=src python3 -m financial_agent.harness gate agents/equity/output/claude-opus-5-2026-09-03
uv run --no-project --python 3.12 --with pytest pytest tests/harness
```

### 4.2 What it showed

- **The open skill format fits.** Both skills validate. Harness binding fits the
  spec's string→string `metadata`. `turtle-trader` is valid but has two problems:
  - It references `../daily_investment_system/` and `../output/`, which breaks
    portability.
  - It sits outside every discovery path (`.claude/skills/`, a plugin), so no
    runtime auto-loads it today despite "Activates on /turtle-trader".
- **The validator must model other parsers.** Unquoted `version: 1.0` or
  `reviewed: 2026-09-28` in `metadata` is a float or a date to PyYAML, which
  violates the spec's string map. The registry flags it.
- **Rules as code are reproducible.** From its own inputs, the policy reproduces a
  published record (VLO, 2026-09-03) to the ledger's stored precision: CI bounds
  within 0.001 USD; VaR, CVaR, composite z, and Adj Score within 1e-6. Kelly
  matches to 1e-5 relative, because the ledger stores a rounded sigma.
- **The gates reproduce the published status on 73 of 83 packages** (§2.1). The
  latest package passes the publish gate. Packages in the percentile-as-score era
  fail it, each with an explanation.
- **The publish gate must be versioned with the artifact contract.** Against
  today's contract, 32 of 95 historical packages fail:
  - 16 on the `adj_score` convention;
  - 12 because they predate the ledger contract (March–May numbering, no
    `15_predictions.json` yet, the 07-16 Haiku shadow test, the unfinished Gemini
    05-30 run);
  - 2 missing core-ETF records around the rule's 06-11 start;
  - 1 mu-band violation;
  - 1 with 3.8 MB of leaked working files (gpt-5 07-30).

  Contract and schema therefore need a version and an effective date, like the
  policy.
- **Governance works as code.** The spike checked these cases:
  - Changing the 5% name cap needs human approval.
  - A 0.10 family-weight step is rejected.
  - A 0.05 step with `eff_n = 2` is `DEFER`red.
  - A proposal can't raise its own step limit, because the `evolution` table is
    protected.
- **Codifying forces decisions.** Threshold #3 ("no family > 50% of total
  conviction") and the meaning of `kelly_025` can't be coded without choosing an
  interpretation (§6).

### 4.3 Not done in the spike

Data adapters, cassettes, the MCP server, the renderer wired into real artifacts,
JSON Schema v1, and any change to the daily prompts or to how runs execute.

## 5. Migration plan

Each phase keeps runs working and has an exit criterion. Historical packages stay
immutable and are normalized at read time (as `settlement_ledger.py` does); they
are never rewritten.

| Phase | Work | Exit criterion |
|---|---|---|
| **1. Validate, don't replace** | Resolve the §6 decisions. Freeze JSON Schema v1 for `15_predictions.json` (canonical names, decimals, `kelly_method`, split Kelly fields, one status key). Call the `gate` command before `PUBLISHED` (one line in `agents.md` + the skill). CI workflow: harness tests + `audit --strict` on PRs touching `agents/equity/`. Content hash per package. *(Gate call, CI workflow (gate by effective date), and content hash / `clones` report shipped. Schema v1 shipped opt-in: `harness schema`, enforced by the gate when a ledger declares `schema_version: 1`; adopting it and the §6 decisions stay open.)* | 10 consecutive runs pass the gate with 0 error findings; no new settlement key-sets |
| **2. Compute, don't transcribe** | Promote the per-run engine to kernels: families/trace, risk analytics, forecast, Kelly, feasibility, earnings sweep (fail closed), liveness and corporate-action screens. Typed ledger writer. Ledger + renderer produce `01`/`05`/`06`/`07`/`09` tables; model text uses `{{L…}}` citations, enforced by the lint. *(`kernels.py` shipped: risk analytics, ratios, and v1 record builders for names and core ETFs that refuse out-of-policy judgment; they reproduce the 2026-09-03 numbers. `portfolio_feasibility` shipped: portfolio beta, sigma, dd95, average pairwise correlation, sector weights and the event-risk count from proposed weights and closes, returned as `risk_breaches` for `decide_status` (`harness kernel portfolio`, MCP `portfolio_feasibility`). `scoring.py` shipped: slot z-scores, family z, Adj Score and the universe percentile per the normative Metric Definition Table, with the slot list in the policy (`harness kernel score`, MCP `score_universe`); its transforms are pinned to the 2026-09-03 published z-scores. Not yet called by the daily prompts.)* | Numeric tables are 100% generated. Two models on the same day with the same inputs produce identical numbers, differing only in judgment fields. |
| **3. Skills, not monolith** | Split the prompt stack into the §3.4 skills. `equity_policy.toml` becomes canonical and generates the `rules.md` tables. Evolution emits policy diffs or PRs; an accepted Track B change is a merged PR with a test. | Per-stage prompt context under 15 KB (from 104 KB); zero accepted changes that exist only in run logs |
| **4. Run anywhere, on schedule** | `fa-harness run` entry point *(skeleton shipped: `harness run`, lock, handler table, gated publish, run journal under `output/.runs/`; handlers for PRECHECK (calendar + GO reachability) and REFLECTION (settlement summary); `harness manifest` generates the checklist, replay, and hash)*; MCP server over the same functions *(shipped: `harness mcp`, read-only tools over stdio)*; scheduled GitHub Actions workflow with a (model, date) lock, heartbeat, and duplicate-run guard; cassette record/replay; golden-run regression over history. | ≥ 95% of trading days run within ±30 min of schedule; any run replays byte-for-byte from cassettes |
| **5. Make GO reachable** | Fund/Sent Phase 2 (bulk `companyfacts` + threaded Nasdaq) as capability skills and adapters. SHADOW → promoted becomes a policy diff with human approval *(`score.shadow_families`, protected)*. GO-reachability check at PRECHECK *(shipped: `harness reachability`, the PRECHECK handler, and the gate output)*. | GO is reachable, or its impossibility is reported by the harness on the first run instead of being discovered |

## 6. Decisions needed from the owner

1. **`adj_score`** is the score, never a percentile. Make `pctl` a separate
   required field. (The rules already say this; 15 packages disagree.)
2. **Kelly.** `rules.md` defines `0.25 × Kelly` as capped at 5% and also gates on
   it reaching 5%, which only works uncapped. Proposal:
   - `kelly_fractional` (uncapped) is the gate input;
   - `position_weight` (capped) is the sizing input;
   - `kelly_method` ∈ {`BETA_ADJ_TE`, `MU_OVER_SIGMA2`}.
3. **Units.** Every return and risk field is a decimal in JSON. Percent is for
   rendering only.
4. **Threshold #3 ("conviction share").** The spike uses the largest positive
   weighted family contribution divided by the sum of positive contributions.
   Alternative: the share of absolute contributions. Pick one.
5. **Threshold #4 ("data completeness ≥ 85%").** Define the denominator. The spike
   uses family availability as a labeled proxy. Under that proxy only 4 of 4
   families pass, so promoting one SHADOW family would not make `GO` reachable
   (`harness reachability --families fund_z tech_z macro_z`).
6. **Non-trading days.** One status rule for weekends and holidays, computed from
   the exchange calendar. Today fable says `REVIEW_ONLY` and opus-5 says
   `NO_TRADE`. The harness applies the runbook's holiday rule (`REVIEW_ONLY`) and
   keeps the computed status on weekends until `calendar.weekend_status` is set.
   With the calendar the replay still agrees on 73 of 83 packages: fable 07-03
   now matches, and gpt-5 06-19 (Juneteenth, published `NO_TRADE`) is a new miss.
7. **Exposure basis.** The beta band and the 30% sector cap are measured on
   NAV (uninvested NAV is cash at beta 0) or on the invested book (normalized by
   gross). Past runs use both: several gpt-5 packages publish `NO_TRADE` because
   "maximum NAV beta is 0.509" at 35% gross, others check sleeve beta. On NAV a
   book of at most 10 names at the 5% cap (50% gross) reaches the 0.90 floor only
   with an average beta of 1.8, so `GO` is structurally unreachable. The harness
   computes both and gates on `risk.exposure_basis` (protected), set to the
   literal `NAV` until this is decided. The drawdown cap stays on NAV either way.
8. **Governance.** An accepted evolution change means a merged PR (human merge).
   Is that acceptable? It closes the 46-flag `HUMAN_REVIEW` loop that never closes
   today.

Also open:

- Canonical skill location: `skills/` plus `.claude/skills` symlinks, or
  `.claude/skills` only.
- Stay stdlib-only, or adopt `pydantic`/`jsonschema`/`PyYAML` once schemas grow.
- The environment itself (below).

**Environment finding.** `uv sync --locked` fails on Python 3.12 today. `pandas<2.0`
resolves to 1.5.3, which has no cp312 wheel and fails to build from source
(`ModuleNotFoundError: pkg_resources`). The pin is owner-controlled per `AGENTS.md`,
so this spike runs its tests in an isolated `uv run --no-project` environment. It
needs a separate decision: bump pandas, or add
`[tool.uv.extra-build-dependencies]`.

## 7. Risks

| Risk | Mitigation |
|---|---|
| Over-constraining the model hides novel problems (the LLM found vendor bar lag and symbol reuse) | Keep an anomaly-notes channel and the risk committee's veto. Codifying a new check is a small PR, cheaper than a prose rule |
| Two sources of truth during migration (prose and policy) | `tests/harness/test_policy_matches_rules.py` (in this spike) fails whenever `equity_policy.toml` and the `rules.md` tables and thresholds diverge. Phase 3 flips the direction and generates the tables |
| Harness becomes a second prompt stack nobody reads | Require every harness rule to have a test and an error message citing its `rules.md` section. The parity test above is the first |
| Runtime lock-in | Open skill format; tools over CLI/MCP; enforcement inside the harness, not in runtime hooks |
| Effort | Phase 1 is small (this spike plus a schema and a CI job) and pays off immediately; later phases are gated on their exit criteria |

## Appendix A — audit output (as of 2026-09-03)

```text
| check | severity | checked | failed | fail % | packages | models |
|---|---|---|---|---|---|---|
| equity.benchmark_price | - | 1637 | 0 | 0.0 | 0 | - |
| formula.adj_score | error | 1574 | 234 | 14.9 | 16 | claude-fable-5, gemini-3.5-flash, gpt-5 |
| formula.ci70 | - | 1877 | 0 | 0.0 | 0 | - |
| formula.composite_z | - | 1574 | 0 | 0.0 | 0 | - |
| formula.cvar95 | - | 1574 | 0 | 0.0 | 0 | - |
| formula.mu_band | error | 227 | 1 | 0.4 | 1 | claude-fable-5 |
| formula.target_price | - | 361 | 0 | 0.0 | 0 | - |
| formula.var95 | - | 1574 | 0 | 0.0 | 0 | - |
| horizon.target_offset | - | 1877 | 0 | 0.0 | 0 | - |
| lineage.kelly_raw_method | drift | 1499 | 388 | 25.9 | 21 | claude-fable-5, gemini-3.5-flash, gpt-5 |
| market_forecast.shape | - | 240 | 0 | 0.0 | 0 | - |
| package.core_etf_forecasts | error | 80 | 1 | 1.2 | 1 | gpt-5 |
| schema.enums | - | 1877 | 0 | 0.0 | 0 | - |
| schema.required_fields | - | 1877 | 0 | 0.0 | 0 | - |
| semantics.kelly_025 | - | 1499 | 0 | 0.0 | 0 | - |
| units.cvar95_decimal | drift | 1574 | 106 | 6.7 | 5 | claude-fable-5, claude-opus-4-8 |
| units.kelly_decimal | drift | 1499 | 35 | 2.3 | 2 | claude-fable-5, claude-opus-4-8 |
| units.mu_sigma_decimal | - | 1877 | 0 | 0.0 | 0 | - |
| units.var95_decimal | drift | 1574 | 106 | 6.7 | 5 | claude-fable-5, claude-opus-4-8 |

kelly_025 convention by model:
- claude-fable-5: CAPPED_DECIMAL 360, CAPPED_PERCENT 20
- claude-opus-4-8: CAPPED_MIXED_UNITS 15
- claude-opus-5: CAPPED_DECIMAL 72, UNCAPPED_DECIMAL 314
- claude-sonnet-5: CAPPED_DECIMAL 26, UNCAPPED_DECIMAL 12
- gemini-3.5-flash: CAPPED_DECIMAL 52
- gpt-5: CAPPED_DECIMAL 588, UNCAPPED_DECIMAL 20
- gpt-5.6-sol: CAPPED_DECIMAL 20

Settlement rows use 35 distinct key-sets; legacy field names: settled_on 335,
current_price 152, current_price_date 135, current_price_tag 74, settle_date 17,
settlement_timing_flag 17, settlement_price 12, settlement_date 12.
```

## Appendix B — sources

- Spike code and tests: `src/financial_agent/harness/`, `tests/harness/`,
  `skills/equity-publish-gate/`.
- Run history: `agents/equity/output/*/13_evolution_log.md` and `08_risk_review.md`
  (all read or searched), git history (143 commits; the local clone is shallow).
  Cited as model + date, e.g. "opus-5 08-07".
- Prior plans: `plan/2026-07-15-canonical-settlement-ledger.md`,
  `agents/equity/plan/2026-07-15-claude-fable-5-top-priority.md`.
- Agent Skills specification: agentskills.io/specification (fetched via the
  `agentskills/agentskills` repository); Claude Code skills and Agent SDK
  documentation at code.claude.com/docs.
