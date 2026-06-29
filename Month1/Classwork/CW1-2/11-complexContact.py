# make a contact notebook
# give it the ability to add, search, show, exit
contacts = {}
while True:
    print("1, Add: ")
    print("2, Search: ")
    print("3, Show: ")
    print("4, Exit: ")

    choice = input("Choose.")
    if choice == "1":
        name = input("Enter name: ")
        number = input("Enter number: ")
        contacts[name] = number

    elif choice == "2":
        name = input("Enter name: ")
        if name in contacts:
            print("phone number= ", contacts[name])
        else:
            print("not found")
    
    elif choice == "3":
        print("Contact list= ")
        for name, number in contacts.items():
            print(name, ":", number)
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid")
        