"""
1- Pick a value for K
2- Search for the K observations in the training data that are "nearest" to the measurements of the unknown list
3- Use the most popular response value from the K nearest neighbors as the predicted response value for the unknown iris
"""
# Review of the previous note
from sklearn.datasets import load_iris
iris = load_iris()
X = iris.data
y = iris.target

print(X.shape)
print(y.shape)

"""
SCIKIT-LEARN 4 STEPS MODELING PATTERN
    1- Import the class you plan to use
    2- "instantiate" the "estimator"
        - "Estimator" is scikit's term for model
        - "Instantiate" means "make and instance of"
        - Name of the object does not matter
        - Can specify tuning parameters during this step
        - All parameters not specified are set to their defaults
    3- Fit the model with data
        - Model is learning the relationship between X and y
        - Occurs in place
    4- Predict the response for a new observation
        - New Observations are called "out-of-sample" data
        - Uses the information it learned during the model training process
        - Returns NumPy array
        - Can predict for multiple observations at once
"""
# 1
from sklearn.neighbors import KNeighborsClassifier

# 2
# We change the n_neighbors number for a better fit
knn = KNeighborsClassifier(n_neighbors=1)

# 3
knn.fit(X, y)

# 4

X_new1 = ([[3, 5, 4, 2]])
X_new2 = ([3, 5, 4, 2], [5, 4, 3, 2])
print(knn.predict(X_new1))
print(knn.predict(X_new2))


"""
We can use the same 4 step for other classification modules
"""
from sklearn.linear_model import LogisticRegression

# It gives me the error Total of number of iterations reached limit, check why later
# because it has a max_iter of 100
logreg = LogisticRegression(max_iter=150)
logreg.fit(X, y)

print(logreg.predict(X_new2))