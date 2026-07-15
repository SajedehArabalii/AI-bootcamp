# Save names in txt file
with open("names.txt","w") as file:
    for i in range(5):
        name = input("Enter name: ")
        file.write(f"{name}\n")