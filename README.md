# financial-agent

A Python research repository for reinforcement learning in financial markets,
portfolio simulation, and evidence-backed equity research. It combines a small
generic RL framework with trading experiments, historical notebooks, and
deterministic tools for checking equity-research reports.

**Status:** the package is version `0.1.0` and classified as alpha. The components
have different levels of completeness; this is not a verified live-trading
system, and neither saved notebook outputs nor published reports establish
investment performance. Use it for research and education, not investment advice.

## What is here

- **Generic RL:** tabular Q-learning and a random baseline, a GridWorld
  environment, a Gymnasium wrapper, and training/evaluation loops. Examples
  cover GridWorld, CartPole, Acrobot, and MountainCar.
- **Financial RL experiments:** Yahoo Finance data loading, technical-feature
  preprocessing, stock/portfolio simulation environments (including cash-penalty
  and stop-loss variants), Stable-Baselines3 model wrappers for A2C, DDPG, PPO,
  SAC, and TD3, and backtest utilities.
- **Equity research:** a prompt-driven daily research workflow with source and
  prediction ledgers; deterministic universe, indicator, scoring, diagnostic,
  and settlement helpers; and a Python harness for schema validation,
  publication gates, status replay, audits, and risk/portfolio calculations.
- **Turtle strategy research:** a rule-based breakout scanner and
  per-instrument backtester, with offline CSV input as well as online data.

The `src/financial_agent/agents/{claude,gpt,grok}/` packages are empty placeholders,
not implemented model agents. The equity prompt workflow lives separately under
`agents/equity/` and requires an agent runtime and sourced inputs.

## Setup

