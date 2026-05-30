import numpy as np
from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional, Tuple


class RLAgent(ABC):
    """Base class for reinforcement learning agents."""

    def __init__(self, state_dim: int, action_dim: int, learning_rate: float = 0.01):
        self.state_dim = state_dim
        self.action_dim = action_dim
        self.learning_rate = learning_rate

    @abstractmethod
    def select_action(self, state: np.ndarray) -> int:
        """Select an action given the current state."""
        pass

    @abstractmethod
    def update(self, state: np.ndarray, action: int, reward: float,
               next_state: np.ndarray, done: bool) -> None:
        """Update the agent's policy based on experience."""
        pass


class RandomAgent(RLAgent):
    """Random agent for baseline comparison."""

    def select_action(self, state: np.ndarray) -> int:
        return np.random.randint(0, self.action_dim)

    def update(self, state: np.ndarray, action: int, reward: float,
               next_state: np.ndarray, done: bool) -> None:
        pass


class QLearningAgent(RLAgent):
    """Q-Learning agent implementation."""

    def __init__(self, state_dim: int, action_dim: int,
                 learning_rate: float = 0.1, discount_factor: float = 0.95,
                 epsilon: float = 0.1, epsilon_decay: float = 0.995):
        super().__init__(state_dim, action_dim, learning_rate)
        self.discount_factor = discount_factor
        self.epsilon = epsilon
        self.epsilon_decay = epsilon_decay
        self.q_table = {}

    def _state_to_key(self, state: np.ndarray) -> str:
        """Convert state array to string key for Q-table."""
        return str(tuple(np.round(state, 3)))

    def select_action(self, state: np.ndarray) -> int:
        """Epsilon-greedy action selection."""
        state_key = self._state_to_key(state)

        if np.random.random() < self.epsilon:
            return np.random.randint(0, self.action_dim)

        if state_key not in self.q_table:
            self.q_table[state_key] = np.zeros(self.action_dim)

        return np.argmax(self.q_table[state_key])

    def update(self, state: np.ndarray, action: int, reward: float,
               next_state: np.ndarray, done: bool) -> None:
        """Q-learning update rule."""
        state_key = self._state_to_key(state)
        next_state_key = self._state_to_key(next_state)

        if state_key not in self.q_table:
            self.q_table[state_key] = np.zeros(self.action_dim)
        if next_state_key not in self.q_table:
            self.q_table[next_state_key] = np.zeros(self.action_dim)

        if done:
            target = reward
        else:
            target = reward + self.discount_factor * np.max(self.q_table[next_state_key])

        self.q_table[state_key][action] += self.learning_rate * (
            target - self.q_table[state_key][action]
        )

        self.epsilon = max(0.01, self.epsilon * self.epsilon_decay)