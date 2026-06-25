contacts = {}
while True:
    name = input("Enter contact name: ")
    if name == "exit":
        break
    number = input("Enter contact number: ")
    contacts[name] = number
print("Contacts:", contacts)