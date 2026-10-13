"""Environment lifecycle and current Gymnasium API integration."""

from typing import Any

import gymnasium as gym
import numpy as np
import pytest

from financial_agent.rl import GymEnvironmentWrapper, SimpleGridWorld


def test_gridworld_reaches_goal_and_requires_reset() -> None:
    env = SimpleGridWorld(grid_size=2, goal_reward=3.0, step_penalty=-0.5)
    state, info = env.reset()
    np.testing.assert_array_equal(state, [0.0, 0.0])
    assert info == {}

    _, reward, terminated, truncated, _ = env.step(1)
    assert (reward, terminated, truncated) == (-0.5, False, False)
    state, reward, terminated, truncated, info = env.step(2)
    np.testing.assert_array_equal(state, [1.0, 1.0])
    assert (reward, terminated, truncated) == (3.0, True, False)
    assert info["distance_to_goal"] == 0

    with pytest.raises(RuntimeError, match="reset"):
        env.step(0)
    env.reset()
    assert not env.done


def test_gridworld_clamps_movement_at_boundaries() -> None:
    env = SimpleGridWorld(grid_size=2)
    env.reset()

    for action in (0, 3):
        state, _, terminated, _, _ = env.step(action)
        np.testing.assert_array_equal(state, [0.0, 0.0])
        assert not terminated


@pytest.mark.parametrize("grid_size", [0, -1])
def test_gridworld_rejects_invalid_sizes(grid_size: int) -> None:
    with pytest.raises(ValueError, match="grid_size"):
        SimpleGridWorld(grid_size=grid_size)


def test_gridworld_requires_reset_before_stepping() -> None:
    with pytest.raises(RuntimeError, match="reset"):
        SimpleGridWorld().step(0)


@pytest.mark.parametrize("action", [-1, 4])
def test_gridworld_rejects_invalid_actions(action: int) -> None:
    env = SimpleGridWorld()
    env.reset()

    with pytest.raises(ValueError, match="action"):
        env.step(action)


def test_gridworld_reset_does_not_reseed_the_global_generator() -> None:
    original_state = np.random.get_state()
    try:
        np.random.seed(123)
        expected = np.random.random()
        np.random.seed(123)

        SimpleGridWorld().reset(seed=456)

        assert np.random.random() == expected
    finally:
        np.random.set_state(original_state)


def test_gymnasium_seed_dimensions_and_time_limit() -> None:
    env = GymEnvironmentWrapper("CartPole-v1", max_episode_steps=1)
    try:
        assert env.get_state_dim() == 4
        assert env.get_action_dim() == 2
        initial_state, _ = env.reset(seed=42)
        repeated_state, _ = env.reset(seed=42)
        np.testing.assert_array_equal(initial_state, repeated_state)

        state, reward, terminated, truncated, _ = env.step(0)
        assert state.shape == (4,)
        assert state.dtype == np.float32
        assert (reward, terminated, truncated) == (1.0, False, True)
        with pytest.raises(RuntimeError, match="reset"):
            env.step(0)
    finally:
        env.close()


def test_gymnasium_requires_reset_before_stepping() -> None:
    env = GymEnvironmentWrapper("CartPole-v1")
    try:
        with pytest.raises(RuntimeError, match="reset"):
            env.step(0)
    finally:
        env.close()


def test_discrete_observations_work_with_the_tabular_agent() -> None:
    from financial_agent.rl import QLearningAgent

    env = GymEnvironmentWrapper("FrozenLake-v1", is_slippery=False)
    try:
        assert env.get_state_dim() == 1
        state, _ = env.reset(seed=42)
        assert state.shape == (1,)
        agent = QLearningAgent(1, env.get_action_dim(), epsilon=0.0)
        assert agent.select_action(state) == 0
    finally:
        env.close()


def test_continuous_action_spaces_are_rejected() -> None:
    with pytest.raises(ValueError, match="Discrete action space"):
        GymEnvironmentWrapper("Pendulum-v1")


def test_gymnasium_render_uses_the_configured_mode() -> None:
    env = GymEnvironmentWrapper("FrozenLake-v1", render_mode="ansi")
    try:
        env.reset(seed=42)
        frame = env.render()

        assert isinstance(frame, str)
        assert "S" in frame
        assert "G" in frame
    finally:
        env.close()


def test_multidimensional_observations_match_the_reported_dimension(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    class MatrixEnvironment(gym.Env[np.ndarray, int]):
        observation_space = gym.spaces.Box(0.0, 1.0, shape=(2, 2), dtype=np.float32)
        action_space = gym.spaces.Discrete(2)

        def reset(
            self,
            *,
            seed: int | None = None,
            options: dict[str, Any] | None = None,
        ) -> tuple[np.ndarray, dict[str, Any]]:
            return np.zeros((2, 2), dtype=np.float32), {}

        def step(
            self, action: int
        ) -> tuple[np.ndarray, float, bool, bool, dict[str, Any]]:
            return np.ones((2, 2), dtype=np.float32), 1.0, False, False, {}

    monkeypatch.setattr(gym, "make", lambda *args, **kwargs: MatrixEnvironment())
    env = GymEnvironmentWrapper("matrix")
    try:
        state, _ = env.reset()
        assert state.shape == (env.get_state_dim(),) == (4,)
        state, *_ = env.step(0)
        np.testing.assert_array_equal(state, [1.0] * 4)
    finally:
        env.close()
