class Student:
    ...

def main():
    student = get_student()
    print(f"{student.name} from {student.city}")

def get_student():
    student = Student()
    Student.name = input("Name: ")
    Student.city = input("City: ")
    return student

if __name__ == "__main__":
    main()