# Research notebooks

Saved outputs from the reinforcement-learning and deep-learning experiments that
preceded the quant platform. They are a historical record: they do not feed the
`fa-quant` strategies, and their results have not passed the platform's
validation gates. Re-running them rewrites the outputs; avoid it unless the task
is about the notebook itself.

| Notebook | Contents |
|---|---|
| [rl_portfolio_trading.ipynb](rl_portfolio_trading.ipynb) | Deep RL portfolio trading on the 20 largest S&P 500 stocks, with backtest plots |
| [rl_portfolio_trading_phase2.ipynb](rl_portfolio_trading_phase2.ipynb) | Second phase of the same experiment |
| [env_multistock_cashpenalty.ipynb](env_multistock_cashpenalty.ipynb) | FinRL multi-stock environment with a cash-penalty reward |
| [multistock_docker.ipynb](multistock_docker.ipynb) | FinRL multi-stock PPO run with an out-of-cash penalty |
| [FinRL_freq_model.ipynb](FinRL_freq_model.ipynb) | FinRL on 4-hour bars (Colab) |
| [LSTM_prediction.ipynb](LSTM_prediction.ipynb) | LSTM price prediction with a hyperparameter search |
| [CS230_milestone.ipynb](CS230_milestone.ipynb) | Stanford CS230 project milestone write-up |

Install the stacks with `uv sync --locked --extra rl --extra notebooks` (add
`--extra dl` for the LSTM notebook), then run `uv run --extra notebooks jupyter notebook`.

To keep the repository small, long training logs keep their first and last 40
lines and very long printed lines are clipped; each cut is marked in the output.
Plots are stored as 256-colour PNGs.

The CS230 project write-up is on
[Google Drive](https://drive.google.com/file/d/1-ogSAAA5L0sdy1iLt8HQKwV2kcN1UuCc/view?usp=sharing),
with a [video walkthrough](https://www.youtube.com/watch?v=bE8MFq4sB2k).
