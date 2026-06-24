#How to make a dictionary
students = {
    "Ali" : "5",
    "Reza" : "2",
    "Maryam" : "3",
}


#Print all the student names
print("All student names and groups= ")
for student in students:
    print(student, students[student], sep=',')

print("----------------------")

#A list of dictionaries, more like a table with 3 columns
students = [
    {"name":"Ali", "group": "5", "gender": "male"},
    {"name":"Reza", "group": "2", "gender": "male"},
    {"name":"Maryam", "group": "3", "gender": "female"},
]

for student in students:
    print(student["name"],student["group"], student["gender"], sep=", ")
print("----------------------")


