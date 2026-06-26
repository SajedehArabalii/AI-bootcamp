
# def main():
#     # name , city = get_student()
#     student =  get_student()
#     # print(f"{name} from {city}")
#     print(f"{student[0]} from {student[1]}")

#new main for new get_student
def main():
    student = get_student()
    print(f"{student['name']} from {student['city']}")

# def get_name():
#     return input("Name: ").strip()

# def get_city():
#     return input("City: ").strip()

# def get_student():
#     name =  input("Name: ").strip()
#     city = input("City: ").strip()
#     # This returns one value(tupple) with 2 values inside it(name , city)
#     #return name, city 
#     #Tupples are immutible. you cannot change the value of them
#     # This returns a list
#     return [name, city]

#another way of writing get_student() where we return dictionaries which are mutable
def get_student():
    student = {}
    student["name"] = input("Name: ")
    student["city"] = input("City: ")
    return student

if __name__ == "__main__":
    main()