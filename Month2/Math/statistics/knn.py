"""
MENTAL CHEAT SHEET OF UNIVERSAL LINEAR REGRESSION ROUTE
1- Imports : mp, pd, plt, sklearn, StandardScaler
2- Canvas : plt.figure(figsize = (width, height))
3- Features & Target : X(2D), y(1D)
4- Split : train_test_split(X, y)
5- Scale : StandardScaler().fit_transform(X_train) and (X_test)
6- fit : model.fit(X_train_scaled, y_train)
7- Predict : y_pred = model.predict(X_test_scaled) 
8- Evaluate : accuracy_score
9- Plot : loop through K to plot error curve
"""

"""
1 - Core Inputs
"""
import numpy as np # Math and array operations
import pandas as pd # Data manipulation / reading CSV
import matplotlib.pyplot as plt # Plotting
from sklearn.neighbors import KNeighborsClassifier # or KNeighborRegressor
from sklearn.preprocessing import StandardScaler  # Distance scaling ( critical )
from sklearn.model_selection import train_test_split # Split Data
from sklearn.metrics import accuracy_score, classification_report

"""
2-  Set Canvas Defaults
"""
plt.figure(figsize=(10, 5))

"""
3- Load data and Isolate features(X) vs Target(y)
"""
df = pd.read_csv('data.csv')
X = [['feature1', 'feature2']]
y = ['target']

"""
4- Split into Train and Test Sets
"""
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify = y
)

"""
5- Scale features (Mandetory for KNN)
"""
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.fit_transform(X_test)

"""
6- Initialize and fit the KNN Model
"""
model = KNeighborsClassifier(n_neighbors = 3)
model.fit(X_train_scaled, y_train)

"""
7- Make predictions
"""
y_pred = model.predict(X_test)

"""
8- Evaluate and find Optimal K (Elbow / Error Curve)
"""
print(f"Test Accuracy: {accuracy_score(y_test, y_pred):.3f}")
print(classification_report(y_test, y_pred))

# Find Best K (Optional Loop)
error_rates = []
for k in range(1, 20):
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train_scaled, y_train)
    pred_k = knn.predict(X_test_scaled)
    error_rates.append(np.mean(pred_k != y_test))

"""
9- Plot Error rate vs. K Value
"""
plt.plot(range(1, 20), error_rates, color='blue', linestyle='--', marker='o')
plt.title('Error Rate vs. K Value')
plt.xlabel('K')
plt.ylabel('Error Rate')
plt.show()
