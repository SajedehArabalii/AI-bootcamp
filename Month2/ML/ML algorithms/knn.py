"""
To classify a new point x:
    1- Look at the k training points closest to x
    2- Count how many belong to each class
    3- Predict the majority class
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
np.random.seed(42)
plt.rcParams['figure.figsize'] = (10,5)

#TODO I still don't get stats.norm
# Regenerate the tav-hormone dataset
P_GIRL , P_BOY = 0.7, 0.3
girl_dist = stats.norm(4.0, 1.2)
boy_dist = stats.norm(7.0, 1.5)
"""
girl_dist.rvs generates 1400 random hormone values from the girls' normal distribution.
generate randome hormone values for boys
then join array of girl hormones and boy hormones

"""
n = 2000
n_girls = int(n * P_GIRL)
X = np.concatenate([girl_dist.rvs(n_girls), boy_dist.rvs(n - n_girls)]).reshape(-1,1)# (2000,1) instead of (2000,)
Y = np.array([0] * n_girls + [1] * (n - n_girls)) 

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

#random_state=0 => Before splitting, the data is shuffled randomly
#stratify keeps the same class proportions in both sets
X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size = 0.3, random_state = 0, stratify = Y
)

knn = KNeighborsClassifier(n_neighbors=15)
# knn.fit(...) is the step where the KNN model learns from the training data.
knn.fit(X_train, Y_train)
"""
The score() method:

    Uses the trained model to predict the labels for X_test.
    Compares those predictions to the true labels in y_test.
    Returns the accuracy.
"""
print(f"Test accuracy: {knn.score(X_test, Y_test):.3f}")
print((knn.predict(X_test) == Y_test).mean())

from sklearn.datasets import make_blobs
from matplotlib.colors import ListedColormap

"""
make_blobs is a function from sklearn.datasets that generates clusters of data points.


n_samples=[700, 300]

    This specifies how many points to generate for each cluster.

        First cluster: 700 points
        Second cluster: 300 points

centers=[[4, 4], [7, 6]]

    These are the centers (means) of the two clusters.

cluster_std=[1.2, 1.5]

    This controls how spread out each cluster is.

        First cluster has standard deviation 1.2
        Second cluster has standard deviation 1.5

    Larger standard deviation means the points are more dispersed

random_state=42

    Fixes the random seed so that the same dataset is generated every time you run the code.
"""
X2, Y2 = make_blobs(n_samples = [700, 300],
                    centers= [[4, 4], [7, 6]],
                    cluster_std = [1.2, 1.5],
                    random_state = 42)


"""
y2 == 0: Creates a Boolean mask selecting all samples labeled girl.
X2[y2 == 0, 0]: Takes the first feature (x-coordinate) of all girls.
X2[y2 == 0, 1]: Takes the second feature (y-coordinate) of all girls.
plt.scatter(x, y): Plots those points on a scatter plot.
c="tab:pink": Colors the points pink.
s=15: Sets the marker size.
label="girl": Adds "girl" to the plot legend.
"""
plt.scatter( X2[Y2 == 0, 0], X2[Y2 == 0, 1], c='tab:pink', s=15, label='girl')

plt.scatter( X2[Y2 == 1, 0], X2[Y2 == 1, 1], c='tab:blue', s=15, label='boy')

plt.xlabel("tav-hormone")
plt.ylabel("second hormone")
plt.legend()
plt.title("Two-feature dataset")
plt.show()

def plot_decision_boundary(model, X, Y, title):
    """
    X[:, 0]: First feature (x-axis).
    X[:, 1]: Second feature (y-axis).
    .min() - 1 / .max() + 1: Extend the grid slightly beyond the data.
    np.linspace(start, end, 300): Generate 300 evenly spaced values.
    np.meshgrid(...): Combine the x-values and y-values into a 2D grid

    Result
        xx and yy are both 300 × 300 arrays.    
    """
    xx, yy =np.meshgrid(
        np.linspace(X[:,0].min()-1, X[:,0].max()+1,300),
        np.linspace(X[:,1].min()-1, X[:,1].max()+1, 300))
    """
    xx.ravel(): Flattens the xx grid into a 1D array.
    yy.ravel(): Flattens the yy grid into a 1D array.
    np.c_[...]: Combines them into (x, y) coordinate pairs.
    model.predict(...): Predicts the class for every grid point.
    .reshape(xx.shape): Reshapes the predictions back into the original grid shape
    """
    Z = model.predict(np.c_[xx.ravel(), yy.ravel()]).reshape(xx.shape)
    """
    contourf(): Fills regions with colors based on the predicted class.
    alpha=0.3: Makes the colors 30% opaque (semi-transparent).
    ListedColormap(["pink", "lightblue"]): Uses pink for one class and light blue for the other.
    """
    plt.contourf(xx, yy, Z, alpha = 0.3, cmap = ListedColormap(['pink', 'lightblue']))
    plt.scatter(X[Y == 0, 0], X[Y == 0, 1], c='deeppink', s = 10)
    plt.scatter(X[Y == 1, 0], X[Y == 1, 1], c='navy', s = 10)
    plt.title(title)
    plt.show()

X2_train, X2_test, Y2_train, Y2_test = train_test_split(
    X2, Y2, test_size=0.3, random_state=0
)
knn2 = KNeighborsClassifier(n_neighbors=5).fit(X2_train,Y2_train)
plot_decision_boundary(knn2, X2_train, Y2_train, 'KNN decision regions (k=15)')

train_acc = (knn2.predict(X2_train) == Y2_train).mean()
test_acc = (knn2.predict(X2_test) == Y2_test).mean()
print(train_acc)
print(test_acc)


for k in [1, 15, 200]:
    m = KNeighborsClassifier(n_neighbors=k).fit(X2_train, Y2_train)
    plot_decision_boundary(m, X2_train, Y2_train, f"k = {k}")
    train_acc = m.score(X2_train, Y2_train)
    test_acc = m.score(X2_test, Y2_test)

    print(f"k = {k}")
    print(f"Train Accuracy: {train_acc:.3f}")
    print(f"Test Accuracy : {test_acc:.3f}")
    print("----------------")






