import numpy as np

size = 12350
# np.random.seed(42)
X = np.random.rand(size, 5)
Y = np.random.rand(size,1)

# i = np.random.permutation(size)

# shuff_X = X[i]
# shuff_Y = Y[i]

train_size = int(size * 0.80)
validation_size = int(size * 0.10)
test_size = size - train_size - validation_size

print(f"Training samples: {train_size}")
print(f"Validation samples: {validation_size}")
print(f"Test samples: {test_size}")
print(f"Total: {size}")

import numpy as np
ground_truth = np.array([
 "Normal",
 "Urgent",
 "Normal",
 "Spam",
 "Urgent",
 "Normal",
 "Spam",
 "Normal"
])
predictions = np.array([
 "Normal",
 "Normal",
 "Normal",
 "Spam",
 "Urgent",
 "Spam",
 "Spam",
 "Normal"
])
print(ground_truth)
print(predictions)

correct_mask = ground_truth == predictions
print(correct_mask)
correct_predictions = np.sum(correct_mask)
print(correct_predictions)
incorrect_prediction = len(correct_mask) - correct_predictions
print(incorrect_prediction)