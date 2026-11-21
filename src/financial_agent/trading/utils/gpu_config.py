"""
GPU Configuration Module for Financial Agent
============================================

This module provides centralized GPU configuration for all TensorFlow operations
in the financial agent project. It handles device detection, memory management,
and provides utility functions for GPU-accelerated training.

Usage:
    from gpu_config import setup_gpu, get_device_string, pick_device, DEVICE
    
    # Setup GPU at the beginning of your script
    setup_gpu()
    
    # Or pick a device manually
    device = pick_device(prefer_gpu=True)  # Returns '/device:GPU:0' or '/CPU:0'
    
    # Use DEVICE for all TensorFlow operations
    with tf.device(DEVICE):
        model = build_model()
"""

import os
import tensorflow as tf

# Global device variable
DEVICE = None

def pick_device(prefer_gpu=True) -> str:
    """
    Pick the optimal device for TensorFlow operations.
    
    Args:
        prefer_gpu (bool): Whether to prefer GPU over CPU if available
        
    Returns:
        str: Device name (e.g., '/device:GPU:0' or '/CPU:0')
    """
    if prefer_gpu:
        gpus = tf.config.list_logical_devices('GPU')
        if gpus:
            return gpus[0].name  # e.g., '/device:GPU:0'
    return '/CPU:0'

def setup_gpu():
    """
    Configure GPU settings for optimal performance across all notebooks and scripts.
    
    This function:
    1. Disables XLA compilation to avoid platform detection issues
    2. Sets up memory growth for GPU devices
    3. Configures TensorFlow for better compatibility
    4. Sets the global DEVICE variable
    
    Returns:
        str: The device string to use for TensorFlow operations
    """
    global DEVICE
    
    # Disable XLA compilation to avoid platform detection issues
    os.environ['TF_XLA_FLAGS'] = '--tf_xla_enable_xla_devices=false'
    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
    
    # Configure TensorFlow for better compatibility
    tf.config.run_functions_eagerly(False)
    tf.config.optimizer.set_jit(False)  # Disable XLA JIT compilation
    
    # Set memory growth for GPU if available
    gpus = tf.config.experimental.list_physical_devices('GPU')
    if gpus:
        try:
            for gpu in gpus:
                tf.config.experimental.set_memory_growth(gpu, True)
            print(f"✓ GPU available: {len(gpus)} device(s)")
            print("✓ Memory growth enabled for all GPU devices")
        except RuntimeError as e:
            print(f"GPU memory growth setting failed: {e}")
    else:
        print("✓ No GPU detected, using CPU")
    
    # Pick the optimal device using actual TensorFlow device names
    DEVICE = pick_device(prefer_gpu=True)
    print(f"✓ TensorFlow configured for device: {DEVICE}")
    return DEVICE

def get_device_string():
    """
    Get the current device string for TensorFlow operations.
    
    Returns:
        str: Device string (e.g., '/device:GPU:0' or '/CPU:0')
    """
    if DEVICE is None:
        return setup_gpu()
    return DEVICE

def get_device_info():
    """
    Get detailed information about available devices.
    
    Returns:
        dict: Device information including GPU details
    """
    info = {
        'tensorflow_version': tf.__version__,
        'gpu_available': len(tf.config.experimental.list_physical_devices('GPU')) > 0,
        'gpu_count': len(tf.config.experimental.list_physical_devices('GPU')),
        'current_device': get_device_string(),
        'gpu_devices': tf.config.experimental.list_physical_devices('GPU'),
        'cpu_devices': tf.config.experimental.list_physical_devices('CPU')
    }
    return info

def print_device_info():
    """Print comprehensive device information."""
    info = get_device_info()
    print("=" * 50)
    print("GPU CONFIGURATION INFO")
    print("=" * 50)
    print(f"TensorFlow Version: {info['tensorflow_version']}")
    print(f"GPU Available: {info['gpu_available']}")
    print(f"GPU Count: {info['gpu_count']}")
    print(f"Current Device: {info['current_device']}")
    
    if info['gpu_devices']:
        print("\nGPU Devices:")
        for i, gpu in enumerate(info['gpu_devices']):
            print(f"  {i}: {gpu}")
    
    print(f"\nCPU Devices: {len(info['cpu_devices'])}")
    print("=" * 50)

# Initialize GPU configuration when module is imported
if __name__ == "__main__":
    setup_gpu()
    print_device_info()
else:
    # Auto-setup when imported
    setup_gpu()
