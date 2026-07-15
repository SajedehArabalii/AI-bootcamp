import numpy as np

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

print("dtype: ", students.dtype)
print("size: ",students.size)
print("shape: ",students.shape)
print("ndim: ", students.ndim)

X = students[:,:3]
Y = students[:,-1]
print(X.shape, Y.shape)

rule_based_label = np.where( Y >= 60, "pass","fail")
print(rule_based_label)

sum_pass = np.sum(rule_based_label == "pass")
print(sum_pass)

sum_fail = np.sum(rule_based_label == "fail")
print(sum_fail)


