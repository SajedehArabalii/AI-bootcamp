"""
Code
"""
# Logistic Regression Review — Example

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Load dataset
data = load_breast_cancer()

X = data.data
y = data.target

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# Create the model
model = LogisticRegression(max_iter=5000)

# Train the model
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
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

# Predicted probability of the positive class
y_prob = model.predict_proba(X_test)[:, 1]

# Sort by predicted probability
idx = np.argsort(y_prob)

plt.figure(figsize=(12, 5))

plt.plot(
    y_test[idx],
    "o",
    label="Actual Class",
    markersize=4
)

plt.plot(
    y_prob[idx],
    linewidth=2,
    label="Predicted Probability"
)

plt.axhline(
    y=0.5,
    color="red",
    linestyle="--",
    label="Decision Threshold"
)

plt.xlabel("Test Samples (sorted by predicted probability)")
plt.ylabel("Probability of Malignant")
plt.title("Logistic Regression Predictions")

plt.legend()
plt.grid(True)

plt.show()