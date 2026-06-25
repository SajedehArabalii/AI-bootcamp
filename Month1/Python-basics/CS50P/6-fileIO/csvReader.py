import csv
# Using reader from csv prevent your table from becoming seperated if let's say an address has a , in it

students = []

with open("studentsadd.csv") as file:
    # Read a csv file for us
    reader = csv.reader(file)
    # We iterate over reader instead of file
    for row in reader:
        students.append({"name":row[0],"group":row[1]})

for student in sorted(students, key=lambda student:student["name"]):
    print(f"{student['name']} lives in  {student['group']}")