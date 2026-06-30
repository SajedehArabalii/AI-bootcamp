# Corey Schafer
# Python tutorial for Begginers5: Dictionaries-Working with key-value Pairs

student = {"name":"John", "age": 25, "courses": ['math','compsci']}
print(student)
print(student['name'])
print(student['courses'])

student.update({'name': "Jane"})
# del student['age']
age = student.pop('age')
print(student)
print(age)
print(len(student))
print(student.keys())
print(student.values())
print(student.items())
