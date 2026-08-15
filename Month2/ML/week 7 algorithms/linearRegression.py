# Perfect prediction
"""
Linear Regression and Evaluation code
"""
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import (
    mean_squared_error,
    mean_absolute_error,
    r2_score
)

# Load dataset
data = fetch_california_housing()

X = data.data
y = data.target

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Create the model
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
print("MAE :", mean_absolute_error(y_test, y_pred))
print("MSE :", mean_squared_error(y_test, y_pred))
print("RMSE:", mean_squared_error(y_test, y_pred) ** 0.5)
print("R²  :", r2_score(y_test, y_pred))


"""
Visualizaiton code
"""

import matplotlib.pyplot as plt
import numpy as np

# Visualize predictions vs. actual values
plt.figure(figsize=(7, 7))

plt.scatter(
    y_test,
    y_pred,
    alpha=0.5
)

# Perfect prediction line
min_value = min(y_test.min(), y_pred.min())
max_value = max(y_test.max(), y_pred.max())

plt.plot(
    [min_value, max_value],
    [min_value, max_value],
    "r--",
    linewidth=2,
    label="Perfect Prediction"
)

plt.xlabel("Actual House Value")
plt.ylabel("Predicted House Value")
plt.title("Linear Regression: Predicted vs Actual")
plt.legend()
plt.grid(True)

plt.show()







# Learned regression line
from sklearn.datasets import fetch_california_housing
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import numpy as np

# Load dataset
data = fetch_california_housing()

# Use only one feature: Median Income
X = data.data[:, [0]]      # MedInc
y = data.target

# Train model
model = LinearRegression()
model.fit(X, y)

# Predict
y_pred = model.predict(X)

# Sort points for plotting
idx = np.argsort(X[:, 0])

plt.figure(figsize=(8, 6))

plt.scatter(
    X,
    y,
    s=8,
    alpha=0.3,
    label="Data"
)

plt.plot(
    X[idx],
    y_pred[idx],
    color="red",
    linewidth=3,
    label="Learned Regression Line"
)

plt.xlabel("Median Income")
plt.ylabel("Median House Value")
plt.title("Linear Regression")
plt.legend()
plt.grid(True)

plt.show()