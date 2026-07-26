# A music player app
"""
0- tempo
1- energy
2- groove
"""

import numpy as np

song = np.array([0.7, 0.9, 0.6]) 
user_taste = np.array([0.6, 0.8, 0.5]) 

"""
Part1
"""
element_mul = song * user_taste
print(element_mul)

dot_mul = song @ user_taste
print(f"{dot_mul:.2f}")

w = np.array([0.6, 0.8, 0.5]) 
b = 0.3 

y = w @ element_mul + b
print(y)


song1 = np.array([0.9, 0.1]) 
song2 = np.array([0.85, 0.15]) 
song3 = np.array([-0.9, -0.1])

songs = [song1, song2, song3]

for i in range(len(songs)):
    for j in range(i + 1, len(songs)):
        dot_product = np.dot(songs[i],songs[j])
        normA = np.linalg.norm(songs[i])
        normB = np.linalg.norm(songs[j])
        sim = dot_product / (normA * normB)
        if sim > 0 :
            pos = "Similar"
        else :
            pos = "Not similar"
        print(f"Song {i+1} vs Song {j+1}: {pos}")

#TODO Come back to this part
songs = np.vstack(songs)
# print(songs)

# Gets the dot product of all of them
dot_product = songs @ songs.T
# print(dot_product)

# norms = distance, length
norms = np.linalg.norm(songs, axis=1)
# print(norms)

cosine = dot_product / np.outer(norms, norms)
# print(cosine)
recommend = np.where(cosine > 0, "Similar", "Different")

print(recommend)


"""
Part2
"""
# A mobile game has 4 characters and 3 features
"""
0- Power
1- Speed
2- Defence
"""
stats = np.random.rand(4, 3) 

skill_matrix = np.random.rand(3, 5) 
print(stats @ skill_matrix)

X_chars = np.array([ 
    [80, 40, 60], 
    [30, 90, 50], 
    [70, 70, 70], 
    [95, 20, 40] 
]) 
W_skills = np.random.randn(3, 3) 
b_skills = np.array([1.0, -0.5, 0.2])
Z = X_chars @ W_skills + b_skills 
print(Z)

W_wrong = np.random.randn(5, 3) 
print(X_chars @ W_wrong.T )

"""
Part3
"""
questions = np.array(['Q1','Q2','Q3','Q4','Q5']) 
answers   = np.array(['B','D','A','C','B'])

i = np.random.permutation(len(questions))
testQ = questions[i]
testA = answers[i]
# print(i)
print(testQ)
print(testA)

new_questions = np.array(['Q6', 'Q7']) 
new_answers   = np.array(['A', 'D']) 

questions = np.hstack([questions, new_questions])
answers = np.hstack([answers,new_answers])
difficulty = np.array([1,2,1,3,2,2,3]) 

Q = np.hstack([questions[:,None], answers[:,None] , difficulty[:,None]])

# print(questions)
# print(answers)
print(Q)

"""
Part4
"""

# camera_frames = np.random.randn(54)
# camera_frames = camera_frames.reshape(6,9)
camera_frames = np.random.randn(54).reshape(6,9)
camera_frames = np.random.randn(54).reshape(6,-1)

print(camera_frames.shape)

log = np.random.randn(6,4)
dashboard = log.T
print(log.shape)
print(dashboard.shape)

weekly_data = np.arange(84).reshape(7,4,3)

"""
Part 5
"""
confidence = np.array([0.9, 0.4, 0.7, 0.95, 0.3])
confidence = confidence[:,None]
print(confidence)

single_command_output = np.array([[[0.1, 0.7, 0.2]]])  # shape: (1, 1, 3)
# Removes the first dimension, axis=1 will remove the second dimension and no axis removes all the 1s
single_command_output = np.squeeze(single_command_output, axis = 0)
print(single_command_output.shape) 

"""
Part6
"""
power_readings = np.array([2.1, -0.5, 3.4, -1.1, 0, 5.6]) 
power_readings = np.maximum(power_readings, 0 )
print(power_readings)

raw_output = np.array([[-0.4, 1.2, 0.0],
                      [2.1, -1.5, 0.3]] )
raw_output = np.where(raw_output < 0, 0, raw_output)

"""
Part7
"""

logits = np.array([ 
    [2.5, 0.3, 0.1], 
    [0.2, 0.1, 3.5], 
    [1.0, 1.2, 0.9] 
]) 
soft_max = np.exp(logits)/ np.sum(np.exp(logits),axis=1, keepdims = True)
# print(soft_max)
# print(np.sum(soft_max[0,:]))
genre = np.argmax(soft_max,axis=1)
sure = np.max(soft_max, axis=1)
print(f"genre: {genre}, sure: {sure}")

"""
Part8
"""
cart_prices = np.array([120, 45, 300, 15, 80])
discount_items = cart_prices[:2].copy()
discount_items[0] = 0 
print(cart_prices)

"""
Part9
"""
songs = np.random.randn(8,4)
# print(songs)
songs = np.random.permutation(songs)
# print(songs)
# check_shuffle = songs == songs_n
# print(check_shuffle)

w1 = np.random.randn(4,5)
b1 = np.random.randn(5)

z = songs @ w1 + b
print(z.shape)
# t = z<0
# print(t)

z = np.maximum(z, 0)
# t = z<0
# print(t)


w2 = np.random.randn(5,3)
b2 = np.random.randn(3)

z = z @ w2 + b2
print(z.shape)

soft_max = np.exp(z)/ np.sum(np.exp(z), axis = 1, keepdims = True)
print(soft_max)

prediction = np.argmax(soft_max, axis = 1)
print()

print("Probabilities:")
print(soft_max)

print("\nPredicted moods:")
print(prediction)