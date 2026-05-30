#!/usr/bin/env python3
"""
MountainCar RL Example using Q-Learning

This example demonstrates how to use the RL framework with the classic
MountainCar environment from OpenAI Gym.
"""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from financial_agent.rl import QLearningAgent, GymEnvironmentWrapper, Trainer


def main():
    print("🏔️  MountainCar Q-Learning Example")
    print("=" * 50)

    # Create MountainCar environment
    env = GymEnvironmentWrapper('MountainCar-v0')

    print(f"Environment: {env.env_name}")
    print(f"State dimension: {env.get_state_dim()}")
    print(f"Action dimension: {env.get_action_dim()}")

    # Create Q-learning agent with parameters tuned for MountainCar
    agent = QLearningAgent(
        state_dim=env.get_state_dim(),
        action_dim=env.get_action_dim(),
        learning_rate=0.2,
        discount_factor=0.99,
        epsilon=1.0,  # Start with high exploration
        epsilon_decay=0.9995  # Slower decay for harder environment
    )

    trainer = Trainer(agent, env)

    print("\n📚 Training the Q-Learning agent on MountainCar...")
    print("Note: MountainCar is a challenging environment that may take time to solve")

    training_history = trainer.train(
        num_episodes=2000,
        max_steps_per_episode=200,
        log_interval=400
    )

    print("\n🎯 Evaluating the trained agent...")
    evaluation_results = trainer.evaluate(num_episodes=10, render=False)

    print("\n📊 Final Results:")
    print(f"Mean Episode Reward: {evaluation_results['mean_reward']:.2f} ± {evaluation_results['std_reward']:.2f}")
    print(f"Mean Episode Length: {evaluation_results['mean_length']:.2f} ± {evaluation_results['std_length']:.2f}")

    # MountainCar is solved when the car reaches the flag (reward > -200)
    success_episodes = sum(1 for r in evaluation_results['episode_rewards'] if r > -200)
    print(f"Successful episodes: {success_episodes}/{len(evaluation_results['episode_rewards'])}")

    # Test a few episodes with rendering info
    print("\n🎮 Sample episode rewards:", evaluation_results['episode_rewards'])

    # Close the environment
    env.close()

    print("\n✅ MountainCar example completed successfully!")


if __name__ == "__main__":
    main()