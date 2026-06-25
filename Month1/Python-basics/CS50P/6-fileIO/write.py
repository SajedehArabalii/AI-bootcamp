name = input("What is your name? ")

#w in open recreates the file again and again, but we need it to append 
# file = open("names.txt", "w")
# file = open("names.txt","a")
#instead of file.close we can write the open like this so that it automatically opens and closes the file each time
with open("names.txt","a") as file:
    #it wrote names back to back without any kind of spacing
    #file.write(name)
    file.write(f"{name}\n")

#It is better to not use close, in case in times you might forget and it will ruin the file
# file.close()