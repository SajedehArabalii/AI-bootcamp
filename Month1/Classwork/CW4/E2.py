# age, monthly_visits, avg_order_value, total_purchases
import numpy as np
customers = np.array([
 [22, 2, 15, 1],
 [25, 4, 20, 2],
 [47, 10, 120, 12],
 [52, 12, 150, 15],
 [35, 6, 60, 6],
 [38, 7, 70, 7],
 [19, 1, 10, 1],
 [60, 8, 130, 10],
 [41, 9, 90, 9],
 [28, 5, 35, 4],
 [33, 6, 55, 5],
 [55, 11, 160, 14]
])

print("dtypes: ", customers.dtype)
print("size: ", customers.size)
print("shape: ", customers.shape)
print("ndim: ",customers.ndim)

print("samples: ",customers.shape[0])
print("feates: ", customers.shape[1])

feature_names = np.array([
 "age",
 "monthly_visits",
 "avg_order_value",
 "total_purchases"])

mins = customers.min(axis = 0)
maxs = customers.max(axis = 0)
means = customers.mean(axis=0)
stds =  customers.std(axis=0)


for i, name in enumerate(feature_names):
    print(f"{name}: min={mins[i]}, max={maxs[i]}, mean={means[i]:.2f}, std={stds[i]:.2f}")


customers_scaled = (customers - mins) / (maxs - mins)

print("\ncustomers_scaled:\n", np.round(customers_scaled, 2))

print("\nmin scaled:", np.min(customers_scaled))
print("max scaled:", np.max(customers_scaled))

print("\nmean before scaling:", customers.mean(axis=0))
print("mean after scaling:", customers_scaled.mean(axis=0))