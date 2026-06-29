# What grade did the student get?
grade = int(input("What is your grade?"))

if grade>=90 and grade<=100:
    print("A")
elif grade >=80 and grade<90:
    print("B")
elif grade >=70 and grade<80:
    print("C")
elif grade <70 and grade >=0:
    print("F")
else:
    print("Grade is not valid")