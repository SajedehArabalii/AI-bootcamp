"""
EVALUATION PROCEDURE:
    1- Train and test on the entire dataset
    2- Train/Test split
"""
from sklearn.datasets import load_iris
iris = load_iris()
X = iris.data
y = iris.target

# 1 for logistic regression
from sklearn.linear_model import LogisticRegression
logreg = LogisticRegression()
logreg.fit(X, y)
y_pred = logreg.predict(X)
print(y_pred)
print(len(y_pred))


# 1 Training accuracy for Logistic regression
from sklearn import metrics
print(metrics.accuracy_score(y, y_pred))

# 1 for KNN
from sklearn.neighbors import KNeighborsClassifier
#   K = 1
knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(X, y)
y_pred = knn.predict(X)
print("K=1 : ",metrics.accuracy_score(y, y_pred))

#   K = 5
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X, y)
y_pred = knn.predict(X)
print("K=5 : ",metrics.accuracy_score(y, y_pred))

#   K = 15
knn = KNeighborsClassifier(n_neighbors=15)
knn.fit(X, y)
y_pred = knn.predict(X)
print("K=15 : ",metrics.accuracy_score(y, y_pred))

# 2 
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.4,random_state=42
)

#   K = 1
knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)
print("K=1 : ",metrics.accuracy_score(y_test, y_pred))

#   K = 5
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)
print("K=5 : ",metrics.accuracy_score(y_test, y_pred))

#   K = 15
knn = KNeighborsClassifier(n_neighbors=15)
knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)
print("K=15 : ",metrics.accuracy_score(y_test, y_pred))


"""
How to find an even better value for K
"""
k_range = range(1, 20)
scores = []

for k in k_range:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_test)
    scores.append(metrics.accuracy_score(y_test, y_pred))

import matplotlib.pyplot as plt

plt.scatter(k_range, scores)
plt.xlabel("Value of k for knn")
plt.ylabel("Testing accuracy")
plt.show()

"""
Making predictions on out_of_sample data
"""
knn = KNeighborsClassifier(n_neighbors=12)
knn.fit(X, y)
print(knn.predict([[3, 5, 4, 2]]))

