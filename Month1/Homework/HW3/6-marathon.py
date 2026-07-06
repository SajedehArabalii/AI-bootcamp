import numpy as np

# First group of runners
bib_numbers = np.array([101, 102, 103, 104, 105, 106]) 
times_5k = np.array([22.3, 25.1, 21.8, 26.4, 23.0, 24.7]) 

# Second group of runners
bib_numbers_2 = np.array([107, 108]) 
times_5k_2 = np.array([20.5, 27.9]) 

"""
Merge and keep the pairing integrity
"""
bib_numbers = np.concatenate([bib_numbers, bib_numbers_2])
times_5k = np.concatenate([times_5k, times_5k_2])

"""
Shuffle while keeping the pairs together
"""
indices = np.arange(len(bib_numbers))
np.random.shuffle(indices)

bib_numbers = bib_numbers[indices]
times_5k = times_5k[indices]

"""
Sort and rank: fastest to slowest
"""
sort_i = np.argsort(times_5k)
sorted_bibs = bib_numbers[sort_i]
sorted_times = times_5k[sort_i]

print("Rank | Bib | Time")
print("-----------------")
for i in range(len(sorted_bibs)):
    print(f"{i+1:4} | {sorted_bibs[i]:3} | {sorted_times[i]:.1f}")

"""
Find rank of Bib 104
"""
rank_i = np.where(sorted_bibs == 104)[0][0]
rank_104 = rank_i + 1
print(f"\nBib 104 is ranked: {rank_104}")