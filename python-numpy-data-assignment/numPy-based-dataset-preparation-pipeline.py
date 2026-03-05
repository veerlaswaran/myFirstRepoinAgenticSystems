import numpy as np
np.random.seed(42)

data = np.random.randn(100, 3)

mean = data.mean(axis=0)
std = data.std(axis=0)

normalized = (data - mean) / std

split_index = int(0.8 * normalized.shape[0])
training_data = normalized[:split_index]
test_data = normalized[split_index:]

print("Before modification:")
print("First training sample:", training_data[0])

training_data[0, 0] = 999

print("\nAfter modification:")
print("First training sample:", training_data[0])
print("Corresponding value in normalized array:", normalized[0, 0])

print("\n--- Summary ---")
print("Original data shape:", data.shape)
print("Mean shape:", mean.shape)
print("Training data shape:", training_data.shape)
print("Test data shape:", test_data.shape)
print("Note: Modifying the slice affected the original array")
