"""
MENTAL CHEAT SHEET OF UNIVERSAL LINEAR REGRESSION ROUTE
1- Imports : mp, pd, plt, sklearn
2- Canvas : plt.figure(figsize = (width, height))
3- Features / Target: X(2D), y(1D)
4- Split: train_test_split(X,y)
5- Fit: model.fit(X_train, y_train) with max_depth set(No scaling needed)
6- Predict : y_pred = model.predict(X_teest)
7- Evaluate : Check train vs test accuracy to detect overfitting
8- Inspect : model.feature_importance
9- Plot : plot_tree(model)
"""

"""
1- Core Imports
"""
import numpy as np # math and array operations
import pandas as pd # Data manipulation / reading CSVs 
import matplotlib.pyplot as plt # Plotting
from sklearn.tree import DecisionTreeClassifier, plot_tree # Model and visualization
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

"""
2- Set Canvas defaults
"""
plt.figure(figsize=(10, 5))

"""
3- Load Data and Isolate Features(X), target(y)
"""
df = pd.read_csv('data.csv')
X = df[['feature1', 'feature2']]
y = df['target']

"""
4- Split into Train and Test sets
"""
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

"""
5- Initialize and fit the decision Tree (Control Path)
"""
model = DecisionTreeClassifier(criterion='gini', max_depth=3, random_state=42)
model.fit(X_train, y_train)

"""
6- Make Predictions
"""
y_pred = model.predict(X_test)
y_proba = model.predict_proba(X_test)

"""
7- Evaluate Classification Performance
"""
print(f"Train Accuracy: {model.score(X_train, y_train):.3f}") # Check for overfitting
print(f"Test Accuracy:  {accuracy_score(y_test, y_pred):.3f}")
print("\nClassification Report:\n", classification_report(y_test, y_pred))

"""
8- Inspect feature Importance 
"""
# 1. Feature Importances (Gini importance)
print("Feature Importances:", model.feature_importances_)

"""
9- Visualize the Tree Diagram
"""
# 2. Visualize the Decision Tree Structure
plt.figure(figsize=(12, 8))
plot_tree(
    model, 
    feature_names=X.columns, 
    class_names=['Class 0', 'Class 1'], 
    filled=True, 
    rounded=True
)
plt.title("Decision Tree Decision Logic")
plt.show()