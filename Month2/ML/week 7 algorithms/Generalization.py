import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score


# Create data
np.random.seed(42)

X = np.random.rand(200, 1) * 10

# Real relationship:
# y = 3x + noise
y = 3 * X[:, 0] + np.random.randn(200) * 2


# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# Train model
model = LinearRegression()
model.fit(X_train, y_train)


# Evaluate
train_score = model.score(X_train, y_train)
test_score = model.score(X_test, y_test)


print("Training R²:", train_score)
print("Testing R² :", test_score)