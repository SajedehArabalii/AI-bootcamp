import numpy as np
import pandas as pd
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

flight_data = pd.DataFrame(
    {
        "days_before_flight": [
            6,64,81,82,56,14,77,34,72,83,25,49,33,46,5,35,13,2,75,38,85,82,25,18,68,71,44,65,80,24,28,71,11,58,28,45,15,8,56,80,65,41,28,6,54,72,51,60,2,4,9,88,82,69,73
        ],
        "distance_km": [
            575,2245,1234,3510,2458,1752,564,1229,685,1291,4245,718,319,3456,2142,743,793,1140,1362,2259,419,4258,4171,3104,3216,3504,2533,2669,2088,4486,930,4032,662,3818,4016,3190,4378,1985,1231,2813,2866,4244,2077,614,3949,1424,4340,1105,1929,2600,3550,4009,2305,2051,2358
        ],
        "num_stops": [
            0,1,0,1,0,0,2,2,2,0,0,2,0,1,1,1,0,1,2,2,2,2,0,1,2,2,0,0,2,1,1,2,0,1,1,2,2,1,2,2,1,1,0,2,1,2,1,0,1,0,2,0,2,2,1
        ],
        "ticket_price_usd": [
            335,380,275,391,458,431,61,331,133,233,683,214,308,506,476,298,402,480,162,390,63,425,705,569,368,400,474,375,233,703,354,443,380,492,571,475,663,495,207,287,401,595,453,357,544,189,552,254,476,609,611,456,224,246,315
        ],
    }
)



X = flight_data[["days_before_flight", "distance_km", "num_stops"]]
y = flight_data["ticket_price_usd"]


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

knn = KNeighborsRegressor(n_neighbors=5)
knn.fit(X_train_scaled, y_train)


y_pred = knn.predict(X_test_scaled)
print(f"MAE: {mean_absolute_error(y_test, y_pred):.2f}")
print(f"MSE: {mean_squared_error(y_test, y_pred):.2f}")
print(f"R²:  {r2_score(y_test, y_pred):.2f}")


k_values = [1, 3, 5, 7, 9, 15]
print("\n--- R2 for different ks ---")
for k in k_values:
    model_k = KNeighborsRegressor(n_neighbors=k)
    model_k.fit(X_train_scaled, y_train)

    y_pred = model_k.predict(X_test_scaled)

    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print(f"K={k:2d} -> MAE={mae:.2f}, R²={r2:.4f}")


sample = pd.DataFrame(
    [[20, 2000, 1]],
    columns=["days_before_flight", "distance_km", "num_stops"],
)
sample_scaled = scaler.transform(sample)
pred_price = knn.predict(sample_scaled)
print(f"\nPrediction of flight price for sample: ${pred_price[0]:.2f}")