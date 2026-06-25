# How  to read the file so that even if the user changes the order of the columns your output works out fine
import csv

students = []

with open("studentsadd.csv") as file:
    #Returns dictionary one at a time
    reader = csv.DictReader(file)
    for row in reader:
        students.append({"name": row["Name"],"home": row["Home"]})# It assigns the columns itself

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} leaves in {student['home']}")