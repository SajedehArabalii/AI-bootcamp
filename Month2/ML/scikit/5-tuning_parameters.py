from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score
import matplotlib.pyplot as plt
import numpy as np

iris = load_iris()
X = iris.data
y = iris.target

# 10fold cross validation with k = 5 for knn
knn = KNeighborsClassifier(n_neighbors=5)
scores = cross_val_score(knn, X, y, cv=10, scoring='accuracy')
print(scores)
# use average accuracy as a estimate of out-of-sample accuracy
print(scores.mean())

# Search for an optional value of K for KNN
k_range = range (1, 31)
k_scores = []
for k in k_range:
    knn = KNeighborsClassifier(n_neighbors=k)
    scores = cross_val_score(knn, X, y, cv=10, scoring='accuracy')
    k_scores.append(scores.mean())
print(k_scores)

plt.plot(k_range, k_scores)
plt.xlabel("Values of k in knn")
plt.ylabel('Cross validation accuracy')
# plt.show()

"""
More efficient parameter tuning using GridSearchCV
"""
print("*****************************************************")
from sklearn.model_selection import GridSearchCV

knn = KNeighborsClassifier()
# define the parameter values that should be searched
k_range = range(1,31)

# define the parameter values that should be searched
param_grid = dict(n_neighbors=k_range)
# print(param_grid)

# instantiate the grid
grid = GridSearchCV(knn, param_grid, cv=10, scoring='accuracy')
# print(grid)

grid.fit(X, y)
# print(grid.cv_results_)

import pandas as pd
results = pd.DataFrame(grid.cv_results_)
# print(results[['param_n_neighbors', 'mean_test_score']].to_string(index=False))
print(results[['param_n_neighbors', 'mean_test_score', 'std_test_score', 'rank_test_score']].to_string(index=False))

# Examining the first tuple
print(grid.cv_results_['params'][0])
print([
    grid.cv_results_[f'split{i}_test_score'][0]
    for i in range(10)
])
print(grid.cv_results_['mean_test_score'][0])

print("+++++++++++++++++++++++++++++++++++++++++++")
# create a list of mean scores only
grid_mean_scores = list(grid.cv_results_['mean_test_score'])
print(grid_mean_scores)

# plotting the result
plt.plot(k_range, grid_mean_scores)
plt.xlabel("Value of k for KNN")
plt.ylabel("Cross Validated Accuracy")
# plt.show()

# Examine the best model
print("=====================================")
print(grid.best_score_)
print(grid.best_params_)
print(grid.best_estimator_)


"""
Searching multiple parameters simultaneously
"""
# Define the parametere values that should be searched
k_range = range(1, 31)
weight_options = ['uniform', 'distance']

# Create a parameter grid: map the parameter names to the values that should be searched
param_grid = dict(n_neighbors = k_range, weights = weight_options)
print(param_grid)

grid = GridSearchCV(knn, param_grid, cv=10, scoring='accuracy')
grid.fit(X, y)

# view the result
print(pd.DataFrame(grid.cv_results_)[['mean_test_score', 'std_test_score', 'params']])# .to_string(index=False)

# examine the best model
print(grid.best_score_)
print(grid.best_params_)

"""
Using the best parameters to make predictions
"""
# train your model using all data and the best known parameters
knn = KNeighborsClassifier(n_neighbors=13, weights='uniform')
knn.fit(X, y)
y_pred = knn.predict([[3, 5, 4, 2]])
print(y_pred)
grid_pred = grid.predict([[3, 5, 4, 2]])
print(grid_pred)

"""
Reducing computational expense using RandomizedSearchCv
"""
from sklearn.model_selection import RandomizedSearchCV

# specify 'parameter distributions' rather than a 'parameter grid'
param_dist = dict(n_neighbors = k_range, weights = weight_options)

# IMPORTANT : specify a continuous distribution( rather than a list of values ) for any continous parameters

# n_iter controls the number of searches
rand = RandomizedSearchCV(knn, param_dist, cv=10, scoring='accuracy', n_iter=10, random_state=5)
rand.fit(X, y)
print(pd.DataFrame(rand.cv_results_)[['mean_test_score', 'std_test_score', 'params']])

# examine the best model
print(rand.best_score_)
print(rand.best_params_)

# run randomized search cv 20 times ( with n_iter=10) and record the best score
best_scores = []
for _ in range(20):
    rand = RandomizedSearchCV(knn, param_dist, cv =10, scoring='accuracy', n_iter=10)
    rand.fit(X, y)
    best_scores.append(round(rand.best_score_,3))

print(*best_scores)























