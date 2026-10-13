# AGENTS.md

Guidance for AI coding agents working in this repository.

## Project

Python 3.12 risk-managed systematic ETF platform plus financial/RL research. Managed with `uv`. Build backend is `hatchling`; the wheel packages `src/`.

## Layout

- `src/financial_agent/quant/` — data, strategies, backtest, validation, risk, execution, runner, CLI and paper-only MCP.
- `tests/quant/` — deterministic, network-free regression tests mirroring quant modules.
- `docs/quant/`, `reports/quant/`, `examples/quant/`, `deploy/quant/` — operator guides, evidence, paper configs and scheduler templates.
- `src/financial_agent/harness/` — equity schemas, gates, arithmetic and audits.
- `agents/equity/`, `skills/`, `docs/research/` — daily and native sourced research workflows.
- `src/financial_agent/rl/` — generic RL primitives (`agent.py`, `environment.py`, `trainer.py`).
- `src/financial_agent/dl/` — deep-learning baselines (LSTM, data windowing).
- `src/financial_agent/trading/` — trading-specific code (`env/`, `model/`, `preprocessing/`, `marketdata/`, `autotrain/`, `config/`, `backtest.py`, `utils/`).
- `src/financial_agent/agents/{claude,gpt,grok}/` — placeholders for LLM-agent variants (currently empty).
- `notebooks/` — Jupyter notebooks (committed with outputs).
- `archive/` — frozen old notebooks.
- `assets/img/` — images referenced by notebooks/READMEs.
- `example/rl/` — runnable Gymnasium examples (CartPole, Acrobot, MountainCar).
- `pyproject.toml` is the source of truth for dependencies.

## Setup & run

```shell
uv sync --locked                       # core + default dev tools
uv sync --locked --no-dev               # core runtime only
uv sync --locked --extra rl             # financial trading experiments
uv sync --locked --extra dl             # TensorFlow prediction baselines
uv sync --locked --all-extras           # all research stacks + dev tools
uv run --extra notebooks jupyter notebook
```

The `all` extra combines `rl`, `dl`, and `notebooks`; the `dev` extra matches
uv's default `dev` dependency group. Sync installs the package in editable mode.
Run `uv lock` after changing dependencies, not as part of normal setup.

Offline quickstart: `uv run fa-quant demo` and `uv run fa-quant --help`.
See `docs/quant/strategy-research.md` for dated real-data CLI commands.

```shell
uv run pytest tests agents/equity/daily_investment_system/tests -q
uv run black --check src/financial_agent/rl tests/rl src/financial_agent/quant tests/quant
uv run flake8 src/financial_agent/rl tests/rl src/financial_agent/quant tests/quant
uv run mypy src/financial_agent/quant src/financial_agent/rl src/financial_agent/harness
uv build
```

## Quant rules

- Preserve the binding names/signatures in plan section 3.2; update it alongside any minimal deviation.
- Strategies see only decision prefixes; fills occur later; modeled costs stay enabled.
- Disclose every grid, failure and undefined statistic. Never tune policy or parameters to make an evidence report pass. Live performance is unproven.
- Run configs may only tighten risk. Certificate, Alpaca-paper evidence and explicit live opt-in are independent gates. MCP cannot submit orders or accept live config.
- Keep credentials in the environment only. Preserve journals, deterministic client IDs and persistent kill state. Kill does not cancel or liquidate.
- Tests under `tests/quant/` use seeded synthetic data or tiny fixtures; no network in normal CI. Exercise observable boundaries and failures.
- Never commit raw market downloads or operational state (`var/`, `.quant-cache/`); retain dated aggregate evidence in `reports/quant/`.
- Historical `trading/` and `dl/` experiments are not the live execution path. Do not rerun saved notebooks incidentally.

## Conventions

- Python ≥3.12. Type hints required (`disallow_untyped_defs = true` in mypy config).
- Format with `black` (line length 88, target `py312`). Lint with `flake8`. Type-check with `mypy`.
- `numpy<2.0` and `pandas>=2.0,<3` are pinned — do not bump without asking.
- Tests use `pytest` (+ `pytest-cov`, `pytest-custom-exit-code`). Tests live under `tests/` (quant, RL, harness) and the daily equity helper test directory.

## Agent rules

1. **Surgical edits.** Touch only what the task requires. Don't reformat or refactor adjacent code, and don't "improve" notebooks you weren't asked to change.
2. **No speculative scaffolding.** The empty `src/financial_agent/agents/{claude,gpt,grok}/` dirs are intentional placeholders — don't fill them unless asked.
3. **Notebooks are outputs.** `.ipynb` files in `notebooks/` contain committed results. Re-running them rewrites cell outputs and inflates diffs; avoid unless the task is about the notebook itself.
4. **Dependencies go in `pyproject.toml`**, then `uv lock`. Do not edit `uv.lock` by hand.
5. **Verify before declaring done.** For code changes, run the relevant example or test with `uv run …` and report the actual output.

## Git and pull requests

1. **No assistant attribution.** Nothing pushed to GitHub may name the coding assistant or tool that produced it: branch names (no `claude/` or similar prefix), commit messages, `Co-authored-by` trailers, commit author/committer, PR titles and descriptions, review replies, and PR comments. No "Generated with …" footers or session links. Model names that are part of the data (e.g. a daily-run package such as `claude-opus-5-2026-09-03`) are fine.
2. **Branch prefixes** describe the change: `feat/`, `fix/`, `docs/`, `ci/`, `chore/`, `refactor/`, `test/`, or `run/` for daily-run packages.
3. **Scope feature work into a sequence of PRs.** Split a new feature into small, independently reviewable PRs (at most 10 per feature), each with one purpose and passing CI on its own.
4. **Land them sequentially.** Open each PR from the latest `main`, merge it, then branch the next one from the updated `main`. Don't stack branches on unmerged work or merge out of order.
