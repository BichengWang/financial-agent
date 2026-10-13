import numpy as np
from typing import TypedDict
from .agent import RLAgent
from .environment import Environment


class TrainingHistory(TypedDict):
    episode_rewards: list[float]
    episode_lengths: list[int]


class EvaluationResults(TrainingHistory):
    mean_reward: float
    std_reward: float
    mean_length: float
    std_length: float


class Trainer:
    """Training loop for RL agents."""

    def __init__(self, agent: RLAgent, environment: Environment) -> None:
        self.agent = agent
        self.environment = environment
        self.training_history: list[TrainingHistory] = []

    def train(
        self,
        num_episodes: int,
        max_steps_per_episode: int = 1000,
        log_interval: int = 100,
    ) -> TrainingHistory:
        """Train the agent for a specified number of episodes."""
        if num_episodes <= 0:
            raise ValueError("num_episodes must be positive")
        if max_steps_per_episode <= 0:
            raise ValueError("max_steps_per_episode must be positive")
        if log_interval <= 0:
            raise ValueError("log_interval must be positive")
        episode_rewards: list[float] = []
        episode_lengths: list[int] = []

        for episode in range(num_episodes):
            state, info = self.environment.reset()
            episode_reward = 0.0
            episode_length = 0

            for step in range(max_steps_per_episode):
                action = self.agent.select_action(state)
                next_state, reward, terminated, truncated, info = self.environment.step(
                    action
                )
                done = terminated or truncated

                # Time limits end the rollout but still allow bootstrapping.
                self.agent.update(state, action, reward, next_state, terminated)

                state = next_state
                episode_reward += reward
                episode_length += 1

                if done:
                    break

            episode_rewards.append(episode_reward)
            episode_lengths.append(episode_length)

            if (episode + 1) % log_interval == 0:
                avg_reward = np.mean(episode_rewards[-log_interval:])
                avg_length = np.mean(episode_lengths[-log_interval:])
                print(
                    f"Episode {episode + 1}/{num_episodes}, "
                    f"Avg Reward: {avg_reward:.2f}, "
                    f"Avg Length: {avg_length:.2f}"
                )

        history: TrainingHistory = {
            "episode_rewards": episode_rewards,
            "episode_lengths": episode_lengths,
        }
        self.training_history.append(history)

        return history

    def evaluate(
        self,
        num_episodes: int = 10,
        render: bool = False,
        max_steps_per_episode: int = 1000,
    ) -> EvaluationResults:
        """Evaluate without updates, stopping each episode at the step limit."""
        if num_episodes <= 0:
            raise ValueError("num_episodes must be positive")
        if max_steps_per_episode <= 0:
            raise ValueError("max_steps_per_episode must be positive")
        episode_rewards: list[float] = []
        episode_lengths: list[int] = []

        for episode in range(num_episodes):
            state, info = self.environment.reset()
            episode_reward = 0.0
            episode_length = 0

            if render and hasattr(self.environment, "render"):
                print(f"Episode {episode + 1} - Initial state:")
                print(self.environment.render())

            for step in range(max_steps_per_episode):
                action = self.agent.select_action(state)
                next_state, reward, terminated, truncated, info = self.environment.step(
                    action
                )
                done = terminated or truncated

                if render and hasattr(self.environment, "render"):
                    print(f"Action: {action}, Reward: {reward}")
                    print(self.environment.render())

                state = next_state
                episode_reward += reward
                episode_length += 1

                if done:
                    break

            episode_rewards.append(episode_reward)
            episode_lengths.append(episode_length)

            if render:
                print(
                    f"Episode {episode + 1} completed - "
                    f"Reward: {episode_reward}, Length: {episode_length}\n"
                )

        return {
            "mean_reward": float(np.mean(episode_rewards)),
            "std_reward": float(np.std(episode_rewards)),
            "mean_length": float(np.mean(episode_lengths)),
            "std_length": float(np.std(episode_lengths)),
            "episode_rewards": episode_rewards,
            "episode_lengths": episode_lengths,
        }
