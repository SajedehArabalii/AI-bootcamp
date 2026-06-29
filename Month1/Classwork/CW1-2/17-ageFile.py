# Gets name and age from user and saves in file
with open("ages.txt","w") as file:
    for _ in range(5):
        name = input("Name: ")
        age = input("Age: ")
        file.write(f"{name} - {age}\n")