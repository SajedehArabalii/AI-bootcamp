# Reads names.txt line by line
with open("names.txt", "r") as file:
    for line in file:
        print(line.strip())