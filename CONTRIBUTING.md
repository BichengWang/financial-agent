# Contributing

Thanks for helping. Bug reports, evidence reviews and focused pull requests are
all welcome. For anything larger than a fix, open an issue first so the design
can be agreed before you write code.

## Setup

Install [uv](https://docs.astral.sh/uv/getting-started/installation/), then from
the repository root:

```sh
uv sync --locked --all-extras
uv run fa-quant demo
```

Python 3.12 is the tested version. Dependencies live in `pyproject.toml`; after
changing them run `uv lock` and commit both files. Do not edit `uv.lock` by hand
or bump the NumPy `<2` and pandas `<3` pins without discussing it first.

## Checks

CI runs these on every pull request that touches code; run them before pushing:

```sh
uv run pytest tests agents/equity/daily_investment_system/tests -q
uv run black --check src/financial_agent/rl tests/rl src/financial_agent/quant tests/quant
uv run flake8 src/financial_agent/rl tests/rl src/financial_agent/quant tests/quant
uv run mypy src/financial_agent/quant src/financial_agent/rl src/financial_agent/harness
uv run --only-group docs mkdocs build --strict
```

Tests must stay deterministic and offline: use seeded synthetic data or small
fixtures, never network calls.

## Quant changes

- Strategies see only data available at the decision time; fills happen later and
  modeled costs stay on.
- Disclose every parameter grid, failure and undefined statistic. Never tune a
  strategy or threshold to make an evidence report pass.
- Configs may only tighten risk limits. Do not weaken the certificate, paper
  evidence or live opt-in gates.
- Keep credentials in environment variables. Never commit market downloads or
  runtime state (`var/`, `.quant-cache/`); commit dated aggregate evidence under
  `reports/quant/`.

## Notebooks

Files in `notebooks/` are saved research outputs. Don't re-run or reformat them
unless the change is about that notebook, and keep their outputs small.

## Pull requests

- Branch from the latest `main` with a prefix that names the change: `feat/`,
  `fix/`, `docs/`, `ci/`, `chore/`, `refactor/` or `test/`.
- Keep each pull request to one purpose, and split larger features into a short
  series that lands in order.
- Use [Conventional Commits](https://www.conventionalcommits.org/) titles, such as
  `fix(quant): reject stale certificates`.
- Add user-visible changes to the `Unreleased` section of
  [CHANGELOG.md](CHANGELOG.md).

By contributing you agree that your work is released under the [MIT License](LICENSE).
