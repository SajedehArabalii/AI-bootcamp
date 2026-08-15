from sklearn.datasets import make_moons
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

# Generate classification data
X, y = make_moons(
    n_samples=100,
    noise=0.35,
    random_state=42
)


# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=42
)

# Very complex decision tree
tree = DecisionTreeClassifier(
    max_depth=None,
    random_state=42
)


tree.fit(X_train, y_train)


# Evaluate
train_accuracy = accuracy_score(
    y_train,
    tree.predict(X_train)
)

test_accuracy = accuracy_score(
    y_test,
    tree.predict(X_test)
)

print("Training Accuracy:", train_accuracy)
print("Testing Accuracy :", test_accuracy)

from sklearn.inspection import DecisionBoundaryDisplay


# plt.figure(figsize=(7,5))

# DecisionBoundaryDisplay.from_estimator(
#     tree,
#     X,
#     response_method="predict"
# )

# plt.scatter(
#     X[:,0],
#     X[:,1],
#     c=y,
#     edgecolor="black"
# )

# plt.title("Overfitted Decision Tree")

# plt.show()

plt.figure(figsize=(7,5))

# Add ax=plt.gca() right here:
DecisionBoundaryDisplay.from_estimator(
    tree,
    X,
    response_method="predict",
    ax=plt.gca()  
)

plt.scatter(X[:,0], X[:,1], c=y, edgecolor="black")
plt.title("Overfitted Decision Tree")
plt.show()