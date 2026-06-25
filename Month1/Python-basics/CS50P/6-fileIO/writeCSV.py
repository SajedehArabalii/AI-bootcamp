import csv

name = input("What is your name?: ")
home = input("Where is your home?: ")

#These are writer
# with open("address.csv","a", newline="") as file:
#     writer = csv.writer(file)
#     writer.writerow([name, home])

# Now for dictwriter
with open("address.csv","a", newline="") as file:
    # Necessary to point out the column they have to be written in
    # We should already have home,name written in csv
    writer = csv.DictWriter(file, fieldnames=["name","home"])
    writer.writerow({"name": name,"home":home})
