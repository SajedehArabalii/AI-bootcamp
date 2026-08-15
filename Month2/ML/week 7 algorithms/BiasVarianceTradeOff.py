from sklearn.datasets import make_moons
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
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

depths = list(range(1, 6)) + [None]

train_scores = []
test_scores = []


for depth in depths:

    model = DecisionTreeClassifier(
        max_depth=depth,
        random_state=42
    )

    model.fit(
        X_train,
        y_train
    )

    train_scores.append(
        model.score(X_train, y_train)
    )

    test_scores.append(
        model.score(X_test, y_test)
    )


for d, train, test in zip(
    depths,
    train_scores,
    test_scores
):
    print(
        f"Depth={d}: "
        f"Train={train:.2f}, "
        f"Test={test:.2f}"
    )