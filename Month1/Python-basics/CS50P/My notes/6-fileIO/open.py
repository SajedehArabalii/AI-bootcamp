# with open("names.txt") as file:
#     lines = file.readlines()

# for line in lines:
#     #.rstrip gets rid of all the \n in the file itself so that only the \n of the print remains
#     # we can also write end="" in file
#     print(f"Hello, {line.rstrip()}")





# with open("names.txt","r") as file:
#     for line in file:
#         print(f"Hello, {line.rstrip()}")





# Another version of getting a sorted file
# with open("names.txt") as file:
#     for line in sorted(file):
#         print("Hello,", line.rstrip())





#1-for sorting the names we need to first enter them into the list
names = []
    
with open("names.txt") as file:# No need to put "r" because it is the default
    for line in file:
        names.append(line.rstrip())

#2- print the sorted version of the list
#We can reverse it by:
#for name in sorted(names, reverse=True)
for name in sorted(names):
    print(f"Hello, {name}")