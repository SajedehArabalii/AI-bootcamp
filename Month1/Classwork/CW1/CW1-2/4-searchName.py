# Searching for a name in a list
names = ["Ali","Reza","Maryam","Zaynab"]
name = input("Enter a name: ")
if name in names:
    print("Name exists.")
else:
    print("Name does not exist.")