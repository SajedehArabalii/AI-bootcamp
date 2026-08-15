from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Metrics
from sklearn.metrics import (
    precision_score,
    recall_score,
)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = load_breast_cancer()

X_train, X_test, y_train, y_test = train_test_split(
    data.data,
    data.target,
    test_size=0.30,
    random_state=42,
    stratify=data.target,
)

# Train Logistic Regression
model = LogisticRegression(max_iter=10000)

model.fit(X_train, y_train)

# Predicted probabilities
y_prob = model.predict_proba(X_test)[:, 1]

thresholds = np.arange(0.1, 1.0, 0.1)

results = []

for t in thresholds:
    y_pred = (y_prob >= t).astype(int)

    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)

    results.append([t, precision, recall])

results = pd.DataFrame(
    results,
    columns=["Threshold", "Precision", "Recall"],
)

print(results)

# import matplotlib.pyplot as plt

# plt.figure(figsize=(8,5))

# plt.plot(
#     results["Threshold"],
#     results["Precision"],
#     marker="o",
#     linewidth=2,
#     label="Precision",
# )

# plt.plot(
#     results["Threshold"],
#     results["Recall"],
#     marker="s",
#     linewidth=2,
#     label="Recall",
# )

# plt.xlabel("Classification Threshold")
# plt.ylabel("Score")
# plt.title("Precision and Recall vs Classification Threshold")
# plt.grid(alpha=0.3)
# plt.legend()

# plt.show()


fig, ax = plt.subplots(figsize=(9,5))

ax.plot(
    results["Threshold"],
    results["Precision"],
    marker="o",
    linewidth=2,
    label="Precision",
)

ax.plot(
    results["Threshold"],
    results["Recall"],
    marker="s",
    linewidth=2,
    label="Recall",
)

# Cancer region
ax.annotate(
    "Cancer Detection\nPrefer High Recall",
    xy=(0.2, results.loc[1, "Recall"]),
    xytext=(0.05, 0.82),
    arrowprops=dict(arrowstyle="->"),
    fontsize=11,
)

# Spam region
ax.annotate(
    "Spam Detection\nPrefer High Precision",
    xy=(0.8, results.loc[7, "Precision"]),
    xytext=(0.62, 0.80),
    arrowprops=dict(arrowstyle="->"),
    fontsize=11,
)

ax.set_xlabel("Classification Threshold")
ax.set_ylabel("Metric Value")
ax.set_title("Business Goals Determine the Best Threshold")
ax.grid(alpha=0.3)
ax.legend()

plt.show()