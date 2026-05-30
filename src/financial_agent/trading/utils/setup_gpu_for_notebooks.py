"""
GPU Setup Script for Jupyter Notebooks
======================================

This script sets up GPU configuration for all Jupyter notebooks in the core_trading directory.
Run this script at the beginning of any notebook to ensure proper GPU configuration.

Usage in Jupyter Notebook:
    %run setup_gpu_for_notebooks.py
    
Or import and use:
    from setup_gpu_for_notebooks import setup_gpu_for_notebook
    setup_gpu_for_notebook()
"""

import os
import sys
import warnings

# Add the current directory to Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.append(current_dir)

# Import GPU configuration
from gpu_config import setup_gpu, print_device_info, DEVICE, get_device_string

def setup_gpu_for_notebook():
    """
    Setup GPU configuration for Jupyter notebooks.
    This function should be called at the beginning of any notebook.
    """
    print("=" * 60)
    print("🚀 SETTING UP GPU FOR FINANCIAL AGENT NOTEBOOKS")
    print("=" * 60)
    
    # Setup GPU configuration
    device = setup_gpu()
    
    # Print device information
    print_device_info()
    
    # Import TensorFlow and other ML libraries
    try:
        import tensorflow as tf
        print(f"✅ TensorFlow {tf.__version__} loaded successfully")
        
        # Test GPU availability
        if device == '/GPU:0':
            print("✅ GPU acceleration is ENABLED")
            print("✅ All TensorFlow operations will use GPU")
        else:
            print("⚠️  GPU not available, using CPU")
            
    except ImportError as e:
        print(f"❌ Error importing TensorFlow: {e}")
        return False
    
    # Import other required libraries
    try:
        import numpy as np
        import pandas as pd
        print(f"✅ NumPy {np.__version__} loaded successfully")
        print(f"✅ Pandas {pd.__version__} loaded successfully")
    except ImportError as e:
        print(f"❌ Error importing required libraries: {e}")
        return False
    
    print("=" * 60)
    print("✅ GPU SETUP COMPLETE - READY FOR TRAINING!")
    print("=" * 60)
    
    return True

def get_notebook_device():
    """
    Get the current device for use in notebook cells.
    
    Returns:
        str: Device string ('/GPU:0' or '/CPU:0')
    """
    return get_device_string()

def print_training_info():
    """
    Print information about GPU-accelerated training.
    """
    print("\n" + "=" * 60)
    print("📊 GPU-ACCELERATED TRAINING INFORMATION")
    print("=" * 60)
    
    device = get_device_string()
    
    if device == '/GPU:0':
        print("🚀 GPU ACCELERATION ENABLED")
        print("   • All TensorFlow operations will use GPU")
        print("   • Training will be significantly faster")
        print("   • Memory growth is enabled for optimal performance")
        print("   • XLA compilation is disabled to prevent errors")
    else:
        print("💻 CPU TRAINING MODE")
        print("   • All operations will use CPU")
        print("   • Training will be slower but more stable")
        print("   • No GPU memory management needed")
    
    print("\n📝 USAGE IN YOUR NOTEBOOK:")
    print("   • Use DEVICE variable for all tf.device() calls")
    print("   • Models will automatically be created on the correct device")
    print("   • Training functions handle device placement automatically")
    
    print("=" * 60)

if __name__ == "__main__":
    # Run setup when script is executed directly
    setup_gpu_for_notebook()
    print_training_info()
else:
    # Auto-setup when imported
    setup_gpu_for_notebook()











