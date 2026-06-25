#How to sort a dictionary
students = []
with open("students.csv") as file:
    for line in file:
        name, group = line.rstrip().split(",")

        # # A dictionary to put all the names and lists in and then print
        # student = {}
        # student["name"] = name
        # student["group"] = group
        # students.append(student)
        student = {"name": name, "group":group}
        students.append(student)

#Was replaced by the lambda function
# def get_name(student):
#     return student["name"]

#Would have been called in key=get_name
#lambda input: output
for student in sorted(students, key= lambda student:student["name"]):
    # We use single quotes because we are already using double quotes
    print(f"{student['name']} is in group {student['group']}")