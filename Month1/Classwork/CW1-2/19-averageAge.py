#Reads file and calculates the average age
# total_sum=0
# counter = 0
# with open("ages.txt", "r") as file:
#     for line in file:
#         name,age = line.split("-")
#         total_sum += int(age.strip())
#         counter += 1

# average = total_sum/counter
# print(average)

# Better version
ages = []

with open("ages.txt") as file:
    for line in file:
        name, age = line.split("-")
        ages.append(int(age))

print(sum(ages) / len(ages))


