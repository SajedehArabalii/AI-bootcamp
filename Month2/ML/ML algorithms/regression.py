import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
plt.rcParams['figure.figsize'] = (10 ,5)

# Synthetic data: hormone level vs pregnancy week
n = 100
# Creates n random numbers between 4 and 20
week = np.random.uniform(4, 20, n)
"""
1.5: Intercept (baseline hormone level).
0.4 * week: Hormone increases by 0.4 for each additional pregnancy week.
np.random.normal(0, 1.0, n): Adds random Gaussian noise (mean = 0, standard deviation = 1) to make the data more realistic
"""
hormone = 1.5 + 0.4 * week + np.random.normal(0, 1.0, n)

plt.scatter(week, hormone, s=20, alpha = 0.7)
plt.xlabel("pregnancy week")
plt.ylabel("tav-hormone level")
plt.title("Raw data")
plt.show()



"""
This computes the slope (w1) of the best-fit line using the closed-form formula for simple linear regression.

Breakdown
week - week.mean(): How far each week is from the average.
hormone - hormone.mean(): How far each hormone value is from the average.
np.sum((week - mean_x) * (hormone - mean_y)): Measures how strongly the two variables vary together (covariance numerator).
np.sum((week - mean_x)**2): Measures the spread of the weeks (variance numerator)."""
w1 = np.sum((week - week.mean()) * (hormone - hormone.mean())) / np.sum((week - week.mean())**2)

# BIAS?
w0 = hormone.mean() - w1 * week.mean()
print(f"Manual fit:  y = {w0:.3f} + {w1:.3f} * x")

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

X = week.reshape(-1, 1)
lr = LinearRegression().fit(X, hormone)
print(f"sklearn fit: y = {lr.intercept_:.3f} + {lr.coef_[0]:.3f} * x")

Y_pred = lr.predict(X)
print(f"MSE = {mean_squared_error(hormone, Y_pred):.3f}")
print(f"R²  = {r2_score(hormone, Y_pred):.3f}")

# def mean_squared_error_simple(Y_model, Y_real):
#     return((Y_model - Y_real)**2).mean()
# print(mean_squared_error_simple(hormone, Y_pred))


"""
xs: x-values for drawing a smooth line.
lr.predict(xs): Predicted y-values from the trained linear regression model.
'r-': Red solid line.
lw=2: Line width of 2.
label='fitted line': Label for the legend
"""
xs = np.linspace(4, 20, 100).reshape(-1, 1)
plt.scatter(week, hormone, s=20, alpha=0.6, label='data')
plt.plot(xs, lr.predict(xs), 'r-', lw=2, label='fitted line')

# Show residuals for a few points
"""
range(0, n, 10): Every 10th data point.
[week[i], week[i]]: Same x-value → draws a vertical line.
[hormone[i], y_pred[i]]: Starts at the actual value and ends at the predicted value.
'g-': Green solid line.
alpha=0.5: Semi-transparent.
"""
for i in range(0, n, 10):
    plt.plot([week[i], week[i]], [hormone[i], Y_pred[i]], 'g-', alpha=0.5)

plt.xlabel('pregnancy week')
plt.ylabel('tav-hormone level')
plt.legend()
plt.title("Linear regression minimizes squared residuals (green)")
plt.show()

z= np.linspace(-8, 8, 200)
sigmoid = 1 / (1 + np.exp(-z))

plt.plot(z, sigmoid)
# axhline(0.5): Draws a horizontal line at y = 0.5.
plt.axhline(0.5, ls=":", color='grey')
plt.xlabel("z")
plt.ylabel("σ(z)")
plt.title("The sigmoid function")
plt.show()


from scipy import stats
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# The same database as 1 and 2
P_GIRL, P_BOY = 0.7, 0.3
girl_dist, boy_dist = stats.norm(4.0, 1.2), stats.norm(7.0, 1.5)

n = 2000
n_girls = int(n * P_GIRL)
Xc = np.concatenate([girl_dist.rvs(n_girls), boy_dist.rvs(n - n_girls)]).reshape(-1, 1)
Yc = np.array([0] * n_girls + [1] * (n - n_girls))

X_train, X_test, Y_train, Y_test = train_test_split(Xc, Yc, test_size=0.3, random_state=0, stratify=Yc)

logreg = LogisticRegression().fit(X_train, Y_train)
"""
logreg.intercept_[0]: The learned intercept (bias) w0
logreg.coef_[0,0]: The learned coefficient (weight) w1
:.3f: Display each value with 3 decimal places.
"""
print(f"w0 = {logreg.intercept_[0]:.3f}, w1 = {logreg.coef_[0,0]:.3f}")
"""
-w_0 / w_1: Computes the decision boundary.
"""
print(f"Decision boundary at x = {-logreg.intercept_[0]/logreg.coef_[0,0]:.3f}")
print(f"Test accuracy: {logreg.score(X_test, Y_test):.3f}")

grid = np.linspace(0, 12, 500).reshape(-1, 1)
"""
logreg.predict_proba(grid): Predicts the probability of each class for every point in grid.
"""
proba = logreg.predict_proba(grid)[:,1]

num = P_BOY * boy_dist.pdf(grid.ravel())
true_post = num / (num + P_GIRL * girl_dist.pdf(grid.ravel()))

plt.plot(grid, true_post, "k-", lw=2, label="True P(boy | x)")
plt.plot(grid, proba, color="tab:green", lw=2, label="Logistic regression")
plt.axhline(0.5, ls=":", color="gray")
plt.scatter(Xc[Yc == 0], np.zeros(n_girls), c="deeppink", s=5, alpha=0.3)
plt.scatter(Xc[Yc == 1], np.ones(n - n_girls), c="navy", s=5, alpha=0.3)
plt.xlabel("tav-hormone level")
plt.ylabel("P(boy | x)")
plt.legend()
plt.title("Logistic regression estimates the posterior")
plt.show()



y_pred = logreg.predict(X_test)
print(confusion_matrix(Y_test, y_pred))
print(classification_report(Y_test, y_pred, target_names=["girl", "boy"]))
