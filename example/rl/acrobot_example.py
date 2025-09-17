#!/usr/bin/env python3
"""
Acrobot RL Example using Q-Learning

This example demonstrates how to use the RL framework with the classic
Acrobot environment from OpenAI Gym.
"""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from rl import QLearningAgent, GymEnvironmentWrapper, Trainer


def main():
    print("🤸 Acrobot Q-Learning Example")
    print("=" * 50)

    # Create Acrobot environment
    env = GymEnvironmentWrapper('Acrobot-v1')

    print(f"Environment: {env.env_name}")
    print(f"State dimension: {env.get_state_dim()}")
    print(f"Action dimension: {env.get_action_dim()}")

    # Create Q-learning agent
    agent = QLearningAgent(
        state_dim=env.get_state_dim(),
        action_dim=env.get_action_dim(),
        learning_rate=0.1,
        discount_factor=0.99,
        epsilon=1.0,
        epsilon_decay=0.9995
    )

    trainer = Trainer(agent, env)

    print("\n📚 Training the Q-Learning agent on Acrobot...")
    print("Note: Acrobot is a challenging environment with continuous state space")

    training_history = trainer.train(
        num_episodes=3000,
        max_steps_per_episode=500,
        log_interval=500
    )

    print("\n🎯 Evaluating the trained agent...")
    evaluation_results = trainer.evaluate(num_episodes=5, render=False)

    print("\n📊 Final Results:")
    print(f"Mean Episode Reward: {evaluation_results['mean_reward']:.2f} ± {evaluation_results['std_reward']:.2f}")
    print(f"Mean Episode Length: {evaluation_results['mean_length']:.2f} ± {evaluation_results['std_length']:.2f}")

    # Acrobot is solved when episode length is <= 500 (meaning it reached the goal)
    success_episodes = sum(1 for l in evaluation_results['episode_lengths'] if l < 500)
    print(f"Successful episodes (reached goal): {success_episodes}/{len(evaluation_results['episode_lengths'])}")

    print("\n🎮 Sample episode rewards:", evaluation_results['episode_rewards'])

    # Close the environment
    env.close()

    print("\n✅ Acrobot example completed successfully!")


if __name__ == "__main__":
    main()