Run commands from the repository root. Install
[uv](https://docs.astral.sh/uv/getting-started/installation/) first; the project
requires **Python ≥3.12**, with 3.12 a practical starting point for the scientific
dependency stack. The committed `.python-version` selects 3.12 for `uv` commands;
the locked TensorFlow version does not support newer Python versions.

```sh
uv sync --locked --python 3.12
```

This uses the committed `uv.lock` and installs the local package in editable mode;
a separate `uv pip install -e .` or `uv lock` is not needed for normal setup.
Dependencies are defined in [`pyproject.toml`](pyproject.toml): NumPy
`>=1.24,<2`, pandas `>=2,<3`, Gymnasium, Stable-Baselines3, TensorFlow,
`keras-nightly`, notebook/plotting tools, yfinance, stockstats, and
`pyfolio-reloaded`, among others. Even the small RL example installs this full
stack; there is no lightweight RL-only extra.

For the complete development extra:

```sh
uv sync --locked --python 3.12 --extra dev
```

The `dev` extra contains Black, flake8, mypy, pytest, pytest-cov, and
pytest-custom-exit-code. The default uv `dev` dependency group contains only
Black, flake8, mypy, and pytest; Black and mypy are also main dependencies.

Run the same checks used by the Python quality workflow:

```sh
uv run pytest tests agents/equity/daily_investment_system/tests -q
uv run black --check src/financial_agent/rl tests/rl
uv run flake8 src/financial_agent/rl tests/rl
uv run mypy src/financial_agent/rl src/financial_agent/harness
```

Tests cover the RL core, harness, and daily equity helpers. Formatting and lint
checks currently cover the RL core and its tests; type checks cover RL and the
harness. The separate Harness workflow also checks report publication gates.

## Try a bounded RL example

This uses the public RL API to train on a local 5×5 GridWorld, without fetching
market data or opening a graphical window. Training stops after 20 episodes,
with at most 50 steps per episode.

```sh
uv run python - <<'PY'
from financial_agent.rl import QLearningAgent, SimpleGridWorld, Trainer

env = SimpleGridWorld(grid_size=5, goal_reward=10.0, step_penalty=-0.1)
agent = QLearningAgent(
    state_dim=env.get_state_dim(),
    action_dim=env.get_action_dim(),
    learning_rate=0.1,
    epsilon=0.9,
)
history = Trainer(agent, env).train(
    num_episodes=20, max_steps_per_episode=50, log_interval=10
)
print("Episodes:", len(history["episode_rewards"]))
print("Last episode reward:", history["episode_rewards"][-1])
PY
```

The loop logs average rewards and episode lengths. Rewards vary; this short run
demonstrates the API, not convergence or financial returns. For a longer,
time-limited Gymnasium task:

```sh
uv run python example/rl/cartpole_example.py
```

That script trains for 1,000 episodes (up to 500 steps each), evaluates five
episodes, and prints reward/length statistics.

Training and evaluation both have a `max_steps_per_episode` limit (default:
1,000). Time-limit truncation ends an episode while preserving the Q-learning
bootstrap; only terminal states suppress it. The Gymnasium wrapper accepts
zero-based discrete actions, flattens numeric observations, and requires
`reset()` before the first step and after an episode ends. To render, configure
the mode at creation, such as `GymEnvironmentWrapper("FrozenLake-v1",
render_mode="ansi")`.

## Explore the research workflows

### Notebooks and financial simulation

```sh
uv run jupyter notebook
```

Start with [`notebooks/rl_portfolio_trading.ipynb`](notebooks/rl_portfolio_trading.ipynb)
for portfolio RL or [`notebooks/LSTM_prediction.ipynb`](notebooks/LSTM_prediction.ipynb)
for prediction experiments. These are historical notebooks with saved outputs;
inspect their imports, data requirements, and assumptions before rerunning.
The [`notebook notes`](notebooks/README.md) link to the original write-up and
video, rather than serving as a current performance benchmark.

### Repository-native ticker research

Browse [the dated research index](docs/research/index.md) for the retained 50-security
scan, conditional model targets, declared horizons and source gaps. Read
[run guidance](docs/research/README.md) before collecting or changing evidence.

The [native skill graph](skills/equity-investment-research/README.md) separates nine
analytical nodes from Decimal arithmetic and the structural/evidence audit.
Optional earnings, cash-flow DCF and peer-comparison skills share the ticker/date
workspace; they do not replace the core EPS/exit-multiple model or its audit.

```sh
uv sync --locked --python 3.12 --extra research
uv run --python 3.12 --extra research python \
  skills/equity-investment-research/scripts/research.py plan \
  --tickers INTC CRM --as-of 2026-10-12 \
  --skills earnings-analysis dcf-model comps-analysis
```

`plan` prints instructions, prerequisites and destinations; it does not perform
research. Canonical source lives in `skills/`, with shared discovery links under
`.agents/skills/`. Reports remain in
`docs/research/tickers/TICKER/DATE/`; inputs, calculations and audits remain in
that run's `data/` folder. Shared verification belongs in `batches/DATE/`.

Existing reports are provisional research, not investment approval. Source
coverage and model timing gaps remain explicit. Openpyxl writes formulas but
cannot recalculate them; actual Excel/LibreOffice recalculation is required before
relying on workbook values. No orders, broker actions or autonomous trading.
### Daily equity research and report checks

Read the [`workflow entrypoint`](agents/equity/daily_investment_system/main.md),
then its linked rules, agent stages, and runbook. The workflow covers regime
analysis, factor scoring, portfolio construction, risk review, and prediction
settlement. Durable dated packages live under
[`agents/equity/output/`](agents/equity/output/); temporary computations belong
under the gitignored `agents/equity/.work/`.

The harness can inspect the contract and audit existing ledgers locally:

```sh
uv run python -m financial_agent.harness --help
uv run python -m financial_agent.harness schema --json-schema
uv run python -m financial_agent.harness audit --output-dir agents/equity/output
```

See the [`publication-gate guide`](skills/equity-publish-gate/SKILL.md) for
checking a finished package with `gate`, generating manifest sections, and
replaying status. Passing a gate checks the report's contract and formulas; it
does not independently verify market-data provenance or make a trade safe.
The harness `run` command currently registers only precheck and reflection
handlers and halts at missing later stages; it does **not** autonomously complete
the prompt workflow. The runbook describes manual operation, with no active
scheduler.

### Offline Turtle scanner

Use the bundled `DEMO.csv` fixture for a finite, network-free scan:

```sh
uv run python agents/equity/turtle-trader/turtle.py \
  --mode scan --tickers DEMO \
  --history-dir agents/equity/turtle-trader/fixtures \
  --account 100000 --pretty
```

This prints JSON signals and sizing calculations for fixture data, not today's
market. The [`Turtle operating guide`](agents/equity/turtle-trader/SKILL.md)
documents live scans, historical backtests, rules, and flags. Online fetching
and universe refresh have additional requirements in
[`requirements.txt`](agents/equity/turtle-trader/requirements.txt), including
`lxml`. Its backtests are per-instrument, not portfolio simulations, and the
tool does not place orders.

## Repository map

| Path | Purpose |
| --- | --- |
| [`src/financial_agent/rl/`](src/financial_agent/rl/) | Agent/environment interfaces and training loops |
| [`example/rl/`](example/rl/) | Runnable generic RL examples |
| [`src/financial_agent/trading/`](src/financial_agent/trading/) | Market data, preprocessing, financial environments, model wrappers, backtesting |
| [`src/financial_agent/dl/`](src/financial_agent/dl/) | TensorFlow baseline and data-windowing utilities |
| [`src/financial_agent/harness/`](src/financial_agent/harness/) | Research CLI, deterministic checks, kernels, and `equity_policy.toml` |
| [`agents/equity/daily_investment_system/`](agents/equity/daily_investment_system/) | Prompt workflow, compute helpers, and helper tests |
| [`agents/equity/turtle-trader/`](agents/equity/turtle-trader/) | Turtle scanner/backtester, fixtures, and universe caches |
| [`tests/harness/`](tests/harness/) | Harness tests |
| [`tests/rl/`](tests/rl/) | RL learning, trainer, and environment regression tests |
| [`notebooks/`](notebooks/) / [`archive/`](archive/) | Current experiment notebooks / older notebooks |
| [`pure_prompt_coding/equity/`](pure_prompt_coding/equity/) | Prompt-based research material and outputs |

## Limitations

- Training/evaluation is stochastic; no reproducible return or outperformance
  guarantee is provided here. Historical results require scrutiny of data
  splits, costs, leakage, and market assumptions.
- The generic Q-learning agent uses a tabular state key rounded to three decimal
  places; the Gymnasium examples are learning demonstrations, not deep-RL
  baselines.
- Financial training code is experimental. In particular,
  `trading/autotrain/training.py` currently calls `DRL_prediction` with a
  mismatched signature and references an undefined `BackTestStats`; it is not a
  turnkey training entrypoint.
- Online workflows depend on external data availability and freshness. Missing
  research inputs must be disclosed rather than replaced with fabricated data.

## License

[MIT](LICENSE), copyright © 2025 Kenneth. The software is provided “as is,”
without warranty.
