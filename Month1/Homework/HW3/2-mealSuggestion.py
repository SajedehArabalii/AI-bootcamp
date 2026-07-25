import numpy as np

"""
columns:
    0 => cooking time
    1 => calory
    2 => Hotness (1 to 10)
    3 => amount of ingredients
"""
recipes = np.array([ 
    [15, 350, 2, 5], 
    [45, 600, 7, 10], 
    [10, 200, 0, 3], 
    [30, 450, 5, 7], 
    [60, 800, 8, 12] 
]) 
recipe_names = ["Salad", "Curry", "Toast", "Pasta", "Stew"] 

users = np.array([ 
    [10, 250, 1, 4], 
    [50, 700, 8, 11], 
    [25, 400, 4, 6] 
]) 

"""
Min max Scaling
"""
min_vals = recipes.min(axis=0)
max_vals = recipes.max(axis=0)

recipes_scaled = (recipes - min_vals) / (max_vals - min_vals)

# print(f"Min values: {min_vals}")
# print(f"Max values: {max_vals}")
# print("Scaled recipes:\n", recipes_scaled)

"""
Scaling users the same way
"""
users_scaled = (users - min_vals)/(max_vals - min_vals)
# print(f"Scaledd users:\n{users_scaled}")
# print("----------------------------------")
# print(users_scaled.shape)
# print(recipes_scaled.shape)
# print("----------------------------------")

"""
Distance between users and recipes
"""
distances = np.sqrt(np.sum((users_scaled.reshape(3,1,4)-recipes_scaled.reshape(1,5,4))**2, axis= 2))
# print(f"Distance matrix:\n{distances}")

"""
Finding the nearest recipe
"""
nearest_i = np.argmin(distances, axis=1)

for i in range(len(users)):
    print(f"user {i+1}'s nearest recipe in {recipe_names[nearest_i[i]]}")

"""
Ranking recipes from nearest the farthest
"""
for i in range(len(users)):
    ranked_i = np.argsort(distances[i])
    ranked_recipes = [recipe_names[j] for j in ranked_i]
    print(f"User {i+1} ranking: {ranked_recipes}")