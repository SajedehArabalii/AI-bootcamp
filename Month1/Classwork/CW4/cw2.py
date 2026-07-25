import numpy as np
#age, monthly_visits, avg_order_value, total_purchases 
 
customers = np.array([ 
    [22,  2,  15,  1], 
    [25,  4,  20,  2], 
    [47, 10, 120, 12], 
    [52, 12, 150, 15], 
    [35,  6,  60,  6], 
    [38,  7,  70,  7], 
    [19,  1,  10,  1], 
    [60,  8, 130, 10], 
    [41,  9,  90,  9], 
    [28,  5,  35,  4], 
    [33,  6,  55,  5], 
    [55, 11, 160, 14] 
])

"""
Part1
"""

print(f"Customers matrix dimension: {customers.ndim}")
print(f"Customers matrix shape: {customers.shape}")
print(f"Customers size size: {customers.size}")
print(f"Customers matrix data type: {customers.dtype}")

print(f"samples: {customers.shape[0]}")
print(f"features: {customers.shape[1]}")

"""
Part2
"""
mins = np.min(customers, axis=0)
maxs = np.max(customers,axis=0)
means = np.mean(customers,axis=0)
stds = np.std(customers, axis=0)

feature_names = np.array([ 
    "age", 
    "monthly_visits", 
    "avg_order_value", 
    "total_purchases"
])


age = customers[:, 0]
monthly_visits = customers[:, 1]
avg_order_value = customers[:, 2]
total_purchases = customers[:, 3]


# TODO come back to this
print(f"{'Feature':<20} {'Min':>8} {'Max':>8} {'Mean':>10} {'Std':>10}")

for feature, min_val, max_val, avg, sd in zip(feature_names, mins, maxs, means, stds):
    print(f"{feature:<20} {min_val:>8.2f} {max_val:>8.2f} {avg:>10.2f} {sd:>10.2f}")

highest_mean = np.max(means)
highest_std = np.max(stds)

"""
Part3
"""
scaled_customers = (customers - mins) / (maxs - mins)
# print(scaled_customers.max())
# print(scaled_customers.min())

"""
Part4
"""
# age, monthly_visits, avg_order_value, total_purchases 
 
ref_points = np.array([ 
    [23,  2,  15,  1],    # low activity 
    [32,  5,  45,  4],    # normal 
    [42,  8,  85,  8],    # loyal 
    [55, 12, 150, 14]     # VIP 
])

ref_names = np.array([ 
    "low activity", 
    "normal", 
    "loyal", 
    "VIP" 
])

scaled_ref_points = (ref_points - mins) / (maxs - mins)

#TODO come back to this
distances = np.linalg.norm(
    scaled_customers[:, None] - scaled_ref_points,
    axis=2
)
print(distances.shape)

nearest = np.argmin(distances, axis = 1)
# print(nearest)

cluster = ref_names[nearest]

for i in range(len(nearest)):
    print(f"Customer {i+1} -> {cluster[i]}")

"""
Part5
"""
low = len(np.where(cluster == "low activity")[0])
normal = len(np.where(cluster == "normal")[0])
loyal = len(np.where(cluster== "loyal")[0])
VIP = len(np.where(cluster == "VIP")[0])

print(f"Amount of low activity customers {low}")
print(f"Amount of normal customers {normal}")
print(f"Amount of VIP customers {VIP}")
print(f"Amount of loyal customers {loyal}")

# TODO come back to this
avg_order_values = []

for name in ref_names:
    avg = np.mean(customers[cluster == name, 2])
    avg_order_values.append(avg)

highest_av = np.argmax(avg_order_values)
print(f"Cluster with the higest average: {highest_av}")


monthly_visits =[]
for name in ref_names:
    visits = np.mean(customers[cluster == name,1])
    monthly_visits.append(visits)
highest_mv = np.argmax(monthly_visits)
print(f"Cluster with the highest montly visits: {highest_mv}")

"""
Part6
"""
# if total_purchases >=8=> valuable
# else => regular
customer_label = np.where(total_purchases >= 8 , "Valuable", "Regular")
# print(customer_label)

# valuable = np.where(customer_label == "Valuable")
# regular = np.where(customer_label == "Regular")
#TODO check this part again
regular_avg_mean = np.mean(customers[customer_label == "Regular",2])
valuable_avg_mean = np.mean(customers[customer_label == "Valuable",2])

print(f"Regular customers average order value: {regular_avg_mean:.2f}")
print(f"Valuable customers average order value: {valuable_avg_mean:.2f}")

valuable_mv_mean = np.mean(customers[customer_label == "Valuable",1])
regular_mv_mean = np.mean(customers[customer_label == "Regular",1])

print(f"Regular monthly visit average: {regular_mv_mean:.2f}")
print(f"Valuable monthly visit average: {valuable_mv_mean:.2f}")

"""
Part7
"""
outlier_customer = np.array([[30, 1, 500, 1]])
customers_with_outlier = np.vstack((customers,outlier_customer))

# print(customers_with_outlier.shape)

mins = np.min(customers_with_outlier, axis=0)
maxs = np.max(customers_with_outlier, axis=0)

customers_with_outlier_scaled = (customers_with_outlier - mins) / (maxs - mins)
# print(f"{customers_with_outlier_scaled.min()} , {np.max(customers_with_outlier_scaled)}")

center = np.mean(customers_with_outlier_scaled, axis=0)

customer_distance = np.linalg.norm((customers_with_outlier_scaled[:,None] - center), axis=2)
farthest = np.argmax(customer_distance)
#TODO come back to this
if np.array_equal(customers_with_outlier[farthest], outlier_customer[0]):
    print("Yes")
else:
    print("No")

"""
Part8
"""
#TODO come back to this
diff = scaled_customers[:,np.newaxis,:] - scaled_customers[np.newaxis,:,:]

# print(diff.shape)
distance_matrix = np.linalg.norm(diff, axis=2)
# print(distance_matrix.shape)
print(np.diag(distance_matrix))
# Every customer has 0 distance from itself

# Ignore self distances
np.fill_diagonal(distance_matrix,np.inf)

nearest = np.argmin(distance_matrix, axis=1)

for i in range(len(nearest)):
    print(f"Customer {i+1} is closest to customer {nearest[i]+1}")

"""
Part 9 
"""
# age, monthly_visits, avg_order_value, total_purchase
new_customer = np.array([40, 9, 100, 9])
new_customer_scaled = (new_customer - mins)/ (maxs - mins)
# print(new_customer_scaled.min())
# print(new_customer_scaled.max())

distance_new_data = np.linalg.norm((new_customer_scaled - scaled_ref_points),axis=1)
# print(distance_new_data)

nearest = np.argmin(distance_new_data)
prediction_ref = ref_names[nearest]
prediction_value = np.where(new_customer[-1]>=8, "Valuable", "Regular")
print(f"Nearest cluster: {prediction_ref}")
print(f"Business label: {prediction_value}")

#TODO the rest of 10 to 15

