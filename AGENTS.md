# AGENTS.md

## Cursor Cloud specific instructions

### Product overview

This repo is **financial-agent**: a Python reinforcement-learning toolkit with two main areas:

- `src/rl/` — lightweight Q-learning framework and `example/rl/*` demos (GridWorld, CartPole, etc.).
- `src/core_trading/` — FinRL-style stock portfolio RL (TensorFlow, Stable-Baselines3, notebooks). Requires the full dependency set.

### Python toolchain

- **Python**: 3.12+ (`requires-python` in `pyproject.toml`).
- **Package manager**: [uv](https://github.com/astral-sh/uv). Install if missing: `curl -LsSf https://astral.sh/uv/install.sh | sh`, then `export PATH="$HOME/.local/bin:$PATH"`.

### Dependency install caveat (important)

`uv sync --locked` (as in `README.md`) **fails on Python 3.12** because the project pins `pandas<2.0.0` (resolves to 1.5.3), which has no compatible wheels and does not build cleanly on 3.12.

For Cloud Agent / local dev on 3.12, use the workaround in the VM update script (editable install + explicit deps with `pandas>=2.2`) until `pyproject.toml` constraints are updated. Stock-trading notebooks may need API keys / market data; the RL examples do not.

### Running the RL framework (recommended smoke test)

```bash
source .venv/bin/activate
export PYTHONPATH=src
python example/rl/basic_rl_example.py
python example/rl/cartpole_example.py
# or: python example/rl/run_all_examples.py
```

Note: examples use `sys.path.insert(..., '..', 'src')` from `example/rl/`, which resolves to `example/src` (missing). **`PYTHONPATH=src`** (repo root) is required unless that path is fixed.

### Lint / typecheck

From repo root with `.venv` activated:

```bash
black --check src/rl example/rl
flake8 src/rl example/rl
mypy src/rl
```

There is no `pytest` suite in the repo today; use the RL example scripts as integration checks.

### Jupyter (README “Start” flow)

```bash
source .venv/bin/activate
uv run jupyter notebook --no-browser --ip=127.0.0.1 --port=8888
```

Notebooks live under `src/core_trading/` (e.g. `rl_portfolio_trading.ipynb`).

### Core trading entrypoint

From `src/core_trading/` (needs full TensorFlow / FinRL deps):

```bash
python main.py --mode train
python main.py --mode download_data
```

Full `uv sync --locked` must succeed (or equivalent manual installs) before this path is usable.
