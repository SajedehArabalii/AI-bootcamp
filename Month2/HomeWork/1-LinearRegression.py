#------------------------------
#Q1_Linear Regression
#------------------------------
import numpy as np
from sklearn.datasets import fetch_california_housing  
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
"""
Temporary fix
"""
import os
import certifi

os.environ["SSL_CERT_FILE"] = certifi.where()

# TODO What is a frame?
housing = fetch_california_housing(as_frame=True) 
df = housing.frame 
# Median Income
X = df[["MedInc"]] 
# Median house value
y = df["MedHouseVal"]
print(df.info())


"""
Controls the format of the dataset returned by sklearn.
instructs scikit-learn to return the dataset as pandas DataFrames and Series, enabling easier data manipulation through labeled columns and pandas functionality
"""

#train = 70%
#test = 30%
#based on MedInc
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# train a linearRegression
model1 = LinearRegression()
model1.fit(X_train, y_train)
prediction1 = model1.predict(X_test)

# what are weight, bias and R2 (single feature)
# No [0] because x has only 1 feature
weight = model1.coef_
bias = model1.intercept_
R2 = model1.score(X_test, y_test)
print("Single Feature Model")
print("--------------------")
print("Slope:", weight)
print("Intercept:", bias)
print("R2:", R2)

# scatter plot
# TODO how to choose a figsize
"""
There is no mathematical formula. It depends on:

    amount of data
    readability
    screen/report size
"""
# It gave me error because X was not sorted
X_plot = np.sort(X_test.values, axis=0)
y_plot = model1.predict(X_plot)
plt.figure(figsize=(8, 5))
plt.scatter(
    X_test,
    y_test,
    color='blue',
    label='Actual Data' 
)
plt.plot(
    X_plot,
    y_plot,
    color='black',
    label='Regression Line'
)
plt.xlabel("MedInc")
plt.ylabel("MedHouseVal")
plt.title("Linear Regression using MedInc")
plt.legend()
plt.show()
# Do it again with MedInc، HouseAge، AveRooms
X = df[[
    "MedInc",
    "HouseAge",
    "AveRooms"
]]
y = df["MedHouseVal"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=42
)

model2 = LinearRegression()
model2.fit(X_train, y_train)

y_pred2 = model2.predict(X_test)

r2_three = r2_score(
    y_test,
    y_pred2
)

print("Three Feature Model")
print("-------------------")
print("Coefficients:", model2.coef_)
print("Intercept:", model2.intercept_)
print("R2:", r2_three)

# Compare R2 values
print("Single feature R2:", R2)

print("Three feature R2:", r2_three)

print(
    "Improvement:",
    r2_three - R2
)

"""
No, the improvement is modest.
Income is already the strongest predictor among these three features,
and the extra features only slightly improve prediction accuracy
"""
