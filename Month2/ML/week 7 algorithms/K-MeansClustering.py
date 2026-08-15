"""
Code
"""
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Generate synthetic dataset
X, _ = make_blobs(
    n_samples=500,
    centers=4,
    cluster_std=1.2,
    random_state=42
)

# Create K-Means model
model = KMeans(
    n_clusters=4,
    random_state=42,
    n_init=10
)

# Train the model and assign cluster labels
labels = model.fit_predict(X)

# Display cluster centers
print("Cluster Centers:")
print(model.cluster_centers_)

"""
Visualization
"""
# Visualize the clusters
plt.figure(figsize=(8, 6))

plt.scatter(
    X[:, 0],
    X[:, 1],
    c=labels,
    s=30,
    cmap="viridis"
)

plt.scatter(
    model.cluster_centers_[:, 0],
    model.cluster_centers_[:, 1],
    marker="X",
    s=250,
    color="red",
    label="Centroids"
)

plt.title("K-Means Clustering")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.legend()

plt.show()
