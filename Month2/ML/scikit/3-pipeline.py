"""
Pandas
"""
import pandas as pd 

data= pd.read_csv('data/Advertising.csv', index_col = 0)
print(data.head())
print(data.tail())
print(data.shape)

"""
Visualizing data using seaborn
"""
import seaborn as sns
import matplotlib.pyplot as plt

# Visualize the relationship between the features and the response using scatterplots
sns.pairplot(data, x_vars=['TV', 'Radio', 'Newspaper'], y_vars='Sales' )#, size = 7, aspect = 0.7, kind = reg
# plt.show()

"""
Preparing X and y using panda
"""
feature_cols = ['TV', 'Radio', 'Newspaper']
X = data[feature_cols]
print(X.head())

y = data.Sales
print(y.head())

"""
Train test split
"""
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=1
)

"""
Linear Regression
"""
from sklearn.linear_model import LinearRegression
linreg = LinearRegression()
linreg.fit(X_train, y_train)
y_pred = linreg.predict(X_test)

"""
Interpretting model coefficients
"""
print(linreg.intercept_)
print(linreg.coef_)
# pair the feature names with the coefficients
# zip(feature_cols, linreg.coef_)

for feature, coef in zip(feature_cols, linreg.coef_):
    print(feature, coef)

"""
Evaluation
"""
from sklearn import metrics
import numpy as np

true = [100, 50, 30, 20]
pred = [90, 50, 50, 30]


"""
    # MAE
        print(metrics.mean_absolute_error(true, pred    

    # MSE
        print(metrics.mean_squared_error(true, pred)    

    # RMSE
        print(np.sqrt(metrics.mean_squared_error(true, pred)    
"""


# RMSE for our our sales prediction
print(np.sqrt(metrics.mean_squared_error(y_test, y_pred)))


"""
Feature Selection = our model without newspaper is slightly better than the previous
"""

feature_cols = ['TV', 'Radio']

X = data[feature_cols]
y = data.Sales

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=1
)

linreg.fit(X_train, y_train)
y_pred = linreg.predict(X_test)

print(np.sqrt(metrics.mean_squared_error(y_test, y_pred)))

























































