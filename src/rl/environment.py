import numpy as np
from abc import ABC, abstractmethod
from typing import Tuple, Dict, Any, Optional
import gymnasium as gym


class Environment(ABC):
    """Base class for RL environments."""

    def __init__(self):
        self.state = None
        self.done = False

    @abstractmethod
    def reset(self) -> np.ndarray:
        """Reset environment to initial state."""
        pass

    @abstractmethod
    def step(self, action: int) -> Tuple[np.ndarray, float, bool, Dict[str, Any]]:
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

    def __init__(self, grid_size: int = 5, goal_reward: float = 10.0,
                 step_penalty: float = -0.1):
        super().__init__()
        self.grid_size = grid_size
        self.goal_reward = goal_reward
        self.step_penalty = step_penalty
        self.goal_pos = (grid_size - 1, grid_size - 1)
        self.agent_pos = None

    def reset(self) -> np.ndarray:
        """Reset agent to starting position."""
        self.agent_pos = (0, 0)
        self.done = False
        return np.array(self.agent_pos, dtype=np.float32)

    def step(self, action: int) -> Tuple[np.ndarray, float, bool, Dict[str, Any]]:
        """
        Take a step in the grid world.
        Actions: 0=up, 1=right, 2=down, 3=left
        """
        if self.done:
            return np.array(self.agent_pos, dtype=np.float32), 0, True, {}

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
            "distance_to_goal": abs(self.agent_pos[0] - self.goal_pos[0]) +
                              abs(self.agent_pos[1] - self.goal_pos[1])
        }

        return np.array(self.agent_pos, dtype=np.float32), reward, self.done, info

    def get_state_dim(self) -> int:
        return 2

    def get_action_dim(self) -> int:
        return 4

    def render(self) -> str:
        """Render the current state of the grid world."""
        grid = [['.' for _ in range(self.grid_size)] for _ in range(self.grid_size)]
        grid[self.goal_pos[1]][self.goal_pos[0]] = 'G'
        if self.agent_pos:
            grid[self.agent_pos[1]][self.agent_pos[0]] = 'A'
        return '\n'.join(''.join(row) for row in grid)


class GymEnvironmentWrapper(Environment):
    """Wrapper for OpenAI Gym environments to work with our RL framework."""

    def __init__(self, env_name: str, **kwargs):
        super().__init__()
        self.env = gym.make(env_name, **kwargs)
        self.env_name = env_name

    def reset(self) -> np.ndarray:
        """Reset the gym environment."""
        if hasattr(self.env, 'reset'):
            # Handle both old and new gym API
            result = self.env.reset()
            if isinstance(result, tuple):
                state, _ = result
            else:
                state = result
        else:
            state = self.env.reset()

        self.done = False
        return np.array(state, dtype=np.float32)

    def step(self, action: int) -> Tuple[np.ndarray, float, bool, Dict[str, Any]]:
        """Take a step in the gym environment."""
        if self.done:
            return np.array(self.env.observation_space.sample(), dtype=np.float32), 0, True, {}

        # Handle both old and new gym API
        result = self.env.step(action)
        if len(result) == 4:
            state, reward, done, info = result
        else:  # New gym API returns 5 values
            state, reward, terminated, truncated, info = result
            done = terminated or truncated

        self.done = done
        return np.array(state, dtype=np.float32), float(reward), done, info

    def get_state_dim(self) -> int:
        """Get the dimensionality of the state space."""
        if hasattr(self.env.observation_space, 'shape'):
            if len(self.env.observation_space.shape) == 0:
                return 1
            return int(np.prod(self.env.observation_space.shape))
        else:
            return self.env.observation_space.n

    def get_action_dim(self) -> int:
        """Get the dimensionality of the action space."""
        if hasattr(self.env.action_space, 'n'):
            return self.env.action_space.n
        else:
            return int(np.prod(self.env.action_space.shape))

    def render(self, mode: str = 'human') -> Optional[str]:
        """Render the gym environment."""
        return self.env.render(mode=mode)

    def close(self):
        """Close the gym environment."""
        self.env.close()