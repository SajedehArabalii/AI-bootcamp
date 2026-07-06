import numpy as np

X_messages = np.array([
    [12, 0, 1],
    [45, 5, 8],
    [8,  0, 0],
    [30, 3, 4]
])

w = np.array([0.1, 0.8, 0.5])
b = -2.0

"""
Calculate the raw output
"""
raw_output = np.dot(X_messages, w) + b
print("1. Raw Output (z):\n",raw_output)

"""
Apply activation function (No negative outputs)
"""
activated_output = np.maximum(0,raw_output)
print("\n2. Activated output:\n",activated_output)

"""
Define threshold and classify
"""
threshold = 0.0
predictions = []

for i, score in enumerate(activated_output):
    if score > threshold:
        label = "High energy"
    else:
        label = "calm"
    predictions.append(label)
    print(f"Message {i+1} (Score: {score:4.1f}) -> Classification: {label}")
