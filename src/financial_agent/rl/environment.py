import numpy as np
from abc import ABC, abstractmethod
from typing import Any
import gymnasium as gym


class Environment(ABC):
    """Base class for RL environments."""

    def __init__(self) -> None:
        self.state: np.ndarray | None = None
        self.done = False

    @abstractmethod
    def reset(
        self, seed: int | None = None, options: dict[str, Any] | None = None
    ) -> tuple[np.ndarray, dict[str, Any]]:
        """Reset environment to initial state."""
        pass

    @abstractmethod
    def step(self, action: int) -> tuple[np.ndarray, float, bool, bool, dict[str, Any]]:
        """Take a step in the environment."""
        pass

    @abstractmethod
    def get_state_dim(self) -> int:
        """Get the dimensionality of the state space."""
        pass

    @abstractmethod
    def get_action_dim(self) -> int:
        """Get the dimensionality of the action space."""
        pass


class SimpleGridWorld(Environment):
    """Simple grid world environment for testing."""

    def __init__(
        self, grid_size: int = 5, goal_reward: float = 10.0, step_penalty: float = -0.1
    ) -> None:
        super().__init__()
        if grid_size <= 0:
            raise ValueError("grid_size must be positive")
        self.grid_size = grid_size
        self.goal_reward = goal_reward
        self.step_penalty = step_penalty
        self.goal_pos = (grid_size - 1, grid_size - 1)
        self.agent_pos: tuple[int, int] | None = None

    def reset(
        self, seed: int | None = None, options: dict[str, Any] | None = None
    ) -> tuple[np.ndarray, dict[str, Any]]:
        """Reset to the deterministic starting position without reseeding NumPy."""
        self.agent_pos = (0, 0)
        self.done = False
        return np.array(self.agent_pos, dtype=np.float32), {}

    def step(self, action: int) -> tuple[np.ndarray, float, bool, bool, dict[str, Any]]:
        """
        Take a step in the grid world.
        Actions: 0=up, 1=right, 2=down, 3=left
        """
        if self.agent_pos is None or self.done:
            raise RuntimeError("Call reset() before stepping a new episode")
        if action not in range(self.get_action_dim()):
            raise ValueError("action must be between 0 and 3")

        x, y = self.agent_pos

        if action == 0 and y > 0:  # up
            y -= 1
        elif action == 1 and x < self.grid_size - 1:  # right
            x += 1
        elif action == 2 and y < self.grid_size - 1:  # down
            y += 1
        elif action == 3 and x > 0:  # left
            x -= 1

        self.agent_pos = (x, y)

        if self.agent_pos == self.goal_pos:
            reward = self.goal_reward
            self.done = True
        else:
            reward = self.step_penalty

        info = {
            "agent_pos": self.agent_pos,
            "goal_pos": self.goal_pos,
            "distance_to_goal": abs(self.agent_pos[0] - self.goal_pos[0])
            + abs(self.agent_pos[1] - self.goal_pos[1]),
        }

        return (
            np.array(self.agent_pos, dtype=np.float32),
            reward,
            self.done,
            False,
            info,
        )

    def get_state_dim(self) -> int:
        return 2

    def get_action_dim(self) -> int:
        return 4

    def render(self) -> str:
        """Render the current state of the grid world."""
        grid = [["." for _ in range(self.grid_size)] for _ in range(self.grid_size)]
        grid[self.goal_pos[1]][self.goal_pos[0]] = "G"
        if self.agent_pos:
            grid[self.agent_pos[1]][self.agent_pos[0]] = "A"
        return "\n".join("".join(row) for row in grid)


class GymEnvironmentWrapper(Environment):
    """Gymnasium wrapper for numeric observations and discrete actions.

    Observations are flattened to match get_state_dim(). Configure render_mode
    when creating the wrapper, as required by Gymnasium.
    """

    def __init__(self, env_name: str, **kwargs: Any) -> None:
        super().__init__()
        self.env: gym.Env[Any, int] = gym.make(env_name, **kwargs)
        self.env_name = env_name
        if (
            not isinstance(self.env.action_space, gym.spaces.Discrete)
            or self.env.action_space.start != 0
        ):
            self.env.close()
            raise ValueError("A zero-based Discrete action space is required")
        if self.env.observation_space.shape is None:
            self.env.close()
            raise ValueError("A numeric observation space with a shape is required")

    def reset(
        self, seed: int | None = None, options: dict[str, Any] | None = None
    ) -> tuple[np.ndarray, dict[str, Any]]:
        """Reset the Gymnasium environment."""
        state, info = self.env.reset(seed=seed, options=options)
        self.state = np.asarray(state, dtype=np.float32).reshape(-1)
        self.done = False
        return self.state, info

    def step(self, action: int) -> tuple[np.ndarray, float, bool, bool, dict[str, Any]]:
        """Step once; a terminated or truncated episode requires reset()."""
        if self.state is None or self.done:
            raise RuntimeError("Call reset() before stepping a new episode")
        state, reward, terminated, truncated, info = self.env.step(action)
        self.state = np.asarray(state, dtype=np.float32).reshape(-1)
        self.done = terminated or truncated
        return self.state, float(reward), terminated, truncated, info

    def get_state_dim(self) -> int:
        """Get the dimensionality of the state space."""
        shape = self.env.observation_space.shape
        if shape is None:
            raise ValueError("A numeric observation space with a shape is required")
        return int(np.prod(shape))

    def get_action_dim(self) -> int:
        """Get the dimensionality of the action space."""
        if not isinstance(self.env.action_space, gym.spaces.Discrete):
            raise ValueError("A zero-based Discrete action space is required")
        return int(self.env.action_space.n)

    def render(self) -> object:
        """Render using the mode configured when creating the environment."""
        return self.env.render()

    def close(self) -> None:
        """Close the gym environment."""
        self.env.close()
