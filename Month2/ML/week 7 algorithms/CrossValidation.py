from sklearn.model_selection import KFold, cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor


# Define regression models
models = {
    "Linear Regression": LinearRegression(),
    "Decision Tree": DecisionTreeRegressor(random_state=42),
    "Random Forest": RandomForestRegressor(random_state=42)
}


# Define K-Fold Cross Validation
cv = KFold(
    n_splits=5,
    shuffle=True,
    random_state=42
)


# Compare models
for name, model in models.items():

    scores = cross_val_score(
        model,
        X,
        y,
        cv=cv,
        scoring="r2"
    )

    print(
        f"{name}: {scores.mean():.3f}"
    )


    from sklearn.model_selection import GridSearchCV, KFold
from sklearn.tree import DecisionTreeRegressor


# Define Decision Tree model
model = DecisionTreeRegressor(
    random_state=42
)


# Define only max_depth values to test
param_grid = {
    "max_depth": [2, 3, 5, 7, 10, 15, None]
}


# Define K-Fold Cross Validation
cv = KFold(
    n_splits=5,
    shuffle=True,
    random_state=42
)


# Create GridSearchCV
grid_search = GridSearchCV(
    estimator=model,
    param_grid=param_grid,
    cv=cv,
    scoring="r2"
)


# Run hyperparameter tuning
grid_search.fit(
    X_train,
    y_train
)


# Best hyperparameter
print("Best max_depth:")
print(grid_search.best_params_)


# Best CV score
print("\nBest CV R2 Score:")
print(grid_search.best_score_)

import matplotlib.pyplot as plt


depths = [2, 3, 5, 7, 10, 15, None]

train_scores = []
cv_scores = []


for depth in depths:

    model = DecisionTreeRegressor(
        max_depth=depth,
        random_state=42
    )

    model.fit(
        X_train,
        y_train
    )

    train_scores.append(
        model.score(X_train, y_train)
    )

    cv_score = grid_search.cv_results_[
        "mean_test_score"
    ][depths.index(depth)]

    cv_scores.append(cv_score)


plt.figure(figsize=(8,5))

plt.plot(
    [str(d) for d in depths],
    train_scores,
    marker="o",
    label="Training R2"
)

plt.plot(
    [str(d) for d in depths],
    cv_scores,
    marker="o",
    label="CV R2"
)

plt.xlabel("max_depth")
plt.ylabel("R2 Score")
plt.title("Decision Tree Hyperparameter Tuning")
plt.legend()
plt.show()


import matplotlib.pyplot as plt


depths = [2, 3, 5, 7, 10, 15, None]

train_scores = []
cv_scores = []


for depth in depths:

    model = DecisionTreeRegressor(
        max_depth=depth,
        random_state=42
    )

    model.fit(
        X_train,
        y_train
    )

    train_scores.append(
        model.score(X_train, y_train)
    )

    cv_score = grid_search.cv_results_[
        "mean_test_score"
    ][depths.index(depth)]

    cv_scores.append(cv_score)


plt.figure(figsize=(8,5))

plt.plot(
    [str(d) for d in depths],
    train_scores,
    marker="o",
    label="Training R2"
)

plt.plot(
    [str(d) for d in depths],
    cv_scores,
    marker="o",
    label="CV R2"
)

plt.xlabel("max_depth")
plt.ylabel("R2 Score")
plt.title("Decision Tree Hyperparameter Tuning")
plt.legend()
plt.show()