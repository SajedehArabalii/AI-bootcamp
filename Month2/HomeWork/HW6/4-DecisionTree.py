
#-----------------------------------------------
# Q4_Decision Tree
#-----------------------------------------------

"""
Manual calculations:
    roots = 240 healthy patients + 60 malignent patients
    calculate Entropy and Gini
    left_age = 180 healthy and 10 malignent
    right_age = 60 healthy and 50 malignent
    calculate mean of weight Gini and Information Gain
"""
import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

healthy = 240
risk = 60
total = healthy + risk

p_h = healthy / total
p_r = risk / total

gini_root = 1 - (p_h**2 + p_r**2)
entropy_root = -(p_h*np.log2(p_h) + p_r*np.log2(p_r))

print("Root Gini:", gini_root)
print("Root Entropy:", entropy_root)

# Left child
left_h = 180
left_r = 10
left_total = left_h + left_r

p1 = left_h / left_total
p2 = left_r / left_total

gini_left = 1 - (p1**2 + p2**2)

# Right child
right_h = 60
right_r = 50
right_total = right_h + right_r

p1 = right_h / right_total
p2 = right_r / right_total

gini_right = 1 - (p1**2 + p2**2)

weighted_gini = (left_total/total)*gini_left + (right_total/total)*gini_right

information_gain = gini_root - weighted_gini

print("Left Gini:", gini_left)
print("Right Gini:", gini_right)
print("Weighted Gini:", weighted_gini)
print("Information Gain:", information_gain)
"""
using an example like XOR, explain why a decision tree can learn an algorithm that logistic regression can not
"""

# Use the x and why of 3.1 
# Train DecisionTreeClassifier(max_depth=4)
# Compare Accuracy to logistic regression Accuracy
# Compare _feature_importance to the weights of 3.2

df = pd.read_csv("titanic.csv")

df = df[["Fare","Age","Sex","Pclass","Survived"]]

df["Age"] = df["Age"].fillna(df["Age"].mean())

df = pd.get_dummies(df, columns=["Sex"], drop_first=True)

X = df.drop("Survived", axis=1)
y = df["Survived"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    stratify=y,
    random_state=42
)

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Logistic Regression
log_model = LogisticRegression(max_iter=1000)
log_model.fit(X_train_scaled, y_train)

log_pred = log_model.predict(X_test_scaled)

print("Logistic Accuracy:", accuracy_score(y_test, log_pred))

# Decision Tree
tree = DecisionTreeClassifier(max_depth=4, random_state=42)
tree.fit(X_train, y_train)

tree_pred = tree.predict(X_test)

print("Decision Tree Accuracy:", accuracy_score(y_test, tree_pred))

print("\nDecision Tree Feature Importances")
print(pd.Series(tree.feature_importances_, index=X.columns))

print("\nLogistic Regression Coefficients")
print(pd.Series(log_model.coef_[0], index=X.columns))
# Use dataset heart.csv
# features = age, chol, thal and target
# load dataset
# fill/remove empty data
# use stratigy to split 70/30
# Make 3 models of DecisionTreeClassifier,
# without limiation,
# with min_samples_leaf = 20
# with max_leaf_nodes = 8

# Report Accuracy and test
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

df = pd.read_csv("heart.csv")

df = df.dropna()

X = df.drop("target", axis=1)
y = df["target"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    stratify=y,
    random_state=42
)

models = {
    "Default":
        DecisionTreeClassifier(random_state=42),

    "min_samples_leaf=20":
        DecisionTreeClassifier(
            min_samples_leaf=20,
            random_state=42
        ),

    "max_leaf_nodes=8":
        DecisionTreeClassifier(
            max_leaf_nodes=8,
            random_state=42
        )
}

for name, model in models.items():

    model.fit(X_train, y_train)

    train_acc = accuracy_score(
        y_train,
        model.predict(X_train)
    )

    test_acc = accuracy_score(
        y_test,
        model.predict(X_test)
    )

    print(name)
    print("Train Accuracy:", train_acc)
    print("Test Accuracy:", test_acc)
    print()
"""
Which one is more prone to overfitting
Which scaling was necessary for these models
"""

# Bonus
# change the depth of the tree rom 1 to 8 on the titanic data,
# visualize the accuracy of each depth
# from which point optimization is no longer visible
import matplotlib.pyplot as plt

depths = range(1, 9)
scores = []

for depth in depths:

    model = DecisionTreeClassifier(
        max_depth=depth,
        random_state=42
    )

    model.fit(X_train, y_train)

    pred = model.predict(X_test)

    scores.append(
        accuracy_score(y_test, pred)
    )

plt.figure(figsize=(8,5))
plt.plot(depths, scores, marker='o')
plt.xlabel("Tree Depth")
plt.ylabel("Test Accuracy")
plt.title("Decision Tree Depth vs Test Accuracy")
plt.grid(True)
plt.show()