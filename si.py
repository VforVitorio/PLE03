import tensorflow as tf
import torch  # Alternative GPU check

# TensorFlow GPU check
print("TensorFlow GPUs: ", len(tf.config.list_physical_devices('GPU')))

# PyTorch GPU check
print("CUDA Available: ", torch.cuda.is_available())
print("CUDA Device Name: ", torch.cuda.get_device_name(
    0) if torch.cuda.is_available() else "No CUDA GPU")
