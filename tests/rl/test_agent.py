"""Regression coverage for tabular learning and action selection."""

import numpy as np
import pytest

from financial_agent.rl import QLearningAgent, RandomAgent


@pytest.mark.parametrize("epsilon", [0.0, 1.0])
def test_q_learning_returns_a_python_action(epsilon: float) -> None:
    agent = QLearningAgent(state_dim=2, action_dim=4, epsilon=epsilon)

    action = agent.select_action(np.zeros(2))

    assert type(action) is int
    assert 0 <= action < 4


def test_random_agent_returns_a_python_action() -> None:
    agent = RandomAgent(state_dim=2, action_dim=4)

    action = agent.select_action(np.zeros(2))

    assert type(action) is int
    assert 0 <= action < 4


@pytest.mark.parametrize("terminal, expected", [(True, 2.0), (False, 7.0)])
def test_q_learning_bootstraps_only_nonterminal_states(
    terminal: bool, expected: float
) -> None:
    agent = QLearningAgent(
        state_dim=1, action_dim=2, learning_rate=1.0, discount_factor=0.5
    )
    state, next_state = np.array([0.0]), np.array([1.0])
    agent.q_table[agent._state_to_key(next_state)] = np.array([10.0, 4.0])

    agent.update(state, 1, 2.0, next_state, terminal)

    assert agent.q_table[agent._state_to_key(state)][1] == expected


def test_q_learning_uses_the_highest_valued_action() -> None:
    agent = QLearningAgent(state_dim=1, action_dim=3, epsilon=0.0)
    state = np.array([1.0])
    agent.q_table[agent._state_to_key(state)] = np.array([1.0, 5.0, 2.0])

    assert agent.select_action(state) == 1
