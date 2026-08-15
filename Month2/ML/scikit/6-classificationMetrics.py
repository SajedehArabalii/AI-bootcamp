"""
Classification accuracy
"""
import pandas as pd
path = 'data/pima-indians-diabetes.data'
col_names = ['pregnant', 'glucose', 'bp', 'skin', 'insulin', 'bmi', 'pedigree', 'age', 'label']
pima = pd.read_csv(path, header = None, names= col_names)
print(pima.head())

"""
Can we predict the diabetes status of a patient given their health measurements
"""
feature_cols = ['pregnant', 'insulin', 'bmi', 'age']
X = pima[feature_cols]
y = pima.label

# split X and y into training and testing sets
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, random_state=0
)

# train a logistic regression model on the training set
from sklearn.linear_model import LogisticRegression
#The solver is the numerical algorithm that finds the best coefficients for your logistic regression model.
#liblinear is one of the solvers provided by scikit-learn.
logreg = LogisticRegression(solver='liblinear')
logreg.fit(X_train, y_train)

# make class predictions for the testing set
y_pred_class = logreg.predict(X_test)

# calculate accuracy
from sklearn import metrics
print(metrics.accuracy_score(y_test, y_pred_class))

# TERMINOLOGY: Null accuracy : accuracy that could be achhieved by always predicting the most frequent class

# examine the class distributiion of the testing set (using a pandas series method)
print("value count: ",y_test.value_counts())

# calculate the percentage of ones
print(y_test.mean())

# calculate the percentage of zeros
print( 1 - y_test.mean())

# calculate null accuracy ( for binary classification problems coded as 0/1)
print("null accuracy binary: ",max(y_test.mean(), 1-y_test.mean()))


# calculate null accuracy ( for multiclass classification problems)
# It gives you the baseline accuracy: how accurate a model would be if it always predicted the majority class.
#value_counts() sorts classes from most frequent → least frequent.
# head(1) = give me the majority class count.
print("Null accuracy multiclass: ",y_test.value_counts().head(1) / len(y_test))

# comparing the true and predicted response values
# print the first 25 true and predicted responses
#This compares the actual labels with your model's predicted labels for the first 25 test samples.
print('True: ', y_test.values[0:25])
print('Predicted: ', y_pred_class[0:25])


"""
Confusion metrics
"""
# IMPORTANT: first argument is true values, second argument is predicted values
print(metrics.confusion_matrix(y_test, y_pred_class))

# print the first 25 true and predicted responses
print('True: ', y_test.values[0:25])
print('predicted: ', y_pred_class[0:25])

# save confusion matrix and slice into four pieces
confusion = metrics.confusion_matrix(y_test, y_pred_class)
TP = confusion[1,1]
TN = confusion[0,0]
FP = confusion[0,1]
FN = confusion[1,0]

"""
Metrics computed from a confusion matrix
"""
Total = TP + TN + FP + FN
# Classification accuracy : overall how often is the classifier correct?
print((TP + TN) / (Total))
print(metrics.accuracy_score(y_test, y_pred_class))

# Classification error : overall how often is the classifier incorrect?
print((FP + FN) / (Total))
print(1 - metrics.accuracy_score(y_test, y_pred_class))

# Sensitivity : when the actual value is positive , how often is the prediction correct?
print(TP / (TP + FN))
print(metrics.recall_score(y_test, y_pred_class))

# Specificity : When the actual value is negative, how often is the prediction correct?
print(TN / (TN + FP))

# False positive rate : when the actual value is negative, how often is the prediction incorrect
print(FP / (TN + FP))

# Precision : when a positive value is predicted, how often is the prediction correct
print(TP / (TP + FP))
print(metrics.precision_score(y_test, y_pred_class))

"""
Adjusting the classification Threshold
"""
# print the first predicted responses
print(logreg.predict(X_test)[0:10])

