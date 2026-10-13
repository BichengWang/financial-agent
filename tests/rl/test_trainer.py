"""Finite training/evaluation and termination semantics."""

from typing import Any

import numpy as np
import pytest

from financial_agent.rl import Environment, QLearningAgent, RLAgent, Trainer


class CountingEnvironment(Environment):
    def __init__(self, terminated: bool = False, truncated: bool = False) -> None:
        super().__init__()
        self.terminated = terminated
        self.truncated = truncated
        self.steps = 0
        self.resets = 0

    def reset(
        self, seed: int | None = None, options: dict[str, Any] | None = None
    ) -> tuple[np.ndarray, dict[str, Any]]:
        self.steps = 0
        self.resets += 1
        return np.array([0.0]), {}

    def step(self, action: int) -> tuple[np.ndarray, float, bool, bool, dict[str, Any]]:
        self.steps += 1
        return np.array([1.0]), 2.0, self.terminated, self.truncated, {}

    def get_state_dim(self) -> int:
        return 1

    def get_action_dim(self) -> int:
        return 1


class RecordingAgent(RLAgent):
    def __init__(self) -> None:
        super().__init__(state_dim=1, action_dim=1)
        self.terminal_flags: list[bool] = []

    def select_action(self, state: np.ndarray) -> int:
        return 0

    def update(
        self,
        state: np.ndarray,
        action: int,
        reward: float,
        next_state: np.ndarray,
        done: bool,
    ) -> None:
        self.terminal_flags.append(done)


@pytest.mark.parametrize(
    "terminated, truncated, expected",
    [(False, True, 7.0), (True, False, 2.0), (True, True, 2.0)],
)
def test_training_distinguishes_time_limits_from_terminal_states(
    terminated: bool, truncated: bool, expected: float
) -> None:
    env = CountingEnvironment(terminated=terminated, truncated=truncated)
    agent = QLearningAgent(
        state_dim=1, action_dim=1, learning_rate=1.0, discount_factor=0.5
    )
    agent.q_table[agent._state_to_key(np.array([1.0]))] = np.array([10.0])

    history = Trainer(agent, env).train(1, max_steps_per_episode=3)

    assert history == {"episode_rewards": [2.0], "episode_lengths": [1]}
    assert agent.q_table[agent._state_to_key(np.array([0.0]))][0] == expected


def test_training_caps_episodes_without_marking_them_terminal() -> None:
    env, agent = CountingEnvironment(), RecordingAgent()
    trainer = Trainer(agent, env)

    history = trainer.train(2, max_steps_per_episode=3, log_interval=1)

    assert history == {"episode_rewards": [6.0, 6.0], "episode_lengths": [3, 3]}
    assert env.resets == 2
    assert agent.terminal_flags == [False] * 6
    assert trainer.training_history == [history]


def test_evaluation_caps_episodes_without_updating_the_agent() -> None:
    env, agent = CountingEnvironment(), RecordingAgent()

    results = Trainer(agent, env).evaluate(2, max_steps_per_episode=3)

    assert results == {
        "mean_reward": 6.0,
        "std_reward": 0.0,
        "mean_length": 3.0,
        "std_length": 0.0,
        "episode_rewards": [6.0, 6.0],
        "episode_lengths": [3, 3],
    }
    assert type(results["mean_reward"]) is float
    assert env.resets == 2
    assert agent.terminal_flags == []


@pytest.mark.parametrize("terminated, truncated", [(True, False), (False, True)])
def test_evaluation_stops_on_either_episode_boundary(
    terminated: bool, truncated: bool
) -> None:
    env = CountingEnvironment(terminated=terminated, truncated=truncated)

    results = Trainer(RecordingAgent(), env).evaluate(2)

    assert results["episode_lengths"] == [1, 1]
    assert results["episode_rewards"] == [2.0, 2.0]


@pytest.mark.parametrize("value", [0, -1])
@pytest.mark.parametrize(
    "parameter", ["num_episodes", "max_steps_per_episode", "log_interval"]
)
def test_training_rejects_invalid_limits(parameter: str, value: int) -> None:
    env = CountingEnvironment()
    kwargs = {"num_episodes": 1, parameter: value}

    with pytest.raises(ValueError, match=parameter):
        Trainer(RecordingAgent(), env).train(**kwargs)

    assert env.resets == 0


@pytest.mark.parametrize("value", [0, -1])
@pytest.mark.parametrize("parameter", ["num_episodes", "max_steps_per_episode"])
def test_evaluation_rejects_invalid_limits(parameter: str, value: int) -> None:
    env = CountingEnvironment()
    kwargs = {"num_episodes": 1, parameter: value}

    with pytest.raises(ValueError, match=parameter):
        Trainer(RecordingAgent(), env).evaluate(**kwargs)

    assert env.resets == 0
