
#------------------------------
# Q3_Logistic Regression
#------------------------------
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    log_loss
)
# Use file titanic.csv with features
#   Fare
#   Age
#   Sex
#   Pclass
#   survived = target

# keep only features Fare, Age, Sex and Pclass
df = pd.read_csv("titanic.csv")
X = df[[
    "Pclass",
    "Sex",
    "Age",
    "Fare"
]]
y = df["Survived"]

# fill Age with mean
# TODO filna
X["Age"] = X["Age"].fillna(
    X["Age"].mean()
)
# Turn sex into numerical feature
# TODO get_dummies 
X = pd.get_dummies(
    X,
    columns=["Sex"],
    drop_first=True
)


# using stratify = y, split data 70/30
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.30,
    random_state=42,
    stratify=y
)

# Scale using StandardScaler
scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(
    X_train
)

X_test_scaled = scaler.transform(
    X_test
)

# Train a LogisticRegression model
model = LogisticRegression()

model.fit(
    X_train_scaled,
    y_train
)
# Report the Accuracy
y_pred = model.predict(
    X_test_scaled
)
accuracy = accuracy_score(
    y_test,
    y_pred
)

print("Accuracy:", accuracy)

# Print the confusion Matrix
# TODO confusion matrix
cm = confusion_matrix(
    y_test,
    y_pred
)

print("\nConfusion Matrix")
print(cm)
"""
If FP > FN, the model more often mistakes non-survivors as survivors.
If FN > FP, the model more often mistakes survivors as non-survivors.
"""

# print _coef
print("\nFeature Coefficients")

for feature, coef in zip(
    X.columns,
    model.coef_[0]
):
    print(feature, ":", coef)
"""
The feature with the largest positive coefficient increases the probability of survival the most.
The feature with the most negative coefficient decreases the probability of survival the most.
"""

# TODO come back to this whole section till the end
# Using predit_proba for 1 true prediction and 1 false prediction clculate
#   cross_entropy_loss(p,y)  

probabilities = model.predict_proba(
    X_test_scaled
)
correct_index = None
wrong_index = None

for i in range(len(y_test)):

    if y_pred[i] == y_test.iloc[i] and correct_index is None:
        correct_index = i

    if y_pred[i] != y_test.iloc[i] and wrong_index is None:
        wrong_index = i

    if correct_index is not None and wrong_index is not None:
        break
correct_loss = log_loss(
    [y_test.iloc[correct_index]],
    [probabilities[correct_index]],
    labels=[0, 1]
)

wrong_loss = log_loss(
    [y_test.iloc[wrong_index]],
    [probabilities[wrong_index]],
    labels=[0, 1]
)

print("\nCorrect Prediction Loss:", correct_loss)
print("Wrong Prediction Loss:", wrong_loss)


"""
Cross-entropy measures how confidently the model predicts the correct class. 
A correct prediction with high confidence produces a small loss,
whereas an incorrect prediction—especially one made with high confidence—produces a much larger loss because the predicted probability for the true class is very low.
"""