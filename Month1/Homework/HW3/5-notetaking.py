import numpy as np

importance = np.array([3, 8, 1, 9, 4, 7]) 

"""
Reshape
"""
col1 = importance.reshape(6,1)
print(f"Reshape method 1: {col1.shape}")


col2 = importance[:,np.newaxis]
print(f"Reshape method 2: {col2.shape}")

col3 = importance.T
print(f"Reshape method 3: {col3.shape}")

"""
Extract 0.9 as a scalar from model_out
"""
model_out = np.array([[[0.9]]])
value1 = model_out[0, 0, 0]
print(f"Extraction method 1: {value1}")

value2 = model_out.item()
print(f"Extraction method 2: {value2}")

"""
Predict and explain print(notes)
"""
notes = np.array([5, 10, 15, 20, 25])
pinned = notes[1:3]
pinned[0] = 999
print(notes)
"""
    The slice notes[1:3] is a view, not a copy
    So changing pinned[0] also changes notes[1]
    If you want to avoid changing notes use .copy
    pinned = notes[1:3].copy()
"""
notes = np.array([5, 10, 15, 20, 25])
pinned = notes[1:3].copy()
pinned[0] = 999
print(notes)

"""
Make a subarray change affect the original array
"""
arr = np.array([1, 2, 3, 4, 5])
sub = arr[2:4]
sub[1] = 100
print(arr)



