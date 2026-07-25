import numpy as np

"""
Part1
"""
array_size = 12350
features_size = 5
data_set = np.random.randn(array_size, features_size)

training_set_size = int(array_size * 0.8)
validation_set_size = int(array_size * 0.1)

training_set = data_set[:training_set_size]
validation_set = data_set[
    training_set_size : training_set_size + validation_set_size
]
testing_set = data_set[training_set_size+validation_set_size:]

print(f"Training set shape: {training_set.shape}") 
print(f"Validation set shape: {validation_set.shape}")
print(f"Testing set shape: {testing_set.shape}")   

if len(training_set)+ len(testing_set) + len(validation_set) == array_size:
    print("Correct")

else: 
    print("incorrect")


"""
Part2
"""

ground_truth = np.array([ 
    "Normal", 
    "Urgent", 
    "Normal", 
    "Spam", 
    "Urgent", 
    "Normal", 
    "Spam", 
    "Normal" 
])
 
predictions = np.array([ 
    "Normal", 
    "Normal", 
    "Normal", 
    "Spam", 
    "Urgent", 
    "Spam", 
    "Spam", 
    "Normal" 
])
print(ground_truth)
print(predictions)
correct_mask = ground_truth == predictions
print(correct_mask)

correct = np.where(correct_mask == True)[0]
incorrect = np.where(correct_mask == False)[0]

print(f"Correct predictions: {len(correct)}")
print(f"Incorrect predictions: {len(incorrect)}")

"""
Part3
"""
Accuracy = len(correct) / len(ground_truth)
Error_Rate = len(incorrect) / len(ground_truth)
print(f"Accuracy: {int(Accuracy*100)}%")
print(f"Error rate: {int(Error_Rate*100)}%")

print(f"Accuracy + Error Rate = {Accuracy+Error_Rate}")

"""
Part4
"""
y_true = np.array(["Normal"]*950 + ["Urgent"]*50)
np.random.shuffle(y_true)
y_pred = np.array(["Normal"]*1000)

Accuracy = len(np.where(y_true == y_pred)[0]) / len(y_true)
Error_Rate = 1 - Accuracy
FN = np.sum((y_true == "Urgent") & (y_pred == "Normal"))
print(f"Accuracy = {Accuracy}")
print(f"Error rate = {Error_Rate}")
print(f"False negative = {FN}")

"""
Part5
"""
patient_id = np.array([1, 2, 3, 4, 5]) 
ground_truth = np.array([ 
    "Healthy", 
    "Malignant", 
    "Healthy", 
    "Healthy", 
    "Malignant" 
]) 
predictions = np.array([ 
    "Healthy", 
    "Malignant", 
    "Malignant", 
    "Healthy", 
    "Healthy" 
])

Each_patient = np.where(ground_truth == predictions)[0]
print(f"If True for each patient: {Each_patient}")

Accuracy = np.sum(Each_patient==True) / len(ground_truth)
Error_Rate = 1-Accuracy
# FP = np.sum((ground_truth == "Healthy") & (predictions == "Malignant"))
FP = patient_id[
    (ground_truth=="Healthy")& (predictions=="Malignant")
]
FN = patient_id[(ground_truth=="Malignant")& (predictions=="Healthy")]

print(f"Accuracy: {int(Accuracy*100)}%")
print(f"Error Rate: {int(Error_Rate*100)}%")
print(f"{len(FP)} False positive patients with ids {FP}")
print(f"{len(FN)} False negative patients with ids {FN}")

"""
Part6
"""
email_id = np.array([1, 2, 3, 4, 5]) 
ground_truth = np.array([ 
    "Not Spam", 
    "Spam", 
    "Not Spam", 
    "Not Spam", 
    "Spam" 
]) 
predictions = np.array([ 
    "Not Spam", 
    "Spam", 
    "Spam", 
    "Not Spam", 
    "Not Spam" 
])
Truth = predictions == ground_truth
print(Truth)
Accuracy = np.sum(Truth == True) / len(predictions)
Error_Rate = 1-Accuracy
FP = email_id[
    (ground_truth == "Not Spam")&(predictions == "Spam")
]
FN = email_id[
    (ground_truth=="Spam")& (predictions=="Not Spam")
]


