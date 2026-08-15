from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import (
    mean_squared_error,
    mean_absolute_error,
    r2_score
)
import matplotlib.pyplot as plt
import numpy as np

"""
Code 
`"""
# Load dataset
data = fetch_california_housing()


X = data.data
y = data.target

print(X.shape)
# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Scale features
scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Create model
model = KNeighborsRegressor(n_neighbors=1)

# Train model
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Evaluate
print("MAE :", mean_absolute_error(y_test, y_pred))
print("MSE :", mean_squared_error(y_test, y_pred))
print("RMSE:", mean_squared_error(y_test, y_pred) ** 0.5)
print("R²  :", r2_score(y_test, y_pred))



"""
Visualization
"""

np.random.seed(42)

X_scaled = scaler.transform(X)
y_all_pred = model.predict(X_scaled)

indices = np.random.choice(
    len(y),
    size=200,
    replace=False
)

indices = np.sort(indices)

plt.figure(figsize=(12,5))

plt.plot(
    y[indices],
    linewidth=2,
    label="Actual"
)

plt.plot(
    y_all_pred[indices],
    linewidth=2,
    label="Predicted"
)

plt.xlabel("Selected Samples")
plt.ylabel("Median House Value")
plt.title("KNN Regression Predictions")
plt.legend()
plt.grid(True)

plt.show()