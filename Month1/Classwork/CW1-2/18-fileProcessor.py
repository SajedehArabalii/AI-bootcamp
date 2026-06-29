# Read file and show name and age using strip and split
# with open("file.txt","r") as file:
#     for line in file:
#         name,age = line.strip().split("-")
#         print()
#         print(f"Name = {name}")
#         print(f"Age = {age}")

#better version
with open("file.txt") as file:
    for line in file:
        parts = line.strip().split("-")
        if len(parts) == 2:
            name, age = parts
            name = name.strip()
            age = age.strip()
            print(f"{name} - {age}")

