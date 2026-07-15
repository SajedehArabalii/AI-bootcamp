class Student:
    # Self gives access to current object that we just created
    def __init__(self, name, city,major):
    # Validation and functionalities of the class belongs in the class
        self.name = name
        self.city  = city
        self.major = major
        if not name:
            raise ValueError("Missing name")
        
        if city not in ["Sari", "Tehran"]:
            raise ValueError("Invalid city")
    
    def __str__(self):
        # return "a student" # output of print(student)
        return f"{self.name} from {self.city} : {self.major_emoji()}"
    
    def major_emoji(self):
        match self.major:
            case "art":
                return "🎨"
            case "science":
                return "👩‍🔬"
            case "computer":
                return "👩‍💻"
            case _:
                return "📚"

def main():
    student = get_student()
    # print(f"{student.name} from {student.city}")

    # To override the conditions inside class
    student.city ="Ghaemshahr"
    print(student)

def get_student():
    # Creating an object of class Student
    # student = Student()
    # Student.name = input("Name: ")
    # Student.city = input("City: ")

    # A less manual version
    while True:
        name = input("Name: ").strip().title()
        city = input("City: ").strip().capitalize()
        major = input("Major: ").strip().lower()
        #It needs the __init(self) function
        try:
            return Student(name, city, major)
        except ValueError as e:
            # Check what message was raised
            if str(e) == "Missing name":
                print("You entered no name. Please try again.")
            elif str(e) == "Invalid city":
                print("We only accept Sari or Tehran. Please try again.")

if __name__ == "__main__":
    main()