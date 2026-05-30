# AGENTS.md

Guidance for AI coding agents working in this repository.

## Project

Python 3.12 reinforcement-learning framework for financial / portfolio trading. Managed with `uv`. Build backend is `hatchling`; the wheel packages `src/`.

## Layout

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
uv lock
uv sync --locked
uv pip install -e .
uv run jupyter notebook   # for the .ipynb work in notebooks/
```

Run a script: `uv run python example/rl/cartpole_example.py`.

## Conventions

- Python ≥3.12. Type hints required (`disallow_untyped_defs = true` in mypy config).
- Format with `black` (line length 88, target `py312`). Lint with `flake8`. Type-check with `mypy`.
- `numpy<2.0` and `pandas<2.0` are pinned — do not bump without asking.
- Tests use `pytest` (+ `pytest-cov`, `pytest-custom-exit-code`). There is no top-level `tests/` directory yet; co-locate or create one when adding tests.

## Agent rules

1. **Surgical edits.** Touch only what the task requires. Don't reformat or refactor adjacent code, and don't "improve" notebooks you weren't asked to change.
2. **No speculative scaffolding.** The empty `src/financial_agent/agents/{claude,gpt,grok}/` dirs are intentional placeholders — don't fill them unless asked.
3. **Notebooks are outputs.** `.ipynb` files in `notebooks/` contain committed results. Re-running them rewrites cell outputs and inflates diffs; avoid unless the task is about the notebook itself.
4. **Dependencies go in `pyproject.toml`**, then `uv lock`. Do not edit `uv.lock` by hand.
5. **Verify before declaring done.** For code changes, run the relevant example or test with `uv run …` and report the actual output.
