import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

listener_data = pd.DataFrame(
    {
        "weekly_listening_hours": [
            9.4,3.0,4.6,29.3,27.2,9.6,31.9,16.8,8.2,12.3,4.7,8.8,32.3,8.2,21.8,1.4,5.8,25.3,22.7,22.2,15.7,2.2,31.5,25.1,2.5,12.3,32.4,4.7,4.0,25.9,4.8,3.3,2.2,4.4,11.1,12.7,17.6,11.5,24.2,17.1,23.9,14.7,5.0,3.1,17.7,20.3,30.2,5.5
        ],
        "followed_genres_count": [
            5,1,3,11,14,7,11,7,4,8,1,4,12,7,12,3,1,14,11,10,6,2,12,12,1,6,14,1,3,8,3,3,1,2,6,5,4,5,12,5,14,5,2,3,7,8,12,3
        ],
    }
)


print("Rows 1 to 5:")
print(listener_data.head())
print(f"Count of all samples : {len(listener_data)}")


scaler = StandardScaler()
scaled_features = scaler.fit_transform(listener_data)


kmeans = KMeans(n_clusters=3, random_state=42)
clusters = kmeans.fit_predict(scaled_features)

listener_data["Cluster"] = clusters


plt.figure(figsize=(7, 5))
plt.scatter(
    listener_data["weekly_listening_hours"],
    listener_data["followed_genres_count"],
    c=listener_data["Cluster"],
    cmap="viridis",
)
plt.xlabel("Weekly Listening Hours")
plt.ylabel("Followed Genres Count")
plt.title("Music Listener Clusters")
plt.show()


print("\n--- Table of cluster analysis ---")
cluster_summary = (
    listener_data.groupby("Cluster")
    .agg(
        weekly_listening_hours_mean=("weekly_listening_hours", "mean"),
        followed_genres_count_mean=("followed_genres_count", "mean"),
        member_count=("Cluster", "count"),
    )
    .reset_index()
)

print(cluster_summary)