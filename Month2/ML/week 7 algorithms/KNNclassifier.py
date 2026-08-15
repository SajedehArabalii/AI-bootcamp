"""
Code
"""
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report
)

# Load dataset
data = load_breast_cancer()

X = data.data
y = data.target

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# Scale features
scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Create model
model = KNeighborsClassifier(n_neighbors=5)

# Train model
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Evaluate
print("Accuracy:", accuracy_score(y_test, y_pred))

print("\nConfusion Matrix")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report")
print(classification_report(y_test, y_pred))

"""
Visualization
"""
import matplotlib.pyplot as plt
import numpy as np

# Probability of the positive class
y_prob = model.predict_proba(X_test)[:, 1]
# y_prob = model.predict(X_test)[:, 1]

# Sort by predicted probability
idx = np.argsort(y_prob)

plt.figure(figsize=(12, 5))

# Actual classes
plt.scatter(
    range(len(idx)),
    y_test[idx],
    s=20,
    color="black",
    alpha=0.7,
    label="Actual Class"
)

# Predicted probabilities
plt.plot(
    y_prob[idx],
    linewidth=2,
    color="tab:blue",
    label="Predicted Probability"
)

# Decision threshold
plt.axhline(
    0.5,
    color="red",
    linestyle="--",
    label="Decision Threshold"
)

plt.xlabel("Test Samples (sorted by predicted probability)")
plt.ylabel("Probability of Positive Class")
plt.title("K-Nearest Neighbors Classification")

plt.grid(True)
plt.legend()

plt.show()