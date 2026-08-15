"""
Cross Validation
"""
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics

iris = load_iris()
X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.4,random_state=42
)

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)
print(metrics.accuracy_score(y_test, y_pred))


"""
STEPS FOR K-FOLD CROSS VALIDATION
    1- Split the dataset into K equal partitions('folds')
    2- Use fold 1 as the testing set and the union of the other folds as the training set
    3- Calculate testing accuracy
    4- Repeat steps 2 and 3 K times, using a different fold as the testing set each time
    5- Use the average testing accuracy as the estimate of out-of-sample accuracy
"""

from sklearn.model_selection import KFold
# A 5 fold cross validation
kf = KFold(n_splits=5, shuffle=False)

# for iteration, data in enumerate(kf, start=1):
#     print(iteration, data[0], data[1])

for iteration, data in enumerate(kf.split(X), start=1):
    print(iteration, "\nTraining set: ", data[0], "\nTesting set: ", data[1])

"""
- K can be any number, but K=10 is generally recommended
- For classification problems, stratified sampling is recommended for creating the folds
    - Each response class should be represented with equal proportions in each of the K folds
    - scikit-learn cross_val_score function does this by default
"""

"""
Cross-valudation example: parameter tuning
"""
print("----------------------------------------")
from sklearn.model_selection import cross_val_score

knn = KNeighborsClassifier(n_neighbors=5)
scores = cross_val_score(knn, X, y, cv=10, scoring='accuracy')
print(scores)
print(scores.mean())

k_range = range(1, 31)
k_scores = []
for k in k_range:
    knn = KNeighborsClassifier(n_neighbors=k)
    scores = cross_val_score(knn, X, y, cv=10, scoring='accuracy')
    k_scores.append(scores.mean())
print(k_scores)

import matplotlib.pyplot as plt

plt.plot(k_range, k_scores)
plt.xlabel("Value of K for KNN")
plt.ylabel("Cross validation accuracy")
# plt.show()


"""
Cross Validation Example: MODEL SELECTION
"""

# Compare the best KNN model with logistic regression on the iris dataset
knn = KNeighborsClassifier(n_neighbors=20)
print(cross_val_score(knn, X, y, cv=10, scoring='accuracy').mean())

from sklearn.linear_model import LogisticRegression
logreg = LogisticRegression(max_iter=1000)
print(cross_val_score(logreg, X, y, cv=10, scoring='accuracy').mean())



"""
Cross Validation Example: feature selection
"""
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

data = pd.read_csv('data/Advertising.csv')
feature_cols = ['TV', 'Radio', 'Newspaper']
X = data[feature_cols]
y = data.Sales

# 10 fold cross validation with all three features
print("-----------------------------------------")
lr = LinearRegression()
scores = cross_val_score(lr, X, y, cv=10, scoring='neg_mean_squared_error')
print(scores)

# fix the sign of MSE scores
mse_score = -scores
print(mse_score)

# convert mse to rmse
rmse_scores = np.sqrt(mse_score)
print(rmse_scores)

# calculate the average rmse
print(rmse_scores.mean())


# Now the same as above but excluding newspaper
feature_cols = ['TV', 'Radio']
X = data[feature_cols]

print(np.sqrt(-cross_val_score(lr, X, y, cv=10, scoring='neg_mean_squared_error')).mean())





































