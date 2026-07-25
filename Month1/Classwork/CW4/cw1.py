import numpy as np
import pandas as pd

# study_hours, attendance_percent, previous_score, final_score
students = np.array([
[2, 60, 45, 50],
[5, 80, 70, 75],
[1, 40, 35, 38],
[8, 90, 88, 92],
[4, 75, 60, 65],
[7, 85, 80, 84],
[3, 55, 50, 52],
[6, 70, 72, 78]
]) 

"""
Part one
"""
print(f"Students matrix dimension: {students.ndim}")
print(f"Students matrix shape: {students.shape}")
print(f"Students size size: {students.size}")
print(f"Students matrix data type: {students.dtype}")

X = students[:,:-1]
Y = students[:,-1]

print(f"Shape of features: {X.shape}")
print(f"Shape of label: {Y.shape}")

"""
Part 2 and Part 4
"""
rule_based_label = np.where(Y>60,"pass","fail")
print(rule_based_label)

passed = len(np.where(rule_based_label == "pass")[0])
print(f"Passed: {passed}")
failed = len(np.where(rule_based_label == "fail")[0])
print(f"Failed: {failed}")

# And part 4
percentage = passed / (passed + failed) *100
print(f"Percentage of success: {percentage:.0f}%")

"""
Part 3 
"""
ave_studyhour = np.mean(X[:,0]) 
print(f"Average of study hour: {ave_studyhour:.1f}")

max_attendance = np.max(X[:,1])
print(f"Max of attendance percentage: {max_attendance:.1f}")

min_attendance = np.min(X[:,1])
print(f"Min of attendance percentage: {min_attendance:.1f}")

effort_score = X[:,0] * X[:,1] / 100
print(f"Effort score {effort_score}")

#TODO Learn more about this
X_new = np.concatenate((X, effort_score.reshape(-1, 1)), axis=1)
print(f"New X: {X_new}")
print(f"Shape of new X: {X_new.shape}")

"""
Part 5
"""
level_label = np.where(Y < 60 , "Weak", 
                   np.where(Y < 80, "Normal", "Strong"))

weak = np.where(level_label =="Weak")
normal = np.where(level_label == "Normal")
strong = np.where(level_label == "Strong")

mean_weak = np.mean(students[weak,0])
mean_normal = np.mean(students[normal,0])
mean_strong = np.mean(students[strong,0])

print(f"weak students average study hour {mean_weak}")
print(f"normal students average study hour {mean_normal}")
print(f"strong students average study hour {mean_strong}")

"""
Part 6
"""
mins = X.min(axis=0)
maxs = X.max(axis=0)
means = X.mean(axis=0)
stds = X.k(axis=0)

X_scaled = (X - mins) / (maxs - mins)
# print(X_scaled)
# print("min of X_scaled", np.min(X_scaled))
# print("max of X_scaled", np.max(X_scaled))

"""
Part7
"""
new_student = np.array([5, 75, 68])
student_scaled = (new_student - mins) / (maxs - mins)
# print(scaling)
# TODO I forgot to put axis, not putting axis gives you a completely different output
distance = np.sqrt(np.sum((student_scaled - X_scaled)**2,axis=1))
distance2 = np.linalg.norm(X_scaled - student_scaled, axis=1)
print(distance)
print(distance2)

closest = np.argmin(distance)
print(students[closest,:])

"""
Part8
"""
new_students = np.array([ 
    [2, 50, 40], 
    [6, 82, 78], 
    [4, 65, 58], 
    [8, 88, 85] 
])
new_students_scaled = (new_students - mins) / (maxs - mins)
# print(new_students_scaled)
# TODO come back to this
distances = np.linalg.norm(
    # new_students_scaled[:, np.newaxis, :] - X_scaled[np.newaxis, :, :],
    # axis=2
    new_students_scaled[:, None] - X_scaled,
    axis=2
)

nearest = np.argmin(distances, axis=1)
print(f"Student 1 predicted label: {X[0]}")
for i in range(len(new_students)):
    print(f"New student {i+1} nearest student: {rule_based_label[nearest[i]]}")

"""
Part9 
"""
predicted_labels = rule_based_label[nearest]
ture_labels = np.array(["fail", "pass", "pass", "pass"])

print("Predicted labels:", predicted_labels)
print("Actual labels:   ", ture_labels)

accuracy = np.mean(predicted_labels == ture_labels)
print(f"Accuracy: {accuracy:.2%}")

"""
Part10
"""
actual_scores = np.array([50, 75, 38, 92, 65]) 
predicted_scores = np.array([55, 70, 45, 88, 60])

error = predicted_scores - actual_scores
print(f"Error: {error}")

absolute_error_i = np.abs(predicted_scores - actual_scores)
print(f"Absolute error: {absolute_error_i}")

MAE = np.mean(np.abs(error))
print(f"MAE = {MAE}")

#TODO part 11 tp 13


