"""
MENTAL CHEAT SHEET OF UNIVERSAL LINEAR REGRESSION ROUTE
1- Imports : mp, pd, plt, sklearn
2- Canvas : plt.figure(figsize = (width, height))
3- Features & Target : X(2D), y(1D)
4- Split : train_test_split(X, y)
5- fit : model.fit(X_train, y_train)
6- Predict : y_pred = model.predict(X_test) and y_proba = model.predict_proba(X_test)
7- Evaluate : accuracy_score, confusion metrix, classification_report
8- Inspect: Model.class_prior_
9- Plot : plt.scatter() & plt.axhline()
"""


"""
1- Core Imports
"""
import numpy as np # Math & array operations
import pandas as pd # Data manipulation / reading CSVs
import matplotlib.pyplot as plt  # Plotting
from sklearn.naive_bayes import GaussianNB  # Or MultinomialNB / BernoulliNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

"""
2- Set Canvas defaults
"""
plt.figure(figsize=(10, 5))

"""
3- Load Data & Isolate features(X) vs Target(y)
"""
df = pd.read_csv('data.csv')
x= df[['feature1', 'feature2']] # Double brackets = 2D DataFrame
y = df['target_class'] # Single bracket = 1D Series

"""
Step 4- Split into Train and Test Split
"""
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify= y
)

"""
5- Initialize & Fit the Naive Bayes Classifier
"""

model = GaussianNB()
model.fit(X_train, y_train)

"""
6- Predict Class Labels and Class Probabilities
"""
y_pred =model.predict(X_test)
y_proba = model.predict_proba(X_test)

"""
7- Evaluate Classification Performance
"""
acc = accuracy_score(y_test, y_pred)
cm = confusion_matrix(y_test, y_pred)

print(f"Accuracy: {acc:.3f}")
print("Confusion Matrix:\n", cm)
print(classification_report(y_test, y_pred))

"""
8- INspect Learned Parameters
"""
print(f"Class Priors P(Y): {model.class_prior_}")
print(f"Class Means (mu): {model.theta_}")
print(f"Class Variances (sigma^2): {model.var_}")

"""
9- Visual Verification (Probability Curve or Decision Boundary)"""
plt.scatter(X_test.iloc[:, 0], y_test, c=y_pred, cmap='bwr', alpha=0.6, label='Predicted')
plt.axhline(0.5, linestyle=':', color='gray', label='0.5 Decision Threshold')
plt.xlabel("Feature")
plt.ylabel("Target Class / Probability")
plt.legend()
plt.show()