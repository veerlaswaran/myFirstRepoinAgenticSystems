# visualization.py

import numpy as np
import matplotlib.pyplot as plt

# 1. Create a list of 10 epochs (from 1 to 10)
epochs = list(range(1, 11))

# 2. Generate synthetic training loss values using NumPy
# Loss values decrease gradually with some noise
np.random.seed(42)  # for reproducibility
loss_values = np.linspace(1.0, 0.2, 10) + np.random.normal(0, 0.05, 10)

# 3. Line Plot: Loss vs Epoch
plt.figure(figsize=(8, 5))
plt.plot(epochs, loss_values, marker='o', linestyle='-', color='b', label='Training Loss')
plt.title("Training Loss vs Epoch")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.grid(True)
plt.legend()
plt.show()

# 4. Scatter Plot: Epoch vs Loss
plt.figure(figsize=(8, 5))
plt.scatter(epochs, loss_values, color='r', marker='x')
plt.title("Epoch vs Training Loss")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.grid(True)
plt.show()

# 5. Bar Chart: Accuracy comparison of three models
models = ["Model A", "Model B", "Model C"]
accuracy = [0.85, 0.90, 0.88]

plt.figure(figsize=(8, 5))
plt.bar(models, accuracy, color=['green', 'blue', 'orange'])
plt.title("Model Accuracy Comparison")
plt.xlabel("Models")
plt.ylabel("Accuracy")
plt.ylim(0, 1)  # accuracy ranges between 0 and 1
plt.show()
