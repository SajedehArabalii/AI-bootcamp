import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans

np.random.seed(42)
plt.rcParams['figure.figsize'] = (10, 5)
X, y_true = make_blobs(n_samples=300, centers=3, cluster_std=1.0, random_state=42)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize = (12, 4.5))
ax1.scatter(X[:, 0], X[:,1], s=20, c='tab:gray')
ax1.set_title("What the algorithm sees: just points, no labels")
ax2.scatter(X[:, 0], X[:, 1], s=20, c=y_true, cmap="tab10")
ax2.set_title("The ground truth (hidden from the algorithm)")
plt.show()




kmeans = KMeans(n_clusters=3, n_init=10, random_state=42)
labels = kmeans.fit_predict(X)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize = (12, 4.5))
ax1.scatter(X[:, 0], X[:, 1], s=20, c=labels, cmap='tab10')
ax1.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=200, c='black', marker='X', label='centers')
ax1.set_title(f"K-Means result  (inertia={kmeans.inertia_:.1f})")
ax1.legend()
ax2.scatter(X[:, 0], X[:, 1], s=20, c=y_true, cmap="tab10")
ax2.set_title("Ground truth")
plt.show()


"""
kmeans_steps(X, K, n_iters=8, seed=0)

Purpose: Simulates the K-Means algorithm and records the cluster centers after each iteration, so you can visualize how they move.

Steps
Initialize K random cluster centers from the dataset.
Repeat n_iters times:
Compute the distance from every point to every center.
Assign each point to its nearest center.
Update each center to the mean of its assigned points.
Save the new centers in history.
Return history, which contains the centers at every iteration.

Output: A list of center positions over time, useful for animating or plotting the K-Means optimization process.
"""
def kmeans_steps(X, K, n_iters=8, seed=0):
    # Purpose: Use rng to generate reproducible random numbers without affecting NumPy's global random state. It's the modern replacement for np.random.seed().
    rng = np.random.default_rng(seed)
    # rng.choice(len(X), K, replace=False): Randomly selects K unique indices from the dataset
    centers = X[rng.choice(len(X), K, replace=False)].copy()
    history = [centers.copy()]
    for _ in range(n_iters):
        # assign
        d = np.linalg.norm(X[:, None, :] - centers[None, :, :], axis=2)
        labels = d.argmin(axis = 1)
        for k in range(K):
            if np.any(labels == k):
                centers[k] = X[labels == k].mean(axis=0)
        history.append(centers.copy())
    return history
        
steps = kmeans_steps(X, K=3, n_iters=6, seed=3)
fig,axes = plt.subplots(1, len(steps), figsize= (4 * len(steps), 4))
#zip() is a Python function that iterates over multiple sequences in parallel, pairing corresponding elements together.
for ax, centers, i in zip(axes, steps, range(len(steps))):
    d = np.linalg.norm(X[:, None, :] - centers[None, :, :], axis=2)
    lab = d.argmin(axis = 1)
    ax.scatter(X[:, 0], X[:, 1], s=12, c=lab, cmap='tab10')
    ax.scatter(centers[:, 0], centers[:, 1], s=150, c='black', marker='X', edgecolor='white')
    ax.set_title(f"iter {i}")
plt.tight_layout()
plt.show()



from sklearn.datasets import make_moons
X_moons, _ = make_moons(n_samples=300, noise=0.07, random_state=42)
km = KMeans(n_clusters=2, n_init=10, random_state=0).fit(X_moons)

plt.figure(figsize=(6, 5))
plt.scatter(X_moons[:, 0], X_moons[:, 1], s=20, c=km.labels_, cmap='tab10')
plt.scatter(km.cluster_centers_[:, 0], km.cluster_centers_[:, 1], s=200, c='black', marker='X')
plt.title("K-Means fails on non-spherical clusters (moons)")
plt.show()

ks = range(1, 11)
# Purpose: Compute the inertia for each value of K so you can plot the elbow curve and choose an appropriate number of clusters.
inertias = [KMeans(k, n_init=10, random_state=42).fit(X).inertia_ for k in ks]
"""
'ko-':

    k = black color.
    o = circle markers.
    - = connect the points with a solid line.
"""
plt.plot(ks, inertias, 'ko-', lw=2)
plt.xlabel('K')
plt.ylabel('inertia')
plt.title('Elbow method: where does the curve flatten?')
plt.axvline(3, color='tab:red', ls='--', label='elbow at K=3')
plt.legend()
plt.show()


from sklearn.cluster import DBSCAN
# DBSCAN on the moons
db = DBSCAN(eps=0.2, min_samples=5).fit(X_moons)
plt.figure(figsize=(6, 5))
plt.scatter(X_moons[:, 0], X_moons[:, 1], s=20, c=db.labels_, cmap="tab10")
plt.title(f"DBSCAN on moons: {len(set(db.labels_) - {-1})} clusters, "
          f"{(db.labels_ == -1).sum()} noise points")
plt.show()


