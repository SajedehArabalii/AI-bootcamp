import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.inspection import DecisionBoundaryDisplay

np.random.seed(42)
plt.rcParams['figure.figsize'] = (16, 7)
plt.rcParams['axes.facecolor'] = '#f8f9fa'

# Synthetic non linear data
n = 150
X = np.random.uniform(-3, 3, (n,2))

# Positive if both are positive or both are negative
y = (X[:, 0] * X[:, 1] > 0).astype(int)

# Train the decision tree
#set max_depth = 3 (An unconstrained tree woul overfit)
# Creating an ugly, jagged boundary. /depth 3 captures the XOR clearly
# random state = controls random seed
clf = DecisionTreeClassifier(max_depth=3, random_state=42)
clf.fit(X, y)

"""
plt.subplots(1, 2): Creates a figure with 1 row and 2 columns of subplots.
fig: The overall figure (the entire window/canvas).
ax1: The first subplot (left).
ax2: The second subplot (right).

+-------------------------------+
|          fig                  |
|  +---------+ +---------+      |
|  |  ax1    | |  ax2    |      |
|  +---------+ +---------+      |
+-------------------------------+
"""
fig, (ax1, ax2) = plt.subplots(1, 2)

# Subplot 1 : Decision Boundary
# Use a diverging colormap to clearly distinguish the two classes

"""
DecisionBoundaryDisplay.from_estimator(...): Draws the model's decision boundary.
clf: The trained classifier.
X: The feature data used to determine the plotting range.
response_method="predict": Colors each region according to the predicted class.
cmap="RdBu": Uses the Red–Blue colormap for the classes.
alpha=0.6: Makes the colored regions 60% opaque.
ax=ax1: Draws the boundary on the first subplot (ax1)
"""
DecisionBoundaryDisplay.from_estimator(
    clf, X, response_method='predict', 
    cmap = 'RdBu', alpha=0.6, ax=ax1
)

# Plot the actual data points on top
"""
X[:, 0]: x-coordinates (Feature 1).
X[:, 1]: y-coordinates (Feature 2).
c=y: Colors each point according to its class label.
cmap="RdBu": Uses the Red–Blue colormap for the classes.
edgecolor="black": Draws a black outline around each point.
s=60: Marker size.
linewidth=1.2: Thickness of the black outline.
"""
scatter = ax1.scatter(
    X[:, 0], X[:, 1], c=y, cmap='RdBu',
    edgecolor='black', s=60, linewidth=1.2
)

ax1.set_title("Decision Boundary (XOR Pattern)", fontsize=14, fontweight='bold')
ax1.set_xlabel("Feature $X_1$", fontsize=12)
ax1.set_ylabel("Feature $X_2$", fontsize=12)
# set_xlim(min, max): Sets the range of the x-axis
ax1.set_xlim(-3.2, 3.2)
ax1.set_ylim(-3.2, 3.2)

# Subplot 2: tree structure
"""
clf: The trained decision tree.
feature_names=[...]: Labels the features used in each split.
class_names=[...]: Labels the classes shown in the leaf nodes.
filled=True: Colors nodes based on the majority class.
rounded=True: Uses rounded corners for nodes.
fontsize=10: Sets the text size.
ax=ax2: Draws the tree on the second subplot (ax2)
"""
plot_tree(
    clf,
    feature_names=["Feature 1", "Feature 2"],
    class_names=["Class 0", "Class 1"],
    filled=True,       # Colors the nodes based on majority class
    rounded=True,      # Rounds the corners of the nodes
    fontsize=10, 
    ax=ax2
)
ax2.set_title("Learned Tree Structure", fontsize=14, fontweight='bold')
#tight_layout(): Automatically adjusts the spacing between subplots and plot elements.
plt.tight_layout()
plt.show()

import matplotlib.pyplot as plt
from sklearn.datasets import make_moons
from sklearn.tree import DecisionTreeClassifier
from sklearn.inspection import DecisionBoundaryDisplay


"""
make_moons(): Generates a synthetic dataset of two interleaving half-moon shapes.
n_samples=150: Creates 150 data points.
noise=0.3: Adds random noise, making the classes overlap and the problem more realistic.
random_state=432: Ensures the same dataset is generated every time.
"""
X, y = make_moons(n_samples=150, noise=0.3, random_state=432)

# Fit two trees: one shallow, one completely unconstrained
clf_overfit = DecisionTreeClassifier(random_state=42)# No constraint
clf_regularized = DecisionTreeClassifier(max_depth=3, min_samples_leaf=5, random_state=42)

clf_overfit.fit(X,y)
clf_regularized.fit(X,y)

# Plot the results
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Overfitted
DecisionBoundaryDisplay.from_estimator(
    clf_overfit, X, cmap="RdBu", alpha=0.3,
    ax=ax1, response_method='predict'
)
ax1.scatter(X[:, 0], X[:, 1], c=y, cmap="RdBu", edgecolor="k", s=30)
ax1.set_title("Unconstrained Tree (Overfitting to noise)")


# Regularized
DecisionBoundaryDisplay.from_estimator(clf_regularized, X, cmap="RdBu", alpha=0.3, ax=ax2, response_method="predict")
ax2.scatter(X[:, 0], X[:, 1], c=y, cmap="RdBu", edgecolor="k", s=30)
ax2.set_title("Regularized Tree (max_depth=3, generalizes well)")

plt.show()

# Print Out The Exact Rules The Tree Learned
from sklearn.tree import plot_tree

# fit a small tree on synthetic 2D data
clf_small = DecisionTreeClassifier(max_depth=3, random_state=42)
clf_small.fit(X, y)

#  Render the tree structure
plt.figure(figsize=(12,8))
plot_tree(
    clf_small,
    filled=True,
    feature_names=['feature1', 'feature2'],
    class_names=['class0', 'class1'],
    rounded=True
)

plt.title("Visualizing the Learned Decisions")
plt.show()
# Purpose: Measures how much each feature helped reduce impurity (Gini/Entropy) across all splits in the tree. Higher value = more important feature.
importances = clf_regularized.feature_importances_
print("Feature Importances:")
for i, imp in enumerate(importances):
    print(f"Feature {i+1}: {imp:.3f}")



