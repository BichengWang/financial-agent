#!/usr/bin/env python3
"""
Run all RL examples to demonstrate the framework capabilities

This script runs all available examples in sequence.
"""

import sys
import os
import subprocess
import time

def run_example(script_name, description):
    """Run a single example script."""
    print(f"\n{'='*60}")
    print(f"🚀 Running: {description}")
    print(f"{'='*60}")

    script_path = os.path.join(os.path.dirname(__file__), script_name)

    try:
        start_time = time.time()
        result = subprocess.run([sys.executable, script_path],
                              capture_output=True, text=True, timeout=300)
        end_time = time.time()

        if result.returncode == 0:
            print(result.stdout)
            print(f"✅ {description} completed in {end_time - start_time:.2f} seconds")
        else:
            print(f"❌ {description} failed with return code {result.returncode}")
            print("STDOUT:", result.stdout)
            print("STDERR:", result.stderr)

    except subprocess.TimeoutExpired:
        print(f"⏰ {description} timed out after 5 minutes")
    except Exception as e:
        print(f"💥 Error running {description}: {e}")


def main():
    print("🎯 Running All RL Framework Examples")
    print("=" * 60)

    examples = [
        ("basic_rl_example.py", "Basic GridWorld Q-Learning"),
        ("cartpole_example.py", "CartPole Q-Learning"),
        ("mountain_car_example.py", "MountainCar Q-Learning"),
        ("acrobot_example.py", "Acrobot Q-Learning"),
    ]

    successful = 0
    total = len(examples)

    for script, description in examples:
        try:
            run_example(script, description)
            successful += 1
        except KeyboardInterrupt:
            print("\n🛑 Interrupted by user")
            break
        except Exception as e:
            print(f"💥 Unexpected error: {e}")

    print(f"\n{'='*60}")
    print(f"📊 Summary: {successful}/{total} examples completed successfully")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()