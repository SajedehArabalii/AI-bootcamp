# add => Gets name and grade of student
# saves it in a dictionary
# save => saves info in a file
# show => shows info
# search => gives grade based on student name
# exit

import json

def main():
    try:
        with open("student.json", "r") as file:
            student = json.load(file)
    except FileNotFoundError:
        student = {}
    while True:
        option = input("1-add\n2-save\n3-show\n4-search\n5-exit\nYour choice: ")
        match option:
            case "1":
                add(student)
            case "2":
                save(student)
            case "3":
                show(student)
            case "4":
                search(student)
            case "5":
                print("\tGoodbye!")
                break
            case _:
                print("\tInvalid")

def add(student):
    name = input("What is the student's name? ")

    while True:
        try:
            grade = int(input("What is the student's grade? "))
            if 0 <= grade <= 100:
                student[name] = grade
                break
            else:
                print("\tInvalid grade")
        except ValueError:
            print("\tGrade must be a number.")

def save(student):
    with open("student.json","w") as file:
        json.dump(student,file, indent=4)
    print("\tData was saved")

def show(student):
    if not student:
        print("\tNo students found.")
        return

    for name, grade in sorted(student.items()):
        print(f"\t{name}: {grade}")

def search(student):
    name = input("Which student are you looking for? ")
    if name in student:
        print(f"\t{name} = {student[name]}")
    else:
        print("\tNot found")

if __name__ == "__main__":
    main()