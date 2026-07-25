import numpy as np

def main():
    """
    columns in order:
        0 => age
        1 => weight
        2 => height
        3 => sessions
    """
    gym_data = np.array([ 
        [28, 75, 175, 4], 
        [34, 68, 168, 3], 
        [45, 82, 180, 2], 
        [22, 58, 162, 5], 
        [38, 90, 0, 1], 
        [29, 65, 170, 0] 
    ], dtype = float) 
    member_names = np.array(["Ali", "Sara", "Reza", "Neda", "Hassan", 
"Maryam"]) 
    missing_data(gym_data)
    new_data = array_slicing(gym_data)
    score = fitness_score(new_data)
    new_data = np.c_[new_data,score]
    top_performer(score,member_names)
    outlier(new_data,member_names)

def missing_data(gym_data):
    """
    1. Handling Missing Data
    Within the dataset, a value of 0 in the Weight, Height, or Weekly Sessions columns indicates a missing value.
    Replace these zeros with a logical estimate
    Note: Do not modify the Age column.
    """ 
    # make missing data handling scalable for larger database
    # Creating a mask for zeros
    missing = 0
    for col in [1,2,3]:# columns 1 and 2 and 3
        col_data = gym_data[:,col]
        zero_mask = (col_data == 0)
        missing += np.sum(zero_mask)
        mean_val = col_data[col_data !=0].mean() #calculating means of nonzero values
        gym_data[col_data == 0, col] = mean_val # replace all zeros
        
    print(f"{missing} missing data detected and replaced.")

def array_slicing(gym_data):
    """
    2. Array Slicing
    Extract and create a new array containing only the Weight, Height, and Weekly Sessions columns (excluding Age).
    """

    return gym_data[:,1:]

def fitness_score(new_data):
    """
    3. Calculating Fitness Scores
    For each gym member, calculate a Fitness Score combining their Body Mass Index (BMI) and their weekly session frequency. Append this score as a new column to your sliced array.
    """
    weight = new_data[:,0]
    height = new_data[:,1]/100
    sessions = new_data[:,2]
    
    BMI = np.round(weight/height**2).astype(int)
    # The scoring system does not make sense
    #TODO: ask about scoring system
    return BMI + sessions

def top_performer(score, member_names):
    """
    4. Top Performer Identification
    Find the member with the highest calculated Fitness Score.
    Print their name along with their score.
    """

    best_score = np.argmax(score)
    print(f"Top performer: {member_names[best_score]} | score={score[best_score]:.2f}")

def outlier(new_data,member_names):
    """
    5. Outlier Detection
    Analyze the “Weekly Sessions” column to find the member who is the biggest outlier compared to the rest of the group.
    Use standard deviation (𝜎) as your metric to quantify and detect this deviation.
    """
    sessions = new_data[:,2]
    # Calculate Mean and Standard Deviation
    mean = np.mean(sessions)
    session_std = np.std(sessions, ddof= 1) # ddof=1 divides by (n - 1) instead of n

    if session_std == 0 :
        print("No outlier: all session counts are identical.")
        return

    # Calculate Z-scores (how many standard deviations each person is from the mean)
    z_scores = np.abs(sessions - mean) / session_stdstd

    # Find the index of the highest Z-score
    outlier_index = np.argmax(z_scores)

    # Ouput the result
    print(f"The biggest outlier is: {member_names[outlier_index]}")
    print(f"Number of sessions: {sessions[outlier_index]}")
    print(f"Z-score: {z_scores[outlier_index]:.2f}")


# avg_sessions = np.mean(sessions)
# shape = avg_sessions.shape
# print("shape is ", shape)
# difference = sessions - avg_sessions
# abs_difference = np.abs(difference)
# best_index = np.argmax(abs_difference)
# best_name = member_names[best_index]
# print(f"ozve {best_index} ke esmesh hast {best_name}")

if __name__ == "__main__":
    main()