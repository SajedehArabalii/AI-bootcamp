# import load_iris function from datasets module
from sklearn.datasets import load_iris

# Save "bunch" object containing iris dataset and its attributes
iris = load_iris()
print(type(iris))
print(iris.data)

"""
Row = observation, sample, example, instance, record
Column = feature, predictor, attribute, independant, input, regressor, covariate
Response = target, outcome,label, dependant variable
Classification = supervised learning in which the response is categorical
Regression = supervised learning in which the response is ordered and continuous
"""
print(iris.feature_names)
print(iris.target)
print(iris.target_names)


"""
REQUIREMENTS FOR WORKING WITH DATA IN SCIKIT-LEARN
    1- Feature and response are separate objects
    2- Features and response should be numeric
    3- Features and response should be NumPy arrays
    4- Features and response should have specific shapes
"""

# Check the types of the features and response
print(type(iris.data))
print(type(iris.target))

# Check the shape of the features ( first dimension = number of observations, second dimenstion = number of features)
print(iris.data.shape)

# Check the shape of the response ( single dimension matching the number of observations)
print(iris.target.shape)

# Store features in X and target in y
X = iris.data
y = iris.target

