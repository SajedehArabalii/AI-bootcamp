"""
MENTAL CHEAT SHEET OF UNIVERSAL LINEAR REGRESSION ROUTE
1- Imports : mp, pd, plt, sklearn
2- Canvas : plt.figure(figsize = (width, height))
3- Features & Target : X(2D), y(1D)
4- Split : train_test_split(X, y)
5- fit : model.fit(X_train, y_train)
6- Predict : y_pred = model.predict(X_test)
7- Evaluate : r2_score, mean_squared_error
8- Inspect: Coefficients
9- Plot : plt.scatter() & plt.plot()
"""

"""
1-Core imports(The Big 3 + sklearn)
"""
import numpy as np # Math and array operations
import pandas as pd # Data manipulation / reading CSVs
import matplotlib.pyplot as plt # Plotting
from sklearn.linear_model import LinearRegression # The model itself
from sklearn.model_selection import train_test_split # Split train from test data
from sklearn.metrics import mean_squared_error, r2_score # Model Evaluation Metrics

"""
2- Set Canvas defaults (Optional but Standard)
your plot dimensions at the top so every plot looks consistant
"""
plt.figure(figsize=(10, 5))
# or: sns.set_theme(rc={'figure.figsize': (10, 5)})

"""
3- Load Data and Isolate Features vs Targets
"""
df = pd.read_csv('data.csv')
X = df[['feature_1', 'feature_2']] # Double brackets = @D DataFrame
y = df['target'] # Single bracket = Series / 1D

"""
4- Split into Train and Test sets
"""
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size= 0.2, random_state=42
)

"""
5- Initialize & fit the model
"""
model = LinearRegression()
model.fit(X_train, y_train) # Learns coefficients (w1) and intercept (w0, Bias)

"""
6_ Make predictions
"""
y_pred = model.predict(X_test)

"""
7- Evaluate the model
"""
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

print(f"RMSE: {rmse:.3f}")
print(f"R² Score: {r2:.3f}")

"""
8- Inspect Coefficients 
"""
# Inspect Learned Parameters
print(f"Intercept (w0): {model.intercept_:.3f}")
print(f"Coefficients (w1...): {model.coef_}")


"""
9- Plotting
"""
# Visual Verification (Data vs Predicted Line or Residuals)
plt.scatter(X_test.iloc[:, 0], y_test, alpha=0.6, label='Actual Data')
plt.plot(X_test.iloc[:, 0], y_pred, color='red', label='Regression Line')
plt.xlabel("Feature")
plt.ylabel("Target")
plt.legend()
plt.show()