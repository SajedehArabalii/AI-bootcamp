students = []

with open("students.csv") as file:
    for line in file:
        # We can write name,group = line.rstrip().split(",")
        row = line.rstrip().split(",")
        print(f"{row[0]} is in group {row[1]}")
        students.append(f"{row[0]} is in group {row[1]}")
print("-------------------")

for student in sorted(students):
    print(student)