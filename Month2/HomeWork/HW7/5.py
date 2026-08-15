import pandas as pd
from sklearn.datasets import make_classification
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

X, y = make_classification(
    n_samples=400,
    n_features=4,
    n_informative=3,
    n_redundant=0,
    n_clusters_per_class=2,
    weights=[0.82, 0.18],
    flip_y=0.05,
    class_sep=0.9,
    random_state=42,
)

feature_names = ['accuracy_pct', 'reaction_time_ms', 'headshot_rate_pct', 'reports_count']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)


models = {
    "max_depth=1": DecisionTreeClassifier(max_depth=1, random_state=42),
    "max_depth=4": DecisionTreeClassifier(max_depth=4, random_state=42),
    "Without limit of depth": DecisionTreeClassifier(random_state=42),
}

print("--- Comparing Model Accuracy ---")
for name, clf in models.items():
    clf.fit(X_train, y_train)
    tr_acc = accuracy_score(y_train, clf.predict(X_train))
    te_acc = accuracy_score(y_test, clf.predict(X_test))
    diff = tr_acc - te_acc
    print(
        f"{name:18s} | Train Acc: {tr_acc:.4f} | Test Acc: {te_acc:.4f} | Diff: {diff:.4f}"
    )