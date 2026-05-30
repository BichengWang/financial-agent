#!/usr/bin/env python3
"""
Basic Reinforcement Learning Example using Q-Learning on GridWorld

This example demonstrates how to use the RL framework to train a Q-learning
agent on a simple grid world environment.
"""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from financial_agent.rl import QLearningAgent, SimpleGridWorld, Trainer


def main():
    print("🤖 Basic Reinforcement Learning Example")
    print("=" * 50)

    env = SimpleGridWorld(grid_size=5, goal_reward=10.0, step_penalty=-0.1)

    agent = QLearningAgent(
        state_dim=env.get_state_dim(),
        action_dim=env.get_action_dim(),
        learning_rate=0.1,
        discount_factor=0.95,
        epsilon=0.9,
        epsilon_decay=0.995
    )

    trainer = Trainer(agent, env)

    print("\n📚 Training the Q-Learning agent...")
    training_history = trainer.train(
        num_episodes=500,
        max_steps_per_episode=100,
        log_interval=100
    )

    print("\n🎯 Evaluating the trained agent...")
    evaluation_results = trainer.evaluate(num_episodes=5, render=True)

    print("\n📊 Final Results:")
    print(f"Mean Episode Reward: {evaluation_results['mean_reward']:.2f} ± {evaluation_results['std_reward']:.2f}")
    print(f"Mean Episode Length: {evaluation_results['mean_length']:.2f} ± {evaluation_results['std_length']:.2f}")

    print("\n✅ Example completed successfully!")


if __name__ == "__main__":
    main()