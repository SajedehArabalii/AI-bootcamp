import numpy as np
"""
columns:
    0 => quiz
    1 => midterm
    2 => final
"""
scores = np.array([ 
    [18, 15, 20], 
    [12, 14, 16], 
    [20, 19, 18], 
    [10, 8, 15] 
])

scheme_A = np.array([0.5, 0.3, 0.2]) 
scheme_B = np.array([0.2, 0.3, 0.5]) 
scheme_C = np.array([0.1, 0.2, 0.7]) 

"""
Build weight_matrix
"""
weight_matrix = np.array([scheme_A,scheme_B,scheme_C])
# print(weight_matrix)

"""
Compute final_scores
"""
final_scores = scores @ weight_matrix.T
# print(final_scores)

"""
Find the best weighting scheme for each student
"""
best_scheme_indices = np.argmax(final_scores,axis = 1)
scheme_names = ["A","B","C"]
for i in range(len(scores)):
    print(f"Student {i+1}: best scheme is {scheme_names[best_scheme_indices[i]]}")

"""
Find the strongest subject for each student
"""
best_subject_indices = np.argmax(scores, axis=1)
for i in range(len(scores)):
    print(f"Student {i+1}: strongest subject index is {best_subject_indices[i]}")

"""
Add a new student and explain the new matrix
"""
#TODO: Should ask about this part of the question