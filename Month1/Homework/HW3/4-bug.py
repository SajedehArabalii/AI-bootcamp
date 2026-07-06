import numpy as np

"""
2 days, 8 measurements per day and 4 sensors per measurement
"""
weather_data = np.random.randn(2, 8, 4) * 5 + 20

"""
Pass the data for the second day to analyze_day, which expects a shape of(4,8)
"""
day2 = weather_data[1]
day2_fixed = day2.T

"""
Flatten weather_data
"""
flattened_data_reshape = weather_data.reshape(-1)
flattened_data_flatten = weather_data.flatten()

print(flattened_data_reshape.shape)

"""
Add day3
"""
day3 = np.random.randn(8,4)
# weather_data_updated = np.concatenate([weather_data,day3[np.newaxis,:,:]],axis=0)
# Instead of np.concatenate with newaxis:
weather_data_updated = np.vstack([weather_data, [day3]])

print(weather_data_updated.shape)


"""
Why transpose and flatten are different
"""
# Simple 2x2 example
matrix = np.array([[1, 2], 
                   [3, 4]])

print("Original Matrix:\n", matrix)

# Transpose swaps rows and columns
print("Transposed:\n", matrix.T)

# Flatten collapses everything into a single line
print("Flattened:\n", matrix.flatten())

"""
Transpose (.T): Maintains the dimensionality (it’s still a 2D matrix) but swaps the axes. The structure of the data is preserved, just rotated.

Flatten: Completely destroys the dimensionality (turns a matrix into a flat line). You lose the “rows and columns” structure entirely.

Flattening always returns a 1D array where elements are laid out sequentially in memory.

Transposing doesn’t actually move the data in memory; it just changes the “view” or the “strides” of the array.
"""

# assert weather_data_updated.shape == (3, 8, 4), "Shape should be (3, 8, 4)"
# assert flattened_data_reshape.shape == (64,), "Shape should be (64,)"
# print("All tasks completed successfully!")