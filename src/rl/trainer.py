import numpy as np
from typing import List, Dict, Any, Optional
from .agent import RLAgent
from .environment import Environment


class Trainer:
    """Training loop for RL agents."""

    def __init__(self, agent: RLAgent, environment: Environment):
        self.agent = agent
        self.environment = environment
        self.training_history = []

    def train(self, num_episodes: int, max_steps_per_episode: int = 1000,
              log_interval: int = 100) -> Dict[str, List[float]]:
        """Train the agent for a specified number of episodes."""
        episode_rewards = []
        episode_lengths = []

        for episode in range(num_episodes):
            state = self.environment.reset()
            episode_reward = 0
            episode_length = 0

            for step in range(max_steps_per_episode):
                action = self.agent.select_action(state)
                next_state, reward, done, info = self.environment.step(action)

                self.agent.update(state, action, reward, next_state, done)

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
                print(f"Episode {episode + 1}/{num_episodes}, "
                      f"Avg Reward: {avg_reward:.2f}, "
                      f"Avg Length: {avg_length:.2f}")

        history = {
            "episode_rewards": episode_rewards,
            "episode_lengths": episode_lengths
        }
        self.training_history.append(history)

        return history

    def evaluate(self, num_episodes: int = 10, render: bool = False) -> Dict[str, float]:
        """Evaluate the trained agent."""
        episode_rewards = []
        episode_lengths = []

        for episode in range(num_episodes):
            state = self.environment.reset()
            episode_reward = 0
            episode_length = 0

            if render and hasattr(self.environment, 'render'):
                print(f"Episode {episode + 1} - Initial state:")
                print(self.environment.render())

            while True:
                action = self.agent.select_action(state)
                next_state, reward, done, info = self.environment.step(action)

                if render and hasattr(self.environment, 'render'):
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
                print(f"Episode {episode + 1} completed - "
                      f"Reward: {episode_reward}, Length: {episode_length}\n")

        return {
            "mean_reward": np.mean(episode_rewards),
            "std_reward": np.std(episode_rewards),
            "mean_length": np.mean(episode_lengths),
            "std_length": np.std(episode_lengths),
            "episode_rewards": episode_rewards,
            "episode_lengths": episode_lengths
        }