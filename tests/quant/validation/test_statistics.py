"""Independent formula calculations and selection-bias sanity checks."""

import math
from statistics import NormalDist

import numpy as np
import pandas as pd  # type: ignore[import-untyped]
import pytest

from financial_agent.quant.validation import (
    block_bootstrap_ci,
    deflated_sharpe_ratio,
    expected_max_sharpe,
    pbo_cscv,
    probabilistic_sharpe_ratio,
)


def independent_psr(x: np.ndarray, benchmark: float) -> float:
    n = len(x)
    centered = x - x.mean()
    m2 = float(np.mean(centered**2))
    skew = math.sqrt(n * (n - 1)) / (n - 2) * float(np.mean(centered**3)) / m2**1.5
    excess = (
        (n - 1)
        / ((n - 2) * (n - 3))
        * ((n + 1) * (float(np.mean(centered**4)) / m2**2 - 3) + 6)
    )
    sr = float(x.mean() / x.std(ddof=1))
    z = (
        (sr - benchmark)
        * math.sqrt(n - 1)
        / math.sqrt(1 - skew * sr + (excess + 2) / 4 * sr**2)
    )
    return NormalDist().cdf(z)


def test_psr_and_dsr_independent_formulas_and_trial_penalty() -> None:
    x = np.array([0.01, -0.02, 0.008, 0.012, -0.005, 0.015, 0.004, 0.007])
    gamma, n, variance = 0.5772156649015329, 12, 0.02
    benchmark = math.sqrt(variance) * (
        (1 - gamma) * NormalDist().inv_cdf(1 - 1 / n)
        + gamma * NormalDist().inv_cdf(1 - 1 / (n * math.e))
    )
    assert expected_max_sharpe(n, variance) == pytest.approx(benchmark)
    assert probabilistic_sharpe_ratio(x) == pytest.approx(independent_psr(x, 0))
    dsr = deflated_sharpe_ratio(x, n_trials=n, trials_sharpe_variance=variance)
    assert dsr == pytest.approx(independent_psr(x, benchmark))
    assert dsr < probabilistic_sharpe_ratio(x)
    assert dsr < deflated_sharpe_ratio(
        x, n_trials=n, trials_sharpe_variance=variance / 10
    )
    assert expected_max_sharpe(1, variance) == 0


def test_best_noise_trial_has_high_raw_sharpe_but_not_significant_dsr() -> None:
    trials = np.random.default_rng(42).normal(0, 0.01, (252, 100))
    sharpes = trials.mean(axis=0) / trials.std(axis=0, ddof=1)
    winner = int(np.argmax(sharpes))
    assert sharpes[winner] * math.sqrt(252) > 1.5
    assert (
        deflated_sharpe_ratio(
            trials[:, winner],
            n_trials=100,
            trials_sharpe_variance=float(sharpes.var(ddof=1)),
        )
        < 0.95
    )


def test_cscv_noise_edge_partitions_ties_and_leading_remainder() -> None:
    rng = np.random.default_rng(18)
    noise = pd.DataFrame(rng.normal(0, 0.01, (2000, 12)))
    noise_probabilities = [pbo_cscv(noise, 8).pbo]
    for _ in range(11):
        noise_probabilities.append(
            pbo_cscv(pd.DataFrame(rng.normal(0, 0.01, (2000, 12))), 8).pbo
        )
    assert float(np.mean(noise_probabilities)) > 0.3
    assert float(np.mean(noise_probabilities)) == pytest.approx(0.5, abs=0.15)
    edge = noise.copy()
    edge[0] += 0.006
    result = pbo_cscv(edge, 8)
    assert result.pbo < 0.1
    assert result.n_combinations == math.comb(8, 4)
    assert len(result.logits) == result.n_combinations
    extended = pd.concat([pd.DataFrame([[100] * 12]), edge], ignore_index=True)
    assert pbo_cscv(extended, 8) == result
    identical = pd.DataFrame({"a": noise[0], "b": noise[0]})
    tied = pbo_cscv(identical, 8)
    assert tied.pbo == 1
    assert set(tied.logits) == {0.0}


def test_cscv_matches_independent_rank_calculation() -> None:
    from itertools import combinations

    values = np.random.default_rng(7).normal(size=(24, 4))
    blocks = np.arange(24).reshape(4, 6)
    expected = []
    for chosen in combinations(range(4), 2):
        train = values[blocks[list(chosen)].ravel()]
        test = values[blocks[[i for i in range(4) if i not in chosen]].ravel()]
        winner = int(np.argmax(train.mean(axis=0) / train.std(axis=0, ddof=1)))
        ranks = pd.Series(test.mean(axis=0) / test.std(axis=0, ddof=1)).rank()
        omega = ranks[winner] / 5
        expected.append(math.log(omega / (1 - omega)))
    assert pbo_cscv(pd.DataFrame(values), 4).logits == pytest.approx(expected)


def test_circular_bootstrap_matches_independent_draws_and_seed() -> None:
    values = np.arange(7, dtype=float)
    rng = np.random.default_rng(5)
    stats = []
    for _ in range(200):
        sample = []
        for start in rng.integers(0, 7, size=3):
            sample.extend(values[(start + np.arange(3)) % 7])
        stats.append(float(np.mean(sample[:7])))
    expected = np.quantile(stats, [0.05, 0.95])
    result = block_bootstrap_ci(
        values, lambda x: float(x.mean()), n=200, block=3, seed=5
    )
    assert result == pytest.approx(expected)
    assert result == block_bootstrap_ci(
        values, lambda x: float(x.mean()), n=200, block=3, seed=5
    )
    assert result != block_bootstrap_ci(
        values, lambda x: float(x.mean()), n=200, block=3, seed=6
    )


@pytest.mark.parametrize("values", [[1, 2, 3], [1, 1, 1, 1], [1, 2, 3, np.nan]])
def test_psr_rejects_unusable_data(values: list[float]) -> None:
    with pytest.raises(ValueError):
        probabilistic_sharpe_ratio(values)


@pytest.mark.parametrize("trials,variance", [(0, 1), (True, 1), (2, -1), (2, np.inf)])
def test_expected_max_rejects_invalid_trials(trials: int, variance: float) -> None:
    with pytest.raises(ValueError):
        expected_max_sharpe(trials, variance)


@pytest.mark.parametrize(
    "splits,rows,columns", [(3, 20, 3), (4, 3, 3), (4, 20, 1), (2, 2, 2)]
)
def test_pbo_rejects_invalid_dimensions(splits: int, rows: int, columns: int) -> None:
    with pytest.raises(ValueError):
        pbo_cscv(pd.DataFrame(np.ones((rows, columns))), splits)


@pytest.mark.parametrize("n,block,alpha", [(0, 2, 0.1), (10, 0, 0.1), (10, 2, 1.0)])
def test_bootstrap_rejects_invalid_controls(n: int, block: int, alpha: float) -> None:
    with pytest.raises(ValueError):
        block_bootstrap_ci(
            [1, 2, 3], lambda x: float(x.mean()), n=n, block=block, seed=0, alpha=alpha
        )


def test_bootstrap_rejects_undefined_statistic() -> None:
    with pytest.raises(ValueError, match="statistic"):
        block_bootstrap_ci([1, 2, 3], lambda x: float("nan"), n=2, block=2, seed=0)
