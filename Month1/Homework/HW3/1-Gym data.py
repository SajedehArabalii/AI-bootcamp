import numpy as np
gym_data = np.array([ 
    [28, 75, 175, 4], 
    [34, 68, 168, 3], 
    [45, 82, 180, 2], 
    [22, 58, 162, 5], 
    [38, 90, 0, 1], 
    [29, 65, 170, 0] 
]) 
member_names = np.array(["Ali", "Sara", "Reza", "Neda", "Hassan", 
"Maryam"]) 

"""
1. Handling Missing Data
Within the dataset, a value of 0 in the Weight, Height, or Weekly Sessions columns indicates a missing value.
Replace these zeros with a logical estimate
Note: Do not modify the Age column.
""" 

gym_data[4,2] = gym_data[gym_data[:, 2] != 0, 2].mean()
gym_data[5,3] = gym_data[gym_data[:, 3] != 0, 3].mean()
# print(gym_data)

"""
2. Array Slicing
Extract and create a new array containing only the Weight, Height, and Weekly Sessions columns (excluding Age).
"""

new_data = gym_data[:,1:]
# print(new_data)

"""
3. Calculating Fitness Scores
For each gym member, calculate a Fitness Score combining their Body Mass Index (BMI) and their weekly session frequency. Append this score as a new column to your sliced array.
"""

weight = new_data[:,0]
height = new_data[:,1]/100
sessions = new_data[:,2]

BMI = np.round(np.array(weight/height**2)).astype(int)
score = BMI + sessions

new_gym_data = np.c_[new_data,score]

# print(new_gym_data)

"""
4. Top Performer Identification
Find the member with the highest calculated Fitness Score.
Print their name along with their score.
"""

best_score = np.argmax(score)
print(f"Our member with the best score is {member_names[best_score]}, who got {score[best_score]} points.")


"""
5. Outlier Detection
Analyze the “Weekly Sessions” column to find the member who is the biggest outlier compared to the rest of the group.
Use standard deviation (𝜎) as your metric to quantify and detect this deviation.
"""

# Calculate Mean and Standard Deviation
mean_sessions = np.mean(sessions)
std_sessions = np.std(sessions)

# Calculate Z-scores (how many standard deviations each person is from the mean)
z_scores = np.abs(sessions - mean_sessions) / std_sessions

# Find the index of the highest Z-score
outlier_index = np.argmax(z_scores)

# Ouput the result
print(f"The biggest outlier is: {member_names[outlier_index]}")
print(f"Number of sessions: {sessions[outlier_index]}")
print(f"Z-score: {z_scores[outlier_index]:.2f}")