print(f"Accuracy: {int(Accuracy*100)}%")
print(f"Error Rate: {int(Error_Rate*100)}%")
print(f"{len(FP)} False positive emails with ids {FP}")
print(f"{len(FN)} False negative emails with ids {FN}")

"""
Part7
"""
study_hours = np.array([1, 2, 3, 5, 7, 8]) 
gaming_hours = np.array([6, 5, 4, 3, 2, 1])
actual_scores = np.array([35, 40, 50, 68, 82, 90])

predicted_score = (study_hours* 8) + (gaming_hours*-3) + 45
predicted_score = np.clip(predicted_score,0,100)
print(predicted_score)

error = predicted_score - actual_scores
absError = np.abs(error)
MAE = np.mean(np.abs(error))

print(error)
print(absError)
print(MAE)

"""
Part8
"""
candidate_weight1 = np.array([2, 4, 6, 8, 10, 12])
weight2 = -3
bias = 45

predictions = (
    study_hours[:, None] * candidate_weight1
    + gaming_hours[:, None] * weight2
    + bias
)

predictions = np.clip(predictions, 0, 100)
# print(predictions.shape)
MAE = np.mean(np.abs(predictions - actual_scores[:, None]), axis=0)
least_MAE = np.argmin(MAE)

print(MAE)
print(MAE[least_MAE], "_", candidate_weight1[least_MAE])


"""
Part8 
"""
emails = np.array([
    "URGENT reset my password now!!!", 
    "hello I have a question about my invoice", 
    "refund refund refund this is unacceptable!!!", 
    "please cancel my subscription", 
    "thank you for your help", 
    "URGENT billing error please help!!!" 
]) 

labels = np.array([ 
    "Urgent", 
    "Normal", 
    "Urgent", 
    "Normal", 
    "Normal", 
    "Urgent" 
])

feature_names = np.array([
    "urgent_exist",
    "refund_exist",
    "!_count",
    "word_count",
])


#TODO come back to this
urgent_exist = np.char.find(np.char.lower(emails), "urgent") >= 0
refund_exist = np.char.find(np.char.lower(emails), "refund") >= 0
exclamation_count = np.char.count(emails, "!")
word_count = np.array([len(email.split())for email in emails])

print(f"Urgent: {urgent_exist}")
print(f"Refund: {refund_exist}")
print(f"! count: {exclamation_count}")
print(f"word count: {word_count}")

# or could have used column stack and omited the axis=1
X_email = np.stack(
    [urgent_exist, refund_exist, exclamation_count, word_count],
    axis=1
)
print(X_email.shape)

"""
Part10
"""
email_id = np.array([1,2,3,4,5,6])
urgent = email_id[
    (X_email[:, 0] == 1) |
    (X_email[:, 1] == 1) |
    (X_email[:, 2] >= 3)
]
normal = email_id[
    ~((X_email[:, 0] == 1) |
    (X_email[:, 1] == 1) |
    (X_email[:, 2] >= 3))]
print(f"Urgent emails = {urgent}")
print(f"Normal emails = {normal}")

email_predictions = np.where(np.isin(email_id,urgent), "Urgent", "Normal")
print(email_predictions)

prediction_accuracy = np.sum(email_predictions == labels)
Accuracy =  prediction_accuracy/ len(labels)
Error_Rate = 1-Accuracy

# print(f"Accuracy: {int(Accuracy*100)}%")
print(f"Accuracy: {Accuracy*100}")
print(f"Error Rate: {Error_Rate}")


"""
Part11
"""
X = np.array([1, 2, 3, 4, 5]) 
Y = np.array([3, 6, 9, 12, 15]) 

candidate_w = np.array([1, 2, 2.5, 3, 3.5, 4])

# prediction for each candidate
prediction = X[:,None] * candidate_w
print(prediction)

Accuracy = np.sum(np.where(prediction == Y[:,None])) / len(X)
Error_Rate = 1 - Accuracy

MSE = np.mean((prediction - Y[:,None])**2, axis=0)
print(f"MSE: {MSE}")

best_i = np.argmin(MSE)
best_w = candidate_w[MSE]
print(f"Best weight: {best_w}")

"""
Part12
"""