#print meow 3 times
i = 3
while i!=0:
    print("Meow")
    i-=1
print("----------------------")

#for i in [0,1,2]:
for _ in range(3):
    print("Meow")
print("----------------------")

#The end makes it so that at the end of the print there is not an extra new line
print("Meow\n" *3 , end="")
print("----------------------")

#How to get only positive value
while True:
    n = int(input("Enter a number: "))
    if n > 0:
        break
for _ in range(n):
    print("Meow")
print("----------------------")

#List of students
students = ["Ali", "Reza", "Maryam"]

for student in students:
    print(student)
print("----------------------")

for i in range(len(students)):
    print(i+1,students[i])
print("----------------------")

