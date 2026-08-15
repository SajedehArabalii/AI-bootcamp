# Linear Regression with K-Fold Cross Validation

import numpy as np

from sklearn.datasets import load_diabetes
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import KFold, cross_val_score
from sklearn.metrics import mean_squared_error


# ==========================================
# 1. Load Dataset
# ==========================================

X, y = load_diabetes(
    return_X_y=True
)


print("Features shape:", X.shape)
print("Target shape:", y.shape)


# ==========================================
# 2. Define Model
# ==========================================

model = LinearRegression()


# ==========================================
# 3. Define K-Fold Cross Validation
# ==========================================

kfold = KFold(
    n_splits=5,
    shuffle=True,
    random_state=42
)


# ==========================================
# 4. Evaluate Model Using Cross Validation
# ==========================================

# R² scores for each fold

r2_scores = cross_val_score(
    model,
    X,
    y,
    cv=kfold,
    scoring="r2"
)


print("\nR² scores for each fold:")

for i, score in enumerate(r2_scores):
    print(
        f"Fold {i+1}: {score:.3f}"
    )


print(
    "\nAverage R²:",
    r2_scores.mean()
)


# ==========================================
# 5. Evaluate RMSE
# ==========================================

rmse_scores = np.sqrt(
    -cross_val_score(
        model,
        X,
        y,
        cv=kfold,
        scoring="neg_mean_squared_error"
    )
)


print("\nRMSE scores for each fold:")

for i, score in enumerate(rmse_scores):
    print(
        f"Fold {i+1}: {score:.2f}"
    )


print(
    "\nAverage RMSE:",
    rmse_scores.mean()
)