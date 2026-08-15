from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.linear_model import LinearRegression

np.random.seed(42)


X = np.linspace(
    -3,
    3,
    100
).reshape(-1,1)


# Nonlinear relationship
y = X[:,0]**3 + np.random.randn(100)*5


X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = LinearRegression()

model.fit(
    X_train,
    y_train
)


train_r2 = model.score(
    X_train,
    y_train
)

test_r2 = model.score(
    X_test,
    y_test
)


print("Training R²:", train_r2)
print("Testing R² :", test_r2)