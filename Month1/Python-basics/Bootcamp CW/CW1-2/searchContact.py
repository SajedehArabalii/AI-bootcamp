contacts = {
    "Ali": "09120000000",
    "Sara": "09130000000",
    "Reza": "09140000000"
}

name = input("Enter a name: ")

if name in contacts:
    print("Name exists.")
else:
    print("It does not exist")