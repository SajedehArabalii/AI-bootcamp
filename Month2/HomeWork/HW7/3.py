import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    f1_score,
    precision_score,
    recall_score,
)
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

gym_data = pd.DataFrame(
    {
        "visits_per_month": [
            6,5,0,4,15,12,18,4,17,6,6,0,11,18,8,0,16,12,16,14,17,13,3,19,13,15,15,4,0,16,18,15,0,11,4,0,0,5,17,15,17,10,0,6,5,10,14,4,13,19,6,7,17,4,5,17,3,7,0,12,19,12,1,14,13,9,11,6,8,19,12,8,10,17,14,5,12,7,2,4,14,12,9,16,11,9,3,10,4,16
        ],
        "avg_session_min": [
            51.1,40.8,15.4,74.2,42.2,44.3,26.8,54.0,66.4,56.7,25.1,18.6,66.3,73.9,48.1,13.9,40.4,27.1,49.5,51.0,42.2,51.2,13.4,43.6,54.7,49.9,74.3,47.5,11.3,25.4,51.7,47.2,12.6,32.4,54.5,11.0,13.1,28.6,33.4,45.6,38.9,64.9,24.3,58.1,42.0,72.3,66.1,53.3,64.1,25.1,68.6,52.4,49.4,63.6,63.1,62.6,17.9,71.0,13.2,50.1,59.8,48.8,22.6,27.8,49.8,30.3,51.6,56.8,33.3,54.3,31.1,52.9,35.4,65.0,37.1,47.1,73.8,59.7,12.0,59.5,72.2,52.2,62.6,51.2,37.1,46.4,16.8,39.4,37.3,42.7
        ],
        "days_since_last_visit": [
            8,10,21,1,10,11,8,1,14,3,7,41,1,6,14,20,8,7,12,14,2,14,23,12,7,4,10,5,46,4,11,4,58,11,10,26,49,4,14,5,13,5,43,13,10,7,1,5,2,13,14,11,1,12,3,7,27,3,25,9,1,5,27,11,8,4,9,0,9,5,12,10,5,1,4,2,12,10,55,10,8,14,13,8,3,11,34,12,6,8
        ],
        "has_personal_trainer": [
            1,1,0,1,1,0,1,1,1,1,1,0,1,0,1,0,1,1,0,1,1,1,1,1,1,1,0,1,0,1,0,0,0,0,0,1,0,1,0,1,0,0,0,0,0,1,0,1,0,1,1,1,1,1,0,1,0,1,0,1,1,1,1,1,1,0,1,0,1,1,1,1,1,1,1,0,1,0,1,0,1,1,0,1,1,0,1,1,0,0
        ],
        "churned": [
            0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1,0,0,1,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0
        ],
    }
)


print("Rows 1 to 5")
print(gym_data.head())
print("\nCount of samples of each class:")
print(gym_data["churned"].value_counts())
print("\nClass Proportion: ")
print(gym_data["churned"].value_counts(normalize=True))

X = gym_data.drop("churned", axis=1)
y = gym_data["churned"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)


scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

model = LogisticRegression()
model.fit(X_train_scaled, y_train)

y_pred = model.predict(X_test_scaled)

print("\n---  Evaluation Metrics ---")
print(f"Accuracy:  {accuracy_score(y_test, y_pred):.2f}")
print(f"Precision: {precision_score(y_test, y_pred, zero_division=0):.2f}")
print(f"Recall:    {recall_score(y_test, y_pred, zero_division=0):.2f}")
print(f"F1-score:  {f1_score(y_test, y_pred, zero_division=0):.2f}")

tn, fp, fn, tp = confusion_matrix(y_test, y_pred).ravel()
print(f"\nConfusion Matrix -> TP: {tp}, TN: {tn}, FP: {fp}, FN: {fn}")