# print the first 10 predicted probabilities of class membership
#Because predict_proba() returns a 2D array : (number of samples, number of classes)
print("All the probabilities: \n",logreg.predict_proba(X_test)[0:10,:])

# print the first 10 predicted probabilities for class 1
print("Probabilities of class 1: \n",logreg.predict_proba(X_test)[0:10, 1])

# store the predicted probabilities for class 1 
y_pred_prob = logreg.predict_proba(X_test)[:,1]


# histogram of predicted probabilities
#The histogram shows how your logistic regression's predicted probabilities of diabetes are distributed across the test patients.

# 0.08 → model thinks diabetes is unlikely
# 0.47 → model is uncertain
# 0.91 → model thinks diabetes is very likely

import matplotlib.pyplot as plt
plt.hist(y_pred_prob, bins=8)
plt.xlim(0,1)
plt.title('Histogram of predicted probabilities')
plt.xlabel('Predicted probability of diabetes')
plt.ylabel('Frequency')
# plt.show()

"""
Decrease the threshold for predicting diabetes in order to increase the sensitivity of the classifier
"""
# predict diabetes if the predicted probability is greater than 0.3
# binarize() converts numerical values into 0 or 1 based on a chosen threshold.
from sklearn.preprocessing import binarize
y_pred_class = binarize([y_pred_prob], threshold=0.3)[0]

# print the first 10 predicted probabilities
print(y_pred_prob[0:10])
# print the first 10 predicted probabilities with the lower threshold
print(y_pred_class[0:10])

# print the previous confusion matrix (threshold of 0.5)
print(confusion)

# print new confusion matrix (threshold of 0.3)
print(metrics.confusion_matrix(y_test, y_pred_class))

# IMPORTANT: senitivity has increased and specificity has decreased


"""
ROC curves and areas under the curve (AUC)
    how sensitivity and specificity are affected by various thresholds
    it can help you choose a threshold that balances sensitivity and specificity in a way that makes sense for your particular context
"""

# IMPORTANT: first argument is true values, second argument is predicted probabilities
# Calculates the ROC curve by testing many classification thresholds.

# fpr → False Positive Rate at each threshold
# tpr → True Positive Rate (Sensitivity/Recall) at each threshold
# thresholds → the thresholds used to calculate them
fpr, tpr, thresholds = metrics.roc_curve(y_test, y_pred_prob)
plt.plot(fpr, tpr)
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.0])
plt.title('ROC curve for diabetes classifier')
plt.xlabel('False Positive Rate (1 - Specificity)')
plt.ylabel('True Positive Rate (Sensitivity)')
plt.grid(True)
# plt.show()

# define a function that accepts a threshold and prints sensitivity and specificity

# thresholds = [0.9, 0.7, 0.5, 0.3, 0.1]
# threshold = 0.4
# thresholds > 0.4
# → [0.9, 0.7, 0.5]
# [-1] → 0.5
def evaluate_threshold(threshold):
    print('Sensitivity:', tpr[thresholds > threshold][-1])
    print('Specificity:', 1 - fpr[thresholds > threshold][-1])

evaluate_threshold(0.5)

"""
AUC : the percentage of the ROC plot that is underneath the curve
    -it is useful as a single number summary of classifier performance
    -If you randomly chose one positive and one negative observation, AUC represents the likelihood that your classifier will assign a higher predicted probability to the positive observation
    -AUC is useful even when there is high class imbalance (unlike classification accuracy).
"""
# IMPORTANT : first argument is true values second argument is predicted probabilities
print(metrics.roc_auc_score(y_test, y_pred_prob))

# Calculate cross validated AUC
from sklearn.model_selection import cross_val_score
print(cross_val_score(logreg, X, y, cv=10, scoring='roc_auc').mean())

"""

Confusion matrix advantages:
    Allows you to calculate a variety of metrics
    Useful for multi-class problems (more than two response classes)

ROC/AUC advantages:
    Does not require you to set a classification threshold
    Still useful when there is high class imbalance
"""







































































































































