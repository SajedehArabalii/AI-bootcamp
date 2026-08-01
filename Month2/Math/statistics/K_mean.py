"""
MENTAL CHEAT SHEET OF UNIVERSAL LINEAR REGRESSION ROUTE
1- Imports : mp, pd, plt, sklearn, StandardScaler
2- Canvas : plt.figure(figsize = (width, height))
3- Features only: No y! unsupervised
4- Scale : X_scaled = StandardScaler().fit_transform(X) ( critical )
5- Elbow Method Loop K from 1-10 to plot : kmeans.inertia_
6- Fit/Predict : cluster_labels = kmeans.fit_predict(X_scaled)
7- Evaluate: Silhouetter_score(X_scaled, cluster_labels)
8- Inspect : kmeans.cluster_centers_
9- Plot: plt.scatter() with c=cluster_labels and centroid markers
"""


"""
1- Core Imports
"""
import numpy as np # Math and array operations
import pandas as pd # Data Manipulation / reading CSV
import matplotlib.pyplot as plt # Plotting
from sklearn.cluster import KMeans # The Clustering Model
from sklearn.preprocessing import StandardScaler # Distance scaling( critical )
from sklearn.metrics import silhouette_score # Evaluate performance using unsupervised geometric quality metrics

"""
2- Set Canvas Defaults
"""
plt.figure(figsize=(10, 5))

"""
3- Load Data and Isolate Features (X), because k_means is and unsupervised model , there is no target variable
"""
df = pd.read_csv('data.csv')
X = df[['feature1', 'feature2']]

"""
4- Scale Features (Mandetory for Distance based clustering)
"""
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

"""
5- Find Optimal K Using the Elbow Method (Inertia Curve)
"""
inertia_list = []
k_range = range(1, 11)

for k in k_range:
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    kmeans.fit(X_scaled)
    inertia_list.append(kmeans.inertia_)  # Inertia = SSE to centroids

plt.plot(k_range, inertia_list, marker='o', color='blue')
plt.title('Elbow Method For Optimal K')
plt.xlabel('Number of Clusters (K)')
plt.ylabel('Inertia (SSE)')
plt.show()

"""
6- Initialize & fit Model with chosen K
"""
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
cluster_labels = kmeans.fit_predict(X_scaled)

"""
7- Evaluate Clustering Quality
"""
score = silhouette_score(X_scaled, cluster_labels)
print(f"Inertia (SSE): {kmeans.inertia_:.3f}")
print(f"Silhouette Score: {score:.3f}")  # Ranges -1 to +1 (higher is better)

"""
8-Inspect Centroids and Visualize Clusters
"""
# 1. Extract learned cluster centers (in scaled units)
centroids = kmeans.cluster_centers_

# 2. Plot clustered data
plt.scatter(X_scaled[:, 0], X_scaled[:, 1], c=cluster_labels, cmap='viridis', alpha=0.6, label='Data Points')

# 3. Plot centroid locations (red X markers)
plt.scatter(centroids[:, 0], centroids[:, 1], s=200, c='red', marker='X', label='Centroids')

plt.xlabel("Feature 1 (Scaled)")
plt.ylabel("Feature 2 (Scaled)")
plt.title("K-Means Clustering Results")
plt.legend()
plt.show()