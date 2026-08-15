#------------------------------
# Q2_Bayes and KNN
#------------------------------
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
"""
Part A
"""

# 2 flour categories
#    1- Healthy
#    2- Flawed
# 92% healthy
# 8% flawed
# healthy weight = 1000g , std 15
# flawed wight = 940g , std 25


#Prior probability
P_healthy = 0.92
P_flawed = 1 - P_healthy

# Parameters of the 2 Gaussian distribution
healthy_mean = 1000
healthy_std = 15
flawed_mean = 940
flawed_std = 25

X = np.linspace(850, 1050, 1000)  

# Compute the conditional probability density
# P(x | Healthy)
# P(x | Flawed)
healthy_pdf = norm.pdf(
    X, loc = healthy_mean, scale = healthy_std
)
flawed_pdf = norm.pdf(
    X, loc = flawed_mean, scale = flawed_std
)


# check the plot and describe whether these are completely seperated or have (hampooshani?)
# Plot both gaussian distributions
plt.figure(figsize=(8, 5))
plt.plot(
    X, healthy_pdf, label='Healthy Rags'
)
plt.plot(
    X, flawed_pdf, label='flawed Rags'
)
plt.xlabel("Weight (g)")
plt.ylabel("Probability Density")
plt.title("Conditional Probability Densities")
plt.legend()
plt.grid(True)
plt.show()


# A sack of flours has 970g weight
# P(healthy) * P(x|healthy)
# P(flawed) * p(x|flawed)
# in x= 970 (code or manual), what does bayes think about this
weight = 970
P_X_given_healthy = norm.pdf(
    weight, loc=healthy_mean, scale= healthy_std
)
P_X_given_flawed = norm.pdf(
    weight, loc=flawed_mean, scale= flawed_std
)

healthy_score = P_healthy * P_X_given_healthy
flawed_score = P_flawed * P_X_given_flawed

# print("P(Healthy) × P(x|Healthy) =", healthy_score)
# print("P(Flawed) × P(x|Flawed) =", flawed_score)

if healthy_score > flawed_score:
    print("Prediction: Healthy Bag")
else:
    print("Prediction: Flawed Bag")

"""
-----------------------------------------------------------
"""
# ---------------------------------------------------
# Manual Gaussian calculation
#
# f(x) =
# (1 / (σ√(2π))) *
# exp(-(x-μ)^2 / (2σ²))
# ---------------------------------------------------

healthy_manual = (
    1 / (healthy_std * np.sqrt(2 * np.pi))
) * np.exp(
    -((weight - healthy_mean) ** 2)
    / (2 * healthy_std ** 2)
)

flawed_manual = (
    1 / (flawed_std * np.sqrt(2 * np.pi))
) * np.exp(
    -((weight - flawed_mean) ** 2)
    / (2 * flawed_std ** 2)
)

print("\nManual Calculation")
print("------------------")
print("P(x|Healthy) =", healthy_manual)
print("P(x|Flawed) =", flawed_manual)

print("\nWeighted Manual Values")
print("----------------------")
print("Healthy =", P_healthy * healthy_manual)
print("Flawed =", P_flawed * flawed_manual)
"""
-----------------------------------------------------------
"""
"""
Part B
"""
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# wine => sklearn.datasets.load_wine
# X, y = load_wine(return_X_y=True)
wine = load_wine
X = wine.data
y = wine.target

# Train = 70%
# Test = 30%
# on stratify = y
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# standardize the feature using standard scaler
# TODO check this part again
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train 3 models of KNeighborsClassifier
#   k=5
#   k=1
#   k=15

k_values = [1, 5, 15]
for k in k_values:
    model = KNeighborsClassifier(n_neighbors=k)
    model.fit(X_train_scaled, y_train)
    y_pred = model.predict(X_test_scaled)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"K = {k}  --> Accuracy = {accuracy:.4f}")

"""
Which one is overfitting, underfitting or good fit
k=1 is more prone to overfitting
    The model classifies a sample using only its single nearest neighbor.
    It is very sensitive to noise and outliers.
    It learns the training data too closely, leading to overfitting.
k=15 is more prone to underfitting
    The model considers many neighbors.
    The decision boundaries become smoother.
    Fine details in the data are ignored, which can lead to underfitting.
k=5 is the best fit
    It balances bias and variance.
    It is less sensitive to noise than K=1.
    It preserves more local structure than K=15.
"""
"""
KNN classifies samples based on distance between feature vectors.
 If features have different scales,
variables with larger numeric ranges dominate the distance calculation,
causing smaller-scale features to have little influence. 
StandardScaler transforms all features to a comparable scale (zero mean and unit variance), 
ensuring each feature contributes fairly to the distance computation.
"""
