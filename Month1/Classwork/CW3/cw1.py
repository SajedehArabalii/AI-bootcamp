import numpy as np
"""
Part1
"""
scores = [72, 85, 90, 66, 78]
grades = np.array([ 
 [18, 15, 12, 20],  # Student 1 
 [14, 17, 19, 16],  # Student 2 
 [20, 20, 18, 15]   # Student 3 
]) 

Student2= grades[1,:]
final_exam = grades[:,-1]
sub = grades[:2,:2]

print(Student2)
print(final_exam)
print(sub)

a = np.array([3, 6, 9])  
b = np.array([1, 2, 3])

sum = a+b
subtraction = a-b
mul = a*b
vmul = a * 0.5

print(sum)
print(subtraction)
print(mul)
print(vmul)

v = np.array([100, 0, -5])  
# X = np.random.randn(3,3)
X = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

sum = v + X
print(sum)

point_A = np.array([2, 3, 5]) 
point_B = np.array([7, 1, 9]) 

distance = np.linalg.norm(point_A - point_B)
print(distance)

M = np.array([ 
 [80, 70, 90], 
 [60, 85, 75], 
 [95, 60, 80], 
 [70, 70, 70] 
]) 
weights = np.array([0.5, 0.3, 0.2]) 

transpose = M.T
print(M.shape)
print(transpose.shape)

reshape = M.reshape(6,2)
reshape2 = M.reshape(2,6)

print(reshape.shape)
print(reshape2.shape)

score = M @ weights
score2 = np.sum(M * weights, axis = 1)

print(score)
print(score2)


"""
Paart2
"""
import csv

# with open("cities.csv","r") as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         print(row)


city_names = []
data = []

with open("cities.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        try:
            features = [
                float(row["avg_temp"]),
                float(row["humidity"]),
                float(row["popularity"]),
                float(row["cost_index"])
            ]
            city_names.append(row["city"])
            data.append(features)
        except ValueError:
            print(f"Warning skipped {row['city']}")

print(city_names)
print(data)

data= np.array(data)
print(data)
print(data.shape)#(7,4)
print(data.dtype)



mins = np.min(data, axis = 0)
maxs = np.max(data, axis = 0)
means = np.mean(data, axis = 0)

data_scaling = (data - mins) / (maxs - mins)


ideal = np.array([26, 40, 8, 4]) 
ideal_scaling = (ideal - mins) / (maxs - mins)
distances = np.linalg.norm(
    (data_scaling - ideal_scaling),
    axis = 1
)
print(distances)

nearest_city_i = np.argmin(distances)
print(f"nearest city: {city_names[nearest_city_i]}")
Dot_product = data_scaling @ ideal_scaling
normData = np.linalg.norm(data_scaling, axis = 1)
normIdeal = np.linalg.norm(ideal_scaling)
cosine_similarity = Dot_product / (normData * normIdeal)

print(cosine_similarity)
print(f"{max(cosine_similarity)}, {city_names[np.argmax(cosine_similarity)]}")


weights = np.array([0.1, 0.2, 0.3, 0.4])
data_weight = data_scaling * weights
ideal_weight = ideal_scaling * weights
print(data_weight.shape)
print(ideal_weight[:,None].shape)

distances = np.linalg.norm(
    (data_weight - ideal_weight),
    axis = 1
)

best = np.argmin(distances)
print(city_names[best])

#TODO I did not write the rest of it because I did not understand, 2D4


